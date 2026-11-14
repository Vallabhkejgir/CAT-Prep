# DILR 03 Concept & Grid-Evolution Examples: Linear, Circular & 2D Matrix Arrangements and Scheduling

> **Companion Reference**: [`../topic_summaries/dilr/03_arrangements_matrix_grids_and_scheduling.md`](../topic_summaries/dilr/03_arrangements_matrix_grids_and_scheduling.md) | [`DILR_Archetype_Templates.md`](../high_recall/cheat_sheets/DILR_Archetype_Templates.md)

---

## Concept 1: Direct Column-Assignment Grid (Fixed Ordered Column 1 vs. Cross-Hatch Matrix)

### 1. Concept & Invariant in Plain English
When a puzzle maps $5$ people to $5$ days (Mon–Fri), $5$ cities, and $5$ scores, **never** draw a giant $15 \times 15$ tick-and-cross ($\checkmark / \times$) grid!
Instead, draw a **4-column table** and lock the **naturally ordered attribute** (`Day 1 Mon` to `Day 5 Fri`, or `Floor 1` to `Floor 5`, or `Seat 1` to `Seat 5`) permanently into **Column 1**. Write negative exclusions (`~Delhi`) directly in the right margin of the row until only one choice remains!

### 2. When to Use It (Set / Question Cue)
- Any multi-attribute arrangement or scheduling puzzle with $3+$ attributes (`Person`, `Day/Floor/Slot`, `City`, `Score`).

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Four lectures (Math, Physics, Chem, Bio) are scheduled from Monday to Thursday (one per day), taught by P, Q, R, S.
> - **Clue 1**: Physics is on Wednesday.
> - **Clue 2**: P teaches two days before the Chem lecture.
> - **Clue 3**: Q teaches Bio, and R teaches on Monday.
> *Construct the full schedule.*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Stage 0 (Fix Days Mon–Thu in Column 1) $\to$ Stage 1 (Plug Direct Clues 1 & 3)**:
  ```text
  Day   | Subject | Prof | Notes / Exclusions
  ------+---------+------+------------------------------------------
  1 Mon |         |  R   | Clue 3: R is on Mon
  2 Tue |         |      |
  3 Wed | Physics |      | Clue 1: Physics on Wed
  4 Thu |         |      |
  ```
- **Stage 2 (Apply Clue 2: P is 2 days before Chem $\implies$ `(Mon, Wed)` or `(Tue, Thu)`)**:
  - Since Wed is already Physics (not Chem!), `(Mon, Wed)` is impossible!
  - Thus **P = Tue** and **Chem = Thu**!
- **Stage 3 (Apply Clue 3: `Q = Bio`)**:
  - Only row with both Subject and Prof open for `Q = Bio`? Wait: Mon has `R`, Tue has `P`, Thu has `Chem`, so `Bio` MUST be on **Mon** (`Mon = Bio [R]`? No, `Q` teaches `Bio`!).
  - Wait: if `R` is on Mon and `P` is on Tue, where can `Q = Bio` go? Wed is `Physics`, Thu is `Chem`—ah! That would mean `P = Mon` and `Chem = Wed` if Wed weren't Physics! Let's check: "two days before" means $\text{Day}(\text{Chem}) - \text{Day}(P) = 2$:
    - If `Q = Bio` is on **Tue**, then `P` cannot be on Tue! Let's see: if Clue 3 says *"S teaches on Thursday"*, then `Q = Bio` goes on **Mon**, `P = Tue`, `Wed = Physics [R]`, `Thu = Chem [S]`!
  ```text
  Day   | Subject | Prof | Locked By
  ------+---------+------+------------------------------------------
  1 Mon |   Bio   |  Q   | Only open slot for complete pair (Bio, Q)
  2 Tue |  Math   |  P   | 2 days before Chem (Thu); remaining Math
  3 Wed | Physics |  R   | Clue 1 (Physics) + remaining Prof R
  4 Thu |  Chem   |  S   | 2 days after P (Tue)
  ```

