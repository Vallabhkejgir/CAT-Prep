# Execution Plan: High-Recall CAT Exam Preparation & PYQ Synthesis Pipeline

## Goal
Build an end-to-end, zero-loss extraction and synthesis pipeline that transforms CAT past year papers (PYQs) and syllabus documents into **100%-coverage, high-recall study notes, pattern-recognition triggers, mistake taxonomies, and rapid-revision assets** across **QA (Quant)**, **DILR**, and **VARC**.

---

## Why This Pipeline Architecture (Key Upgrades)

1. **Multimodal & Layout-Preserving PDF Extraction (Zero Loss on Math, Tables & Diagrams)**
   - Plain `pypdf` text extraction mangles mathematical notation ($x^2$, $\log_a b$, inequalities, roots), scrambles DILR tables, and completely drops Quant geometry figures and DI charts (bar, line, pie, radar, scatter, network graphs).
   - This pipeline uses **PyMuPDF (`fitz`) + `pymupdf4llm`** to extract Markdown-formatted tables/text **AND renders high-DPI page images** for every page containing diagrams, geometry figures, charts, or complex layouts so visual inspection complements the extracted text.
2. **Question-Level Granularity Before Synthesis**
   - Summarizing an entire 66-question paper in one pass drops ~70% of question nuances.
   - Each paper is first decomposed at the **individual question / DILR set / RC passage level**, capturing the exact concept, naive vs. optimal solution path, time-sink classification (Round 1 / Round 2 / Trap-Skip), and distractor engineering.
3. **100% Canonical CAT Syllabus Coverage Guarantee (Gap-Fill Engine)**
   - Past papers alone may under-sample certain valid CAT topics.
   - A dedicated **Coverage Audit Pass** maps every extracted PYQ against the **Complete Canonical CAT Syllabus Taxonomy**. Any sub-topic with zero or sparse PYQ occurrences is automatically populated with complete first-principles theory, formulas, standard archetypes, and edge cases so no exam topic is left uncovered.
4. **High-Recall Cognitive Design**
   - Every topic module is structured around **Active Recall & Pattern Recognition** rather than passive prose:
     - **`IF YOU SEE [Trigger] -> THINK [Shortcut/Method]`** heuristics
     - **First-Principles Formula vs. 30-Second CAT Shortcut** (option plugging, dimensional/parity check, extreme-value test)
     - **Boundary & Trap Callout Boxes** (domain restrictions, TITA vs. MCQ traps)
     - **Spaced-Repetition Flashcards (`anki_flashcards.csv`) & 1-Page Last-Mile Cheat Sheets**

---

## 1. Setup Workspace

Create the directory structure:

```bash
mkdir -p docs/syllabus docs/pyqs \
  extractions/markdown extractions/page_images extractions/structured_pyqs \
  insights/topic_summaries/quant insights/topic_summaries/dilr insights/topic_summaries/varc \
  insights/mistakes_and_edge_cases \
  insights/high_recall/cheat_sheets insights/high_recall/active_recall_drills \
  scripts tests
```

### Core Analysis & Synthesis Rules
1. **Zero-Omission Extraction**: Never skip a question, DILR set, RC passage, formula, or syllabus sub-topic. When a page contains a geometry figure, DI chart, table, or equation, inspect the corresponding rendered page image in `extractions/page_images/` alongside the Markdown text.
2. **Dual-Method Solutions**: For every Quant and DILR archetype, document both:
   - **Concept / First-Principles Method** (why it works)
   - **Exam-Hall Speed Method** (value substitution, symmetry, parity/divisibility filter, option elimination, visual ratio, or extreme-case testing)
3. **High-Recall Formatting**: Structure all topic notes using:
   - **Quick-Trigger Table**: `If the question states [X] -> Immediately check/apply [Y]`
   - **Core Formulas & Identities** (with explicit domain/validity conditions)
   - **Canonical Archetypes & Solved PYQ Exemplars**
   - **Deadly Traps & Boundary Conditions** (0, negative integers, non-integral reals, log base/argument rules, distinct vs. identical, TITA rounding/sign errors)
   - **Active-Recall Self-Test Prompts** (question on front, mental trigger + answer in collapsible `<details>` block)
4. **Complete Syllabus Coverage**: Even if a canonical CAT sub-topic appears rarely in the provided PDFs, synthesize full high-recall coverage for it so the notes serve as a self-contained master reference.

---

## 2. Canonical CAT Syllabus Taxonomy (`docs/syllabus/canonical_taxonomy.md`)

