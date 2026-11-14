# CAT-Prep: High-Recall CAT Exam Preparation & PYQ Synthesis Pipeline

> **Start Here — Student Study Roadmap, Concept Examples & Interactive Practice Papers**:
> - [**Master CAT Study Roadmap, Learning Loop & Diagnostic Flow (`insights/CAT_Study_Roadmap_and_Flow.md`)**](insights/CAT_Study_Roadmap_and_Flow.md) — Complete 4-step topic learning loop, ROI-ordered module sequence across QA/DILR/VARC, 3-track study plans (16-week / 8-week / 30-day), daily study block blueprints, and a post-mock diagnostic decision tree.
> - [**Interactive Study Tracker & Post-Mock Error Log (`insights/Study_Tracker_and_Error_Log.md`)**](insights/Study_Tracker_and_Error_Log.md) — Checkable 4-step progress tracker across all 20 modules, 9 official CAT 2025 practice papers, and mistake remediation logs.
> - [**Intuitive Concept Examples Banks (`QA` | `DILR` | `VARC`)**](insights/quant_concept_examples/README.md):
>   - [**Quant Concept Examples (`insights/quant_concept_examples/`)**](insights/quant_concept_examples/README.md) — Plain-English intuition, clean-number general examples, and two-way walkthroughs (Formula vs. Ratio Intuition) across all 10 QA modules.
>   - [**DILR Concept & Grid-Evolution Examples (`insights/dilr_concept_examples/`)**](insights/dilr_concept_examples/README.md) — Step-by-step table evolution from `Empty Grid -> Clue 1 -> Clue 2 -> Final Grid` across all 6 DILR modules.
>   - [**VARC Concept & Elimination Examples (`insights/varc_concept_examples/`)**](insights/varc_concept_examples/README.md) — Bite-sized 1-paragraph mini-passages and sentence sets across all 4 VARC modules.
> - [**Official CAT 2025 Interactive Practice Papers (`practice_papers/cat_2025/`)**](practice_papers/cat_2025/README.md) — All 9 official CAT 2025 sectional papers (Slots 1, 2, 3 $\times$ VARC, DILR, QA = 204 questions) with spoiler-free collapsible hints and dual-method solutions, paired with clean PDFs in [`docs/pyqs/2025/`](docs/pyqs/2025/).

End-to-end, zero-loss extraction and synthesis pipeline that transforms **CAT Past Year Papers (PYQs)** and syllabus documents into **100%-coverage, high-recall study notes, pattern-recognition triggers, mistake taxonomies, and rapid-revision assets** across **Quantitative Ability (QA)**, **Data Interpretation & Logical Reasoning (DILR)**, and **Verbal Ability & Reading Comprehension (VARC)**.

---

## Key Capabilities

1. **Multimodal & Layout-Preserving PDF Extraction (`scripts/extract_pdf.py`)**
   - Uses **PyMuPDF (`fitz`) + `pymupdf4llm`** to extract layout-aware Markdown with tables preserved while rendering **200-DPI PNG page images** so mathematical notation, geometry figures, and DI charts are captured with zero loss.
   - Automatically flags pages containing embedded images or vector drawings (`[VISUAL_DIAGRAM_OR_CHART_PRESENT - INSPECT IMAGE]`) and emits a JSON page manifest.
2. **100% Canonical CAT Syllabus Taxonomy (`docs/syllabus/canonical_taxonomy.md`)**
   - Complete canonical blueprint across QA (Arithmetic, Algebra, Geometry & Mensuration, Number System, Modern Math), DILR (Quantitative DI, Arrangements/Grids, Games & Tournaments, 3/4-Set Venn Optimization, Networks/Flows, Algorithmic Puzzles), and VARC (RC Genre Playbooks, 7 Deadly Distractor Traps, VA TITA/MCQ Frameworks).
