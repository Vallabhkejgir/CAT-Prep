# DILR 03: Linear, Circular & 2D Matrix Arrangements and Scheduling

**Canonical Taxonomy Mapping**: `DILR > Linear, Circular & 2D Matrix Arrangements`  
**Weightage**: ~20–25% of DILR (1 set per slot)  
**Priority Tier**: Tier 1 (High-Yield Core)

---

## 1. Visual & Structural Anatomy

Arrangement, Matrix Grid, and Scheduling sets map a finite set of **Entities** (people, flights, lectures, houses) to **Positions/Slots** (linear chairs $1..N$, circular seats, time slots) and **Secondary Attributes** (cities, colors, numerical scores).
- **Linear & Dual-Row Seating**: Facing North vs. South, relative distance vs. seat index, blood-relation or numerical-value overlays.
- **Circular / Polygonal Seating**: Facing Center vs. Facing Outward (or mixed directions where left/right flips based on facing direction).
- **Multi-Attribute Assignment Matrix**: $N$ people $\times$ $M$ attributes where elimination of cross-pairs $(\times)$ and transitivity locks unique matches $(\checkmark)$.
- **Scheduling & Slot Allocation**: $N$ tasks across $T$ time slots with gap constraints ("exactly 2 days between X and Y"), dependency chains ("X before Y"), and resource capacity limits.

---

## 2. Green Flags vs. Red Flags

- **Green Flags**:
  - **Fixed reference frame** exists (e.g., numbered chairs $1$ to $8$, or days Monday to Saturday).
  - **Bi-conditional or block clues**: "A and B occupy consecutive slots", "The person from Delhi sits 3 places to the left of E".
- **Red Flags**:
  - Circular seating where **neither seat numbers nor facing directions (inward/outward)** are known for any person initially.
  - $\ge 4$ independent attributes with $8+$ entities requiring a massive $24 \times 24$ cross-hatch grid.

---

## 3. Scratchpad Representation Template

**NEVER draw a massive cross-hatch ($\times / \checkmark$) matrix for $\ge 4$ attributes**—it wastes 3 minutes just drawing lines. Instead, use a **Direct Column-Assignment Table** with one fixed anchor column!

```text
+-----------------------------------------------------------------------+
| ANCHOR COLUMN: Fix Time Slots (Mon–Fri) in Column 1!                  |
| Negative Pool (Write barred items directly inside cell with '~'):     |
+-------+----------+----------+----------+------------------------------+
| Slot  | Person   | City     | Score    | Blocked (~) / Notes          |
+-------+----------+----------+----------+------------------------------+
| 1 Mon |    A     | ~Del,~Mum|    40    |                              |
| 2 Tue |  B / C   |   Pune   |    25    | Gap of 2 from Fri            |
| 3 Wed |    D     |   Delhi  |    60    | Anchor clue [2]              |
| 4 Thu |  C / B   |  Mumbai  |    30    |                              |
| 5 Fri |    E     |  Chennai |    50    |                              |
+-------+----------+----------+----------+------------------------------+
```

### Circular Seating Linearization Trick
For $N$ seats around a circle, **break the circle at Anchor #1 (Seat 1 at the bottom facing Inward)** and write Seats $1, 2, \dots, N$ as a horizontal row with wrap-around edges ($N \leftrightarrow 1$):
- Facing **Inward**: `Right = +1 (Counter-Clockwise)`, `Left = -1 (Clockwise)`.
- Facing **Outward**: `Right = -1 (Clockwise)`, `Left = +1 (Counter-Clockwise)`.
- **Opposite Seat** (for even $N$): Seat $k$ is opposite Seat $\left(k + \frac{N}{2}\right) \pmod N$.

---

## 4. Anchor Clue & Case-Splitting Rules

1. **Choose the Ordered Dimension as Column 1**:
   - Always make **Time (Mon–Sat)**, **Floor ($1..8$)**, **Rank ($1..N$)**, or **Seat Number ($1..N$)** your fixed Column 1. Why? Because "2 slots after", "above", and "adjacent" are visually immediate on a fixed ordered column!
2. **Block Clues ("Gaps of Size $k$") First**:
   - A clue like *"There are 3 people between P and Q in an 8-seat row"* (`P _ _ _ Q` or `Q _ _ _ P`, span $= 5$ seats) has only $8 - 5 + 1 = 4$ possible placements—and combined with one exclusion, usually drops to $1$ or $2$ cases immediately.
3. **Distinctness & Pigeonhole Exhaustion**:
   - If cell $R_1$ can only be `{Delhi, Mumbai}` and cell $R_2$ can only be `{Delhi, Mumbai}`, then **no other row** can be Delhi or Mumbai (Naked Pair rule). Cross `{Delhi, Mumbai}` out of all remaining rows immediately!

---

## 5. Mathematical Invariants in Arrangements

- **Span Formula**: "There are $k$ slots between $A$ and $B$" means $| \text{Pos}(A) - \text{Pos}(B) | = k + 1$, occupying a contiguous block of $k + 2$ slots.
- **Parity Alternation on Grids/Rows**:
  - In a row $1..N$, two positions with an **odd** number of seats between them have the **same parity** (both odd or both even); two positions with an **even** number of seats between them have **opposite parity**.
