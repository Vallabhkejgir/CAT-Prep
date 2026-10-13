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


def test_master_notes_and_high_recall_assets_completeness() -> None:
    """Verify all 28 high-recall study notes, mistake manuals, cheat sheets, and flashcards exist."""
    import csv

    expected_quant = [
        "01_arithmetic_percentages_pl_sici.md",
        "02_arithmetic_ratios_averages_mixtures_alligations.md",
        "03_arithmetic_time_work_tsd_races_circular_tracks.md",
        "04_algebra_equations_polynomials_inequalities_modulus.md",
        "05_algebra_functions_graphs_logs_surds.md",
        "06_algebra_sequences_series_maxima_minima.md",
        "07_geometry_triangles_circles_polygons.md",
        "08_geometry_mensuration_3d_coordinate_trig.md",
        "09_number_system_divisibility_factors_hcflcm_remainders_bases.md",
        "10_modern_math_pnc_probability_set_theory.md",
    ]
    for fname in expected_quant:
        path = REPO_ROOT / "insights" / "topic_summaries" / "quant" / fname
        assert path.is_file(), f"Missing QA note: {fname}"
        text = path.read_text(encoding="utf-8")
        assert "<details><summary>Q10:" in text, f"Missing 10 active-recall drills in {fname}"

    expected_dilr = [
        "01_set_selection_and_5min_scanning_framework.md",
        "02_quantitative_di_tables_charts_and_growth_traps.md",
        "03_arrangements_matrix_grids_and_scheduling.md",
        "04_games_and_tournaments_knockout_and_round_robin.md",
        "05_venn_diagrams_and_4set_maxima_minima.md",
        "06_networks_routes_flows_and_quant_lr_puzzles.md",
    ]
    for fname in expected_dilr:
        path = REPO_ROOT / "insights" / "topic_summaries" / "dilr" / fname
        assert path.is_file(), f"Missing DILR playbook: {fname}"

    expected_varc = [
        "01_rc_reading_architecture_and_genre_guides.md",
        "02_rc_question_types_and_7_distractor_traps.md",
        "03_va_parajumbles_and_odd_one_out_tita_mastery.md",
        "04_va_parasummary_and_sentence_placement.md",
    ]
    for fname in expected_varc:
        path = REPO_ROOT / "insights" / "topic_summaries" / "varc" / fname
        assert path.is_file(), f"Missing VARC playbook: {fname}"

    assert (REPO_ROOT / "insights" / "coverage_matrix.md").is_file()
    assert (REPO_ROOT / "insights" / "mistakes_and_edge_cases" / "quant_pitfalls.md").is_file()
    assert (REPO_ROOT / "insights" / "mistakes_and_edge_cases" / "dilr_traps.md").is_file()
    assert (REPO_ROOT / "insights" / "mistakes_and_edge_cases" / "varc_traps.md").is_file()
    assert (REPO_ROOT / "insights" / "high_recall" / "cheat_sheets" / "QA_Formula_and_Trigger_Book.md").is_file()
    assert (REPO_ROOT / "insights" / "high_recall" / "cheat_sheets" / "DILR_Archetype_Templates.md").is_file()
    assert (REPO_ROOT / "insights" / "high_recall" / "cheat_sheets" / "VARC_Elimination_and_VA_Rules.md").is_file()

    anki_csv = REPO_ROOT / "insights" / "high_recall" / "anki_flashcards.csv"
    assert anki_csv.is_file()
    with anki_csv.open(encoding="utf-8", newline="") as f:
        reader = list(csv.DictReader(f))
    assert len(reader) >= 150
    for row in reader:
        assert row["Section"] in {"QA", "DILR", "VARC"}
        assert row["Topic"]
        assert row["Front_Question_or_Cue"]
        assert row["Back_Formula_Trigger_and_Trap"]