3. **Structured Study Roadmap, Intuitive Concept Examples & Interactive Practice Papers**
   - Guides students through a 4-step loop: **Step 1 — Intuition** (`insights/{quant,dilr,varc}_concept_examples/`), **Step 2 — Speed Triggers** (`insights/topic_summaries/`), **Step 3 — Trap Inoculation** (`insights/mistakes_and_edge_cases/`), and **Step 4 — High-Recall Drills & Practice Papers** (`insights/high_recall/active_recall_drills/` and `practice_papers/cat_2025/`).
4. **40-Minute Sectional Execution & Self-Audit Checklist (`insights/CAT_Self_Audit_Checklist.md`)**
   - Ready-to-use exam-hall timing blueprints, DILR 4-minute set-selection & 6-minute bail-out rules, VARC 2-option tie-breaker checklist, and QA A-B-C round strategy + domain/boundary checks.
5. **High-Recall Cognitive Design**
   - Structured around `IF YOU SEE [Trigger] -> THINK [Shortcut/Method]` tables, dual-method solutions (First-Principles vs. 30-Second Exam-Hall Shortcut), boundary/trap callouts, and spaced-repetition flashcards.

---

## Repository Structure

```text
CAT-Prep/
├── execution_plan.md                      # Complete 5-pass pipeline execution blueprint
├── requirements.txt                       # Python dependencies (PyMuPDF, pymupdf4llm, Pillow, pytest)
├── docs/
│   ├── pyqs/
│   │   └── 2025/                          # 9 cleanly named CAT 2025 PDFs (CAT_2025_Slot_{1,2,3}_{VARC,DILR,QA}.pdf)
│   └── syllabus/
│       └── canonical_taxonomy.md          # Complete Canonical CAT Syllabus Taxonomy (QA, DILR, VARC)
├── practice_papers/
│   └── cat_2025/                          # 9 interactive spoiler-free CAT 2025 papers (collapsible hints + solutions)
├── extractions/
│   ├── markdown/                          # Extracted layout-aware Markdown & JSON manifests
│   ├── page_images/                       # Rendered 200-DPI page PNGs per paper
│   └── structured_pyqs/                   # Pass 1 question-level JSON inventories + delta triage flags
├── insights/
│   ├── CAT_Study_Roadmap_and_Flow.md      # Master student study roadmap, 4-step learning loop & mock diagnostic tree
│   ├── Study_Tracker_and_Error_Log.md     # Interactive 20-module progress checklist & post-mock error log
│   ├── CAT_Self_Audit_Checklist.md        # 40-minute sectional strategy & pre-lock audit checklist
│   ├── coverage_matrix.md                 # Pass 2 canonical syllabus coverage & PYQ frequency matrix
│   ├── quant_concept_examples/            # Intuitive plain-English QA concept & formula general examples (10 modules + index)
│   ├── dilr_concept_examples/             # Step-by-step DILR grid evolution & invariant examples (6 modules + index)
│   ├── varc_concept_examples/             # Bite-sized 1-paragraph VARC reading & elimination examples (4 modules + index)
│   ├── topic_summaries/
│   │   ├── quant/                         # Pass 3A QA master notes + newly surfaced CAT 2025 triggers (10 modules)
│   │   ├── dilr/                          # Pass 3B DILR playbooks + newly surfaced CAT 2025 triggers (6 modules)
│   │   └── varc/                          # Pass 3C VARC playbooks + newly surfaced CAT 2025 triggers (4 modules)
│   ├── mistakes_and_edge_cases/           # Pass 4 sectional trap & pitfall compendiums + real PYQ triggers
│   └── high_recall/
│       ├── cheat_sheets/                  # Pass 5 ultra-dense last-mile revision sheets (QA, DILR, VARC)
│       ├── anki_flashcards.csv            # Pass 5 spaced-repetition flashcard deck (162 cards)
│       └── active_recall_drills/          # Speed math playbook + QA/DILR/VARC timed recognition drills (4 modules)
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
