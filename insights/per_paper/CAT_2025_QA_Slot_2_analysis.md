# Pass 1 Master Analysis: CAT 2025 QA Slot 2

## 1. Executive Summary & Exam-Hall Blueprint
- **Section**: QA | **Slot**: Slot 2 (CAT 2025)
- **Source Document**: `docs/pyqs/2025/CAT_2025_QA_slot_2_3__00ee9a29f11dd991be713a852ccdf9c1.pdf`
- **Total Questions**: 22 (15 MCQs, 7 TITA)
- **Difficulty Breakdown**: Easy: **13** | Medium: **9** | Hard: **0**
- **Round-Wise Triage**: Round 1 Sitters: **20** | Round 2 Doables: **2** | Round 3 Time-Sinks: **0**
- **Answer Verification Protocol**: 3-Layer Autonomous Verification (`ai_verified_derivation` — First-Principles Algebraic/Logical Derivation + Programmatic/Cross-Clue Verification + 30-Second Speed Shortcut)

### Percentile Score & Attempt Targets (40-Minute Clock)
| Percentile Target | Scaled Raw Score Target | Net Correct Equivalent | Recommended Execution Strategy |
| :---: | :---: | :---: | :--- |
| **95%ile** | 26-29 (9-10 net) | ~9-11 questions | Clear all Easy Round-1 sitters + all TITA questions with zero negative risk |
| **99%ile** | 37-40 (12-13 net) | ~12-15 questions | Sweep Round 1 in 22 mins + cherry-pick 4-5 Round 2 medium questions |
| **99.5%ile** | 43-46 (14-15 net) | ~15-17 questions | Full Round 1 sweep + 70% of Round 2 using option/parity/invariant shortcuts |
| **99.9%ile** | 51+ (17+ net) | ~17-19 questions | Complete mastery of Round 1 + Round 2 with <90s average per sitter |

### Topic & Sub-Topic Distribution
| Canonical Topic | Canonical Sub-Topic | Question Count | Question IDs |
| :--- | :--- | :---: | :--- |
| **Algebra** | Functions, Graphs & Functional Equations | 1 | Q15 |
| **Algebra** | Inequalities & Modulus | 1 | Q11 |
| **Algebra** | Maxima & Minima | 2 | Q7, Q23 |
| **Algebra** | Quadratic & Higher-Degree Polynomials | 2 | Q8, Q12 |
| **Algebra** | Sequences & Series | 1 | Q2 |
| **Arithmetic** | Averages, Mixtures & Alligations | 2 | Q9, Q21 |
| **Arithmetic** | Percentages & Successive Change | 1 | Q14 |
| **Arithmetic** | Profit, Loss, Discount & Faulty Weights | 1 | Q13 |
| **Arithmetic** | Ratio, Proportion, Variation & Partnerships | 1 | Q6 |
| **Arithmetic** | Simple & Compound Interest, Installments | 1 | Q10 |
| **Arithmetic** | Time & Work, Pipes & Cisterns | 1 | Q18 |
| **Arithmetic** | Time, Speed & Distance (TSD) | 1 | Q22 |
| **Geometry & Mensuration** | Circles | 1 | Q3 |
| **Geometry & Mensuration** | Lines, Angles & Triangles | 1 | Q20 |
| **Geometry & Mensuration** | Quadrilaterals & Polygons | 1 | Q4 |
| **Number System** | Divisibility & Factor Theory | 3 | Q5, Q16, Q19 |
| **Number System** | Factorials, Base Systems & Digits | 1 | Q17 |

---

## 2. Quick-Reference Verified Answer Key
| Q# | Question ID | Type | Difficulty | Round Tag | Verified Answer | Core Concept / Mental Trigger |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| **Q2** | `CAT2025_S2_QA_Q01` | MCQ | Easy | `Round_1_Sitter` | **(C) 54** | Three-term GP symmetric identity a1*a2 + a2*a3 + a3*a1 = a2*(a1 + a2 + a3) |
| **Q3** | `CAT2025_S2_QA_Q02` | TITA | Easy | `Round_1_Sitter` | **80** | Third-tangent theorem for angle subtended at the center of a circle |
| **Q4** | `CAT2025_S2_QA_Q03` | MCQ | Medium | `Round_1_Sitter` | **(B) 5 : 24** | Regular hexagon decomposition into equilateral triangles and midline scaling |
| **Q5** | `CAT2025_S2_QA_Q04` | TITA | Medium | `Round_1_Sitter` | **12** | Diophantine divisibility optimization over distinct natural numbers |
| **Q6** | `CAT2025_S2_QA_Q05` | MCQ | Easy | `Round_1_Sitter` | **(B) 3 : 5** | Chained ratio scaling with Income = Expenditure + Savings |
| **Q7** | `CAT2025_S2_QA_Q06` | MCQ | Medium | `Round_1_Sitter` | **(D) 48** | Logarithm base reduction to powers of 2 combined with 3-variable AM-GM inequality |
| **Q8** | `CAT2025_S2_QA_Q07` | MCQ | Medium | `Round_1_Sitter` | **(D) 20** | Exponential quadratic substitution and Vieta product of roots |
| **Q9** | `CAT2025_S2_QA_Q08` | TITA | Easy | `Round_1_Sitter` | **49** | Sliding-window average difference (Sum(1..9) - Sum(2..9) = Day 1) |
| **Q10** | `CAT2025_S2_QA_Q09` | MCQ | Easy | `Round_1_Sitter` | **(C) 8%** | Two-year compound interest amortization schedule |
| **Q11** | `CAT2025_S2_QA_Q10` | MCQ | Easy | `Round_1_Sitter` | **(C) (-inf, -3) U (3, inf)** | Piecewise modulus quadratic inequality |
| **Q12** | `CAT2025_S2_QA_Q11` | MCQ | Medium | `Round_1_Sitter` | **(C) 8/3 - p + (3/2)q** | Common root elimination and Vieta sum of roots |
| **Q13** | `CAT2025_S2_QA_Q12` | MCQ | Easy | `Round_1_Sitter` | **(C) 14** | Linear sensitivity of profit to discount doubling and equal profit-discount rate equilibrium |
| **Q14** | `CAT2025_S2_QA_Q13` | MCQ | Easy | `Round_1_Sitter` | **(B) 5 : 8** | Successive remainder percentages |
| **Q15** | `CAT2025_S2_QA_Q14` | MCQ | Easy | `Round_1_Sitter` | **(D) -1, 1/2, 1** | Domain of sum of composite rational functions |
| **Q16** | `CAT2025_S2_QA_Q15` | MCQ | Medium | `Round_2_Doable` | **(A) 42** | Modular residue classification of divisors (d == 1 mod 3) |
| **Q17** | `CAT2025_S2_QA_Q16` | TITA | Easy | `Round_1_Sitter` | **25** | Pairing powers of 2 and 5 into trailing zeros 10^k |
| **Q18** | `CAT2025_S2_QA_Q17` | TITA | Easy | `Round_1_Sitter` | **340** | Relative efficiency assignment in Time & Work |
| **Q19** | `CAT2025_S2_QA_Q18` | MCQ | Medium | `Round_1_Sitter` | **(D) 17** | Integer factor-pair decomposition with negative factor pairs |
| **Q20** | `CAT2025_S2_QA_Q19` | MCQ | Medium | `Round_2_Doable` | **(B) 11 : 4** | Mass Point Geometry / Menelaus theorem on intersecting cevians |
| **Q21** | `CAT2025_S2_QA_Q20` | MCQ | Easy | `Round_1_Sitter` | **(B) 5** | Linear interpolation of mixture cost vs concentration |
| **Q22** | `CAT2025_S2_QA_Q21` | TITA | Easy | `Round_1_Sitter` | **8** | Boats and streams upstream-downstream time difference and round-trip harmonic speed |
| **Q23** | `CAT2025_S2_QA_Q22` | TITA | Medium | `Round_1_Sitter` | **2** | Discrete integer sum-of-squares minimization under modular sum constraint |

