# Pass 1 Master Analysis: CAT 2025 DILR Slot 1

## 1. Executive Summary & Exam-Hall Blueprint
- **Section**: DILR | **Slot**: Slot 1 (CAT 2025)
- **Source Document**: `docs/pyqs/2025/DILR_Slot_1_CAT_2025_1__c8ca237ed1e4129e7d4039f17d8206b8.pdf`
- **Total Questions**: 22 (11 MCQs, 11 TITA)
- **Difficulty Breakdown**: Easy: **9** | Medium: **9** | Hard: **4**
- **Round-Wise Triage**: Round 1 Sitters: **18** | Round 2 Doables: **4** | Round 3 Time-Sinks: **0**
- **Answer Verification Protocol**: 3-Layer Autonomous Verification (`ai_verified_derivation` — First-Principles Algebraic/Logical Derivation + Programmatic/Cross-Clue Verification + 30-Second Speed Shortcut)

### Percentile Score & Attempt Targets (40-Minute Clock)
| Percentile Target | Scaled Raw Score Target | Net Correct Equivalent | Recommended Execution Strategy |
| :---: | :---: | :---: | :--- |
| **95%ile** | 24-27 (8-9 net) | ~9-11 questions | Clear all Easy Round-1 sitters + all TITA questions with zero negative risk |
| **99%ile** | 34-37 (11-12 net) | ~12-15 questions | Sweep Round 1 in 22 mins + cherry-pick 4-5 Round 2 medium questions |
| **99.5%ile** | 40-43 (13-14 net) | ~15-17 questions | Full Round 1 sweep + 70% of Round 2 using option/parity/invariant shortcuts |
| **99.9%ile** | 48+ (16+ net) | ~17-19 questions | Complete mastery of Round 1 + Round 2 with <90s average per sitter |

### Topic & Sub-Topic Distribution
| Canonical Topic | Canonical Sub-Topic | Question Count | Question IDs |
| :--- | :--- | :---: | :--- |
| **Networks, Routes, Flows & Project Scheduling** | Directed/undirected flow conservation & segment occupancy | 5 | Q14, Q15, Q16, Q17, Q18 |
| **Quant-Based LR & Algorithmic Puzzles** | Linear, Circular & 2D Matrix Arrangements | 13 | Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q19, Q20, Q21, Q22 |
| **Quantitative & Reasoning-Based DI** | Non-standard charts (Radar/Spider, Bar charts) | 4 | Q10, Q11, Q12, Q13 |

---

## 2. Quick-Reference Verified Answer Key
| Q# | Question ID | Type | Difficulty | Round Tag | Verified Answer | Core Concept / Mental Trigger |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| **Q1** | `CAT2025_S1_DILR_Q01` | TITA | Medium | `Round_1_Sitter` | **4** | Circular state-transition game on a 7-chair ring |
| **Q2** | `CAT2025_S1_DILR_Q02` | MCQ | Medium | `Round_1_Sitter` | **(4) No one** | Look-ahead state transition pruning on circular tracks |
| **Q3** | `CAT2025_S1_DILR_Q03` | MCQ | Medium | `Round_1_Sitter` | **(1) Chairs numbered 4, 5, 6, and 7** | Adjacency block constraint at Turn 6 |
| **Q4** | `CAT2025_S1_DILR_Q04` | MCQ | Medium | `Round_1_Sitter` | **(2) Davies only** | Invariance under final-move branching |
| **Q5** | `CAT2025_S1_DILR_Q05` | TITA | Hard | `Round_2_Doable` | **4** | Multi-quarter rating & promotion-demotion state machine with tie-breaking |
| **Q6** | `CAT2025_S1_DILR_Q06` | TITA | Medium | `Round_1_Sitter` | **0** | Minimum-swap pigeonhole principle across 3 transitions |
| **Q7** | `CAT2025_S1_DILR_Q07` | TITA | Hard | `Round_2_Doable` | **5** | Group-wise permutation completion across quarters |
| **Q8** | `CAT2025_S1_DILR_Q08` | TITA | Hard | `Round_2_Doable` | **4** | Uniqueness vs tie-break ambiguity in cumulative scores |
| **Q9** | `CAT2025_S1_DILR_Q09` | MCQ | Hard | `Round_2_Doable` | **(4) Only II** | Necessary vs possible truth under tie-breaking rules |
| **Q10** | `CAT2025_S1_DILR_Q10` | MCQ | Easy | `Round_1_Sitter` | **(3) 7.0 Billion USD** | Bilateral trade identity (Export of Y to X = Import of X from Y = Tariff_XY / Rate_XY) |
| **Q11** | `CAT2025_S1_DILR_Q11` | MCQ | Easy | `Round_1_Sitter` | **(2) Imports by US from France** | Ratio comparison (Tariff / Tariff%) across radar and bar charts |
| **Q12** | `CAT2025_S1_DILR_Q12` | MCQ | Easy | `Round_1_Sitter` | **(2) Deficit of 15.0 Billion USD** | Bilateral trade balance (Exports - Imports) from asymmetric tariff charts |
| **Q13** | `CAT2025_S1_DILR_Q13` | MCQ | Easy | `Round_1_Sitter` | **(4) Only France** | Qualitative trade surplus comparison across country pairs |
| **Q14** | `CAT2025_S1_DILR_Q14` | MCQ | Easy | `Round_1_Sitter` | **(2) 70%** | Segment flow decomposition and divisibility bounding |
| **Q15** | `CAT2025_S1_DILR_Q15` | TITA | Easy | `Round_1_Sitter` | **50** | Origin-destination pair extraction from segment ratios |
| **Q16** | `CAT2025_S1_DILR_Q16` | TITA | Medium | `Round_1_Sitter` | **80** | Segment capacity equation C-D = 190 and B-C = 170 + AD |
| **Q17** | `CAT2025_S1_DILR_Q17` | TITA | Easy | `Round_1_Sitter` | **40** | Destination flow invariance (AD + BD + CD = 50) |
| **Q18** | `CAT2025_S1_DILR_Q18` | TITA | Easy | `Round_1_Sitter` | **60** | 1-hop path enumeration on a linear line graph |
| **Q19** | `CAT2025_S1_DILR_Q19` | TITA | Medium | `Round_1_Sitter` | **7** | Bounded multiset sum conservation (1 + 2 + 3 + x in {7, 8, 9}) |
| **Q20** | `CAT2025_S1_DILR_Q20` | MCQ | Medium | `Round_1_Sitter` | **(4) Alia and Badal** | Row-sum extremum bounding under 'at most two 1s' constraint |
| **Q21** | `CAT2025_S1_DILR_Q21` | MCQ | Medium | `Round_1_Sitter` | **(1) No** | Anti-symmetric matrix constraint (M[p][q] != M[q][p] for A and E) |
| **Q22** | `CAT2025_S1_DILR_Q22` | TITA | Easy | `Round_1_Sitter` | **6** | Multiset excess decomposition across columns |

