# CAT Preparation Master Study Roadmap, Learning Loop & Diagnostic Flow

> **Quick Links**: [Repository Home (`README.md`)](../README.md) | [Study Tracker & Error Log (`Study_Tracker_and_Error_Log.md`)](./Study_Tracker_and_Error_Log.md) | [Quant Examples (`quant_concept_examples/`)](./quant_concept_examples/README.md) | [DILR Examples (`dilr_concept_examples/`)](./dilr_concept_examples/README.md) | [VARC Examples (`varc_concept_examples/`)](./varc_concept_examples/README.md) | [CAT 2025 Practice Papers (`../practice_papers/cat_2025/`)](../practice_papers/cat_2025/README.md) | [Active-Recall Drills (`high_recall/active_recall_drills/`)](./high_recall/active_recall_drills/README.md) | [Self-Audit Checklist (`CAT_Self_Audit_Checklist.md`)](./CAT_Self_Audit_Checklist.md)

This guide provides a complete, structured roadmap for navigating the **CAT-Prep** repository—whether you are starting from scratch 4 months before the exam, breaking through an 80th-percentile mock plateau, or executing a final 30-day high-recall sprint.

---

## Flow 1: The 4-Step Learning Loop for Any Single Topic (How to Use This Repo)

Never read formula lists passively. Every topic across **QA, DILR, and VARC** in this repository is engineered around a **4-step active learning loop** that moves you from *plain-English intuition* $\to$ *pattern recognition* $\to$ *trap immunity* $\to$ *timed execution & retention*.

```mermaid
flowchart LR
    S1["<b>Step 1: Build Intuition</b><br/><code>quant_concept_examples/</code><br/><code>dilr_concept_examples/</code><br/><code>varc_concept_examples/</code><br/>Plain-English meaning +<br/>Clean single-concept example"]
    S2["<b>Step 2: Master Speed Triggers</b><br/><code>insights/topic_summaries/</code><br/><code>See X -> Do Y</code> Trigger Table +<br/>Active-Recall Prompts +<br/>CAT 2025 Variant Triggers"]
    S3["<b>Step 3: Trap Inoculation</b><br/><code>insights/mistakes_and_edge_cases/</code><br/>Domain traps, TITA pitfalls,<br/>and -1 mark distractor patterns"]
    S4["<b>Step 4: Drill & Lock Into Memory</b><br/><code>high_recall/cheat_sheets/</code> +<br/><code>active_recall_drills/</code> +<br/><code>practice_papers/cat_2025/</code> +<br/><code>anki_flashcards.csv</code>"]

    S1 --> S2 --> S3 --> S4
    S4 -.->|"Log in Study_Tracker_and_Error_Log.md"| S1
```

### Step-by-Step Execution Protocol

| Step | Folder / File to Open | What You Do (25–45 mins per step) | Readiness Gate Before Moving On |
| :--- | :--- | :--- | :--- |
| **Step 1: Build Intuition** | [`quant_concept_examples/`](./quant_concept_examples/README.md), [`dilr_concept_examples/`](./dilr_concept_examples/README.md), [`varc_concept_examples/`](./varc_concept_examples/README.md) | Read **1. Concept in Plain English** and solve **3. General Example** on scratch paper using both **Way 1 (Formula / Grid Evolution)** and **Way 2 (Ratio / Elimination Shortcut)**. | You can explain *why* the rule works and solve the clean-number/mini-passage example both ways without looking. |
| **Step 2: Master Speed Triggers** | [`insights/topic_summaries/`](./topic_summaries/) (`quant/`, `dilr/`, `varc/`) | Study **Section 2 (Pattern-Recognition Trigger Table)**, solve all **Active-Recall Drill prompts** (`<details>` tags) before clicking to reveal, and review the **Newly Surfaced CAT 2025 Triggers**. | You score $\ge 80\%$ on the Active-Recall prompts and can state the `See X -> Do Y` trigger in under 10 seconds. |
| **Step 3: Trap Inoculation** | [`quant_pitfalls.md`](./mistakes_and_edge_cases/quant_pitfalls.md), [`dilr_traps.md`](./mistakes_and_edge_cases/dilr_traps.md), [`varc_traps.md`](./mistakes_and_edge_cases/varc_traps.md) | Read the boundary conditions and classic exam traps for that module (e.g., $a = 0$ degenerate quadratics, log base $\in (0,1)$ sign-flips, CAGR $n-1$ intervals, RC `Too_Extreme` modals). | You can name the #1 trap for each concept before attempting timed sets. |
| **Step 4: Lock Into Memory & Practice** | [`cheat_sheets/`](./high_recall/cheat_sheets/), [`active_recall_drills/`](./high_recall/active_recall_drills/README.md), [`practice_papers/cat_2025/`](../practice_papers/cat_2025/README.md), [`anki_flashcards.csv`](./high_recall/anki_flashcards.csv) | Review the 1-page Cheat Sheet, complete the timed Recognition Drills, solve the official CAT 2025 papers, and check off the module in [`Study_Tracker_and_Error_Log.md`](./Study_Tracker_and_Error_Log.md). | Instant $< 5$-second recall of every trigger and identity during timed mocks. |

