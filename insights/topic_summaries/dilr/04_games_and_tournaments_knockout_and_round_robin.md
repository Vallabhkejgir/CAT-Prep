# DILR 04: Games & Tournaments — Seeded Knockouts & Round-Robin Leagues

**Canonical Taxonomy Mapping**: `DILR > Games & Tournaments`  
**Weightage**: ~15–25% of DILR (1 set in almost every CAT paper)  
**Priority Tier**: Tier 1 (Highest-ROI Algorithmic DILR Topic)

---

## 1. Visual & Structural Anatomy

Games & Tournaments sets are pure mathematical invariants disguised as sports stories. Once you know the equations for **Seeded Knockout Brackets** and **Round-Robin League Tables**, these sets become the fastest 10-minute 100%-accuracy solves on the paper.

### 1.1 Knockout (Single-Elimination) Brackets ($N = 2^k$ Players, Seeds $1$ to $2^k$)
- **Total Matches** to crown a champion $= N - 1$ (since every match eliminates exactly $1$ player).
- **Number of Rounds** $= k = \log_2 N$:
  - $N = 16 \implies 4\text{ rounds}$: R1 ($8$ matches), QF ($4$ matches), SF ($2$ matches), Final ($1$ match).
  - $N = 32 \implies 5\text{ rounds}$ ($16 + 8 + 4 + 2 + 1 = 31$ matches).
  - $N = 64 \implies 6\text{ rounds}$ ($32 + 16 + 8 + 4 + 2 + 1 = 63$ matches).
- **Standard Seeding Pairing Rule**:
  In any round containing $M$ players (assuming **no upsets** in prior rounds), if the remaining seeds are $1, 2, \dots, M$, the paired seeds in every match of that round sum to **$M + 1$**:
  $$\text{Seed}_A + \text{Seed}_B = M + 1 = 2^{k - r + 1} + 1$$
  - For $N = 16$:
    - **Round 1 ($M = 16$, sum $= 17$)**: $(1,16), (2,15), (3,14), (4,13), (5,12), (6,11), (7,10), (8,9)$.
    - **Quarter-Finals ($M = 8$, sum $= 9$)**: $(1,8), (2,7), (3,6), (4,5)$.
    - **Semi-Finals ($M = 4$, sum $= 5$)**: $(1,4), (2,3)$.
    - **Finals ($M = 2$, sum $= 3$)**: $(1,2)$.
- **Upset Mechanics**:
  - An **upset** occurs when a numerically higher seed number (weaker player, e.g., Seed $12$) defeats a lower seed number (stronger player, e.g., Seed $5$).
  - When Seed $12$ upsets Seed $5$ in R1, **Seed $12$ inherits Seed $5$'s bracket slot** for all subsequent rounds!

---

### 1.2 Round-Robin Leagues ($n$ Teams, Each Plays Every Other Team $m$ Times)
- **Total Matches**: $M = m \cdot \binom{n}{2} = \frac{m \cdot n(n-1)}{2}$ (for single round-robin $m=1$ with $n=6$ teams: $\binom{6}{2} = 15$ matches).
- **Conservation Laws**:
  1. $\sum \text{Wins} = \sum \text{Losses} = M - D$ (where $D =$ number of drawn matches; Note: $\sum \text{Draws Column} = 2D$ because each drawn match gives $1$ draw to **two** teams!).
  2. $\sum \text{Goals For (GF)} = \sum \text{Goals Against (GA)}$, so $\sum \text{Goal Difference (GD)} = 0$.
  3. **Total Points Conservation**:
     - **2–1–0 System** (Win $= 2$, Draw $= 1$, Loss $= 0$): Every match awards exactly $2$ points regardless of result $\implies \sum \text{Points} = 2M$.
     - **3–1–0 System** (Win $= 3$, Draw $= 1$, Loss $= 0$): A decisive match awards $3$ points; a draw awards $1 + 1 = 2$ points $\implies \sum \text{Points} = 3M - D$.

---

## 2. Green Flags vs. Red Flags

- **Green Flags**:
  - Standard $16$- or $32$-player seeded knockout tournament asking who played whom given $2$–$3$ upsets.
  - $5$- or $6$-team round-robin table with partially filled $W, D, L, GF, GA, \text{Points}$.
- **Red Flags**:
  - Multi-stage Swiss-system or variable-point bonus rules with $> 8$ teams and no total conservation anchor.

---

## 3. Scratchpad Representation Template

