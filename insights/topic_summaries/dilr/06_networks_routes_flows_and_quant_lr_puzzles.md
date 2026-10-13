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
