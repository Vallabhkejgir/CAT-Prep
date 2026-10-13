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
│   └── structured_pyqs/                   # Pass 1 question-level JSON inventories + delta triage flags
├── insights/
│   ├── CAT_Self_Audit_Checklist.md        # 40-minute sectional strategy & pre-lock audit checklist
│   ├── coverage_matrix.md                 # Pass 2 canonical syllabus coverage & PYQ frequency matrix
│   ├── topic_summaries/
│   │   ├── quant/                         # Pass 3A QA master notes + embedded PYQ edge examples (10 modules)
│   │   ├── dilr/                          # Pass 3B DILR playbooks + embedded PYQ sets (6 modules)
│   │   └── varc/                          # Pass 3C VARC playbooks + embedded PYQ passages/VA (4 modules)
│   ├── mistakes_and_edge_cases/           # Pass 4 sectional trap & pitfall compendiums + real PYQ triggers
│   └── high_recall/
│       ├── cheat_sheets/                  # Pass 5 ultra-dense last-mile revision sheets
│       ├── anki_flashcards.csv            # Pass 5 spaced-repetition flashcard deck
│       └── active_recall_drills/          # Pass 5 active-recall prompts & drills
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

## 5-Pass Incremental Insight-Enrichment Workflow

See [`execution_plan.md`](execution_plan.md) for the complete architecture and step-by-step instructions. Instead of maintaining separate `per_paper` summary files, each newly extracted PYQ paper directly enriches the canonical topic master notes, mistake manuals, and rapid-revision assets in place:

- **Pass 1 — Multimodal Extraction & Delta Triage**: Decomposes each extracted paper into `extractions/structured_pyqs/<PAPER>_questions.json` with dual-method answer verification (`derived_answer`, `answer_source`, `verification_notes`) and delta triage flags (`is_new_subtopic_or_variant`, `is_mistake_or_trap_worthy`, `is_edge_example`, `target_insight_files`).
- **Pass 2 — Syllabus Coverage & Gap-Fill Audit**: Audits extracted PYQs against `docs/syllabus/canonical_taxonomy.md` to update `insights/coverage_matrix.md`, map question IDs to sub-topics, and flag newly discovered variants or `< 3` occurrence sub-topics.
- **Pass 3 — In-Place Enrichment of Topic Master Notes**: Updates all 20 modular master note files across `insights/topic_summaries/{quant,dilr,varc}/` with newly surfaced sub-topics, pattern triggers, and solved PYQ edge examples.
- **Pass 4 — In-Place Enrichment of Sectional Mistake & Trap Manuals**: Updates `quant_pitfalls.md`, `dilr_traps.md`, and `varc_traps.md` under `insights/mistakes_and_edge_cases/` with real PYQ mistake triggers, boundary traps, and distractor tie-breakers.
- **Pass 5 — High-Recall Cheat Sheets & Flashcard Sync**: Propagates new triggers and edge traps into `insights/high_recall/cheat_sheets/*.md` and `insights/high_recall/anki_flashcards.csv`.