- **Consecutive Sum / Average Overlays**:
  - When arrangement clues include *"Each person's age equals the average of their two immediate neighbors"*, then $a_{i} = \frac{a_{i-1} + a_{i+1}}{2} \implies$ the ages along the line MUST form an **Arithmetic Progression** (and around a circle, all ages must be **equal**!).

---

## 6. Solved Archetype Walkthrough: 5-Day Multi-Attribute Scheduling with Gap & Numerical Constraints

> **Set Scenario**: Five workshops (AI, Cloud, Cyber, Data, Web) are scheduled from Monday (Day 1) to Friday (Day 5), one per day, in 5 rooms ($101$ to $105$, not necessarily in order).
> 1. `Data` is held 3 days before the workshop in Room `104`.
> 2. Exactly 1 day separates `Cyber` (in Room `101`) and `AI`.
> 3. The workshop on Wednesday has a room number that is the average of Monday's and Friday's room numbers.
> 4. `Web` is held immediately after Room `105`, and neither `Web` nor `AI` is in Room `104`.
> 5. Room `102` is used before Room `103`.

### Step-by-Step Execution
1. **Anchor Clue 1 (`Data` is 3 days before Room `104`, so $\text{Day}(104) - \text{Day}(\text{Data}) = 3$)**:
   - Only two pairs of days have difference $3$: `(Mon, Thu)` or `(Tue, Fri)`.
2. **Test Case A: `Data` = Mon (Day 1), Room `104` = Thu (Day 4)** vs. **Case B: `Data` = Tue (Day 2), Room `104` = Fri (Day 5)**:
   - Look at Clue 2 (`Cyber [101]` and `AI` have gap of 1 day: `(1,3), (2,4),` or `(3,5)`):
     - In **Case B** (`Data` = Day 2, Room `104` = Day 5): Neither `Web` nor `AI` is in `104` (Day 5), and `Cyber` is in `101` ($\neq 104$). Since `Data` is on Day 2, who can be on Day 5 (`104`)? Only `Cloud`!
     - Then `Cyber` and `AI` must occupy `(Day 1, Day 3)` or `(Day 3, Day 5 - impossible)`. So `{Cyber, AI} = {Day 1, Day 3}`, leaving `Web` for Day 4!
     - Check Clue 4 (`Web` is immediately after `105`): So Day 3 = `105`. Since `Cyber` is `101`, Day 3 must be `AI [105]` and Day 1 must be `Cyber [101]`.
     - Check Clue 3 (Wed = Day 3 room is average of Mon and Fri rooms): Wed room is `105`, which CANNOT be the average of two distinct numbers from $\{101..105\}$! **Contradiction $\implies$ Case B is eliminated!**
3. **Lock Case A (`Data` = Mon [Day 1], Room `104` = Thu [Day 4])**:
   - Who is on Thu (`104`)? Not `Data` (Day 1), not `Cyber` (`101`), not `Web` or `AI` (Clue 4) $\implies$ **Thu (Day 4) = `Cloud [104]`**!
   - Clue 2 (`Cyber [101]` and `AI` separated by 1 day): Available days are Tue (2), Wed (3), Fri (5). Only pair with difference 2 is **(Wed [3], Fri [5])**!
   - Thus **Tue (Day 2) = `Web`**!
   - Clue 4 (`Web` is immediately after `105`): **Mon (Day 1) = `Data [105]`**.
   - Clue 3 (Wed room is average of Mon `105` and Fri room): From remaining rooms $\{101, 102, 103\}$, only $\frac{105 + 101}{2} = 103$ works!
   - Thus **Fri (Day 5) = `Cyber [101]`** and **Wed (Day 3) = `AI [103]`**!
   - Remaining room for **Tue (Day 2) = `Web [102]`** (check Clue 5: `102` on Tue is before `103` on Wed — valid!).

| Day | Workshop | Room |
| :--- | :--- | :--- |
| **1 Mon** | Data | 105 |
| **2 Tue** | Web | 102 |
| **3 Wed** | AI | 103 |
| **4 Thu** | Cloud | 104 |
| **5 Fri** | Cyber | 101 |

---

## 7. Active-Recall Drills

<details><summary>Q1: In an 8-seat linear row (Seats 1 to 8), 'there are 4 seats between A and B, and neither sits at an extreme end'. What are the exact seats occupied by A and B?</summary>
A: Span = 4 + 2 = 6 seats. Extreme ends (1 and 8) are excluded, so the seats must lie inside {2, 3, 4, 5, 6, 7}. The only pair at distance 5 inside {2..7} is {2, 7}!
</details>

<details><summary>Q2: Six people sit around a circular table; some face inward and some face outward. A sits 2nd to the right of B, and B sits 2nd to the right of A. What can you conclude about the facing directions of A and B?</summary>
A: Moving from B to A is 2 seats in B's right direction; moving back from A to B (the opposite physical direction around the circle) is also 2 seats in A's right direction. Therefore, A and B must face OPPOSITE directions (one inward, one outward)!
</details>

<details><summary>Q3: Why should you make the ordered dimension (e.g., Days Mon-Fri or Floors 1-6) the fixed leftmost column of your scratchpad table?</summary>
A: Because positional clues ('2 days before', 'immediately above', 'at least 3 slots between') translate into fixed visual row offsets only when the ordered dimension is sorted in Column 1.
</details>

