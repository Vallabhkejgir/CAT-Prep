# CAT Quant Concept & Formula Examples — Master Intuitive Learning Guide

> **Study Flow Navigation**: See [**Master CAT Study Roadmap, Learning Loop & Diagnostic Flow (`../CAT_Study_Roadmap_and_Flow.md`)**](../CAT_Study_Roadmap_and_Flow.md) for how to combine these intuitive concept examples (Step 1) with [`topic_summaries/`](../topic_summaries/) (Step 2), [`mistakes_and_edge_cases/`](../mistakes_and_edge_cases/) (Step 3), and [`high_recall/`](../high_recall/) (Step 4).

Welcome to the **Intuitive Concept & Formula Examples Bank** (`insights/quant_concept_examples/`).

While [`insights/topic_summaries/quant/`](../topic_summaries/quant/) and [`QA_Formula_and_Trigger_Book.md`](../high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md) provide rapid-revision formulas and exam-hall speed triggers, this folder is designed for **deep conceptual clarity and intuition**. Every formula, identity, and pattern trigger across all 10 Quantitative Ability (QA) modules is unpacked using a standardized **5-Part Learning Template**:

1. **Concept & Formula in Plain English**: What the formula actually means in everyday language and *why* it works mechanically.
2. **When to Use It (Question Cue)**: The exact phrasing in a problem that tells you to reach for this tool.
3. **General Example (Clean Numbers, Single Concept)**: A self-contained, distraction-free example with friendly numbers that isolates just that one concept.
4. **Step-by-Step Walkthrough (Two Ways)**:
   - **Way 1 — Direct Formula Plug-in**: Variable-by-variable substitution so you see how every symbol maps to a number.
   - **Way 2 — Common-Sense / Ratio Intuition**: How to solve the exact same problem using $100$s, fractions, or mental ratios if you blank out on the formula.
5. **The 1 Common Mistake to Avoid**: The classic number trap or wrong denominator that catches test-takers off guard.

---

## Master Module & Concept Navigation Index

### Module 01: Arithmetic — Percentages, Profit & Loss, Discount, Faulty Weights, SI & CI, Installments
- **Example File**: [`01_arithmetic_percentages_pl_sici_examples.md`](./01_arithmetic_percentages_pl_sici_examples.md)
- **Companion Topic Summary**: [`../topic_summaries/quant/01_arithmetic_percentages_pl_sici.md`](../topic_summaries/quant/01_arithmetic_percentages_pl_sici.md)
- **Concepts & Formulas Covered**:
  1. **Multiplying Factor (MF) & Base-Shift Identity** ($\text{MF} = 1 \pm \frac{p}{100}$, "increased by" vs. "increased to", $X$ more than $Y \implies Y$ less than $X$)
  2. **Successive Percentage Change & Zero-Sum Loss** ($a + b + \frac{ab}{100}$ and $+x\% / -x\% \implies -\frac{x^2}{100}\%$)
  3. **Product Constancy ($A \times B = \text{Constant}$) & Non-Constant Expenditure Shift** ($\frac{a}{b} \uparrow \implies \frac{a}{b+a} \downarrow$)
  4. **Solid/Pulp Mass Invariance in Evaporation** (Fresh vs. Dry Fruit water percentage shifts)
  5. **Markup, Discount & Direct CP-to-MP Ratio** ($p = m - d - \frac{md}{100}$ and $\frac{\text{CP}}{\text{MP}} = \frac{100-d}{100+p}$)
  6. **Gross Margin (Profit on SP) vs. Markup (Profit on CP)** ($\text{Margin} = \frac{a}{b+a}$)
  7. **Two Articles Sold at the Same Selling Price ($S_1 = S_2$)** (Equal $+x\%$ profit and $-x\%$ loss trap)
  8. **Promotional Free Articles & Discount Sensitivity** ("Buy $m$ get $n$ free" with discount $d\%$, and doubling discount impact)
  9. **Dishonest Dealer & Faulty Weights Universal MF** ($\frac{\text{Price Charged}}{\text{Cost}} \times \frac{\text{Claimed Weight}}{\text{Actual Weight Dispensed}}$)
  10. **Simple Interest (SI), Compound Interest (CI) & Effective Annual Rate (EAR)** (Annual vs. semi-annual/quarterly compounding)
  11. **CI vs. SI 2-Year & 3-Year Difference Shortcuts & Pascal Tree** ($Pr^2$ and $Pr^2(3+r)$)
  12. **CI for the $n$-th Year vs. CI for $n$ Years & Exponential Doubling** ($I_n = Pr(1+r)^{n-1}$)
  13. **Equal Installments (CI Present Value Method vs. SI End-of-Term Debt Settlement)**