See `docs/syllabus/canonical_taxonomy.md` for the full canonical blueprint across:
- **Section 1: Quantitative Ability (QA)** — Arithmetic (~40–45%), Algebra (~30–35%), Geometry & Mensuration (~15–20%), Number System (~5–10%), Modern Math (~5–10%)
- **Section 2: Data Interpretation & Logical Reasoning (DILR)** — Quantitative & Reasoning-Based DI, Linear/Circular/2D Matrix Arrangements, Games & Tournaments, Venn Diagrams & Set Theory Optimization, Networks/Routes/Flows & Scheduling, Quant-Based LR & Algorithmic Puzzles
- **Section 3: Verbal Ability & Reading Comprehension (VARC)** — RC Passage Architecture & Genre Playbooks, RC Question Types & 7 Deadly Distractor Archetypes, VA TITA & MCQ Frameworks (Para-Jumbles, Odd-One-Out, Para-Summary, Sentence Placement)

---

## 3. Multimodal & Layout-Preserving PDF Extraction

Install extraction dependencies:
```bash
pip install -r requirements.txt
```

Run `scripts/extract_pdf.py` to extract both **structured Markdown (preserving tables)** and **200-DPI page images (preserving geometry figures, DI charts, and math notation)**:
```bash
python scripts/extract_pdf.py
```

---

## 4. 5-Pass Incremental Insight-Enrichment Pipeline

Execute these passes in order whenever new CAT PYQ papers are added. Instead of generating redundant `per_paper` markdown summaries, every newly extracted PYQ paper directly enriches the canonical topic master notes, mistake & trap manuals, and high-recall revision assets in place.

### Pass 1: Multimodal Extraction & Delta Triage (`extractions/structured_pyqs/<PAPER>_questions.json`)
For every extracted paper `<PAPER>` in `extractions/markdown/`:

1. `extractions/structured_pyqs/<PAPER>_questions.json` — a complete question-level inventory of EVERY question/set in the paper with autonomous dual-method answer derivation and **Insight-Enrichment Delta Triage**:
   - `question_id`, `section` (`QA|DILR|VARC`), `slot`, `question_type` (`MCQ|TITA`)
   - `canonical_topic` & `canonical_subtopic` (mapped to `docs/syllabus/canonical_taxonomy.md`)
   - `difficulty` (`Easy|Medium|Hard`) & `exam_round_tag` (`Round_1_Sitter | Round_2_Doable | Round_3_TimeSink_Skip`)
   - `derived_answer`, `answer_source`, `verification_notes` (dual-method cross-checked solution)
   - `core_concept_tested`
   - `mental_trigger` (`When you see ... -> Immediately do ...`)
   - `first_principles_method` vs `speed_shortcut`
   - `boundary_conditions_and_traps` (domain limits, TITA trap, distractor design)
   - **Insight-Enrichment Delta Fields**:
     - `is_new_subtopic_or_variant` (`bool`): `True` if the question tests a sub-topic, cross-topic hybrid, or angle not yet explicitly covered in `insights/topic_summaries/`.
     - `is_mistake_or_trap_worthy` (`bool`): `True` if the question contains a high-probability exam-hall mistake, domain restriction trap, TITA rounding/sign trap, DILR constraint trap, or VARC 2-option tie-breaker trap.
     - `is_edge_example` (`bool`): `True` if the question is a high-yield boundary/edge exemplar that must be embedded directly into the corresponding topic master note.
     - `target_insight_files` (`list[str]`): Exact repo-relative paths in `insights/topic_summaries/` and `insights/mistakes_and_edge_cases/` that this question enriches.

### Pass 2: Syllabus Coverage & Gap-Fill Audit (`insights/coverage_matrix.md`)
Compare `docs/syllabus/canonical_taxonomy.md` against all files in `extractions/structured_pyqs/` to update `insights/coverage_matrix.md` containing:
1. A complete table of every Canonical Topic & Sub-Topic across QA, DILR, and VARC.
2. Exact PYQ frequency count and question IDs mapped to each sub-topic.
3. Priority Tier (Tier 1 High-Yield, Tier 2 Medium-Yield, Tier 3 Rare-but-Tested).
4. Newly discovered sub-topic variants and explicit `[GAP_FILL_REQUIRED]` / `[GAP_FILLED]` markers on any sub-topic with `< 3` PYQ instances so Pass 3 maintains 100% syllabus coverage.