---

## Flow 2: Dependency & ROI-Ordered Module Sequence (Across QA, DILR, and VARC)

Do **not** study chapters in random order. In CAT, Arithmetic ratios power Quantitative DI, Quadratics/Modulus power Functions and Sequences, and 2D Triangle similarity powers 3D Mensuration. Follow the exact dependency and Return-on-Investment (ROI) chains below.

```mermaid
flowchart TD
    subgraph QA ["<b>Quantitative Ability (QA) — 4-Tier ROI & Dependency Chain</b>"]
        direction TB
        QA_T1["<b>Tier 1: Arithmetic Core (~40–45% of QA) — DO FIRST</b><br/>01 Percentages/P&L/SI-CI ➔ 02 Ratios/Averages/Mixtures ➔ 03 Time-Work/TSD/Races"]
        QA_T2["<b>Tier 2: Algebra Core (~28–32% of QA)</b><br/>04 Equations/Quadratics/Modulus ➔ 05 Functions/Logs/Surds ➔ 06 Sequences/Series/AM-GM"]
        QA_T3["<b>Tier 3: Number System & Geometry (~18–22% of QA)</b><br/>09 Number System/Remainders ➔ 07 Triangles/Circles/Polygons ➔ 08 3D Mensuration/Coord Geom"]
        QA_T4["<b>Tier 4: Modern Math & DILR Crossover (~8–10% of QA)</b><br/>10 P&C, Probability & 3-Set Inclusion-Exclusion"]
        QA_T1 --> QA_T2 --> QA_T3 --> QA_T4
    end

    subgraph DILR ["<b>Data Interpretation & Logical Reasoning (DILR) — Grid-to-Optimization Chain</b>"]
        direction TB
        D1["01 5-Min Set Selection Framework"] --> D3["03 Arrangements & Matrix Grids"]
        D3 --> D5["05 Venn Diagrams & 4-Set Min/Max"]
        D5 --> D2["02 Quantitative DI & Growth Traps<br/><i>(Unlocks after QA 01 & QA 02)</i>"]
        D2 --> D4["04 Games, Tournaments & Invariants"]
        D4 --> D6["06 Networks, Routes & Flow Optimization"]
    end

    subgraph VARC ["<b>Verbal Ability & Reading Comprehension (VARC) — Accuracy Chain</b>"]
        direction TB
        V1["01 RC Architecture & Genre Reading"] --> V2["02 RC Question Types & 7 Distractor Traps"]
        V2 --> V4["04 Para-Summary & Sentence Placement<br/><i>(Highest VA ROI — MCQ + TITA)</i>"]
        V4 --> V3["03 TITA Para-Jumbles & Odd-One-Out<br/><i>(Zero-Negative-Marking Anchors)</i>"]
    end

    QA_T1 -.->|"Feeds % & Alligation"| D2
    QA_T4 -.->|"Feeds Set Theory & Counting"| D5
```

### 2.1 Quantitative Ability (QA) Ordered Module Table