---

### Module 02: Arithmetic — Ratios, Proportions, Variation, Averages, Mixtures & Alligations
- **Example File**: [`02_arithmetic_ratios_averages_mixtures_alligations_examples.md`](./02_arithmetic_ratios_averages_mixtures_alligations_examples.md)
- **Companion Topic Summary**: [`../topic_summaries/quant/02_arithmetic_ratios_averages_mixtures_alligations.md`](../topic_summaries/quant/02_arithmetic_ratios_averages_mixtures_alligations.md)
- **Concepts & Formulas Covered**:
  1. **Equal Ratio Property (Linear Combination Theorem) & Zero-Sum Case** ($\frac{pa+qc}{pb+qd} = k$ and $a+b+c=0$ caveat)
  2. **Componendo & Dividendo and Adding Constant $x$ to a Fraction** ($\frac{a+b}{a-b}$ and drift toward $1$)
  3. **Direct, Inverse & Joint/Partial Variation** ($y = a + bx$ fixed + variable expense models)
  4. **Partnership Capital-Time Ratio** ($\text{Profit} \propto C_1 T_1 : C_2 T_2$)
  5. **Weighted Average & Assumed Mean Deviation Shortcut** ($A_{\text{avg}} = M + \frac{\sum n_i(A_i - M)}{\sum n_i}$)
  6. **Average Shift on Member Replacement or Inclusion** ($V_{\text{new}} = V_{\text{old}} + N\Delta A$)
  7. **Arithmetic Progression (AP) Average & Outlier Maximization** (Median property and maximizing largest of $N$ distinct positive integers)
  8. **Alligation Seesaw / Lever Rule & The Denominator Unit Law** ($\frac{n_1}{n_2} = \frac{A_2 - A_{\text{avg}}}{A_{\text{avg}} - A_1}$)
  9. **Combining Vessels with Different Capacities & Concentrations** (LCM scaling method)
  10. **Repeated Removal & Replacement (Dilution & Alternating Enrichment)** ($C_{\text{final}} = C_0(1 - \frac{x}{V})^n$)
  11. **Two-Vessel Equilibrium Swap & Symmetric Transfer Invariant** ($x^* = \frac{V_A V_B}{V_A + V_B}$ and $V : v$ ratio)

---