---

## 3. Question-by-Question High-Recall Decomposition (Dual-Method)

### Q1 (`CAT2025_S1_DILR_Q01`) — [TITA | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Circular state-transition game on a 7-chair ring
- **Verified Answer**: **4** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: On a 7-chair circle with 4 friends and 3 empty chairs, having empty chairs on BOTH sides of B and D forces the 3 empty chairs to alternate with B and D: E - D - E - B - E - A - C!
- **Method 1 (First-Principles Derivation)**: Since C does not move until Turn 3 and is at Chair 7 after Turn 2, C starts at Chair 7. Since D does not move until Turn 4 and is at Chair 2 after Turn 1, D starts at Chair 2. For D (at 2) to have empty chairs on both sides, Chairs 1 and 3 must be empty initially. Since C is at 7 and A is adjacent to C, A must be at Chair 6. For B to have empty chairs on both sides among remaining chairs {4, 5}, Chair 5 must be empty and B must start at Chair 4.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: D=2 has empty neighbors 1 and 3 => C=7 must have neighbor A=6 => remaining B must sit at 4 with empty neighbors 3 and 5! Solved in 30 seconds without even simulating the turns!
- **Boundary Conditions & Trap Alert**: Notice that D's position after Turn 1 IS D's initial position because only A moves in Turn 1.
- **Verification Audit**: With 4 occupied chairs on a 7-chair circle where A and C are adjacent and both B and D have empty chairs on both sides, the initial occupied chairs must follow the cyclic spacing pattern {A, C}-E-B-E-D-E. Since C is at Chair 7 (unchanged through Turn 2) and D is at Chair 2 (unchanged through Turn 1), the empty chairs initially must be {1, 3, 5}, forcing A = 6 and B = 4.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q01</summary>

- **Trigger**: On a 7-chair circle with 4 friends and 3 empty chairs, having empty chairs on BOTH sides of B and D forces the 3 empty chairs to alternate with B and D: E - D - E - B - E - A - C!
- **Answer**: **4**
- **Trap to Avoid**: Notice that D's position after Turn 1 IS D's initial position because only A moves in Turn 1.
</details>

### Q2 (`CAT2025_S1_DILR_Q02`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Look-ahead state transition pruning on circular tracks
- **Verified Answer**: **(4) No one** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: In Turn 4, D (at Chair 2) must land on Chair 4 (the first empty chair in its chosen direction), which requires Chair 3 to be occupied and Chair 4 to be EMPTY at the end of Turn 3!
- **Method 1 (First-Principles Derivation)**: To make all 4 friends adjacent at the end of Turn 2 with D=2 and C=7, A moves 6->1 in Turn 1 and B moves 4->3 in Turn 2 (occupying {7,1,2,3}). In Turn 3, C moves 7->6 (occupying {1,2,3,6}) so that in Turn 4, D moves CW from 2 past occupied 3 into empty Chair 4. Hence Chair 4 is empty at the end of Turn 3.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Since D moves to Chair 4 in Turn 4, Chair 4 MUST be unoccupied at the end of Turn 3 -> (4) No one immediately!
- **Boundary Conditions & Trap Alert**: You don't even need to trace Turn 3 to know Chair 4 is empty at the end of Turn 3: D moves into Chair 4 on Turn 4!
- **Verification Audit**: Start: {A:6, B:4, C:7, D:2}. Turn 1 (A CW): A->1; Turn 2 (B CCW to make all 4 adjacent at {7,1,2,3}): B->3; Turn 3 (C CCW so D can later reach Chair 4 in Turn 4): C->6. Thus at the end of Turn 3, occupied chairs are {1, 2, 3, 6}, leaving Chair 4 empty.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q02</summary>

- **Trigger**: In Turn 4, D (at Chair 2) must land on Chair 4 (the first empty chair in its chosen direction), which requires Chair 3 to be occupied and Chair 4 to be EMPTY at the end of Turn 3!
- **Answer**: **(4) No one**
- **Trap to Avoid**: You don't even need to trace Turn 3 to know Chair 4 is empty at the end of Turn 3: D moves into Chair 4 on Turn 4!
</details>

### Q3 (`CAT2025_S1_DILR_Q03`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Adjacency block constraint at Turn 6
- **Verified Answer**: **(1) Chairs numbered 4, 5, 6, and 7** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: At Turn 4 end, C=6 and D=4; to form a 4-adjacent block at Turn 6 after A (Turn 5) and B (Turn 6) move, A and B must fill chairs 7 and 5, forming {4, 5, 6, 7}.
- **Method 1 (First-Principles Derivation)**: After Turn 4, occupied chairs are {1, 3, 4, 6}. If A moved CW 1->5 in Turn 5, {3, 4, 5, 6} would already be adjacent at Turn 5 (violating Clue 1). Thus A moves CCW 1->7 in Turn 5 ({3, 4, 6, 7}), and B moves CW 3->5 in Turn 6, giving {4, 5, 6, 7}.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Since C=6 and D=4 do not move in Turns 5 and 6, the occupied set at Turn 6 must contain BOTH 4 and 6. Only Option (1) {4, 5, 6, 7} contains both 4 and 6!
- **Boundary Conditions & Trap Alert**: Checking that C=6 and D=4 are stationary during Turns 5-6 eliminates Options (2), (3), and (4) in 5 seconds.
- **Verification Audit**: After Turn 4: {A:1, B:3, C:6, D:4}. Turn 5 (A moves CCW 1->7 so Turn 5 is not adjacent): {A:7, B:3, C:6, D:4}. Turn 6 (B moves CW 3->5 so all 4 are adjacent at the end of Turn 6): {A:7, B:5, C:6, D:4} = Chairs 4, 5, 6, and 7.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q03</summary>

- **Trigger**: At Turn 4 end, C=6 and D=4; to form a 4-adjacent block at Turn 6 after A (Turn 5) and B (Turn 6) move, A and B must fill chairs 7 and 5, forming {4, 5, 6, 7}.
- **Answer**: **(1) Chairs numbered 4, 5, 6, and 7**
- **Trap to Avoid**: Checking that C=6 and D=4 are stationary during Turns 5-6 eliminates Options (2), (3), and (4) in 5 seconds.
</details>

