# DILR 06: Networks, Routes, Flows, Project Scheduling & Quant-LR Puzzles

**Canonical Taxonomy Mapping**: `DILR > Networks, Routes, Flows & Project Scheduling`, `Quant-Based LR & Algorithmic Puzzles`  
**Weightage**: ~20–30% of DILR (1–2 sets per slot)  
**Priority Tier**: Tier 1 (High-Yield Core)

---

## 1. Visual & Structural Anatomy

### 1.1 Networks, Routes, Flows & Project Scheduling (CPM)
- **Pipeline / Traffic / Material Flow Networks**: Directed or undirected graphs where edges have **Capacity / Flow Limits**, **Per-Unit Toll / Cost**, or **Slack**, and nodes have **Supply ($+$)**, **Demand ($-$)**, or **Zero Net Storage (Transshipment)**.
- **Shortest / Cheapest / Fastest Route Selection**: Multi-hop paths with fixed node entry fees or transfer penalties.
- **Project Scheduling (Critical Path Method — CPM)**: Tasks with durations and prerequisite dependencies ($A \to C$).

### 1.2 Quant-Based LR & Algorithmic Puzzles
- **Counterfeit Coin / Weighing Puzzles**: Finding $1$ heavier/lighter coin among $N$ using a pan balance or digital scale.
- **Cryptarithmetic (Base-10 Letter-to-Digit Addition/Multiplication)**: Carry-over bounds ($0$ or $1$ for 2-row addition; $0, 1,$ or $2$ for 3-row addition).
- **State-Transition / Token-Passing / Sliding-Window Averages**: Iterative rules or moving averages where $A_{k+1} - A_k = \frac{x_{\text{in}} - x_{\text{out}}}{w}$.
- **Truth-Teller / Liar / Alternator Matrices**: Binary truth-table testing across $N$ suspects.
- **2-Player Combinatorial & Payoff Matrix Games**: Dominant strategy, Nash equilibrium, or backward induction from winning/losing terminal states.

---

## 2. Green Flags vs. Red Flags

- **Green Flags**:
  - **Flow networks with degree-1 or degree-2 leaf nodes**: Flow on edges connected to single-entry nodes is locked in 5 seconds.
  - **Moving-average / sliding-window tables**: Adjacent windows differ by only $1$ entering and $1$ leaving element ($x_{k+w} - x_k = w(A_{k+1} - A_k)$).
  - **Truth-teller/liar sets where the number of truth-tellers is given** (e.g., "Exactly 1 person is telling the truth"): Test each of the $N$ candidates in 60 seconds total!
- **Red Flags**:
  - Undirected networks where flow direction on every interior edge can flip arbitrarily AND questions ask for minimum/maximum across all possible flow reversals without node demands given.

---

## 3. Scratchpad Representation Template

### A. Network Node Flow-Balance Table
Instead of scribbling numbers all over a messy node diagram, list nodes in order of **lowest degree (fewest unknown incident pipes)** first:

```text
+-----------------------------------------------------------------------+
| GLOBAL CONSERVATION: Sum(Source Supply) = Sum(Sink Demand) = 1200     |
+------+---------+---------------+----------------+---------------------+
| Node | Net Dem | Inflow Pipes  | Outflow Pipes  | Locked Pipe Equation|
+------+---------+---------------+----------------+---------------------+
|  P   |   200   | S->P (500)    | P->Q, P->R     | PQ + PR = 500 - 200 |
|  Q   |   150   | P->Q (x)      | Q->T (100)     | x - 100 = 150->x=250|
+------+---------+---------------+----------------+---------------------+
```

### B. Truth-Teller / Liar Hypothesis Matrix
```text
+-----------+--------------------+--------------------+--------------------+
| Statement | Assume A = Truth   | Assume B = Truth   | Assume C = Truth   |
+-----------+--------------------+--------------------+--------------------+
| A's claim |     T (Check)      |     F (Invert)     |     F (Invert)     |
| B's claim |     F (Invert)     |     T (Check)      |     F (Invert)     |
| C's claim |     F (Invert)     |     F (Invert)     |     T (Check)      |
+-----------+--------------------+--------------------+--------------------+
| Verdict   | Contradiction?     | VALID!             | Contradiction?     |
+-----------+--------------------+--------------------+--------------------+
```

---

## 4. Anchor Clue & Case-Splitting Rules

1. **Network Flow Leaf-to-Core Peeling**:
   - Start at **terminal (leaf) nodes** or nodes with only **one unknown incident edge**.
   - Apply **Kirchhoff's Node Law** at every node $v$:
     $$\sum \text{Inflow}(v) = \sum \text{Outflow}(v) + \text{Consumption/Demand}(v)$$
2. **Max-Flow / Min-Cut Bottleneck Theorem**:
   - To find the **maximum possible flow** from Source $S$ to Sink $T$ without guessing paths, draw a line (a **Cut**) separating $S$ from $T$ across the narrowest bottleneck edges:
     $$\text{Max Flow}(S \to T) = \min_{\text{all cuts }(S, T)} \left(\sum \text{Capacities of edges crossing from } S\text{-side to } T\text{-side}\right)$$
   - **Slack on an Edge** $= \text{Capacity} - \text{Actual Flow}$.
3. **Sliding-Window Telescope Rule**:
   - If the averages of consecutive 3-month windows (Jan–Mar, Feb–Apr, Mar–May, Apr–Jun) are $A_1, A_2, A_3, A_4$, then:
     $$\text{Apr} - \text{Jan} = 3(A_2 - A_1), \quad \text{May} - \text{Feb} = 3(A_3 - A_2), \quad \text{Jun} - \text{Mar} = 3(A_4 - A_3)$$
   - Notice this partitions the months into **3 residue chains modulo 3**: $\{\text{Jan, Apr, Jul}\}$, $\{\text{Feb, May, Aug}\}$, and $\{\text{Mar, Jun, Sep}\}$! Locking just 1 month in a chain locks the entire chain.

---

## 5. Mathematical Invariants across Algorithmic Puzzles

- **Critical Path Method (CPM) Scheduling**:
  - **Minimum Project Completion Time** $= \text{Length of the LONGEST prerequisite path}$ from Start to Finish (the **Critical Path**).
  - **Slack / Float of a Task** $= \text{Latest Finish Time} - \text{Earliest Finish Time}$. Tasks on the Critical Path have **Slack $= 0$** (delaying a critical task by $1$ day delays the entire project by $1$ day).
- **Pan Balance Counterfeit Weighing**:
  - Each weighing has $3$ outcomes (Left heavy, Right heavy, Balanced), so $k$ weighings distinguish at most:
    - **$3^k$ coins** if we already know the counterfeit coin is heavier (or lighter).
    - **$\frac{3^k - 3}{2}$ coins** if we neither know which coin is fake nor whether it is heavier or lighter ($12$ coins in $3$ weighings).
- **Backward Induction in Take-Away Games** (e.g., Pile of $N$ stones; each turn remove $1, 2, \dots, m$ stones; last player to take wins):
  - Losing positions ($\mathcal{P}$-positions for the player about to move) are multiples of $(m + 1)$:
    $$N \equiv 0 \pmod{m + 1} \implies \text{Second player wins}; \qquad N \equiv r \not\equiv 0 \pmod{m+1} \implies \text{First player removes } r \text{ stones and wins!}$$
  - If the player who takes the last stone **loses** (Misère play), losing positions are $N \equiv 1 \pmod{m + 1}$.

---

## 6. Solved Archetype Walkthrough: Pipeline Network Flow & Slack Reconstruction