---

## 3. Question-by-Question High-Recall Decomposition (Dual-Method)

### Q2 (`CAT2025_S2_QA_Q01`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Sequences & Series*
- **Core Concept Tested**: Three-term GP symmetric identity a1*a2 + a2*a3 + a3*a1 = a2*(a1 + a2 + a3)
- **Verified Answer**: **(C) 54** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: For ANY 3 consecutive GP terms, a1*a2 + a2*a3 + a3*a1 = a2*(a1 + a2 + a3), so divide the two given sums immediately to get a2 = 624/52 = 12!
- **Method 1 (First-Principles Derivation)**: Let the GP be a, ar, ar^2 with 0 < r < 1. Since a1*a2 + a2*a3 + a3*a1 = ar(a + ar + ar^2), we get ar = 624/52 = 12. Then a + ar^2 = 52 - 12 = 40 => 12/r + 12r = 40 => r = 1/3, a = 36. Infinite sum S = 36/(1 - 1/3) = 54.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Once a2 = 12 and a1 + a3 = 40, spot 36 + 4 = 40 with 36*4 = 12^2 => a1 = 36, r = 1/3 => S = 36 * (3/2) = 54.
- **Boundary Conditions & Trap Alert**: Since the GP is decreasing, choose r = 1/3 (not r = 3, for which the infinite sum diverges).
- **Verification Audit**: In GP a, ar, ar^2: a(1 + r + r^2) = 52 and a^2*r*(1 + r + r^2) = 624. Dividing gives a*r = 12. Then 12/r + 12 + 12r = 52 => 3r^2 - 10r + 3 = 0 => r = 1/3 (decreasing GP), a = 36. Sum = a/(1 - r) = 36/(2/3) = 54.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q01</summary>

- **Trigger**: For ANY 3 consecutive GP terms, a1*a2 + a2*a3 + a3*a1 = a2*(a1 + a2 + a3), so divide the two given sums immediately to get a2 = 624/52 = 12!
- **Answer**: **(C) 54**
- **Trap to Avoid**: Since the GP is decreasing, choose r = 1/3 (not r = 3, for which the infinite sum diverges).
</details>

### Q3 (`CAT2025_S2_QA_Q02`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Geometry & Mensuration $\rightarrow$ *Circles*
- **Core Concept Tested**: Third-tangent theorem for angle subtended at the center of a circle
- **Verified Answer**: **80** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: When tangent segment AB intercepted between two tangents PQ and PR subtends angle AOB at center O, use angle AOB = 90 - (1/2) angle APB => angle APB = 180 - 2 * angle AOB.
- **Method 1 (First-Principles Derivation)**: Let AB touch the circle at M. By tangent symmetry, triangle OQA is congruent to triangle OMA and triangle ORB is congruent to triangle OMB. Thus angle QOR = 2 * angle AOB = 100 deg. Since OQ perp PQ and OR perp PR, angle APB = 180 - 100 = 80 deg.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Apply the standard identity angle APB = 180 - 2(50) = 80 in 5 seconds.
- **Boundary Conditions & Trap Alert**: Do not confuse angle AOB (50 deg) with angle QOR (100 deg); taking 180 - 50 = 130 is the classic trap.
- **Verification Audit**: Let AB touch the circle at M. Then OA bisects angle QOM and OB bisects angle ROM, so angle QOR = 2 * angle AOB = 100 deg. In quadrilateral PQOR, angle OQP = angle ORP = 90 deg, so angle APB = 180 - angle QOR = 80 deg.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q02</summary>

- **Trigger**: When tangent segment AB intercepted between two tangents PQ and PR subtends angle AOB at center O, use angle AOB = 90 - (1/2) angle APB => angle APB = 180 - 2 * angle AOB.
- **Answer**: **80**
- **Trap to Avoid**: Do not confuse angle AOB (50 deg) with angle QOR (100 deg); taking 180 - 50 = 130 is the classic trap.
</details>

