"""Unit and smoke tests for scripts/extract_pdf.py."""

import json
import os
import sys
from pathlib import Path

import fitz  # PyMuPDF

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.extract_pdf import batch_extract, extract_pdf_multimodal  # noqa: E402


def _create_sample_cat_pdf(pdf_path: Path) -> None:
    """Create a 2-page synthetic CAT PYQ PDF with text and vector drawings."""
    doc = fitz.open()

    # Page 1: Quant problem with text
    page1 = doc.new_page(width=595, height=842)
    page1.insert_text(
        (72, 72),
        "CAT Sample PYQ - Section 1: Quantitative Ability\n"
        "Q1 (TITA): Find the number of positive integral solutions to x + y + z = 12.",
        fontsize=12,
    )

    # Page 2: Geometry problem with vector drawings (>10 drawing operations)
    page2 = doc.new_page(width=595, height=842)
    page2.insert_text(
        (72, 72),
        "Q2 (MCQ): In triangle ABC inscribed in a circle, find the area ratio.",
        fontsize=12,
    )
    for i in range(12):
        rect = fitz.Rect(80 + i * 10, 120 + i * 5, 140 + i * 10, 180 + i * 5)
        page2.draw_rect(rect, color=(0, 0, 0), width=1)

    doc.save(str(pdf_path))
    doc.close()


def test_extract_pdf_multimodal_creates_markdown_images_and_manifest(tmp_path: Path) -> None:
    sample_pdf = tmp_path / "cat_2024_slot1_sample.pdf"
    _create_sample_cat_pdf(sample_pdf)

    md_dir = tmp_path / "extractions" / "markdown"
    img_dir = tmp_path / "extractions" / "page_images"

    manifest = extract_pdf_multimodal(
        str(sample_pdf),
        md_dir=str(md_dir),
        img_dir=str(img_dir),
        dpi=100,
    )

    expected_md = md_dir / "cat_2024_slot1_sample.md"
    expected_manifest = md_dir / "cat_2024_slot1_sample_manifest.json"
    expected_p1_img = img_dir / "cat_2024_slot1_sample" / "page_001.png"
    expected_p2_img = img_dir / "cat_2024_slot1_sample" / "page_002.png"

    assert expected_md.is_file()
    assert expected_manifest.is_file()
    assert expected_p1_img.is_file()
    assert expected_p2_img.is_file()

    md_text = expected_md.read_text(encoding="utf-8")
    assert "# Document: cat_2024_slot1_sample" in md_text
    assert "## Page 1" in md_text
    assert "## Page 2 [VISUAL_DIAGRAM_OR_CHART_PRESENT - INSPECT IMAGE]" in md_text
    assert "Quantitative Ability" in md_text

    saved_manifest = json.loads(expected_manifest.read_text(encoding="utf-8"))
    assert saved_manifest["document"] == "cat_2024_slot1_sample"
    assert len(saved_manifest["pages"]) == 2
    assert saved_manifest["pages"][0]["page"] == 1
    assert saved_manifest["pages"][0]["has_visuals"] is False
    assert saved_manifest["pages"][1]["page"] == 2
    assert saved_manifest["pages"][1]["has_visuals"] is True
    assert manifest == saved_manifest


def test_batch_extract_processes_docs_directory(tmp_path: Path) -> None:
    docs_dir = tmp_path / "docs" / "pyqs"
    docs_dir.mkdir(parents=True)
    sample_pdf = docs_dir / "sample_paper.pdf"
    _create_sample_cat_pdf(sample_pdf)

    md_dir = tmp_path / "extractions" / "markdown"
    img_dir = tmp_path / "extractions" / "page_images"

    results = batch_extract(
        docs_root=str(tmp_path / "docs"),
        md_dir=str(md_dir),
        img_dir=str(img_dir),
    )
    assert len(results) == 1
    assert (md_dir / "sample_paper.md").is_file()
    assert os.path.isfile(img_dir / "sample_paper" / "page_001.png")