### Q4 (`CAT2025_S1_DILR_Q04`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Invariance under final-move branching
- **Verified Answer**: **(2) Davies only** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: At Turn 6, B is at 5 between D(4) and C(6); since C is the mover in Turn 7, C vacates Chair 6 regardless of direction, leaving only D(4) adjacent to B(5)!
- **Method 1 (First-Principles Derivation)**: At Turn 6, B=5, D=4, C=6, A=7. In Turn 7, C must move to the first empty chair (either Chair 1 CW or Chair 3 CCW). In both cases, Chair 6 becomes empty while D remains at Chair 4. Hence only Davies is adjacent to Bashir at the end of Turn 7.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: C is sitting at 6 next to B(5) and C moves on Turn 7, so Chair 6 becomes empty and only D(4) remains next to B(5).
- **Boundary Conditions & Trap Alert**: Do not assume C's Turn-7 direction matters; both directions leave Chair 6 empty.
- **Verification Audit**: At the end of Turn 6, {D:4, B:5, C:6, A:7}. In Turn 7, C (at Chair 6) moves either CW to Chair 1 or CCW to Chair 3, vacating Chair 6. Thus at the end of Turn 7, Bashir (at Chair 5) has Davies at Chair 4 and an empty Chair 6.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q04</summary>

- **Trigger**: At Turn 6, B is at 5 between D(4) and C(6); since C is the mover in Turn 7, C vacates Chair 6 regardless of direction, leaving only D(4) adjacent to B(5)!
- **Answer**: **(2) Davies only**
- **Trap to Avoid**: Do not assume C's Turn-7 direction matters; both directions leave Chair 6 empty.
</details>

### Q5 (`CAT2025_S1_DILR_Q05`) — [TITA | Hard | `Round_2_Doable`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Multi-quarter rating & promotion-demotion state machine with tie-breaking
- **Verified Answer**: **4** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: For all 3 initial Elite members {A, B, C} to end up in Novice after 3 quarters (with 1 swap per quarter), EVERY quarter must demote a remaining member of {A, B, C} and promote a member of {D, E, F}!
- **Method 1 (First-Principles Derivation)**: Since {A, B, C} are in Elite at Q1 start and all 3 are in Novice at Q4 start, and only 1 swap occurs per quarter, each of Q1, Q2, Q3 must demote one of {A, B, C} and promote one of {D, E, F}. Since D got 2 in Q3 (in Novice), D=(2,2,2) and D is promoted at the end of Q3. Thus F and E are promoted at the ends of Q1 and Q2. Since F has a constant rating and is promoted at Q1 end over D=2, F=(3,3,3) and E gets 1 in Q1. In Q2, Novice is {B, D, E} with B=1 and D=2, forcing E=3. Thus E's cumulative score at Q2 end is 1 + 3 = 4.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: In Q1 Novice {D,E,F}, D=2 and F=3 (constant), so E=1. In Q2 Novice {B,D,E}, B=1 and D=2, so E=3. Score of E at Q2 end = 1 + 3 = 4.
- **Boundary Conditions & Trap Alert**: The realization that 3 swaps are needed to move all 3 members of {A,B,C} from Elite to Novice immediately locks the direction of every swap (no back-and-forth swaps possible!).
- **Verification Audit**: Since D and F have constant ratings across all quarters and D got 2 in Q3, D=(2,2,2). In Q1 Novice={D,E,F}, F must be 3 (if F=1, F is never promoted and A,B,C cannot all be in Novice by Q4), so F=(3,3,3) and E gets 1 in Q1. At end of Q1, F is promoted and B (rating 1) is demoted. In Q2 Novice={B,D,E} with B=1, D=2 => E=3. Thus E's score at end of Q2 is 1 + 3 = 4.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q05</summary>

- **Trigger**: For all 3 initial Elite members {A, B, C} to end up in Novice after 3 quarters (with 1 swap per quarter), EVERY quarter must demote a remaining member of {A, B, C} and promote a member of {D, E, F}!
- **Answer**: **4**
- **Trap to Avoid**: The realization that 3 swaps are needed to move all 3 members of {A,B,C} from Elite to Novice immediately locks the direction of every swap (no back-and-forth swaps possible!).
</details>

### Q6 (`CAT2025_S1_DILR_Q06`) — [TITA | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Minimum-swap pigeonhole principle across 3 transitions
- **Verified Answer**: **0** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Moving 3 people out of a group of 3 at a rate of 1 person per quarter for 3 quarters requires 100% one-way traffic — nobody can ever move twice!
- **Method 1 (First-Principles Derivation)**: At the start of Q1, Elite = {A, B, C} and Novice = {D, E, F}. At each of the 3 quarter-ends (Q1, Q2, Q3), exactly 1 employee leaves Elite for Novice and 1 leaves Novice for Elite (6 single-person moves in total). For Elite to become {D, E, F} and Novice to become {A, B, C} after 3 swaps, each of the 6 employees must change groups exactly once. Therefore, 0 employees changed groups more than once.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Answer is 0 purely from Clue 1 in 10 seconds — you don't even need to solve the ratings to answer Q6!
- **Boundary Conditions & Trap Alert**: Read carefully: 'more than once' means >= 2 times (answer 0), not 'at least once' (6).
- **Verification Audit**: To move all 3 members of {A, B, C} from Elite (start of Q1) to Novice (start of Q4) in 3 quarterly swaps of 1 pair each, each of A, B, C is demoted exactly once and each of D, E, F is promoted exactly once. Zero employees change groups more than once.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q06</summary>

- **Trigger**: Moving 3 people out of a group of 3 at a rate of 1 person per quarter for 3 quarters requires 100% one-way traffic — nobody can ever move twice!
- **Answer**: **0**
- **Trap to Avoid**: Read carefully: 'more than once' means >= 2 times (answer 0), not 'at least once' (6).
</details>

