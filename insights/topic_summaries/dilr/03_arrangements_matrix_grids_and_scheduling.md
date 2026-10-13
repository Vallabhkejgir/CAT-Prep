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