def test_cat_2025_pyq_incremental_insight_enrichment_completeness() -> None:
    """Verify no per_paper directory exists, all 9 CAT 2025 JSONs have delta triage fields, and all 20 topic notes + 3 mistake manuals contain integrated CAT 2025 PYQ edge examples."""
    per_paper_dir = REPO_ROOT / "insights" / "per_paper"
    assert not per_paper_dir.exists(), "insights/per_paper must not exist under the Incremental Insight-Enrichment Architecture"

    expected_papers = [
        ("CAT_2025_QA_Slot_1", "QA", 22),
        ("CAT_2025_QA_Slot_2", "QA", 22),
        ("CAT_2025_QA_Slot_3", "QA", 22),
        ("CAT_2025_DILR_Slot_1", "DILR", 22),
        ("CAT_2025_DILR_Slot_2", "DILR", 22),
        ("CAT_2025_DILR_Slot_3", "DILR", 22),
        ("CAT_2025_VARC_Slot_1", "VARC", 24),
        ("CAT_2025_VARC_Slot_2", "VARC", 24),
        ("CAT_2025_VARC_Slot_3", "VARC", 24),
    ]
    required_keys = {
        "question_id",
        "section",
        "slot",
        "question_type",
        "canonical_topic",
        "canonical_subtopic",
        "difficulty",
        "exam_round_tag",
        "derived_answer",
        "answer_source",
        "verification_notes",
        "core_concept_tested",
        "mental_trigger",
        "first_principles_method",
        "speed_shortcut",
        "boundary_conditions_and_traps",
        "is_new_subtopic_or_variant",
        "is_mistake_or_trap_worthy",
        "is_edge_example",
        "target_insight_files",
    }

    total_questions = 0
    for base, section, expected_count in expected_papers:
        json_path = REPO_ROOT / "extractions" / "structured_pyqs" / f"{base}_questions.json"
        assert json_path.is_file(), f"Missing structured PYQ JSON: {json_path}"

        questions = json.loads(json_path.read_text(encoding="utf-8"))
        assert len(questions) == expected_count, f"Expected {expected_count} questions in {base}, got {len(questions)}"
        total_questions += len(questions)

        for q in questions:
            missing = required_keys - set(q.keys())
            assert not missing, f"Question {q.get('question_id')} missing keys: {missing}"
            assert q["section"] == section
            assert q["question_type"] in {"MCQ", "TITA"}
            assert q["difficulty"] in {"Easy", "Medium", "Hard"}
            assert q["exam_round_tag"] in {"Round_1_Sitter", "Round_2_Doable", "Round_3_TimeSink_Skip"}
            assert q["derived_answer"]
            assert isinstance(q["is_new_subtopic_or_variant"], bool)
            assert isinstance(q["is_mistake_or_trap_worthy"], bool)
            assert isinstance(q["is_edge_example"], bool)
            assert isinstance(q["target_insight_files"], list) and len(q["target_insight_files"]) >= 2
            for rel_target in q["target_insight_files"]:
                assert (REPO_ROOT / rel_target).is_file(), f"Target insight file missing: {rel_target}"

    assert total_questions == 204

    topic_files = list((REPO_ROOT / "insights" / "topic_summaries").rglob("*.md"))
    assert len(topic_files) == 20
    for tpath in topic_files:
        content = tpath.read_text(encoding="utf-8")
        assert "## CAT 2025 PYQ Edge Examples & Newly Surfaced Patterns" in content, f"Missing 2025 PYQ section in {tpath.name}"
        assert "CAT_2025_" in content and "CAT2025_" in content, f"Missing 2025 PYQ exemplars in {tpath.name}"

    mistake_files = [
        REPO_ROOT / "insights" / "mistakes_and_edge_cases" / "quant_pitfalls.md",
        REPO_ROOT / "insights" / "mistakes_and_edge_cases" / "dilr_traps.md",
        REPO_ROOT / "insights" / "mistakes_and_edge_cases" / "varc_traps.md",
    ]
    for mpath in mistake_files:
        content = mpath.read_text(encoding="utf-8")
        assert "## CAT 2025 Real PYQ Mistake Triggers & Edge Traps" in content, f"Missing 2025 traps section in {mpath.name}"
        assert "CAT_2025_" in content and "CAT2025_" in content, f"Missing 2025 trap citations in {mpath.name}"