### Module 03: Arithmetic — Time & Work, Pipes & Cisterns, Time Speed Distance, Races & Circular Tracks
- **Example File**: [`03_arithmetic_time_work_tsd_races_circular_tracks_examples.md`](./03_arithmetic_time_work_tsd_races_circular_tracks_examples.md)
- **Companion Topic Summary**: [`../topic_summaries/quant/03_arithmetic_time_work_tsd_races_circular_tracks.md`](../topic_summaries/quant/03_arithmetic_time_work_tsd_races_circular_tracks.md)
- **Concepts & Formulas Covered**:
  1. **LCM Total-Work Method & Man-Days-Hours Equivalence** ($\frac{M_1 D_1 H_1 E_1}{W_1} = \frac{M_2 D_2 H_2 E_2}{W_2}$)
  2. **Extra Time Over Combined Work Time** ($T_{AB} = \sqrt{ab}$)
  3. **Alternating Positive & Negative Work (Monkey Climb / Emptying Pipe Trap)** (Reserving the positive jump $W - p$)
  4. **Proportionality Laws in TSD & Breakdown Delay Localization** ($S \propto \frac{1}{T}$ for constant distance)
  5. **Average Speed: Harmonic Mean vs. Arithmetic Mean & Bus Stoppage Formula** ($\frac{2s_1 s_2}{s_1+s_2}$ and $\frac{S_{\text{fast}}-S_{\text{slow}}}{S_{\text{fast}}}$)
  6. **Radha–Shyam Post-Meeting Theorem** ($\frac{S_A}{S_B} = \sqrt{\frac{t_B}{t_A}}$ and $t_{\text{meet}} = \sqrt{t_A t_B}$)
  7. **Trains Crossing Poles, Platforms & Moving Observers** (Relative speed and length addition)
  8. **Boats & Streams Upstream/Downstream Decomposition** ($u = \frac{S_D+S_U}{2}, v = \frac{S_D-S_U}{2}$)
  9. **Escalators — Visible Steps Invariant** ($N = S_p \pm e \cdot t$)
  10. **Linear Races (Start of Distance $d$ and/or Time $t$) & Chained Race Ratios**
  11. **Shuttle Runs Between Two Towns ($k$-th Head-On & Same-End Meetings)** ($(2k-1)D$ vs. $2kD$)
  12. **Circular Tracks (First Meeting, Starting Point Reunion & Distinct Meeting Points $|a \mp b|$)**
  13. **Clocks & Relative Angular Speed** ($\frac{11}{2}^\circ/\text{min}$ and $\frac{720}{11}\text{ min}$ coincidence cycle)

---

### Module 04: Algebra — Linear & Diophantine Equations, Polynomials, Inequalities & Modulus
- **Example File**: [`04_algebra_equations_polynomials_inequalities_modulus_examples.md`](./04_algebra_equations_polynomials_inequalities_modulus_examples.md)
- **Companion Topic Summary**: [`../topic_summaries/quant/04_algebra_equations_polynomials_inequalities_modulus.md`](../topic_summaries/quant/04_algebra_equations_polynomials_inequalities_modulus.md)
- **Concepts & Formulas Covered**:
  1. **Consistency of 2-Variable Linear Systems & Indeterminate Block Substitution** (Unique, No Solution, Infinite Solutions)
  2. **Linear Diophantine Equations ($ax + by = c$) & Step-Shifting** ($x = x_0 + kb, y = y_0 - ka$)
  3. **Frobenius Coin / Postage Stamp Theorem** ($ab - a - b$ and $ab$)
  4. **Simon's Favorite Factoring Trick ($xy + ax + by = c$)** (Completing the rectangle $(x+b)(y+a) = c+ab$ over $\mathbb{Z}^+$ and $\mathbb{Z}$)
  5. **Vieta's Root-Coefficient Relations, Power Sums & Reciprocal Newton Recurrence** ($S_n = S_{n-k}S_k - S_{|n-2k|}$)
  6. **Quadratic Discriminant, Constant-Sign Condition ($ax^2+bx+c > 0$) & Degenerate $a=0$ Check**
  7. **Location of Roots Relative to a Number $k$** ($a \cdot f(k) < 0$ for root separation)
  8. **Polynomial Remainder & Factor Theorems + Coefficient Sums ($P(1), P(-1), P(0)$)**
  9. **Wavy Curve Method of Intervals (Odd vs. Even Multiplicity & Denominator Exclusions)**
  10. **Modulus Triangle Inequalities & Equality Conditions** ($|A| + |B| = |A \pm B| \iff AB \gtrless 0$)
  11. **Sum of Absolute Deviations ($\sum |x - a_i|$) — Median Minimization Rule**
  12. **Diamond / Rhombus Region ($|x - h| + |y - k| \le r$) Area & Lattice Points** ($\text{Area} = 2r^2$, Points $= 2r^2+2r+1$)
  13. **Nested Modulus Equations ($\big||x - a| - b\big| = c$) & W-Graph Root Counting**

---