<details><summary>Q4: Five people have distinct scores from {1, 2, 3, 4, 5}. Clue: 'A's score is the average of B's and C's scores, and D's score is the average of A's and E's scores.' What can A's score be?</summary>
A: For D = (A + E)/2 to be an integer, A and E must have the same parity. If A = 3, E in {1, 5} -> D in {2, 4}, leaving the other three numbers for {B, C} averaging to 3! Check A = 2: B, C must be {1, 3}, then E = 4 -> D = 3 (collision with C = 3!). By symmetry A = 4 also fails. Thus A MUST be 3!
</details>

<details><summary>Q5: In a bi-directional matrix puzzle, 3 rows (R1, R2, R3) each have 2 items selected from 6 items, and you find R1 has {P, Q} or {P, R}, while R2 has {Q, R}. How do you reduce R1?</summary>
A: In R1 U R2, if R1 = {P, Q} and R2 = {Q, R}, item Q is used twice. If each of the 6 items is used exactly once across the 3 rows, Q and R are already taken by R2, which contradicts both options unless items can repeat; if each item is used once, R2={Q,R} eliminates both Q and R from R1!
</details>

---

## CAT 2025 PYQ Edge Examples & Newly Surfaced Patterns

### Newly Surfaced Sub-Topic Variants & Pattern Triggers (CAT 2025)
- **Ball-Hoop Threshold Interval Ordering / Ferrers Graph (`CAT_2025_DILR_Slot_2` `SET1`)**: If Ball $B_i$ passes without pinging ($d_B < d_H$), pings ($d_B = d_H$ or threshold range), or gets stuck, row/column sums induce a strict monotonic ordering of ball and hoop diameters.
- **Circular Seating with Modular Step Transitions (`CAT_2025_DILR_Slot_1` `SET1` & `CAT_2025_DILR_Slot_3` `SET4`)**: Convert clockwise/counterclockwise seat jumps on a 7-chair circle into residues $\pmod 7$ and prune impossible branches using 1-step look-ahead.
- **Interval Packing with Pairwise Overlap ('Gurubhai' Scheduling, `CAT_2025_DILR_Slot_2` `SET5`)**: Partition a 12-year timeline into four disjoint 3-year blocks for a capacity-1 Guru before placing overlapping 2-capacity intervals.

### Solved CAT 2025 PYQ Edge Exemplars

#### CAT2025_S1_DILR_Q01 (`CAT_2025_DILR_Slot_1` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Circular state-transition game on a 7-chair ring*
- **Verified Answer**: `4` (With 4 occupied chairs on a 7-chair circle where A and C are adjacent and both B and D have empty chairs on both sides, the initial occupied chairs must follow the cyclic spacing pattern {A, C}-E-B-E-D-E. Since C is at Chair 7 (unchanged through Turn 2) and D is at Chair 2 (unchanged through Turn 1), the empty chairs initially must be {1, 3, 5}, forcing A = 6 and B = 4.)
- **Mental Trigger (`See X -> Do Y`)**: On a 7-chair circle with 4 friends and 3 empty chairs, having empty chairs on BOTH sides of B and D forces the 3 empty chairs to alternate with B and D: E - D - E - B - E - A - C!
- **First-Principles Method**: Since C does not move until Turn 3 and is at Chair 7 after Turn 2, C starts at Chair 7. Since D does not move until Turn 4 and is at Chair 2 after Turn 1, D starts at Chair 2. For D (at 2) to have empty chairs on both sides, Chairs 1 and 3 must be empty initially. Since C is at 7 and A is adjacent to C, A must be at Chair 6. For B to have empty chairs on both sides among remaining chairs {4, 5}, Chair 5 must be empty and B must start at Chair 4.
- **30-Second Exam-Hall Speed Shortcut**: D=2 has empty neighbors 1 and 3 => C=7 must have neighbor A=6 => remaining B must sit at 4 with empty neighbors 3 and 5! Solved in 30 seconds without even simulating the turns!
- **Trap Alert & Boundary Condition**: Notice that D's position after Turn 1 IS D's initial position because only A moves in Turn 1.

#### CAT2025_S1_DILR_Q02 (`CAT_2025_DILR_Slot_1` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Look-ahead state transition pruning on circular tracks*
- **Verified Answer**: `(4) No one` (Start: {A:6, B:4, C:7, D:2}. Turn 1 (A CW): A->1; Turn 2 (B CCW to make all 4 adjacent at {7,1,2,3}): B->3; Turn 3 (C CCW so D can later reach Chair 4 in Turn 4): C->6. Thus at the end of Turn 3, occupied chairs are {1, 2, 3, 6}, leaving Chair 4 empty.)
- **Mental Trigger (`See X -> Do Y`)**: In Turn 4, D (at Chair 2) must land on Chair 4 (the first empty chair in its chosen direction), which requires Chair 3 to be occupied and Chair 4 to be EMPTY at the end of Turn 3!
- **First-Principles Method**: To make all 4 friends adjacent at the end of Turn 2 with D=2 and C=7, A moves 6->1 in Turn 1 and B moves 4->3 in Turn 2 (occupying {7,1,2,3}). In Turn 3, C moves 7->6 (occupying {1,2,3,6}) so that in Turn 4, D moves CW from 2 past occupied 3 into empty Chair 4. Hence Chair 4 is empty at the end of Turn 3.
- **30-Second Exam-Hall Speed Shortcut**: Since D moves to Chair 4 in Turn 4, Chair 4 MUST be unoccupied at the end of Turn 3 -> (4) No one immediately!
- **Trap Alert & Boundary Condition**: You don't even need to trace Turn 3 to know Chair 4 is empty at the end of Turn 3: D moves into Chair 4 on Turn 4!