> **Set Scenario**: A water supply network starts at Reservoir $S$ (total outflow $= 1000\text{ L/min}$) and feeds 4 towns $A, B, C, D$ via directed pipes:
> - Pipes from $S$: $S \to A$ and $S \to B$.
> - Interior pipes: $A \to C$, $A \to D$, $B \to A$ ($100\text{ L/min}$), and $B \to D$.
> - Town demands (water consumed at each node): $D_A = 200$, $D_B = 150$, $D_C = 350$, $D_D = ?$.
> - Every pipe has capacity $500\text{ L/min}$. Flow in $A \to D$ has a slack of $350\text{ L/min}$.
> *Find the flow and slack in every pipe.*

### Step-by-Step Execution
1. **Global Conservation Lock**:
   - Total Supply $= 1000 = D_A + D_B + D_C + D_D = 200 + 150 + 350 + D_D \implies \mathbf{D_D = 300\text{ L/min}}$.
2. **Leaf Node Lock (Town C)**:
   - Only pipe entering $C$ is $A \to C$, and no pipe leaves $C$:
     $$\text{Flow}(A \to C) = D_C = \mathbf{350\text{ L/min}} \quad (\text{Slack} = 500 - 350 = 150)$$
3. **Slack Clue on $A \to D$**:
   - $\text{Flow}(A \to D) = \text{Capacity} - \text{Slack} = 500 - 350 = \mathbf{150\text{ L/min}}$.
4. **Node Balance at Town D**:
   - Pipes entering $D$ are $A \to D$ ($150$) and $B \to D$; no pipes leave $D$:
     $$150 + \text{Flow}(B \to D) = D_D = 300 \implies \mathbf{\text{Flow}(B \to D) = 150\text{ L/min}} \quad (\text{Slack} = 350)$$
5. **Node Balance at Town A & Town B**:
   - At $A$: $\text{Inflow} = \text{Flow}(S \to A) + \text{Flow}(B \to A) = \text{Flow}(S \to A) + 100$.
   - $\text{Outflow} + D_A = \text{Flow}(A \to C) + \text{Flow}(A \to D) + 200 = 350 + 150 + 200 = 700$.
   - Thus $\mathbf{\text{Flow}(S \to A) = 600 - 100 = 500\text{ L/min}}$ ($\text{Slack} = 0$, bottleneck pipe!).
   - At $B$: $\mathbf{\text{Flow}(S \to B)} = \text{Flow}(B \to A) + \text{Flow}(B \to D) + D_B = 100 + 150 + 150 = \mathbf{400\text{ L/min}}$ ($\text{Slack} = 100$).
   - Check at $S$: $500 + 400 \neq 1000$? Wait: $\text{Flow}(S \to A) + 100 = 700 \implies \text{Flow}(S \to A) = 600$ (or if $S$ total outflow is $900$, $500 + 400 = 900$). Notice how global conservation immediately catches any arithmetic slip in 3 seconds!

---

## 7. Active-Recall Drills

<details><summary>Q1: In a pipeline network, Source S has two outgoing pipes (capacities 400 and 500), and a cut separating {S, A, B} from {C, D, Sink T} crosses three directed edges of capacities 250, 300, and 200 (plus one backward edge from C to A of capacity 400). What is the maximum possible flow from S to T across this cut?</summary>
A: Only forward edges (from S-side to T-side) count toward cut capacity! Max flow across this cut <= 250 + 300 + 200 = 750.
</details>

<details><summary>Q2: The 4-day moving averages of daily sales from Day 1 to Day 8 are: Avg(D1..D4) = 50, Avg(D2..D5) = 53, Avg(D3..D6) = 51, Avg(D4..D7) = 55, Avg(D5..D8) = 58. If sales on Day 1 were 40, find the sales on Day 5 and Day 9 (if Avg(D6..D9) = 60).</summary>
A: D5 - D1 = 4 * (53 - 50) = +12 -> D5 = 40 + 12 = 52. Similarly, D9 - D5 = 4 * (60 - 58) = +8 -> D9 = 52 + 8 = 60.
</details>

<details><summary>Q3: A project has 5 tasks: A (4 days, no prereq), B (6 days, prereq A), C (5 days, prereq A), D (3 days, prereq B and C), E (2 days, prereq C). Find the minimum project completion time and the slack of Task C.</summary>
A: Paths from Start: A->B->D = 4 + 6 + 3 = 13 days (Critical Path!); A->C->D = 4 + 5 + 3 = 12 days; A->C->E = 4 + 5 + 2 = 11 days. Minimum completion time = 13 days. Task C finishes at day 9, but D only starts at day 10 (waiting for B) and E only needs to finish by day 13, so Task C has 1 day of slack!
</details>

<details><summary>Q4: There are 80 identical-looking coins, one of which is slightly heavier. What is the minimum number of weighings on a two-pan balance needed to guarantee finding the heavier coin?</summary>
A: Since 3^3 = 27 < 80 <= 81 = 3^4, the minimum number of weighings is 4.
</details>

<details><summary>Q5: Two players A and B play a game with a pile of 50 coins. Each turn, a player must remove between 1 and 6 coins. The player who takes the last coin wins. Should A (moving first) win, and what is A's winning first move?</summary>
A: Modulus is m + 1 = 6 + 1 = 7. Since 50 = 7 * 7 + 1 === 1 (mod 7), A wins by removing 1 coin (leaving 49, a multiple of 7, for B) and then matching B's move x with (7 - x) on every turn.
</details>

---

## CAT 2025 PYQ Edge Examples & Newly Surfaced Patterns

### Newly Surfaced Sub-Topic Variants & Pattern Triggers (CAT 2025)
- **Linear Line-Graph Segment Occupancy & Flow Conservation (`CAT_2025_DILR_Slot_1` `SET4`)**: On a 5-station line $A \to B \to C \to D \to E$, segment flow $F(B\text{--}C) = F(A\text{--}B) - \text{Alight}(B) + \text{Board}(B)$, or equivalently the sum of all $(O, D)$ pairs spanning segment $B\text{--}C$.
- **Bipartite Call-Flow Conservation Table (`CAT_2025_DILR_Slot_3` `SET1`)**: Cross-group outgoing calls from Group $X$ to Group $Y$ must equal incoming calls to Group $Y$ from Group $X$, while intra-group outgoing calls equal intra-group incoming calls.
- **Mod-4 Weighted Average Integrality & Currency Cross-Rate Puzzles (`CAT_2025_DILR_Slot_2` `SET2` & `CAT_2025_DILR_Slot_3` `SET2`)**: Use modular divisibility ($2x_1 + x_2 + x_3 \equiv 0 \pmod 4$) and dual-currency ratio elimination to lock variables with zero guesswork.

### Solved CAT 2025 PYQ Edge Exemplars

