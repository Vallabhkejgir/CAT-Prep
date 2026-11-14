# DILR 01 Concept & Grid-Evolution Examples: Set Selection, 4-Minute Scanning & Mathematical Invariants

> **Companion Reference**: [`../topic_summaries/dilr/01_set_selection_and_5min_scanning_framework.md`](../topic_summaries/dilr/01_set_selection_and_5min_scanning_framework.md) | [`DILR_Archetype_Templates.md`](../high_recall/cheat_sheets/DILR_Archetype_Templates.md)

---

## Concept 1: Bucket A / B / C Triage & The 60-Second Green-Flag / Red-Flag Filter

### 1. Concept & Invariant in Plain English
In CAT DILR, solving just **2 out of 5 sets (9–10 questions)** with high accuracy places you around the **99th percentile**. The biggest reason students score poorly is not lack of logic—it is spending 18 minutes on a "Bucket C" monster set first!
Before solving anything, spend **Minutes 00–04** scanning all 5 sets (45 seconds per set) and classifying each set into:
- **Bucket A (Sitter — Solve First)**: Familiar grid/Venn/tournament/table structure, small finite numbers, and $\ge 2$ direct anchor clues.
- **Bucket B (Doable — Solve Second)**: Familiar structure but requires 2 parallel cases (`Case 1 | Case 2`).
- **Bucket C (Trap — Skip Initially)**: Custom multi-round game rules, 5+ loosely coupled attributes, or every MCQ having *"Cannot be determined"* as Option D.

### 2. When to Use It (Set / Question Cue)
- At Minute `00:00` of every DILR sectional or mock test.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> You open a DILR paper and see three sets:
> - **Set X**: 6 people sit in a circle facing either inward or outward, each likes a different fruit and visits a different city; all 6 clues are conditional (*"If A faces inward, the person liking Mango sits opposite B"*), and all 4 MCQs have *"Cannot be determined"*.
> - **Set Y**: A $4 \times 3$ table of calls made between two telecom operators (Xitel with 2 users, Yocel with 4 users) with row/column sums given and 3 zero-call clues.
> - **Set Z**: 5 people pick 3 balls each from $\{1..15\}$; P picks primes summing to $10$, Q picks consecutive numbers summing to $42$, R picks multiples of $4$.
> *Rank Sets X, Y, Z into Buckets A/B/C and pick your opening order.*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Step-by-Step Triage Table**:
  ```text
  Set | Archetype          | Anchors?                    | Option D "CBD"? | Bucket & Order
  ----+--------------------+-----------------------------+-----------------+----------------
   X  | Circular + 2 Attrs | 0 anchors (all conditional) | YES (All 4 Qs)  | Bucket C (SKIP)
   Y  | 2-Group Flow Table | 2-user Xitel + 3 zero clues | NO (3 TITAs)    | Bucket A (#2)
   Z  | Unique Sum Partition| P={2,3,5}, Q={13,14,15}     | NO              | Bucket A (#1)
  ```
- **30-Second Invariant / Ratio Shortcut**:
  - Spot that in Set Z, P ($2+3+5=10$), Q ($13+14+15=42$), and R ($4,8,12$) lock **9 out of 15 balls in 15 seconds** during the scan itself! Start with **Set Z $\to$ Set Y**, and leave **Set X** untouched.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Starting Set #1 on page 1 at Minute `00:00` without scanning Sets 2–5 first, and discovering at Minute 38 that Set 4 and Set 5 were 6-minute sitters!

---

## Concept 2: The 3-Zone Scratchpad Architecture & Parallel Column Splitting (Never Erase!)

### 1. Concept & Invariant in Plain English
When a clue narrows a person or value down to **2 possibilities** (e.g., $A = 10$ or $A = 30$), beginners guess $A = 10$, write it into their single table, hit a contradiction 4 minutes later, and then furiously erase or scribble over their table—destroying their base clues in the process!
Instead, use **Parallel Column Splitting**: draw `Case 1` and `Case 2` side by side in the same table. When one case hits a contradiction, simply draw a single line through that column and keep rolling with the surviving column!