### Module 05: Algebra — Functions, Graphs, Functional Equations, Logarithms, Surds & Indices
- **Example File**: [`05_algebra_functions_graphs_logs_surds_examples.md`](./05_algebra_functions_graphs_logs_surds_examples.md)
- **Companion Topic Summary**: [`../topic_summaries/quant/05_algebra_functions_graphs_logs_surds.md`](../topic_summaries/quant/05_algebra_functions_graphs_logs_surds.md)
- **Concepts & Formulas Covered**:
  1. **Logarithm Strict Domain Rules ($\text{arg} > 0, \text{base} > 0, \text{base} \neq 1$) & Variable-Base Filtering**
  2. **Core Log Identities, Base-Change Chain Rule & Exponent-Swap ($a^{\log_b c} = c^{\log_b a}$)**
  3. **Logarithmic Inequalities & The Base $0 < b < 1$ Sign-Flip Rule** ($\log_b f(x) \ge k \iff 0 < f(x) \le b^k$)
  4. **Characteristic & Mantissa: Counting Digits in $N$ & Leading Zeros in $0 < N < 1$** ($\lfloor \log_{10} N \rfloor + 1$)
  5. **De-nesting Nested Square Roots ($\sqrt{a \pm 2\sqrt{b}} = |\sqrt{x} \pm \sqrt{y}|$)**
  6. **Rationalizing Surd Denominators & Telescoping Surd Sums** ($\frac{1}{\sqrt{k+1}+\sqrt{k}} = \sqrt{k+1}-\sqrt{k}$)
  7. **Comparing Surds & Solving $f(x)^{g(x)} = 1$ (The 3-Case Checklist)**
  8. **Counting Functions (Total $n^m$, One-to-One / Injective, Onto / Surjective, Bijective)**
  9. **Standard Cauchy Functional Equations & Symmetric Pairing ($f(x) + f(1-x) = c$)**
  10. **Iterative / Periodic Composite Functions $f^{(n)}(x)$ & Domain of Composite Rational Functions**
  11. **Greatest Integer Function $\lfloor x \rfloor$, Fractional Part $\{x\}$, Hermite's Identity & $\lfloor x^2 \rfloor = \lfloor x \rfloor^2$**

---

### Module 06: Algebra — Sequences, Series, Telescoping Sums & Maxima/Minima
- **Example File**: [`06_algebra_sequences_series_maxima_minima_examples.md`](./06_algebra_sequences_series_maxima_minima_examples.md)
- **Companion Topic Summary**: [`../topic_summaries/quant/06_algebra_sequences_series_maxima_minima.md`](../topic_summaries/quant/06_algebra_sequences_series_maxima_minima.md)
- **Concepts & Formulas Covered**:
  1. **Arithmetic Progression (AP): $T_n$, Middle-Term Sum $S_n = n \cdot T_{\text{mid}}$ & Quadratic Sum Signature $S_n = An^2 + Bn$**
  2. **AP Ratio of Sums vs. Ratio of Terms ($\frac{S_{2m-1}}{S'_{2m-1}} = \frac{T_m}{T'_m}$) & Common Terms of Multiple APs**
  3. **Geometric Progression (GP), Infinite GP, Product of Terms & 3-Term Pairwise Identity**
  4. **Harmonic Progression (HP) & Arithmetico-Geometric Progression (AGP)**
  5. **Standard Power Sums ($\sum k, \sum k^2, \sum k^3$, Odd Prefix Sum $m^2$) & Method of Finite Differences**
  6. **Telescoping Partial Fractions ($\frac{1}{k(k+d)}$ and $\frac{1}{k(k+1)(k+2)}$)**
  7. **Factorial Telescoping ($k \cdot k!$, $\frac{k}{(k+1)!}$) & Telescoping Radical $\sqrt{1 + \frac{1}{k^2} + \frac{1}{(k+1)^2}}$**
  8. **AM-GM-HM Inequality & Shifted-Denominator Balancing (plus Boundary Attainability Guard)**
  9. **Weighted AM-GM Term Splitting (Maximizing $x^p y^q z^r$ & Cancelling Unequal Powers)**
  10. **Cauchy-Schwarz Inequality / Titu's Lemma & Parabola Vertex Extrema**

---