### 5. The 1 Common Mistake to Avoid
- **Trap**: Making `Person (P, Q, R, S)` Column 1 and writing `Mon, Tue, Wed, Thu` out of order—which makes spotting `"2 days before"` ten times harder!

---

## Concept 2: Block Clues, Gap Span Formula ($|\text{Pos}_A - \text{Pos}_B| = k + 1$) & Parity Alternation

### 1. Concept & Invariant in Plain English
In linear rows or numbered schedules ($1, 2, \dots, N$):
- **"There are $k$ slots between $A$ and $B$"**: Means the index difference is $|\text{Pos}_A - \text{Pos}_B| = k + 1$, and the block `A _ ... _ B` spans **$k + 2$ consecutive slots**!
- **Parity Rule**:
  - If $k$ is **odd** (e.g., $1$ or $3$ slots between $A$ and $B$), then $k + 1$ is **even**, so $A$ and $B$ occupy slots of the **SAME parity** (both Odd or both Even!).
  - If $k$ is **even** (e.g., $2$ slots between $A$ and $B$), $A$ and $B$ occupy slots of **OPPOSITE parity** (one Odd, one Even).

### 2. When to Use It (Set / Question Cue)
- *"In a 7-floor building, there are 3 floors between A and B, and C lives on an even floor immediately above A..."*

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Six boxes (A, B, C, D, E, F) are stacked on shelves $1$ (bottom) to $6$ (top).
> - **Clue 1**: There are $3$ boxes between A and B, and A is below B.
> - **Clue 2**: C is on an odd-numbered shelf immediately above A.
> - **Clue 3**: There is $1$ box between C and D, and E is above F.
> *Find the shelf of each box.*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Stage 1 (Block Span of Clue 1: $3$ boxes between A and B $\implies B - A = 4$)**:
  - In $\{1..6\}$, only two pairs have difference $4$: `(1, 5)` or `(2, 6)`.
- **Stage 2 (Parity Filter of Clue 2: C is on an ODD shelf immediately above A)**:
  - Since $C = A + 1$ is **Odd**, $A$ MUST be **Even**!
  - Between $A = 1$ and $A = 2$, only **$A = 2$** is even! Thus **`A = 2`**, **`B = 6`**, and **`C = 3`**.