### A. 16-Player Bracket Tree (Draw Top-Down from Final!)
To build any standard seeded bracket in **15 seconds**, start from the Final $(1, 2)$ and expand each seed $s$ into $(s,\; M + 1 - s)$:

```text
FINAL (Sum=3):              [1]                 vs                 [2]
                         /       \                              /       \
SF (Sum=5):           [1]         [4]                        [2]         [3]
                     /   \       /   \                      /   \       /   \
QF (Sum=9):        [1]   [8]   [4]   [5]                  [2]   [7]   [3]   [6]
                   / \   / \   / \   / \                  / \   / \   / \   / \
R1 (Sum=17):      1 16  8  9  4 13  5 12                 2 15  7 10  3 14  6 11
                  (Half A: {1,4,5,8,9,12,13,16})         (Half B: {2,3,6,7,10,11,14,15})
```

### B. Round-Robin Cross-Match Matrix + Points Table
```text
      A   B   C   D   E   |  W   D   L  | GF  GA  GD | Pts
  A [ X                   |             |            |     ]
  B [     X               |             |            |     ]
  C [         X           |             |            |     ]
  D [             X       |             |            |     ]
  E [                 X   |             |            |     ]
  ------------------------+-------------+------------+-----
  TOTAL (M = 10 matches)  | 10-D 2D 10-D|  S   S   0 | 30-D
```

---

## 4. Anchor Clue & Case-Splitting Rules