### Module 07: Geometry — Lines, Angles, Triangles, Circles, Quadrilaterals & Polygons
- **Example File**: [`07_geometry_triangles_circles_polygons_examples.md`](./07_geometry_triangles_circles_polygons_examples.md)
- **Companion Topic Summary**: [`../topic_summaries/quant/07_geometry_triangles_circles_polygons.md`](../topic_summaries/quant/07_geometry_triangles_circles_polygons.md)
- **Concepts & Formulas Covered**:
  1. **Triangle Existence Inequality, Acute/Right/Obtuse Classification & Counting Integer Triangles**
  2. **The 5 Triangle Area Formulas ($\frac{1}{2}bh, \frac{1}{2}ab\sin C$, Heron, $rs$, $\frac{abc}{4R}$) & Equilateral/Right Formulas**
  3. **Right-Triangle Altitude to Hypotenuse Similarity & Inscribed Square ($x = \frac{ab}{a+b}$)**
  4. **The 4 Triangle Centers ($I, O, G, H$), Euler Line & Center Angle Formulas**
  5. **Internal Angle Bisector Theorem & Length Formula ($AD^2 = bc - pq$)**
  6. **Apollonius' Median Theorem & Stewart's Cevian Theorem**
  7. **Mass Point Geometry (Replacing Ceva's & Menelaus' Theorems)**
  8. **Circle Chords, Power of a Point ($PA \cdot PB = PT^2$) & Alternate Segment Theorem**
  9. **Direct & Transverse Common Tangents, Ford Tangent Circle ($\frac{1}{\sqrt{r}} = \frac{1}{\sqrt{r_1}} + \frac{1}{\sqrt{r_2}}$) & Third-Tangent Center Angle**
  10. **Cyclic Quadrilaterals (Ptolemy & Brahmagupta) & Tangential Quadrilaterals (Pitot's Theorem)**
  11. **Trapezium Diagonal Triangle Areas ($(\sqrt{A_1}+\sqrt{A_2})^2$) & Harmonic Mean Segment ($\frac{2ab}{a+b}$)**
  12. **Rhombus Diagonal-Side Identity ($d_1^2 + d_2^2 = 4a^2$) & Regular Polygon / Hexagon Properties**

---

### Module 08: Geometry — 3D Mensuration, Inscribed Solids, Coordinate Geometry & Trigonometry
- **Example File**: [`08_geometry_mensuration_3d_coordinate_trig_examples.md`](./08_geometry_mensuration_3d_coordinate_trig_examples.md)
- **Companion Topic Summary**: [`../topic_summaries/quant/08_geometry_mensuration_3d_coordinate_trig.md`](../topic_summaries/quant/08_geometry_mensuration_3d_coordinate_trig.md)
- **Concepts & Formulas Covered**:
  1. **Cuboid & Cube Mensuration, Edge-Diagonal-TSA Identity $(l+b+h)^2 = d^2 + \text{TSA}$ & Shortest Ant Path**
  2. **Cylinder & Cone Mensuration, Unfolded Spiral Path & Sector-to-Cone Folding**
  3. **Cone Sliced Parallel to Base ($1 : 7 : 19$ Volume Ratio) & Frustum of a Cone**
  4. **Sphere, Hemisphere, Solid Cutting Surface Area Gain & Regular Tetrahedron**
  5. **Inscribed 3D Solids (Sphere in Cone $R = \frac{rh}{r+l}$, Max Cylinder in Cone $\frac{4}{27}V$, Cube/Cylinder/Cone in Sphere)**
  6. **Coordinate Distance, Section Formula, Parallelogram Vertex Rule ($S = P + R - Q$) & Segment Lattice Points**
  7. **Triangle Coordinate Centers (Centroid $G$, Incenter $I$) & Shift-to-Origin Shoelace Area**
  8. **Point-to-Line Distance, Parallel Line Distance & Reflection / Foot of Perpendicular**
  9. **Circle Coordinate Equation & Tangent Condition**
  10. **Trigonometric Identities ($\sec\theta \pm \tan\theta$), Extrema of $a\sin\theta + b\cos\theta$, Sine/Cosine Rules & Two-Angle Heights/Distances**

---

### Module 09: Number System — Divisibility, Factors, HCF/LCM, Remainders, Factorials & Base Systems
- **Example File**: [`09_number_system_divisibility_factors_hcflcm_remainders_examples.md`](./09_number_system_divisibility_factors_hcflcm_remainders_examples.md)
- **Companion Topic Summary**: [`../topic_summaries/quant/09_number_system_divisibility_factors_hcflcm_remainders_bases.md`](../topic_summaries/quant/09_number_system_divisibility_factors_hcflcm_remainders_bases.md)
- **Concepts & Formulas Covered**:
  1. **Prime Form $6k \pm 1$ ($p^2 \equiv 1 \pmod{24}$), Special Divisibility ($1001 = 7 \times 11 \times 13$) & Algebraic Divisibility ($a^n \pm b^n$)**
  2. **Counting, Summing & Multiplying Factors ($d(N), \sigma(N), N^{d(N)/2}$, Odd/Even/Square/Mod-3 Factors)**
  3. **Factor Pairs, Coprime Factor Pairs ($2^{k-1}$), Difference of Squares ($x^2 - y^2 = N$) & Unit Fraction Equation ($\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$)**
  4. **HCF & LCM Parameterization ($a = Hx, b = Hy$) & HCF/LCM of Fractions**
  5. **The 3 Canonical Remainder Models (Same Remainder, Constant Difference & Chinese Remainder Stepping)**
  6. **Common-Factor Cancellation in Remainders, Euler's Totient & Fermat's Little Theorem**
  7. **Wilson's Factorial Remainder Theorem ($(p-1)! \equiv p-1 \pmod p$ and $(p-2)! \equiv 1 \pmod p$)**
  8. **Legendre's Formula for $E_p(n!)$ & Trailing Zeros of $n!$ in Base $10$ and Base $B$**
  9. **Last Two Digits ($\bmod 100$) Shortcuts & Base System Divisibility by $(B-1)$ and $(B+1)$**
  10. **Recurring Decimals to Fractions & Decimal Borrow Propagation ($10^m + 10^n - k$)**

---

### Module 10: Modern Math — Permutations & Combinations, Probability & Set Theory
- **Example File**: [`10_modern_math_pnc_probability_set_theory_examples.md`](./10_modern_math_pnc_probability_set_theory_examples.md)
- **Companion Topic Summary**: [`../topic_summaries/quant/10_modern_math_pnc_probability_set_theory.md`](../topic_summaries/quant/10_modern_math_pnc_probability_set_theory.md)
- **Concepts & Formulas Covered**:
  1. **Fundamental Counting, 'Up to $k$' Selections, Tie/String Method (Together) & Gap Method (No Two Adjacent)**
  2. **The 4-Box Distribution Matrix & Stars and Bars ($\binom{n+r-1}{r-1}$, Lower Bounds, Upper Bounds & Slack Inequality $\le n$)**
  3. **Circular Permutations ($(n-1)!$ vs. $\frac{(n-1)!}{2}$) & Unlabeled Equal-Size Group Division**
  4. **Derangements ($D_n$ — No Element in Right Place) & Partial Derangements ($\binom{n}{k}D_{n-k}$)**
  5. **Geometric Counting (Collinear Points Lines/Triangles & $m \times n$ Grid Rectangles/Squares) & Dictionary Rank**
  6. **Probability Addition/Multiplication Rules, Independent vs. Mutually Exclusive Events & 'At Least One' Complement**
  7. **Conditional Probability & Bayes' Theorem (Including Multi-Outcome Witness Lie Factor)**
  8. **Binomial Probability, Odd/Even Successes Shortcut & Infinite Alternating Geometric Game ($\frac{p_A}{1 - q_A q_B}$)**
  9. **3-Set Inclusion-Exclusion, 'Exactly $k$ Sets' Layer Equations ($E_1, E_2, E_3$) & Positivity Constraint ($x \ge 1$)**
  10. **$k$-Set Intersection Minimum (Surplus Rule $\sum |A_i| - (k-1)|U|$) & Maximum**
