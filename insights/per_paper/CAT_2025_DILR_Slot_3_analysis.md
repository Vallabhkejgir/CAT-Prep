# Pass 1 Master Analysis: CAT 2025 DILR Slot 3

## 1. Executive Summary & Exam-Hall Blueprint
- **Section**: DILR | **Slot**: Slot 3 (CAT 2025)
- **Source Document**: `docs/pyqs/2025/DILR_Slot_3_QP_edd269e2f55435bb1244b866ae3981ff.pdf`
- **Total Questions**: 22 (11 MCQs, 11 TITA)
- **Difficulty Breakdown**: Easy: **13** | Medium: **7** | Hard: **2**
- **Round-Wise Triage**: Round 1 Sitters: **20** | Round 2 Doables: **2** | Round 3 Time-Sinks: **0**
- **Answer Verification Protocol**: 3-Layer Autonomous Verification (`ai_verified_derivation` — First-Principles Algebraic/Logical Derivation + Programmatic/Cross-Clue Verification + 30-Second Speed Shortcut)

### Percentile Score & Attempt Targets (40-Minute Clock)
| Percentile Target | Scaled Raw Score Target | Net Correct Equivalent | Recommended Execution Strategy |
| :---: | :---: | :---: | :--- |
| **95%ile** | 26-29 (9-10 net) | ~9-11 questions | Clear all Easy Round-1 sitters + all TITA questions with zero negative risk |
| **99%ile** | 36-39 (12-13 net) | ~12-15 questions | Sweep Round 1 in 22 mins + cherry-pick 4-5 Round 2 medium questions |
| **99.5%ile** | 42-45 (14-15 net) | ~15-17 questions | Full Round 1 sweep + 70% of Round 2 using option/parity/invariant shortcuts |
| **99.9%ile** | 50+ (17+ net) | ~17-19 questions | Complete mastery of Round 1 + Round 2 with <90s average per sitter |

### Topic & Sub-Topic Distribution
| Canonical Topic | Canonical Sub-Topic | Question Count | Question IDs |
| :--- | :--- | :---: | :--- |
| **Linear, Circular & 2D Matrix Arrangements** | Circular seating with modular step transitions | 4 | Q14, Q15, Q16, Q17 |
| **Quant-Based LR & Algorithmic Puzzles** | Currency exchange rates & linear constraint puzzles | 5 | Q5, Q6, Q7, Q8, Q9 |
| **Quantitative & Reasoning-Based DI** | Bilateral trade matrices & normalized trade balance | 5 | Q18, Q19, Q20, Q21, Q22 |
| **Quantitative & Reasoning-Based DI** | Cumulative step-function progress charts | 4 | Q10, Q11, Q12, Q13 |
| **Quantitative & Reasoning-Based DI** | Missing-value tables & bipartite flow conservation | 4 | Q1, Q2, Q3, Q4 |

---

## 2. Quick-Reference Verified Answer Key
| Q# | Question ID | Type | Difficulty | Round Tag | Verified Answer | Core Concept / Mental Trigger |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| **Q1** | `CAT2025_S3_DILR_Q01` | TITA | Easy | `Round_1_Sitter` | **50** | 2-node intra-group flow identity in grouped call tables |
| **Q2** | `CAT2025_S3_DILR_Q02` | TITA | Easy | `Round_1_Sitter` | **525** | Cross-operator bipartite flow conservation (Sum Out(X->Y) = Sum In(Y<-X)) |
| **Q3** | `CAT2025_S3_DILR_Q03` | TITA | Easy | `Round_1_Sitter` | **350** | Intra-operator flow conservation (Sum Out(Y->Y) = Sum In(Y<-Y)) |
| **Q4** | `CAT2025_S3_DILR_Q04` | MCQ | Easy | `Round_1_Sitter` | **(C) 100** | Zero-edge elimination in a 4-node directed call graph |
| **Q5** | `CAT2025_S3_DILR_Q05` | TITA | Medium | `Round_1_Sitter` | **41000** | Cross-currency equivalence from dual-currency observations of the same traveler |
| **Q6** | `CAT2025_S3_DILR_Q06` | TITA | Easy | `Round_1_Sitter` | **13000** | Travel Cost decomposition (Spend = Travel Cost - Flight Cost) |
| **Q7** | `CAT2025_S3_DILR_Q07` | TITA | Easy | `Round_1_Sitter` | **1500** | Currency conversion of Flight Cost into Aurels |
| **Q8** | `CAT2025_S3_DILR_Q08` | MCQ | Easy | `Round_1_Sitter` | **(C) 8** | Chained exchange rate ratio |
| **Q9** | `CAT2025_S3_DILR_Q09` | MCQ | Easy | `Round_1_Sitter` | **(B) Jano spent 2000 in Aurevia** | Verification of local-currency spend allocations |
| **Q10** | `CAT2025_S3_DILR_Q10` | MCQ | Easy | `Round_1_Sitter` | **(B) Koushik** | Reading cumulative step functions at a vertical time slice (t = 20) |
| **Q11** | `CAT2025_S3_DILR_Q11` | TITA | Medium | `Round_1_Sitter` | **2** | Aligning cumulative total vs category-subset step functions to extract individual task duration |
| **Q12** | `CAT2025_S3_DILR_Q12` | TITA | Medium | `Round_1_Sitter` | **6** | Sequence classification by matching jump timestamps between Total and Subset step charts |
| **Q13** | `CAT2025_S3_DILR_Q13` | MCQ | Medium | `Round_1_Sitter` | **(C) 4.0 minutes** | Complementary duration sum (Total Time - Visual Time = Number-Based Time) |
| **Q14** | `CAT2025_S3_DILR_Q14` | MCQ | Medium | `Round_1_Sitter` | **(D) Eshan** | Modular arithmetic (+1, +2, -1, -2 mod 7) on a 7-seat circle |
| **Q15** | `CAT2025_S3_DILR_Q15` | MCQ | Easy | `Round_1_Sitter` | **(B) Chirag** | Circular offset lookup |
| **Q16** | `CAT2025_S3_DILR_Q16` | MCQ | Hard | `Round_2_Doable` | **(D) Immediately to the right** | Modular wrap-around equivalence (+1 + 2 == -2 - 2 mod 7) |
| **Q17** | `CAT2025_S3_DILR_Q17` | MCQ | Hard | `Round_2_Doable` | **(B) Gaurav** | Intermediate state reachability in 2-step modular paths |
| **Q18** | `CAT2025_S3_DILR_Q18` | TITA | Easy | `Round_1_Sitter` | **48** | Normalized Trade Balance conversion (NTB = k => E/I = (1+k)/(1-k)) |
| **Q19** | `CAT2025_S3_DILR_Q19` | TITA | Medium | `Round_1_Sitter` | **200** | 2x2 linear flow system for total imports/exports |
| **Q20** | `CAT2025_S3_DILR_Q20` | TITA | Medium | `Round_1_Sitter` | **1008** | Composite region internal trade (ROW -> ROW) |
| **Q21** | `CAT2025_S3_DILR_Q21` | MCQ | Easy | `Round_1_Sitter` | **(A) 200** | Zero-sum global conservation of trade balances (Sum(TB) = 0) |
| **Q22** | `CAT2025_S3_DILR_Q22` | MCQ | Easy | `Round_1_Sitter` | **(A) Both X and C** | Total trade (E + I) comparison |

