# DILR 05 Concept & Grid-Evolution Examples: Venn Diagrams & 3-Set / 4-Set Maxima-Minima Optimization

> **Companion Reference**: [`../topic_summaries/dilr/05_venn_diagrams_and_4set_maxima_minima.md`](../topic_summaries/dilr/05_venn_diagrams_and_4set_maxima_minima.md) | [`DILR_Archetype_Templates.md`](../high_recall/cheat_sheets/DILR_Archetype_Templates.md)

---

## Concept 1: 3-Set Venn Anatomy & Natural-Language Region Translation

### 1. Concept & Invariant in Plain English
A 3-set Venn diagram (Sets $A, B, C$) has **$8$ disjoint elementary regions** grouped into 4 layers:
- **Layer $E_1$ (Exactly 1 set)**: $a$ (Only A), $b$ (Only B), $c$ (Only C).
- **Layer $E_2$ (Exactly 2 sets)**: $d$ (A & B only), $e$ (B & C only), $f$ (A & C only).
- **Layer $E_3$ (All 3 sets)**: $g$ ($A \cap B \cap C$).
- **Layer $E_0$ (None)**: $n$ (Outside all 3 circles).

**The #1 Wording Distinction**:
- *"People who like **A and B**"* $= d + g$ (includes the center $g$!).
- *"People who like **only A and B**"* (or *"A and B but not C"*) $= d$ alone!

### 2. When to Use It (Set / Question Cue)
- Any 3-category survey with overlapping memberships.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> In a survey of $100$ people on Tea ($T = 50$), Coffee ($C = 45$), and Milk ($M = 40$):
> - $10$ people drink all three ($g = 10$).
> - $20$ people drink both Tea and Coffee; $18$ drink both Coffee and Milk; $15$ drink both Tea and Milk.
> *Find the number of people in every single region and how many drink None ($n$).*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Stage 1 (Fill Center $g = 10$ First) $\to$ Stage 2 (Subtract $g$ from Pairwise Overlaps)**:
  ```text
  Region                       | Formula / Peeling from Center Out | Value
  -----------------------------+-----------------------------------+------
  g (All three: T & C & M)     | Given anchor                      |  10
  d (T & C only)               | (T & C) - g = 20 - 10             |  10
  e (C & M only)               | (C & M) - g = 18 - 10             |   8
  f (T & M only)               | (T & M) - g = 15 - 10             |   5
  a (Only T)                   | 50 - (d + f + g) = 50 - (10+5+10) |  25
  b (Only C)                   | 45 - (d + e + g) = 45 - (10+8+10) |  17
  c (Only M)                   | 40 - (e + f + g) = 40 - (8+5+10)  |  17
  -----------------------------+-----------------------------------+------
  Total Inside (a+b+c+d+e+f+g) | 25 + 17 + 17 + 10 + 8 + 5 + 10    |  92
  n (Outside / None)           | 100 - 92                          |   8
  ```
- **30-Second Invariant / Ratio Shortcut**:
  - Inclusion-Exclusion: $|T \cup C \cup M| = (50 + 45 + 40) - (20 + 18 + 15) + 10 = 135 - 53 + 10 = 92 \implies \text{None} = 100 - 92 = \mathbf{8}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Writing `20` directly into the `T & C only` lens ($d$) without subtracting the center `10` ($g$) first!

---

## Concept 2: 4-Set Karnaugh $4 \times 4$ Grid ($16$ Regions — Why 4 Circles Fail)

### 1. Concept & Invariant in Plain English
If you draw $4$ overlapping circles on paper, two opposite circles miss a dedicated pairwise-only region ($14$ regions instead of $2^4 = 16$!).
Instead, draw a **$4 \times 4$ Karnaugh Table**:
- **Rows**: The 4 combinations of Sets $A$ and $B$ (`A & B`, `A only`, `B only`, `Neither A nor B`).
- **Columns**: The 4 combinations of Sets $C$ and $D$ (`C & D`, `C only`, `D only`, `Neither C nor D`).
Every single one of the $16$ regions has its own clean box, and you can read off how many sets a box belongs to by adding the row count + column count!