### Q4 (`CAT2025_S2_QA_Q03`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Geometry & Mensuration $\rightarrow$ *Quadrilaterals & Polygons*
- **Core Concept Tested**: Regular hexagon decomposition into equilateral triangles and midline scaling
- **Verified Answer**: **(B) 5 : 24** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: In a regular hexagon of side 2a, the long diagonal CF has length 4a; since P and Q are midpoints of AB and CD, PQ is the mid-segment of trapezium ABCF, so PQ = (2a + 4a)/2 = 3a!
- **Method 1 (First-Principles Derivation)**: Half the hexagon (trapezium ABCF) has parallel sides AB = 2a and CF = 4a, and area = 3 equilateral triangles = 12 sub-triangles. Since P and Q are midpoints of the slant sides AB and CD (symmetric to BC and AD), PQ has length (2a + 3a)... wait: BC = 2a, AD = 4a, and P, Q are midpoints of AB, CD, so PQ is the midline of trapezium ABCD! Thus PQ = (BC + AD)/2 = 3a, height is half the height of ABCD, and Area(PBCQ)/Area(ABCD) = ((2a + 3a)/2) / ((2a + 4a)/2) * (1/2) = 5/12 of half-hexagon = 5/24 of full hexagon!
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Trapezium ABCD is half the hexagon (12/24). Midline PQ divides trapezium ABCD (bases 2 and 4, midline 3) into two strips of area ratio (2+3) : (3+4) = 5 : 7. So PBCQ is (5/12) * (1/2) = 5/24 of the hexagon!
- **Boundary Conditions & Trap Alert**: Remember trapezium ABCD is HALF the hexagon (not the whole hexagon), so multiply 5/12 by 1/2 to get 5/24.
- **Verification Audit**: Set regular hexagon side = 2. Area(ABCDEF) = 6 * sqrt(3). In trapezium PBCQ, BC = 2, PB = QC = 1, interior angles at B and C are 120 deg, so PQ = 2 + 2*(1*cos 60) = 3 and height h = 1*sin 60 = sqrt(3)/2. Area(PBCQ) = 0.5*(2 + 3)*(sqrt(3)/2) = (5/4)*sqrt(3). Ratio = (5/4) : 6 = 5 : 24.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q03</summary>

- **Trigger**: In a regular hexagon of side 2a, the long diagonal CF has length 4a; since P and Q are midpoints of AB and CD, PQ is the mid-segment of trapezium ABCF, so PQ = (2a + 4a)/2 = 3a!
- **Answer**: **(B) 5 : 24**
- **Trap to Avoid**: Remember trapezium ABCD is HALF the hexagon (not the whole hexagon), so multiply 5/12 by 1/2 to get 5/24.
</details>

### Q5 (`CAT2025_S2_QA_Q04`) — [TITA | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Number System $\rightarrow$ *Divisibility & Factor Theory*
- **Core Concept Tested**: Diophantine divisibility optimization over distinct natural numbers
- **Verified Answer**: **12** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Isolate b = a(3c - 8)/8; since b > 0, c >= 3. Test c = 3 and c = 4 to minimize a!
- **Method 1 (First-Principles Derivation)**: Rewrite 3ac = 8(a + b) as 8b = a(3c - 8). Since b >= 1, 3c - 8 >= 1 => c >= 3. If c = 3, 8b = a => smallest distinct (a,b,c) is (8,1,3) giving 3(8)+2(1)+3 = 29. If c = 4, 8b = 4a => a = 2b => smallest distinct (a,b,c) is (2,1,4), giving 3(2)+2(1)+4 = 12.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: To make a small in 8b = a(3c - 8), pick 3c - 8 to share a large factor with 8: 3c - 8 = 4 (c = 4) gives a = 2, b = 1 -> 3(2) + 2(1) + 4 = 12.
- **Boundary Conditions & Trap Alert**: Check that a, b, c are DISTINCT: (2, 1, 4) has three distinct natural numbers.
- **Verification Audit**: 3ac = 8(a + b) => b = a(3c - 8)/8. Since a, b, c >= 1 are distinct natural numbers, we need 3c > 8 => c >= 3. For c = 3: b = a/8 => a = 8, b = 1, c = 3 gives 3a + 2b + c = 29. For c = 4: b = 4a/8 = a/2 => a = 2, b = 1, c = 4 (all distinct!) gives 3(2) + 2(1) + 4 = 12.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q04</summary>

- **Trigger**: Isolate b = a(3c - 8)/8; since b > 0, c >= 3. Test c = 3 and c = 4 to minimize a!
- **Answer**: **12**
- **Trap to Avoid**: Check that a, b, c are DISTINCT: (2, 1, 4) has three distinct natural numbers.
</details>

### Q6 (`CAT2025_S2_QA_Q05`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Ratio, Proportion, Variation & Partnerships*
- **Core Concept Tested**: Chained ratio scaling with Income = Expenditure + Savings
- **Verified Answer**: **(B) 3 : 5** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Since E_L : E_M = 2 : 3 and I_L : E_M = 6 : 7, scale E_M to LCM(3, 7) = 21 so all quantities are integers!
- **Method 1 (First-Principles Derivation)**: Let E_M = 21k. Then E_L = 14k and I_L = 18k. Lakshmi's savings S_L = 18k - 14k = 4k. Since S_L : S_M = 4 : 9, S_M = 9k. Meenakshi's income I_M = E_M + S_M = 21k + 9k = 30k. Ratio I_L : I_M = 18k : 30k = 3 : 5.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: With E_M = 21, E_L = 14, I_L = 18 => S_L = 4 => S_M = 9 => I_M = 30 => 18:30 = 3:5.
- **Boundary Conditions & Trap Alert**: Read carefully that 6 : 7 is the ratio of Income of Lakshmi to Expenditure of Meenakshi (not Income of Lakshmi to Income of Meenakshi).
- **Verification Audit**: Set E_L = 14, E_M = 21 (ratio 2:3). Then I_L = (6/7)*E_M = 18. Saving S_L = I_L - E_L = 18 - 14 = 4. Since S_L : S_M = 4 : 9, S_M = 9. Thus I_M = E_M + S_M = 21 + 9 = 30. Ratio I_L : I_M = 18 : 30 = 3 : 5.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q05</summary>

- **Trigger**: Since E_L : E_M = 2 : 3 and I_L : E_M = 6 : 7, scale E_M to LCM(3, 7) = 21 so all quantities are integers!
- **Answer**: **(B) 3 : 5**
- **Trap to Avoid**: Read carefully that 6 : 7 is the ratio of Income of Lakshmi to Expenditure of Meenakshi (not Income of Lakshmi to Income of Meenakshi).
</details>