#### CAT2025_S1_DILR_Q03 (`CAT_2025_DILR_Slot_1` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Adjacency block constraint at Turn 6*
- **Verified Answer**: `(1) Chairs numbered 4, 5, 6, and 7` (After Turn 4: {A:1, B:3, C:6, D:4}. Turn 5 (A moves CCW 1->7 so Turn 5 is not adjacent): {A:7, B:3, C:6, D:4}. Turn 6 (B moves CW 3->5 so all 4 are adjacent at the end of Turn 6): {A:7, B:5, C:6, D:4} = Chairs 4, 5, 6, and 7.)
- **Mental Trigger (`See X -> Do Y`)**: At Turn 4 end, C=6 and D=4; to form a 4-adjacent block at Turn 6 after A (Turn 5) and B (Turn 6) move, A and B must fill chairs 7 and 5, forming {4, 5, 6, 7}.
- **First-Principles Method**: After Turn 4, occupied chairs are {1, 3, 4, 6}. If A moved CW 1->5 in Turn 5, {3, 4, 5, 6} would already be adjacent at Turn 5 (violating Clue 1). Thus A moves CCW 1->7 in Turn 5 ({3, 4, 6, 7}), and B moves CW 3->5 in Turn 6, giving {4, 5, 6, 7}.
- **30-Second Exam-Hall Speed Shortcut**: Since C=6 and D=4 do not move in Turns 5 and 6, the occupied set at Turn 6 must contain BOTH 4 and 6. Only Option (1) {4, 5, 6, 7} contains both 4 and 6!
- **Trap Alert & Boundary Condition**: Checking that C=6 and D=4 are stationary during Turns 5-6 eliminates Options (2), (3), and (4) in 5 seconds.

#### CAT2025_S1_DILR_Q04 (`CAT_2025_DILR_Slot_1` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Invariance under final-move branching*
- **Verified Answer**: `(2) Davies only` (At the end of Turn 6, {D:4, B:5, C:6, A:7}. In Turn 7, C (at Chair 6) moves either CW to Chair 1 or CCW to Chair 3, vacating Chair 6. Thus at the end of Turn 7, Bashir (at Chair 5) has Davies at Chair 4 and an empty Chair 6.)
- **Mental Trigger (`See X -> Do Y`)**: At Turn 6, B is at 5 between D(4) and C(6); since C is the mover in Turn 7, C vacates Chair 6 regardless of direction, leaving only D(4) adjacent to B(5)!
- **First-Principles Method**: At Turn 6, B=5, D=4, C=6, A=7. In Turn 7, C must move to the first empty chair (either Chair 1 CW or Chair 3 CCW). In both cases, Chair 6 becomes empty while D remains at Chair 4. Hence only Davies is adjacent to Bashir at the end of Turn 7.
- **30-Second Exam-Hall Speed Shortcut**: C is sitting at 6 next to B(5) and C moves on Turn 7, so Chair 6 becomes empty and only D(4) remains next to B(5).
- **Trap Alert & Boundary Condition**: Do not assume C's Turn-7 direction matters; both directions leave Chair 6 empty.

#### CAT2025_S2_DILR_Q01 (`CAT_2025_DILR_Slot_2` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Multi-variable attribute mapping & ordering inequalities — *Transitive interval ordering of ball and hoop diameters (Ferrers / threshold graph)*
- **Verified Answer**: `6` (A ball pings iff diameter(B) <= diameter(H). From Clue 4 (only B2 pings on H2), B2 <= H2 < all other balls (B2 is smallest, pings on all 4 hoops = 4 pings). From Clue 3 (all except B3 ping on H1), H1 < B3 (B3 is largest, pings on 0 hoops = 0 pings). From Clue 1 & 2, B4 <= H3 < B1 <= H4 < B5 <= H1 < B3, so B1 pings on H4 and H1 (2 pings). Total pings by B1, B2, B3 = 2 + 4 + 0 = 6.)
- **Mental Trigger (`See X -> Do Y`)**: Translate every 'ping' into B_i <= H_j and every 'no ping' into B_i > H_j, then chain all balls and hoops on a single 1D number line!
- **First-Principles Method**: Clue 4: B2 <= H2 < {B1,B3,B4,B5,B6}. Clue 2: B4 <= H3 < B1. Clue 1: {B1,B6} <= H4 < B5. Clue 3: {B1,B2,B4,B5,B6} <= H1 < B3. Combining gives the strict chain: B2 <= H2 < B4 <= H3 < B1 <= H4 < B5 <= H1 < B3 (with H2 < B6 <= H4). Thus B1 pings on {H4, H1} (2), B2 pings on {H2, H3, H4, H1} (4), and B3 pings on {} (0). Sum = 2 + 4 + 0 = 6.
- **30-Second Exam-Hall Speed Shortcut**: Single number-line chain B2 <= H2 < B4 <= H3 < B1 <= H4 < B5 <= H1 < B3 cracks all 4 questions in 90 seconds flat!
- **Trap Alert & Boundary Condition**: Remember 'ping' means B <= H (smaller ball passes through larger hoop), not B >= H.

