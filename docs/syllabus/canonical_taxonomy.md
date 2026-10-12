# Canonical CAT Syllabus Taxonomy & Pattern Blueprint

This canonical taxonomy serves as the **100% syllabus coverage baseline** for the CAT preparation and PYQ synthesis pipeline across **Quantitative Ability (QA)**, **Data Interpretation & Logical Reasoning (DILR)**, and **Verbal Ability & Reading Comprehension (VARC)**. Every extracted PYQ is mapped to a canonical topic and sub-topic below, and any sub-topic with fewer than 3 PYQ instances is flagged `[GAP_FILL_REQUIRED]` during Pass 2 so Pass 3 generates full first-principles theory, shortcuts, traps, and synthetic CAT-grade exemplars.

---

## Section 1: Quantitative Ability (QA)

### 1. Arithmetic (Weightage: ~40–45%)
- **Percentages & Successive Change**
  - Multiplying factors, successive percentage changes $a + b + \frac{ab}{100}$, base-shift traps (% of A vs. % more than B), $A \times B = \text{const}$ product constancy ($\frac{+1}{n} \leftrightarrow \frac{-1}{n+1}$), Venn percentages.
- **Profit, Loss, Discount & Faulty Weights**
  - Cost Price (CP), Selling Price (SP), Marked Price (MP), markup vs. margin, dishonest dealer (weight vs. price manipulation: $\text{Multiplying Factor} = \frac{\text{True Weight}}{\text{Actual Weight Given}}$), successive discounts, false scale formulas.
- **Simple & Compound Interest, Installments**
  - SI vs. CI 2-year difference $P\left(\frac{R}{100}\right)^2$ and 3-year difference $P\left(\frac{R}{100}\right)^2\left(3 + \frac{R}{100}\right)$, effective annual rate, present value of equal installments $P = \sum_{k=1}^n \frac{X}{(1+r)^k}$, continuous compounding limits.
- **Ratio, Proportion, Variation & Partnerships**
  - Componendo-Dividendo, $\frac{a}{b} = \frac{c}{d} = k \implies \frac{pa + qc}{pb + qd} = k$ equal ratio property, direct/inverse/joint variation ($y = ax + \frac{b}{x}$), time-weighted capital in partnerships.
- **Averages, Mixtures & Alligations**
  - Weighted average seesaw/lever rule $\frac{n_1}{n_2} = \frac{A_2 - A_{\text{avg}}}{A_{\text{avg}} - A_1}$, deviation from assumed mean, repeated replacement formula $C_{\text{final}} = C_0\left(1 - \frac{x}{V}\right)^n$, 3-component mixtures.
- **Time & Work, Pipes & Cisterns**
  - LCM efficiency method, $\frac{M_1 D_1 H_1}{W_1} = \frac{M_2 D_2 H_2}{W_2}$, alternating work cycles (positive + negative work final-turn wrap-around trap), efficiency-to-time inverse ratios.
- **Time, Speed & Distance (TSD)**
  - Proportional TSD ($D$ constant $\implies S \propto \frac{1}{T}$; $T$ constant $\implies D \propto S$), average speed (harmonic mean $\frac{2s_1 s_2}{s_1 + s_2}$ for equal distances), relative speed, trains/boats/streams, **Escalators** ($N_{\text{total}} = S_{\text{person}} \pm S_{\text{escalator}} \cdot t$), **Linear Races** (head-start in distance vs. time, dead heat), **Circular Tracks** (first meeting $\frac{L}{|v_1 \mp v_2|}$, meeting at starting point $\text{LCM}\left(\frac{L}{v_1}, \frac{L}{v_2}\right)$, number of distinct meeting points $|a \mp b|$ where $\frac{v_1}{v_2} = \frac{a}{b}$ in lowest terms).

### 2. Algebra (Weightage: ~30–35%)
- **Linear Equations & Indeterminate Systems**
  - Unique, infinite, or no solution conditions ($\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$, $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$), integer Diophantine equations ($ax + by = c$, non-negative integer solutions, stamp/coin Frobenius largest unattainable value $ab - a - b$).
- **Quadratic & Higher-Degree Polynomials**
  - Vieta's root-coefficient relations, nature of roots ($\Delta = b^2 - 4ac$, rational roots when $\Delta$ is a perfect square), location of roots on the number line ($af(k) > 0$, vertex $-\frac{b}{2a}$), common roots, reciprocal equations, Descartes' rule of signs, Remainder & Factor theorems.