### 2. When to Use It (Set / Question Cue)
- Whenever your anchor clue leaves exactly 2 (or 3) valid placements.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Four tasks (P, Q, R, S) are scheduled on Days 1, 2, 3, 4 (one per day).
> - **Clue 1**: Task P is on Day 1 or Day 3.
> - **Clue 2**: Task Q is immediately after Task P.
> - **Clue 3**: Task R is on an earlier day than Task S, and Task R is NOT on Day 1.
> *Find the schedule.*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Stage 0 $\to$ Stage 1 (Open Parallel Columns for Clue 1 & Clue 2)**:
  ```text
  Day | Case 1 (P = Day 1) | Case 2 (P = Day 3)
  ----+--------------------+-------------------
   1  |         P          |                   
   2  |         Q          |                   
   3  |                    |         P         
   4  |                    |         Q         
  ```
- **Stage 2 (Apply Clue 3: $R < S$ and $R \neq \text{Day } 1$)**:
  - In **Case 1**, remaining days for $\{R, S\}$ are Day 3 and Day 4. Since $R < S$, **Day 3 = R** and **Day 4 = S** (and $R$ is on Day $3 \neq \text{Day } 1$ — Valid!).
  - In **Case 2**, remaining days for $\{R, S\}$ are Day 1 and Day 2. Since $R < S$, $R$ would have to be on **Day 1**, violating $R \neq \text{Day } 1$! Cross out Case 2!
  ```text
  Day | Case 1 (LOCKED!)   | Case 2 (ELIMINATED)
  ----+--------------------+--------------------
   1  |         P          |     R (Violates!)  
   2  |         Q          |         S          
   3  |         R          |         P          
   4  |         S          |         Q          
  ```
- **30-Second Invariant / Ratio Shortcut**:
  - Since $R < S$ and $R \neq \text{Day } 1$, both $R$ and $S$ must sit in $\{2, 3, 4\}$, which leaves **Day 1** only for $P$ (since $Q$ is after $P$)!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Overwriting or erasing cells inside a single column instead of adding a parallel `Case 2` column right next to `Case 1`.

---

## Concept 3: Unique Partition Sums from $\{1..9\}$ & Extreme-Value Squeeze

### 1. Concept & Invariant in Plain English
In sets where distinct integers from a small set like $\{1, 2, 3, 4, 5, 6, 7, 8, 9\}$ are grouped into sums, **extreme sums have only 1 possible combination**:
- Smallest sum of 3 distinct numbers from $\{1..9\}$: $1 + 2 + 3 = \mathbf{6}$; next smallest: $1 + 2 + 4 = \mathbf{7}$.
- Largest sum of 3 distinct numbers from $\{1..9\}$: $7 + 8 + 9 = \mathbf{24}$; second largest: $6 + 8 + 9 = \mathbf{23}$.
Similarly, if $4$ variables each capped at $\le 10$ sum to $38$, then even if three of them take their absolute maximum ($10 + 10 + 10 = 30$), the fourth variable is **squeezed** to be at least $38 - 30 = 8$!

### 2. When to Use It (Set / Question Cue)
- *"Each person picked 3 distinct cards from 1 to 9; A's cards sum to 7 and B's cards sum to 23..."*

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Nine tokens numbered $1$ to $9$ are distributed among A, B, and C (3 tokens each).
> - **Clue 1**: The sum of A's tokens is $7$.
> - **Clue 2**: The sum of B's tokens is $23$.
> *Find the exact tokens held by A, B, and C.*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Stage 1 (Lock Unique Extreme Partitions)**:
  - **A (3 distinct tokens from $\{1..9\}$ summing to $7$)**: Minimum possible is $1+2+3=6$, so $7$ MUST be $\mathbf{\{1, 2, 4\}}$.
  - **B (3 distinct tokens from $\{1..9\}$ summing to $23$)**: Maximum possible is $7+8+9=24$, so $23$ MUST be $\mathbf{\{6, 8, 9\}}$.
- **Stage 2 (Remaining Universe for C)**:
  - Cross out $\{1, 2, 4, 6, 8, 9\}$ from $\{1..9\}$ $\implies$ **C gets $\mathbf{\{3, 5, 7\}}$** (sum $= 15$).