### Q7 (`CAT2025_S2_QA_Q06`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Maxima & Minima*
- **Core Concept Tested**: Logarithm base reduction to powers of 2 combined with 3-variable AM-GM inequality
- **Verified Answer**: **(D) 48** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Bases 64 = 2^6, 8 = 2^3, 512 = 2^9 are all powers of 2; convert immediately to log_2 and apply AM >= GM.
- **Method 1 (First-Principles Derivation)**: (1/3)log_2(x) + (1/6)log_2(y) + (1/3)log_2(y^(1/2)*z) = (1/3)log_2(xyz) = 4 => log_2(xyz) = 12 => xyz = 2^12. For positive reals, (x + y + z)/3 >= (xyz)^(1/3) = 2^4 = 16, so min(x + y + z) = 48 at x = y = z = 16.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Symmetric minimum among options (24, 36, 96, 48) is 3 * 2^k = 3 * 16 = 48.
- **Boundary Conditions & Trap Alert**: Note that in 3*log_512(sqrt(y)*z), the radical covers y only, making the final log product symmetric in x, y, z.
- **Verification Audit**: Convert all logs to base 2 (64=2^6, 8=2^3, 512=2^9): (2/6)log_2(x) + (1/6)log_2(y) + (3/9)log_2(sqrt(y)*z) = (1/3)log_2(x) + (1/6)log_2(y) + (1/6)log_2(y) + (1/3)log_2(z) = (1/3)log_2(xyz) = 4 => xyz = 2^12. By AM-GM, x + y + z >= 3*(xyz)^(1/3) = 3 * 2^4 = 48.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q06</summary>

- **Trigger**: Bases 64 = 2^6, 8 = 2^3, 512 = 2^9 are all powers of 2; convert immediately to log_2 and apply AM >= GM.
- **Answer**: **(D) 48**
- **Trap to Avoid**: Note that in 3*log_512(sqrt(y)*z), the radical covers y only, making the final log product symmetric in x, y, z.
</details>

### Q8 (`CAT2025_S2_QA_Q07`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Quadratic & Higher-Degree Polynomials*
- **Core Concept Tested**: Exponential quadratic substitution and Vieta product of roots
- **Verified Answer**: **(D) 20** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Write 3^(x^2+2x-2) = 3 * 3^(x^2+2x-3) so the equation becomes u^2 - 12u + 27 = 0.
- **Method 1 (First-Principles Derivation)**: Substitute u = 3^(x^2+2x-3) into 9^(x^2+2x-3) - 4*3^(x^2+2x-2) + 27 = 0 to get u^2 - 12u + 27 = 0 => (u - 3)(u - 9) = 0. Equating exponents gives x^2 + 2x - 4 = 0 (Delta = 20 > 0, root product = -4) and x^2 + 2x - 5 = 0 (Delta = 24 > 0, root product = -5). Total product = (-4)(-5) = 20.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Once x^2 + 2x - 3 in {1, 2}, the constant terms of x^2 + 2x - (3+k) = 0 are -4 and -5; their product is (-4)(-5) = 20.
- **Boundary Conditions & Trap Alert**: Always verify Discriminant > 0 for both quadratic branches before multiplying Vieta root products.
- **Verification Audit**: Let u = 3^(x^2+2x-3). Then u^2 - 12u + 27 = 0 => u = 3 or u = 9. Thus x^2 + 2x - 3 = 1 (x^2 + 2x - 4 = 0, product of roots = -4) or x^2 + 2x - 3 = 2 (x^2 + 2x - 5 = 0, product of roots = -5). Product of all 4 real roots = (-4)*(-5) = 20.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q07</summary>

- **Trigger**: Write 3^(x^2+2x-2) = 3 * 3^(x^2+2x-3) so the equation becomes u^2 - 12u + 27 = 0.
- **Answer**: **(D) 20**
- **Trap to Avoid**: Always verify Discriminant > 0 for both quadratic branches before multiplying Vieta root products.
</details>

### Q9 (`CAT2025_S2_QA_Q08`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Averages, Mixtures & Alligations*
- **Core Concept Tested**: Sliding-window average difference (Sum(1..9) - Sum(2..9) = Day 1)
- **Verified Answer**: **49** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Day 8 raises the 7-day average from 60 to 63 (+3 across 8 days) => Day 8 = 60 + 8*3 = 84; then shifting the 8-day window from (1..8) to (2..9) raises average from 63 to 66 (+3 across 8 days) => Day 9 - Day 1 = 8*3 = 24!
- **Method 1 (First-Principles Derivation)**: S_7 = 420, S_8 = 504 => d_8 = 84 => d_9 = 73. Also S_{2..9} = 8 * 66 = 528. Therefore d_1 = S_8 + d_9 - S_{2..9} = 504 + 73 - 528 = 49.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: d_8 = 60 + 8(3) = 84 => d_9 = 73. Window shift (2..9) vs (1..8): d_9 - d_1 = 8(66 - 63) = 24 => d_1 = 73 - 24 = 49!
- **Boundary Conditions & Trap Alert**: Days 2 to 9 inclusive is 8 days (not 7 or 9 days).
- **Verification Audit**: Sum(1..7) = 420, Sum(1..8) = 504 => Day 8 = 84. Day 9 = 84 - 11 = 73. Sum(1..9) = 504 + 73 = 577. Given Sum(2..9) = 8 * 66 = 528. Thus Day 1 = 577 - 528 = 49.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q08</summary>

- **Trigger**: Day 8 raises the 7-day average from 60 to 63 (+3 across 8 days) => Day 8 = 60 + 8*3 = 84; then shifting the 8-day window from (1..8) to (2..9) raises average from 63 to 66 (+3 across 8 days) => Day 9 - Day 1 = 8*3 = 24!
- **Answer**: **49**
- **Trap to Avoid**: Days 2 to 9 inclusive is 8 days (not 7 or 9 days).
</details>

### Q10 (`CAT2025_S2_QA_Q09`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Simple & Compound Interest, Installments*
- **Core Concept Tested**: Two-year compound interest amortization schedule
- **Verified Answer**: **(C) 8%** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Notice 594 = 550 * 1.08 and 1000 * 1.08 - 530 = 550! Always test Year-1 balance (1000*(1+r) - 530)*(1+r) = 594.
- **Method 1 (First-Principles Derivation)**: After 1 year at rate r, balance is 1000(1 + r) - 530. After 2 years, (1000(1 + r) - 530)(1 + r) = 594. Testing r = 0.08 gives (1080 - 530)(1.08) = 550 * 1.08 = 594.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Factor 594 = 54 * 11 = 27 * 22. Since 1 + r = 1 + R/100 has factor 27 when R = 8 (1.08 = 27/25), R = 8% is immediate!
- **Boundary Conditions & Trap Alert**: Never equate simple sum of installments to 1000*(1+r)^2; each installment is discounted by its own time period.
- **Verification Audit**: Present value equation: 530/(1+r) + 594/(1+r)^2 = 1000. At r = 8% (1+r = 1.08): after Year 1, principal 1000 grows to 1080; paying 530 leaves 550; after Year 2, 550 * 1.08 = 594, which is paid off exactly!

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q09</summary>