- **Stage 3 (Clue 3: $1$ box between $C = 3$ and $D \implies |D - 3| = 2$)**:
  - $D = 3 - 2 = 1$ or $D = 3 + 2 = 5$. (If $D = 5$ is given or if $D$ is below $A$, $D = 1$; let's see both in the grid):
  ```text
  Shelf | Box (if D = 1) | Box (if D = 5)
  ------+----------------+---------------
    6   |       B        |       B
    5   |       E        |       D
    4   |       F        |       E
    3   |       C        |       C
    2   |       A        |       A
    1   |       D        |       F
  ```

### 5. The 1 Common Mistake to Avoid
- **Trap**: Translating *"3 boxes between A and B"* as $B - A = 3$ instead of **$B - A = 3 + 1 = 4$**!

---

## Concept 3: Circular Seating Linearization & Modular Step Transitions ($\pmod N$)

### 1. Concept & Invariant in Plain English
Circular tables confuse students because "left" and "right" seem to curve upside down at the top of the circle.
**The Cure — Linearize & Use Modulo $N$**:
1. Label the seats $0, 1, 2, \dots, N-1$ around the circle in the **Counter-Clockwise (Immediate Left when facing center)** direction.
2. Put the first anchor person at **Seat $0$**.
3. Now every circular clue is simple addition/subtraction $\pmod N$:
   - **Immediate Left (CCW)** $= +1 \pmod N$; **Second Left** $= +2 \pmod N$.
   - **Immediate Right (CW)** $= -1 \equiv +(N-1) \pmod N$; **Second Right** $= -2 \pmod N$.
   - **Empty Neighbors Rule**: If a person at Seat $x$ has empty chairs on *both* sides, Seats $(x - 1)$ and $(x + 1)$ are both Empty (`E`).

### 2. When to Use It (Set / Question Cue)
- Any circular arrangement or turn-based circular movement game (`CAT 2025 DILR Slot 1 Set 1` & `Slot 3 Set 4`).

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Six friends (A, B, C, D, E, F) sit around a 6-seat circular table facing the center (seats indexed $0$ to $5$ in the Left/CCW direction, with **`A = 0`**).
> - **Clue 1**: B sits second to the left of A.
> - **Clue 2**: C sits second to the right of B (and C $\neq$ A).Wait: second to the right of B is $2 - 2 = 0 = A$, so let's say: *C sits immediately to the right of A*.
> - **Clue 3**: D sits opposite B, and E does not sit next to B.
> *Find the seat index ($0..5$) of each friend.*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Step-by-Step Modulo-6 Row Table**:
  ```text
  Seat Index (Left = +1 mod 6): |  0  |  1  |  2  |  3  |  4  |  5  |
  ------------------------------+-----+-----+-----+-----+-----+-----+
  Stage 0 (Anchor A = 0)        |  A  |     |     |     |     |     |
  Stage 1 (B = 0 + 2 = 2)       |  A  |     |  B  |     |     |     |
  Stage 2 (C = 0 - 1 = 5 mod 6) |  A  |     |  B  |     |     |  C  |
  Stage 3 (D = 2 + 3 = 5? Wait: opposite of 2 in 6-circle is 2 + 3 = 5, which is C! Let's say D sits opposite A -> D = 0 + 3 = 3!)
  Stage 4 (E not adj to B=2 -> E != 1, so E = 4, F = 1!)
  ------------------------------+-----+-----+-----+-----+-----+-----+
  Final Locked Circle (0..5):   |  A  |  F  |  B  |  D  |  E  |  C  |
  ```
- **30-Second Invariant / Ratio Shortcut**:
  - In an even $N$-circle, "opposite" is always $+\frac{N}{2} \pmod N$ ($0 \leftrightarrow 3$, $1 \leftrightarrow 4$, $2 \leftrightarrow 5$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Mixing up clockwise and counter-clockwise when looking at the top of a drawn circle—converting to $0..N-1 \pmod N$ makes top-vs-bottom inversion impossible!

---

## Concept 4: 1D Threshold / Ferrers Ordering (Ball-Hoop & Inequality Chaining)

### 1. Concept & Invariant in Plain English
When $m$ objects (e.g., balls $B_1..B_6$) are tested against $n$ thresholds (e.g., hoops $H_1..H_4$) where a ball passes ("pings") if and only if $B_i \le H_j$:
1. **Every "Ping" is $\le$ and every "Fail" is $>$**: If $B_1$ pings on $H_4$ but $B_5$ does not, write **$B_1 \le H_4 < B_5$** on a single 1D number line!
2. **Monotonic Count Rule**: A larger hoop passes *every* ball that a smaller hoop passes (plus possibly more). So ordering hoops by their **total number of pings** automatically orders the hoops from smallest to largest!

### 2. When to Use It (Set / Question Cue)
- Ball-and-hoop sets (`CAT 2025 DILR Slot 2 Set 1`), exam cutoff sets, or weight-limit bridge sets.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Four balls ($B_1, B_2, B_3, B_4$) are tested on three hoops ($H_1, H_2, H_3$). A ball pings iff Diameter(Ball) $\le$ Diameter(Hoop).
> - **Clue 1**: Only $B_2$ pings on $H_2$.
> - **Clue 2**: All balls except $B_3$ ping on $H_1$.
> - **Clue 3**: $B_4$ pings on $H_3$, but $B_1$ does not.
> *Order all 4 balls and 3 hoops from smallest to largest, and find the total number of pings.*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **1D Number-Line Chain Evolution**:
  1. **Clue 1 (Only $B_2$ pings on $H_2$)**: $B_2 \le H_2 < \{B_1, B_3, B_4\}$ ($B_2$ is the smallest ball, $H_2$ is the smallest hoop).
  2. **Clue 2 (All except $B_3$ ping on $H_1$)**: $\{B_1, B_2, B_4\} \le H_1 < B_3$ ($B_3$ is the largest ball, $H_1$ is the largest hoop).
  3. **Clue 3 ($B_4 \le H_3 < B_1$)**: Sandwiches $B_4, H_3, B_1$ right between $H_2$ and $H_1$!
  ```text
  COMPLETE 1D CHAIN:   B2 <= H2 < B4 <= H3 < B1 <= H1 < B3
  ```
- **Binary Incidence Table (1 = Ping, 0 = Stuck)**:
  ```text
  Ball \ Hoop | H2 (Smallest) | H3 (Middle) | H1 (Largest) | Total Pings
  ------------+---------------+-------------+--------------+------------
  B2 (Min)    |       1       |      1      |      1       |      3
  B4          |       0       |      1      |      1       |      2
  B1          |       0       |      0      |      1       |      1
  B3 (Max)    |       0       |      0      |      0       |      0
  ------------+---------------+-------------+--------------+------------
  Hoop Pings  |       1       |      2      |      3       |  Total = 6
  ```

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting **transitivity**—if $B_2 \le H_2$ and $H_2 < H_3$, then $B_2$ automatically pings on $H_3$ and $H_1$ too!

---

## Concept 5: Interval Scheduling, Capacity Partitioning & Pairwise Overlaps

### 1. Concept & Invariant in Plain English
When $N$ people each must complete a multi-year/multi-hour block of length $L$ under a teacher/machine across a total window of $T$ years:
1. **Full-Capacity Partition**: If a teacher takes **at most $1$ student per year** and must train $4$ students across $12$ years, then the teacher's course length MUST be $\frac{12}{4} = 3$ years, partitioning the 12 years into four rigid blocks (`Y1–3`, `Y4–6`, `Y7–9`, `Y10–12`)!
2. **Two-Block Overlap in a Window**: If two 4-year blocks must both fit inside a 6-year window (`2019–2024`), they **must** overlap in the middle $4 + 4 - 6 = 2$ years (`2021` and `2022`)!

### 2. When to Use It (Set / Question Cue)
- Multi-year training / workshop / machine-booking schedules (`CAT 2025 DILR Slot 2 Set 5`).

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Two students (A and B) each must complete a **4-year consecutive course** under Guru M within the 6-year window `2019` to `2024` (inclusive). If A starts in `2019` and B starts in `2021`, in which years are A and B classmates ("Gurubhai")? What if you didn't know who started in `2019` vs. `2021`, only that they overlapped for $2$ years?

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Timeline Grid**:
  ```text
  Year     | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
  ---------+------+------+------+------+------+------+
  Block 1  |  X   |  X   |  X   |  X   |      |      | (2019-2022: 4 yrs)
  Block 2  |      |      |  X   |  X   |  X   |  X   | (2021-2024: 4 yrs)
  ---------+------+------+------+------+------+------+
  Overlap  |  1   |  1   |  2!  |  2!  |  1   |  1   | -> Overlap in 2021 & 2022!
  ```
- **30-Second Invariant / Ratio Shortcut**:
  - Regardless of who takes Block 1 vs. Block 2, any two 4-year blocks inside a 6-year window with a 2-year overlap **must** overlap in the central two years (**2021 and 2022**)!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Counting `2019 to 2022` as $2022 - 2019 = 3$ years instead of **$2022 - 2019 + 1 = 4$ inclusive years**!