### 2. When to Use It (Set / Question Cue)
- Any 4-category Venn puzzle (e.g., 4 newspapers, 4 sports, 4 electives).

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> A club offers 4 sports (A, B, C, D). Every member plays at least 1 sport (`None = 0`).
> - **Clue 1**: $10$ play all 4 sports.
> - **Clue 2**: Everyone who plays A also plays B (so `A & not-B` row is all $0$s!).
> - **Clue 3**: No one plays both C and D without playing A (so `C & D` column is $0$ outside `A & B`!).
> *Show how the $4 \times 4$ grid knocks out 7 regions in 10 seconds.*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Karnaugh $4 \times 4$ Grid Evolution**:
  ```text
  Rows \ Cols  |  C & D (2)  | C only (1) | D only (1) | Neither C,D (0)
  -------------+-------------+------------+------------+----------------
  A & B (2)    |  10 (All 4) |  ABC only  |  ABD only  |   AB only
  A only (1)   |   0 [Cl.2]  |   0 [Cl.2] |   0 [Cl.2] |    0 [Cl.2]
  B only (1)   |   0 [Cl.3]  |  BC only   |  BD only   |    B only
  Neither A,B  |   0 [Cl.3]  |   C only   |   D only   |    0 [None=0]
  ```
- **30-Second Invariant / Ratio Shortcut**:
  - Notice that Clue 2 (*"Everyone in A is in B"*) zeroes out an **entire row of 4 cells** in one stroke!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Trying to draw 4 intersecting circles and forgetting the `A & C only` or `B & D only` diagonal intersections!

---

## Concept 3: The Two Master Layer Equations & The Golden Surplus Identity

### 1. Concept & Invariant in Plain English
When a Venn problem deals with **how many sets** people belong to (`Exactly 1`, `Exactly 2`, `Exactly 3`, `Exactly 4`), you don't even need individual regions! Just write the two accounting equations:
1. **Headcount Equation**: $E_1 + E_2 + E_3 + E_4 = N$ (where $N = U - E_0$ is total active people).
2. **Ticket Sum Equation**: $E_1 + 2E_2 + 3E_3 + 4E_4 = S$ (where $S = |A| + |B| + |C| + |D|$ is the sum of the circle totals).
**Subtract Equation (1) from Equation (2)** to eliminate $E_1$ immediately:
$$\mathbf{E_2 + 2E_3 + 3E_4 = S - N \quad (\text{The Golden Surplus Identity})}$$

### 2. When to Use It (Set / Question Cue)
- Whenever set sizes $|A|, |B|, |C|, |D|$ and total people $N$ are given alongside clues about *"exactly 2 sets"* or *"at least 3 sets"*.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Out of $100$ students, every student joined at least one of 4 clubs: $A (60)$, $B (55)$, $C (50)$, and $D (45)$. If $15$ students joined all 4 clubs and $25$ students joined exactly 3 clubs, how many students joined **exactly 2** clubs ($E_2$) and **exactly 1** club ($E_1$)?

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Layer Accounting Table**:
  ```text
  Layer | Meaning          | Count      | Tickets (= k * E_k)
  ------+------------------+------------+--------------------
   E_1  | Exactly 1 club   | [45] (St.2)| 1 * 45 = 45
   E_2  | Exactly 2 clubs  | [15] (St.1)| 2 * 15 = 30
   E_3  | Exactly 3 clubs  |  25 (Given)| 3 * 25 = 75
   E_4  | All 4 clubs      |  15 (Given)| 4 * 15 = 60
  ------+------------------+------------+--------------------
  Total | N = 100 students | 100        | S = 60+55+50+45 = 210
  ```
  1. **Stage 1 (Surplus Identity)**: $E_2 + 2E_3 + 3E_4 = 210 - 100 = 110$.
     Plug $E_3 = 25, E_4 = 15$: $E_2 + 2(25) + 3(15) = 110 \implies E_2 + 95 = 110 \implies \mathbf{E_2 = 15}$.
  2. **Stage 2 (Headcount)**: $E_1 = 100 - (15 + 25 + 15) = \mathbf{45}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting to subtract $E_0$ (people in **0 sets**) from $U$ before computing $N = U - E_0$.

---

## Concept 4: Surplus Maxima & Minima Optimization