- **Inequalities & Modulus**
  - Wavy curve method (even vs. odd multiplicity power sign-flip), AM-GM-HM inequality (equality condition + positive reals domain), Cauchy-Schwarz inequality, triangle inequality $|a \pm b|$, graphical optimization of $\sum_{i=1}^n |x - a_i|$ (minimum at the median), $|f(x)| + |g(x)| = |f(x) + g(x)| \iff f(x)g(x) \ge 0$, $|f(x)| + |g(x)| = |f(x) - g(x)| \iff f(x)g(x) \le 0$.
- **Logarithms, Surds & Indices**
  - Base-change rules $\log_b a = \frac{\ln a}{\ln b}$, strict domain conditions ($\text{base} > 0, \text{base} \neq 1, \text{argument} > 0$), characteristic & mantissa (number of digits $\lfloor \log_{10} N \rfloor + 1$ and leading zeros after decimal), nested radicals $\sqrt{a \pm 2\sqrt{b}} = |\sqrt{x} \pm \sqrt{y}|$.
- **Functions, Graphs & Functional Equations**
  - Domain & range, odd/even/periodic functions, inverse & composite functions $f(f(x))$, standard Cauchy functional equations:
    - $f(x+y) = f(x) + f(y) \implies f(x) = kx$
    - $f(x+y) = f(x)f(y) \implies f(x) = a^x$
    - $f(xy) = f(x) + f(y) \implies f(x) = k\log x$
    - $f(x) \cdot f(1/x) = f(x) + f(1/x) \implies f(x) = 1 \pm x^n$
  - Greatest integer $\lfloor x \rfloor$ and fractional part $\{x\} = x - \lfloor x \rfloor$.
- **Sequences & Series**
  - AP, GP, HP, Arithmetico-Geometric Progression (AGP), method of finite differences, telescoping series ($\frac{1}{k(k+d)} = \frac{1}{d}\left(\frac{1}{k} - \frac{1}{k+d}\right)$, factorials $k \cdot k! = (k+1)! - k!$), power sums $\sum k, \sum k^2, \sum k^3$.
- **Maxima & Minima**
  - Quadratic vertex $-\frac{\Delta}{4a}$, AM-GM with term splitting to balance variables ($x^2 + \frac{16}{x} = x^2 + \frac{8}{x} + \frac{8}{x}$), piecewise linear / modulus extrema.

