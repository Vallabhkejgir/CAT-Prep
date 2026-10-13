# Pass 1 Master Analysis: CAT 2025 QA Slot 3

## 1. Executive Summary & Exam-Hall Blueprint
- **Section**: QA | **Slot**: Slot 3 (CAT 2025)
- **Source Document**: `docs/pyqs/2025/QA_CAT_2025_Slot_3_2__61e479fed6cbac240075572f15c59e27.pdf`
- **Total Questions**: 22 (14 MCQs, 8 TITA)
- **Difficulty Breakdown**: Easy: **16** | Medium: **6** | Hard: **0**
- **Round-Wise Triage**: Round 1 Sitters: **20** | Round 2 Doables: **2** | Round 3 Time-Sinks: **0**
- **Answer Verification Protocol**: 3-Layer Autonomous Verification (`ai_verified_derivation` — First-Principles Algebraic/Logical Derivation + Programmatic/Cross-Clue Verification + 30-Second Speed Shortcut)

### Percentile Score & Attempt Targets (40-Minute Clock)
| Percentile Target | Scaled Raw Score Target | Net Correct Equivalent | Recommended Execution Strategy |
| :---: | :---: | :---: | :--- |
| **95%ile** | 27-30 (9-10 net) | ~9-11 questions | Clear all Easy Round-1 sitters + all TITA questions with zero negative risk |
| **99%ile** | 38-41 (13-14 net) | ~12-15 questions | Sweep Round 1 in 22 mins + cherry-pick 4-5 Round 2 medium questions |
| **99.5%ile** | 44-47 (15-16 net) | ~15-17 questions | Full Round 1 sweep + 70% of Round 2 using option/parity/invariant shortcuts |
| **99.9%ile** | 52+ (17-18 net) | ~17-19 questions | Complete mastery of Round 1 + Round 2 with <90s average per sitter |

### Topic & Sub-Topic Distribution
| Canonical Topic | Canonical Sub-Topic | Question Count | Question IDs |
| :--- | :--- | :---: | :--- |
| **Algebra** | Functions, Graphs & Functional Equations | 1 | Q16 |
| **Algebra** | Inequalities & Modulus | 1 | Q19 |
| **Algebra** | Linear Equations & Indeterminate Systems | 1 | Q21 |
| **Algebra** | Logarithms, Surds & Indices | 2 | Q8, Q13 |
| **Algebra** | Quadratic & Higher-Degree Polynomials | 2 | Q6, Q15 |
| **Algebra** | Sequences & Series | 1 | Q22 |
| **Arithmetic** | Averages, Mixtures & Alligations | 2 | Q3, Q20 |
| **Arithmetic** | Profit, Loss, Discount & Faulty Weights | 1 | Q17 |
| **Arithmetic** | Ratio, Proportion, Variation & Partnerships | 1 | Q9 |
| **Arithmetic** | Time & Work, Pipes & Cisterns | 2 | Q10, Q11 |
| **Arithmetic** | Time, Speed & Distance (TSD) | 2 | Q7, Q12 |
| **Geometry & Mensuration** | Lines, Angles & Triangles | 2 | Q5, Q18 |
| **Geometry & Mensuration** | Quadrilaterals & Polygons | 1 | Q2 |
| **Modern Math** | Set Theory | 1 | Q4 |
| **Number System** | Factorials, Base Systems & Digits | 2 | Q1, Q14 |

---

