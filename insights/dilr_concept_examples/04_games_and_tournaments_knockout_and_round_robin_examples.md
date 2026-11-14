# DILR 04 Concept & Grid-Evolution Examples: Games & Tournaments — Knockouts & Round-Robin Leagues

> **Companion Reference**: [`../topic_summaries/dilr/04_games_and_tournaments_knockout_and_round_robin.md`](../topic_summaries/dilr/04_games_and_tournaments_knockout_and_round_robin.md) | [`DILR_Archetype_Templates.md`](../high_recall/cheat_sheets/DILR_Archetype_Templates.md)

---

## Concept 1: Seeded Knockout Brackets — Match Count ($N - 1$), Seed Sum ($M + 1$) & Top-Down Tree

### 1. Concept & Invariant in Plain English
In a standard single-elimination knockout tournament with $N = 2^k$ players seeded $1$ (best) to $N$ (worst):
1. **Total Matches $= N - 1$**: Since every match sends $1$ loser home and $N - 1$ players must go home to leave $1$ champion, $16$ players always play **$15$ matches** ($8 + 4 + 2 + 1$).
2. **The Magic Seed-Sum Rule ($\text{Seed}_A + \text{Seed}_B = M + 1$)**: In any round where **$M$ players remain** (if there are no upsets), the two seeds playing each other always add up to **$M + 1$**:
   - **Finals ($M = 2$, Sum $= 3$)**: $1$ vs $2$
   - **Semi-Finals ($M = 4$, Sum $= 5$)**: $(1, 4)$ and $(2, 3)$
   - **Quarter-Finals ($M = 8$, Sum $= 9$)**: $(1, 8), (4, 5)$ in Half A; $(2, 7), (3, 6)$ in Half B
   - **Round 1 ($M = 16$, Sum $= 17$)**: $(1,16), (8,9), (4,13), (5,12)$ in Half A; $(2,15), (7,10), (3,14), (6,11)$ in Half B.