### Pass 3: In-Place Enrichment of Topic Master Notes (`insights/topic_summaries/{quant,dilr,varc}/`)
Instead of creating separate per-paper markdown files, directly enrich the 20 modular topic master notes in place using questions flagged with `is_new_subtopic_or_variant` or `is_edge_example`:
- Add any newly surfaced sub-topics, cross-topic hybrid variants, and `IF YOU SEE [Trigger] -> THINK [Shortcut]` rows.
- Maintain a dedicated **`## CAT 2025 PYQ Edge Examples & Newly Surfaced Patterns`** section in each of the 20 topic modules containing actual solved PYQ edge examples (with question ID, problem statement/set structure, First-Principles derivation, 30-Second Exam-Hall Shortcut, and Trap Alert).

#### 3A. Quantitative Ability Master Notes (`insights/topic_summaries/quant/`)
- `01_arithmetic_percentages_pl_sici.md`
- `02_arithmetic_ratios_averages_mixtures_alligations.md`
- `03_arithmetic_time_work_tsd_races_circular_tracks.md`
- `04_algebra_equations_polynomials_inequalities_modulus.md`
- `05_algebra_functions_graphs_logs_surds.md`
- `06_algebra_sequences_series_maxima_minima.md`
- `07_geometry_triangles_circles_polygons.md`
- `08_geometry_mensuration_3d_coordinate_trig.md`
- `09_number_system_divisibility_factors_hcflcm_remainders_bases.md`
- `10_modern_math_pnc_probability_set_theory.md`

#### 3B. DILR Archetype & Set-Cracking Playbooks (`insights/topic_summaries/dilr/`)
- `01_set_selection_and_5min_scanning_framework.md`
- `02_quantitative_di_tables_charts_and_growth_traps.md`
- `03_arrangements_matrix_grids_and_scheduling.md`
- `04_games_and_tournaments_knockout_and_round_robin.md`
- `05_venn_diagrams_and_4set_maxima_minima.md`
- `06_networks_routes_flows_and_quant_lr_puzzles.md`

#### 3C. VARC Strategy & Elimination Playbooks (`insights/topic_summaries/varc/`)
- `01_rc_reading_architecture_and_genre_guides.md`
- `02_rc_question_types_and_7_distractor_traps.md`
- `03_va_parajumbles_and_odd_one_out_tita_mastery.md`
- `04_va_parasummary_and_sentence_placement.md`

### Pass 4: In-Place Enrichment of Sectional Mistake & Trap Manuals (`insights/mistakes_and_edge_cases/`)
Using all questions flagged with `is_mistake_or_trap_worthy`, enrich the sectional mistake manuals in place with a dedicated **`## CAT 2025 Real PYQ Mistake Triggers & Edge Traps`** section citing the exact PYQ question IDs, naive trap answers, and prevention rules:
1. `insights/mistakes_and_edge_cases/quant_pitfalls.md` — Complete catalogue of algebraic/geometric/number-theory domain traps, non-unique case omissions, and TITA traps.
2. `insights/mistakes_and_edge_cases/dilr_traps.md` — Complete catalogue of constraint misinterpretations (`must be` vs `can be`, `only` placement, hidden zero/empty cases, unstated uniqueness assumptions).
3. `insights/mistakes_and_edge_cases/varc_traps.md` — Complete catalogue of option-elimination traps, scope creeps, extreme qualifiers, and TITA para-jumble ordering illusions.

### Pass 5: High-Recall Cheat Sheets & Flashcard Sync (`insights/high_recall/`)
Propagate newly discovered pattern triggers and edge traps into the last-mile rapid-revision assets:
1. `insights/high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md` — Ultra-dense rapid-revision compendium of every CAT Quant formula, shortcut, Pythagorean/number triplet, fraction-percentage table, and `See X -> Do Y` trigger.
2. `insights/high_recall/cheat_sheets/DILR_Archetype_Templates.md` — 1-page-per-archetype scratchpad templates, equations, and set-selection checklist.
3. `insights/high_recall/cheat_sheets/VARC_Elimination_and_VA_Rules.md` — Rapid checklist for RC option elimination and VA TITA solving.
4. `insights/high_recall/anki_flashcards.csv` — Spaced-repetition CSV (`Section,Topic,Front_Question_or_Cue,Back_Formula_Trigger_and_Trap`) ready for direct import into Anki/RemNote/Quizlet for daily active recall.
5. `insights/CAT_Self_Audit_Checklist.md` — The 40-minute per-section exam-hall execution & pre-submission double-check protocol.