---

## 3. Question-by-Question High-Recall Decomposition (Dual-Method)

### Q1 (`CAT2025_S3_DILR_Q01`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Missing-value tables & bipartite flow conservation*
- **Core Concept Tested**: 2-node intra-group flow identity in grouped call tables
- **Verified Answer**: **50** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Since Xitel has ONLY two users (Anu and Bijay), Anu's Outgoing-to-Xitel IS Anu->Bijay (100), and Anu's Incoming-from-Xitel IS Bijay->Anu (50)!
- **Method 1 (First-Principles Derivation)**: The six friends are partitioned into Xitel = {Anu, Bijay} and Yocel = {Chetan, Deepak, Eshan, Faruq}. Because no friend calls themselves, any call between Xitel users is either Anu->Bijay or Bijay->Anu. From the table, Anu's Incoming minutes from Operator Xitel is 50, which equals the duration of calls from Bijay to Anu.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Direct 5-second read from the Xitel 2-person sub-block: Anu's In<-Xitel = 50 = Bijay->Anu!
- **Boundary Conditions & Trap Alert**: Do not confuse Anu->Bijay (100, Anu's Out->Xitel) with Bijay->Anu (50, Anu's In<-Xitel).
- **Verification Audit**: Only Anu and Bijay use Operator Xitel. From the table, Anu's Incoming minutes from Operator Xitel = 50. Since Anu cannot call herself, all 50 minutes of Incoming Xitel calls to Anu must come from Bijay!

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q01</summary>

- **Trigger**: Since Xitel has ONLY two users (Anu and Bijay), Anu's Outgoing-to-Xitel IS Anu->Bijay (100), and Anu's Incoming-from-Xitel IS Bijay->Anu (50)!
- **Answer**: **50**
- **Trap to Avoid**: Do not confuse Anu->Bijay (100, Anu's Out->Xitel) with Bijay->Anu (50, Anu's In<-Xitel).
</details>

### Q2 (`CAT2025_S3_DILR_Q02`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Missing-value tables & bipartite flow conservation*
- **Core Concept Tested**: Cross-operator bipartite flow conservation (Sum Out(X->Y) = Sum In(Y<-X))
- **Verified Answer**: **525** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Total Outgoing from Xitel to Yocel (Anu + Bijay) MUST equal Total Incoming from Xitel to Yocel (Chetan + Deepak + Eshan + Faruq)!
- **Method 1 (First-Principles Derivation)**: Every call from a Xitel user (A, B) to a Yocel user (C, D, E, F) is recorded in Outgoing-to-Yocel for {A, B} and in Incoming-from-Xitel for {C, D, E, F}. Summing Incoming-from-Xitel for C, D, E, F gives 250 + 275 + 100 + 100 = 725. Subtracting Bijay's Outgoing-to-Yocel (200) gives Anu's Outgoing-to-Yocel = 725 - 200 = 525.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: (250 + 275 + 100 + 100) - 200 = 525 in 10 seconds!
- **Boundary Conditions & Trap Alert**: Never try to find individual A->C, A->D, A->E, A->F calls to answer Q2; block conservation gives the sum directly.
- **Verification Audit**: Total Incoming minutes from Xitel received by Yocel friends (C, D, E, F) = 250 + 275 + 100 + 100 = 725. This must equal Total Outgoing minutes to Yocel made by Xitel friends (Anu and Bijay). Since Bijay's Outgoing to Yocel = 200, Anu's Outgoing to Yocel = 725 - 200 = 525.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q02</summary>

- **Trigger**: Total Outgoing from Xitel to Yocel (Anu + Bijay) MUST equal Total Incoming from Xitel to Yocel (Chetan + Deepak + Eshan + Faruq)!
- **Answer**: **525**
- **Trap to Avoid**: Never try to find individual A->C, A->D, A->E, A->F calls to answer Q2; block conservation gives the sum directly.
</details>

### Q3 (`CAT2025_S3_DILR_Q03`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Missing-value tables & bipartite flow conservation*
- **Core Concept Tested**: Intra-operator flow conservation (Sum Out(Y->Y) = Sum In(Y<-Y))
- **Verified Answer**: **350** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Within Operator Yocel (C, D, E, F), sum of Outgoing-to-Yocel MUST equal sum of Incoming-from-Yocel!
- **Method 1 (First-Principles Derivation)**: Summing Incoming-from-Yocel across C, D, E, F gives 150 + 100 + 375 + 150 = 775. Summing known Outgoing-to-Yocel across C, D, E gives 175 + 150 + 100 = 425. Therefore, Faruq's Outgoing-to-Yocel = 775 - 425 = 350.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: (150 + 100 + 375 + 150) - (175 + 150 + 100) = 775 - 425 = 350 in 10 seconds!
- **Boundary Conditions & Trap Alert**: Do not include Anu and Bijay's Incoming-from-Yocel when balancing Yocel-to-Yocel internal calls!
- **Verification Audit**: Total Incoming minutes from Yocel received by Yocel friends (C, D, E, F) = 150 + 100 + 375 + 150 = 775. This must equal Total Outgoing minutes to Yocel made by Yocel friends (C, D, E, F) = 175 + 150 + 100 + Faruq = 425 + Faruq. Thus Faruq's Outgoing to Yocel = 775 - 425 = 350.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q03</summary>

- **Trigger**: Within Operator Yocel (C, D, E, F), sum of Outgoing-to-Yocel MUST equal sum of Incoming-from-Yocel!
- **Answer**: **350**
- **Trap to Avoid**: Do not include Anu and Bijay's Incoming-from-Yocel when balancing Yocel-to-Yocel internal calls!
</details>