### 3. Geometry & Mensuration (Weightage: ~15–20%)
- **Lines, Angles & Triangles**
  - Triangle inequality ($|a-b| < c < a+b$), acute/right/obtuse condition ($a^2 + b^2 \gtrless c^2$), similarity models (AA, parallel-line trapezium, right-triangle altitude $h^2 = pq$, $\frac{1}{h^2} = \frac{1}{a^2} + \frac{1}{b^2}$), Area formulas ($\frac{1}{2}ab\sin C$, Heron's $\sqrt{s(s-a)(s-b)(s-c)}$, $r \cdot s$, $\frac{abc}{4R}$), **4 Centers** (Incenter, Circumcenter, Centroid, Orthocenter & Euler line $OG : GH = 1 : 2$), **Angle Bisector Theorem** (length $l^2 = ab - pq$), **Apollonius Theorem**, **Stewart's Theorem**, **Ceva's & Menelaus' Theorems**, **Mass Point Geometry**.
- **Circles**
  - Chord properties, tangent-secant power of a point ($PT^2 = PA \cdot PB$), **Alternate Segment Theorem**, common tangents (direct $\sqrt{d^2 - (r_1-r_2)^2}$ vs. transverse $\sqrt{d^2 - (r_1+r_2)^2}$), cyclic quadrilaterals (Ptolemy's theorem $AC \cdot BD = AB \cdot CD + BC \cdot AD$, Brahmagupta's area $\sqrt{(s-a)(s-b)(s-c)(s-d)}$).
- **Quadrilaterals & Polygons**
  - Parallelogram ($d_1^2 + d_2^2 = 2(a^2 + b^2)$), rhombus, trapezium (mid-segment $\frac{a+b}{2}$, segment joining midpoints of diagonals $\frac{|a-b|}{2}$, diagonal triangle area ratios $1 : r : r : r^2$), regular polygons (interior angle $\frac{(n-2)180^\circ}{n}$, exterior angle $\frac{360^\circ}{n}$, diagonals $\frac{n(n-3)}{2}$, regular hexagon decomposition into 6 equilateral triangles of side $a$).
- **3D Mensuration & Solids**
  - Cube, cuboid, cylinder, cone, sphere, hemisphere, frustum of a cone ($V = \frac{1}{3}\pi h(R^2 + r^2 + Rr)$), prism, pyramid, regular tetrahedron ($h = \sqrt{\frac{2}{3}}a, V = \frac{\sqrt{2}}{12}a^3$), **inscribed/circumscribed 3D solids**, shortest surface path (unfolding net), cutting/painting cubes.
- **Coordinate Geometry & Trigonometry**
  - Distance, section formula, slope, line forms, distance of point from line $\frac{|ax_0 + by_0 + c|}{\sqrt{a^2+b^2}}$, reflection/foot of perpendicular across a line, area of polygon by shoelace formula, circle equations, trigonometric identities & heights/distances.

### 4. Number System (Weightage: ~5–10%)
- **Classification & Properties**
  - Primes, composites, odd/even parity, twin primes, $(6k \pm 1)$ prime form ($p > 3 \implies p^2 \equiv 1 \pmod{24}$), rational vs. irrational, recurring decimals to fractions.
- **Divisibility & Factor Theory**
  - Divisibility rules ($2^n, 3, 7, 9, 11, 13, 37, 73, 101$), prime factorization $N = p_1^a p_2^b \dots$, number of factors $(a+1)(b+1)\dots$, sum of factors, product of factors $N^{d(N)/2}$, odd/even/perfect-square factors, ways to write $N$ as product of two factors or difference of two squares ($a^2 - b^2 = N$).
- **HCF & LCM Models**
  - $\text{HCF} \times \text{LCM} = a \times b$, standard remainder models:
    - Same remainder $r$: $N = k \cdot \text{LCM}(d_1, d_2) + r$
    - Constant difference $(d_i - r_i) = c$: $N = k \cdot \text{LCM}(d_1, d_2) - c$
    - General case: Chinese Remainder Theorem (CRT) & step-march.
- **Remainders & Modular Arithmetic**
  - Negative remainders, Binomial theorem remainders, **Euler's Totient Theorem** ($a^{\phi(n)} \equiv 1 \pmod n$ for $\gcd(a,n)=1$), **Fermat's Little Theorem** ($a^{p-1} \equiv 1 \pmod p$), **Wilson's Theorem** ($(p-1)! \equiv -1 \pmod p$, $(p-2)! \equiv 1 \pmod p$).
- **Factorials, Base Systems & Digits**
  - Legendre's formula (highest power of prime $p$ in $n!$: $\sum_{k \ge 1} \lfloor \frac{n}{p^k} \rfloor = \frac{n - S_p(n)}{p - 1}$), trailing zeros in base $10$ and base $B$, cyclicity of unit digits, last two digits (odd endings $1, 3, 7, 9$ & even numbers via $2^{10} \equiv 24 / 76 \pmod{100}$), base conversion & base arithmetic.

### 5. Modern Math (Weightage: ~5–10%)
- **Permutations & Combinations**
  - Fundamental counting, gap method vs. tie/string method, arrangements with repetition, circular permutations $(n-1)!$, **Beggar's Method / Stars & Bars** ($\binom{n+r-1}{r-1}$ non-negative vs. $\binom{n-1}{r-1}$ positive integral solutions with upper/lower bounds), **Derangements** $D_n = n!\sum_{k=0}^n \frac{(-1)^k}{k!}$ ($D_1=0, D_2=1, D_3=2, D_4=9, D_5=44$), geometric counting (lines/triangles in grids/polygons, $\binom{m+1}{2}\binom{n+1}{2}$ rectangles vs. $\sum_{k=1}^{\min(m,n)}(m-k+1)(n-k+1)$ squares on $m \times n$ grid).
- **Probability**
  - Classical definition, complementary probability ($1 - P(\text{none})$), independent vs. mutually exclusive, **Conditional Probability & Bayes' Theorem**, Binomial distribution ($\binom{n}{r} p^r q^{n-r}$), geometric probability, expected value linearity $E[X+Y] = E[X] + E[Y]$.
- **Set Theory**
  - 2-set, 3-set, and 4-set inclusion-exclusion, **Set Theory Maxima & Minima** (surplus redistribution method).

---

## Section 2: Data Interpretation & Logical Reasoning (DILR)

### 1. Quantitative & Reasoning-Based DI
- Missing-value tables, percentage/ratio/index-number traps (base-year indexing vs. year-on-year change), CAGR vs. simple average growth, Non-standard charts (Radar/Spider, Scatter plots, Bubble charts, Stacked bars, Candlestick/High-Low-Open-Close charts, Cumulative vs. Periodic data traps).

### 2. Linear, Circular & 2D Matrix Arrangements
- Multi-variable attribute mapping, relative vs. absolute positioning, circular seating with facing inward/outward, bi-directional grid elimination, scheduling with slot/gap constraints.

### 3. Games & Tournaments
- **Knockout / Seeded Brackets**: Round of $2^k$, standard seeding where sum of seeds in round $r$ is $2^r + 1$, upset tracking, minimum/maximum seed that can reach finals or win under at most $u$ upsets.
- **Round-Robin Leagues**: $\binom{n}{2}$ matches, total wins = total losses, sum of points $= 2\binom{n}{2}$ (or $3\binom{n}{2} - \text{draws}$ in 3-2-0/3-1-0 systems), points table with bonus/tie/net-run-rate or goal-difference constraints, minimum points to **guarantee** qualification vs. minimum points to **possibly** qualify.

### 4. Venn Diagrams & Set Theory Optimization (3-Set & 4-Set)
- "Exactly $k$" ($E_1, E_2, E_3, E_4$) equation system:
  - $E_1 + E_2 + E_3 + E_4 = U - \text{None}$
  - $E_1 + 2E_2 + 3E_3 + 4E_4 = \sum |A_i|$
- Maximizing/minimizing specific regions or intersections under inequality constraints.

### 5. Networks, Routes, Flows & Project Scheduling
- Directed/undirected flow conservation ($\text{Total Inflow} = \text{Total Outflow} + \text{Node Demand}$), bottleneck/cut-set capacity, shortest/cheapest path, Critical Path Method (CPM) / task dependencies / slack time.

### 6. Quant-Based LR & Algorithmic Puzzles
- Coins/weights/counterfeits, cryptarithmetic, token/state-transition machines, sliding windows / moving averages, truth-teller/liar/alternator matrices, game theory (minimax / dominant strategy / backward induction).

---

## Section 3: Verbal Ability & Reading Comprehension (VARC)

### 1. Reading Comprehension (RC) — Passage Architecture & Genre Playbooks
- **Genres**: Philosophy & Epistemology, Economics & Public Policy, Evolutionary Biology & Science/Tech, Sociology/Anthropology/History, Art/Literature/Psychology.
- **Structural Mapping**: Author's thesis vs. counter-argument ("The Old View" vs. "The Author's Pivot"), concession markers (*admittedly, granted, while it is true*), tone calibration (critical vs. skeptical vs. analytical vs. acerbic vs. didactic).
- **RC Question Types & Option Elimination Matrix**:
  - *Main Idea / Primary Purpose* (Too narrow vs. too broad vs. secondary paragraph trap)
  - *Inference / Must-Be-True* (Strict textual entailment vs. plausible real-world leap)
  - *Critical Reasoning in RC* (Strengthen, Weaken, Necessary Assumption, Flaw in reasoning, Paradox resolution)
  - *Tone / Attitude & Application / Analogy*
- **The 7 Deadly RC Distractor Archetypes**:
  1. **Extreme Quantifier Trap** (*always, never, only, completely, impossible, exclusively*)
  2. **Unauthorized Comparison Trap** (passage states $A$ is high and $B$ is high; option claims $A > B$)
  3. **Causal Reversal / Correlation-as-Causation Trap**
  4. **True-in-Passage but Answers Wrong Question** (Right Line, Wrong Question)
  5. **Half-Right, Half-Poisoned Option** (first clause matches passage verbatim; last 3 words twist the claim)
  6. **Scope Shift** (Descriptive *is* $\to$ Normative *should/must*; *Some* $\to$ *Most*)
  7. **Alien / Out-of-Scope Concept** (uses outside domain knowledge not grounded in text)

### 2. Verbal Ability (VA) — TITA & MCQ Frameworks
- **Para-Jumbles (TITA 4-Sentence)**: Opening sentence identification (independent thesis/premise), mandatory pairs (Pronoun-Antecedent, Acronym-Full Form, Demonstrative `this/these/such`, Chronology, General-to-Specific, Contrast pivots), closing vs. continuation checks.
- **Odd-One-Out (TITA)**: Identifying the 4-sentence coherent para-jumble first; spotting the outlier sentence that shares *keywords* but shifts *aspect, time frame, scale, or thesis*.
- **Para-Summary (MCQ)**: 3-Point Check — *Captures Main Claim + Preserves Author's Tone + Excludes Minor Examples/New Inferences*.
- **Para-Completion / Sentence Placement (4-Slot Gap)**: Pre-gap & post-gap logical bridge, pronoun/reference continuity, contrast/elaboration flow.