| Tier & Weightage | Order | Topic Summary File (Step 2) | Intuitive Concept Examples File (Step 1) | Why This Order? |
| :--- | :---: | :--- | :--- | :--- |
| **Tier 1: Arithmetic Core**<br/>*(~40–45% of QA; 8–10 Qs/slot)* | **1** | [`01_arithmetic_percentages_pl_sici.md`](./topic_summaries/quant/01_arithmetic_percentages_pl_sici.md) | [`01_arithmetic_percentages_pl_sici_examples.md`](./quant_concept_examples/01_arithmetic_percentages_pl_sici_examples.md) | Multiplying factors ($\text{MF} = 1 \pm \frac{p}{100}$) and base-shift fractions are the language of all Arithmetic and DI. |
| **Tier 1: Arithmetic Core** | **2** | [`02_arithmetic_ratios_averages_mixtures_alligations.md`](./topic_summaries/quant/02_arithmetic_ratios_averages_mixtures_alligations.md) | [`02_arithmetic_ratios_averages_mixtures_alligations_examples.md`](./quant_concept_examples/02_arithmetic_ratios_averages_mixtures_alligations_examples.md) | Ratio scaling and the Alligation lever rule directly speed up P&L, SI/CI, TSD, and DILR weighted tables. |
| **Tier 1: Arithmetic Core** | **3** | [`03_arithmetic_time_work_tsd_races_circular_tracks.md`](./topic_summaries/quant/03_arithmetic_time_work_tsd_races_circular_tracks.md) | [`03_arithmetic_time_work_tsd_races_circular_tracks_examples.md`](./quant_concept_examples/03_arithmetic_time_work_tsd_races_circular_tracks_examples.md) | Applies inverse proportionality ($S \propto 1/T$) and LCM scaling from QA 01–02 to Work, TSD, and Circular Tracks. |
| **Tier 2: Algebra Core**<br/>*(~28–32% of QA; 6–7 Qs/slot)* | **4** | [`04_algebra_equations_polynomials_inequalities_modulus.md`](./topic_summaries/quant/04_algebra_equations_polynomials_inequalities_modulus.md) | [`04_algebra_equations_polynomials_inequalities_modulus_examples.md`](./quant_concept_examples/04_algebra_equations_polynomials_inequalities_modulus_examples.md) | Linear Diophantine equations, Vieta's root relations, Wavy Curve, and Modulus are prerequisites for all higher Algebra. |
| **Tier 2: Algebra Core** | **5** | [`05_algebra_functions_graphs_logs_surds.md`](./topic_summaries/quant/05_algebra_functions_graphs_logs_surds.md) | [`05_algebra_functions_graphs_logs_surds_examples.md`](./quant_concept_examples/05_algebra_functions_graphs_logs_surds_examples.md) | Builds on QA 04 quadratics/inequalities to solve Log domain filters, Surd de-nesting, GIF $\lfloor x \rfloor$, and Cauchy equations. |
| **Tier 2: Algebra Core** | **6** | [`06_algebra_sequences_series_maxima_minima.md`](./topic_summaries/quant/06_algebra_sequences_series_maxima_minima.md) | [`06_algebra_sequences_series_maxima_minima_examples.md`](./quant_concept_examples/06_algebra_sequences_series_maxima_minima_examples.md) | Completes Algebra with AP/GP/AGP, telescoping series, and AM-GM / Cauchy-Schwarz optimization. |
| **Tier 3: Numbers & Geometry**<br/>*(~18–22% of QA; 4–5 Qs/slot)* | **7** | [`09_number_system_divisibility_factors_hcflcm_remainders_bases.md`](./topic_summaries/quant/09_number_system_divisibility_factors_hcflcm_remainders_bases.md) | [`09_number_system_divisibility_factors_hcflcm_remainders_examples.md`](./quant_concept_examples/09_number_system_divisibility_factors_hcflcm_remainders_examples.md) | Prime factorization, divisor counting $d(N)$, HCF/LCM models, and modular arithmetic sharpen integer TITA intuition. |
| **Tier 3: Numbers & Geometry** | **8** | [`07_geometry_triangles_circles_polygons.md`](./topic_summaries/quant/07_geometry_triangles_circles_polygons.md) | [`07_geometry_triangles_circles_polygons_examples.md`](./quant_concept_examples/07_geometry_triangles_circles_polygons_examples.md) | 2D Euclidean geometry: Pythagorean triplets, similarity, Mass Point Geometry, Circle tangents, and Trapeziums/Polygons. |
| **Tier 3: Numbers & Geometry** | **9** | [`08_geometry_mensuration_3d_coordinate_trig.md`](./topic_summaries/quant/08_geometry_mensuration_3d_coordinate_trig.md) | [`08_geometry_mensuration_3d_coordinate_trig_examples.md`](./quant_concept_examples/08_geometry_mensuration_3d_coordinate_trig_examples.md) | Extends 2D similarity and right triangles into 3D cones/spheres/frustums, Shoelace coordinates, and line reflections. |
| **Tier 4: Modern Math**<br/>*(~8–10% of QA; 2–3 Qs/slot)* | **10** | [`10_modern_math_pnc_probability_set_theory.md`](./topic_summaries/quant/10_modern_math_pnc_probability_set_theory.md) | [`10_modern_math_pnc_probability_set_theory_examples.md`](./quant_concept_examples/10_modern_math_pnc_probability_set_theory_examples.md) | Stars & Bars, Derangements, Bayes' Theorem, and 3-Set Inclusion-Exclusion (which directly overlaps with DILR 05!). |