#### CAT2025_S2_DILR_Q02 (`CAT_2025_DILR_Slot_2` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Multi-variable attribute mapping & ordering inequalities — *Partial order vs total order identification*
- **Verified Answer**: `(D) B1 < B6 < B3` (From the number-line chain B2 <= H2 < B4 <= H3 < B1 <= H4 < B5 <= H1 < B3, options (A) B4 < B5 < B3, (B) B2 < B1 < B5, and (C) B1 < B5 < B3 are all necessarily true. However, for B6 we only know H2 < B6 <= H4, so B6 could be smaller than B1 (e.g., B6 <= H3 < B1). Thus B1 < B6 < B3 is NOT necessarily true.)
- **Mental Trigger (`See X -> Do Y`)**: We have no clue about B6 on H3, so B6 and B1 are incomparable (both lie <= H4, and B6 could be <= H3 < B1)!
- **First-Principles Method**: B1, B2, B3, B4, B5 are totally ordered as B2 < B4 < B1 < B5 < B3, making (A), (B), and (C) definitely true. Since B6 is only constrained by H2 < B6 <= H4, B6 can be smaller than, equal to, or larger than B1. Hence (D) is not necessarily true.
- **30-Second Exam-Hall Speed Shortcut**: Spot B6 in Option (D): B6 is the only ball not tested against H3 in the clues!
- **Trap Alert & Boundary Condition**: None; classic 10-second elimination.

#### CAT2025_S2_DILR_Q03 (`CAT_2025_DILR_Slot_2` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Multi-variable attribute mapping & ordering inequalities — *Monotonic ordering of threshold hoops by ping counts*
- **Verified Answer**: `(B) H2 < H3 < H4 < H1` (From the number-line chain H2 < B4 <= H3 < B1 <= H4 < B5 <= H1, the hoop order is strictly H2 < H3 < H4 < H1.)
- **Mental Trigger (`See X -> Do Y`)**: Since a larger hoop passes every ball a smaller hoop passes, just order hoops by number of pings: H2 (1 ping) < H3 (2 or 3 pings) < H4 (4 pings) < H1 (5 pings)!
- **First-Principles Method**: H2 is passed only by B2 (1 ball); H3 is passed by B2, B4 (and possibly B6); H4 is passed by B2, B4, B1, B6 (4 balls); H1 is passed by all except B3 (5 balls). Thus H2 < H3 < H4 < H1.
- **30-Second Exam-Hall Speed Shortcut**: H2 has 1 ping and H1 has 5 pings -> H2 is smallest and H1 is largest -> H2 < H3 < H4 < H1 (Option B).
- **Trap Alert & Boundary Condition**: Do not invert the inequality direction.

#### CAT2025_S2_DILR_Q04 (`CAT_2025_DILR_Slot_2` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Multi-variable attribute mapping & ordering inequalities — *Degree-of-freedom counting in binary incidence matrices*
- **Verified Answer**: `(C) 12 or 13` (Pings by B1..B5 are fixed at 2 + 4 + 0 + 3 + 1 = 10. B6 pings on H1 and H4 (2), does not ping on H2 (0), and may or may not ping on H3 (0 or 1), giving 2 or 3 pings for B6. Total pings = 10 + (2 or 3) = 12 or 13.)
- **Mental Trigger (`See X -> Do Y`)**: Only 1 cell in the entire 6x4 matrix is unknown: (B6, H3) in {0, 1}! All other 23 cells are fixed, with 12 ones!
- **First-Principles Method**: Summing pings by hoop: H2 = 1 (only B2), H1 = 5 (all except B3), H4 = 4 (B2, B4, B1, B6 since B5 and B3 fail), and H3 = 2 or 3 (B2 and B4 definitely pass; B1, B5, B3 definitely fail; B6 is unknown). Total = 1 + 5 + 4 + (2 or 3) = 12 or 13.
- **30-Second Exam-Hall Speed Shortcut**: Sum by hoops: H1(5) + H4(4) + H2(1) + H3(2 or 3) = 12 or 13 (Option C).
- **Trap Alert & Boundary Condition**: Do not forget that B4 <= H3 < B1 <= H4 implies B4 also passes through H4!