### 2. When to Use It (Set / Question Cue)
- *"16 (or 32 or 64) players seeded 1 to 16 play a knockout tournament where in each round the highest seed plays the lowest seed..."*

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> In a 16-player seeded knockout tournament with **no upsets**, find:
> (a) Who plays Seed $6$ in Round 1 and in the Quarter-Finals?
> (b) Which 4 seeds belong to the same Quarter-Bracket as Seed $4$?

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Top-Down Bracket Unfolding (Start from Final `1 vs 2` and split each seed $s \to (s,\; M+1-s)$)**:
  ```text
  Round            | Players (M) | Seed Sum (M+1) | Match Pairings
  -----------------+-------------+----------------+-----------------------------------------
  Final            |    M = 2    |    Sum = 3     | [1 vs 2]
  Semi-Finals      |    M = 4    |    Sum = 5     | [1 vs 4]               | [2 vs 3]
  Quarter-Finals   |    M = 8    |    Sum = 9     | [1v8] [4v5]            | [2v7] [3v6]
  Round 1          |   M = 16    |   Sum = 17     | (1,16)(8,9)(4,13)(5,12)| (2,15)(7,10)(3,14)(6,11)
  ```
  - **Part (a)**: In Round 1 ($M=16$, Sum $=17$), Seed $6$ plays $17 - 6 = \mathbf{\text{Seed } 11}$. In Quarter-Finals ($M=8$, Sum $=9$), Seed $6$ plays $9 - 6 = \mathbf{\text{Seed } 3}$.
  - **Part (b)**: Expand Seed $4$ at QF ($9 - 4 = 5 \implies \{4, 5\}$) and then at R1 ($17 - 4 = 13$, $17 - 5 = 12$) $\implies \mathbf{\{4, 5, 12, 13\}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Drawing Round 1 as $(1,16), (2,15), (3,14), (4,13)$ from top to bottom on the same side of the bracket—remember that Seeds $1$ and $2$ sit in **opposite halves**, and Seeds $1, 4$ vs. $2, 3$ only meet in the **Semi-Finals**!

---

## Concept 2: Knockout Upset Mechanics & Bracket Slot Inheritance

### 1. Concept & Invariant in Plain English
An **upset** happens when a worse seed (larger number, e.g., Seed $12$) beats a better seed (smaller number, e.g., Seed $5$).
**The Slot-Inheritance Rule**: When Seed $12$ upsets Seed $5$ in Round 1, Seed $12$ **steps into Seed $5$'s shoes** for the rest of the tournament! So in the Quarter-Finals, instead of Seed $4$ playing Seed $5$ ($4 + 5 = 9$), Seed $4$ now plays **Seed $12$**!

### 2. When to Use It (Set / Question Cue)
- *"Seed 13 reached the Semi-Finals, and there were only 2 upsets in the tournament..."*

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> In an 8-player seeded knockout tournament (Seeds $1$ to $8$: R1 has $M=8$, SF has $M=4$, Final has $M=2$), there were **exactly 2 upsets** in the entire tournament, and **Seed $6$ won the tournament**? Wait: to win 3 rounds, Seed $6$ must win 3 matches! Can Seed $6$ win a 3-round tournament with only 2 upsets? Let's check: in R1, $6$ beats $3$ (**Upset #1**); in SF, $6$ plays the winner of $(2, 7)$—if $7$ upset $2$ (**Upset #2**), then in SF **Seed $6$ beats Seed $7$ WITHOUT an upset** ($6 < 7$!), and in the Final $6$ beats $1$ (**Upset #3**). So reaching the Final takes only **2 upsets**! Let's solve: *Seed $6$ reached the Final with only $1$ upset in Half B? No, $6$ beating $3$ and $2$ is $2$ upsets!*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **8-Player Bracket Evolution When Seed $6$ Reaches the Final**:
  ```text
  Half / Round | Normal Match (No Upset) | Actual Match (Seed 6 Reaches Final)
  -------------+-------------------------+------------------------------------
  R1 (Sum = 9) | (3 vs 6) and (2 vs 7)   | 6 beats 3 (Upset #1: 6 inherits #3's slot!)
               |                         | 2 beats 7 (Normal)
  SF (Sum = 5) | (2 vs 3's slot)         | 6 beats 2 (Upset #2: 6 inherits #2's slot!)
  Final (Sum=3)| (1 vs 2's slot)         | 1 beats 6 (Normal)
  ```
- **30-Second Invariant / Ratio Shortcut**:
  - To find who a Cinderella player (like Seed $6$) played in each round, just replace its seed with the **top seed of the mini-bracket it conquered**: after R1, $6$ acts as **$3$**; after SF, $6$ acts as **$2$**!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Thinking that if Seed $7$ plays Seed $6$ in the Semi-Final and Seed $6$ wins, that counts as an upset—since $6 < 7$, **Seed $6$ beating Seed $7$ is NOT an upset**!

---

## Concept 3: Round-Robin Leagues — Match Count $\binom{n}{2}$, Win-Loss-Draw & Points Conservation

### 1. Concept & Invariant in Plain English
In a single round-robin league where $n$ teams each play every other team once:
1. **Total Matches**: $M = \binom{n}{2} = \frac{n(n-1)}{2}$ ($4\text{ teams} \to 6\text{ matches}$; $5\text{ teams} \to 10\text{ matches}$; $6\text{ teams} \to 15\text{ matches}$).
2. **Win-Loss-Draw Balance** (if $D$ matches end in a draw):
   - $\sum \text{Wins} = \sum \text{Losses} = M - D$.
   - $\sum (\text{Draws column in table}) = \mathbf{2D}$ (each drawn match puts a `1` in **both** teams' Draw column, so the Draw column sum is always **even**!).
3. **Total Points Sum**:
   - **2–1–0 System**: Every match gives $2$ points total $\implies \sum \text{Points} = 2M$.
   - **3–1–0 System**: Each non-draw gives $3$ pts, each draw gives $1+1=2$ pts $\implies \sum \text{Points} = \mathbf{3M - D}$.

### 2. When to Use It (Set / Question Cue)
- Any league points table with columns `Played | Won | Drawn | Lost | Points`.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Five teams (A, B, C, D, E) play a single round-robin tournament ($3$ points for a Win, $1$ point for a Draw, $0$ for a Loss). At the end of the tournament, the points of A, B, C, D are $10, 7, 5, 4$, and only $3$ matches in the entire tournament ended in a draw. Find Team E's points and Team A's exact $(W, D, L)$ record.

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Points Conservation Table ($n = 5 \implies M = \binom{5}{2} = 10$ matches, $4$ matches per team)**:
  ```text
  Team | Played | W | D | L | Points | Deduction
  -----+--------+---+---+---+--------+----------------------------------------
   A   |   4    | 3 | 1 | 0 |   10   | 10 pts in 4 games => uniquely 3W, 1D, 0L!
   B   |   4    | 2 | 1 | 1 |    7   | 7 pts in 4 games  => uniquely 2W, 1D, 1L!
   C   |   4    | 1 | 2 | 1 |    5   | 5 pts in 4 games  => uniquely 1W, 2D, 1L!
   D   |   4    | 1 | 1 | 2 |    4   | 4 pts in 4 games  => uniquely 1W, 1D, 2L!
   E   |   4    | 0 | 1 | 3 |  [ 1]  | Total Pts = 3(10) - 3 = 27 => E = 27 - 26 = 1!
  -----+--------+---+---+---+--------+----------------------------------------
  Sum  |  20    | 7 | 6 | 7 |   27   | Sum(W)=7, Sum(D)=2*3=6, Sum(Pts)=30-3=27
  ```
- **30-Second Invariant / Ratio Shortcut**:
  - Total points across all $10$ matches with $D = 3$ draws is $3(10) - 3 = 27$. Subtracting $10 + 7 + 5 + 4 = 26$ gives **Team E $= 1$ point** (`0W, 1D, 3L`) in 5 seconds!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Thinking $D = 3$ drawn matches means the `D` (Draws) column in the table adds up to $3$ instead of **$2 \times 3 = 6$**!

---

## Concept 4: Goal Difference Conservation ($\sum \text{GF} = \sum \text{GA}$) & Low-Score Match Reconstruction

### 1. Concept & Invariant in Plain English
Every goal scored by one team (`GF`) is a goal conceded by its opponent (`GA`), so $\sum \text{GF} = \sum \text{GA}$.
**The Low-Goal Lock Rule**: Always attack teams with **`GF` or `GA` equal to $0, 1,$ or $2$ first**!
- If a team has `3 Wins, 0 Draws, 0 Losses` with `GF = 3, GA = 0`, it **must** have won all three of its matches by the exact scoreline **`1–0, 1–0, 1–0`**!
- If a team has `0 Wins, 2 Draws, 1 Loss` with `GF = 0, GA = 1`, its two draws **must** be **`0–0, 0–0`** and its loss **must** be **`0–1`**!

### 2. When to Use It (Set / Question Cue)
- Football / Hockey tournament tables with `GF (Goals For)` and `GA (Goals Against)` columns.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Three teams (A, B, C) play each other once (2 matches per team).
> - Team A: `2 Wins, 0 Draws, 0 Losses`, `GF = 3, GA = 0`.
> - Team B: `0 Wins, 1 Draw, 1 Loss`, `GF = 1, GA = 2`.
> *Find the exact scoreline of every match (A vs B, A vs C, B vs C).*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Stage 1 (Analyze Team B: 1 Draw, 1 Loss, GF = 1, GA = 2)**:
  - Since A won both its matches with `GA = 0`, A beat B and A beat C without conceding any goal!
  - So B's **Loss** was against A, and since A conceded $0$ goals (`GA = 0`), B scored **$0$ goals against A**!
  - Therefore, B's $1$ goal (`GF = 1`) was scored in its **Draw against C** $\implies$ **`B vs C = 1–1`**!
- **Stage 2 (Lock Remaining Scorelines)**:
  - Since B conceded $2$ goals total (`GA = 2`) and conceded $1$ goal in `B vs C (1–1)`, B conceded $2 - 1 = 1$ goal against A $\implies$ **`A vs B = 1–0`**!
  - Since A scored $3$ goals total (`GF = 3`) and scored $1$ against B, A scored $3 - 1 = 2$ goals against C $\implies$ **`A vs C = 2–0`**!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Trying to guess high-scoring teams (`GF = 7, GA = 5`) first instead of locking the `0`-goal and `1`-goal cells first!

---

## Concept 5: Top-$k$ Qualification Extrema (Guarantee vs. Possibly Qualify)

### 1. Concept & Invariant in Plain English
When $n$ teams play a single round-robin (no draws, $1$ win per match, total wins $= \binom{n}{2}$) and the **Top $k$ teams advance**:
1. **To GUARANTEE advancing (Worst-Case Tie)**: Assume the top $(k + 1)$ teams beat all the bottom $(n - k - 1)$ teams AND split their head-to-head matches equally! Each of those $(k+1)$ teams gets $(n - k - 1) + \lfloor \frac{k}{2} \rfloor$ wins—and one of them still gets eliminated on tie-breaker! Add $+1$ to **guarantee** advancing.
2. **To POSSIBLY advance (Best-Case Tie)**: Assume the top $(k - 1)$ teams win every match they can, and the remaining $(n - k + 1)$ teams tie equally at the bottom with $\lceil \frac{n - k}{2} \rceil$ wins!

### 2. When to Use It (Set / Question Cue)
- *"8 teams play a round-robin; top 4 advance to the semi-finals. What is the minimum wins needed to guarantee qualification (or to possibly qualify)?"*

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> In a 6-team single round-robin tournament ($15$ matches, no draws, each team plays $5$ matches), the **Top 2** teams qualify for the Final. Find:
> (a) The maximum number of wins a team can have and **still fail** to qualify.
> (b) The minimum number of wins with which a team can **still possibly** qualify.

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Worst-Case & Best-Case Win Distributions (Total Wins $= 15$)**:
  ```text
  Scenario                                | Rank 1 | Rank 2 | Rank 3 (Out!) | Rank 4 | Rank 5 | Rank 6 | Sum
  ----------------------------------------+--------+--------+---------------+--------+--------+--------+----
  (a) 3-Way Tie at Top (Max Fail)         |   4    |   4    |   4 (Fails!)  |   1    |   1    |   1    | 15
  (b) 5-Way Tie for 2nd Place (Min Pass)  |   5    | 2 (In!)|   2           |   2    |   2    |   2    | 15
  ```
  - **Part (a)**: Three teams can tie at **$4$ wins each** (beating the bottom 3 teams and going 1–1 in their 3-team circle), so a team with **$4$ wins** can still be eliminated! ($5$ wins guarantees qualification.)
  - **Part (b)**: Rank 1 goes $5\text{–}0$, and the other 5 teams tie at **$2$ wins each** ($5 + 2 + 2 + 2 + 2 + 2 = 15$), so a team can qualify with just **$2$ wins**!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Proposing a win distribution whose sum does not equal $\binom{n}{2} = 15$ or where $3$ teams have $5$ wins each (impossible since they play each other!).