1. **Bracket Slot Inheritance Rule**:
   - In a $16$-player knockout, if Seed $11$ reaches the Semi-Finals, immediately look at $11$'s R1 slot: $17 - 11 = \text{Seed }6$, and in QF $6$'s slot plays $9 - 6 = \text{Seed }3$ (or $3$'s R1 opponent $17 - 3 = 14$). You instantly know $11$ beat $6$ in R1 and beat $(3 \text{ or } 14)$ in QF!
2. **Low-Scoring Goal/Run Reconstruction**:
   - If a team played $4$ matches with $W = 3, D = 1, L = 0$ and $\text{GF} = 3, \text{GA} = 0$, there is **only one way** to win 3 matches and draw 1 match with 3 goals scored and 0 conceded: three $1\text{–}0$ wins and one $0\text{–}0$ draw! Always lock teams with $\text{GF}$ or $\text{GA} \in \{0, 1, 2\}$ first.

---

## 5. Mathematical Invariants: Qualification Extrema (Top $k$ Out of $n$ Teams Advance)

In a single round-robin among $n$ teams ($2$ points per win, $0$ per loss, no draws; modify accordingly for 3-point wins):
1. **Minimum Wins to GUARANTEE Qualification in Top $k$** (even in the worst-case $(k+1)$-way tie):
   - Set the bottom $n - (k + 1)$ teams to lose all matches against the top $(k + 1)$ teams, and make the top $(k + 1)$ teams tie equally among themselves:
     $$W_{\text{max-fail}} = \left\lfloor (n - k - 1) + \frac{k}{2} \right\rfloor \implies W_{\text{guarantee}} = W_{\text{max-fail}} + 1$$
2. **Minimum Wins to POSSIBLY Qualify in Top $k$** (best-case tie-break in your favor):
   - Give the top $k - 1$ teams all possible wins, and make the remaining $n - (k - 1)$ teams tie equally at the lowest possible win count:
     $$W_{\text{possible}} = \left\lceil \frac{n - k}{2} \right\rceil$$

| $n = 6$ Teams (5 matches each, 2 pts/win) | Top $k = 2$ Advance | Top $k = 4$ Advance |
| :--- | :--- | :--- |
| **Max wins a team can get & STILL be eliminated** | $3$ wins (3-way tie at $4, 4, 4$ wins; bottom 3 have $1, 1, 1$) $\implies$ wait: $\lfloor 3 + 1 \rfloor = 4$ wins! | $2$ wins (5-way tie at $2$ wins when #1 has $5$ wins) |
| **Min wins to GUARANTEE qualification (without tie-breaker)** | $5$ wins (since 3 teams can tie at $4$ wins: $4+4+4+1+1+1=15$) | $3$ wins |
| **Min wins to POSSIBLY qualify (with favorable tie-breaker)** | $2$ wins (1 team has $5$ wins; 5 teams tie at $2$ wins: $5+2+2+2+2+2=15$) | $1$ win (3 teams have $4,4,4$; 3 teams tie at $1,1,1$) |

---

## 6. Solved Archetype Walkthrough: 16-Player Knockout with Upsets

> **Set Scenario**: 16 players seeded $1$ to $16$ play a standard single-elimination knockout tournament.
> 1. There were exactly $4$ upsets in the entire tournament (an upset is when a worse seed beats a better seed).
> 2. Seed $1$ won the tournament without facing any player seeded $4$ or better in any round.
> 3. Seed $11$ reached the Finals.
> *Who did Seed $11$ defeat in the Quarter-Finals and Semi-Finals, and which upsets occurred?*

### Step-by-Step Execution
1. **Locate Seed $11$ in Half B**:
   - Half B has R1 pairs $(2,15), (7,10)$ in Quarter-Bracket $B_1$ and $(3,14), (6,11)$ in Quarter-Bracket $B_2$.
   - For Seed $11$ to reach the Finals, Seed $11$ MUST win R1, QF, and SF (3 matches).
   - In R1, $11$ plays $6$ ($11$ beats $6$ $\to$ **Upset #1**).
   - In QF, $11$ plays the winner of $(3, 14)$ ($11$ beats $3$ or $14$ $\to$ if $3$ beat $14$, $11$ beating $3$ is **Upset #2**; if $14$ beat $3$, $14$ beating $3$ is **Upset #2**).
   - In SF, $11$ plays the winner of Quarter-Bracket $B_1$ $\{2, 15, 7, 10\}$. Whoever emerges from $\{2, 7, 10, 15\}$, either $11$ beats $\{2, 7, 10\}$ (**Upset #3**) or $15$ had already caused at least two upsets in $B_1$.
2. **Count Upsets Required in Half A (Clue 2: Seed $1$ never faced $\le 4$, so Seed $1$ did NOT play Seed $4$ in SF)**:
   - Since Seed $1$ won all 4 of its matches in Half A, Seed $4$ MUST have been upset in either R1 (by $13$) or QF (by $5$ or $12$) $\to$ **at least $1$ upset in Half A (Upset #4)**!
3. **Deduce Exact Upsets Since Total Upsets $= 4$**:
   - Half A uses at least $1$ upset, and Half B needs at least $3$ upsets for Seed $11$ to reach the Finals.
   - Therefore, Half A has **exactly $1$ upset** and Half B has **exactly $3$ upsets**!
   - In Half A (1 upset): Seed $5$ beat $12$ in R1 (no upset), and **Seed $5$ upset Seed $4$ in QF** (1 upset), then Seed $1$ beat Seed $5$ in SF.
   - In Half B (3 upsets): No extra upsets can happen outside $11$'s path! Thus:
     - $3$ beat $14$ in R1 (no upset), and **$11$ upset $3$ in QF**.
     - $2$ beat $15$ and $7$ beat $10$ in R1, $2$ beat $7$ in QF (no upsets), and **$11$ upset $2$ in SF**!
   - **Result**: Seed $11$ defeated **Seed $6$ (R1), Seed $3$ (QF), and Seed $2$ (SF)** before losing to Seed $1$ in the Final!

---

## 7. Active-Recall Drills

<details><summary>Q1: In a 64-player standard seeded knockout tournament with no upsets before the Quarter-Finals, who plays Seed 6 in the Quarter-Finals?</summary>
A: Quarter-Finals have M = 8 players remaining, so paired seeds sum to M + 1 = 9. Therefore Seed 6 plays Seed (9 - 6) = Seed 3.
</details>

<details><summary>Q2: In a 32-player seeded knockout tournament, what is the worst (numerically largest) seed that can win the tournament if there are at most 2 upsets in the entire tournament?</summary>
A: With 2 upsets, a player can win via 2 upsets of its own (or 1 upset + 1 pre-cleared bracket). In a 32-player bracket, to win 5 rounds with only 2 upsets, the winner must be the better seed in 3 of its 5 matches! Wait: to be the favorite in R1, R2, R3 (first 3 rounds, M = 32, 16, 8), the player must be seeded in the top 4 (Seed 4 beats 29, 13, 5 without upset, then upsets 1 and 2 in SF and Final)! Can Seed 5 do it? Seed 5 beats 28 and 12 (2 wins), then if Seed 4 was already upset by 29 (1 upset), Seed 5 beats 29 without an upset in R3, then upsets 1 in SF... wait: still needs an upset in Final (total 3 upsets!). Thus the worst seed that can win with at most 2 upsets is Seed 4!
</details>

<details><summary>Q3: In an 8-team single round-robin football league (3 pts for win, 1 pt for draw, 0 for loss), the sum of points of all 8 teams at the end of the tournament is 76. How many matches ended in a draw?</summary>
A: Total matches M = C(8, 2) = 28. Using Total Points = 3M - D -> 76 = 3(28) - D = 84 - D -> D = 8 drawn matches.
</details>

<details><summary>Q4: In a 6-team round-robin tournament (no draws), can two teams both finish with 5 wins?</summary>
A: No! Those two teams must play each other, so at least one of them must lose at least 1 match. At most one team can finish 5-0.
</details>

<details><summary>Q5: In a 16-player seeded knockout, which seeds are in the same Quarter-Bracket (top-fourth of the draw) as Seed 3?</summary>
A: Expand backwards from QF (sum=9): 3 is paired with 9 - 3 = 6. Expand R1 (sum=17): 3 is paired with 17 - 3 = 14, and 6 is paired with 17 - 6 = 11. Thus the Quarter-Bracket is {3, 6, 11, 14}.
</details>

---

## CAT 2025 PYQ Edge Examples & Newly Surfaced Patterns

### Newly Surfaced Sub-Topic Variants & Pattern Triggers (CAT 2025)
- **Turn-Based State-Transition & Modular Buck Games (`CAT_2025_DILR_Slot_1` `SET1` & `CAT_2025_DILR_Slot_3` `SET4`)**: Game-theoretic turn-by-turn movement on circular boards where players transition to empty seats or pass the buck $\pm 1, \pm 2 \pmod 7$ until a termination state is reached.
- **5-Round 2-Player Matrix Game with Bounded Multiset Sums (`CAT_2025_DILR_Slot_1` `SET5`)**: In the 5-round Foot-Tapping game, each column is a permutation of $\{1,2,3,4,5\}$ except one repeated number, bounding 4-player row sums to $\{7,8,9\}$ and forcing anti-symmetric tie-breakers.
- **Competitive Multi-Stage Puzzle Race Tracking (`CAT_2025_DILR_Slot_3` `SET3`)**: Tracking lead changes and category completion times across 5 contestants via cumulative step functions.

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

#### CAT2025_S3_DILR_Q10 (`CAT_2025_DILR_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Cumulative step-function progress charts — *Reading cumulative step functions at a vertical time slice (t = 20)*
- **Verified Answer**: `(B) Koushik` (At t = 20 minutes on the left chart ('All puzzles'), Koushik (green curve) is at 7 puzzles (having solved Puzzle 7 at t = 19), whereas Chandranath is at 5, Anirbid is at 5, and Suranjan is at 4.)
- **Mental Trigger (`See X -> Do Y`)**: Look vertically above Time = 20 on the 'All puzzles' chart: the highest step-line is Green (Koushik) at y = 7!
- **First-Principles Method**: At Time = 20 min, reading the vertical slice on the 'All puzzles' chart gives: Koushik = 7 (completed at min 19), Chandranath = 5 (completed at min 17, 6th at min 21), Anirbid = 5 (completed at min 19), Suranjan = 4 (completed at min 18). Thus Koushik had solved the largest number of puzzles.
- **30-Second Exam-Hall Speed Shortcut**: Direct visual read at t = 20 -> Green line (Koushik) is highest at 7 puzzles.
- **Trap Alert & Boundary Condition**: Although Chandranath wins the overall race (finishing Puzzle 10 at t = 30 vs Koushik at t = 31), Koushik leads at t = 20!

#### CAT2025_S3_DILR_Q11 (`CAT_2025_DILR_Slot_3` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Cumulative step-function progress charts — *Aligning cumulative total vs category-subset step functions to extract individual task duration*
- **Verified Answer**: `2` (From the right chart ('Visual puzzles'), Suranjan (blue) finishes Visual Puzzle 3 at t = 28 min. On the left chart ('All puzzles'), Suranjan finishes a puzzle at t = 28 min (Puzzle 8), having finished the previous puzzle (Puzzle 7) at t = 26 min. Since a competitor gets access to a puzzle as soon as they solve the previous puzzle, Suranjan took 28 - 26 = 2 minutes to solve the third visual puzzle.)
- **Mental Trigger (`See X -> Do Y`)**: Find when Suranjan's Visual count jumps from 2 to 3 (at t = 28 min), then look at the 'All puzzles' chart at t = 28 min (Puzzle 8) and subtract the completion time of Puzzle 7 (t = 26 min) -> 28 - 26 = 2 min!
- **First-Principles Method**: Every jump in the 'Visual puzzles' chart coincides with a jump in the 'All puzzles' chart. For Suranjan, the jump to 3 visual puzzles occurs at t = 28 min, which corresponds to Puzzle 8 on the 'All puzzles' chart. Suranjan completed Puzzle 7 at t = 26 min, so he spent 28 - 26 = 2 minutes on Puzzle 8.
- **30-Second Exam-Hall Speed Shortcut**: Time of Visual #3 completion (28) minus Time of previous All-Puzzle completion (26) = 2 minutes.
- **Trap Alert & Boundary Condition**: Never subtract the completion time of Visual #2 (t = 18) from Visual #3 (t = 28) — that 10-minute gap includes Puzzles 5, 6, and 7 (which were number-based puzzles)!

#### CAT2025_S3_DILR_Q12 (`CAT_2025_DILR_Slot_3` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Cumulative step-function progress charts — *Sequence classification by matching jump timestamps between Total and Subset step charts*
- **Verified Answer**: `6` (Comparing jump times for any competitor (e.g., Koushik): All-puzzles jumps occur at t = 2, 4, 7, 12, 14, 16, 19, 25, 29, 31 (for Puzzles 1..10), while Visual-puzzles jumps occur at t = 2, 12, 25, 29 (which are Puzzles 1, 4, 8, 9). Thus Number-based puzzles are at positions 2, 3, 5, 6, 7, 10. The 4th number-based puzzle is at position 6.)
- **Mental Trigger (`See X -> Do Y`)**: Track Koushik's jumps: Visual jumps at t = 2 (P1), 12 (P4), 25 (P8), 29 (P9) -> non-visual (number-based) puzzles are P2, P3, P5, P6 (4th!), P7, P10!
- **First-Principles Method**: Since all competitors solve the 10 puzzles in the exact same sequence, match the jump timestamps of any single competitor across the two charts. For Koushik, Puzzles 1..10 finish at minutes (2, 4, 7, 12, 14, 16, 19, 25, 29, 31), and Visual Puzzles 1..4 finish at minutes (2, 12, 25, 29). Hence Puzzles 1, 4, 8, 9 are visual, and Puzzles 2, 3, 5, 6, 7, 10 are number-based. The 4th number-based puzzle is #6.
- **30-Second Exam-Hall Speed Shortcut**: Up to Puzzle 6, exactly 2 visual puzzles (P1 at t=2 and P4 at t=12) have been solved, so Puzzle 6 is the (6 - 2) = 4th number-based puzzle!
- **Trap Alert & Boundary Condition**: Using K_number(n) = n - K_visual(n) gives 6 - 2 = 4 immediately at n = 6.

#### CAT2025_S3_DILR_Q13 (`CAT_2025_DILR_Slot_3` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Cumulative step-function progress charts — *Complementary duration sum (Total Time - Visual Time = Number-Based Time)*
- **Verified Answer**: `(C) 4.0 minutes` (Anirbid (red) finishes all 10 puzzles at t = 37 min. His times on the 4 visual puzzles are: P1 (0->4 = 4 min), P4 (11->14 = 3 min), P8 (27->29 = 2 min), P9 (29->33 = 4 min), totaling 4 + 3 + 2 + 4 = 13 min. Thus his total time on the 6 number-based puzzles is 37 - 13 = 24 min, giving an average of 24 / 6 = 4.0 minutes.)
- **Mental Trigger (`See X -> Do Y`)**: Instead of summing 6 number-based puzzles, sum the 4 visual puzzles (4 + 3 + 2 + 4 = 13 min), subtract from Anirbid's finish time (37 - 13 = 24 min), and divide by 6 -> 24/6 = 4.0 min!
- **First-Principles Method**: Anirbid's completion times for Puzzles 1..10 are (4, 9, 11, 14, 19, 22, 27, 29, 33, 37). Durations of the 6 number-based puzzles (P2, P3, P5, P6, P7, P10) are (9-4)=5, (11-9)=2, (19-14)=5, (22-19)=3, (27-22)=5, and (37-33)=4. Sum = 5 + 2 + 5 + 3 + 5 + 4 = 24 minutes. Average = 24 / 6 = 4.0 minutes.
- **30-Second Exam-Hall Speed Shortcut**: Total time (37) - Visual durations (4 + 3 + 2 + 4 = 13) = 24 min across 6 number-based puzzles -> 24 / 6 = 4.0 minutes (Option C).
- **Trap Alert & Boundary Condition**: There are 6 number-based puzzles (and 4 visual puzzles), not 5!

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