#### CAT2025_S2_DILR_Q18 (`CAT_2025_DILR_Slot_2` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Scheduling with slot/gap constraints — *Interval scheduling with disjoint capacity and span deduction*
- **Verified Answer**: `(A) 2020` (Raghunath (R) only trained students during 2013-2014 (2 yrs) and 2019-2020 (2 yrs), so R's span is 2 years! Since Samiran (S) trains at most 1 student per year across 12 years (2013-2024) for 4 students, S's span is 3 years (4*3 = 12), and Meghnath's (M) span is 4 years. Since A started under M in 2013 (2013-2016) and B started under S in 2013 (2013-2015), neither A nor B could train under R in 2013-2014! Thus C and D trained under R in 2013-2014, and A and B trained together under R in 2019-2020! Hence A and B were Gurubhai in 2020.)
- **Mental Trigger (`See X -> Do Y`)**: R is active ONLY in 2013-2014 and 2019-2020 -> R's span MUST be 2 years! Since A and B are busy with M and S in 2013-2014, A and B MUST take R's 2019-2020 slot together -> Gurubhai in 2019 and 2020!
- **First-Principles Method**: Clue 2 restricts R to two 2-year windows: 2013-2014 and 2019-2020. Since all 4 students must train under R for consecutive years and at most 2 students can train under a Guru simultaneously, R's span is 2 years, with 2 students in 2013-2014 and 2 students in 2019-2020. By Clue 4, A and B are occupied with M and S in 2013, so C and D take R in 2013-2014, forcing A and B to take R together in 2019-2020. Thus A and B were Gurubhai in 2020 (Option A).
- **30-Second Exam-Hall Speed Shortcut**: You don't even need the full 12-year schedule to answer Q18: R only has 2013-14 and 2019-20, and A, B are busy in 2013 -> A and B are Gurubhai under R in 2019-2020 -> (A) 2020 in 30 seconds!
- **Trap Alert & Boundary Condition**: Deducing the 3 Guru spans (R = 2, S = 3, M = 4) first is the master key to the entire set.

#### CAT2025_S2_DILR_Q19 (`CAT_2025_DILR_Slot_2` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Scheduling with slot/gap constraints — *Pairwise overlap (Gurubhai = 2 years) forcing interval start times*
- **Verified Answer**: `(A) 2015` (A is under M in 2013-2016 (4 yrs). By Clue 3, A and C are Gurubhai for 2 years, and A and B are already Gurubhai under R in 2019-2020 (2 yrs), while S never has Gurubhais (1 student/yr). So A and C MUST be Gurubhai under M for 2 years! Since C is under R in 2013-2014, C must overlap with A (2013-2016) in 2015-2016, meaning C starts under M in 2015 (2015-2018)!)
- **Mental Trigger (`See X -> Do Y`)**: Since S trains only 1 student/year (0 Gurubhais) and R only pairs (C,D) in 2013-14 and (A,B) in 2019-20, the pairs (A,C) and (B,D) MUST be Gurubhais under M for 2 years each!
- **First-Principles Method**: Gurubhai pairs can only occur under R or M (since S trains at most 1 student/year). Under R, (C, D) are Gurubhai in 2013-2014 (2 yrs) and (A, B) are Gurubhai in 2019-2020 (2 yrs). By Clue 3, (A, C) and (B, D) must also be Gurubhai for 2 years each, which can ONLY happen under M! Since A is under M in 2013-2016 and C is busy with R in 2013-2014, C must overlap with A in 2015-2016, so C begins under M in 2015 (2015-2018).
- **30-Second Exam-Hall Speed Shortcut**: A is under M in 2013-2016; C needs a 2-year overlap with A under M and is busy in 2013-2014 -> C must start M in 2015 (Option A)!
- **Trap Alert & Boundary Condition**: Realizing S produces 0 Gurubhai pairs and R produces only (C,D) and (A,B) makes M's overlaps 100% deterministic.

#### CAT2025_S2_DILR_Q20 (`CAT_2025_DILR_Slot_2` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Scheduling with slot/gap constraints — *Disjoint block packing in 2019-2024*
- **Verified Answer**: `(A) 2022` (In M, (A,C) occupy 2013-2018 (A: 2013-16, C: 2015-18). Since (A,D), (B,C), (C,D) cannot overlap in M (C,D already have 2 Gurubhai years in R!), the (B,D) 4-year blocks in M must start at >= 2019! Specifically, D is under M in 2019-2022 and B (who is under R in 2019-2020) is under M in 2021-2024, overlapping in 2021 and 2022!)
- **Mental Trigger (`See X -> Do Y`)**: Since C is under M until 2018 and neither B nor D can overlap with C in M, both B and D must do their M training in 2019-2024 (6 years for two 4-year blocks -> they MUST overlap in the middle 2 years: 2021 and 2022)!
- **First-Principles Method**: C is under M in 2015-2018. If B or D trained under M in 2018 or earlier, they would overlap with A or C (violating Clue 3 since (A,D)=0, (B,C)=0, and (C,D) already has 2 years in R). Thus both B and D must fit their 4-year M blocks inside the 6-year window 2019-2024! Any two 4-year blocks inside 2019-2024 with a 2-year overlap must be 2019-2022 (D) and 2021-2024 (B), overlapping in 2021 and 2022. Hence 2022 (Option A).
- **30-Second Exam-Hall Speed Shortcut**: Two 4-year blocks in the 6-year window 2019..2024 ALWAYS overlap in the middle 2 years: 2021 and 2022 -> (A) 2022!
- **Trap Alert & Boundary Condition**: You don't even need to know which of B or D starts in 2019 vs 2021 to know their overlap is {2021, 2022}!

#### CAT2025_S2_DILR_Q21 (`CAT_2025_DILR_Slot_2` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Scheduling with slot/gap constraints — *Partitioning 12 years into four 3-year non-overlapping slots for Ustad Samiran*
- **Verified Answer**: `(A) Charu was training under Ustad Samiran in 2019.` (S's four 3-year blocks are 2013-15 (B), 2016-18, 2019-21, and 2022-24. In 2016-18, A is busy in 2016 (M) and C is busy in 2016-18 (M), so D MUST take S in 2016-2018! In 2019-21, A is busy in 2019-20 (R), so C MUST take S in 2019-2021, and A takes S in 2022-2024. Thus Charu was training under Ustad Samiran in 2019.)
- **Mental Trigger (`See X -> Do Y`)**: 4 students * 3 years = 12 years means Ustad Samiran's 4 slots are strictly 2013-15 (B), 2016-18 (D), 2019-21 (C), and 2022-24 (A)!
- **First-Principles Method**: Since S trains 1 student at a time for 3 consecutive years across the 12-year span 2013-2024, S's four slots are 2013-15, 2016-18, 2019-21, and 2022-24. B takes 2013-15 (Clue 4). In 2016-18, both A (in M till 2016) and C (in M 2015-18) are busy, so D takes 2016-18. In 2019-21, A is busy with R (2019-20), so C takes 2019-21 and A takes 2022-24. Thus Charu was under S in 2019 (Option A).
- **30-Second Exam-Hall Speed Shortcut**: In 2016-18, A and C are in M => D gets S(2016-18). In 2019-21, A is in R => C gets S(2019-21) -> Option (A)!
- **Trap Alert & Boundary Condition**: Recognizing that 4 * 3 = 12 partitions 2013-2024 into four rigid 3-year blocks avoids trial-and-error.

#### CAT2025_S2_DILR_Q22 (`CAT_2025_DILR_Slot_2` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Scheduling with slot/gap constraints — *Column-wise capacity summation across the 12-year schedule*
- **Verified Answer**: `4` (Active students per year: 2013(4), 2014(4), 2015(3), 2016(3), 2017(2: C in M, D in S), 2018(2: C in M, D in S), 2019(4), 2020(4), 2021(3), 2022(3), 2023(2: B in M, A in S), 2024(2: B in M, A in S). Years with exactly 2 musicians training = 4 (2017, 2018, 2023, 2024).)
- **Mental Trigger (`See X -> Do Y`)**: In every year, S has 1 student. R has 2 students in 2013-14 & 2019-20 (0 otherwise). M has 2 students in overlap years (2015-16, 2021-22) and 1 student in non-overlap years (2013-14, 2017-18, 2019-20, 2023-24). Total = 2 occurs when R=0 and M=1 (2017, 2018, 2023, 2024) = 4 years!
- **First-Principles Method**: Total active students in year y is S(y) + R(y) + M(y). Since S(y) = 1 for all y, we need R(y) + M(y) = 1. Since M(y) >= 1 for all y, this requires R(y) = 0 and M(y) = 1 (non-overlap years of M outside 2013-14 and 2019-20), which are 2017, 2018, 2023, and 2024 (4 years).
- **30-Second Exam-Hall Speed Shortcut**: Total student-years = 4*(2 + 3 + 4) = 36 across 12 years. The two 6-year halves (2013-18 and 2019-24) are completely symmetric: each has two 4-student years, two 3-student years, and two 2-student years -> 2 + 2 = 4 years!
- **Trap Alert & Boundary Condition**: Notice the exact 6-year translational symmetry between 2013-2018 and 2019-2024!

#### CAT2025_S3_DILR_Q14 (`CAT_2025_DILR_Slot_3` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Circular seating with modular step transitions — *Modular arithmetic (+1, +2, -1, -2 mod 7) on a 7-seat circle*
- **Verified Answer**: `(D) Eshan` (Index seats 0..6 in the 'Immediate left' (+1) direction with Bina = 0. Round 1 (+1): Aarav = 1. Round 2 (-2): seat 1 - 2 = 6 (R1 of Bina). Round 3 (-1): Diya = seat 6 - 1 = 5. Round 5 ends at Aarav (1); Round 6 (+2): seat 3; Round 7 (+1): Gaurav = 4. Remaining seats {2, 3, 6} are {Chirag, Farhan, Eshan}. Since Round 8 (+1 from Gaurav=4) lands on Diya (5), Round 9 goes from Diya (5) to Farhan (must be seat 3 via -2, since if Farhan were at 6, Round 10 from 6 could only reach {0,1,4,5}, none of which is Chirag!), and Round 10 goes from Farhan (3) to Chirag (seat 2 via -1). Thus Eshan is at seat 6 (immediately to the right of Bina).)
- **Mental Trigger (`See X -> Do Y`)**: Encode 'Immediate left' = +1, 'Second left' = +2, 'Immediate right' = -1, 'Second right' = -2 (mod 7) with Bina = 0!
- **First-Principles Method**: Setting Bina = 0 and Left = +1 (mod 7): Round 1 gives Aarav = 0 + 1 = 1. Round 2 goes to 1 - 2 = 6, and Round 3 goes to Diya = 6 - 1 = 5. From Round 5 (Aarav = 1), Round 6 (+2) goes to 3, Round 7 (+1) gives Gaurav = 4, and Round 8 (+1) lands on 5 (Diya). From 5 (Diya), Round 9 reaches Farhan and Round 10 reaches Chirag among unoccupied seats {2, 3, 6}. Since 2 cannot be reached from 5 in one step and 6 cannot reach 2 or 3 in one step, Round 9 must go 5 -> 3 (Farhan = 3) and Round 10 must go 3 -> 2 (Chirag = 2), leaving Eshan = 6 (immediately to the right of Bina).
- **30-Second Exam-Hall Speed Shortcut**: Modulo-7 addition fixes B=0, A=1, G=4, D=5 in 15 seconds; then 5 -> Farhan -> Chirag inside {2, 3, 6} forces Farhan=3, Chirag=2, leaving Eshan=6 (R1 of Bina)!
- **Trap Alert & Boundary Condition**: Converting circular left/right passes into +-1, +-2 (mod 7) eliminates all spatial confusion.

#### CAT2025_S3_DILR_Q15 (`CAT_2025_DILR_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Circular seating with modular step transitions — *Circular offset lookup*
- **Verified Answer**: `(B) Chirag` (Eshan is at seat 6. Third to the left (+3 mod 7) of seat 6 is (6 + 3) mod 7 = seat 2, which is occupied by Chirag.)
- **Mental Trigger (`See X -> Do Y`)**: In our +1 = Left coordinate system, 'third to the left of Eshan (6)' is simply (6 + 3) mod 7 = 2 = Chirag!
- **First-Principles Method**: The seating order in the left (+1) direction is 0:Bina, 1:Aarav, 2:Chirag, 3:Farhan, 4:Gaurav, 5:Diya, 6:Eshan. Moving 3 seats to the left from Eshan (6) reaches 0 (1st), 1 (2nd), 2 (3rd) = Chirag.
- **30-Second Exam-Hall Speed Shortcut**: (6 + 3) mod 7 = 2 -> Chirag (Option B).
- **Trap Alert & Boundary Condition**: None; instant 5-second read from the seating circle.

#### CAT2025_S3_DILR_Q16 (`CAT_2025_DILR_Slot_3` | MCQ | Hard | `Round_2_Doable`)
- **Sub-Topic**: Circular seating with modular step transitions — *Modular wrap-around equivalence (+1 + 2 == -2 - 2 mod 7)*
- **Verified Answer**: `(D) Immediately to the right` (Between Round 3 (Diya at seat 5) and Round 5 (Aarav at seat 1), the net shift over Rounds 4 and 5 is 1 - 5 = -4 == +3 (mod 7). In two steps from {+1, +2, -1, -2}, this shift can be achieved EITHER as (+1) + (+2) (one L1 and one L2) OR as (-2) + (-2) = -4 == +3 (mod 7) (two R2s)! Thus L1, L2, and R2 counts vary between the two cases, whereas R1 (-1, 'Immediately to the right') is NEVER used in Rounds 4-5 and is uniquely fixed at 2 occurrences (Round 3 and Round 10)!)
- **Mental Trigger (`See X -> Do Y`)**: On a 7-circle, moving +3 (from 5 to 1) in 2 steps can be done EITHER via Left (+1 + 2 = +3) OR via Right (-2 + -2 = -4 == +3 mod 7)! Neither uses R1 (-1)!
- **First-Principles Method**: All rounds except Rounds 4 and 5 have fixed pass types: R1=L1, R2=R2, R3=R1, R6=L2, R7=L1, R8=L1, R9=R2, R10=R1. In Rounds 4 and 5, moving from seat 5 to seat 1 requires a 2-step displacement of +3 == -4 (mod 7), which can be (+1, +2), (+2, +1), or (-2, -2). Across all three valid paths, the pass type -1 ('Immediately to the right') occurs 0 times in Rounds 4-5, so its total count is uniquely 2.
- **30-Second Exam-Hall Speed Shortcut**: Spot that (+1) + (+2) creates an order ambiguity in Round 4 vs Round 5, AND (-2) + (-2) = -4 == +3 (mod 7) trades L1+L2 for R2+R2, leaving only R1 (-1) invariant!
- **Trap Alert & Boundary Condition**: Students who forget modular wrap-around (-4 == +3 mod 7) think only the order of L1 and L2 is ambiguous and miss why L1, L2, and R2 counts all change!

#### CAT2025_S3_DILR_Q17 (`CAT_2025_DILR_Slot_3` | MCQ | Hard | `Round_2_Doable`)
- **Sub-Topic**: Circular seating with modular step transitions — *Intermediate state reachability in 2-step modular paths*
- **Verified Answer**: `(B) Gaurav` (Every round's receiver is fixed EXCEPT Round 4 (which starts at Diya = 5 and ends at Aarav = 1 in Round 5). The three possible intermediate receivers in Round 4 are seat 6 (Eshan, via +1), seat 0 (Bina, via +2), or seat 3 (Farhan, via -2). Thus Eshan, Bina, and Farhan each have an uncertain count depending on Round 4, whereas Gaurav (seat 4) is never visited in Round 4 and received the Buck uniquely 1 time (in Round 7).)
- **Mental Trigger (`See X -> Do Y`)**: From Diya (5) to Aarav (1) in 2 steps, the Round-4 intermediate holder can be 5+1=6 (Eshan), 5+2=0 (Bina), or 5-2=3 (Farhan) — eliminating (A), (C), and (D) and leaving (B) Gaurav!
- **First-Principles Method**: Receivers in Rounds 1, 2, 3, 5, 6, 7, 8, 9, 10 are uniquely fixed as: 1:Aarav, 2:Eshan(6), 3:Diya(5), 5:Aarav(1), 6:Farhan(3), 7:Gaurav(4), 8:Diya(5), 9:Farhan(3), 10:Chirag(2). In Round 4, the receiver can be Eshan (if R4=+1, R5=+2), Bina (if R4=+2, R5=+1), or Farhan (if R4=-2, R5=-2). Only Gaurav's count (1 time, in Round 7) is invariant.
- **30-Second Exam-Hall Speed Shortcut**: The 3 paths in Round 4 visit seats 6 (Eshan), 0 (Bina), and 3 (Farhan) — which are literally the 3 distractors (A), (C), (D)! Only Gaurav (seat 4, Option B) is untouched!
- **Trap Alert & Boundary Condition**: Notice how the 3 distractors in Q17 (Bina, Farhan, Eshan) are the exact 3 intermediate vertices of the 3 paths in Q16!
