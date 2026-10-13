# Canonical CAT Syllabus Coverage & 2025 PYQ Gap-Fill Audit Matrix

This matrix audits **100% of the Canonical CAT Syllabus Taxonomy** (`docs/syllabus/canonical_taxonomy.md`) against all **204 extracted CAT 2025 PYQ questions** across the 9 official question papers (**QA Slots 1–3**: 66 questions; **DILR Slots 1–3**: 66 questions / 15 sets; **VARC Slots 1–3**: 72 questions / 12 RC passages + 24 VA questions), mapping every sub-topic to its exact 2025 PYQ frequency count, Question IDs, Priority Tier, Gap-Fill status, and Master Note / Playbook file.

- **Priority Tiers**:
  - **Tier 1 (High-Yield Core)**: Tested in virtually every CAT slot (accounts for ~75% of exam marks).
  - **Tier 2 (Medium-Yield Scorer)**: Tested in 1–2 slots per year; high accuracy when formulas/templates are known.
  - **Tier 3 (Rare-but-Tested Edge Topic)**: Appears periodically; any sub-topic with `< 3` CAT 2025 PYQ instances is flagged `[GAP_FILL_REQUIRED -> SYNTHESIZED]` to ensure complete first-principles theory, shortcuts, and CAT-grade solved exemplars are present in the master notes.

---

## 1. Quantitative Ability (QA) — 100% Sub-Topic Coverage & CAT 2025 PYQ Map (66 Questions)