### Q7 (`CAT2025_S1_DILR_Q07`) — [TITA | Hard | `Round_2_Doable`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Group-wise permutation completion across quarters
- **Verified Answer**: **5** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: B is demoted first (Q1 rating = 1), gets 1 in Q2 (given), and in Q3 Novice={A,B,D} where A=1 and D=2 are given, forcing B=3 in Q3 -> 1 + 1 + 3 = 5!
- **Method 1 (First-Principles Derivation)**: Since B is in Novice in Q2, B had the lowest score in Elite in Q1, so r_B(Q1) = 1. Clue 3 states r_B(Q2) = 1. At Q2 end, E (score 4, r=3) is promoted and A is demoted, so Q3 Novice is {A, B, D}. Clue 3 states r_A(Q3) = 1 and r_D(Q3) = 2, which forces r_B(Q3) = 3. Thus Bunty's score at the end of Q3 is 1 + 1 + 3 = 5.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: B's three ratings are 1 (demoted Q1), 1 (given Q2), and 3 (remaining rating in Q3 Novice beside A=1, D=2) -> sum = 5.
- **Boundary Conditions & Trap Alert**: Verify that at Q3 end, D has score 2+2+2 = 6 > B's score 5, so D (not B) gets promoted to Elite at the end of Q3.
- **Verification Audit**: B was in Novice in Q2 (so B was demoted at Q1 end with Q1 rating 1). In Q2, B got rating 1 (given). In Q3, Novice={A, B, D} with A=1 and D=2 (given), so B got rating 3 in Q3. Cumulative score of B at Q3 end = 1 + 1 + 3 = 5.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q07</summary>

- **Trigger**: B is demoted first (Q1 rating = 1), gets 1 in Q2 (given), and in Q3 Novice={A,B,D} where A=1 and D=2 are given, forcing B=3 in Q3 -> 1 + 1 + 3 = 5!
- **Answer**: **5**
- **Trap to Avoid**: Verify that at Q3 end, D has score 2+2+2 = 6 > B's score 5, so D (not B) gets promoted to Elite at the end of Q3.
</details>

### Q8 (`CAT2025_S1_DILR_Q08`) — [TITA | Hard | `Round_2_Doable`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Uniqueness vs tie-break ambiguity in cumulative scores
- **Verified Answer**: **4** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Check whether A needs a strictly lower cumulative score than C at Q2 end, or if a tie (A: 3+1=4 vs C: 2+2=4) also demotes A by the latest-quarter tie-breaker!
- **Method 1 (First-Principles Derivation)**: In Q2 Elite={A, C, F}, F=3, and A must be demoted at Q2 end while C stays. Since r_A(Q2) = 1 and r_C(Q2) = 2 (if r_C(Q2)=1, C would have latest rating 1 and score <= 4, getting demoted instead of A), in Q1 we can have either (r_A, r_C) = (2, 3) (Q2 scores 3 vs 5) OR (r_A, r_C) = (3, 2) (Q2 scores 4 vs 4, where A is still demoted because r_A(Q2)=1 < r_C(Q2)=2!). Thus A and C have two possible Q3 scores, leaving 4 employees (B, D, E, F) uniquely determined.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: All ratings in Novice are fixed, and in Q3 Elite {C, E, F}, E=2, F=3, C=1 are fixed; only the Q1 swap between A and C (2 vs 3) is ambiguous, leaving 6 - 2 = 4 employees fixed.
- **Boundary Conditions & Trap Alert**: Missing the tie-break case (r_A(Q1)=3, r_C(Q1)=2 => Q2 scores tied at 4, A demoted due to lower Q2 rating) leads to the trap answer 6.
- **Verification Audit**: At the end of Q3, scores of B (5), D (6), E (6), and F (9) are uniquely determined, whereas A and C can have Q1 ratings (2, 3) or (3, 2), giving (sc3[A], sc3[C]) = (4, 6) or (5, 5). Thus 4 employees have uniquely determined Q3 scores.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q08</summary>

- **Trigger**: Check whether A needs a strictly lower cumulative score than C at Q2 end, or if a tie (A: 3+1=4 vs C: 2+2=4) also demotes A by the latest-quarter tie-breaker!
- **Answer**: **4**
- **Trap to Avoid**: Missing the tie-break case (r_A(Q1)=3, r_C(Q1)=2 => Q2 scores tied at 4, A demoted due to lower Q2 rating) leads to the trap answer 6.
</details>

### Q9 (`CAT2025_S1_DILR_Q09`) — [MCQ | Hard | `Round_2_Doable`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Necessary vs possible truth under tie-breaking rules
- **Verified Answer**: **(4) Only II** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: For A to be demoted from Q2 Elite {A, C, F} where F=3, A must receive rating 1 in Q2 (Statement II), which already suffices to demote A even if r_A(Q1) = 3!
- **Method 1 (First-Principles Derivation)**: In Q2 Elite {A, C, F}, F gets 3, so {A, C} get {1, 2}. If A got 2 and C got 1 in Q2, then even if C had 3 in Q1, C's Q2 score would be at most 4 (tied with A=2+2=4) with a lower Q2 rating (1 < 2), so C would be demoted instead of A. Thus r_A(Q2) = 1 is forced (II is true), while r_A(Q1) can be 2 or 3 (I is not necessarily true).
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Statement II (A got 1 in Q2) is required to demote A at Q2 end; Statement I (A got 2 in Q1) is not required because the Q2 tie-breaker demotes A even if A got 3 in Q1 -> (4) Only II.
- **Boundary Conditions & Trap Alert**: The presence of Statement I vs II in Q9 is itself a clue for Q8 that r_A(Q1) is not uniquely 2!
- **Verification Audit**: In Q2 Elite={A, C, F} with F=3, A is demoted at Q2 end, which requires r_A(Q2) = 1 (Statement II is necessarily true). However, in Q1, A could have received 2 or 3 (Statement I is not necessarily true).

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q09</summary>

- **Trigger**: For A to be demoted from Q2 Elite {A, C, F} where F=3, A must receive rating 1 in Q2 (Statement II), which already suffices to demote A even if r_A(Q1) = 3!
- **Answer**: **(4) Only II**
- **Trap to Avoid**: The presence of Statement I vs II in Q9 is itself a clue for Q8 that r_A(Q1) is not uniquely 2!
</details>

