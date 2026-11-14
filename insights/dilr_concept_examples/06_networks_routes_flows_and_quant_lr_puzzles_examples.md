# DILR 06 Concept & Grid-Evolution Examples: Networks, Routes, Flows, Project Scheduling & Quant-LR Puzzles

> **Companion Reference**: [`../topic_summaries/dilr/06_networks_routes_flows_and_quant_lr_puzzles.md`](../topic_summaries/dilr/06_networks_routes_flows_and_quant_lr_puzzles.md) | [`DILR_Archetype_Templates.md`](../high_recall/cheat_sheets/DILR_Archetype_Templates.md)

---

## Concept 1: Kirchhoff Node Flow Conservation ($\text{In} = \text{Out} + \text{Demand}$), Leaf Peeling & Pipe Slack

### 1. Concept & Invariant in Plain English
In any pipeline, traffic, or power network:
1. **Global Balance**: $\sum \text{Source Supply} = \sum \text{Town Demands}$.
2. **Node Conservation (Kirchhoff's Law)**: At every junction node $v$, total water flowing **in** equals total water consumed at $v$ **plus** total water flowing **out**:
   $$\sum \text{Inflow}(v) = \text{Demand}(v) + \sum \text{Outflow}(v)$$
3. **Pipe Slack**: $\text{Slack} = \text{Pipe Capacity} - \text{Actual Flow}$.
4. **Leaf-Peeling Order**: Never start in the middle of the web! Start at **degree-1 leaf nodes** (where only 1 pipe enters or leaves), lock that pipe, and peel inward!

### 2. When to Use It (Set / Question Cue)
- Pipeline diagrams with node demands and pipe capacities/slacks.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Source $S$ pumps $500\text{ L}$ into a network feeding towns $A, B, C$ with demands $D_A = 100$, $D_B = 150$, $D_C = ?$.
> - Pipes are $S \to A$, $S \to B$, $A \to B$ ($50\text{ L}$), and $A \to C$.
> - Every pipe has capacity $400\text{ L}$.
> *Find $D_C$, the flow in every pipe, and the slack in $S \to A$.*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Node Balance Table (Peel from Leaf $C \to B \to A$)**:
  ```text
  Step | Node / Global | Inflow            | Demand | Outflow      | Locked Value
  -----+---------------+-------------------+--------+--------------+----------------------------
   1   | Global Sum    | 500 (from S)      | 500    | --           | D_C = 500 - (100+150) = 250
   2   | Leaf Node C   | A->C              | 250    | 0            | Flow(A->C) = 250
   3   | Node B        | S->B + A->B (50)  | 150    | 0            | Flow(S->B) = 150 - 50 = 100
   4   | Node A        | S->A              | 100    | A->B(50)+250 | Flow(S->A) = 100 + 300 = 400
  ```
  - **Slack in $S \to A$** $= \text{Capacity} (400) - \text{Flow} (400) = \mathbf{0\text{ L}}$ (full capacity!).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting to include the local town's own **Demand** in $\text{Inflow} = \text{Demand} + \text{Outflow}$.

---

## Concept 2: Max-Flow / Min-Cut Bottleneck Theorem & Linear Station Segment Occupancy

### 1. Concept & Invariant in Plain English
1. **Max-Flow Min-Cut**: The maximum flow that can ever travel from Source $S$ to Sink $T$ equals the capacity of the **narrowest bottleneck cut** separating $S$ from $T$ (counting only edges directed from the $S$-side to the $T$-side).
2. **Linear Train Route ($A \to B \to C \to D \to E$)**:
   - A ticket from $A$ to $D$ occupies $1$ seat on **every intermediate segment** ($A\text{--}B$, $B\text{--}C$, and $C\text{--}D$).
   - **Station Conservation**: $\text{Occupancy}(C\text{--}D) - \text{Occupancy}(D\text{--}E) = (\text{Passengers Alighting at } D) - (\text{Passengers Boarding at } D)$!

### 2. When to Use It (Set / Question Cue)
- Train / bus multi-stop booking sets (`CAT 2025 DILR Slot 1 Set 4`) or max-capacity pipeline sets.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> A train runs $A \to B \to C \to D$. No one boards at $C$ (i.e., $CD = 0$). If segment $B\text{--}C$ has $180$ occupied seats and segment $C\text{--}D$ has $130$ occupied seats, how many passengers bought tickets whose destination was Station $C$ ($AC + BC$)?

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Segment-to-Node Peeling**:
  ```text
  Segment | Tickets Occupying Segment      | Count
  --------+--------------------------------+------
  B--C    | AC + AD + BC + BD              |  180
  C--D    |      AD      + BD + CD(=0)     |  130
  --------+--------------------------------+------
  Diff    | (B--C) - (C--D) = AC + BC      |   50
  ```
  - Tickets booked **to Station C** ($AC + BC$) $= 180 - 130 = \mathbf{50}$ in one subtraction!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Trying to solve for $AC$ and $BC$ individually when the question only asks for total passengers alighting at $C$ ($AC + BC$).

---

## Concept 3: Critical Path Method (CPM) Project Scheduling (Longest Path & Slack)

### 1. Concept & Invariant in Plain English
When a project has tasks with durations and prerequisites ("Task C can start only after both A and B finish"):
- **Minimum Time to Finish the Project** $= \text{Length of the **LONGEST** path}$ from Start to Finish! Why longest? Because you cannot declare the project done until the slowest prerequisite chain finishes!
- This longest path is called the **Critical Path**. Tasks on the Critical Path have **$0$ Slack**; tasks on shorter parallel branches have **Slack** $= (\text{Latest Finish}) - (\text{Earliest Finish})$.

### 2. When to Use It (Set / Question Cue)
- Project tables listing `Task | Duration (Days) | Prerequisites`.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> A project has 4 tasks:
> - `A` ($5$ days, no prerequisite)
> - `B` ($3$ days, no prerequisite)
> - `C` ($4$ days, prerequisite `A`)
> - `D` ($6$ days, prerequisites `B` and `C`)
> *Find the minimum project completion time and the slack of Task B.*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Forward & Backward Schedule Table**:
  ```text
  Task | Duration | Prereq | Earliest Start (ES) | Earliest Finish (EF) | Slack
  -----+----------+--------+---------------------+----------------------+-------------------
   A   |    5     |   --   |         0           |          5           | 0 (Critical!)
   B   |    3     |   --   |         0           |          3           | 9 - 3 = 6 days!
   C   |    4     |   A    |         5           |          9           | 0 (Critical!)
   D   |    6     |  B, C  |  max(3, 9) = 9      |         15           | 0 (Critical!)
  ```
  - **Minimum Completion Time**: Path $A \to C \to D = 5 + 4 + 6 = \mathbf{15\text{ days}}$.
  - **Slack of Task B**: Task D doesn't start until Day $9$ (because it has to wait for $C$ to finish at Day $9$). Since $B$ finishes at Day $3$, $B$ can be delayed by $9 - 3 = \mathbf{6\text{ days}}$ without delaying the project!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Taking the *shortest* path ($B \to D = 3 + 6 = 9$ days) as the minimum project completion time instead of the **longest prerequisite chain** ($15$ days).

---

## Concept 4: Sliding-Window Moving Averages ($x_{t+w} - x_t = w\Delta A$) & Truth-Teller Matrices

### 1. Concept & Invariant in Plain English
1. **Sliding-Window Telescope**: When a $w$-day moving average shifts forward by $1$ day (from $\text{Days } 1..w$ to $\text{Days } 2..w+1$), all middle days stay identical—only $\text{Day } 1$ drops out and $\text{Day } (w+1)$ enters:
   $$x_{t+w} - x_t = w \times (A_{\text{new}} - A_{\text{old}})$$
2. **Truth-Teller / Liar Hypothesis Table**: When *"Exactly $1$ of the $N$ suspects is telling the truth"*, test each suspect as the truth-teller in a column; the column where $(N - 1)$ statements are False and $1$ is True wins in 30 seconds!

### 2. When to Use It (Set / Question Cue)
- Consecutive multi-day/multi-month average tables or Truth/Liar puzzles.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> The 4-day average temperature for Mon–Thu is $30^\circ\text{C}$, and the 4-day average for Tue–Fri is $32^\circ\text{C}$. If Monday's temperature was $25^\circ\text{C}$, find Friday's temperature.

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Window Shift Comparison**:
  ```text
  Window 1 (Mon-Thu):  [Mon] + Tue + Wed + Thu         = 4 * 30 = 120
  Window 2 (Tue-Fri):          Tue + Wed + Thu + [Fri] = 4 * 32 = 128
  -------------------------------------------------------------------
  Subtract (W2 - W1):  Fri - Mon = 4 * (32 - 30) = +8  => Fri = 25 + 8 = 33
  ```

### 5. The 1 Common Mistake to Avoid
- **Trap**: Trying to solve for Tuesday, Wednesday, and Thursday individually—they cancel out completely!

---

## Concept 5: Pan-Balance Counterfeit Weighing ($3^k$) & Take-Away Game Modulo $(m + 1)$

### 1. Concept & Invariant in Plain English
1. **Pan Balance ($3^k$ Ternary Split)**: A two-pan balance has **3 outcomes**: Left heavy, Right heavy, or Equal. Divide $N$ coins into **3 nearly equal piles** ($A, B$ on the pans, $C$ on the table). In $k$ weighings, you can isolate 1 heavier coin out of up to **$3^k$ coins**!
2. **Subtraction / Take-Away Game (Remove $1$ to $m$ coins; last coin wins)**:
   - Group the pile into multiples of **$(m + 1)$**.
   - If $N$ is NOT a multiple of $(m + 1)$, the **1st player wins** by removing $r = N \bmod (m + 1)$ coins on Turn 1, leaving a multiple of $(m + 1)$ for the opponent!

### 2. When to Use It (Set / Question Cue)
- Coin weighing puzzles or 2-player stone/coin removal games with "optimal play".

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> A pile has $23$ stones. Players A and B take turns removing $1, 2, 3,$ or $4$ stones. The player who takes the last stone wins. If A goes first, how many stones should A remove on Turn 1 to guarantee a win?

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Backward Induction Modulo $(m + 1 = 5)$ Table**:
  ```text
  Stones Left | Losing Position (Multiple of 5) | Winning First Move for A
  ------------+---------------------------------+------------------------------------------
     0, 5     | 5 (Whoever faces 5 loses!)      | From 23: 23 = 4*5 + 3 => Remove 3 stones!
  10, 15, 20  | Multiples of 5                  | Leaves 20 for B; whenever B takes x, A takes (5-x)!
  ```
  - Since $m = 4$, magic modulus is $m + 1 = 5$. Since $23 \equiv 3 \pmod 5$, A removes **$3$ stones** (leaving $20$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: If the game says *"The player who takes the last stone **LOSES**"* (Misère rule), target **$1 \pmod{m + 1}$** ($1, 6, 11, 16, 21$) instead of $0 \pmod{m + 1}$ ($23 - 21 = \mathbf{2\text{ stones}}$)!