- **Trigger**: Notice 594 = 550 * 1.08 and 1000 * 1.08 - 530 = 550! Always test Year-1 balance (1000*(1+r) - 530)*(1+r) = 594.
- **Answer**: **(C) 8%**
- **Trap to Avoid**: Never equate simple sum of installments to 1000*(1+r)^2; each installment is discounted by its own time period.
</details>

### Q11 (`CAT2025_S2_QA_Q10`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Inequalities & Modulus*
- **Core Concept Tested**: Piecewise modulus quadratic inequality
- **Verified Answer**: **(C) (-inf, -3) U (3, inf)** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Test x = -4 (gives 16 - 5 - 4 = 7 > 0) and x = -10 (gives 100 - 1 - 10 = 89 > 0) to eliminate 3 options in 10 seconds!
- **Method 1 (First-Principles Derivation)**: For x >= -9, |x + 9| = x + 9, so x^2 - x - 9 + x = x^2 - 9 > 0 => x in [-9, -3) U (3, inf). For x < -9, |x + 9| = -x - 9, so x^2 + 2x + 9 = (x+1)^2 + 8 > 0 for all x < -9. Combining both regions gives (-inf, -3) U (3, inf).
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Plug x = -4: 16 - 5 - 4 = 7 > 0 (eliminates A). Plug x = 4: 16 - 13 + 4 = 7 > 0 (eliminates B). Plug x = -10: 100 - 1 - 10 = 89 > 0 (eliminates D). Only (C) remains!
- **Boundary Conditions & Trap Alert**: Students who forget to include the x < -9 branch pick distractor (A) or (D).
- **Verification Audit**: Case 1 (x >= -9): x^2 - (x + 9) + x > 0 => x^2 - 9 > 0 => x in [-9, -3) U (3, inf). Case 2 (x < -9): x^2 + (x + 9) + x > 0 => (x + 1)^2 + 8 > 0, which holds for all x < -9. Union is (-inf, -3) U (3, inf).

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q10</summary>

- **Trigger**: Test x = -4 (gives 16 - 5 - 4 = 7 > 0) and x = -10 (gives 100 - 1 - 10 = 89 > 0) to eliminate 3 options in 10 seconds!
- **Answer**: **(C) (-inf, -3) U (3, inf)**
- **Trap to Avoid**: Students who forget to include the x < -9 branch pick distractor (A) or (D).
</details>

### Q12 (`CAT2025_S2_QA_Q11`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Quadratic & Higher-Degree Polynomials*
- **Core Concept Tested**: Common root elimination and Vieta sum of roots
- **Verified Answer**: **(C) 8/3 - p + (3/2)q** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Eliminate r^2 between 3r^2 - 5r + p = 0 and 2r^2 - 2r + q = 0 to get 2r directly in terms of p and q!
- **Method 1 (First-Principles Derivation)**: Let r be the common root, and r1, r2 the other roots. From Vieta, (r + r1) + (r + r2) = 5/3 + 1 = 8/3 => r1 + r2 = 8/3 - 2r. Since 2(3r^2 - 5r + p) - 3(2r^2 - 2r + q) = -4r + 2p - 3q = 0, we have 2r = p - (3/2)q. Substituting gives r1 + r2 = 8/3 - p + (3/2)q.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Set common root r = 0 => p = 0, q = 0, and other roots are 5/3 and 1, summing to 8/3 (eliminates A and D). Set r = 1 => p = 2, q = 0, other roots are 2/3 and 0, summing to 2/3. Plug p=2, q=0 into (B) 14/3 vs (C) 2/3 -> (C) wins!
- **Boundary Conditions & Trap Alert**: Setting r = 0 and r = 1 solves any parametric common-root MCQ in under 15 seconds.
- **Verification Audit**: Let common root be r. By Vieta, the other roots are (5/3 - r) and (1 - r), whose sum is 8/3 - 2r. Also 3r^2 - 5r + p = 0 and 2r^2 - 2r + q = 0. Eliminate r^2: 2(3r^2 - 5r + p) - 3(2r^2 - 2r + q) = 0 => -4r + 2p - 3q = 0 => 2r = p - (3/2)q. Thus sum of other roots = 8/3 - p + (3/2)q.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q11</summary>

- **Trigger**: Eliminate r^2 between 3r^2 - 5r + p = 0 and 2r^2 - 2r + q = 0 to get 2r directly in terms of p and q!
- **Answer**: **(C) 8/3 - p + (3/2)q**
- **Trap to Avoid**: Setting r = 0 and r = 1 solves any parametric common-root MCQ in under 15 seconds.
</details>

### Q13 (`CAT2025_S2_QA_Q12`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Profit, Loss, Discount & Faulty Weights*
- **Core Concept Tested**: Linear sensitivity of profit to discount doubling and equal profit-discount rate equilibrium
- **Verified Answer**: **(C) 14** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Doubling the discount reduces SP (and profit) by exactly 1x the original discount D; then for Profit% = Discount% = k%, use k = 100*(MP - CP)/(MP + CP)!
- **Method 1 (First-Principles Derivation)**: Initial profit = 0.20 * 1650 = 330. Doubling discount reduces profit from 330 to 110, so initial discount D = 220 and MP = 1650 + 330 + 220 = 2200. Equating CP(1 + k/100) = MP(1 - k/100) gives k = 100*(2200 - 1650)/(2200 + 1650) = 100/7 = 14.285%, nearest to 14.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Universal identity: Profit% = Discount% = k% <=> k = 100*(MP - CP)/(MP + CP) = 100*(4 - 3)/(4 + 3) = 100/7 = 14.28%.
- **Boundary Conditions & Trap Alert**: Remember profit% is on CP (1650) while discount% is on MP (2200).
- **Verification Audit**: CP = 1650. Initial profit = 20% of 1650 = 330 (SP = 1980). When discount is doubled, profit drops to 110, so discount amount = 330 - 110 = 220, and MP = 1980 + 220 = 2200. For profit% = discount% = k%: 1650(1 + k/100) = 2200(1 - k/100) => 3(100 + k) = 4(100 - k) => 7k = 100 => k = 14.29% -> 14.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q12</summary>

- **Trigger**: Doubling the discount reduces SP (and profit) by exactly 1x the original discount D; then for Profit% = Discount% = k%, use k = 100*(MP - CP)/(MP + CP)!
- **Answer**: **(C) 14**
- **Trap to Avoid**: Remember profit% is on CP (1650) while discount% is on MP (2200).
</details>

