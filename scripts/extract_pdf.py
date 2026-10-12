"""Multimodal & Layout-Preserving PDF Extractor for CAT PYQs and Syllabus Documents.

Uses PyMuPDF (fitz) + pymupdf4llm (with graceful fallback to PyMuPDF text extraction
if pymupdf4llm is not installed) to extract layout-aware Markdown and render 200-DPI
PNG page images so geometry figures, DI charts, tables, and mathematical notation
are preserved without loss.
"""

import glob
import json
import os
from typing import Dict, List, Optional

import fitz  # PyMuPDF

try:
    import pymupdf4llm  # type: ignore

    HAS_PYMUPDF4LLM = True
except ImportError:
    pymupdf4llm = None  # type: ignore
    HAS_PYMUPDF4LLM = False


def _extract_markdown_pages(pdf_path: str, doc: fitz.Document) -> List[Dict[str, str]]:
    """Extract per-page markdown using pymupdf4llm when available, with fitz fallback."""
    if HAS_PYMUPDF4LLM and pymupdf4llm is not None:
        try:
            chunks = pymupdf4llm.to_markdown(pdf_path, page_chunks=True)
            if isinstance(chunks, list) and len(chunks) == len(doc):
                return [
                    {"text": str(chunk.get("text", ""))}
                    for chunk in chunks
                ]
        except Exception:
            pass

    return [{"text": page.get_text("text")} for page in doc]


def extract_pdf_multimodal(
    pdf_path: str,
    md_dir: str = "extractions/markdown",
    img_dir: str = "extractions/page_images",
    dpi: int = 200,
) -> Dict[str, object]:
    """Extract layout-aware Markdown, 200-DPI page PNGs, and a JSON manifest for a PDF."""
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    os.makedirs(md_dir, exist_ok=True)
    paper_img_dir = os.path.join(img_dir, base_name)
    os.makedirs(paper_img_dir, exist_ok=True)

    doc = fitz.open(pdf_path)
    try:
        md_pages = _extract_markdown_pages(pdf_path, doc)
        combined_md = [f"# Document: {base_name}\nTotal Pages: {len(doc)}\n"]
        manifest: Dict[str, object] = {
            "document": base_name,
            "source_pdf": pdf_path,
            "extractor": "pymupdf4llm+fitz" if HAS_PYMUPDF4LLM else "fitz",
            "pages": [],
        }
        pages_list: List[Dict[str, object]] = []

        for idx, page in enumerate(doc):
            page_num = idx + 1
            page_md = (
                md_pages[idx]["text"]
                if idx < len(md_pages)
                else page.get_text("text")
            )

            has_images = len(page.get_images(full=True)) > 0
            has_drawings = len(page.get_drawings()) > 10
            img_path = os.path.join(paper_img_dir, f"page_{page_num:03d}.png")

            pix = page.get_pixmap(dpi=dpi)
            pix.save(img_path)

            visual_flag = (
                " [VISUAL_DIAGRAM_OR_CHART_PRESENT - INSPECT IMAGE]"
                if (has_images or has_drawings)
                else ""
            )
            combined_md.append(
                f"\n\n---\n## Page {page_num}{visual_flag}\n"
                f"- **Page Image**: `{img_path}`\n\n"
                f"{page_md}"
            )

            pages_list.append(
                {
                    "page": page_num,
                    "image_path": img_path,
                    "has_visuals": has_images or has_drawings,
                    "char_count": len(page_md),
                }
            )

        manifest["pages"] = pages_list
        num_pages = len(doc)
    finally:
        doc.close()

    out_md_path = os.path.join(md_dir, f"{base_name}.md")
    with open(out_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(combined_md))

    manifest_path = os.path.join(md_dir, f"{base_name}_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"Extracted: {out_md_path} ({num_pages} pages, images in {paper_img_dir})")
    return manifest


def batch_extract(
    docs_root: str = "docs",
    md_dir: str = "extractions/markdown",
    img_dir: str = "extractions/page_images",
) -> List[Dict[str, object]]:
    """Extract all PDFs found recursively under docs_root."""
    pattern = os.path.join(docs_root, "**", "*.pdf")
    pdf_files = sorted(glob.glob(pattern, recursive=True))
    if not pdf_files:
        print(
            f"No PDFs found in {docs_root}/. "
            "Place syllabus PDFs in docs/syllabus/ and PYQ PDFs in docs/pyqs/."
        )
        return []

    results: List[Dict[str, object]] = []
    for pdf in pdf_files:
        results.append(extract_pdf_multimodal(pdf, md_dir=md_dir, img_dir=img_dir))
    return results


if __name__ == "__main__":
    batch_extract()
