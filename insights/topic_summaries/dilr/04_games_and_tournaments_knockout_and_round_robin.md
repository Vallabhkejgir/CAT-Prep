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