### 2.2 DILR & VARC Ordered Module Table

| Section | Order | Topic Summary File (Step 2) | Intuitive Concept Examples File (Step 1) | High-Yield Focus & Prerequisite Link |
| :--- | :---: | :--- | :--- | :--- |
| **DILR** | **1** | [`01_set_selection_and_5min_scanning_framework.md`](./topic_summaries/dilr/01_set_selection_and_5min_scanning_framework.md) | [`01_set_selection_and_5min_scanning_examples.md`](./dilr_concept_examples/01_set_selection_and_5min_scanning_examples.md) | Master the 4-minute scanning pass, 6-minute bail-out rule, and mathematical invariants before solving sets. |
| **DILR** | **2** | [`03_arrangements_matrix_grids_and_scheduling.md`](./topic_summaries/dilr/03_arrangements_matrix_grids_and_scheduling.md) | [`03_arrangements_matrix_grids_and_scheduling_examples.md`](./dilr_concept_examples/03_arrangements_matrix_grids_and_scheduling_examples.md) | Build deterministic 2D table-grid habits, bijective row/column elimination, and modular circular seating ($\pmod N$). |
| **DILR** | **3** | [`05_venn_diagrams_and_4set_maxima_minima.md`](./topic_summaries/dilr/05_venn_diagrams_and_4set_maxima_minima.md) | [`05_venn_diagrams_and_4set_maxima_minima_examples.md`](./dilr_concept_examples/05_venn_diagrams_and_4set_maxima_minima_examples.md) | Master 3-Set and 4-Set layer equations ($E_1 + 2E_2 + 3E_3 + 4E_4$) and surplus extrema (pairs with `QA 10`). |
| **DILR** | **4** | [`02_quantitative_di_tables_charts_and_growth_traps.md`](./topic_summaries/dilr/02_quantitative_di_tables_charts_and_growth_traps.md) | [`02_quantitative_di_tables_charts_and_growth_traps_examples.md`](./dilr_concept_examples/02_quantitative_di_tables_charts_and_growth_traps_examples.md) | Apply `QA 01` & `QA 02` ratios to missing-value matrices, waterfall diffs, and index-base traps. |
| **DILR** | **5** | [`04_games_and_tournaments_knockout_and_round_robin.md`](./topic_summaries/dilr/04_games_and_tournaments_knockout_and_round_robin.md) | [`04_games_and_tournaments_knockout_and_round_robin_examples.md`](./dilr_concept_examples/04_games_and_tournaments_knockout_and_round_robin_examples.md) | Knockout match invariants ($N - 1$), Round-Robin $\binom{n}{2}$ point sums, and seeded upsets. |
| **DILR** | **6** | [`06_networks_routes_flows_and_quant_lr_puzzles.md`](./topic_summaries/dilr/06_networks_routes_flows_and_quant_lr_puzzles.md) | [`06_networks_routes_flows_and_quant_lr_puzzles_examples.md`](./dilr_concept_examples/06_networks_routes_flows_and_quant_lr_puzzles_examples.md) | Flow conservation ($\text{In} = \text{Out}$), min-cut bottlenecks, and diophantine coin/weight puzzles. |
| **VARC** | **1** | [`01_rc_reading_architecture_and_genre_guides.md`](./topic_summaries/varc/01_rc_reading_architecture_and_genre_guides.md) | [`01_rc_reading_architecture_and_genre_guides_examples.md`](./varc_concept_examples/01_rc_reading_architecture_and_genre_guides_examples.md) | 3-minute structural map (Author's Thesis + Pivot Words + Tone) across Humanities, Economics, and Science genres. |
| **VARC** | **2** | [`02_rc_question_types_and_7_distractor_traps.md`](./topic_summaries/varc/02_rc_question_types_and_7_distractor_traps.md) | [`02_rc_question_types_and_7_distractor_traps_examples.md`](./varc_concept_examples/02_rc_question_types_and_7_distractor_traps_examples.md) | Eliminate `Too_Extreme`, `Out_of_Scope`, `Causal_Inversion`, and `Half_Truth` distractors in 2-contender showdowns. |
| **VARC** | **3** | [`04_va_parasummary_and_sentence_placement.md`](./topic_summaries/varc/04_va_parasummary_and_sentence_placement.md) | [`04_va_parasummary_and_sentence_placement_examples.md`](./varc_concept_examples/04_va_parasummary_and_sentence_placement_examples.md) | Highest-accuracy VA questions: Thesis-match Para-Summary and pronoun/bridge-hook Sentence Placement. |
| **VARC** | **4** | [`03_va_parajumbles_and_odd_one_out_tita_mastery.md`](./topic_summaries/varc/03_va_parajumbles_and_odd_one_out_tita_mastery.md) | [`03_va_parajumbles_and_odd_one_out_tita_mastery_examples.md`](./varc_concept_examples/03_va_parajumbles_and_odd_one_out_tita_mastery_examples.md) | Zero-negative-marking TITA strategy: mandatory pairs (`Pronoun -> Referent`, `Contrast Pivot`) and 3-1-Outlier detection. |

---

## Flow 3: 3-Track Study Plans Based on Starting Point & Time Left

Choose the track that matches your current timeline and mock percentile, and check off completed items in [`Study_Tracker_and_Error_Log.md`](./Study_Tracker_and_Error_Log.md):

### Track A: Full Foundation Track (12–16 Weeks | Starting from Scratch or $< 70\%$ile)

| Phase | Weeks | QA Assignment (4-Step Loop) | DILR Assignment (4-Step Loop) | VARC Assignment (4-Step Loop) | Milestone Check |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Phase 1: Arithmetic & Reading Core** | **Weeks 1–4** | `QA 01`, `QA 02`, `QA 03` ([Concept Examples](./quant_concept_examples/README.md) $\to$ [Summaries](./topic_summaries/quant/)) | `DILR 01`, `DILR 03`, `DILR 02` ([Examples](./dilr_concept_examples/README.md) $\to$ [Summaries](./topic_summaries/dilr/)) | `VARC 01` + `VARC 02` ([Examples](./varc_concept_examples/README.md) $\to$ [Summaries](./topic_summaries/varc/)) | Master [`01_speed_math_and_di_calculation_playbook.md`](./high_recall/active_recall_drills/01_speed_math_and_di_calculation_playbook.md); 1 mock every 2 weeks. |
| **Phase 2: Algebra & Venn/Tournament Core** | **Weeks 5–8** | `QA 04`, `QA 05`, `QA 06` ([Concept Examples](./quant_concept_examples/README.md) $\to$ [Summaries](./topic_summaries/quant/)) | `DILR 05` (3/4-Set Venn) + `DILR 04` (Games & Tournaments) | `VARC 04` (Para-Summary & Placement) + 2 RCs/day | 1 full mock/week; log every `-1` trap in [`Study_Tracker_and_Error_Log.md`](./Study_Tracker_and_Error_Log.md). |
| **Phase 3: Numbers, Geometry & Modern Math** | **Weeks 9–12** | `QA 09`, `QA 07`, `QA 08`, `QA 10` ([Concept Examples](./quant_concept_examples/README.md) $\to$ [Summaries](./topic_summaries/quant/)) | `DILR 06` (Networks/Optimization) + [`03_dilr_5min_set_selection_drill.md`](./high_recall/active_recall_drills/03_dilr_5min_set_selection_drill.md) | `VARC 03` (TITA Para-Jumbles & Odd-One-Out) + [`04_varc_2option_tiebreaker_drill.md`](./high_recall/active_recall_drills/04_varc_2option_tiebreaker_drill.md) | Complete [`02_qa_round1_sitter_recognition_drill.md`](./high_recall/active_recall_drills/02_qa_round1_sitter_recognition_drill.md) & [`CAT_Self_Audit_Checklist.md`](./CAT_Self_Audit_Checklist.md). |
| **Phase 4: Official CAT 2025 Paper Sprint** | **Weeks 13–16** | Timed QA Slots 1–3 in [`practice_papers/cat_2025/`](../practice_papers/cat_2025/README.md) + [`QA_Formula_and_Trigger_Book.md`](./high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md) | Timed DILR Slots 1–3 in [`practice_papers/cat_2025/`](../practice_papers/cat_2025/README.md) | Timed VARC Slots 1–3 in [`practice_papers/cat_2025/`](../practice_papers/cat_2025/README.md) | 2 mocks/week + daily 15-min [`anki_flashcards.csv`](./high_recall/anki_flashcards.csv) review. |

---

### Track B: Score-Booster / Plateau Breaker Track (6–8 Weeks | Stuck at $75\text{–}90\%$ile)
*For students who already know basic formulas but run out of time in QA, pick wrong sets in DILR, or lose marks to 50-50 RC traps.*

- **Weeks 1–2 (Arithmetic Speed & DILR Selection Overhaul)**:
  - Go straight to **Way 2 (Ratio/Common-Sense Intuition)** in [`01..03_arithmetic_*_examples.md`](./quant_concept_examples/README.md) and drill [`01_speed_math_and_di_calculation_playbook.md`](./high_recall/active_recall_drills/01_speed_math_and_di_calculation_playbook.md).
  - Enforce the **4-Minute DILR Set Selection Pass** using [`03_dilr_5min_set_selection_drill.md`](./high_recall/active_recall_drills/03_dilr_5min_set_selection_drill.md) and [`DILR_Archetype_Templates.md`](./high_recall/cheat_sheets/DILR_Archetype_Templates.md).
- **Weeks 3–4 (Algebra Triggers & VARC 2-Option Tie-Breaking)**:
  - Drill value-plugging, symmetry, and Wavy Curve triggers in [`04..06_algebra_*.md`](./topic_summaries/quant/) + [`quant_pitfalls.md`](./mistakes_and_edge_cases/quant_pitfalls.md).
  - Complete [`04_varc_2option_tiebreaker_drill.md`](./high_recall/active_recall_drills/04_varc_2option_tiebreaker_drill.md) and tag the flaw on every eliminated RC option using [`varc_traps.md`](./mistakes_and_edge_cases/varc_traps.md).
- **Weeks 5–6 (Geometry, Numbers & Official CAT 2025 Slot Simulations)**:
  - Drill [`02_qa_round1_sitter_recognition_drill.md`](./high_recall/active_recall_drills/02_qa_round1_sitter_recognition_drill.md) and take all 9 papers in [`practice_papers/cat_2025/`](../practice_papers/cat_2025/README.md) (paired with the official PDFs in [`../docs/pyqs/2025/`](../docs/pyqs/2025/)) under strict 40-minute timers.
- **Weeks 7–8 (Mistake Elimination & High-Recall Lock)**:
  - Audit every weak cell in [`CAT_Self_Audit_Checklist.md`](./CAT_Self_Audit_Checklist.md) and review all 3 [`cheat_sheets/`](./high_recall/cheat_sheets/) every 48 hours.

---

### Track C: Final 30-Day High-Recall Sprint (4 Weeks Before CAT)

| Week | Primary Daily Focus | Exact Repository Files to Drill |
| :--- | :--- | :--- |
| **Week 1 (Days 1–7)** | **High-Yield Trigger & Speed Drill Sweep** | [`QA_Formula_and_Trigger_Book.md`](./high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md), [`DILR_Archetype_Templates.md`](./high_recall/cheat_sheets/DILR_Archetype_Templates.md), [`VARC_Elimination_and_VA_Rules.md`](./high_recall/cheat_sheets/VARC_Elimination_and_VA_Rules.md) + [`active_recall_drills/`](./high_recall/active_recall_drills/README.md) |
| **Week 2 (Days 8–14)** | **Pitfall Inoculation & Active Recall** | [`quant_pitfalls.md`](./mistakes_and_edge_cases/quant_pitfalls.md), [`dilr_traps.md`](./mistakes_and_edge_cases/dilr_traps.md), [`varc_traps.md`](./mistakes_and_edge_cases/varc_traps.md) + all Active-Recall prompts across `topic_summaries/` |
| **Week 3 (Days 15–21)** | **Official CAT 2025 9-Paper Simulation** | [`practice_papers/cat_2025/README.md`](../practice_papers/cat_2025/README.md) (`Slot 1, 2, 3` $\times$ `VARC, DILR, QA`) + [`coverage_matrix.md`](./coverage_matrix.md) |
| **Week 4 (Days 22–30)** | **Readiness Verification & Flashcard Lock** | [`CAT_Self_Audit_Checklist.md`](./CAT_Self_Audit_Checklist.md) + [`anki_flashcards.csv`](./high_recall/anki_flashcards.csv) + [`Study_Tracker_and_Error_Log.md`](./Study_Tracker_and_Error_Log.md) |

---

## Flow 4: Daily Balanced Study Block Blueprint (Weekday 3-Hour vs. Weekend 6-Hour)

Never spend an entire week studying only QA while letting VARC and DILR go cold—CAT rewards **daily multi-section rhythm**.

### 4.1 Weekday 3-Hour Balanced Study Block (180 Minutes)

```text
+-----------------------------------------------------------------------------------+
| BLOCK 1: VARC Daily Rhythm (45 mins)                                              |
|  - 2 Timed RC Passages (16 mins) + 4 VA Questions (8 mins)                        |
|  - 21-min Deep Post-Mortem: Tag every wrong option using varc_concept_examples/   |
|    and mistakes_and_edge_cases/varc_traps.md                                      |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| BLOCK 2: DILR Timed Set Execution (45 mins)                                       |
|  - Pick 2 sets: 3-min scan -> 15-min solve per set (enforce 6-min bail-out rule!) |
|  - 12-min Grid Audit: Rebuild the cleanest 2D table/Venn representation from      |
|    dilr_concept_examples/ and topic_summaries/dilr/ without time pressure.        |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| BLOCK 3: QA Concept + Two-Pass Sprint (75 mins)                                   |
|  - 30 mins: 1 Module slice in quant_concept_examples/ + topic_summaries/quant/    |
|  - 30 mins: 12-question timed drill using the Two-Pass Method (Pass 1: Round_1    |
|    Sitters in <90s; Pass 2: Round_2 Doables)                                      |
|  - 15 mins: Re-solve every missed/slow question using the 30-Second Speed Trigger |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| BLOCK 4: Spaced-Repetition Recall Lock (15 mins)                                  |
|  - 20 cards from insights/high_recall/anki_flashcards.csv + Cheat Sheet scan      |
+-----------------------------------------------------------------------------------+
```

### 4.2 Weekend 6-Hour Mock + Deep Diagnostic Block (360 Minutes)
1. **Hours 1–2 (120 mins)**: Full-length 2-hour CAT Mock ($40\text{ min VARC} + 40\text{ min DILR} + 40\text{ min QA}$) or a full slot from [`practice_papers/cat_2025/`](../practice_papers/cat_2025/README.md).
2. **Hours 3–5 (180 mins)**: **3-Hour Post-Mock Diagnostic Audit** using **Flow 5** below and logging every error in [`Study_Tracker_and_Error_Log.md`](./Study_Tracker_and_Error_Log.md).
3. **Hour 6 (60 mins)**: Targeted remediation in the exact files from `quant_concept_examples/`, `dilr_concept_examples/`, `varc_concept_examples/`, and `mistakes_and_edge_cases/`.

---

## Flow 5: Post-Mock Diagnostic Decision Tree ("Why Did I Lose Marks $\to$ Which File Fixes It?")

After every mock or sectional test, classify each lost mark using this decision tree to jump straight to the file that fixes the root cause:

```mermaid
flowchart TD
    Root["<b>Lost Marks or Wasted Time in Mock</b>"] --> Q1{"What went wrong?"}

    Q1 -->|"1. Blanked on concept /<br/>Didn't know how to set up grid"| Fix1["<b>Fix: Concept / Setup Intuition Gap</b><br/>Open <code>quant_concept_examples/</code>,<br/><code>dilr_concept_examples/</code>, or<br/><code>varc_concept_examples/</code><br/>Work through Step-by-Step Walkthrough"]

    Q1 -->|"2. Knew concept, but took<br/>3–5 mins of heavy algebra"| Fix2["<b>Fix: Missing Speed Trigger</b><br/>Open <code>insights/topic_summaries/</code> Section 2<br/>& <code>active_recall_drills/01..02_*.md</code><br/>Drill <code>See X -> Do Y</code> shortcut"]

    Q1 -->|"3. Solved fast, but got<br/>-1 mark (or wrong TITA)"| Fix3["<b>Fix: Domain / Edge-Case Trap</b><br/>Open <code>insights/mistakes_and_edge_cases/</code><br/>(<code>quant_pitfalls.md</code>, <code>dilr_traps.md</code>, <code>varc_traps.md</code>)<br/>Log in <code>Study_Tracker_and_Error_Log.md</code>"]

    Q1 -->|"4. Ran out of time /<br/>Got stuck on 1 hard set/Q"| Fix4["<b>Fix: Two-Pass / Set-Selection Failure</b><br/>Open <code>03_dilr_5min_set_selection_drill.md</code><br/>& <code>CAT_Self_Audit_Checklist.md</code> Section 3<br/>Enforce 90s QA skip & 6-min DILR bail-out"]
```

### Actionable Symptom-to-File Remediation Matrix

| Mock Symptom Observed | Root Cause Diagnosis | Exact Repository File(s) to Open Right Now |
| :--- | :--- | :--- |
| **QA**: Confused by faulty weights, installments, or alligation denominator units | Arithmetic setup gap | [`01_arithmetic_percentages_pl_sici_examples.md`](./quant_concept_examples/01_arithmetic_percentages_pl_sici_examples.md), [`02_arithmetic_ratios_averages_mixtures_alligations_examples.md`](./quant_concept_examples/02_arithmetic_ratios_averages_mixtures_alligations_examples.md) |
| **QA**: Circular track meeting points, shuttle runs, or escalator steps took $> 3$ mins | TSD relative motion gap | [`03_arithmetic_time_work_tsd_races_circular_tracks_examples.md`](./quant_concept_examples/03_arithmetic_time_work_tsd_races_circular_tracks_examples.md), [`03_arithmetic_time_work_tsd_races_circular_tracks.md`](./topic_summaries/quant/03_arithmetic_time_work_tsd_races_circular_tracks.md) |
| **QA**: Got $-1$ on quadratic/modulus inequality, log base, or $\lfloor x \rfloor$ equation | Domain / boundary trap ($a=0$, base $\in (0,1)$, open bracket $\sqrt{n^2+1}$) | [`quant_pitfalls.md`](./mistakes_and_edge_cases/quant_pitfalls.md) (Pitfalls 2.1–2.6), [`04_algebra_*_examples.md`](./quant_concept_examples/04_algebra_equations_polynomials_inequalities_modulus_examples.md), [`05_algebra_*_examples.md`](./quant_concept_examples/05_algebra_functions_graphs_logs_surds_examples.md) |
| **QA**: Missed telescoping sum, AP sum-to-term ratio, or AM-GM split | Missing series/max-min trigger | [`06_algebra_sequences_series_maxima_minima_examples.md`](./quant_concept_examples/06_algebra_sequences_series_maxima_minima_examples.md), [`02_qa_round1_sitter_recognition_drill.md`](./high_recall/active_recall_drills/02_qa_round1_sitter_recognition_drill.md) |
| **QA**: Stuck on triangle cevian ratios, inscribed solids, or coordinate reflection | Missing Mass Point / 2D-slice / reflection formula | [`07_geometry_triangles_circles_polygons_examples.md`](./quant_concept_examples/07_geometry_triangles_circles_polygons_examples.md), [`08_geometry_mensuration_3d_coordinate_trig_examples.md`](./quant_concept_examples/08_geometry_mensuration_3d_coordinate_trig_examples.md) |
| **QA**: Confused by remainders, trailing zeros, Stars & Bars, or 3-Set Venn extrema | Number system / P&C / Set formula gap | [`09_number_system_*_examples.md`](./quant_concept_examples/09_number_system_divisibility_factors_hcflcm_remainders_examples.md), [`10_modern_math_*_examples.md`](./quant_concept_examples/10_modern_math_pnc_probability_set_theory_examples.md) |
| **DILR**: Spent 18 mins on an impossible set and solved $< 1.5$ sets total | Set selection & sunk-cost trap | [`01_set_selection_and_5min_scanning_examples.md`](./dilr_concept_examples/01_set_selection_and_5min_scanning_examples.md), [`03_dilr_5min_set_selection_drill.md`](./high_recall/active_recall_drills/03_dilr_5min_set_selection_drill.md) |
| **DILR**: Didn't know how to draw the grid for arrangements, Venn, or tournaments | Grid evolution / invariant gap | [`03_arrangements_*_examples.md`](./dilr_concept_examples/03_arrangements_matrix_grids_and_scheduling_examples.md), [`04_games_*_examples.md`](./dilr_concept_examples/04_games_and_tournaments_knockout_and_round_robin_examples.md), [`05_venn_*_examples.md`](./dilr_concept_examples/05_venn_diagrams_and_4set_maxima_minima_examples.md) |
| **VARC**: Narrowed RC down to 2 options and consistently picked the wrong one | Falling for `Too_Extreme`, `Scope_Shift`, or `Half_Truth` | [`02_rc_question_types_and_7_distractor_traps_examples.md`](./varc_concept_examples/02_rc_question_types_and_7_distractor_traps_examples.md), [`04_varc_2option_tiebreaker_drill.md`](./high_recall/active_recall_drills/04_varc_2option_tiebreaker_drill.md) |
| **VARC**: Low accuracy on Para-Summary, Sentence Placement, or TITA Para-Jumbles | Missing structural link pairs & thesis check | [`03_va_parajumbles_*_examples.md`](./varc_concept_examples/03_va_parajumbles_and_odd_one_out_tita_mastery_examples.md), [`04_va_parasummary_*_examples.md`](./varc_concept_examples/04_va_parasummary_and_sentence_placement_examples.md) |