- **30-Second Invariant / Ratio Shortcut**:
  - Total sum of $1..9$ is $\frac{9 \times 10}{2} = 45$. So C's sum is $45 - (7 + 23) = 15$ before even listing individual tokens!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Treating $7$ or $23$ as "one of many possibilities" instead of recognizing immediately that $\{1,2,4\}$ and $\{6,8,9\}$ are **100% unique**.

---

## Concept 4: Parity & Divisibility Invariants (Integer Mean & Modulo Conservation)

### 1. Concept & Invariant in Plain English
Whenever a DILR prompt says *"The average (or weighted average) of $A, B,$ and $C$ is an **integer**"*, translate it immediately into a **divisibility / remainder rule**:
- $\frac{A + B}{2} \in \mathbb{Z} \iff A$ and $B$ have the **same parity** (both Odd or both Even).
- $\frac{A + B + C}{3} \in \mathbb{Z} \iff (A + B + C) \equiv 0 \pmod 3$.
- $\frac{2A + B + C}{4} \in \mathbb{Z} \iff 2A + B + C \equiv 0 \pmod 4$.

### 2. When to Use It (Set / Question Cue)
- *"The index of each group is the average of its 3 members, and all group indices are integers..."*

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Six numbers $\{10, 20, 31, 40, 52, 63\}$ are paired into 3 groups of 2 numbers each (Group X, Group Y, Group Z) such that the average of the 2 numbers in each group is an **integer**, and the average of Group X is a multiple of $25$. Find the pairs.

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Stage 1 (Parity Filter)**:
  - For $\frac{a + b}{2}$ to be an integer, Odd must pair with Odd, and Even must pair with Even!
  - Odd numbers in the list: only $\{31, 63\} \implies$ **One group MUST be $\{31, 63\}$** (average $= \frac{94}{2} = 47$).
- **Stage 2 (Multiple of 25 Filter on Even Numbers $\{10, 20, 40, 52\}$)**:
  - For the average $\frac{a+b}{2}$ to be a multiple of $25$, the sum $a + b$ must be a multiple of $50$.
  - Among $\{10, 20, 40, 52\}$, only $10 + 40 = 50$ is a multiple of $50 \implies$ **Group X $= \{10, 40\}$** (average $= 25$), leaving **$\{20, 52\}$** (average $= 36$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Testing all $\frac{6!}{2^3 \cdot 3!} = 15$ pairings by brute force instead of separating Odd vs. Even first!

---

## Concept 5: Question-Stem Reverse Engineering & The 6-Minute Hard Bail-Out Gate

### 1. Concept & Invariant in Plain English
Before spending 5 minutes trying to force every cell of a DILR grid to be unique, **read the 4 question stems**:
- If Question 3 asks: *"If C is assigned to Mumbai, then which city is D assigned to?"*, that proves **C and D are NOT uniquely fixed by the main prompt clues**! Stop trying to solve C and D in the base grid—leave `{C, D}` as a rotating pair `Mumbai / Pune` and go straight to the questions!

### 2. When to Use It (Set / Question Cue)
- Whenever your grid is 80% full and 2 or 3 cells seem to swap symmetrically with no clue left to break the tie.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> You are solving a 4-person (A, B, C, D) city-assignment set. After using all clues, you have locked `A = Delhi`, `B = Chennai`, and `{C, D} = {Mumbai, Kolkata}` (either order works). You panic thinking you missed a clue. Then you glance at Q2: *"If C is from Mumbai, who is from Kolkata?"*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Grid Representation**:
  ```text
  Person | City
  -------+-------------------
    A    | Delhi (Locked)
    B    | Chennai (Locked)
    C    | Mumbai / Kolkata  <-- Leave as a 2-way slash! Do NOT keep hunting!
    D    | Kolkata / Mumbai
  ```
- **30-Second Invariant / Ratio Shortcut**:
  - Conditional question stems (`"If..."`) and `"Cannot be determined"` options are **meta-clues** telling you which cells have 2 degrees of freedom in the base grid.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Writing the temporary condition from Question 2 (*"If C is from Mumbai"*) permanently into your master base table and accidentally using it to answer Question 3!