| Module | Canonical Topic & Sub-Topic | 2025 PYQ Count | CAT 2025 Question IDs (Slots 1, 2, 3) | Priority Tier | Coverage & Gap-Fill Status | Master Note File |
| :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| **QA-01** | **Percentages & Successive Change** (MF, $a+b+ab/100$, Product Constancy, Base-Shift) | **2** | `CAT2025_S1_QA_Q01`, `CAT2025_S2_QA_Q13` | Tier 1 | Complete (`[GAP_FILL_REQUIRED -> SYNTHESIZED]`) | `insights/topic_summaries/quant/01_arithmetic_percentages_pl_sici.md` |
| **QA-01** | **Profit, Loss, Discount & Faulty Weights** (CP/SP/MP, Margin vs Markup, Dishonest Scale MF) | **3** | `CAT2025_S1_QA_Q07`, `CAT2025_S2_QA_Q12`, `CAT2025_S3_QA_Q17` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/01_arithmetic_percentages_pl_sici.md` |
| **QA-01** | **SI, CI & Equal Installments** (2/3-Yr CI-SI Diff, Effective Rate, Present Value Amortization) | **2** | `CAT2025_S1_QA_Q04`, `CAT2025_S2_QA_Q09` | Tier 1 | Complete (`[GAP_FILL_REQUIRED -> SYNTHESIZED]`) | `insights/topic_summaries/quant/01_arithmetic_percentages_pl_sici.md` |
| **QA-02** | **Ratio, Proportion, Variation & Partnerships** (Equal Ratio Theorem, Componendo-Dividendo, Joint Variation) | **3** | `CAT2025_S1_QA_Q17`, `CAT2025_S2_QA_Q05`, `CAT2025_S3_QA_Q09` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/02_arithmetic_ratios_averages_mixtures_alligations.md` |
| **QA-02** | **Averages, Mixtures & Alligations** (Seesaw Rule, Assumed Mean, Repeated Replacement $C_0(1-x/V)^n$) | **6** | `CAT2025_S1_QA_Q13`, `CAT2025_S1_QA_Q20`, `CAT2025_S2_QA_Q08`, `CAT2025_S2_QA_Q20`, `CAT2025_S3_QA_Q03`, `CAT2025_S3_QA_Q20` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/02_arithmetic_ratios_averages_mixtures_alligations.md` |
| **QA-03** | **Time & Work, Pipes & Cisterns** (LCM Efficiency, Cost-Optimal Scheduling, Team Replacement) | **4** | `CAT2025_S1_QA_Q21`, `CAT2025_S2_QA_Q17`, `CAT2025_S3_QA_Q10`, `CAT2025_S3_QA_Q11` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/03_arithmetic_time_work_tsd_races_circular_tracks.md` |
| **QA-03** | **Time, Speed & Distance (TSD), Trains, Boats & Escalators** ($\sqrt{t_A t_B}$, Harmonic Mean, Boats & Streams) | **4** | `CAT2025_S1_QA_Q15`, `CAT2025_S2_QA_Q21`, `CAT2025_S3_QA_Q07`, `CAT2025_S3_QA_Q12` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/03_arithmetic_time_work_tsd_races_circular_tracks.md` |
| **QA-03** | **Linear Races & Circular Tracks** (Dead Heat, $\text{LCM}(L/v_i)$, Distinct Meeting Points $|a \mp b|$) | **0** | *(Tested via circular state-ring transitions in `CAT2025_S1_DILR_SET1` & `CAT2025_S3_DILR_SET4`)* | Tier 1 | Complete (`[GAP_FILL_REQUIRED -> SYNTHESIZED]`) | `insights/topic_summaries/quant/03_arithmetic_time_work_tsd_races_circular_tracks.md` |
| **QA-04** | **Linear & Diophantine Equations** ($ax+by=c$, Frobenius Stamp/Coin Theorem, Block Elimination) | **3** | `CAT2025_S1_QA_Q02`, `CAT2025_S1_QA_Q22`, `CAT2025_S3_QA_Q21` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/04_algebra_equations_polynomials_inequalities_modulus.md` |
| **QA-04** | **Quadratic & Higher-Degree Polynomials** (Vieta's Relations, Common Roots, Reciprocal Power Sums) | **5** | `CAT2025_S1_QA_Q06`, `CAT2025_S2_QA_Q07`, `CAT2025_S2_QA_Q11`, `CAT2025_S3_QA_Q06`, `CAT2025_S3_QA_Q15` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/04_algebra_equations_polynomials_inequalities_modulus.md` |
| **QA-04** | **Inequalities & Modulus** (Wavy Curve, Lattice Counting, Piecewise Quadratic Modulus, Bounded Ratios) | **3** | `CAT2025_S1_QA_Q11`, `CAT2025_S2_QA_Q10`, `CAT2025_S3_QA_Q19` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/04_algebra_equations_polynomials_inequalities_modulus.md` |
| **QA-05** | **Logarithms, Surds & Indices** (Base-Change, $0<b<1$ Flip, Variable-Base Domain, Prime Exponent Matching) | **3** | `CAT2025_S1_QA_Q09`, `CAT2025_S3_QA_Q08`, `CAT2025_S3_QA_Q13` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/05_algebra_functions_graphs_logs_surds.md` |
| **QA-05** | **Functions, Graphs, GIF & Functional Equations** ($\lfloor x^2 \rfloor = \lfloor x \rfloor^2$, Composite Domains, Rational Range) | **3** | `CAT2025_S1_QA_Q05`, `CAT2025_S2_QA_Q14`, `CAT2025_S3_QA_Q16` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/05_algebra_functions_graphs_logs_surds.md` |
| **QA-06** | **Sequences & Series** (AP, Decreasing Infinite GP, Sum of Squares vs AP, Odd Prefix Sums) | **4** | `CAT2025_S1_QA_Q10`, `CAT2025_S1_QA_Q19`, `CAT2025_S2_QA_Q01`, `CAT2025_S3_QA_Q22` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/06_algebra_sequences_series_maxima_minima.md` |
| **QA-06** | **Maxima & Minima** (Parabola Vertex Extrema, Log-Reduced AM-GM, Discrete Sum of Squares) | **3** | `CAT2025_S1_QA_Q14`, `CAT2025_S2_QA_Q06`, `CAT2025_S2_QA_Q22` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/06_algebra_sequences_series_maxima_minima.md` |
| **QA-07** | **Lines, Angles & Triangles** (Circumcircle Similarity, Mass Point / Menelaus, Isosceles Altitudes) | **3** | `CAT2025_S2_QA_Q19`, `CAT2025_S3_QA_Q05`, `CAT2025_S3_QA_Q18` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/07_geometry_triangles_circles_polygons.md` |
| **QA-07** | **Circles, Quadrilaterals & Polygons** (Parallel Chords, Third Tangent, Rhombus, Hexagon, Tangential Trapezium) | **5** | `CAT2025_S1_QA_Q12`, `CAT2025_S1_QA_Q18`, `CAT2025_S2_QA_Q02`, `CAT2025_S2_QA_Q03`, `CAT2025_S3_QA_Q02` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/07_geometry_triangles_circles_polygons.md` |
| **QA-08** | **3D Mensuration & Inscribed Solids** (Frustum, Tetrahedron, Cone Slices, Inscribed Sphere/Cylinder, Surface Net) | **0** | *(0 direct instances in 2025; full exemplar bank synthesized)* | Tier 2 | Complete (`[GAP_FILL_REQUIRED -> SYNTHESIZED]`) | `insights/topic_summaries/quant/08_geometry_mensuration_3d_coordinate_trig.md` |
| **QA-08** | **Coordinate Geometry & Trigonometry** (Parallelogram Vertex Invariance, Section Formula, Shoelace Area) | **1** | `CAT2025_S1_QA_Q03` | Tier 2 | Complete (`[GAP_FILL_REQUIRED -> SYNTHESIZED]`) | `insights/topic_summaries/quant/08_geometry_mensuration_3d_coordinate_trig.md` |
| **QA-09** | **Divisibility, Primes & Factor Theory** ($d(N)$, $(3r+1)$ Divisors, Negative Factor Pairs, Distinct Naturals) | **4** | `CAT2025_S1_QA_Q16`, `CAT2025_S2_QA_Q04`, `CAT2025_S2_QA_Q15`, `CAT2025_S2_QA_Q18` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/09_number_system_divisibility_factors_hcflcm_remainders_bases.md` |
| **QA-09** | **HCF/LCM, Modular Remainders, Factorials & Base Systems** ($5^{260}\cdot 2^{252}$ Digit Sum, $10^{50}+10^{25}-123$, 4-Digit Place Value) | **3** | `CAT2025_S2_QA_Q16`, `CAT2025_S3_QA_Q01`, `CAT2025_S3_QA_Q14` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/quant/09_number_system_divisibility_factors_hcflcm_remainders_bases.md` |
| **QA-10** | **Permutations & Combinations** (Fundamental Counting, 'Up to $k$' Combinations, Stars & Bars, Derangements) | **1** | `CAT2025_S1_QA_Q08` | Tier 1 | Complete (`[GAP_FILL_REQUIRED -> SYNTHESIZED]`) | `insights/topic_summaries/quant/10_modern_math_pnc_probability_set_theory.md` |
| **QA-10** | **Probability & Set Theory** (3-Set Inclusion-Exclusion Maxima/Minima, Bayes' Theorem, Binomial Trials) | **1** | `CAT2025_S3_QA_Q04` | Tier 2 | Complete (`[GAP_FILL_REQUIRED -> SYNTHESIZED]`) | `insights/topic_summaries/quant/10_modern_math_pnc_probability_set_theory.md` |

---

## 2. Data Interpretation & Logical Reasoning (DILR) — 100% Archetype & CAT 2025 PYQ Map (66 Questions / 15 Sets)

| Module | Canonical Archetype & Sub-Topic | 2025 PYQ Count | CAT 2025 Set & Question IDs (Slots 1, 2, 3) | Priority Tier | Coverage & Gap-Fill Status | Playbook File |
| :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| **DILR-01** | **Set Selection & 4-Minute Scanning Framework** (Bucket A/B/C Triage, 6-Min Bailout, Scratchpad Zones) | **All 15 Sets** | Applied across `CAT2025_S1_DILR_SET1..5`, `CAT2025_S2_DILR_SET1..5`, `CAT2025_S3_DILR_SET1..5` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/dilr/01_set_selection_and_5min_scanning_framework.md` |
| **DILR-02** | **Quantitative & Reasoning-Based DI** (Radar + Bar Tariff Charts, Missing-Value Call Table, Step-Function Progress Charts, Bilateral Trade Matrices, Sustainability Scatter Plot) | **21 Qs (5 Sets)** | `S1_SET3` (`Q10–Q13`), `S2_SET4` (`Q14–Q17`), `S3_SET1` (`Q01–Q04`), `S3_SET3` (`Q10–Q13`), `S3_SET5` (`Q18–Q22`) | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/dilr/02_quantitative_di_tables_charts_and_growth_traps.md` |
| **DILR-03** | **Linear, Circular & 2D Matrix Arrangements & Scheduling** (7-Chair Circular Ring Moves, Ball-Hoop Threshold Ordering, 12-Year Musician-Guru Scheduling, 7-Child Circular Modular Buck Game) | **17 Qs (4 Sets)** | `S1_SET1` (`Q01–Q04`), `S2_SET1` (`Q01–Q04`), `S2_SET5` (`Q18–Q22`), `S3_SET4` (`Q14–Q17`) | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/dilr/03_arrangements_matrix_grids_and_scheduling.md` |
| **DILR-04** | **Games & Tournaments** (Seeded Knockout Brackets $2^r+1$, Upsets, Round-Robin $3M-D$, Qualification Extrema) | **0** | *(0 direct knockout/league brackets in 2025; competitive puzzle-race in `S3_SET3`; full exemplar bank synthesized)* | Tier 1 | Complete (`[GAP_FILL_REQUIRED -> SYNTHESIZED]`) | `insights/topic_summaries/dilr/04_games_and_tournaments_knockout_and_round_robin.md` |
| **DILR-05** | **Venn Diagrams & 3/4-Set Maxima-Minima** (4-Author Multi-Paper Hypergraph Degree-Sum Set) | **4 Qs (1 Set)** | `S2_SET3` (`Q10–Q13`, plus QA `CAT2025_S3_QA_Q04`) | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/dilr/05_venn_diagrams_and_4set_maxima_minima.md` |
| **DILR-06** | **Networks, Flows, CPM Scheduling & Quant-LR Puzzles** (Train Segment Occupancy Flow, Quarterly Rating Promotion/Demotion Machine, 5x5 Foot-Tapping Game, State Pollution Weighted Averages, 4-Country Currency Exchange Puzzle) | **24 Qs (5 Sets)** | `S1_SET2` (`Q05–Q09`), `S1_SET4` (`Q14–Q18`), `S1_SET5` (`Q19–Q22`), `S2_SET2` (`Q05–Q09`), `S3_SET2` (`Q05–Q09`) | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/dilr/06_networks_routes_flows_and_quant_lr_puzzles.md` |

---

## 3. Verbal Ability & Reading Comprehension (VARC) — 100% Sub-Topic & CAT 2025 PYQ Map (72 Questions)

| Module | Canonical Topic & Sub-Topic | 2025 PYQ Count | CAT 2025 Question IDs (Slots 1, 2, 3) | Priority Tier | Coverage & Gap-Fill Status | Playbook File |
| :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| **VARC-01** | **RC Passage Architecture & 5 Genre Playbooks** (12 Full RC Passages across Aesthetics/Music, Complexity Science, Legal History, Political Economy, Literary Geography, AI Ethics/Rhetoric, Evolutionary Biology, Philosophy of Science, Environmental History, Colonial Forestry, Dams/Ecology, Tribal Aesthetics) | **12 Passages (48 Qs)** | `S1`: `Q02–Q05`, `Q09–Q12`, `Q15–Q18`, `Q20–Q23`; `S2`: `Q02–Q05`, `Q06–Q09`, `Q10–Q13`, `Q15–Q18`; `S3`: `Q01–Q04`, `Q05–Q08`, `Q16–Q19`, `Q20–Q23` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/varc/01_rc_reading_architecture_and_genre_guides.md` |
| **VARC-02** | **RC Question Types, Critical Reasoning & 7 Distractor Traps** (Main Idea/Conceptual Map: 8; Inference/EXCEPT: 15; Critical Reasoning Strengthen/Weaken/Assumption: 8; Paragraph/Example Function: 8; Vocabulary/Application: 9) | **48 Qs** | All 48 RC questions across `CAT2025_S1_VARC`, `CAT2025_S2_VARC`, `CAT2025_S3_VARC` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/varc/02_rc_question_types_and_7_distractor_traps.md` |
| **VARC-03** | **VA TITA Para-Jumbles & Odd-One-Out** (6 TITA 4-Sentence Para-Jumbles + 6 TITA 5-Sentence Odd-One-Out) | **12 Qs** | **PJ**: `S1_Q06`, `S1_Q13`, `S2_Q19`, `S2_Q23`, `S3_Q11`, `S3_Q15`; **OOO**: `S1_Q01`, `S1_Q19`, `S2_Q22`, `S2_Q24`, `S3_Q10`, `S3_Q14` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/varc/03_va_parajumbles_and_odd_one_out_tita_mastery.md` |
| **VARC-04** | **VA Para-Summary & 4-Slot Sentence Placement** (6 MCQ Para-Summaries + 6 MCQ 4-Slot Sentence Placements) | **12 Qs** | **Summary**: `S1_Q14`, `S1_Q24`, `S2_Q01`, `S2_Q21`, `S3_Q13`, `S3_Q24`; **Placement**: `S1_Q07`, `S1_Q08`, `S2_Q14`, `S2_Q20`, `S3_Q09`, `S3_Q12` | Tier 1 | Complete (`2025_PYQ_VERIFIED`) | `insights/topic_summaries/varc/04_va_parasummary_and_sentence_placement.md` |

---

## 4. Cross-Sectional Audit & High-Recall Assets Verification

| Asset Type | File Path | Status |
| :--- | :--- | :---: |
| **CAT 2025 Structured PYQ Inventory (9 JSONs, 204 Qs)** | `extractions/structured_pyqs/CAT_2025_*_Slot_*_questions.json` | Complete |
| **CAT 2025 Per-Paper Pass 1 Analyses (9 Papers + Master Key)** | `insights/per_paper/CAT_2025_*_analysis.md` & `CAT_2025_Master_Answer_Key_and_Slot_Comparison.md` | Complete |
| **QA Pitfalls Manual** | `insights/mistakes_and_edge_cases/quant_pitfalls.md` | Complete |
| **DILR Traps Manual** | `insights/mistakes_and_edge_cases/dilr_traps.md` | Complete |
| **VARC Traps Manual** | `insights/mistakes_and_edge_cases/varc_traps.md` | Complete |
| **QA Formula & Trigger Book** | `insights/high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md` | Complete |
| **DILR Archetype Templates** | `insights/high_recall/cheat_sheets/DILR_Archetype_Templates.md` | Complete |
| **VARC Elimination & VA Rules** | `insights/high_recall/cheat_sheets/VARC_Elimination_and_VA_Rules.md` | Complete |
| **Spaced-Repetition Deck (150+ Cards)** | `insights/high_recall/anki_flashcards.csv` | Complete |
| **40-Min Execution & Self-Audit Checklist** | `insights/CAT_Self_Audit_Checklist.md` | Complete |