### Q14 (`CAT2025_S2_QA_Q13`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Percentages & Successive Change*
- **Core Concept Tested**: Successive remainder percentages
- **Verified Answer**: **(B) 5 : 8** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Set Total = 100 and compute shares sequentially: P = 20, M = 32, S = 16 => R = 32.
- **Method 1 (First-Principles Derivation)**: With Total = 100, P = 20, M = 0.40 * (100 - 20) = 32, S = 0.80 * 20 = 16, leaving R = 100 - 68 = 32. Thus P : R = 20 : 32 = 5 : 8.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 10-second mental arithmetic with Total = 100 -> 20 : 32 = 5 : 8.
- **Boundary Conditions & Trap Alert**: Meena gets 40% of the REMAINING amount (40% of 80 = 32), not 40% of total.
- **Verification Audit**: Assume Total = 100. Pinu = 20. Remaining = 80; Meena = 40% of 80 = 32. Seema = 0.8 * 20 = 16. Rinu = 100 - (20 + 32 + 16) = 32. Ratio Pinu : Rinu = 20 : 32 = 5 : 8.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q13</summary>

- **Trigger**: Set Total = 100 and compute shares sequentially: P = 20, M = 32, S = 16 => R = 32.
- **Answer**: **(B) 5 : 8**
- **Trap to Avoid**: Meena gets 40% of the REMAINING amount (40% of 80 = 32), not 40% of total.
</details>

### Q15 (`CAT2025_S2_QA_Q14`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Functions, Graphs & Functional Equations*
- **Core Concept Tested**: Domain of sum of composite rational functions
- **Verified Answer**: **(D) -1, 1/2, 1** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: For h(x) = f(g(x)) + g(f(x)), exclude singularities of inner functions (x = 1/2, x = 1) AND pre-images where inner function equals outer singularity (g(x) = 1/2 and f(x) = 1).
- **Method 1 (First-Principles Derivation)**: Singularities are: (1) 2x - 1 = 0 => x = 1/2; (2) x - 1 = 0 => x = 1; (3) 2*g(x) - 1 = 0 => 2x/(x-1) = 1 => x = -1; (4) f(x) - 1 = 0 => x/(2x-1) = 1 => x = 1. Total excluded set: {-1, 1/2, 1}.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Solve x/(x-1) = 1/2 => 2x = x - 1 => x = -1. Only Option (D) contains -1!
- **Boundary Conditions & Trap Alert**: Never simplify a composite fraction before recording the denominator exclusions of the inner function.
- **Verification Audit**: f(x) = x/(2x-1) excludes x = 1/2; g(x) = x/(x-1) excludes x = 1. Composite f(g(x)) additionally excludes g(x) = 1/2 => x/(x-1) = 1/2 => x = -1; composite g(f(x)) excludes f(x) = 1 => x/(2x-1) = 1 => x = 1. Union of excluded points is {-1, 1/2, 1}.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q14</summary>

- **Trigger**: For h(x) = f(g(x)) + g(f(x)), exclude singularities of inner functions (x = 1/2, x = 1) AND pre-images where inner function equals outer singularity (g(x) = 1/2 and f(x) = 1).
- **Answer**: **(D) -1, 1/2, 1**
- **Trap to Avoid**: Never simplify a composite fraction before recording the denominator exclusions of the inner function.
</details>

### Q16 (`CAT2025_S2_QA_Q15`) — [MCQ | Medium | `Round_2_Doable`]
- **Canonical Taxonomy**: Number System $\rightarrow$ *Divisibility & Factor Theory*
- **Core Concept Tested**: Modular residue classification of divisors (d == 1 mod 3)
- **Verified Answer**: **(A) 42** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Mod 3: prime 3 must have exponent 0; prime 7 == 1 mod 3 is free (3 choices); primes 2 and 5 are both -1 mod 3, so their exponents (a, c) must have the same parity!
- **Method 1 (First-Principles Derivation)**: For d = 2^a * 3^b * 5^c * 7^d to be of form 3r + 1: b must be 0 (1 way); d can be 0, 1, 2 (3 ways); and (-1)^a * (-1)^c = 1 => a + c is even. With a in {0..6} (4 even, 3 odd) and c in {0..3} (2 even, 2 odd), there are 4*2 + 3*2 = 14 pairs. Total = 3 * 14 = 42.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Whenever one factor has an even number of exponent choices (here 5^c has 4 choices: 0,1,2,3), exactly HALF of all (a,c) pairs have even sum: (7 * 4)/2 = 14. Multiply by 3 choices for 7^d -> 14 * 3 = 42!
- **Boundary Conditions & Trap Alert**: Do not include b >= 1 (any multiple of 3 is 0 mod 3, never 3r + 1).
- **Verification Audit**: Divisor d = 2^a * 3^b * 5^c * 7^d == 1 (mod 3) requires b = 0 (1 choice). Since 7 == 1 (mod 3), d in {0, 1, 2} gives 3 choices. Since 2 == -1 and 5 == -1 (mod 3), (-1)^(a+c) == 1 (mod 3) requires a + c even: 4*2 + 3*2 = 14 choices. Total = 1 * 3 * 14 = 42.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q15</summary>

- **Trigger**: Mod 3: prime 3 must have exponent 0; prime 7 == 1 mod 3 is free (3 choices); primes 2 and 5 are both -1 mod 3, so their exponents (a, c) must have the same parity!
- **Answer**: **(A) 42**
- **Trap to Avoid**: Do not include b >= 1 (any multiple of 3 is 0 mod 3, never 3r + 1).
</details>

### Q17 (`CAT2025_S2_QA_Q16`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Number System $\rightarrow$ *Factorials, Base Systems & Digits*
- **Core Concept Tested**: Pairing powers of 2 and 5 into trailing zeros 10^k
- **Verified Answer**: **25** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Convert 625 = 5^4 and 128 = 2^7, pair min(260, 252) = 252 powers into 10^252 (which only adds zeros), and sum the digits of 5^8 = 390625.
- **Method 1 (First-Principles Derivation)**: 625^65 * 128^36 = (5^4)^65 * (2^7)^36 = 5^260 * 2^252 = 5^8 * (5*2)^252 = 390625 * 10^252. The sum of digits is 3 + 9 + 0 + 6 + 2 + 5 = 25.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 5^4 = 625 => 5^8 = 625^2 = (600 + 25)^2 = 390625 -> sum of digits = 25.
- **Boundary Conditions & Trap Alert**: Remember squaring a number ending in 25: 625^2 = (62 * 63) concatenated with 25? Wait: for N = 100a + 25, N^2 = 10000a(a+0.5) + 625 -> for 625, 6 * 6.5 = 39 -> 390625!
- **Verification Audit**: (625)^65 * (128)^36 = 5^260 * 2^252 = 5^8 * 10^252 = 390625 * 10^252. Sum of digits = 3 + 9 + 0 + 6 + 2 + 5 = 25.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q16</summary>