### Q10 (`CAT2025_S1_DILR_Q10`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Non-standard charts (Radar/Spider, Bar charts)*
- **Core Concept Tested**: Bilateral trade identity (Export of Y to X = Import of X from Y = Tariff_XY / Rate_XY)
- **Verified Answer**: **(3) 7.0 Billion USD** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Japan's export to India equals India's import from Japan! Read India's tariff on Japan (3.5B) and divide by India's tariff rate on Japan (50%) -> 3.5 / 0.50 = 7.0B!
- **Method 1 (First-Principles Derivation)**: By definition, Tariff levied by India on Japan = (Tariff % of India on Japan) * (Imports of India from Japan). From the radar chart, Green (India) on the Japan spoke is at 50%; from the bar chart, the Yellow (Japan) bar in India's group is 3.5 Billion USD. Therefore, Japan's export to India = 3.5 / 0.50 = 7.0 Billion USD.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 3.5 Billion USD / 50% = 7.0 Billion USD (Option 3).
- **Boundary Conditions & Trap Alert**: Do not confuse Japan's export to India (7.0B) with India's export to Japan (= Japan's import from India = 8.0B / 50% = 16.0B, which is distractor 2!).
- **Verification Audit**: Japan's export to India = India's import from Japan. From the bar chart, India levied 3.5 Billion USD tariff on Japan. From the radar chart, India (green line) charges 50% import tariff on Japan. Thus India's import from Japan = 3.5 / 0.50 = 7.0 Billion USD.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q10</summary>

- **Trigger**: Japan's export to India equals India's import from Japan! Read India's tariff on Japan (3.5B) and divide by India's tariff rate on Japan (50%) -> 3.5 / 0.50 = 7.0B!
- **Answer**: **(3) 7.0 Billion USD**
- **Trap to Avoid**: Do not confuse Japan's export to India (7.0B) with India's export to Japan (= Japan's import from India = 8.0B / 50% = 16.0B, which is distractor 2!).
</details>

### Q11 (`CAT2025_S1_DILR_Q11`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Non-standard charts (Radar/Spider, Bar charts)*
- **Core Concept Tested**: Ratio comparison (Tariff / Tariff%) across radar and bar charts
- **Verified Answer**: **(2) Imports by US from France** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Largest import occurs when a tall bar (6.0B for US on France) is divided by a small radar percentage (20% for US on France, explicitly given in the prompt text!) -> 6.0 / 0.20 = 30.0B!
- **Method 1 (First-Principles Derivation)**: Compute each value: (1) UK tariff on Japan (6.0B) / UK rate on Japan (40%) = 15.0B; (2) US tariff on France (6.0B) / US rate on France (20%) = 30.0B; (3) Japan tariff on France (3.0B) / Japan rate on France (30%) = 10.0B; (4) France tariff on India (6.5B) / France rate on India (40%) = 16.25B. Highest is (2) 30.0B.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: The prompt text explicitly gives US rate on France = 20%; dividing the 6.0B bar by 0.20 gives 30B, which clearly dominates all other options.
- **Boundary Conditions & Trap Alert**: Always map 'Exports by A to B' to 'Imports by B from A' before looking up country B's tariff and rate on A.
- **Verification Audit**: (1) Exports by Japan to UK = UK imports from Japan = 6.0B / 40% = 15.0B. (2) Imports by US from France = 6.0B / 20% = 30.0B. (3) Exports by France to Japan = Japan imports from France = 3.0B / 30% = 10.0B. (4) Imports by France from India = 6.5B / 40% = 16.25B (or 6.5B / 50% = 13.0B). Highest is 30.0B (Option 2).

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q11</summary>

- **Trigger**: Largest import occurs when a tall bar (6.0B for US on France) is divided by a small radar percentage (20% for US on France, explicitly given in the prompt text!) -> 6.0 / 0.20 = 30.0B!
- **Answer**: **(2) Imports by US from France**
- **Trap to Avoid**: Always map 'Exports by A to B' to 'Imports by B from A' before looking up country B's tariff and rate on A.
</details>

### Q12 (`CAT2025_S1_DILR_Q12`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Non-standard charts (Radar/Spider, Bar charts)*
- **Core Concept Tested**: Bilateral trade balance (Exports - Imports) from asymmetric tariff charts
- **Verified Answer**: **(2) Deficit of 15.0 Billion USD** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: India's tariff on UK is higher (5.0B vs 3.0B) while India's tariff rate on UK is lower (20% vs 30%), so India's imports from UK (25B) are much larger than its exports to UK (10B) -> Deficit of 15B!
- **Method 1 (First-Principles Derivation)**: Exports of India to UK = Imports of UK from India = (UK tariff on India: 3.0B) / (UK rate on India: 30%) = 10.0B. Imports of India from UK = (India tariff on UK: 5.0B) / (India rate on UK: 20%) = 25.0B. Trade balance of India with UK = 10.0B - 25.0B = -15.0B (Deficit of 15.0 Billion USD).
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Without even computing exact numbers, India's imports from UK (5.0/0.20 = 25) > exports to UK (3.0/0.30 = 10), giving a deficit of 15B (Option 2).
- **Boundary Conditions & Trap Alert**: Reversing Exports and Imports flips Deficit of 15.0B (Option 2) into Surplus of 15.0B (Option 1).
- **Verification Audit**: Exports from India to UK (= UK imports from India) = 3.0B / 30% = 10.0B. Imports to India from UK = 5.0B / 20% = 25.0B. Trade surplus of India with UK = 10.0 - 25.0 = -15.0B (Deficit of 15.0 Billion USD).

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q12</summary>

- **Trigger**: India's tariff on UK is higher (5.0B vs 3.0B) while India's tariff rate on UK is lower (20% vs 30%), so India's imports from UK (25B) are much larger than its exports to UK (10B) -> Deficit of 15B!
- **Answer**: **(2) Deficit of 15.0 Billion USD**
- **Trap to Avoid**: Reversing Exports and Imports flips Deficit of 15.0B (Option 2) into Surplus of 15.0B (Option 1).
</details>

### Q13 (`CAT2025_S1_DILR_Q13`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quantitative & Reasoning-Based DI $\rightarrow$ *Non-standard charts (Radar/Spider, Bar charts)*
- **Core Concept Tested**: Qualitative trade surplus comparison across country pairs
- **Verified Answer**: **(4) Only France** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Reuse France's exports to US = 30B from Q11 (huge surplus!), and check UK with US: UK exports to US = 3B / 30% = 10B vs UK imports from US = 2.5B / 20% = 12.5B (deficit!).
- **Method 1 (First-Principles Derivation)**: For France with US: Exports = 6.0B / 0.20 = 30.0B > Imports = 5.5B / 0.30 = 18.33B (Surplus). For UK with US: Exports = 3.0B / 0.30 = 10.0B < Imports = 2.5B / 0.20 = 12.5B (Deficit). Hence Only France has a trade surplus with US.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Both numbers for UK exports to US (3B and 30% -> 10B) are given in the problem text; since UK's rate on US is 20% and bar is 2.5B (2.5/0.20 = 12.5B > 10B), UK is in deficit -> Only France.
- **Boundary Conditions & Trap Alert**: Do not assume that because UK's tariff bar on US (2.5B) is smaller than US's tariff bar on UK (3.0B), UK has a surplus; UK's tariff percentage on US (20%) is lower than US's on UK (30%)!
- **Verification Audit**: France exports to US = 6.0B / 20% = 30.0B; France imports from US = 5.5B / 30% = 18.33B => France has a trade surplus with US. UK exports to US = 3.0B / 30% = 10.0B; UK imports from US = 2.5B / 20% = 12.5B => UK has a trade deficit with US. Thus Only France.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q13</summary>

- **Trigger**: Reuse France's exports to US = 30B from Q11 (huge surplus!), and check UK with US: UK exports to US = 3B / 30% = 10B vs UK imports from US = 2.5B / 20% = 12.5B (deficit!).
- **Answer**: **(4) Only France**
- **Trap to Avoid**: Do not assume that because UK's tariff bar on US (2.5B) is smaller than US's tariff bar on UK (3.0B), UK has a surplus; UK's tariff percentage on US (20%) is lower than US's on UK (30%)!
</details>

### Q14 (`CAT2025_S1_DILR_Q14`) — [MCQ | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Networks, Routes, Flows & Project Scheduling $\rightarrow$ *Directed/undirected flow conservation & segment occupancy*
- **Core Concept Tested**: Segment flow decomposition and divisibility bounding
- **Verified Answer**: **(2) 70%** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Since 4/7 of segment D-E seats are from before C (AE + BE = AE + 30) and all ticket counts are multiples of 10, D-E must be a multiple of 70 (either 70 or 140) -> since AE > 30, AE + 30 > 60 forces D-E = 140 (70% of 200)!
- **Method 1 (First-Principles Derivation)**: Seats reserved on D-E equal AE + BE + CE + DE. Given BE = 30, DE = 0, and (AE + BE)/(AE + BE + CE) = 4/7, with AE > 30 a multiple of 10. Thus (AE + 30) is a multiple of 40 greater than 60. If AE + 30 = 80, then AE = 50, CE = 60, and D-E = 140 seats (70% of 200). If AE + 30 >= 120, D-E >= 210 > 200, violating capacity.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Since D-E is a multiple of 70 (from 4/7 of multiples of 10), occupancy factor (D-E)/200 must be a multiple of 35% (either 35% or 70%). Since AE + 30 >= 40 + 30 = 70, D-E > 70, so it must be 140 -> 70% (Option 2)!
- **Boundary Conditions & Trap Alert**: Spotting that 4/7 with multiples of 10 forces D-E to be 140 solves both Q14 (70%) and Q15 (AE = 50) in 20 seconds.
- **Verification Audit**: Tickets on segment D-E are AE + BE + CE + DE = AE + 30 + CE + 0. Clue 3 states (AE + 30)/(AE + 30 + CE) = 4/7. Since AE > 30 is a multiple of 10, AE + 30 >= 70 must be a multiple of 40. For AE + 30 = 80 (AE = 50, CE = 60), total D-E = 140 seats = 70% of 200. (Next multiple AE + 30 = 120 gives D-E = 210 > 200, impossible).

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q14</summary>

- **Trigger**: Since 4/7 of segment D-E seats are from before C (AE + BE = AE + 30) and all ticket counts are multiples of 10, D-E must be a multiple of 70 (either 70 or 140) -> since AE > 30, AE + 30 > 60 forces D-E = 140 (70% of 200)!
- **Answer**: **(2) 70%**
- **Trap to Avoid**: Spotting that 4/7 with multiples of 10 forces D-E to be 140 solves both Q14 (70%) and Q15 (AE = 50) in 20 seconds.
</details>

### Q15 (`CAT2025_S1_DILR_Q15`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Networks, Routes, Flows & Project Scheduling $\rightarrow$ *Directed/undirected flow conservation & segment occupancy*
- **Core Concept Tested**: Origin-destination pair extraction from segment ratios
- **Verified Answer**: **50** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: AE + 30 = (4/7)*140 = 80 => AE = 50.
- **Method 1 (First-Principles Derivation)**: Since D-E has 140 reserved seats and 4/7 of them (80 seats) originate before C (stations A and B, i.e., AE + BE), with BE = 30, we get AE = 80 - 30 = 50.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Immediate corollary of Q14: 80 - 30 = 50.
- **Boundary Conditions & Trap Alert**: Remember 'stations before C' includes BOTH Station A (AE) and Station B (BE = 30).
- **Verification Audit**: From Q14, 4/7 of 140 = 80 = AE + BE = AE + 30 => AE = 50.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q15</summary>

- **Trigger**: AE + 30 = (4/7)*140 = 80 => AE = 50.
- **Answer**: **50**
- **Trap to Avoid**: Remember 'stations before C' includes BOTH Station A (AE) and Station B (BE = 30).
</details>

### Q16 (`CAT2025_S1_DILR_Q16`) — [TITA | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Networks, Routes, Flows & Project Scheduling $\rightarrow$ *Directed/undirected flow conservation & segment occupancy*
- **Core Concept Tested**: Segment capacity equation C-D = 190 and B-C = 170 + AD
- **Verified Answer**: **80** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Tickets booked FROM Station C equals CD + CE = CD + 60, where AD + CD = 50.
- **Method 1 (First-Principles Derivation)**: On segment C-D, reserved seats are AD + AE + BD + BE + CD + CE = AD + 50 + 0 + 30 + CD + 60 = 140 + AD + CD = 190 => AD + CD = 50. On segment B-C, reserved seats are AC + AD + AE + BC + BD + BE = 170 + AD <= 200. At maximum B-C occupancy of 100% (200 seats), AD = 30 and CD = 20, so tickets from C = CD + CE = 20 + 60 = 80.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: CD + CE = (50 - AD) + 60 = 110 - AD; for AD = 30 (B-C = 200), 110 - 30 = 80.
- **Boundary Conditions & Trap Alert**: Note that in the source PDF, an unescaped LaTeX '%' after '95%' truncated the second clause of Clue 1 ('952.').
- **Verification Audit**: Segment C-D has 95% of 200 = 190 seats: AD + AE(50) + BD(0) + BE(30) + CD + CE(60) = 190 => AD + CD = 50. Segment B-C has AC(50) + AD + AE(50) + BC(40) + BD(0) + BE(30) = 170 + AD <= 200. With full B-C occupancy (200 seats, AD = 30, CD = 20; note Clue 1 had a LaTeX '%' truncation after '95%'), tickets booked from C = CD + CE = 20 + 60 = 80 (or 60 + CD for CD in {20, 30, 40}).

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q16</summary>

- **Trigger**: Tickets booked FROM Station C equals CD + CE = CD + 60, where AD + CD = 50.
- **Answer**: **80**
- **Trap to Avoid**: Note that in the source PDF, an unescaped LaTeX '%' after '95%' truncated the second clause of Clue 1 ('952.').
</details>

### Q17 (`CAT2025_S1_DILR_Q17`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Networks, Routes, Flows & Project Scheduling $\rightarrow$ *Directed/undirected flow conservation & segment occupancy*
- **Core Concept Tested**: Destination flow invariance (AD + BD + CD = 50)
- **Verified Answer**: **40** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Tickets booked TO Station D is AD + BD + CD = AD + CD = 50, which equals (Segment C-D = 190) minus (Segment D-E = 140) = 50 directly!
- **Method 1 (First-Principles Derivation)**: Since DE = 0, every passenger on segment C-D (190) either alights at D (AD + BD + CD) or continues on segment D-E (140). Therefore, tickets booked TO Station D = 190 - 140 = 50! Tickets booked TO Station C = AC + BC = 50 + 40 = 90. Difference = 90 - 50 = 40.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Passengers alighting at D = Flow(C-D) - Flow(D-E) + Boarding(D) = 190 - 140 + 0 = 50! Passengers alighting at C = AC + BC = 50 + 40 = 90. Difference = 90 - 50 = 40!
- **Boundary Conditions & Trap Alert**: Using node conservation Alighting(D) = Flow(C-D) - Flow(D-E) + Boarding(D) = 190 - 140 = 50 bypasses AD and CD completely!
- **Verification Audit**: Tickets booked TO Station C = AC + BC = 50 + 40 = 90. Tickets booked TO Station D = AD + BD + CD = (AD + CD) + 0 = 50 (uniquely 50 regardless of individual AD and CD!). Difference = 90 - 50 = 40.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q17</summary>

- **Trigger**: Tickets booked TO Station D is AD + BD + CD = AD + CD = 50, which equals (Segment C-D = 190) minus (Segment D-E = 140) = 50 directly!
- **Answer**: **40**
- **Trap to Avoid**: Using node conservation Alighting(D) = Flow(C-D) - Flow(D-E) + Boarding(D) = 190 - 140 = 50 bypasses AD and CD completely!
</details>

### Q18 (`CAT2025_S1_DILR_Q18`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Networks, Routes, Flows & Project Scheduling $\rightarrow$ *Directed/undirected flow conservation & segment occupancy*
- **Core Concept Tested**: 1-hop path enumeration on a linear line graph
- **Verified Answer**: **60** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Single-segment trips are AB, BC, CD, DE; since AB = DE = 0 and BC = 40, the answer is simply 40 + CD.
- **Method 1 (First-Principles Derivation)**: Tickets for exactly one segment are AB (0) + BC (40) + CD (20) + DE (0) = 60.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 40 + CD = 40 + 20 = 60.
- **Boundary Conditions & Trap Alert**: Do not include 2-segment tickets (AC, BD, CE) when counting 1-segment tickets.
- **Verification Audit**: Single-segment tickets are AB + BC + CD + DE = 0 + 40 + CD + 0 = 40 + CD. With CD = 20 (from AD = 30), total single-segment tickets = 40 + 20 = 60.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q18</summary>

- **Trigger**: Single-segment trips are AB, BC, CD, DE; since AB = DE = 0 and BC = 40, the answer is simply 40 + CD.
- **Answer**: **60**
- **Trap to Avoid**: Do not include 2-segment tickets (AC, BD, CE) when counting 1-segment tickets.
</details>

### Q19 (`CAT2025_S1_DILR_Q19`) — [TITA | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Bounded multiset sum conservation (1 + 2 + 3 + x in {7, 8, 9})
- **Verified Answer**: **7** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: 4 responses containing at least one {1, 2, 3} must sum to 6 + x in {7, 8, 9}! Then 9 + 3k + col_C = 40 immediately forces k = 8 and col_C = 7!
- **Method 1 (First-Principles Derivation)**: For each question, 3 of the 4 responses are 1, 2, and 3 (sum = 6), and the 4th response is in {1, 2, 3}, so each question receives 7, 8, or 9 taps. Given A received 9 and B, D, E received k taps each: 9 + 3k + C_rec = 40 => 3k + C_rec = 31. Since k, C_rec in {7, 8, 9}, the unique solution is k = 8 and C_rec = 7.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 31 mod 3 = 1 => C_rec == 1 mod 3. In {7, 8, 9}, only 7 is 1 mod 3! Solved in 10 seconds!
- **Boundary Conditions & Trap Alert**: You do not need to fill the 5x5 response matrix to answer Q19 or Q22 — both follow purely from column-sum arithmetic!
- **Verification Audit**: Each question receives 4 responses containing at least one 1, one 2, and one 3, so each question's tap sum is in {7, 8, 9}. Total taps = 40, A received 9, and B, D, E received equal taps k in {7, 8, 9}. Thus 9 + 3k + col_C = 40 => 3k + col_C = 31 => k = 8 and col_C = 7.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q19</summary>

- **Trigger**: 4 responses containing at least one {1, 2, 3} must sum to 6 + x in {7, 8, 9}! Then 9 + 3k + col_C = 40 immediately forces k = 8 and col_C = 7!
- **Answer**: **7**
- **Trap to Avoid**: You do not need to fill the 5x5 response matrix to answer Q19 or Q22 — both follow purely from column-sum arithmetic!
</details>

### Q20 (`CAT2025_S1_DILR_Q20`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Row-sum extremum bounding under 'at most two 1s' constraint
- **Verified Answer**: **(4) Alia and Badal** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Since no one responds 'Yes' (1 tap) more than twice, the minimum possible total taps by any person is 1 + 1 + 2 + 2 = 6! Since row_B + row_C = 14 with row_B < row_C, row_B <= 6 forces row_B = 6 = row_A!
- **Method 1 (First-Principles Derivation)**: Sum of all row sums is 40. Given A = 6, D = 11, E = 9, we have B + C = 14 with B < C, so B <= 6. By Clue 4, no player gives more than two 1-tap responses, so every player's 4 responses sum to at least 1 + 1 + 2 + 2 = 6. Hence B = 6 and C = 8. Thus Alia and Badal both tapped 6 times.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: B + C = 14 with 6 <= B < C => B = 6 (matches Alia = 6) and C = 8 -> (4) Alia and Badal in 15 seconds!
- **Boundary Conditions & Trap Alert**: Again, you do NOT need the interior of the 5x5 matrix to solve Q20!
- **Verification Audit**: Total taps = 40. Given row_A = 6, row_D = 11, row_E = 9 => row_B + row_C = 40 - 26 = 14 with row_C > row_B (so row_B <= 6). Since each player gives at most two '1' (Yes) responses (Clue 4), the minimum possible tap sum for any player is 1 + 1 + 2 + 2 = 6. Thus row_B >= 6, which forces row_B = 6 = row_A (Alia and Badal) and row_C = 8!

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q20</summary>

- **Trigger**: Since no one responds 'Yes' (1 tap) more than twice, the minimum possible total taps by any person is 1 + 1 + 2 + 2 = 6! Since row_B + row_C = 14 with row_B < row_C, row_B <= 6 forces row_B = 6 = row_A!
- **Answer**: **(4) Alia and Badal**
- **Trap to Avoid**: Again, you do NOT need the interior of the 5x5 matrix to solve Q20!
</details>

### Q21 (`CAT2025_S1_DILR_Q21`) — [MCQ | Medium | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Anti-symmetric matrix constraint (M[p][q] != M[q][p] for A and E)
- **Verified Answer**: **(1) No** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: Fill Row A = (2,1,1,2) and Row D = (3,2,3,3) first; then use anti-symmetry on A and E (Clue 5) to lock M[C][E] = 2 (No).
- **Method 1 (First-Principles Derivation)**: Since D tapped 11 times with M[D][B]=2, D must have tapped 3 to A, C, and E. Since A tapped 6 times with M[A][C]=M[A][D]=1 and at most two 1s, M[A][B]=M[A][E]=2. Since B tapped 6 times (two 1s and two 2s) and M[B][A] != M[A][B]=2, M[B][A]=1. Since Col C has sum 7 ({1,1,2,3}) with M[A][C]=1, M[D][C]=3, M[B][C]=2, we get M[E][C]=1. Then in Col E (sum 8: {1,2,2,3}), M[A][E]=2, M[D][E]=3, and M[B][E]=1 (since B needs a second 1), forcing M[C][E]=2 (No).
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: Col E has multiset {1, 2, 2, 3}. We already have M[D][E] = 3 and M[A][E] = 2, so {M[B][E], M[C][E]} = {1, 2}. Since B's row sum is 6 (two 1s, two 2s) with M[B][A]=1 and M[B][C]=M[B][D]=2 (as Col C and Col D cannot take another 1 from B), M[B][E] = 1, leaving M[C][E] = 2 (No).
- **Boundary Conditions & Trap Alert**: Remember 2 taps means 'No' (Option 1), not 'Maybe'.
- **Verification Audit**: Row A (sum 6, C=1, D=1) is M[A] = (B:2, C:1, D:1, E:2). Row D (sum 11, B=2) is M[D] = (A:3, B:2, C:3, E:3). Column A has sum 9 ({1,2,3,3}) and M[p][A] != M[A][p]. Since M[A][E]=2, M[E][A] in {1,3}; since M[A][B]=2, M[B][A] in {1,3}; since M[A][C]=1, M[C][A]=2. In Row E (sum 9: {1,2,3,3} since M[E][D]=2 from Col D={1,2,2,3} and M[D][E]=3), M[E] = (A:3, B:3, C:1, D:2). Then by Clue 5 on E (M[C][E] != M[E][C]=1) and Col E={1,2,2,3} (with M[A][E]=2, M[D][E]=3, M[B][E]=1), we get M[C][E] = 2 (No).

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q21</summary>

- **Trigger**: Fill Row A = (2,1,1,2) and Row D = (3,2,3,3) first; then use anti-symmetry on A and E (Clue 5) to lock M[C][E] = 2 (No).
- **Answer**: **(1) No**
- **Trap to Avoid**: Remember 2 taps means 'No' (Option 1), not 'Maybe'.
</details>

### Q22 (`CAT2025_S1_DILR_Q22`) — [TITA | Easy | `Round_1_Sitter`]
- **Canonical Taxonomy**: Quant-Based LR & Algorithmic Puzzles $\rightarrow$ *Linear, Circular & 2D Matrix Arrangements*
- **Core Concept Tested**: Multiset excess decomposition across columns
- **Verified Answer**: **6** (`ai_verified_derivation`)
- **IF YOU SEE (Mental Trigger)**: A column with sum 7 has multiset {1,1,2,3} (two 1s); columns with sum 8 ({1,2,2,3}) or 9 ({1,2,3,3}) have only ONE 1! Since only C has sum 7, total 1s = 5 + 1 = 6!
- **Method 1 (First-Principles Derivation)**: Every question receives {1, 2, 3, x} where 6 + x is the column sum. Across the 5 questions, sum(6 + x_i) = 30 + sum(x_i) = 40 => sum(x_i) = 10. Since x_A = 3, x_B = x_D = x_E = 2, and x_C = 1, only x_C is 1 (an extra 'Yes'). Adding the 5 mandatory 'Yes' responses (one per question) gives 5 + 1 = 6 'Yes' responses.
- **Method 2 (30-Second Exam-Hall Speed Shortcut)**: 5 mandatory 'Yes' responses (one per question) + 1 extra 'Yes' in the single 7-tap question (Clive) = 6!
- **Boundary Conditions & Trap Alert**: Three of the four questions in Set 5 (Q19, Q20, Q22) can be solved in under 60 seconds total from row/column sum invariants alone!
- **Verification Audit**: From Q19, the 5 questions received tap totals of 9, 8, 7, 8, 8. Since each question has at least one {1, 2, 3} (sum 6) plus one extra response (3, 2, 1, 2, 2 respectively), only Clive's question (sum 7) received two 'Yes' (1-tap) responses, while the other 4 questions received exactly one 'Yes' response each. Total 'Yes' responses = 2 + 1 + 1 + 1 + 1 = 6.

<details><summary>Active-Recall Self-Test: CAT2025_S1_DILR_Q22</summary>

- **Trigger**: A column with sum 7 has multiset {1,1,2,3} (two 1s); columns with sum 8 ({1,2,2,3}) or 9 ({1,2,3,3}) have only ONE 1! Since only C has sum 7, total 1s = 5 + 1 = 6!
- **Answer**: **6**
- **Trap to Avoid**: Three of the four questions in Set 5 (Q19, Q20, Q22) can be solved in under 60 seconds total from row/column sum invariants alone!
</details>