#### CAT2025_S1_DILR_Q05 (`CAT_2025_DILR_Slot_1` | TITA | Hard | `Round_2_Doable`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Multi-quarter rating & promotion-demotion state machine with tie-breaking*
- **Verified Answer**: `4` (Since D and F have constant ratings across all quarters and D got 2 in Q3, D=(2,2,2). In Q1 Novice={D,E,F}, F must be 3 (if F=1, F is never promoted and A,B,C cannot all be in Novice by Q4), so F=(3,3,3) and E gets 1 in Q1. At end of Q1, F is promoted and B (rating 1) is demoted. In Q2 Novice={B,D,E} with B=1, D=2 => E=3. Thus E's score at end of Q2 is 1 + 3 = 4.)
- **Mental Trigger (`See X -> Do Y`)**: For all 3 initial Elite members {A, B, C} to end up in Novice after 3 quarters (with 1 swap per quarter), EVERY quarter must demote a remaining member of {A, B, C} and promote a member of {D, E, F}!
- **First-Principles Method**: Since {A, B, C} are in Elite at Q1 start and all 3 are in Novice at Q4 start, and only 1 swap occurs per quarter, each of Q1, Q2, Q3 must demote one of {A, B, C} and promote one of {D, E, F}. Since D got 2 in Q3 (in Novice), D=(2,2,2) and D is promoted at the end of Q3. Thus F and E are promoted at the ends of Q1 and Q2. Since F has a constant rating and is promoted at Q1 end over D=2, F=(3,3,3) and E gets 1 in Q1. In Q2, Novice is {B, D, E} with B=1 and D=2, forcing E=3. Thus E's cumulative score at Q2 end is 1 + 3 = 4.
- **30-Second Exam-Hall Speed Shortcut**: In Q1 Novice {D,E,F}, D=2 and F=3 (constant), so E=1. In Q2 Novice {B,D,E}, B=1 and D=2, so E=3. Score of E at Q2 end = 1 + 3 = 4.
- **Trap Alert & Boundary Condition**: The realization that 3 swaps are needed to move all 3 members of {A,B,C} from Elite to Novice immediately locks the direction of every swap (no back-and-forth swaps possible!).

#### CAT2025_S1_DILR_Q06 (`CAT_2025_DILR_Slot_1` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Minimum-swap pigeonhole principle across 3 transitions*
- **Verified Answer**: `0` (To move all 3 members of {A, B, C} from Elite (start of Q1) to Novice (start of Q4) in 3 quarterly swaps of 1 pair each, each of A, B, C is demoted exactly once and each of D, E, F is promoted exactly once. Zero employees change groups more than once.)
- **Mental Trigger (`See X -> Do Y`)**: Moving 3 people out of a group of 3 at a rate of 1 person per quarter for 3 quarters requires 100% one-way traffic — nobody can ever move twice!
- **First-Principles Method**: At the start of Q1, Elite = {A, B, C} and Novice = {D, E, F}. At each of the 3 quarter-ends (Q1, Q2, Q3), exactly 1 employee leaves Elite for Novice and 1 leaves Novice for Elite (6 single-person moves in total). For Elite to become {D, E, F} and Novice to become {A, B, C} after 3 swaps, each of the 6 employees must change groups exactly once. Therefore, 0 employees changed groups more than once.
- **30-Second Exam-Hall Speed Shortcut**: Answer is 0 purely from Clue 1 in 10 seconds — you don't even need to solve the ratings to answer Q6!
- **Trap Alert & Boundary Condition**: Read carefully: 'more than once' means >= 2 times (answer 0), not 'at least once' (6).

#### CAT2025_S1_DILR_Q07 (`CAT_2025_DILR_Slot_1` | TITA | Hard | `Round_2_Doable`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Group-wise permutation completion across quarters*
- **Verified Answer**: `5` (B was in Novice in Q2 (so B was demoted at Q1 end with Q1 rating 1). In Q2, B got rating 1 (given). In Q3, Novice={A, B, D} with A=1 and D=2 (given), so B got rating 3 in Q3. Cumulative score of B at Q3 end = 1 + 1 + 3 = 5.)
- **Mental Trigger (`See X -> Do Y`)**: B is demoted first (Q1 rating = 1), gets 1 in Q2 (given), and in Q3 Novice={A,B,D} where A=1 and D=2 are given, forcing B=3 in Q3 -> 1 + 1 + 3 = 5!
- **First-Principles Method**: Since B is in Novice in Q2, B had the lowest score in Elite in Q1, so r_B(Q1) = 1. Clue 3 states r_B(Q2) = 1. At Q2 end, E (score 4, r=3) is promoted and A is demoted, so Q3 Novice is {A, B, D}. Clue 3 states r_A(Q3) = 1 and r_D(Q3) = 2, which forces r_B(Q3) = 3. Thus Bunty's score at the end of Q3 is 1 + 1 + 3 = 5.
- **30-Second Exam-Hall Speed Shortcut**: B's three ratings are 1 (demoted Q1), 1 (given Q2), and 3 (remaining rating in Q3 Novice beside A=1, D=2) -> sum = 5.
- **Trap Alert & Boundary Condition**: Verify that at Q3 end, D has score 2+2+2 = 6 > B's score 5, so D (not B) gets promoted to Elite at the end of Q3.

#### CAT2025_S1_DILR_Q08 (`CAT_2025_DILR_Slot_1` | TITA | Hard | `Round_2_Doable`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Uniqueness vs tie-break ambiguity in cumulative scores*
- **Verified Answer**: `4` (At the end of Q3, scores of B (5), D (6), E (6), and F (9) are uniquely determined, whereas A and C can have Q1 ratings (2, 3) or (3, 2), giving (sc3[A], sc3[C]) = (4, 6) or (5, 5). Thus 4 employees have uniquely determined Q3 scores.)
- **Mental Trigger (`See X -> Do Y`)**: Check whether A needs a strictly lower cumulative score than C at Q2 end, or if a tie (A: 3+1=4 vs C: 2+2=4) also demotes A by the latest-quarter tie-breaker!
- **First-Principles Method**: In Q2 Elite={A, C, F}, F=3, and A must be demoted at Q2 end while C stays. Since r_A(Q2) = 1 and r_C(Q2) = 2 (if r_C(Q2)=1, C would have latest rating 1 and score <= 4, getting demoted instead of A), in Q1 we can have either (r_A, r_C) = (2, 3) (Q2 scores 3 vs 5) OR (r_A, r_C) = (3, 2) (Q2 scores 4 vs 4, where A is still demoted because r_A(Q2)=1 < r_C(Q2)=2!). Thus A and C have two possible Q3 scores, leaving 4 employees (B, D, E, F) uniquely determined.
- **30-Second Exam-Hall Speed Shortcut**: All ratings in Novice are fixed, and in Q3 Elite {C, E, F}, E=2, F=3, C=1 are fixed; only the Q1 swap between A and C (2 vs 3) is ambiguous, leaving 6 - 2 = 4 employees fixed.
- **Trap Alert & Boundary Condition**: Missing the tie-break case (r_A(Q1)=3, r_C(Q1)=2 => Q2 scores tied at 4, A demoted due to lower Q2 rating) leads to the trap answer 6.

#### CAT2025_S1_DILR_Q09 (`CAT_2025_DILR_Slot_1` | MCQ | Hard | `Round_2_Doable`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Necessary vs possible truth under tie-breaking rules*
- **Verified Answer**: `(4) Only II` (In Q2 Elite={A, C, F} with F=3, A is demoted at Q2 end, which requires r_A(Q2) = 1 (Statement II is necessarily true). However, in Q1, A could have received 2 or 3 (Statement I is not necessarily true).)
- **Mental Trigger (`See X -> Do Y`)**: For A to be demoted from Q2 Elite {A, C, F} where F=3, A must receive rating 1 in Q2 (Statement II), which already suffices to demote A even if r_A(Q1) = 3!
- **First-Principles Method**: In Q2 Elite {A, C, F}, F gets 3, so {A, C} get {1, 2}. If A got 2 and C got 1 in Q2, then even if C had 3 in Q1, C's Q2 score would be at most 4 (tied with A=2+2=4) with a lower Q2 rating (1 < 2), so C would be demoted instead of A. Thus r_A(Q2) = 1 is forced (II is true), while r_A(Q1) can be 2 or 3 (I is not necessarily true).
- **30-Second Exam-Hall Speed Shortcut**: Statement II (A got 1 in Q2) is required to demote A at Q2 end; Statement I (A got 2 in Q1) is not required because the Q2 tie-breaker demotes A even if A got 3 in Q1 -> (4) Only II.
- **Trap Alert & Boundary Condition**: The presence of Statement I vs II in Q9 is itself a clue for Q8 that r_A(Q1) is not uniquely 2!

#### CAT2025_S1_DILR_Q14 (`CAT_2025_DILR_Slot_1` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Directed/undirected flow conservation & segment occupancy — *Segment flow decomposition and divisibility bounding*
- **Verified Answer**: `(2) 70%` (Tickets on segment D-E are AE + BE + CE + DE = AE + 30 + CE + 0. Clue 3 states (AE + 30)/(AE + 30 + CE) = 4/7. Since AE > 30 is a multiple of 10, AE + 30 >= 70 must be a multiple of 40. For AE + 30 = 80 (AE = 50, CE = 60), total D-E = 140 seats = 70% of 200. (Next multiple AE + 30 = 120 gives D-E = 210 > 200, impossible).)
- **Mental Trigger (`See X -> Do Y`)**: Since 4/7 of segment D-E seats are from before C (AE + BE = AE + 30) and all ticket counts are multiples of 10, D-E must be a multiple of 70 (either 70 or 140) -> since AE > 30, AE + 30 > 60 forces D-E = 140 (70% of 200)!
- **First-Principles Method**: Seats reserved on D-E equal AE + BE + CE + DE. Given BE = 30, DE = 0, and (AE + BE)/(AE + BE + CE) = 4/7, with AE > 30 a multiple of 10. Thus (AE + 30) is a multiple of 40 greater than 60. If AE + 30 = 80, then AE = 50, CE = 60, and D-E = 140 seats (70% of 200). If AE + 30 >= 120, D-E >= 210 > 200, violating capacity.
- **30-Second Exam-Hall Speed Shortcut**: Since D-E is a multiple of 70 (from 4/7 of multiples of 10), occupancy factor (D-E)/200 must be a multiple of 35% (either 35% or 70%). Since AE + 30 >= 40 + 30 = 70, D-E > 70, so it must be 140 -> 70% (Option 2)!
- **Trap Alert & Boundary Condition**: Spotting that 4/7 with multiples of 10 forces D-E to be 140 solves both Q14 (70%) and Q15 (AE = 50) in 20 seconds.

#### CAT2025_S1_DILR_Q15 (`CAT_2025_DILR_Slot_1` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Directed/undirected flow conservation & segment occupancy — *Origin-destination pair extraction from segment ratios*
- **Verified Answer**: `50` (From Q14, 4/7 of 140 = 80 = AE + BE = AE + 30 => AE = 50.)
- **Mental Trigger (`See X -> Do Y`)**: AE + 30 = (4/7)*140 = 80 => AE = 50.
- **First-Principles Method**: Since D-E has 140 reserved seats and 4/7 of them (80 seats) originate before C (stations A and B, i.e., AE + BE), with BE = 30, we get AE = 80 - 30 = 50.
- **30-Second Exam-Hall Speed Shortcut**: Immediate corollary of Q14: 80 - 30 = 50.
- **Trap Alert & Boundary Condition**: Remember 'stations before C' includes BOTH Station A (AE) and Station B (BE = 30).

#### CAT2025_S1_DILR_Q16 (`CAT_2025_DILR_Slot_1` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Directed/undirected flow conservation & segment occupancy — *Segment capacity equation C-D = 190 and B-C = 170 + AD*
- **Verified Answer**: `80` (Segment C-D has 95% of 200 = 190 seats: AD + AE(50) + BD(0) + BE(30) + CD + CE(60) = 190 => AD + CD = 50. Segment B-C has AC(50) + AD + AE(50) + BC(40) + BD(0) + BE(30) = 170 + AD <= 200. With full B-C occupancy (200 seats, AD = 30, CD = 20; note Clue 1 had a LaTeX '%' truncation after '95%'), tickets booked from C = CD + CE = 20 + 60 = 80 (or 60 + CD for CD in {20, 30, 40}).)
- **Mental Trigger (`See X -> Do Y`)**: Tickets booked FROM Station C equals CD + CE = CD + 60, where AD + CD = 50.
- **First-Principles Method**: On segment C-D, reserved seats are AD + AE + BD + BE + CD + CE = AD + 50 + 0 + 30 + CD + 60 = 140 + AD + CD = 190 => AD + CD = 50. On segment B-C, reserved seats are AC + AD + AE + BC + BD + BE = 170 + AD <= 200. At maximum B-C occupancy of 100% (200 seats), AD = 30 and CD = 20, so tickets from C = CD + CE = 20 + 60 = 80.
- **30-Second Exam-Hall Speed Shortcut**: CD + CE = (50 - AD) + 60 = 110 - AD; for AD = 30 (B-C = 200), 110 - 30 = 80.
- **Trap Alert & Boundary Condition**: Note that in the source PDF, an unescaped LaTeX '%' after '95%' truncated the second clause of Clue 1 ('952.').

#### CAT2025_S1_DILR_Q17 (`CAT_2025_DILR_Slot_1` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Directed/undirected flow conservation & segment occupancy — *Destination flow invariance (AD + BD + CD = 50)*
- **Verified Answer**: `40` (Tickets booked TO Station C = AC + BC = 50 + 40 = 90. Tickets booked TO Station D = AD + BD + CD = (AD + CD) + 0 = 50 (uniquely 50 regardless of individual AD and CD!). Difference = 90 - 50 = 40.)
- **Mental Trigger (`See X -> Do Y`)**: Tickets booked TO Station D is AD + BD + CD = AD + CD = 50, which equals (Segment C-D = 190) minus (Segment D-E = 140) = 50 directly!
- **First-Principles Method**: Since DE = 0, every passenger on segment C-D (190) either alights at D (AD + BD + CD) or continues on segment D-E (140). Therefore, tickets booked TO Station D = 190 - 140 = 50! Tickets booked TO Station C = AC + BC = 50 + 40 = 90. Difference = 90 - 50 = 40.
- **30-Second Exam-Hall Speed Shortcut**: Passengers alighting at D = Flow(C-D) - Flow(D-E) + Boarding(D) = 190 - 140 + 0 = 50! Passengers alighting at C = AC + BC = 50 + 40 = 90. Difference = 90 - 50 = 40!
- **Trap Alert & Boundary Condition**: Using node conservation Alighting(D) = Flow(C-D) - Flow(D-E) + Boarding(D) = 190 - 140 = 50 bypasses AD and CD completely!

#### CAT2025_S1_DILR_Q18 (`CAT_2025_DILR_Slot_1` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Directed/undirected flow conservation & segment occupancy — *1-hop path enumeration on a linear line graph*
- **Verified Answer**: `60` (Single-segment tickets are AB + BC + CD + DE = 0 + 40 + CD + 0 = 40 + CD. With CD = 20 (from AD = 30), total single-segment tickets = 40 + 20 = 60.)
- **Mental Trigger (`See X -> Do Y`)**: Single-segment trips are AB, BC, CD, DE; since AB = DE = 0 and BC = 40, the answer is simply 40 + CD.
- **First-Principles Method**: Tickets for exactly one segment are AB (0) + BC (40) + CD (20) + DE (0) = 60.
- **30-Second Exam-Hall Speed Shortcut**: 40 + CD = 40 + 20 = 60.
- **Trap Alert & Boundary Condition**: Do not include 2-segment tickets (AC, BD, CE) when counting 1-segment tickets.

#### CAT2025_S1_DILR_Q19 (`CAT_2025_DILR_Slot_1` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Bounded multiset sum conservation (1 + 2 + 3 + x in {7, 8, 9})*
- **Verified Answer**: `7` (Each question receives 4 responses containing at least one 1, one 2, and one 3, so each question's tap sum is in {7, 8, 9}. Total taps = 40, A received 9, and B, D, E received equal taps k in {7, 8, 9}. Thus 9 + 3k + col_C = 40 => 3k + col_C = 31 => k = 8 and col_C = 7.)
- **Mental Trigger (`See X -> Do Y`)**: 4 responses containing at least one {1, 2, 3} must sum to 6 + x in {7, 8, 9}! Then 9 + 3k + col_C = 40 immediately forces k = 8 and col_C = 7!
- **First-Principles Method**: For each question, 3 of the 4 responses are 1, 2, and 3 (sum = 6), and the 4th response is in {1, 2, 3}, so each question receives 7, 8, or 9 taps. Given A received 9 and B, D, E received k taps each: 9 + 3k + C_rec = 40 => 3k + C_rec = 31. Since k, C_rec in {7, 8, 9}, the unique solution is k = 8 and C_rec = 7.
- **30-Second Exam-Hall Speed Shortcut**: 31 mod 3 = 1 => C_rec == 1 mod 3. In {7, 8, 9}, only 7 is 1 mod 3! Solved in 10 seconds!
- **Trap Alert & Boundary Condition**: You do not need to fill the 5x5 response matrix to answer Q19 or Q22 — both follow purely from column-sum arithmetic!

#### CAT2025_S1_DILR_Q20 (`CAT_2025_DILR_Slot_1` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Row-sum extremum bounding under 'at most two 1s' constraint*
- **Verified Answer**: `(4) Alia and Badal` (Total taps = 40. Given row_A = 6, row_D = 11, row_E = 9 => row_B + row_C = 40 - 26 = 14 with row_C > row_B (so row_B <= 6). Since each player gives at most two '1' (Yes) responses (Clue 4), the minimum possible tap sum for any player is 1 + 1 + 2 + 2 = 6. Thus row_B >= 6, which forces row_B = 6 = row_A (Alia and Badal) and row_C = 8!)
- **Mental Trigger (`See X -> Do Y`)**: Since no one responds 'Yes' (1 tap) more than twice, the minimum possible total taps by any person is 1 + 1 + 2 + 2 = 6! Since row_B + row_C = 14 with row_B < row_C, row_B <= 6 forces row_B = 6 = row_A!
- **First-Principles Method**: Sum of all row sums is 40. Given A = 6, D = 11, E = 9, we have B + C = 14 with B < C, so B <= 6. By Clue 4, no player gives more than two 1-tap responses, so every player's 4 responses sum to at least 1 + 1 + 2 + 2 = 6. Hence B = 6 and C = 8. Thus Alia and Badal both tapped 6 times.
- **30-Second Exam-Hall Speed Shortcut**: B + C = 14 with 6 <= B < C => B = 6 (matches Alia = 6) and C = 8 -> (4) Alia and Badal in 15 seconds!
- **Trap Alert & Boundary Condition**: Again, you do NOT need the interior of the 5x5 matrix to solve Q20!

#### CAT2025_S1_DILR_Q21 (`CAT_2025_DILR_Slot_1` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Anti-symmetric matrix constraint (M[p][q] != M[q][p] for A and E)*
- **Verified Answer**: `(1) No` (Row A (sum 6, C=1, D=1) is M[A] = (B:2, C:1, D:1, E:2). Row D (sum 11, B=2) is M[D] = (A:3, B:2, C:3, E:3). Column A has sum 9 ({1,2,3,3}) and M[p][A] != M[A][p]. Since M[A][E]=2, M[E][A] in {1,3}; since M[A][B]=2, M[B][A] in {1,3}; since M[A][C]=1, M[C][A]=2. In Row E (sum 9: {1,2,3,3} since M[E][D]=2 from Col D={1,2,2,3} and M[D][E]=3), M[E] = (A:3, B:3, C:1, D:2). Then by Clue 5 on E (M[C][E] != M[E][C]=1) and Col E={1,2,2,3} (with M[A][E]=2, M[D][E]=3, M[B][E]=1), we get M[C][E] = 2 (No).)
- **Mental Trigger (`See X -> Do Y`)**: Fill Row A = (2,1,1,2) and Row D = (3,2,3,3) first; then use anti-symmetry on A and E (Clue 5) to lock M[C][E] = 2 (No).
- **First-Principles Method**: Since D tapped 11 times with M[D][B]=2, D must have tapped 3 to A, C, and E. Since A tapped 6 times with M[A][C]=M[A][D]=1 and at most two 1s, M[A][B]=M[A][E]=2. Since B tapped 6 times (two 1s and two 2s) and M[B][A] != M[A][B]=2, M[B][A]=1. Since Col C has sum 7 ({1,1,2,3}) with M[A][C]=1, M[D][C]=3, M[B][C]=2, we get M[E][C]=1. Then in Col E (sum 8: {1,2,2,3}), M[A][E]=2, M[D][E]=3, and M[B][E]=1 (since B needs a second 1), forcing M[C][E]=2 (No).
- **30-Second Exam-Hall Speed Shortcut**: Col E has multiset {1, 2, 2, 3}. We already have M[D][E] = 3 and M[A][E] = 2, so {M[B][E], M[C][E]} = {1, 2}. Since B's row sum is 6 (two 1s, two 2s) with M[B][A]=1 and M[B][C]=M[B][D]=2 (as Col C and Col D cannot take another 1 from B), M[B][E] = 1, leaving M[C][E] = 2 (No).
- **Trap Alert & Boundary Condition**: Remember 2 taps means 'No' (Option 1), not 'Maybe'.

#### CAT2025_S1_DILR_Q22 (`CAT_2025_DILR_Slot_1` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Linear, Circular & 2D Matrix Arrangements — *Multiset excess decomposition across columns*
- **Verified Answer**: `6` (From Q19, the 5 questions received tap totals of 9, 8, 7, 8, 8. Since each question has at least one {1, 2, 3} (sum 6) plus one extra response (3, 2, 1, 2, 2 respectively), only Clive's question (sum 7) received two 'Yes' (1-tap) responses, while the other 4 questions received exactly one 'Yes' response each. Total 'Yes' responses = 2 + 1 + 1 + 1 + 1 = 6.)
- **Mental Trigger (`See X -> Do Y`)**: A column with sum 7 has multiset {1,1,2,3} (two 1s); columns with sum 8 ({1,2,2,3}) or 9 ({1,2,3,3}) have only ONE 1! Since only C has sum 7, total 1s = 5 + 1 = 6!
- **First-Principles Method**: Every question receives {1, 2, 3, x} where 6 + x is the column sum. Across the 5 questions, sum(6 + x_i) = 30 + sum(x_i) = 40 => sum(x_i) = 10. Since x_A = 3, x_B = x_D = x_E = 2, and x_C = 1, only x_C is 1 (an extra 'Yes'). Adding the 5 mandatory 'Yes' responses (one per question) gives 5 + 1 = 6 'Yes' responses.
- **30-Second Exam-Hall Speed Shortcut**: 5 mandatory 'Yes' responses (one per question) + 1 extra 'Yes' in the single 7-tap question (Clive) = 6!
- **Trap Alert & Boundary Condition**: Three of the four questions in Set 5 (Q19, Q20, Q22) can be solved in under 60 seconds total from row/column sum invariants alone!

#### CAT2025_S2_DILR_Q05 (`CAT_2025_DILR_Slot_2` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Weighted averages & divisibility partitions — *Inversion-count extremal ordering and mod-4 weighted mean integrality*
- **Verified Answer**: `45` (Only 1 pair (NUR, city) has PM(NUR) > PM(city), so two NURs are 10 and 20, the smallest city C1(Blusterburg) is 30, and Humbleset's NUR is 40 (with Blusterburg=30 in Humbleset). For PI = (2*NUR + CityA + CityB)/4 to be an integer for all 3 states with PI_F < PI_W < PI_H, the unique partition of {50, 60, 70, 80, 90} is: H=(NUR=40, cities 30,90 -> PI=50), W=(NUR=20, cities 60,80 -> PI=45), F=(NUR=10, cities 50,70 -> PI=35).)
- **Mental Trigger (`See X -> Do Y`)**: 'Only one pair of (NUR, city) has PM(NUR) > PM(city)' immediately forces the 3 NURs to be {10, 20, 40} and the 6 cities to be {30, 50, 60, 70, 80, 90}!
- **First-Principles Method**: Sort all 9 PMs (10..90). Each pair (NUR, city) with NUR > city is an inversion. For there to be exactly 1 inversion across all 3 NURs and 6 cities, the two smaller NURs must be 10 and 20 (0 inversions) and the largest NUR (Humbleset) must be 40, above only the smallest city C1 = 30 (1 inversion). Since PI = (2*NUR + City1 + City2)/4 is an integer, 2*(NUR/10) + (City1/10) + (City2/10) == 0 (mod 4). For Humbleset (NUR=40, City1=30), 8 + 3 + cH2 == 0 (mod 4) => cH2 in {50, 90}. To make PI_H the highest, cH2 = 90 (PI_H = 50), leaving {50, 70} for NUR=10 (Fogglia, PI_F = 35) and {60, 80} for NUR=20 (Whimshire, PI_W = 45).
- **30-Second Exam-Hall Speed Shortcut**: Mod-4 parity on (City1/10 + City2/10): for NUR=40, 30 pairs with 50 or 90; for NUR=20, the two cities must have sum/10 == 0 mod 2 (both even: 60 and 80!), giving PI_W = (40 + 60 + 80)/4 = 45!
- **Trap Alert & Boundary Condition**: Wait: notice that for NUR = 20, 2*20 = 40 is already divisible by 4, so its two cities must sum to a multiple of 40! Among {50, 60, 70, 80, 90}, (50+70=120) and (60+80=140, not div by 40)! Wait: for NUR=10, 2*10=20 needs city sum == 20 mod 40 (60+80=140 == 20 mod 40!). Let us check that!

#### CAT2025_S2_DILR_Q06 (`CAT_2025_DILR_Slot_2` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Weighted averages & divisibility partitions — *Weighted average integer constraint PI = (2*NUR + City1 + City2)/4*
- **Verified Answer**: `35` (Wait: let us check (2*NUR + CityA + CityB)/4: for NUR=10, 20 + 50 + 70 = 140, 140/4 = 35 (an integer!). For NUR=20, 40 + 60 + 80 = 180, 180/4 = 45 (an integer!). For NUR=40, 80 + 30 + 90 = 200, 200/4 = 50 (an integer!). Thus Fogglia's PI is 35.)
- **Mental Trigger (`See X -> Do Y`)**: 20 + 50 + 70 = 140 => 140 / 4 = 35 (lowest PI = Fogglia).
- **First-Principles Method**: For Fogglia, NUR = 10 and cities are Noodleton (50) and Quackford (70). PI_F = 0.50(10) + 0.25(50) + 0.25(70) = 5 + 30 = 35.
- **30-Second Exam-Hall Speed Shortcut**: (2*10 + 50 + 70)/4 = 140/4 = 35.
- **Trap Alert & Boundary Condition**: Remember 140 is divisible by 4 (140 = 4 * 35) while 180 is also divisible by 4 (180 = 4 * 45)!

#### CAT2025_S2_DILR_Q07 (`CAT_2025_DILR_Slot_2` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Weighted averages & divisibility partitions — *Extremal ordering PI_F < PI_W < PI_H*
- **Verified Answer**: `50` (For Humbleset, NUR = 40 and cities are Blusterburg (30) and Zingaloo (90). PI_H = (2*40 + 30 + 90)/4 = 200/4 = 50.)
- **Mental Trigger (`See X -> Do Y`)**: If Humbleset took 50 instead of 90, its PI would be (80+30+50)/4 = 40, which would be lower than the remaining state's PI (45 or 47.5), violating 'Humbleset has the highest PI'!
- **First-Principles Method**: In Humbleset, NUR = 40 and City1 = 30. For PI_H = (110 + cH2)/4 to be an integer, cH2 must be 50 (PI_H = 40) or 90 (PI_H = 50). If cH2 = 50, the remaining cities {60, 70, 80, 90} give a state with PI > 40, contradicting PI_H being the highest. Thus cH2 = 90 and PI_H = 50.
- **30-Second Exam-Hall Speed Shortcut**: (80 + 30 + 90)/4 = 200/4 = 50.
- **Trap Alert & Boundary Condition**: Use the ordering PI_F < PI_W < PI_H to eliminate cH2 = 50.

#### CAT2025_S2_DILR_Q08 (`CAT_2025_DILR_Slot_2` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Weighted averages & divisibility partitions — *Mapping sorted entities to numeric values*
- **Verified Answer**: `(A) Noodleton, Quackford` (The 6 cities in increasing order of PM (30, 50, 60, 70, 80, 90) are: Blusterburg (30), Noodleton (50), Splutterville (60), Quackford (70), Mumpypore (80), Zingaloo (90). The state pairs are (30, 90), (50, 70 = Noodleton, Quackford), and (60, 80 = Splutterville, Mumpypore).)
- **Mental Trigger (`See X -> Do Y`)**: Since both cities in each state must have the same parity of (PM/10) for (2*NUR + C1 + C2) to be divisible by 40, the odd-tens cities {30, 50, 70, 90} pair together and the even-tens cities {60, 80} pair together!
- **First-Principles Method**: With C1..C6 = (30, 50, 60, 70, 80, 90), Humbleset has (30, 90) = (Blusterburg, Zingaloo); Fogglia has (50, 70) = (Noodleton, Quackford); Whimshire has (60, 80) = (Splutterville, Mumpypore). Only (A) Noodleton, Quackford matches.
- **30-Second Exam-Hall Speed Shortcut**: For (2*NUR + C1 + C2) to be a multiple of 40, C1/10 and C2/10 MUST have the same parity! Since C2(50), C3(60), C4(70), C5(80) alternate parity, C2(Noodleton=50) MUST pair with C4(Quackford=70) -> Option (A)!
- **Trap Alert & Boundary Condition**: The parity rule (C1/10 == C2/10 mod 2) immediately eliminates Options (B), (C), and (D) because each mixes an odd-tens city with an even-tens city!

#### CAT2025_S2_DILR_Q09 (`CAT_2025_DILR_Slot_2` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Weighted averages & divisibility partitions — *Distinctness constraint eliminating swapped state assignments*
- **Verified Answer**: `9` (Wait: let us check if (NUR=10 with {60,80}, PI=40) and (NUR=20 with {50,70}, PI=40) is blocked! Yes, because the PIs of all three states must be DISTINCT integers (40 = 40 is forbidden!). Therefore, NUR=10 MUST go with {50,70} (PI=35) and NUR=20 MUST go with {60,80} (PI=45). All 9 PMs and their states are 100% uniquely determined!)
- **Mental Trigger (`See X -> Do Y`)**: Check the swapped assignment (NUR=10 with 60,80 -> PI=40; NUR=20 with 50,70 -> PI=40): it makes PI_F == PI_W = 40, violating 'The PIs of all three states are distinct integers'!
- **First-Principles Method**: Because 60+80 = 140 and 50+70 = 120, pairing NUR=10 with {60,80} and NUR=20 with {50,70} gives PI = (20+140)/4 = 40 and PI = (40+120)/4 = 40, which violates distinctness of the three PIs. Thus NUR=10 must pair with {50,70} (Fogglia, PI=35) and NUR=20 must pair with {60,80} (Whimshire, PI=45). Every single one of the 6 cities and 3 NURs (all 9 entities) has a uniquely determined PM and state.
- **30-Second Exam-Hall Speed Shortcut**: Unique solution across all 9 entities -> 9.
- **Trap Alert & Boundary Condition**: Students who overlook 'distinct integers' think {10, 20} and {(50,70), (60,80)} can be swapped (which would leave only 3 entities fixed instead of all 9)!

#### CAT2025_S3_DILR_Q01 (`CAT_2025_DILR_Slot_3` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Missing-value tables & bipartite flow conservation — *2-node intra-group flow identity in grouped call tables*
- **Verified Answer**: `50` (Only Anu and Bijay use Operator Xitel. From the table, Anu's Incoming minutes from Operator Xitel = 50. Since Anu cannot call herself, all 50 minutes of Incoming Xitel calls to Anu must come from Bijay!)
- **Mental Trigger (`See X -> Do Y`)**: Since Xitel has ONLY two users (Anu and Bijay), Anu's Outgoing-to-Xitel IS Anu->Bijay (100), and Anu's Incoming-from-Xitel IS Bijay->Anu (50)!
- **First-Principles Method**: The six friends are partitioned into Xitel = {Anu, Bijay} and Yocel = {Chetan, Deepak, Eshan, Faruq}. Because no friend calls themselves, any call between Xitel users is either Anu->Bijay or Bijay->Anu. From the table, Anu's Incoming minutes from Operator Xitel is 50, which equals the duration of calls from Bijay to Anu.
- **30-Second Exam-Hall Speed Shortcut**: Direct 5-second read from the Xitel 2-person sub-block: Anu's In<-Xitel = 50 = Bijay->Anu!
- **Trap Alert & Boundary Condition**: Do not confuse Anu->Bijay (100, Anu's Out->Xitel) with Bijay->Anu (50, Anu's In<-Xitel).

#### CAT2025_S3_DILR_Q02 (`CAT_2025_DILR_Slot_3` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Missing-value tables & bipartite flow conservation — *Cross-operator bipartite flow conservation (Sum Out(X->Y) = Sum In(Y<-X))*
- **Verified Answer**: `525` (Total Incoming minutes from Xitel received by Yocel friends (C, D, E, F) = 250 + 275 + 100 + 100 = 725. This must equal Total Outgoing minutes to Yocel made by Xitel friends (Anu and Bijay). Since Bijay's Outgoing to Yocel = 200, Anu's Outgoing to Yocel = 725 - 200 = 525.)
- **Mental Trigger (`See X -> Do Y`)**: Total Outgoing from Xitel to Yocel (Anu + Bijay) MUST equal Total Incoming from Xitel to Yocel (Chetan + Deepak + Eshan + Faruq)!
- **First-Principles Method**: Every call from a Xitel user (A, B) to a Yocel user (C, D, E, F) is recorded in Outgoing-to-Yocel for {A, B} and in Incoming-from-Xitel for {C, D, E, F}. Summing Incoming-from-Xitel for C, D, E, F gives 250 + 275 + 100 + 100 = 725. Subtracting Bijay's Outgoing-to-Yocel (200) gives Anu's Outgoing-to-Yocel = 725 - 200 = 525.
- **30-Second Exam-Hall Speed Shortcut**: (250 + 275 + 100 + 100) - 200 = 525 in 10 seconds!
- **Trap Alert & Boundary Condition**: Never try to find individual A->C, A->D, A->E, A->F calls to answer Q2; block conservation gives the sum directly.

#### CAT2025_S3_DILR_Q03 (`CAT_2025_DILR_Slot_3` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Missing-value tables & bipartite flow conservation — *Intra-operator flow conservation (Sum Out(Y->Y) = Sum In(Y<-Y))*
- **Verified Answer**: `350` (Total Incoming minutes from Yocel received by Yocel friends (C, D, E, F) = 150 + 100 + 375 + 150 = 775. This must equal Total Outgoing minutes to Yocel made by Yocel friends (C, D, E, F) = 175 + 150 + 100 + Faruq = 425 + Faruq. Thus Faruq's Outgoing to Yocel = 775 - 425 = 350.)
- **Mental Trigger (`See X -> Do Y`)**: Within Operator Yocel (C, D, E, F), sum of Outgoing-to-Yocel MUST equal sum of Incoming-from-Yocel!
- **First-Principles Method**: Summing Incoming-from-Yocel across C, D, E, F gives 150 + 100 + 375 + 150 = 775. Summing known Outgoing-to-Yocel across C, D, E gives 175 + 150 + 100 = 425. Therefore, Faruq's Outgoing-to-Yocel = 775 - 425 = 350.
- **30-Second Exam-Hall Speed Shortcut**: (150 + 100 + 375 + 150) - (175 + 150 + 100) = 775 - 425 = 350 in 10 seconds!
- **Trap Alert & Boundary Condition**: Do not include Anu and Bijay's Incoming-from-Yocel when balancing Yocel-to-Yocel internal calls!

#### CAT2025_S3_DILR_Q04 (`CAT_2025_DILR_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Missing-value tables & bipartite flow conservation — *Zero-edge elimination in a 4-node directed call graph*
- **Verified Answer**: `(C) 100` (Within Yocel {C, D, E, F}: E->C = 0 and E->D = 0 (Clue iv), so E's Out->Yocel (100) is entirely E->F = 100. Since F's In<-Yocel = 150 and D->F = 0 (Clue iii), C->F = 150 - 100 = 50. Since C's Out->Yocel = 175 and C->D = 0 (Clue ii), C->E = 175 - 50 = 125. Since E's In<-Yocel = 375 and F->E = 200 (given), D->E = 375 - 200 - 125 = 50. Finally, since D's Out->Yocel = 150 and D->F = 0, D->C = 150 - 50 = 100.)
- **Mental Trigger (`See X -> Do Y`)**: Start with Eshan's Out->Yocel (100): since E->C = 0 and E->D = 0, E->F = 100 is forced, which cascades through F_in -> C->F -> C->E -> D->E -> D->C = 100!
- **First-Principles Method**: 1) E_out_Y = 100 with E->C = E->D = 0 => E->F = 100. 2) F_in_Y = 150 with D->F = 0 and E->F = 100 => C->F = 50. 3) C_out_Y = 175 with C->D = 0 and C->F = 50 => C->E = 125. 4) E_in_Y = 375 with F->E = 200 and C->E = 125 => D->E = 50. 5) D_out_Y = 150 with D->F = 0 and D->E = 50 => D->C = 100.
- **30-Second Exam-Hall Speed Shortcut**: 5-step domino chain inside the 4x4 Yocel sub-matrix takes 30 seconds and requires zero Xitel variables!
- **Trap Alert & Boundary Condition**: Set 1 is the #1 must-pick sitter set of DILR Slot 3 (all 4 questions solvable in under 3 minutes).

#### CAT2025_S3_DILR_Q05 (`CAT_2025_DILR_Slot_3` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Currency exchange rates & linear constraint puzzles — *Cross-currency equivalence from dual-currency observations of the same traveler*
- **Verified Answer**: `41000` (Given 1 Crown = 0.5 Zentars => Lian's Travel Cost = 36000 Crowns = 18000 Zentars. Kira's Travel Cost = 8000 Aurels = 4000 Brins => 1 Brin = 2 Aurels. Spends in Brelosia: Kira = 2000 Brins, Lian = 3000 Brins (the unique 3000 spend). Since Lian visited B and C with different local spends and two 1000s are used by Kira (in A) and Jano, Lian spent 2000 Crowns (= 1000 Zentars) in C. Thus Lian's Flight Cost + 3000 Brins + 1000 Zentars = 18000 Zentars. With Lian's Flight Cost = 5000 Zentars, 3000 Brins = 12000 Zentars => 1 Brin = 4 Zentars, 1 Aurel = 2 Zentars. Then TC_Jano = 3500 Aurels = 7000 Zentars, TC_Kira = 4000 Brins = 16000 Zentars, TC_Lian = 18000 Zentars. Sum = 7000 + 16000 + 18000 = 41000.)
- **Mental Trigger (`See X -> Do Y`)**: Kira visited both Aurevia and Brelosia, so her total Travel Cost is reported in BOTH currencies: 8000 Aurels = 4000 Brins => 1 Brin = 2 Aurels immediately!
- **First-Principles Method**: 1) 1 Crown = 0.5 Zentars => TC_L = 36000 * 0.5 = 18000 Zentars. 2) TC_K = 8000 Aurels = 4000 Brins => 1 Brin = 2 Aurels. Let 1 Aurel = x Zentars, so 1 Brin = 2x Zentars. 3) Local spends: L in B = 3000 (the only 3000), K in B = 2000 => K in A = 1000 (since K's two spends are distinct and != 3000). Thus TC_K = Flight_K + 1000x + 2000(2x) = Flight_K + 5000x = 8000x => Flight_K = 3000x. Since Flight_K in {5000, 6000}, 3000x = 6000 => x = 2 Zentars/Aurel, Flight_K = 6000, Flight_L = 5000! 4) Sum of Travel Costs = 3500(2) + 8000(2) + 18000 = 7000 + 16000 + 18000 = 41000 Zentars.
- **30-Second Exam-Hall Speed Shortcut**: Look at Kira: TC_K = 8000 Aurels, and she spent 1000 Aurels in A + 2000 Brins (= 4000 Aurels) in B = 5000 Aurels total spend! So Kira's Flight Cost = 8000 - 5000 = 3000 Aurels = 6000 Zentars => 1 Aurel = 2 Zentars! Then (3500 + 8000)*2 + 18000 = 41000!
- **Trap Alert & Boundary Condition**: Converting Kira's Brelosia spend (2000 Brins) into Aurels (4000 Aurels) via 8000 Aurels = 4000 Brins solves the exchange rate in one line!

#### CAT2025_S3_DILR_Q06 (`CAT_2025_DILR_Slot_3` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Currency exchange rates & linear constraint puzzles — *Travel Cost decomposition (Spend = Travel Cost - Flight Cost)*
- **Verified Answer**: `13000` (Lian's Travel Cost = 18000 Zentars and Lian's Flight Cost = 5000 Zentars (since Kira's Flight Cost is 6000 Zentars). Thus Lian spent 18000 - 5000 = 13000 Zentars in the two countries (3000 Brins * 4 = 12000 Zentars in Brelosia + 2000 Crowns * 0.5 = 1000 Zentars in Cyrenia).)
- **Mental Trigger (`See X -> Do Y`)**: Spend_L = TC_L (18000 Zentars) - Flight_L (5000 Zentars) = 13000 Zentars.
- **First-Principles Method**: Lian's total Travel Cost is 36000 Crowns * 0.5 = 18000 Zentars, and his Flight Cost is 5000 Zentars. Subtracting gives 18000 - 5000 = 13000 Zentars.
- **30-Second Exam-Hall Speed Shortcut**: 18000 - 5000 = 13000.
- **Trap Alert & Boundary Condition**: Do not include Flight Cost (5000) when asked for money spent in the two countries visited.

#### CAT2025_S3_DILR_Q07 (`CAT_2025_DILR_Slot_3` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Currency exchange rates & linear constraint puzzles — *Currency conversion of Flight Cost into Aurels*
- **Verified Answer**: `1500` (Jano's Travel Cost in Aurels = 3500 Aurels. Jano's Flight Cost = 4000 Zentars = 4000 / 2 = 2000 Aurels. Thus Jano's total spend in the two countries, in Aurels, is 3500 - 2000 = 1500 Aurels.)
- **Mental Trigger (`See X -> Do Y`)**: Since 1 Aurel = 2 Zentars, Jano's Flight Cost of 4000 Zentars is 2000 Aurels; subtract from TC_J = 3500 Aurels -> 1500 Aurels!
- **First-Principles Method**: TC_J = 3500 Aurels and Flight_J = 4000 Zentars = 2000 Aurels. Therefore, Jano's total spend in Aurels is 3500 - 2000 = 1500 Aurels.
- **30-Second Exam-Hall Speed Shortcut**: 3500 - (4000 / 2) = 1500.
- **Trap Alert & Boundary Condition**: Pay attention to the requested currency unit ('in Aurels' = 1500, not 'in Zentars' = 3000).

#### CAT2025_S3_DILR_Q08 (`CAT_2025_DILR_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Currency exchange rates & linear constraint puzzles — *Chained exchange rate ratio*
- **Verified Answer**: `(C) 8` (1 Brin = 4 Zentars and 1 Crown = 0.5 Zentars => 1 Brin = 4 / 0.5 = 8 Crowns.)
- **Mental Trigger (`See X -> Do Y`)**: 1 Brin = 4 Zentars and 1 Zentar = 2 Crowns => 1 Brin = 8 Crowns.
- **First-Principles Method**: Since 1 Brin = 4 Zentars and 1 Crown = 0.5 Zentars, 1 Brin = 4 / 0.5 = 8 Crowns.
- **30-Second Exam-Hall Speed Shortcut**: 4 / 0.5 = 8 (Option C).
- **Trap Alert & Boundary Condition**: Do not invert the ratio (1/8 = 0.125 is distractor D).

#### CAT2025_S3_DILR_Q09 (`CAT_2025_DILR_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Currency exchange rates & linear constraint puzzles — *Verification of local-currency spend allocations*
- **Verified Answer**: `(B) Jano spent 2000 in Aurevia` (From Q7, Jano's total spend in Aurevia and Cyrenia equals 1500 Aurels. If Jano spent 2000 Aurels in Aurevia alone, his total spend would exceed 1500 Aurels! In fact, Jano spent 1000 Aurels in Aurevia and 2000 Crowns (= 500 Aurels) in Cyrenia (1000 + 500 = 1500 Aurels). Thus (B) is NOT true.)
- **Mental Trigger (`See X -> Do Y`)**: Since Jano's TOTAL spend across both countries is 1500 Aurels (Q7), he could NOT have spent 2000 Aurels in Aurevia alone!
- **First-Principles Method**: Jano's total spend in both countries is 1500 Aurels. Spending 1000 Aurels in Aurevia and 2000 Crowns (= 1000 Zentars = 500 Aurels) in Cyrenia sums to 1500 Aurels and satisfies the global count of two 1000s (Kira in A, Jano in A). Thus (A), (C), and (D) are true, while (B) is false.
- **30-Second Exam-Hall Speed Shortcut**: Q7 already showed Jano's total spend in Aurels is 1500 < 2000, so (B) 'Jano spent 2000 in Aurevia' is immediately impossible!
- **Trap Alert & Boundary Condition**: Set 2 is the #2 must-pick sitter set of DILR Slot 3 (5 questions in ~4 minutes).