## 2. Quick-Reference Verified Answer Key
| Q# | Question ID | Type | Difficulty | Round Tag | Verified Answer | Core Concept / Mental Trigger |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| **Q1** | `CAT2025_S3_QA_Q01` | MCQ | Easy | `Round_1_Sitter` | **(C) 811** | Place-value digit constraints and linear parameter variation |
| **Q2** | `CAT2025_S3_QA_Q02` | MCQ | Medium | `Round_1_Sitter` | **(C) 48** | Tangential right-trapezium properties (Pitot's theorem AB + CD = AD + BC) |
| **Q3** | `CAT2025_S3_QA_Q03` | TITA | Easy | `Round_1_Sitter` | **16** | Two-vessel symmetric transfer invariant (final ratio in A equals 60 : v) |
| **Q4** | `CAT2025_S3_QA_Q04` | MCQ | Medium | `Round_1_Sitter` | **(C) 35** | 3-Set Inclusion-Exclusion optimization with strict positive intersection constraint |
| **Q5** | `CAT2025_S3_QA_Q05` | MCQ | Easy | `Round_1_Sitter` | **(A) 18** | Circumcircle chord-secant similarity (AB^2 = AD * AE in isosceles triangle) |
| **Q6** | `CAT2025_S3_QA_Q06` | MCQ | Medium | `Round_1_Sitter` | **(B) 44853*sqrt(3)** | Reciprocal power sum recurrence S_7 = S_3 * S_4 - S_1 |
| **Q7** | `CAT2025_S3_QA_Q07` | MCQ | Easy | `Round_1_Sitter` | **(B) 15** | Proportional TSD time-saving identity D = Delta_t * v1 * v2 / Delta_v |
| **Q8** | `CAT2025_S3_QA_Q08` | MCQ | Medium | `Round_1_Sitter` | **(C) (3 + sqrt(33))/2** | Logarithmic equation with variable base domain filtering (base > 0, base != 1) |
| **Q9** | `CAT2025_S3_QA_Q09` | TITA | Easy | `Round_1_Sitter` | **272** | Total-invariance scaling in two-box internal transfers |
| **Q10** | `CAT2025_S3_QA_Q10` | MCQ | Easy | `Round_1_Sitter` | **(C) 73** | Combined flow rate scaling in Pipes & Cisterns |
| **Q11** | `CAT2025_S3_QA_Q11` | MCQ | Easy | `Round_1_Sitter` | **(B) 2** | Individual member efficiency LCM scaling in multi-team work problems |
| **Q12** | `CAT2025_S3_QA_Q12` | TITA | Easy | `Round_1_Sitter` | **444** | Inverse speed-time ratio on fixed segments |
| **Q13** | `CAT2025_S3_QA_Q13` | TITA | Easy | `Round_1_Sitter` | **112** | Unique prime factorization exponent matching |
| **Q14** | `CAT2025_S3_QA_Q14` | MCQ | Easy | `Round_1_Sitter` | **(B) 221** | Decimal borrow propagation in 10^n - k |
| **Q15** | `CAT2025_S3_QA_Q15` | MCQ | Easy | `Round_1_Sitter` | **(B) -3** | Completing the square under a radical and checking discriminant on both modulus branches |
| **Q16** | `CAT2025_S3_QA_Q16` | MCQ | Medium | `Round_2_Doable` | **(B) (-inf, 1/8] U [1/2, inf)** | Range of rational quadratic function via Discriminant >= 0 method |
| **Q17** | `CAT2025_S3_QA_Q17` | MCQ | Easy | `Round_1_Sitter` | **(A) 525** | Weighted revenue aggregation across multi-period discount rates |
| **Q18** | `CAT2025_S3_QA_Q18` | TITA | Easy | `Round_1_Sitter` | **126** | Altitudes of an isosceles triangle via area invariance (a*h_a = b*h_b = c*h_c = 2*Area) |
| **Q19** | `CAT2025_S3_QA_Q19` | TITA | Medium | `Round_2_Doable` | **397** | Bounded ratio extrema with perfect-square domain endpoints |
| **Q20** | `CAT2025_S3_QA_Q20` | MCQ | Easy | `Round_1_Sitter` | **(B) 54000** | Weighted percentage contribution to overall mean shift |
| **Q21** | `CAT2025_S3_QA_Q21` | TITA | Easy | `Round_1_Sitter` | **700** | Three-variable linear system optimization with ordering constraint S <= A |
| **Q22** | `CAT2025_S3_QA_Q22` | TITA | Easy | `Round_1_Sitter` | **65** | Symmetric AP mean properties (T4 + T7 + T10 = 3*T7 and S5 = 5*T3) |

---

## 3. Question-by-Question High-Recall Decomposition (Dual-Method)

### Q1 (`CAT2025_S3_QA_Q01`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Number System $\rightarrow$ *Factorials, Base Systems & Digits*
- **Core Concept Tested**: Place-value digit constraints and linear parameter variation
- **Verified Answer**: **(C) 811** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Subtract T + H + X = 15 from H + X + U = 16 immediately to get U = T + 1; then X = U + 6 = T + 7 <= 9 restricts T to {1, 2}!
- **Method 1 (First-Principles Derivation)**: Let the digits be T, H, X, U. From U - T = 1 and X = U + 6, we have U = T + 1, X = T + 7, and H = 15 - T - (T + 7) = 8 - 2T. Since T >= 1 and X <= 9, T can only be 1 (number = 1682) or 2 (number = 2493). Difference = 2493 - 1682 = 811.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Increasing T by 1 changes H by -2, X by +1, U by +1, so the 4-digit number changes by 1000(1) + 100(-2) + 10(1) + 1(1) = 811!
- **Boundary Conditions & Trap Alert**: T >= 1 since the number is greater than 1000 (so T = 0 giving 0871 is excluded).
- **Verification Audit**: For 4-digit number THXU: T + H + X = 15, H + X + U = 16 => U = T + 1 (with T >= 1), and X = U + 6 = T + 7 <= 9 => T in {1, 2}. For T = 1: 1682; for T = 2: 2493. Difference = 2493 - 1682 = 811.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q01</summary>

- **Trigger**: Subtract T + H + X = 15 from H + X + U = 16 immediately to get U = T + 1; then X = U + 6 = T + 7 <= 9 restricts T to {1, 2}!
- **Answer**: **(C) 811**
- **Trap to Avoid**: T >= 1 since the number is greater than 1000 (so T = 0 giving 0871 is excluded).
</details>

### Q2 (`CAT2025_S3_QA_Q02`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Geometry & Mensuration $\rightarrow$ *Quadrilaterals & Polygons*
- **Core Concept Tested**: Tangential right-trapezium properties (Pitot's theorem AB + CD = AD + BC)
- **Verified Answer**: **(C) 48** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: In ANY right trapezium circumscribing a circle of radius r with parallel bases a and b, the perpendicular leg is h = 2r and harmonic mean of bases is 2ab/(a+b) = 2r? Even faster: Drop tangents from C and B to get r + x? Wait: at right angles A and D, tangent lengths from A and D along AB and DC are r = 3! So DC = 3 + t1 and AB = 3 + t2 with t1*t2 = r^2 = 9!
- **Method 1 (First-Principles Derivation)**: Height AD = 2r = 6. Let DC = x and AB = 3x. Since a circle is inscribed in ABCD, opposite sides sum equally: AB + DC = AD + BC => 4x = 6 + BC => BC = 4x - 6. Dropping an altitude from C to AB gives (4x - 6)^2 = 6^2 + (2x)^2 => 12x^2 = 48x => x = 4. Area = 0.5*(16)*6 = 48.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Since AD perp AB and DC, tangent segments at A and D have length r = 3. Let remaining tangent segments at C and B be t1, t2; then t1*t2 = r^2 = 9, DC = 3 + t1, AB = 3 + t2 = 3(3 + t1) => t1 = 1, t2 = 9 => DC = 4, AB = 12 => Area = 8 * 6 = 48!
- **Boundary Conditions & Trap Alert**: Remember the identity t1 * t2 = r^2 for the two non-perpendicular corners of a right tangential trapezium.
- **Verification Audit**: Height AD = 2r = 6 cm. Let DC = x, AB = 3x. By Pitot's theorem for tangential quadrilateral ABCD, BC + AD = AB + DC => BC = 4x - 6. By Pythagoras on right triangle with legs 6 and 2x: (4x - 6)^2 = 36 + 4x^2 => 12x^2 - 48x = 0 => x = 4. Area = 0.5*(4 + 12)*6 = 48.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q02</summary>

- **Trigger**: In ANY right trapezium circumscribing a circle of radius r with parallel bases a and b, the perpendicular leg is h = 2r and harmonic mean of bases is 2ab/(a+b) = 2r? Even faster: Drop tangents from C and B to get r + x? Wait: at right angles A and D, tangent lengths from A and D along AB and DC are r = 3! So DC = 3 + t1 and AB = 3 + t2 with t1*t2 = r^2 = 9!
- **Answer**: **(C) 48**
- **Trap to Avoid**: Remember the identity t1 * t2 = r^2 for the two non-perpendicular corners of a right tangential trapezium.
</details>

### Q3 (`CAT2025_S3_QA_Q03`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Averages, Mixtures & Alligations*
- **Core Concept Tested**: Two-vessel symmetric transfer invariant (final ratio in A equals 60 : v)
- **Verified Answer**: **16** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: When v litres are transferred from pure vessel A (volume V) to pure vessel B (volume V) and v litres are transferred back, the final ratio of A-liquid to B-liquid in A is ALWAYS V : v!
- **Method 1 (First-Principles Derivation)**: After step 1, A has (60 - v) alcohol; B has v alcohol and 60 water. Step 2 transfers v*(60/(60+v)) water into A, leaving 60v/(60+v) water and 3600/(60+v) alcohol in A. Their ratio is 3600 : 60v = 60 : v = 15 : 4 => v = 16.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: By the V : v symmetric transfer identity, 60 : v = 15 : 4 => v = 16 in 5 seconds!
- **Boundary Conditions & Trap Alert**: Do not use the repeated-replacement formula (which applies when vessel A stays at constant volume 60 during both steps); here B's volume temporarily becomes 60 + v.
- **Verification Audit**: After pouring v litres of alcohol from A into B (60L water), B has v alcohol and 60 water, which is in ratio v : 60. When v litres of this mixture are poured back into A, the ratio of alcohol to water in A is 60 : v. Given 60 : v = 15 : 4 => v = 16.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q03</summary>

- **Trigger**: When v litres are transferred from pure vessel A (volume V) to pure vessel B (volume V) and v litres are transferred back, the final ratio of A-liquid to B-liquid in A is ALWAYS V : v!
- **Answer**: **16**
- **Trap to Avoid**: Do not use the repeated-replacement formula (which applies when vessel A stays at constant volume 60 during both steps); here B's volume temporarily becomes 60 + v.
</details>

### Q4 (`CAT2025_S3_QA_Q04`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Modern Math $\rightarrow$ *Set Theory*
- **Core Concept Tested**: 3-Set Inclusion-Exclusion optimization with strict positive intersection constraint
- **Verified Answer**: **(C) 35** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Write |P \ M| = |P| - |P n M| = 75 - 2k; to maximize 75 - 2k, minimize k subject to x = 4k - 76 >= 1!
- **Method 1 (First-Principles Derivation)**: Sum of singletons = 75 + 111 + 40 = 226. Sum of pairwise intersections = k + k + 2k = 4k. By PIE, 150 = 226 - 4k + x => x = 4k - 76. Since x >= 1 and k is an integer, 4k >= 77 => k >= 20. At k = 20, x = 4, and |P \ M| = 75 - 2(20) = 35.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 4k = 76 + x with x >= 1 => smallest multiple of 4 above 76 is 80 (k = 20, x = 4) => 75 - 2(20) = 35.
- **Boundary Conditions & Trap Alert**: Ignoring 'at least one student chose all three subjects' (x >= 1) sets x = 0, k = 19, giving the trap answer 75 - 38 = 37 (or if k=20 -> 35).
- **Verification Audit**: Let |P n C| = |C n M| = k, |P n M| = 2k, and |P n M n C| = x >= 1. By Inclusion-Exclusion: 150 = 75 + 111 + 40 - 4k + x => 4k - x = 76. To maximize |P \ M| = 75 - 2k, minimize k. Since x = 4k - 76 >= 1, 4k >= 77 => k >= 20 (at k=20, x=4, all regions >= 0). Thus max(75 - 2k) = 75 - 40 = 35.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q04</summary>

- **Trigger**: Write |P \ M| = |P| - |P n M| = 75 - 2k; to maximize 75 - 2k, minimize k subject to x = 4k - 76 >= 1!
- **Answer**: **(C) 35**
- **Trap to Avoid**: Ignoring 'at least one student chose all three subjects' (x >= 1) sets x = 0, k = 19, giving the trap answer 75 - 38 = 37 (or if k=20 -> 35).
</details>

### Q5 (`CAT2025_S3_QA_Q05`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Geometry & Mensuration $\rightarrow$ *Lines, Angles & Triangles*
- **Core Concept Tested**: Circumcircle chord-secant similarity (AB^2 = AD * AE in isosceles triangle)
- **Verified Answer**: **(A) 18** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: In isosceles triangle ABC (AB = AC) with E on the circumcircle (angle ACB = angle AEB), ALWAYS use AB^2 = AD * AE!
- **Method 1 (First-Principles Derivation)**: Since AB = AC, angle ABD = angle ACB. Given angle ACB = angle AEB, we have angle ABD = angle AEB. With common angle BAD = angle EAB, triangle ABD is similar to triangle AEB by AA similarity. Therefore AB/AE = AD/AB => AE = 12^2 / 8 = 18.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Direct theorem: AB^2 = AD * AE => 144 = 8 * AE => AE = 18.
- **Boundary Conditions & Trap Alert**: Do not confuse AE (18) with DE = AE - AD = 10.
- **Verification Audit**: Since AB = AC = 12, angle ABC = angle ACB = angle AEB. In triangles ABD and AEB, angle BAE is common and angle ABD = angle AEB. Thus triangle ABD ~ triangle AEB, giving AB/AE = AD/AB => AE = AB^2 / AD = 144 / 8 = 18.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q05</summary>

- **Trigger**: In isosceles triangle ABC (AB = AC) with E on the circumcircle (angle ACB = angle AEB), ALWAYS use AB^2 = AD * AE!
- **Answer**: **(A) 18**
- **Trap to Avoid**: Do not confuse AE (18) with DE = AE - AD = 10.
</details>

### Q6 (`CAT2025_S3_QA_Q06`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Quadratic & Higher-Degree Polynomials*
- **Core Concept Tested**: Reciprocal power sum recurrence S_7 = S_3 * S_4 - S_1
- **Verified Answer**: **(B) 44853*sqrt(3)** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Use S_7 = S_3 * S_4 - S_1 and check ONLY the units digit of the coefficient of sqrt(3): 72 * 623 - 3 ends in 6 - 3 = 3!
- **Method 1 (First-Principles Derivation)**: Let S_k = x^k + 1/x^k. Given S_2 = 25 => S_1 = sqrt(25 + 2) = 3*sqrt(3). Next, S_3 = S_1^3 - 3*S_1 = 81*sqrt(3) - 9*sqrt(3) = 72*sqrt(3), and S_4 = S_2^2 - 2 = 623. Using S_7 = S_3*S_4 - S_1 gives (72*623 - 3)*sqrt(3) = 44853*sqrt(3).
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Units digit check on (72 * 623 - 3): 2 * 3 - 3 = 3 -> immediately selects (B) 44853*sqrt(3) without multiplying 72 * 623!
- **Boundary Conditions & Trap Alert**: Forgetting to subtract S_1 = 3*sqrt(3) in S_3 * S_4 = S_7 + S_1 gives the trap answer (D) 44856*sqrt(3)!
- **Verification Audit**: x^2 + 1/x^2 = 25 => x + 1/x = sqrt(27) = 3*sqrt(3). Then x^3 + 1/x^3 = (3*sqrt(3))^3 - 3(3*sqrt(3)) = 72*sqrt(3), and x^4 + 1/x^4 = 25^2 - 2 = 623. Finally x^7 + 1/x^7 = (x^3 + 1/x^3)(x^4 + 1/x^4) - (x + 1/x) = (72*623 - 3)*sqrt(3) = 44853*sqrt(3).

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q06</summary>

- **Trigger**: Use S_7 = S_3 * S_4 - S_1 and check ONLY the units digit of the coefficient of sqrt(3): 72 * 623 - 3 ends in 6 - 3 = 3!
- **Answer**: **(B) 44853*sqrt(3)**
- **Trap to Avoid**: Forgetting to subtract S_1 = 3*sqrt(3) in S_3 * S_4 = S_7 + S_1 gives the trap answer (D) 44856*sqrt(3)!
</details>

### Q7 (`CAT2025_S3_QA_Q07`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Time, Speed & Distance (TSD)*
- **Core Concept Tested**: Proportional TSD time-saving identity D = Delta_t * v1 * v2 / Delta_v
- **Verified Answer**: **(B) 15** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Equate remaining distance D = Delta_t1 * v(v + s1)/s1 = Delta_t2 * v(v + s2)/s2 => (v + s1)/s1 * Delta_t1 = (v + s2)/s2 * Delta_t2!
- **Method 1 (First-Principles Derivation)**: Let remaining distance after the stop be D. Saving 20 min requires +3 km/h, and saving 30 min (20 + 10) requires +5 km/h: D = (20/60)*v(v+3)/3 = (30/60)*v(v+5)/5 => 20(v+3)/3 = 30(v+5)/5 => (v+3)/9 = (v+5)/10 => v = 15.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: (v + 3)/9 = (v + 5)/10 => v = 15 in 10 seconds (notice the 5 pm to 11 pm window is completely extraneous!).
- **Boundary Conditions & Trap Alert**: '10 minutes more' means total stop = 20 + 10 = 30 minutes (not 10 minutes).
- **Verification Audit**: Remaining distance D = (20/60) * v(v+3)/3 = (30/60) * v(v+5)/5 => (v+3)/9 = (v+5)/10 => 10v + 30 = 9v + 45 => v = 15 km/h.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q07</summary>

- **Trigger**: Equate remaining distance D = Delta_t1 * v(v + s1)/s1 = Delta_t2 * v(v + s2)/s2 => (v + s1)/s1 * Delta_t1 = (v + s2)/s2 * Delta_t2!
- **Answer**: **(B) 15**
- **Trap to Avoid**: '10 minutes more' means total stop = 20 + 10 = 30 minutes (not 10 minutes).
</details>

### Q8 (`CAT2025_S3_QA_Q08`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Logarithms, Surds & Indices*
- **Core Concept Tested**: Logarithmic equation with variable base domain filtering (base > 0, base != 1)
- **Verified Answer**: **(C) (3 + sqrt(33))/2** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Before applying Vieta sum of roots (which gives the trap answer 3!), ALWAYS enforce log base > 0 => x > 3!
- **Method 1 (First-Principles Derivation)**: Domain requires x - 3 > 0, x - 3 != 1, x^2 - 9 > 0, x + 1 > 0 => x > 3, x != 4. Then x^2 - 9 = (x + 1)(x - 3)^2 => x + 3 = x^2 - 2x - 3 => x^2 - 3x - 6 = 0. Roots are (3 + sqrt(33))/2 approx 4.37 > 3 (valid) and (3 - sqrt(33))/2 approx -1.37 < 3 (rejected). Thus the only real root is (3 + sqrt(33))/2.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Spot that one root of x^2 - 3x - 6 = 0 is negative (product = -6 < 0) and must be rejected by x > 3, leaving only the single positive root (3 + sqrt(33))/2 (Option C).
- **Boundary Conditions & Trap Alert**: Blindly taking Vieta's sum of roots -b/a = 3 without rejecting the negative root (3 - sqrt(33))/2 falls straight into trap (D) 3!
- **Verification Audit**: Domain of log_{x-3}: x - 3 > 0 and x - 3 != 1 => x > 3, x != 4. Cancelling (x - 3) from x^2 - 9 = (x + 1)(x - 3)^2 gives x + 3 = (x + 1)(x - 3) => x^2 - 3x - 6 = 0 => x = (3 +- sqrt(33))/2. Only (3 + sqrt(33))/2 > 3 is in the domain.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q08</summary>

- **Trigger**: Before applying Vieta sum of roots (which gives the trap answer 3!), ALWAYS enforce log base > 0 => x > 3!
- **Answer**: **(C) (3 + sqrt(33))/2**
- **Trap to Avoid**: Blindly taking Vieta's sum of roots -b/a = 3 without rejecting the negative root (3 - sqrt(33))/2 falls straight into trap (D) 3!
</details>

### Q9 (`CAT2025_S3_QA_Q09`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Ratio, Proportion, Variation & Partnerships*
- **Core Concept Tested**: Total-invariance scaling in two-box internal transfers
- **Verified Answer**: **272** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Equate total units before and after internal transfer: 17+7 = 24, 37+20 = 57; LCM(24, 57) = 456 (since 24=3*8, 57=3*19), and 1:1 target is 456/2 = 228 units!
- **Method 1 (First-Principles Derivation)**: (17x - 108)/(7x + 108) = 37/20 => 81x = 6156 => x = 76. Total coins = 24 * 76 = 1824, so 1:1 means 912 coins each. Box A currently has 17(76) - 108 = 1184 coins, so 1184 - 912 = 272 more coins must be shifted.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: In 456-unit scale: A drops from 323 -> 296 (27 units = 108 => 1 unit = 4 coins) and needs to reach 228 (68 units * 4 = 272 coins).
- **Boundary Conditions & Trap Alert**: The question asks how many coins need to be shifted FURTHER (272), not total shifted from the start (108 + 272 = 380).
- **Verification Audit**: Initial ratio 17:7 (sum 24); after shifting 108, ratio is 37:20 (sum 57). Scale to LCM(24, 57) = 456: initial is 17*19 : 7*19 = 323 : 133; after shift is 37*8 : 20*8 = 296 : 160. Shift of 323 - 296 = 27 units = 108 coins => 1 unit = 4 coins. To reach 1:1 (228 : 228), shift 296 - 228 = 68 units = 68 * 4 = 272 coins.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q09</summary>

- **Trigger**: Equate total units before and after internal transfer: 17+7 = 24, 37+20 = 57; LCM(24, 57) = 456 (since 24=3*8, 57=3*19), and 1:1 target is 456/2 = 228 units!
- **Answer**: **272**
- **Trap to Avoid**: The question asks how many coins need to be shifted FURTHER (272), not total shifted from the start (108 + 272 = 380).
</details>

### Q10 (`CAT2025_S3_QA_Q10`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Time & Work, Pipes & Cisterns*
- **Core Concept Tested**: Combined flow rate scaling in Pipes & Cisterns
- **Verified Answer**: **(C) 73** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Convert 15 hours to 900 minutes first, then multiply by 4 / (4 + 9 + 36) = 4/49.
- **Method 1 (First-Principles Derivation)**: Total time in minutes = (15 * 60) * 4 / (4 + 9 + 36) = 3600 / 49 = 73.469 minutes, nearest to 73.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 3600 / 49 = 73 + 23/49 -> 73.
- **Boundary Conditions & Trap Alert**: Pay attention to unit conversion from hours (15 h) to minutes (900 min).
- **Verification Audit**: Rates A:B:C = 4:9:36 (total = 49). Pipe A (rate 4) takes 15 hours = 900 minutes, so tank volume = 4 * 900 = 3600 units. All 3 pipes together take 3600 / 49 = 73.47 minutes, nearest to 73.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q10</summary>

- **Trigger**: Convert 15 hours to 900 minutes first, then multiply by 4 / (4 + 9 + 36) = 4/49.
- **Answer**: **(C) 73**
- **Trap to Avoid**: Pay attention to unit conversion from hours (15 h) to minutes (900 min).
</details>

### Q11 (`CAT2025_S3_QA_Q11`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Time & Work, Pipes & Cisterns*
- **Core Concept Tested**: Individual member efficiency LCM scaling in multi-team work problems
- **Verified Answer**: **(B) 2** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Take Total Work = LCM(5*40, 8*50, 10*4) = LCM(200, 400, 40) = 400 units so each B-member has efficiency = 1 unit/hour!
- **Method 1 (First-Principles Derivation)**: Set Total Work = 400 units. Individual efficiencies: a = 400/200 = 2, b = 400/400 = 1, c = 400/40 = 10 units/hr. In 23 hours, (2a + 3b + c) completes 23*(4 + 3 + 10) = 391 units. Remaining 9 units in 1 hour require 2a + (3 + x)b = 4 + 3 + x = 9 => x = 2 additional B-members.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 1 member of C (rate 10) equals 10 members of B (rate 1). Over 24 hours, 2A + 3B + 1C would do 24*17 = 408 units (8 units excess). Removing 1C in the last hour loses 10 units, leaving a net deficit of 10 - 8 = 2 units = 2 B-members!
- **Boundary Conditions & Trap Alert**: The question asks for ADDITIONAL members from Team B (2), not the total members from Team B (3 + 2 = 5).
- **Verification Audit**: Per-member hourly work (out of 400 total units): Team A member = 400/(5*40) = 2 units/h; Team B member = 400/(8*50) = 1 unit/h; Team C member = 400/(10*4) = 10 units/h. Initial group (2A + 3B + 1C) does 2(2) + 3(1) + 1(10) = 17 units/h. In 23 hours, they complete 23 * 17 = 391 units, leaving 9 units for the 24th hour. Since 2A + 3B do 7 units/h, 2 additional members from Team B (1 unit/h each) are needed.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q11</summary>

- **Trigger**: Take Total Work = LCM(5*40, 8*50, 10*4) = LCM(200, 400, 40) = 400 units so each B-member has efficiency = 1 unit/hour!
- **Answer**: **(B) 2**
- **Trap to Avoid**: The question asks for ADDITIONAL members from Team B (2), not the total members from Team B (3 + 2 = 5).
</details>

### Q12 (`CAT2025_S3_QA_Q12`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Time, Speed & Distance (TSD)*
- **Core Concept Tested**: Inverse speed-time ratio on fixed segments
- **Verified Answer**: **444** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Since v_run / v_walk = 7/5, multiply by 7/5 to convert Run time -> Walk time, and by 5/7 to convert Walk time -> Run time!
- **Method 1 (First-Principles Derivation)**: 3 hours 30 minutes = 210 minutes. Since running speed is 7/5 of walking speed, time taken is inversely proportional (5/7). Thus Walk(AB) = (7/5)*Run(BA) = (7/5)*210 = 294 min, and Run(BC) = (5/7)*Walk(BC) = (5/7)*210 = 150 min. Total = 294 + 150 = 444 min.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 210 * (7/5 + 5/7) = 210 * (74/35) = 6 * 74 = 444 minutes!
- **Boundary Conditions & Trap Alert**: Keep all times in minutes (3 hr 30 min = 210 min).
- **Verification Audit**: Run speed : Walk speed = 1.4 : 1 = 7 : 5, so Run time : Walk time = 5 : 7 on any fixed segment. Given Walk(BC) = 210 min => Run(BC) = 210 * (5/7) = 150 min. Given Run(BA) = 210 min => Walk(AB) = 210 * (7/5) = 294 min. Total = 294 + 150 = 444 min.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q12</summary>

- **Trigger**: Since v_run / v_walk = 7/5, multiply by 7/5 to convert Run time -> Walk time, and by 5/7 to convert Walk time -> Run time!
- **Answer**: **444**
- **Trap to Avoid**: Keep all times in minutes (3 hr 30 min = 210 min).
</details>

### Q13 (`CAT2025_S3_QA_Q13`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Logarithms, Surds & Indices*
- **Core Concept Tested**: Unique prime factorization exponent matching
- **Verified Answer**: **112** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Decompose every composite base (12, 4, 8, 20, 243) into primes {2, 3, 5} and equate exponents of 3 first to find x!
- **Method 1 (First-Principles Derivation)**: Comparing exponents of 3: 12x = 5(3x - 6) => 3x = 30 => x = 10. Comparing exponents of 5: 2y = 12x = 120 => y = 60. Comparing exponents of 2: 24x + 2(24x + 12) = 12z + 24x => 12z = 48x + 24 = 504 => z = 42. Therefore x + y + z = 10 + 60 + 42 = 112.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: In base 2, cancel 24x (from 12^(12x) and 20^(12x)) on both sides before expanding: 4^(24x+12) = 8^(4z) => 48x + 24 = 12z => z = 4x + 2 = 42!
- **Boundary Conditions & Trap Alert**: Cancelling 4^(12x) from 12^(12x) and 20^(12x) immediately saves half the exponent arithmetic.
- **Verification Audit**: Prime factorize into bases 2, 3, 5: 12^(12x)*4^(24x+12)*5^(2y) = 2^(72x+24) * 3^(12x) * 5^(2y), and 8^(4z)*20^(12x)*243^(3x-6) = 2^(12z+24x) * 3^(15x-30) * 5^(12x). Equating exponents: 12x = 15x - 30 => x = 10; 2y = 12x => y = 60; 72x + 24 = 12z + 24x => 12z = 48x + 24 = 504 => z = 42. Sum x + y + z = 112.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q13</summary>

- **Trigger**: Decompose every composite base (12, 4, 8, 20, 243) into primes {2, 3, 5} and equate exponents of 3 first to find x!
- **Answer**: **112**
- **Trap to Avoid**: Cancelling 4^(12x) from 12^(12x) and 20^(12x) immediately saves half the exponent arithmetic.
</details>

### Q14 (`CAT2025_S3_QA_Q14`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Number System $\rightarrow$ *Factorials, Base Systems & Digits*
- **Core Concept Tested**: Decimal borrow propagation in 10^n - k
- **Verified Answer**: **(B) 221** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: 10^25 - 123 has 25 digits: (25 - 3) = 22 nines followed by (1000 - 123) = 877; 10^50 just adds a single digit '1' at the front!
- **Method 1 (First-Principles Derivation)**: 10^25 - 123 = 99...9877 (with twenty-two 9s and 877). Since 10^50 is at the 51st place, 10^50 + (10^25 - 123) has non-zero digits: one 1, twenty-two 9s, one 8, and two 7s. Digit sum = 1 + 22(9) + 8 + 7 + 7 = 221.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Mod 9 check: 10^50 + 10^25 - 123 == 1 + 1 - 6 = -4 == 5 (mod 9). Among (A) 21 (3), (B) 221 (5), (C) 324 (0), (D) 255 (3), ONLY (B) 221 leaves remainder 5 mod 9!
- **Boundary Conditions & Trap Alert**: Digital-root / Modulo-9 invariant solves this question in 5 seconds without counting how many 9s appear!
- **Verification Audit**: 10^25 - 123 consists of twenty-two 9s followed by 877. Adding 10^50 places a leading 1 followed by zeros ahead of those 25 digits. Sum of digits = 1 + 22*9 + 8 + 7 + 7 = 1 + 198 + 22 = 221.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q14</summary>

- **Trigger**: 10^25 - 123 has 25 digits: (25 - 3) = 22 nines followed by (1000 - 123) = 877; 10^50 just adds a single digit '1' at the front!
- **Answer**: **(B) 221**
- **Trap to Avoid**: Digital-root / Modulo-9 invariant solves this question in 5 seconds without counting how many 9s appear!
</details>

### Q15 (`CAT2025_S3_QA_Q15`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Quadratic & Higher-Degree Polynomials*
- **Core Concept Tested**: Completing the square under a radical and checking discriminant on both modulus branches
- **Verified Answer**: **(B) -3** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: u(u + 2) + 1 = (u + 1)^2, so sqrt(f(x) + 1) = |x^2 + 3x + 1|; check which branch has real roots!
- **Method 1 (First-Principles Derivation)**: Since (x^2 + 3x)(x^2 + 3x + 2) + 1 = (x^2 + 3x + 1)^2, the equation becomes |x^2 + 3x + 1| = 9701. Branch 1: x^2 + 3x - 9700 = 0 has two real roots with sum -3. Branch 2: x^2 + 3x + 9702 = 0 has discriminant 9 - 4(9702) < 0 (no real roots). Thus the sum of all real roots is -3.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: The parabola x^2 + 3x + 1 is symmetric about x = -3/2; only the upper horizontal line y = 9701 intersects it (in 2 real points), whose sum is 2*(-3/2) = -3 (Option B).
- **Boundary Conditions & Trap Alert**: Adding the non-real roots of the second branch gives the classic trap answer (C) -6.
- **Verification Audit**: Let u = x^2 + 3x. Then f(x) + 1 = u(u + 2) + 1 = (u + 1)^2 = (x^2 + 3x + 1)^2. Thus sqrt(f(x) + 1) = |x^2 + 3x + 1| = 9701. For x^2 + 3x + 1 = 9701, Delta > 0 and sum of real roots = -3. For x^2 + 3x + 1 = -9701, x^2 + 3x + 9702 = 0 has Delta < 0 (no real roots). Total sum of real roots = -3.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q15</summary>

- **Trigger**: u(u + 2) + 1 = (u + 1)^2, so sqrt(f(x) + 1) = |x^2 + 3x + 1|; check which branch has real roots!
- **Answer**: **(B) -3**
- **Trap to Avoid**: Adding the non-real roots of the second branch gives the classic trap answer (C) -6.
</details>

### Q16 (`CAT2025_S3_QA_Q16`) — [MCQ | Medium | `Round_2_Doable`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Functions, Graphs & Functional Equations*
- **Core Concept Tested**: Range of rational quadratic function via Discriminant >= 0 method
- **Verified Answer**: **(B) (-inf, 1/8] U [1/2, inf)** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Cross-multiply y = P(x)/Q(x) into a quadratic in x and set Discriminant Delta(y) >= 0, factoring out common binomials before expanding!
- **Method 1 (First-Principles Derivation)**: Rearranging into a quadratic in x yields 2y*x^2 + 2(2y - 1)x + 3(1 - 2y) = 0. For real x, Delta/4 = (2y - 1)^2 - 6y(1 - 2y) = (2y - 1)(2y - 1 + 6y) = (2y - 1)(8y - 1) >= 0, yielding y <= 1/8 or y >= 1/2.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Factor (2y - 1) out of the discriminant immediately: (2y - 1)[(2y - 1) + 6y] = (2y - 1)(8y - 1) >= 0 -> critical points are 1/8 and 1/2 (Option B).
- **Boundary Conditions & Trap Alert**: Never expand (2y - 1)^2 and 6y(2y - 1) separately when (2y - 1) is a common factor!
- **Verification Audit**: Setting y = (2x - 3)/(2x^2 + 4x - 6) (or with the sign convention in the paper 2y*x^2 + (4y - 2)x + (3 - 6y) = 0), the discriminant with respect to x is Delta = (4y - 2)^2 - 8y(3 - 6y) = 4(2y - 1)^2 + 24y(2y - 1) = 4(2y - 1)(8y - 1) >= 0, which gives y in (-inf, 1/8] U [1/2, inf).

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q16</summary>

- **Trigger**: Cross-multiply y = P(x)/Q(x) into a quadratic in x and set Discriminant Delta(y) >= 0, factoring out common binomials before expanding!
- **Answer**: **(B) (-inf, 1/8] U [1/2, inf)**
- **Trap to Avoid**: Never expand (2y - 1)^2 and 6y(2y - 1) separately when (2y - 1) is a common factor!
</details>

### Q17 (`CAT2025_S3_QA_Q17`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Profit, Loss, Discount & Faulty Weights*
- **Core Concept Tested**: Weighted revenue aggregation across multi-period discount rates
- **Verified Answer**: **(A) 525** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Notice monthly sales (120, 135, 150, 165) form an AP with mean 142.5 (total = 4 * 142.5 = 570), and effective MP coefficient is 96 + 121.5 + 142.5 + 165 = 525!
- **Method 1 (First-Principles Derivation)**: Total Cost = (120 + 135 + 150 + 165) * 240 = 570 * 240 = 136800. Total Revenue = 136800 + 138825 = 275625. Also Total Revenue = MP * (120*0.80 + 135*0.90 + 150*0.95 + 165*1.00) = 525 * MP. Hence MP = 275625 / 525 = 525.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Since 525 * MP = 275625 ends in 25 and 525 = 21 * 25, test MP = 525: 525^2 = (52 * 53) concatenated with 25 = 275625! Exact match!
- **Boundary Conditions & Trap Alert**: Recognizing 275625 = 525^2 via the (n*10 + 5)^2 shortcut makes the final division instantaneous.
- **Verification Audit**: Total units = 120 + 135 + 150 + 165 = 570. Total CP = 570 * 240 = 136800. Total SP = 136800 + 138825 = 275625. Effective MP units sold = 120(0.8) + 135(0.9) + 150(0.95) + 165(1.0) = 96 + 121.5 + 142.5 + 165 = 525. Thus MP = 275625 / 525 = 525.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q17</summary>

- **Trigger**: Notice monthly sales (120, 135, 150, 165) form an AP with mean 142.5 (total = 4 * 142.5 = 570), and effective MP coefficient is 96 + 121.5 + 142.5 + 165 = 525!
- **Answer**: **(A) 525**
- **Trap to Avoid**: Recognizing 275625 = 525^2 via the (n*10 + 5)^2 shortcut makes the final division instantaneous.
</details>

### Q18 (`CAT2025_S3_QA_Q18`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Geometry & Mensuration $\rightarrow$ *Lines, Angles & Triangles*
- **Core Concept Tested**: Altitudes of an isosceles triangle via area invariance (a*h_a = b*h_b = c*h_c = 2*Area)
- **Verified Answer**: **126** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Split the 50-50-80 triangle into two 30-40-50 right triangles; then h_b = h_c = (80 * 30)/50 = 48!
- **Method 1 (First-Principles Derivation)**: Drop altitude h_a to BC = 80: by Pythagoras on half-base 40 and hypotenuse 50, h_a = 30 cm. By area invariance, 50 * h_b = 50 * h_c = 80 * 30 = 2400 => h_b = h_c = 48 cm. Sum = 30 + 48 + 48 = 126 cm.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: h_a = 30, h_b = h_c = 48 -> 30 + 96 = 126.
- **Boundary Conditions & Trap Alert**: Remember there are THREE altitudes (count both equal altitudes of length 48).
- **Verification Audit**: In isosceles triangle ABC (50, 50, 80), altitude to base 80 is sqrt(50^2 - 40^2) = 30 cm, and Area = 0.5 * 80 * 30 = 1200 sq cm. Altitudes to the two equal sides of 50 cm are each 2*1200 / 50 = 48 cm. Sum of altitudes = 30 + 48 + 48 = 126 cm.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q18</summary>

- **Trigger**: Split the 50-50-80 triangle into two 30-40-50 right triangles; then h_b = h_c = (80 * 30)/50 = 48!
- **Answer**: **126**
- **Trap to Avoid**: Remember there are THREE altitudes (count both equal altitudes of length 48).
</details>

### Q19 (`CAT2025_S3_QA_Q19`) — [TITA | Medium | `Round_2_Doable`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Inequalities & Modulus*
- **Core Concept Tested**: Bounded ratio extrema with perfect-square domain endpoints
- **Verified Answer**: **397** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Convert 0.3q <= p <= 0.7q into fractions of S = p + q: (3/13)S <= p <= (7/17)S! Notice 416 = 900 - 484 is divisible by 13, and 731 = 900 - 169 is divisible by 17!
- **Method 1 (First-Principles Derivation)**: Since p + q = 900 - r and 3/10 <= p/q <= 7/10, p/(p+q) lies in [3/13, 7/17]. For r in {13^2=169, ..., 22^2=484}: to minimize p, take largest r = 484 (p+q = 416), giving p_min = (3/13)*416 = 96. To maximize p, take smallest r = 169 (p+q = 731), giving p_max = (7/17)*731 = 301. Sum = 96 + 301 = 397.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 900 - 22^2 = 416 = 13 * 32 => p_min = 3 * 32 = 96; 900 - 13^2 = 731 = 17 * 43 => p_max = 7 * 43 = 301. Sum = 397.
- **Boundary Conditions & Trap Alert**: The divisibility of 416 by 13 and 731 by 17 confirms you have the exact intended boundary squares (484 and 169).
- **Verification Audit**: Perfect squares r in (150, 500) range from 13^2 = 169 to 22^2 = 484, so S = p + q = 900 - r ranges from 416 (at r=484) to 731 (at r=169). Since 0.3q <= p <= 0.7q, we have (3/13)S <= p <= (7/17)S. Minimum p at S = 416: p >= (3/13)*416 = 96. Maximum p at S = 731: p <= (7/17)*731 = 7 * 43 = 301. Sum = 96 + 301 = 397.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q19</summary>

- **Trigger**: Convert 0.3q <= p <= 0.7q into fractions of S = p + q: (3/13)S <= p <= (7/17)S! Notice 416 = 900 - 484 is divisible by 13, and 731 = 900 - 169 is divisible by 17!
- **Answer**: **397**
- **Trap to Avoid**: The divisibility of 416 by 13 and 731 by 17 confirms you have the exact intended boundary squares (484 and 169).
</details>

### Q20 (`CAT2025_S3_QA_Q20`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Arithmetic $\rightarrow$ *Averages, Mixtures & Alligations*
- **Core Concept Tested**: Weighted percentage contribution to overall mean shift
- **Verified Answer**: **(B) 54000** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: If a 20% raise for managers produces a 5% raise in the overall mean, managers hold 5/20 = 25% of the total wage pool, so engineers hold 75% of the total wage pool!
- **Method 1 (First-Principles Derivation)**: Total initial salary = 30 * 60000 = 1800000. Increase = 5% of 1800000 = 90000 = 20% of managers' total salary => managers' total = 450000. Engineers' total = 1800000 - 450000 = 1350000 across 25 engineers => average = 1350000 / 25 = 54000.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Engineers get 75% of total pay while being 25/30 = 5/6 of the headcount, so their average is (3/4) / (5/6) * 60000 = (9/10) * 60000 = 54000!
- **Boundary Conditions & Trap Alert**: None; 15-second sitter.
- **Verification Audit**: A 20% increase in managers' total salary raises the overall company salary bill by 5%, so managers account for 5% / 20% = 1/4 = 25% of the total salary bill, while the 25 engineers account for 75% of the total salary bill (0.75 * 30 * 60000 = 1350000). Average engineer salary = 1350000 / 25 = 54000.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q20</summary>

- **Trigger**: If a 20% raise for managers produces a 5% raise in the overall mean, managers hold 5/20 = 25% of the total wage pool, so engineers hold 75% of the total wage pool!
- **Answer**: **(B) 54000**
- **Trap to Avoid**: None; 15-second sitter.
</details>

### Q21 (`CAT2025_S3_QA_Q21`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Linear Equations & Indeterminate Systems*
- **Core Concept Tested**: Three-variable linear system optimization with ordering constraint S <= A
- **Verified Answer**: **700** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Take Rs 1000 (Arts fee) as the assumed baseline: total fee 15,50,000 exceeds 1500 * 1000 by +50,000, so +100*S - 200*C = 50,000 => S - 2C = 500!
- **Method 1 (First-Principles Derivation)**: Deviation from Rs 1000/student: 100S + 0A - 200C = 50000 => S = 500 + 2C. Since S + A + C = 1500 and S <= A, we have 2S + C <= 1500 => 2(500 + 2C) + C <= 1500 => 5C <= 500 => C <= 100. Thus max S = 500 + 2(100) = 700.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: To maximize S with S <= A, set S = A: then 2S + C = 1500 and S - 2C = 500 => C = 100, S = 700.
- **Boundary Conditions & Trap Alert**: 'Not more than' means S <= A (equality S = A = 700 is permitted).
- **Verification Audit**: S + A + C = 1500 and 11S + 10A + 8C = 15500. Subtracting 10(S + A + C) = 15000 gives S - 2C = 500 => C = (S - 500)/2. Given S <= A = 1500 - S - C => 2S + (S - 500)/2 <= 1500 => 5S <= 3500 => S <= 700 (achieved at S = 700, A = 700, C = 100).

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q21</summary>

- **Trigger**: Take Rs 1000 (Arts fee) as the assumed baseline: total fee 15,50,000 exceeds 1500 * 1000 by +50,000, so +100*S - 200*C = 50,000 => S - 2C = 500!
- **Answer**: **700**
- **Trap to Avoid**: 'Not more than' means S <= A (equality S = A = 700 is permitted).
</details>

### Q22 (`CAT2025_S3_QA_Q22`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Algebra $\rightarrow$ *Sequences & Series*
- **Core Concept Tested**: Symmetric AP mean properties (T4 + T7 + T10 = 3*T7 and S5 = 5*T3)
- **Verified Answer**: **65** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: T4 + T7 + T10 = 3*T7 gives T7 = 33 immediately; S14/14 = 35.5 = T7 + 0.5d gives 0.5d = 2.5 => d = 5!
- **Method 1 (First-Principles Derivation)**: From T4 + T7 + T10 = 3(a + 6d) = 99, a + 6d = 33. From S14 = 7(2a + 13d) = 497, 2a + 13d = 71. Solving gives d = 5 and a = 3. Finally, S5 = 5(a + 2d) = 5(3 + 10) = 65.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Average of first 14 terms is T_7.5 = 497/14 = 35.5. Since T_7 = 99/3 = 33, half-step 0.5d = 2.5 => d = 5! Then T_3 = T_7 - 4d = 33 - 20 = 13, and S_5 = 5 * T_3 = 65!
- **Boundary Conditions & Trap Alert**: Using S_{2k-1} = (2k-1)*T_k avoids computing the first term a.
- **Verification Audit**: In AP, T4 + T7 + T10 = 3 * T7 = 99 => T7 = a + 6d = 33. Also S14 = 7*(2a + 13d) = 497 => 2a + 13d = 71. Subtracting 2(a + 6d) = 66 gives d = 5, a = 3. Then S5 = 5 * T3 = 5 * (a + 2d) = 5 * 13 = 65.

<details><summary>Active-Recall Self-Test: CAT2025_S3_QA_Q22</summary>

- **Trigger**: T4 + T7 + T10 = 3*T7 gives T7 = 33 immediately; S14/14 = 35.5 = T7 + 0.5d gives 0.5d = 2.5 => d = 5!
- **Answer**: **65**
- **Trap to Avoid**: Using S_{2k-1} = (2k-1)*T_k avoids computing the first term a.
</details>