### Q4 (`CAT2025_S3_DILR_Q04`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Missing-value tables & bipartite flow conservation*
- **Core Concept Tested**: Zero-edge elimination in a 4-node directed call graph
- **Verified Answer**: **(C) 100** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Start with Eshan's Out->Yocel (100): since E->C = 0 and E->D = 0, E->F = 100 is forced, which cascades through F_in -> C->F -> C->E -> D->E -> D->C = 100!
- **Method 1 (First-Principles Derivation)**: 1) E_out_Y = 100 with E->C = E->D = 0 => E->F = 100. 2) F_in_Y = 150 with D->F = 0 and E->F = 100 => C->F = 50. 3) C_out_Y = 175 with C->D = 0 and C->F = 50 => C->E = 125. 4) E_in_Y = 375 with F->E = 200 and C->E = 125 => D->E = 50. 5) D_out_Y = 150 with D->F = 0 and D->E = 50 => D->C = 100.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 5-step domino chain inside the 4x4 Yocel sub-matrix takes 30 seconds and requires zero Xitel variables!
- **Boundary Conditions & Trap Alert**: Set 1 is the #1 must-pick sitter set of DILR Slot 3 (all 4 questions solvable in under 3 minutes).
- **Verification Audit**: Within Yocel {C, D, E, F}: E->C = 0 and E->D = 0 (Clue iv), so E's Out->Yocel (100) is entirely E->F = 100. Since F's In<-Yocel = 150 and D->F = 0 (Clue iii), C->F = 150 - 100 = 50. Since C's Out->Yocel = 175 and C->D = 0 (Clue ii), C->E = 175 - 50 = 125. Since E's In<-Yocel = 375 and F->E = 200 (given), D->E = 375 - 200 - 125 = 50. Finally, since D's Out->Yocel = 150 and D->F = 0, D->C = 150 - 50 = 100.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q04</summary>

- **Trigger**: Start with Eshan's Out->Yocel (100): since E->C = 0 and E->D = 0, E->F = 100 is forced, which cascades through F_in -> C->F -> C->E -> D->E -> D->C = 100!
- **Answer**: **(C) 100**
- **Trap to Avoid**: Set 1 is the #1 must-pick sitter set of DILR Slot 3 (all 4 questions solvable in under 3 minutes).
</details>