- **Trigger**: Convert 625 = 5^4 and 128 = 2^7, pair min(260, 252) = 252 powers into 10^252 (which only adds zeros), and sum the digits of 5^8 = 390625.
- **Answer**: **25**
- **Trap to Avoid**: Remember squaring a number ending in 25: 625^2 = (62 * 63) concatenated with 25? Wait: for N = 100a + 25, N^2 = 10000a(a+0.5) + 625 -> for 625, 6 * 6.5 = 39 -> 390625!
</details>

### Q18 (`CAT2025_S2_QA_Q17`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Time & Work, Pipes & Cisterns*
- **Core Concept Tested**: Relative efficiency assignment in Time & Work
- **Verified Answer**: **340** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Assign the slowest worker (Chandan) efficiency = 1 unit/day so Total Work numerically equals Chandan's solo days!
- **Method 1 (First-Principles Derivation)**: Let rates of C, B, A be 1, 2, 4 units/day. All three work for 20 days (20 * 7 = 140 units) and A + C work for the remaining 40 days (40 * 5 = 200 units). Total work = 340 units, so C alone needs 340/1 = 340 days.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: A and C work all 60 days: 60*(4+1) = 300. B works 20 days: 20*2 = 40. Total = 340.
- **Boundary Conditions & Trap Alert**: 'Completed in 60 days' means 60 days in total (40 days after Bipin leaves), not 60 days after Bipin leaves.
- **Verification Audit**: Set daily efficiencies C = 1, B = 2, A = 4. Work in first 20 days = 20*(4+2+1) = 140. Work in remaining 40 days by A and C = 40*(4+1) = 200. Total work = 340 units. Chandan alone (rate 1) takes 340 days.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q17</summary>

- **Trigger**: Assign the slowest worker (Chandan) efficiency = 1 unit/day so Total Work numerically equals Chandan's solo days!
- **Answer**: **340**
- **Trap to Avoid**: 'Completed in 60 days' means 60 days in total (40 days after Bipin leaves), not 60 days after Bipin leaves.
</details>

### Q19 (`CAT2025_S2_QA_Q18`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Number System $\rightarrow$ *Divisibility & Factor Theory*
- **Core Concept Tested**: Integer factor-pair decomposition with negative factor pairs
- **Verified Answer**: **(D) 17** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: 'm and n are integers' (not just positive integers!) means you MUST test negative factor pairs (-9, -3) of 27!
- **Method 1 (First-Principles Derivation)**: Let u = m + 2n and v = 2m + n. Since u + v = 3(m + n) is a multiple of 3 and u*v = 27, both u and v are multiples of 3: (u, v) in {(3, 9), (9, 3), (-3, -9), (-9, -3)}. For (u, v) = (-9, -3), m = 1 and n = -5, giving 2m - 3n = 2(1) - 3(-5) = 17.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Positive factor pair (3, 9) gives (m, n) = (5, -1) -> 2m - 3n = 13 and (-1, 5) -> 2m - 3n = -17. Negating (m, n) to (1, -5) flips -17 to +17!
- **Boundary Conditions & Trap Alert**: Ignoring negative integers gives the classic trap answer (B) 13.
- **Verification Audit**: Factor pairs (u, v) of 27 where u = m + 2n and v = 2m + n must satisfy u + v = 3(m + n) == 0 mod 3, so {u, v} in {(3, 9), (9, 3), (-3, -9), (-9, -3)}. Solving gives (m, n) in {(5, -1), (-1, 5), (-5, 1), (1, -5)}. Evaluating 2m - 3n gives {13, -17, -13, 17}, with maximum 17 at (m, n) = (1, -5).

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q18</summary>

- **Trigger**: 'm and n are integers' (not just positive integers!) means you MUST test negative factor pairs (-9, -3) of 27!
- **Answer**: **(D) 17**
- **Trap to Avoid**: Ignoring negative integers gives the classic trap answer (B) 13.
</details>

### Q20 (`CAT2025_S2_QA_Q19`) — [MCQ | Medium | `Round_2_Doable`]
- **Canonical Taxonomy**: Geometry & Mensuration $\rightarrow$ *Lines, Angles & Triangles*
- **Core Concept Tested**: Mass Point Geometry / Menelaus theorem on intersecting cevians
- **Verified Answer**: **(B) 11 : 4** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Intersecting cevians AD and BE with given internal ratios AT:TD and BT:TE -> apply Mass Point Geometry (note that point F with DF || BE is a red herring!).
- **Method 1 (First-Principles Derivation)**: Since DF || BE, by Thales theorem in triangle BCE, EF : FC = BD : CD, and in triangle ADF, TE || DF gives AT : TD = AE : EF = 3 : 1. Alternatively by Mass Points: AT/TD = (m_B + m_C)/m_A = 3/1 and BT/TE = (m_A + m_C)/m_B = 4/1. Solving gives m_A : m_B : m_C = 20 : 16 : 44 = 5 : 4 : 11, so BD : CD = m_C : m_B = 11 : 4.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Using DF || BE: let AT = 3, TD = 1 => AE = 3x, EF = x. Then in triangle BCE, DF / BE = 1/3? No, in triangle ADF, TE/DF = AT/AD = 3/4, and BT/TE = 4/1 => BT : TE : DF = 12 : 3 : 4 => BE : DF = 15 : 4 => BC : DC = 15 : 4 => BD : CD = (15 - 4) : 4 = 11 : 4!
- **Boundary Conditions & Trap Alert**: BC : CD is 15 : 4 (distractor A), whereas the question asks for BD : CD = (15 - 4) : 4 = 11 : 4 (Option B)!
- **Verification Audit**: AT : TD = 3 : 1 and BT : TE = 4 : 1. By Mass Point Geometry on triangle ABC with cevians AD and BE intersecting at T: m_A : (m_B + m_C) = 1 : 3 and m_B : (m_A + m_C) = 1 : 4. Setting m_A = 4 gives m_B + m_C = 12 and 4m_B = 4 + m_C => m_B = 16/5, m_C = 44/5. Thus BD : CD = m_C : m_B = 44 : 16 = 11 : 4.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q19</summary>

