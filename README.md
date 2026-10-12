# CAT-Prep: High-Recall CAT Exam Preparation & PYQ Synthesis Pipeline

End-to-end, zero-loss extraction and synthesis pipeline that transforms **CAT Past Year Papers (PYQs)** and syllabus documents into **100%-coverage, high-recall study notes, pattern-recognition triggers, mistake taxonomies, and rapid-revision assets** across **Quantitative Ability (QA)**, **Data Interpretation & Logical Reasoning (DILR)**, and **Verbal Ability & Reading Comprehension (VARC)**.

---

## Key Capabilities

1. **Multimodal & Layout-Preserving PDF Extraction (`scripts/extract_pdf.py`)**
   - Uses **PyMuPDF (`fitz`) + `pymupdf4llm`** to extract layout-aware Markdown with tables preserved while rendering **200-DPI PNG page images** so mathematical notation, geometry figures, and DI charts are captured with zero loss.
   - Automatically flags pages containing embedded images or vector drawings (`[VISUAL_DIAGRAM_OR_CHART_PRESENT - INSPECT IMAGE]`) and emits a JSON page manifest.
2. **100% Canonical CAT Syllabus Taxonomy (`docs/syllabus/canonical_taxonomy.md`)**
   - Complete canonical blueprint across QA (Arithmetic, Algebra, Geometry & Mensuration, Number System, Modern Math), DILR (Quantitative DI, Arrangements/Grids, Games & Tournaments, 3/4-Set Venn Optimization, Networks/Flows, Algorithmic Puzzles), and VARC (RC Genre Playbooks, 7 Deadly Distractor Traps, VA TITA/MCQ Frameworks).
3. **40-Minute Sectional Execution & Self-Audit Checklist (`insights/CAT_Self_Audit_Checklist.md`)**
   - Ready-to-use exam-hall timing blueprints, DILR 4-minute set-selection & 6-minute bail-out rules, VARC 2-option tie-breaker checklist, and QA A-B-C round strategy + domain/boundary checks.
4. **High-Recall Cognitive Design**
   - Structured around `IF YOU SEE [Trigger] -> THINK [Shortcut/Method]` tables, dual-method solutions (First-Principles vs. 30-Second Exam-Hall Shortcut), boundary/trap callouts, and spaced-repetition flashcards.

---

## Repository Structure

```text
CAT-Prep/
├── execution_plan.md                      # Complete 5-pass pipeline execution blueprint
├── requirements.txt                       # Python dependencies (PyMuPDF, pymupdf4llm, Pillow, pytest)
├── docs/
│   ├── pyqs/                              # Drop CAT Past Year Paper PDFs here
│   └── syllabus/
│       └── canonical_taxonomy.md          # Complete Canonical CAT Syllabus Taxonomy (QA, DILR, VARC)
├── extractions/
│   ├── markdown/                          # Extracted layout-aware Markdown & JSON manifests
│   ├── page_images/                       # Rendered 200-DPI page PNGs per paper
│   └── structured_pyqs/                   # Pass 1 question-level JSON inventories
├── insights/
│   ├── CAT_Self_Audit_Checklist.md        # 40-minute sectional strategy & pre-lock audit checklist
│   ├── per_paper/                         # Pass 1 human-readable paper breakdowns
│   ├── topic_summaries/
│   │   ├── quant/                         # Pass 3A QA high-recall master notes (10 modules)
│   │   ├── dilr/                          # Pass 3B DILR archetype playbooks (6 modules)
│   │   └── varc/                          # Pass 3C VARC reading & elimination playbooks (4 modules)
│   ├── mistakes_and_edge_cases/           # Pass 4 sectional trap & pitfall compendiums
│   └── high_recall/
│       ├── cheat_sheets/                  # Pass 5 ultra-dense last-mile revision sheets
│       └── active_recall_drills/          # Pass 5 active-recall prompts & flashcard decks
├── scripts/
│   └── extract_pdf.py                     # Multimodal PDF -> Markdown + 200-DPI PNG extractor
└── tests/
    └── test_extract_pdf.py                # Automated smoke & unit tests for PDF extraction
```

---

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Add PYQ and Syllabus PDFs
Place CAT Past Year Paper PDFs inside `docs/pyqs/` and any additional syllabus PDFs inside `docs/syllabus/`.

### 3. Run Multimodal PDF Extraction
```bash
python scripts/extract_pdf.py
```
This populates `extractions/markdown/<paper>.md`, `extractions/markdown/<paper>_manifest.json`, and 200-DPI page renders under `extractions/page_images/<paper>/page_001.png`.

### 4. Run Tests
```bash
pytest
```

---

## 5-Pass High-Recall Synthesis Workflow

See [`execution_plan.md`](execution_plan.md) for the complete prompt templates and step-by-step instructions:

- **Pass 1 — Deep Per-Paper Question & Set Decomposition**: Decomposes each extracted paper into `extractions/structured_pyqs/<PAPER>_questions.json` and `insights/per_paper/<PAPER>_analysis.md`.
- **Pass 2 — Syllabus Coverage Audit & Gap-Fill Matrix**: Audits extracted PYQs against `docs/syllabus/canonical_taxonomy.md` to produce `insights/coverage_matrix.md` and mark `< 3` occurrence sub-topics with `[GAP_FILL_REQUIRED]`.
- **Pass 3 — High-Recall Topic Master Notes**: Generates all 20 modular master note files across `insights/topic_summaries/{quant,dilr,varc}/`.
- **Pass 4 — Sectional Mistake Patterns & Edge-Case Compendium**: Synthesizes `quant_pitfalls.md`, `dilr_traps.md`, and `varc_traps.md` under `insights/mistakes_and_edge_cases/`.
- **Pass 5 — High-Recall Revision Assets & Pre-Submission Audit**: Produces rapid cheat sheets, `anki_flashcards.csv`, and `insights/CAT_Self_Audit_Checklist.md`.