### Q5 (`CAT2025_S3_DILR_Q05`) — [TITA | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Currency exchange rates & linear constraint puzzles*
- **Core Concept Tested**: Cross-currency equivalence from dual-currency observations of the same traveler
- **Verified Answer**: **41000** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Kira visited both Aurevia and Brelosia, so her total Travel Cost is reported in BOTH currencies: 8000 Aurels = 4000 Brins => 1 Brin = 2 Aurels immediately!
- **Method 1 (First-Principles Derivation)**: 1) 1 Crown = 0.5 Zentars => TC_L = 36000 * 0.5 = 18000 Zentars. 2) TC_K = 8000 Aurels = 4000 Brins => 1 Brin = 2 Aurels. Let 1 Aurel = x Zentars, so 1 Brin = 2x Zentars. 3) Local spends: L in B = 3000 (the only 3000), K in B = 2000 => K in A = 1000 (since K's two spends are distinct and != 3000). Thus TC_K = Flight_K + 1000x + 2000(2x) = Flight_K + 5000x = 8000x => Flight_K = 3000x. Since Flight_K in {5000, 6000}, 3000x = 6000 => x = 2 Zentars/Aurel, Flight_K = 6000, Flight_L = 5000! 4) Sum of Travel Costs = 3500(2) + 8000(2) + 18000 = 7000 + 16000 + 18000 = 41000 Zentars.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Look at Kira: TC_K = 8000 Aurels, and she spent 1000 Aurels in A + 2000 Brins (= 4000 Aurels) in B = 5000 Aurels total spend! So Kira's Flight Cost = 8000 - 5000 = 3000 Aurels = 6000 Zentars => 1 Aurel = 2 Zentars! Then (3500 + 8000)*2 + 18000 = 41000!
- **Boundary Conditions & Trap Alert**: Converting Kira's Brelosia spend (2000 Brins) into Aurels (4000 Aurels) via 8000 Aurels = 4000 Brins solves the exchange rate in one line!
- **Verification Audit**: Given 1 Crown = 0.5 Zentars => Lian's Travel Cost = 36000 Crowns = 18000 Zentars. Kira's Travel Cost = 8000 Aurels = 4000 Brins => 1 Brin = 2 Aurels. Spends in Brelosia: Kira = 2000 Brins, Lian = 3000 Brins (the unique 3000 spend). Since Lian visited B and C with different local spends and two 1000s are used by Kira (in A) and Jano, Lian spent 2000 Crowns (= 1000 Zentars) in C. Thus Lian's Flight Cost + 3000 Brins + 1000 Zentars = 18000 Zentars. With Lian's Flight Cost = 5000 Zentars, 3000 Brins = 12000 Zentars => 1 Brin = 4 Zentars, 1 Aurel = 2 Zentars. Then TC_Jano = 3500 Aurels = 7000 Zentars, TC_Kira = 4000 Brins = 16000 Zentars, TC_Lian = 18000 Zentars. Sum = 7000 + 16000 + 18000 = 41000.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q05</summary>

- **Trigger**: Kira visited both Aurevia and Brelosia, so her total Travel Cost is reported in BOTH currencies: 8000 Aurels = 4000 Brins => 1 Brin = 2 Aurels immediately!
- **Answer**: **41000**
- **Trap to Avoid**: Converting Kira's Brelosia spend (2000 Brins) into Aurels (4000 Aurels) via 8000 Aurels = 4000 Brins solves the exchange rate in one line!
</details>

### Q6 (`CAT2025_S3_DILR_Q06`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Currency exchange rates & linear constraint puzzles*
- **Core Concept Tested**: Travel Cost decomposition (Spend = Travel Cost - Flight Cost)
- **Verified Answer**: **13000** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Spend_L = TC_L (18000 Zentars) - Flight_L (5000 Zentars) = 13000 Zentars.
- **Method 1 (First-Principles Derivation)**: Lian's total Travel Cost is 36000 Crowns * 0.5 = 18000 Zentars, and his Flight Cost is 5000 Zentars. Subtracting gives 18000 - 5000 = 13000 Zentars.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 18000 - 5000 = 13000.
- **Boundary Conditions & Trap Alert**: Do not include Flight Cost (5000) when asked for money spent in the two countries visited.
- **Verification Audit**: Lian's Travel Cost = 18000 Zentars and Lian's Flight Cost = 5000 Zentars (since Kira's Flight Cost is 6000 Zentars). Thus Lian spent 18000 - 5000 = 13000 Zentars in the two countries (3000 Brins * 4 = 12000 Zentars in Brelosia + 2000 Crowns * 0.5 = 1000 Zentars in Cyrenia).

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q06</summary>

- **Trigger**: Spend_L = TC_L (18000 Zentars) - Flight_L (5000 Zentars) = 13000 Zentars.
- **Answer**: **13000**
- **Trap to Avoid**: Do not include Flight Cost (5000) when asked for money spent in the two countries visited.
</details>

### Q7 (`CAT2025_S3_DILR_Q07`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Currency exchange rates & linear constraint puzzles*
- **Core Concept Tested**: Currency conversion of Flight Cost into Aurels
- **Verified Answer**: **1500** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Since 1 Aurel = 2 Zentars, Jano's Flight Cost of 4000 Zentars is 2000 Aurels; subtract from TC_J = 3500 Aurels -> 1500 Aurels!
- **Method 1 (First-Principles Derivation)**: TC_J = 3500 Aurels and Flight_J = 4000 Zentars = 2000 Aurels. Therefore, Jano's total spend in Aurels is 3500 - 2000 = 1500 Aurels.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 3500 - (4000 / 2) = 1500.
- **Boundary Conditions & Trap Alert**: Pay attention to the requested currency unit ('in Aurels' = 1500, not 'in Zentars' = 3000).
- **Verification Audit**: Jano's Travel Cost in Aurels = 3500 Aurels. Jano's Flight Cost = 4000 Zentars = 4000 / 2 = 2000 Aurels. Thus Jano's total spend in the two countries, in Aurels, is 3500 - 2000 = 1500 Aurels.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q07</summary>

- **Trigger**: Since 1 Aurel = 2 Zentars, Jano's Flight Cost of 4000 Zentars is 2000 Aurels; subtract from TC_J = 3500 Aurels -> 1500 Aurels!
- **Answer**: **1500**
- **Trap to Avoid**: Pay attention to the requested currency unit ('in Aurels' = 1500, not 'in Zentars' = 3000).
</details>

### Q8 (`CAT2025_S3_DILR_Q08`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Currency exchange rates & linear constraint puzzles*
- **Core Concept Tested**: Chained exchange rate ratio
- **Verified Answer**: **(C) 8** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: 1 Brin = 4 Zentars and 1 Zentar = 2 Crowns => 1 Brin = 8 Crowns.
- **Method 1 (First-Principles Derivation)**: Since 1 Brin = 4 Zentars and 1 Crown = 0.5 Zentars, 1 Brin = 4 / 0.5 = 8 Crowns.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 4 / 0.5 = 8 (Option C).
- **Boundary Conditions & Trap Alert**: Do not invert the ratio (1/8 = 0.125 is distractor D).
- **Verification Audit**: 1 Brin = 4 Zentars and 1 Crown = 0.5 Zentars => 1 Brin = 4 / 0.5 = 8 Crowns.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q08</summary>

- **Trigger**: 1 Brin = 4 Zentars and 1 Zentar = 2 Crowns => 1 Brin = 8 Crowns.
- **Answer**: **(C) 8**
- **Trap to Avoid**: Do not invert the ratio (1/8 = 0.125 is distractor D).
</details>

### Q9 (`CAT2025_S3_DILR_Q09`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Currency exchange rates & linear constraint puzzles*
- **Core Concept Tested**: Verification of local-currency spend allocations
- **Verified Answer**: **(B) Jano spent 2000 in Aurevia** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Since Jano's TOTAL spend across both countries is 1500 Aurels (Q7), he could NOT have spent 2000 Aurels in Aurevia alone!
- **Method 1 (First-Principles Derivation)**: Jano's total spend in both countries is 1500 Aurels. Spending 1000 Aurels in Aurevia and 2000 Crowns (= 1000 Zentars = 500 Aurels) in Cyrenia sums to 1500 Aurels and satisfies the global count of two 1000s (Kira in A, Jano in A). Thus (A), (C), and (D) are true, while (B) is false.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Q7 already showed Jano's total spend in Aurels is 1500 < 2000, so (B) 'Jano spent 2000 in Aurevia' is immediately impossible!
- **Boundary Conditions & Trap Alert**: Set 2 is the #2 must-pick sitter set of DILR Slot 3 (5 questions in ~4 minutes).
- **Verification Audit**: From Q7, Jano's total spend in Aurevia and Cyrenia equals 1500 Aurels. If Jano spent 2000 Aurels in Aurevia alone, his total spend would exceed 1500 Aurels! In fact, Jano spent 1000 Aurels in Aurevia and 2000 Crowns (= 500 Aurels) in Cyrenia (1000 + 500 = 1500 Aurels). Thus (B) is NOT true.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q09</summary>

- **Trigger**: Since Jano's TOTAL spend across both countries is 1500 Aurels (Q7), he could NOT have spent 2000 Aurels in Aurevia alone!
- **Answer**: **(B) Jano spent 2000 in Aurevia**
- **Trap to Avoid**: Set 2 is the #2 must-pick sitter set of DILR Slot 3 (5 questions in ~4 minutes).
</details>

### Q10 (`CAT2025_S3_DILR_Q10`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Cumulative step-function progress charts*
- **Core Concept Tested**: Reading cumulative step functions at a vertical time slice (t = 20)
- **Verified Answer**: **(B) Koushik** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Look vertically above Time = 20 on the 'All puzzles' chart: the highest step-line is Green (Koushik) at y = 7!
- **Method 1 (First-Principles Derivation)**: At Time = 20 min, reading the vertical slice on the 'All puzzles' chart gives: Koushik = 7 (completed at min 19), Chandranath = 5 (completed at min 17, 6th at min 21), Anirbid = 5 (completed at min 19), Suranjan = 4 (completed at min 18). Thus Koushik had solved the largest number of puzzles.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Direct visual read at t = 20 -> Green line (Koushik) is highest at 7 puzzles.
- **Boundary Conditions & Trap Alert**: Although Chandranath wins the overall race (finishing Puzzle 10 at t = 30 vs Koushik at t = 31), Koushik leads at t = 20!
- **Verification Audit**: At t = 20 minutes on the left chart ('All puzzles'), Koushik (green curve) is at 7 puzzles (having solved Puzzle 7 at t = 19), whereas Chandranath is at 5, Anirbid is at 5, and Suranjan is at 4.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q10</summary>

- **Trigger**: Look vertically above Time = 20 on the 'All puzzles' chart: the highest step-line is Green (Koushik) at y = 7!
- **Answer**: **(B) Koushik**
- **Trap to Avoid**: Although Chandranath wins the overall race (finishing Puzzle 10 at t = 30 vs Koushik at t = 31), Koushik leads at t = 20!
</details>

### Q11 (`CAT2025_S3_DILR_Q11`) — [TITA | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Cumulative step-function progress charts*
- **Core Concept Tested**: Aligning cumulative total vs category-subset step functions to extract individual task duration
- **Verified Answer**: **2** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Find when Suranjan's Visual count jumps from 2 to 3 (at t = 28 min), then look at the 'All puzzles' chart at t = 28 min (Puzzle 8) and subtract the completion time of Puzzle 7 (t = 26 min) -> 28 - 26 = 2 min!
- **Method 1 (First-Principles Derivation)**: Every jump in the 'Visual puzzles' chart coincides with a jump in the 'All puzzles' chart. For Suranjan, the jump to 3 visual puzzles occurs at t = 28 min, which corresponds to Puzzle 8 on the 'All puzzles' chart. Suranjan completed Puzzle 7 at t = 26 min, so he spent 28 - 26 = 2 minutes on Puzzle 8.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Time of Visual #3 completion (28) minus Time of previous All-Puzzle completion (26) = 2 minutes.
- **Boundary Conditions & Trap Alert**: Never subtract the completion time of Visual #2 (t = 18) from Visual #3 (t = 28) — that 10-minute gap includes Puzzles 5, 6, and 7 (which were number-based puzzles)!
- **Verification Audit**: From the right chart ('Visual puzzles'), Suranjan (blue) finishes Visual Puzzle 3 at t = 28 min. On the left chart ('All puzzles'), Suranjan finishes a puzzle at t = 28 min (Puzzle 8), having finished the previous puzzle (Puzzle 7) at t = 26 min. Since a competitor gets access to a puzzle as soon as they solve the previous puzzle, Suranjan took 28 - 26 = 2 minutes to solve the third visual puzzle.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q11</summary>

- **Trigger**: Find when Suranjan's Visual count jumps from 2 to 3 (at t = 28 min), then look at the 'All puzzles' chart at t = 28 min (Puzzle 8) and subtract the completion time of Puzzle 7 (t = 26 min) -> 28 - 26 = 2 min!
- **Answer**: **2**
- **Trap to Avoid**: Never subtract the completion time of Visual #2 (t = 18) from Visual #3 (t = 28) — that 10-minute gap includes Puzzles 5, 6, and 7 (which were number-based puzzles)!
</details>

### Q12 (`CAT2025_S3_DILR_Q12`) — [TITA | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Cumulative step-function progress charts*
- **Core Concept Tested**: Sequence classification by matching jump timestamps between Total and Subset step charts
- **Verified Answer**: **6** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Track Koushik's jumps: Visual jumps at t = 2 (P1), 12 (P4), 25 (P8), 29 (P9) -> non-visual (number-based) puzzles are P2, P3, P5, P6 (4th!), P7, P10!
- **Method 1 (First-Principles Derivation)**: Since all competitors solve the 10 puzzles in the exact same sequence, match the jump timestamps of any single competitor across the two charts. For Koushik, Puzzles 1..10 finish at minutes (2, 4, 7, 12, 14, 16, 19, 25, 29, 31), and Visual Puzzles 1..4 finish at minutes (2, 12, 25, 29). Hence Puzzles 1, 4, 8, 9 are visual, and Puzzles 2, 3, 5, 6, 7, 10 are number-based. The 4th number-based puzzle is #6.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Up to Puzzle 6, exactly 2 visual puzzles (P1 at t=2 and P4 at t=12) have been solved, so Puzzle 6 is the (6 - 2) = 4th number-based puzzle!
- **Boundary Conditions & Trap Alert**: Using K_number(n) = n - K_visual(n) gives 6 - 2 = 4 immediately at n = 6.
- **Verification Audit**: Comparing jump times for any competitor (e.g., Koushik): All-puzzles jumps occur at t = 2, 4, 7, 12, 14, 16, 19, 25, 29, 31 (for Puzzles 1..10), while Visual-puzzles jumps occur at t = 2, 12, 25, 29 (which are Puzzles 1, 4, 8, 9). Thus Number-based puzzles are at positions 2, 3, 5, 6, 7, 10. The 4th number-based puzzle is at position 6.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q12</summary>

- **Trigger**: Track Koushik's jumps: Visual jumps at t = 2 (P1), 12 (P4), 25 (P8), 29 (P9) -> non-visual (number-based) puzzles are P2, P3, P5, P6 (4th!), P7, P10!
- **Answer**: **6**
- **Trap to Avoid**: Using K_number(n) = n - K_visual(n) gives 6 - 2 = 4 immediately at n = 6.
</details>

### Q13 (`CAT2025_S3_DILR_Q13`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Cumulative step-function progress charts*
- **Core Concept Tested**: Complementary duration sum (Total Time - Visual Time = Number-Based Time)
- **Verified Answer**: **(C) 4.0 minutes** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Instead of summing 6 number-based puzzles, sum the 4 visual puzzles (4 + 3 + 2 + 4 = 13 min), subtract from Anirbid's finish time (37 - 13 = 24 min), and divide by 6 -> 24/6 = 4.0 min!
- **Method 1 (First-Principles Derivation)**: Anirbid's completion times for Puzzles 1..10 are (4, 9, 11, 14, 19, 22, 27, 29, 33, 37). Durations of the 6 number-based puzzles (P2, P3, P5, P6, P7, P10) are (9-4)=5, (11-9)=2, (19-14)=5, (22-19)=3, (27-22)=5, and (37-33)=4. Sum = 5 + 2 + 5 + 3 + 5 + 4 = 24 minutes. Average = 24 / 6 = 4.0 minutes.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Total time (37) - Visual durations (4 + 3 + 2 + 4 = 13) = 24 min across 6 number-based puzzles -> 24 / 6 = 4.0 minutes (Option C).
- **Boundary Conditions & Trap Alert**: There are 6 number-based puzzles (and 4 visual puzzles), not 5!
- **Verification Audit**: Anirbid (red) finishes all 10 puzzles at t = 37 min. His times on the 4 visual puzzles are: P1 (0->4 = 4 min), P4 (11->14 = 3 min), P8 (27->29 = 2 min), P9 (29->33 = 4 min), totaling 4 + 3 + 2 + 4 = 13 min. Thus his total time on the 6 number-based puzzles is 37 - 13 = 24 min, giving an average of 24 / 6 = 4.0 minutes.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q13</summary>

- **Trigger**: Instead of summing 6 number-based puzzles, sum the 4 visual puzzles (4 + 3 + 2 + 4 = 13 min), subtract from Anirbid's finish time (37 - 13 = 24 min), and divide by 6 -> 24/6 = 4.0 min!
- **Answer**: **(C) 4.0 minutes**
- **Trap to Avoid**: There are 6 number-based puzzles (and 4 visual puzzles), not 5!
</details>

### Q14 (`CAT2025_S3_DILR_Q14`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Linear, Circular & 2D Matrix Arrangements $\rightarrow$ *Circular seating with modular step transitions*
- **Core Concept Tested**: Modular arithmetic (+1, +2, -1, -2 mod 7) on a 7-seat circle
- **Verified Answer**: **(D) Eshan** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Encode 'Immediate left' = +1, 'Second left' = +2, 'Immediate right' = -1, 'Second right' = -2 (mod 7) with Bina = 0!
- **Method 1 (First-Principles Derivation)**: Setting Bina = 0 and Left = +1 (mod 7): Round 1 gives Aarav = 0 + 1 = 1. Round 2 goes to 1 - 2 = 6, and Round 3 goes to Diya = 6 - 1 = 5. From Round 5 (Aarav = 1), Round 6 (+2) goes to 3, Round 7 (+1) gives Gaurav = 4, and Round 8 (+1) lands on 5 (Diya). From 5 (Diya), Round 9 reaches Farhan and Round 10 reaches Chirag among unoccupied seats {2, 3, 6}. Since 2 cannot be reached from 5 in one step and 6 cannot reach 2 or 3 in one step, Round 9 must go 5 -> 3 (Farhan = 3) and Round 10 must go 3 -> 2 (Chirag = 2), leaving Eshan = 6 (immediately to the right of Bina).
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Modulo-7 addition fixes B=0, A=1, G=4, D=5 in 15 seconds; then 5 -> Farhan -> Chirag inside {2, 3, 6} forces Farhan=3, Chirag=2, leaving Eshan=6 (R1 of Bina)!
- **Boundary Conditions & Trap Alert**: Converting circular left/right passes into +-1, +-2 (mod 7) eliminates all spatial confusion.
- **Verification Audit**: Index seats 0..6 in the 'Immediate left' (+1) direction with Bina = 0. Round 1 (+1): Aarav = 1. Round 2 (-2): seat 1 - 2 = 6 (R1 of Bina). Round 3 (-1): Diya = seat 6 - 1 = 5. Round 5 ends at Aarav (1); Round 6 (+2): seat 3; Round 7 (+1): Gaurav = 4. Remaining seats {2, 3, 6} are {Chirag, Farhan, Eshan}. Since Round 8 (+1 from Gaurav=4) lands on Diya (5), Round 9 goes from Diya (5) to Farhan (must be seat 3 via -2, since if Farhan were at 6, Round 10 from 6 could only reach {0,1,4,5}, none of which is Chirag!), and Round 10 goes from Farhan (3) to Chirag (seat 2 via -1). Thus Eshan is at seat 6 (immediately to the right of Bina).

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q14</summary>

- **Trigger**: Encode 'Immediate left' = +1, 'Second left' = +2, 'Immediate right' = -1, 'Second right' = -2 (mod 7) with Bina = 0!
- **Answer**: **(D) Eshan**
- **Trap to Avoid**: Converting circular left/right passes into +-1, +-2 (mod 7) eliminates all spatial confusion.
</details>

### Q15 (`CAT2025_S3_DILR_Q15`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Linear, Circular & 2D Matrix Arrangements $\rightarrow$ *Circular seating with modular step transitions*
- **Core Concept Tested**: Circular offset lookup
- **Verified Answer**: **(B) Chirag** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: In our +1 = Left coordinate system, 'third to the left of Eshan (6)' is simply (6 + 3) mod 7 = 2 = Chirag!
- **Method 1 (First-Principles Derivation)**: The seating order in the left (+1) direction is 0:Bina, 1:Aarav, 2:Chirag, 3:Farhan, 4:Gaurav, 5:Diya, 6:Eshan. Moving 3 seats to the left from Eshan (6) reaches 0 (1st), 1 (2nd), 2 (3rd) = Chirag.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: (6 + 3) mod 7 = 2 -> Chirag (Option B).
- **Boundary Conditions & Trap Alert**: None; instant 5-second read from the seating circle.
- **Verification Audit**: Eshan is at seat 6. Third to the left (+3 mod 7) of seat 6 is (6 + 3) mod 7 = seat 2, which is occupied by Chirag.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q15</summary>

- **Trigger**: In our +1 = Left coordinate system, 'third to the left of Eshan (6)' is simply (6 + 3) mod 7 = 2 = Chirag!
- **Answer**: **(B) Chirag**
- **Trap to Avoid**: None; instant 5-second read from the seating circle.
</details>

### Q16 (`CAT2025_S3_DILR_Q16`) — [MCQ | Hard | `Round_2_Doable`]
- **Canonical Taxonomy**: Linear, Circular & 2D Matrix Arrangements $\rightarrow$ *Circular seating with modular step transitions*
- **Core Concept Tested**: Modular wrap-around equivalence (+1 + 2 == -2 - 2 mod 7)
- **Verified Answer**: **(D) Immediately to the right** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: On a 7-circle, moving +3 (from 5 to 1) in 2 steps can be done EITHER via Left (+1 + 2 = +3) OR via Right (-2 + -2 = -4 == +3 mod 7)! Neither uses R1 (-1)!
- **Method 1 (First-Principles Derivation)**: All rounds except Rounds 4 and 5 have fixed pass types: R1=L1, R2=R2, R3=R1, R6=L2, R7=L1, R8=L1, R9=R2, R10=R1. In Rounds 4 and 5, moving from seat 5 to seat 1 requires a 2-step displacement of +3 == -4 (mod 7), which can be (+1, +2), (+2, +1), or (-2, -2). Across all three valid paths, the pass type -1 ('Immediately to the right') occurs 0 times in Rounds 4-5, so its total count is uniquely 2.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Spot that (+1) + (+2) creates an order ambiguity in Round 4 vs Round 5, AND (-2) + (-2) = -4 == +3 (mod 7) trades L1+L2 for R2+R2, leaving only R1 (-1) invariant!
- **Boundary Conditions & Trap Alert**: Students who forget modular wrap-around (-4 == +3 mod 7) think only the order of L1 and L2 is ambiguous and miss why L1, L2, and R2 counts all change!
- **Verification Audit**: Between Round 3 (Diya at seat 5) and Round 5 (Aarav at seat 1), the net shift over Rounds 4 and 5 is 1 - 5 = -4 == +3 (mod 7). In two steps from {+1, +2, -1, -2}, this shift can be achieved EITHER as (+1) + (+2) (one L1 and one L2) OR as (-2) + (-2) = -4 == +3 (mod 7) (two R2s)! Thus L1, L2, and R2 counts vary between the two cases, whereas R1 (-1, 'Immediately to the right') is NEVER used in Rounds 4-5 and is uniquely fixed at 2 occurrences (Round 3 and Round 10)!

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q16</summary>

- **Trigger**: On a 7-circle, moving +3 (from 5 to 1) in 2 steps can be done EITHER via Left (+1 + 2 = +3) OR via Right (-2 + -2 = -4 == +3 mod 7)! Neither uses R1 (-1)!
- **Answer**: **(D) Immediately to the right**
- **Trap to Avoid**: Students who forget modular wrap-around (-4 == +3 mod 7) think only the order of L1 and L2 is ambiguous and miss why L1, L2, and R2 counts all change!
</details>

### Q17 (`CAT2025_S3_DILR_Q17`) — [MCQ | Hard | `Round_2_Doable`]
- **Canonical Taxonomy**: Linear, Circular & 2D Matrix Arrangements $\rightarrow$ *Circular seating with modular step transitions*
- **Core Concept Tested**: Intermediate state reachability in 2-step modular paths
- **Verified Answer**: **(B) Gaurav** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: From Diya (5) to Aarav (1) in 2 steps, the Round-4 intermediate holder can be 5+1=6 (Eshan), 5+2=0 (Bina), or 5-2=3 (Farhan) — eliminating (A), (C), and (D) and leaving (B) Gaurav!
- **Method 1 (First-Principles Derivation)**: Receivers in Rounds 1, 2, 3, 5, 6, 7, 8, 9, 10 are uniquely fixed as: 1:Aarav, 2:Eshan(6), 3:Diya(5), 5:Aarav(1), 6:Farhan(3), 7:Gaurav(4), 8:Diya(5), 9:Farhan(3), 10:Chirag(2). In Round 4, the receiver can be Eshan (if R4=+1, R5=+2), Bina (if R4=+2, R5=+1), or Farhan (if R4=-2, R5=-2). Only Gaurav's count (1 time, in Round 7) is invariant.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: The 3 paths in Round 4 visit seats 6 (Eshan), 0 (Bina), and 3 (Farhan) — which are literally the 3 distractors (A), (C), (D)! Only Gaurav (seat 4, Option B) is untouched!
- **Boundary Conditions & Trap Alert**: Notice how the 3 distractors in Q17 (Bina, Farhan, Eshan) are the exact 3 intermediate vertices of the 3 paths in Q16!
- **Verification Audit**: Every round's receiver is fixed EXCEPT Round 4 (which starts at Diya = 5 and ends at Aarav = 1 in Round 5). The three possible intermediate receivers in Round 4 are seat 6 (Eshan, via +1), seat 0 (Bina, via +2), or seat 3 (Farhan, via -2). Thus Eshan, Bina, and Farhan each have an uncertain count depending on Round 4, whereas Gaurav (seat 4) is never visited in Round 4 and received the Buck uniquely 1 time (in Round 7).

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q17</summary>

- **Trigger**: From Diya (5) to Aarav (1) in 2 steps, the Round-4 intermediate holder can be 5+1=6 (Eshan), 5+2=0 (Bina), or 5-2=3 (Farhan) — eliminating (A), (C), and (D) and leaving (B) Gaurav!
- **Answer**: **(B) Gaurav**
- **Trap to Avoid**: Notice how the 3 distractors in Q17 (Bina, Farhan, Eshan) are the exact 3 intermediate vertices of the 3 paths in Q16!
</details>

### Q18 (`CAT2025_S3_DILR_Q18`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Bilateral trade matrices & normalized trade balance*
- **Core Concept Tested**: Normalized Trade Balance conversion (NTB = k => E/I = (1+k)/(1-k))
- **Verified Answer**: **48** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: For Normalized Trade Balance = k, the Export-to-Import ratio is ALWAYS E / I = (1 + k) / (1 - k)! For C (k = -0.2), E_C / I_C = 0.8 / 1.2 = 2/3!
- **Method 1 (First-Principles Derivation)**: Since only P exports to C and P->C = 1200, I_C = 1200. From (E_C - I_C)/(E_C + I_C) = -0.20, we get E_C = (0.8/1.2)*1200 = 800. Since 90% of E_C goes to P and 4% goes to ROW (and C cannot export to C), the remaining 6% goes to X: 0.06 * 800 = 48.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: I_C = 1200 => E_C = 800 => C->X = 6% of 800 = 48 in 20 seconds!
- **Boundary Conditions & Trap Alert**: Memorize E/I = (1 + NTB)/(1 - NTB): for NTB = 0%, E/I = 1; for NTB = +10%, E/I = 11/9; for NTB = -20%, E/I = 2/3.
- **Verification Audit**: Clue 5 states P->C = 1200 and P is the ONLY country that exports to C, so C's total imports I_C = 1200. Clue 1 states C's normalized trade balance (E_C - I_C)/(E_C + I_C) = -20% = -1/5 => E_C / I_C = 2/3 => E_C = 800. Clue 3 states 90% of C's exports are to P and 4% are to ROW, leaving 100% - 94% = 6% to X. Thus C->X = 6% of 800 = 48.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q18</summary>

- **Trigger**: For Normalized Trade Balance = k, the Export-to-Import ratio is ALWAYS E / I = (1 + k) / (1 - k)! For C (k = -0.2), E_C / I_C = 0.8 / 1.2 = 2/3!
- **Answer**: **48**
- **Trap to Avoid**: Memorize E/I = (1 + NTB)/(1 - NTB): for NTB = 0%, E/I = 1; for NTB = +10%, E/I = 11/9; for NTB = -20%, E/I = 2/3.
</details>

### Q19 (`CAT2025_S3_DILR_Q19`) — [TITA | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Bilateral trade matrices & normalized trade balance*
- **Core Concept Tested**: 2x2 linear flow system for total imports/exports
- **Verified Answer**: **200** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Express both E_X = 0.55 I_P and I_X = 0.45 I_P in terms of I_P, then eliminate E_ROW between the import equations of P (0.40 E_ROW) and X (0.12 E_ROW)!
- **Method 1 (First-Principles Derivation)**: From 0.40 E_X = 0.22 I_P, E_X = 0.55 I_P and I_X = (9/11)E_X = 0.45 I_P. P's imports: 0.78 I_P = 720 + 0.40 E_ROW. X's imports: 0.45 I_P = 648 + 0.12 E_ROW. Multiply the second by 10/3: 1.50 I_P = 2160 + 0.40 E_ROW. Subtract the first: 0.72 I_P = 1440 => I_P = 2000 = E_P. Finally, P->ROW = 2000 - 600 - 1200 = 200.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Since E_X = (11/20)I_P and I_X = (9/20)I_P, I_P must be a clean multiple of 200 (and >= 1800 since E_P = I_P >= 600 + 1200 = 1800) -> test I_P = 2000 first: P->ROW = 2000 - 1800 = 200!
- **Boundary Conditions & Trap Alert**: Testing I_P = 2000 (the first round multiple of 1000 above 1800) immediately satisfies both equations!
- **Verification Audit**: X->P = 0.40 E_X = 0.22 I_P => E_X = 0.55 I_P, and since NTB(X) = +10% (E_X/I_X = 11/9), I_X = 0.45 I_P. Also I_P = (X->P) + (C->P) + (ROW->P) = 0.22 I_P + 720 + 0.40 E_ROW => 0.78 I_P - 0.40 E_ROW = 720. And I_X = (P->X) + (C->X) + (ROW->X) = 600 + 48 + 0.12 E_ROW = 0.45 I_P. Eliminating E_ROW gives I_P = 2000 = E_P. Then P->ROW = E_P - (P->X + P->C) = 2000 - (600 + 1200) = 200.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q19</summary>

- **Trigger**: Express both E_X = 0.55 I_P and I_X = 0.45 I_P in terms of I_P, then eliminate E_ROW between the import equations of P (0.40 E_ROW) and X (0.12 E_ROW)!
- **Answer**: **200**
- **Trap to Avoid**: Testing I_P = 2000 (the first round multiple of 1000 above 1800) immediately satisfies both equations!
</details>

### Q20 (`CAT2025_S3_DILR_Q20`) — [TITA | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Bilateral trade matrices & normalized trade balance*
- **Core Concept Tested**: Composite region internal trade (ROW -> ROW)
- **Verified Answer**: **1008** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Unlike a single country, 'Rest of World (ROW)' is a group of countries that trade among themselves: ROW->ROW = (100% - 40% - 12% - 0%) = 48% of E_ROW = 0.48 * 2100 = 1008!
- **Method 1 (First-Principles Derivation)**: With I_P = 2000, ROW->P = 2000 - 440 - 720 = 840 = 40% of E_ROW => E_ROW = 2100. Since ROW->C = 0 (Clue 5), ROW->ROW accounts for 100% - 40% - 12% = 48% of E_ROW = 0.48 * 2100 = 1008.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: ROW->P is 40% of E_ROW = 840 => 1% of E_ROW = 21 => 48% of E_ROW = 48 * 21 = 1008!
- **Boundary Conditions & Trap Alert**: Since ROW->P (40%) = 840, simply multiply 840 by (48/40) = 1.2 -> 840 * 1.2 = 1008!
- **Verification Audit**: From Q19, 0.40 E_ROW = 0.78(2000) - 720 = 1560 - 720 = 840 => E_ROW = 2100. Since ROW exports 12% to X, 40% to P, and 0% to C (only P exports to C), the remaining 100% - 52% = 48% of ROW's exports are from ROW to ROW (trade among countries inside ROW): 0.48 * 2100 = 1008.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q20</summary>

- **Trigger**: Unlike a single country, 'Rest of World (ROW)' is a group of countries that trade among themselves: ROW->ROW = (100% - 40% - 12% - 0%) = 48% of E_ROW = 0.48 * 2100 = 1008!
- **Answer**: **1008**
- **Trap to Avoid**: Since ROW->P (40%) = 840, simply multiply 840 by (48/40) = 1.2 -> 840 * 1.2 = 1008!
</details>

### Q21 (`CAT2025_S3_DILR_Q21`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Bilateral trade matrices & normalized trade balance*
- **Core Concept Tested**: Zero-sum global conservation of trade balances (Sum(TB) = 0)
- **Verified Answer**: **(A) 200** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Every export is someone's import, so TB(P) + TB(X) + TB(C) + TB(ROW) = 0! Never compute I_ROW the long way!
- **Method 1 (First-Principles Derivation)**: Method 1 (Conservation): TB(ROW) = -(TB(P) + TB(X) + TB(C)) = -(0 + 200 - 400) = +200. Method 2 (Direct): E_ROW = 2100, and I_ROW = (P->ROW = 200) + (X->ROW = 1100 - 440 = 660) + (C->ROW = 32) + (ROW->ROW = 1008) = 1900 => TB(ROW) = 2100 - 1900 = 200.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Zero-sum trade balance identity: TB(ROW) = 400 - 200 = 200 (Option A) in 5 seconds!
- **Boundary Conditions & Trap Alert**: Notice that ROW->ROW (1008) cancels out in E_ROW - I_ROW because it is both an export of ROW and an import of ROW!
- **Verification Audit**: By global conservation of trade, the sum of Trade Balances (Exports - Imports) across all 4 regions (P, X, C, ROW) is identically 0! Since TB(P) = 0, TB(X) = 1100 - 900 = +200, and TB(C) = 800 - 1200 = -400, we have TB(ROW) = -(0 + 200 - 400) = +200.

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q21</summary>

- **Trigger**: Every export is someone's import, so TB(P) + TB(X) + TB(C) + TB(ROW) = 0! Never compute I_ROW the long way!
- **Answer**: **(A) 200**
- **Trap to Avoid**: Notice that ROW->ROW (1008) cancels out in E_ROW - I_ROW because it is both an export of ROW and an import of ROW!
</details>

### Q22 (`CAT2025_S3_DILR_Q22`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Bilateral trade matrices & normalized trade balance*
- **Core Concept Tested**: Total trade (E + I) comparison
- **Verified Answer**: **(A) Both X and C** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Total trade(X) = 1100 + 900 = 2000 and Total trade(C) = 800 + 1200 = 2000 (tied for least!).
- **Method 1 (First-Principles Derivation)**: Compute E + I for each country: Total(P) = 4000, Total(X) = 1100 + 900 = 2000, Total(C) = 800 + 1200 = 2000. Both X and C tie for the minimum of 2000.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 1100 + 900 = 800 + 1200 = 2000 < 4000 -> (A) Both X and C.
- **Boundary Conditions & Trap Alert**: Do not confuse Exports (where C = 800 < X = 1100) with Total Trade = Exports + Imports (where X and C both equal 2000)!
- **Verification Audit**: Total trade (Exports + Imports): P = 2000 + 2000 = 4000; X = 1100 + 900 = 2000; C = 800 + 1200 = 2000. Thus Both X and C have the least total trade (2000 each).

<details><summary>Active-Recall Self-Test: CAT2025_S3_DILR_Q22</summary>

- **Trigger**: Total trade(X) = 1100 + 900 = 2000 and Total trade(C) = 800 + 1200 = 2000 (tied for least!).
- **Answer**: **(A) Both X and C**
- **Trap to Avoid**: Do not confuse Exports (where C = 800 < X = 1100) with Total Trade = Exports + Imports (where X and C both equal 2000)!
</details>