- **Trigger**: Intersecting cevians AD and BE with given internal ratios AT:TD and BT:TE -> apply Mass Point Geometry (note that point F with DF || BE is a red herring!).
- **Answer**: **(B) 11 : 4**
- **Trap to Avoid**: BC : CD is 15 : 4 (distractor A), whereas the question asks for BD : CD = (15 - 4) : 4 = 11 : 4 (Option B)!
</details>

### Q21 (`CAT2025_S2_QA_Q20`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Averages, Mixtures & Alligations*
- **Core Concept Tested**: Linear interpolation of mixture cost vs concentration
- **Verified Answer**: **(B) 5** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Mixture cost is an affine function of concentration: Delta(Price)/Delta(Coffee%) = (320 - 240)/(36 - 16) = Rs 4 per 1% coffee.
- **Method 1 (First-Principles Derivation)**: Let pure coffee cost C and pure cocoa cost K. Then 0.16C + 0.84K = 240 and 0.36C + 0.64K = 320 => C - K = 400 and K = 176. For a mixture costing 376: K + p(C - K) = 176 + 400p = 376 => p = 0.50. In 10 kg, coffee = 0.50 * 10 = 5 kg.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Slope is Rs 4 per 1% coffee. From Rs 320 (36%) to Rs 376 (+56), add 56/4 = 14% -> 50% of 10 kg = 5 kg.
- **Boundary Conditions & Trap Alert**: Notice 376 > 320 means the new mixture has a higher coffee percentage than both given mixtures (an external alligation / pure ingredient extrapolation).
- **Verification Audit**: Cost increases linearly with coffee%: from 16% (Rs 240) to 36% (Rs 320), a 20% increase in coffee raises price by Rs 80 (Rs 4 per 1% coffee). At Rs 376 (+Rs 56 above 320), coffee% = 36% + 56/4 = 50%. In 10 kg, coffee = 5 kg.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q20</summary>

- **Trigger**: Mixture cost is an affine function of concentration: Delta(Price)/Delta(Coffee%) = (320 - 240)/(36 - 16) = Rs 4 per 1% coffee.
- **Answer**: **(B) 5**
- **Trap to Avoid**: Notice 376 > 320 means the new mixture has a higher coffee percentage than both given mixtures (an external alligation / pure ingredient extrapolation).
</details>

### Q22 (`CAT2025_S2_QA_Q21`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Time, Speed & Distance (TSD)*
- **Core Concept Tested**: Boats and streams upstream-downstream time difference and round-trip harmonic speed
- **Verified Answer**: **8** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Test integer stream speed u = 1 km/h first: 14/5 - 14/7 = 2.8 - 2.0 = 0.8 hrs = 48 min!
- **Method 1 (First-Principles Derivation)**: Sneha: 14/(6-u) - 14/(6+u) = 4/5 => 28u/(36 - u^2) = 4/5 => u = 1 km/h. Rita's upstream speed is 5 - 1 = 4 km/h and downstream speed is 5 + 1 = 6 km/h. Average speed for round trip = 2*4*6/(4+6) = 4.8 km/h. Total distance in 100/60 hrs = 4.8 * (5/3) = 8 km.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Spot u = 1 km/h by inspection (14/5 - 14/7 = 4/5 hr). Then Rita's round-trip average speed is 2(4)(6)/10 = 4.8 km/h; for 5/3 hr, total distance = 4.8 * 5/3 = 8 km.
- **Boundary Conditions & Trap Alert**: The question asks for the TOTAL distance Rita will cover (upstream + downstream = 2d = 8 km), not the one-way distance d = 4 km.
- **Verification Audit**: For Sneha (6 km/h): 14/(6 - u) - 14/(6 + u) = 48/60 = 4/5 => u = 1 km/h. For Rita (5 km/h): upstream = 4 km/h, downstream = 6 km/h. Round trip in 100 min = 5/3 hrs: d/4 + d/6 = 5/3 => d = 4 km one-way. Total distance = 2d = 8 km.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q21</summary>

- **Trigger**: Test integer stream speed u = 1 km/h first: 14/5 - 14/7 = 2.8 - 2.0 = 0.8 hrs = 48 min!
- **Answer**: **8**
- **Trap to Avoid**: The question asks for the TOTAL distance Rita will cover (upstream + downstream = 2d = 8 km), not the one-way distance d = 4 km.
</details>

### Q23 (`CAT2025_S2_QA_Q22`) — [TITA | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Maxima & Minima*
- **Core Concept Tested**: Discrete integer sum-of-squares minimization under modular sum constraint
- **Verified Answer**: **2** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Cluster all 4 integers as close to 46/4 = 11.5 as possible: {11, 11, 12, 12}, and set a = 11 or 12!
- **Method 1 (First-Principles Derivation)**: Notice (a-b) + (a-c) + (a-d) = 4a - (a+b+c+d) = 4a - 46. Closest multiple of 4 to 46 is 44 (a = 11) or 48 (a = 12), making the sum of the 3 integer differences equal to -2 or +2. The minimum sum of squares of 3 integers summing to 2 is 1^2 + 1^2 + 0^2 = 2 (e.g., a=12, b=11, c=11, d=12).
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Divide 46 as evenly as possible into 4 integers: 12, 12, 11, 11. Pick a = 12: (12-11)^2 + (12-11)^2 + (12-12)^2 = 1 + 1 + 0 = 2.
- **Boundary Conditions & Trap Alert**: Do not assume a, b, c, d must be distinct (the problem only states 'a, b, c and d are integers').
- **Verification Audit**: Let x = a - b, y = a - c, z = a - d. Since a + b + c + d = 46, x + y + z = 4a - 46. Since 4a - 46 == 2 (mod 4), the smallest |x + y + z| is 2 (at a = 11 or 12). To minimize x^2 + y^2 + z^2 for integers summing to +-2, pick {1, 1, 0} or {-1, -1, 0}, giving 1^2 + 1^2 + 0^2 = 2.

<details><summary>Active-Recall Self-Test: CAT2025_S2_QA_Q22</summary>

- **Trigger**: Cluster all 4 integers as close to 46/4 = 11.5 as possible: {11, 11, 12, 12}, and set a = 11 or 12!
- **Answer**: **2**
- **Trap to Avoid**: Do not assume a, b, c, d must be distinct (the problem only states 'a, b, c and d are integers').
</details>