### 1. Concept & Invariant in Plain English
Given fixed active people $N = U - E_0$ and fixed ticket sum $S$, the Surplus $K = S - N$ is a fixed budget to be spent across:
$$1 \cdot E_2 + 2 \cdot E_3 + 3 \cdot E_4 = K$$
- **To MAXIMIZE $E_4$ (or $E_3$ in a 3-set diagram)**: Put all the surplus budget into the highest bucket ($3E_4 \le K \implies E_4 \le \lfloor K/3 \rfloor$, also capped by the smallest set size!).
- **To MINIMIZE $E_3$ (in a 3-set diagram where $E_2 + 2E_3 = K$)**: Pack as many people as possible into $E_2$ (by making $E_1 = 0$, so $E_2 + E_3 = N$). Then $E_3 = K - N = S - 2N$ (or $0$ if negative)!

### 2. When to Use It (Set / Question Cue)
- *"What is the maximum / minimum possible number of people who like all 3 (or at least 2) products?"*

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> In a survey of $100$ people where everyone likes at least one of A ($75$), B ($65$), and C ($50$), find the **maximum** and **minimum** possible number of people who like **all three** ($E_3$).

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Surplus Equation**: $N = 100$, $S = 75 + 65 + 50 = 190 \implies E_2 + 2E_3 = 190 - 100 = 90$.
  ```text
  Goal         | Strategy                      | E_1 | E_2 | E_3 | Check: E_2 + 2*E_3 = 90
  -------------+-------------------------------+-----+-----+-----+------------------------
  Maximize E_3 | Minimize E_2 = 0              |  55 |  0  |  45 | 0 + 2(45) = 90 (<=50 OK!)
  Minimize E_3 | Maximize E_2 (set E_1 = 0)    |   0 | 100 |   0 | Wait: if E_3=0, E_2=90, E_1=10!
  ```
  - **Maximum $E_3$**: $\min(\lfloor 90/2 \rfloor, 50) = \mathbf{45}$ (with $E_2 = 0, E_1 = 55$).
  - **Minimum $E_3$**: $\max(0,\; 190 - 200) = \mathbf{0}$ (with $E_2 = 90, E_1 = 10$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Saying $\max E_3 = 50$ (the smallest circle size) without checking that $2E_3$ cannot exceed the surplus $90$ ($\implies E_3 \le 45$ when $E_0 = 0$ is fixed!).

---

## Concept 5: Multi-Author Hypergraph Degree-Sum Conservation ($\sum \text{Credits}_k = k \cdot N_k$)

### 1. Concept & Invariant in Plain English
When a group of authors collaborate on papers of size $k$ ($1$-author, $2$-author, $3$-author, $4$-author papers), every single $k$-author paper gives **$1$ credit to each of its $k$ co-authors**.
Therefore, if you add up the "$k$-author paper count" across all authors in the table, that sum MUST be a multiple of $k$:
$$\sum_{\text{all authors}} (\text{Author's count of } k\text{-author papers}) = k \times (\text{Total number of } k\text{-author papers } N_k)$$

### 2. When to Use It (Set / Question Cue)
- Co-authored papers, committee memberships, or team project participation sets (`CAT 2025 DILR Slot 2 Set 3`).

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Four researchers (A, B, C, D) co-authored several **3-author papers** (each written by 3 of the 4 researchers). Every researcher co-authored at least $1$ three-author paper, and both C and D co-authored **more** three-author papers than B. If there were only $2$ three-author papers in total ($N_3 = 2$), find how many 3-author papers each researcher co-authored and which two triples wrote them.

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Degree-Sum Deduction Table**:
  1. Total 3-author credits across A, B, C, D $= 3 \times N_3 = 3 \times 2 = \mathbf{6\text{ credits}}$.
  2. Each of A, B, C, D has $\ge 1$ credit, and $C > B \ge 1, D > B \ge 1 \implies C \ge 2$ and $D \ge 2$.
  3. Since $1 + 1 + 2 + 2 = 6$, the credits MUST be **`A = 1, B = 1, C = 2, D = 2`**!
  ```text
  Paper # | Co-Authors (Must include C & D in both!) | A | B | C | D
  --------+------------------------------------------+---+---+---+---
  Paper 1 | {A, C, D}                                | 1 | 0 | 1 | 1
  Paper 2 | {B, C, D}                                | 0 | 1 | 1 | 1
  --------+------------------------------------------+---+---+---+---
  Credits | Total = 6 (= 3 * 2 papers)               | 1 | 1 | 2 | 2
  ```

### 5. The 1 Common Mistake to Avoid
- **Trap**: Thinking that the sum of the "3-author papers" column across A, B, C, D equals the number of papers ($2$) instead of **$3 \times 2 = 6$**!
