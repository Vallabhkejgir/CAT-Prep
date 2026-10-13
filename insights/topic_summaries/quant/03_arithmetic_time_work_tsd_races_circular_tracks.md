# QA 03: Arithmetic — Time & Work, Pipes & Cisterns, Time Speed Distance, Races & Circular Tracks

**Canonical Taxonomy Mapping**: `QA > Arithmetic > Time & Work, Pipes & Cisterns`, `Time, Speed & Distance (TSD)`  
**Weightage**: ~12–15% of QA (3–4 questions per slot)  
**Priority Tier**: Tier 1 (High-Yield Core)

---

## 1. 30-Second Concept & Formula Blueprint

### 1.1 Time & Work, Pipes & Cisterns
- **LCM Total-Work Method**: Set Total Work $W = \text{LCM}(t_1, t_2, \dots, t_k)$ units. Individual daily efficiency $e_i = \frac{W}{t_i}$ units/day.
- **Man-Days-Hours Formula**:
  $$\frac{M_1 D_1 H_1 E_1}{W_1} = \frac{M_2 D_2 H_2 E_2}{W_2}$$
- **Extra Time Over Combined Time $T_{AB}$**:
  If $A$ takes $a$ days more than $(A+B)$ together, and $B$ takes $b$ days more than $(A+B)$ together:
  $$T_{AB} = \sqrt{ab}$$
- **Alternating Pipes with Negative Work (Monkey Climbing / Cistern Emptying Trap)**:
  If Pipe $A$ fills $+p$ units in hour 1 and Pipe $B$ empties $-q$ units in hour 2 (net $+p-q$ per 2-hour cycle) for tank capacity $W$:
  1. Reserve the **positive peak** $p$ from $W$: compute cycles required to reach at least $W - p$:
     $$N_{\text{cycles}} = \left\lceil \frac{W - p}{p - q} \right\rceil$$
  2. Work done in $N_{\text{cycles}}$ is $N_{\text{cycles}}(p - q)$. The remaining $W - N_{\text{cycles}}(p - q)$ units are filled by Pipe $A$ in the final fractional turn **before** Pipe $B$ opens.

---

### 1.2 Time, Speed & Distance (TSD), Trains, Boats & Escalators
- **Proportionality Laws**:
  - Constant Distance ($D$ fixed): $S_1 T_1 = S_2 T_2 \implies \frac{S_1}{S_2} = \frac{T_2}{T_1}$. If speed changes by $\frac{a}{b}$, time changes by $\frac{-a}{a+b}$.
  - Constant Time ($T$ fixed, e.g., simultaneous start to first meeting): $\frac{D_1}{D_2} = \frac{S_1}{S_2}$.
- **Average Speed**:
  - General: $S_{\text{avg}} = \frac{\text{Total Distance}}{\text{Total Time}}$
  - Equal distances at $s_1, s_2$: Harmonic Mean $S_{\text{avg}} = \frac{2s_1 s_2}{s_1 + s_2}$
  - Equal time intervals at $s_1, s_2$: Arithmetic Mean $S_{\text{avg}} = \frac{s_1 + s_2}{2}$
- **Radha–Shyam Post-Meeting Theorem**:
  $A$ and $B$ start simultaneously from $P$ and $Q$ toward each other, meet at $M$, and then take $t_A$ and $t_B$ hours respectively to reach $Q$ and $P$:
  $$\frac{S_A}{S_B} = \sqrt{\frac{t_B}{t_A}}, \quad \text{Time to meet } t_{\text{meet}} = \sqrt{t_A \cdot t_B}$$
- **Boats & Streams**:
  $$S_D = u + v, \quad S_U = u - v \iff u = \frac{S_D + S_U}{2}, \quad v = \frac{S_D - S_U}{2} \quad (u > v > 0)$$
- **Escalators (Visible Steps Invariant)**:
  If an escalator has $N$ visible steps and moves at $e$ steps/sec, while a person takes $S_p$ steps in time $t$ (or walks at $p$ steps/sec):
  - Moving **with** the escalator: $N = S_p + e \cdot t$
  - Moving **against** the escalator: $N = S_p - e \cdot t$

---

### 1.3 Linear Races & Circular Tracks
- **Linear Races (Length $L$)**:
  - "$A$ beats $B$ by $d$ meters": When $A$ covers $L$, $B$ covers $L - d \implies \frac{S_A}{S_B} = \frac{L}{L - d}$.
  - "$A$ beats $B$ by $t$ seconds": $B$ covers the final $d$ meters in $t$ seconds $\implies S_B = \frac{d}{t}$.
  - "$A$ gives $B$ a start of $d$ m and $t$ sec": $B$ runs $L - d$ meters in $T_A + t$ seconds.
- **Circular Tracks (Length $L$, speeds $v_1 > v_2$ with $\frac{v_1}{v_2} = \frac{a}{b}$ in lowest terms, $\gcd(a,b)=1$)**:

| Scenario | Same Direction | Opposite Direction |
| :--- | :--- | :--- |
| **Time for 1st Meeting Anywhere** | $\frac{L}{v_1 - v_2}$ | $\frac{L}{v_1 + v_2}$ |
| **Time for 1st Meeting at Starting Point** | $\text{LCM}\left(\frac{L}{v_1}, \frac{L}{v_2}\right)$ | $\text{LCM}\left(\frac{L}{v_1}, \frac{L}{v_2}\right)$ |
| **Number of Distinct Meeting Points on Track** | $a - b$ | $a + b$ |
| **Laps Completed at 1st Meeting at Start** | $a$ and $b$ laps ($a - b$ relative meetings) | $a$ and $b$ laps ($a + b$ relative meetings) |

- **3 Runners on Circular Track**:
  - Time to meet anywhere $= \text{LCM}\left(\frac{L}{|v_1 \mp v_2|}, \frac{L}{|v_2 \mp v_3|}\right)$.
  - Time to meet at starting point $= \text{LCM}\left(\frac{L}{v_1}, \frac{L}{v_2}, \frac{L}{v_3}\right)$.

---

## 2. Pattern-Recognition Trigger Table

| Question Cue / Wording | Hidden Constraint | Fastest Attack Strategy |
| :--- | :--- | :--- |
| "Walking at $5/7$ of normal speed, a man is $20$ min late..." | Distance is constant; time ratio is $7:5$ | $2\text{ parts} = 20\text{ min} \implies \text{Usual Time} = 5\text{ parts} = 50\text{ min}$ |
| "Train breaks down $d\text{ km}$ further and arrives $\Delta t$ less late..." | Difference in delay occurs strictly over the $d\text{ km}$ segment between the two breakdown points | Apply speed ratio directly to the $d\text{ km}$ segment to find normal speed in 15 seconds |
| "Two runners run back and forth between $A$ and $B$; find distance at $k$-th meeting..." | 1st opposite meeting covers $1D$ combined; every subsequent meeting requires $+2D$ combined | At $k$-th meeting (opposite start), total combined distance $= (2k - 1)D$; individual distance $= (2k-1)D \cdot \frac{v_1}{v_1+v_2}$ |
| "Two runners start from the **same end** $A$ and shuttle between $A$ and $B$..." | At $k$-th head-on meeting, combined distance is $2kD$ | Check whether meeting is head-on ($D_1 + D_2 = 2kD$) or overtaking ($D_1 - D_2 = 2kD$) |
| "Clock hands coincide / form $90^\circ$ / swap positions..." | Relative angular speed $= 6 - 0.5 = 5.5^\circ/\text{min} = \frac{11}{2}^\circ/\text{min}$ | Hands coincide every $\frac{720}{11} = 65\frac{5}{11}\text{ min}$ ($11$ times in $12\text{ hrs}$, $22$ times in $24\text{ hrs}$) |
| "Runner $A$ and $B$ have speeds in ratio $a:b$; how many times do they meet before meeting at the start?" | Includes or excludes the starting/ending point depending on wording | Total meetings in one full cycle $= |a \mp b|$; strictly *between* start and first start-point reunion $= |a \mp b| - 1$ |

---

## 3. Canonical CAT Archetypes & Solved Exemplars

### Archetype 1: Alternating Positive & Negative Work (Wrap-Around Trap)
> **Problem**: Pipe A can fill a tank in $10$ hours and Pipe B can empty the full tank in $15$ hours. If both pipes are opened on alternate hours starting with Pipe A at 8:00 AM, at what time will the tank be completely full for the first time?

- **First-Principles Method**:
  1. Let Tank Capacity $W = \text{LCM}(10, 15) = 30\text{ units}$.
  2. Efficiency: $e_A = +3\text{ units/hr}$, $e_B = -2\text{ units/hr}$.
  3. Every 2-hour cycle $(A \text{ then } B)$ adds $3 - 2 = +1\text{ unit}$.
  4. Reserve $e_A = 3\text{ units}$: target after complete 2-hour cycles is $30 - 3 = 27\text{ units}$.
  5. $27$ cycles take $27 \times 2 = 54\text{ hours}$, bringing the tank to $27\text{ units}$.
  6. In the 55th hour, Pipe A adds $+3\text{ units}$, reaching $30\text{ units}$ (full!).
  7. Total time $= 55\text{ hours}$ from 8:00 AM $= 2\text{ days} + 7\text{ hours} =$ **3:00 PM on Day 3**.

- **30-Second Exam-Hall Speed Shortcut**:
  - Formula: $T = 2 \left\lceil \frac{W - p}{p - q} \right\rceil + \frac{\text{Remainder}}{p} = 2\left(\frac{30 - 3}{1}\right) + 1 = \mathbf{55\text{ hours}}$ (Avoid the naive $30 \times 2 = 60\text{ hr}$ trap!).

---

### Archetype 2: Escalator Steps with Two Walkers
> **Problem**: A walks down an upward-moving escalator and counts $150$ steps in $60$ seconds. B walks down the same escalator and counts $120$ steps in $30$ seconds. How many steps are visible on the stationary escalator?

- **First-Principles Method**:
  1. Moving **against** the escalator: $N = S_{\text{person}} - e \cdot t$.
  2. For A: $N = 150 - 60e$.
  3. For B: $N = 120 - 30e$.
  4. Subtract $(2) - (3)$: $0 = 30 - 30e \implies e = 1\text{ step/sec}$.
  5. Substitute $e = 1$: $N = 120 - 30(1) = \mathbf{90\text{ steps}}$.

- **30-Second Exam-Hall Speed Shortcut (Time Doubling Eliminate)**:
  - Double B's time to match A's $60\text{ s}$: $2N = 240 - 60e$.
  - Subtract A's equation ($N = 150 - 60e$): $N = 240 - 150 = \mathbf{90\text{ steps}}$.

---

### Archetype 3: Shuttle Run Between Two Ends (k-th Meeting)
> **Problem**: P and Q start simultaneously from towns X and Y ($900\text{ m}$ apart) toward each other at $25\text{ m/s}$ and $20\text{ m/s}$ respectively, reversing direction immediately upon reaching either end. Find the distance from X where they meet for the 4th time.

- **First-Principles Method**:
  1. Speed ratio $S_P : S_Q = 25 : 20 = 5 : 4$ (opposite direction, coprime).
  2. Since $5 + 4 = 9$ is odd, all meetings are head-on (never at endpoints unless $2k-1$ is a multiple of $9$).
  3. For the 4th meeting ($k = 4$), combined distance covered $= (2(4) - 1) \times 900 = 7 \times 900\text{ m}$.
  4. Distance covered by P $= 7 \times 900 \times \frac{5}{5+4} = 7 \times 500 = 3500\text{ m}$.
  5. Decompose $3500\text{ m}$ into $900\text{ m}$ laps from X: $3500 = 3 \times 900 + 800\text{ m}$.
  6. After 3 laps ($2700\text{ m}$), P is at town Y and moving back toward X by $800\text{ m}$.
  7. Distance from X $= 900 - 800 = \mathbf{100\text{ m}}$.

- **30-Second Exam-Hall Speed Shortcut (Unit Track Folding)**:
  - Divide track into $5 + 4 = 9$ parts ($1\text{ part} = 100\text{ m}$).
  - In each $1D$ combined distance, P moves $5\text{ parts}$. At the 4th meeting ($7D$ combined), P is at $7 \times 5 = 35\text{ parts}$.
  - Fold $35 \pmod{18} = 17\text{ parts} \implies 18 - 17 = 1\text{ part from X} = \mathbf{100\text{ m}}$.

---

## 4. Boundary Conditions, Domain Traps & TITA Pitfalls

1. **Coprime Reduction Before Counting Circular Meeting Points**:
   - If $v_1 = 6\text{ m/s}$ and $v_2 = 4\text{ m/s}$, you MUST reduce $\frac{6}{4}$ to $\frac{3}{2}$ first! Distinct meeting points $= 3 - 2 = 1$ (same direction) or $3 + 2 = 5$ (opposite direction), **never** $6 - 4 = 2$ or $6 + 4 = 10$.
2. **Same-End Shuttle vs. Opposite-End Shuttle**:
   - When both runners start from the **same end** $A$ with speeds $a : b$, they meet both head-on ($D_1 + D_2 = 2mL$) and by overtaking ($D_1 - D_2 = 2nL$). List exact meeting times $t = \frac{2mL}{v_1+v_2}$ and $t = \frac{2nL}{v_1-v_2}$ and deduplicate common timestamps when meetings occur at the endpoints!
3. **Train Crossing a Moving Person vs. Platform**:
   - Crossing a person/pole uses $D = L_{\text{train}}$; crossing a bridge/platform uses $D = L_{\text{train}} + L_{\text{bridge}}$. Always convert $\text{km/hr} \times \frac{5}{18} \to \text{m/s}$ before multiplying by seconds!
4. **Boats & Streams Impossible Upstream Trap**:
   - If stream speed $v \ge$ boat speed $u$, the boat can never return upstream. In TITA equation setups, discard roots where $u \le v$.

---

## 5. Active-Recall Drill (10 Prompts)

<details><summary>Q1: A takes 9 days more than (A+B) together to finish a job, while B takes 16 days more than (A+B) together. How many days does A alone take?</summary>
A: Combined time T_AB = sqrt(9 * 16) = 12 days. Therefore A alone takes 12 + 9 = 21 days.
</details>

<details><summary>Q2: Two trains start simultaneously from A and B toward each other and take 4 hours and 9 hours respectively to reach their destinations after crossing each other. If the first train runs at 54 km/hr, find the speed of the second train.</summary>
A: S_1 / S_2 = sqrt(t_2 / t_1) = sqrt(9 / 4) = 3 / 2. Since S_1 = 54 km/hr, S_2 = 54 * (2/3) = 36 km/hr.
</details>

<details><summary>Q3: Three runners A, B, C run in the same direction on a circular track at speeds 12 m/s, 18 m/s, and 30 m/s. At how many distinct points on the track can all three meet simultaneously?</summary>
A: Pairwise reduced speed ratios: A:B = 2:3 (|2-3| = 1 point); B:C = 3:5 (|3-5| = 2 points). Number of common meeting points = gcd(1, 2) = 1 point (only the starting point).
</details>

<details><summary>Q4: Without stoppages, a bus travels at 60 km/hr, and with stoppages it averages 45 km/hr. How many minutes per hour does the bus stop?</summary>
A: Stoppage time per hour = (S_fast - S_slow) / S_fast = (60 - 45) / 60 = 15/60 hr = 15 minutes per hour.
</details>

<details><summary>Q5: In a 1000 m race, A beats B by 100 m, and in an 800 m race, B beats C by 80 m. By how many meters will A beat C in a 500 m race?</summary>
A: S_A / S_B = 1000 / 900 = 10/9; S_B / S_C = 800 / 720 = 10/9 -> S_A / S_C = 100 / 81 = 500 / 405. Thus in a 500 m race, A beats C by 500 - 405 = 95 m.
</details>

<details><summary>Q6: A boat rows 24 km upstream and 36 km downstream in 6 hours, and 36 km upstream and 24 km downstream in 6.5 hours. Find the speed of the stream.</summary>
A: Add both: 60/S_U + 60/S_D = 12.5. Inspect clean factors of 24 & 36: S_D = 12 km/hr, S_U = 6 km/hr -> 24/6 + 36/12 = 4 + 3 = 7 (adjust: try S_D = 12, S_U = 8 -> 24/8 + 36/12 = 3 + 3 = 6 hrs; 36/8 + 24/12 = 4.5 + 2 = 6.5 hrs!). Stream speed v = (12 - 8)/2 = 2 km/hr.
</details>

<details><summary>Q7: A monkey climbs 6 m in the first minute and slips 4 m in the second minute on a 60 m greased pole. In how many minutes does it touch the top?</summary>
A: Reserve final positive jump of 6 m: target = 60 - 6 = 54 m. Each 2-min cycle gains 2 m -> 27 cycles = 54 minutes to reach 54 m. In the 55th minute, it climbs +6 m to reach 60 m. Answer: 55 minutes.
</details>

<details><summary>Q8: Two runners run in opposite directions on a circular track at speeds 15 m/s and 25 m/s. How many distinct meeting points exist on the track?</summary>
A: Reduce speed ratio to lowest terms: 15 : 25 = 3 : 5. For opposite directions, distinct points = a + b = 3 + 5 = 8 points.
</details>

<details><summary>Q9: 12 men or 18 women can reap a field in 14 days. How many days will 8 men and 16 women take to reap it?</summary>
A: 12M = 18W -> M/W = 3/2. Total work = 12 * 3 * 14 = 504 units. Daily work of (8M + 16W) = 8(3) + 16(2) = 24 + 32 = 56 units/day. Days = 504 / 56 = 9 days.
</details>

<details><summary>Q10: A and B run in the same direction around a 600 m circular track at 9 m/s and 5 m/s. When do they meet at the starting point for the first time?</summary>
A: LCM(600/9, 600/5) = LCM(200/3, 120) = LCM(200, 360) / GCD(3, 1) = 1800 / 3 = 600 seconds.
</details>

---

## CAT 2025 PYQ Edge Examples & Newly Surfaced Patterns

### Newly Surfaced Sub-Topic Variants & Pattern Triggers (CAT 2025)
- **Integer-Day Billing Step Optimization in Time & Work (`CAT_2025_QA_Slot_1` / `CAT2025_S1_QA_Q21`)**: When workers charge full daily rates for any fractional day worked, compare cost-per-unit-work $\frac{C_i}{e_i}$ and test whether assigning 1 integer day to the higher-rate worker eliminates an extra ceiling day.
- **TSD with Speeds and Times Simultaneously in AP (`CAT_2025_QA_Slot_1` / `CAT2025_S1_QA_Q15`)**: Parameterize symmetrically around the middle day: $d_1 = (v-a)(t+b)$, $d_2 = vt$, $d_3 = (v+a)(t-b) \implies d_1 + d_3 - 2d_2 = -2ab$.
- **Turn-Based Circular Track & Modular Step Transitions (`CAT_2025_DILR_Slot_1` `SET1` & `CAT_2025_DILR_Slot_3` `SET4`)**: Discrete circular track movement on an $N$-seat ring reduces to modular arithmetic $\pmod N$ where clockwise/counterclockwise steps $(+1, +2, -1, -2 \pmod 7)$ satisfy wrap-around equivalence ($+3 \equiv -4 \pmod 7$).

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

#### CAT2025_S1_QA_Q15 (`CAT_2025_QA_Slot_1` | MCQ | Medium | `Round_2_Doable`)
- **Sub-Topic**: Time, Speed & Distance (TSD) — *TSD with speeds and times both in Arithmetic Progression*
- **Verified Answer**: `(C) 86400` (Total time = 180 min in 4 AP parts starting at t1 = 30 => times are 30, 40, 50, 60 min. Speeds: 960, 960+d, 960+2d, 960+3d m/min. Total dist = 180*960 + 320d = 224000 => d = 160 m/min. 4th part dist = (960 + 480)*60 = 86400 m.)
- **Mental Trigger (`See X -> Do Y`)**: Convert 224 km to 224000 m and 3 hours to 180 minutes immediately so units match 960 m/min and 30 min.
- **First-Principles Method**: Since 4 times in AP sum to 180 min with t1 = 30, 2(30 + t4) = 180 => t4 = 60 min, so times are 30, 40, 50, 60 min. Then 30(960) + 40(960+d) + 50(960+2d) + 60(960+3d) = 224000 => 172800 + 320d = 224000 => d = 160. Distance in 4th part = (960 + 3*160)*60 = 1440*60 = 86400 m.
- **30-Second Exam-Hall Speed Shortcut**: Base distance at constant speed 960 m/min for 180 min is 172800 m. Extra distance = 224000 - 172800 = 51200 m over (0*30 + 1*40 + 2*50 + 3*60) = 320 d-units => d = 160 => s4*t4 = 1440*60 = 86400.
- **Trap Alert & Boundary Condition**: Do not assume average speed equals the arithmetic mean of the 4 speeds because the time intervals (30, 40, 50, 60) are unequal.

#### CAT2025_S1_QA_Q21 (`CAT_2025_QA_Slot_1` | MCQ | Medium | `Round_2_Doable`)
- **Sub-Topic**: Time & Work, Pipes & Cisterns — *Cost-per-unit-work optimization with integer day-charge step constraints*
- **Verified Answer**: `(B) 38400` (Total cost per full task: Tarun = 15*2160 = 32400 (cheapest), Varun = 21*2400 = 50400, Arun = 24*2160 = 51840. Employ Tarun for all 10 days (does 10/15 = 2/3 of task, cost 21600). Remaining 1/3 task takes Varun exactly 7 integer days (7/21 = 1/3, cost 7*2400 = 16800) vs Arun 8 days (8/24 = 1/3, cost 8*2160 = 17280). Minimum cost = 21600 + 16800 = 38400.)
- **Mental Trigger (`See X -> Do Y`)**: Rank workers by Cost per Complete Task (Daily Wage * Days Alone): Tarun (32400) < Varun (50400) < Arun (51840), and max out the cheapest worker for all 10 days.
- **First-Principles Method**: To minimize cost within 10 days, employ Tarun (lowest cost per unit work: 32400/task) for the maximum 10 days, completing 10/15 = 2/3 of the task for Rs 21600. For the remaining 1/3 task, Varun needs exactly 7 days (7/21 = 1/3) costing 7*2400 = 16800, whereas Arun needs 8 days (8/24 = 1/3) costing 8*2160 = 17280 (and mixing them requires partial days billed as full days, costing >= 17040). Thus minimum total cost = 21600 + 16800 = 38400.
- **30-Second Exam-Hall Speed Shortcut**: Tarun 10 days (2/3 work, Rs 21600) + Varun 7 days (1/3 work, Rs 16800) = Rs 38400 with zero wasted partial-day billing.
- **Trap Alert & Boundary Condition**: Choosing Arun over Varun because Arun has a lower daily wage (2160 vs 2400) is a classic trap: Arun is slower (24 days vs 21 days), so Arun costs 17280 for 1/3 work -> 38880 (distractor D).

#### CAT2025_S2_QA_Q17 (`CAT_2025_QA_Slot_2` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Time & Work, Pipes & Cisterns — *Relative efficiency assignment in Time & Work*
- **Verified Answer**: `340` (Set daily efficiencies C = 1, B = 2, A = 4. Work in first 20 days = 20*(4+2+1) = 140. Work in remaining 40 days by A and C = 40*(4+1) = 200. Total work = 340 units. Chandan alone (rate 1) takes 340 days.)
- **Mental Trigger (`See X -> Do Y`)**: Assign the slowest worker (Chandan) efficiency = 1 unit/day so Total Work numerically equals Chandan's solo days!
- **First-Principles Method**: Let rates of C, B, A be 1, 2, 4 units/day. All three work for 20 days (20 * 7 = 140 units) and A + C work for the remaining 40 days (40 * 5 = 200 units). Total work = 340 units, so C alone needs 340/1 = 340 days.
- **30-Second Exam-Hall Speed Shortcut**: A and C work all 60 days: 60*(4+1) = 300. B works 20 days: 20*2 = 40. Total = 340.
- **Trap Alert & Boundary Condition**: 'Completed in 60 days' means 60 days in total (40 days after Bipin leaves), not 60 days after Bipin leaves.

#### CAT2025_S2_QA_Q21 (`CAT_2025_QA_Slot_2` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Time, Speed & Distance (TSD) — *Boats and streams upstream-downstream time difference and round-trip harmonic speed*
- **Verified Answer**: `8` (For Sneha (6 km/h): 14/(6 - u) - 14/(6 + u) = 48/60 = 4/5 => u = 1 km/h. For Rita (5 km/h): upstream = 4 km/h, downstream = 6 km/h. Round trip in 100 min = 5/3 hrs: d/4 + d/6 = 5/3 => d = 4 km one-way. Total distance = 2d = 8 km.)
- **Mental Trigger (`See X -> Do Y`)**: Test integer stream speed u = 1 km/h first: 14/5 - 14/7 = 2.8 - 2.0 = 0.8 hrs = 48 min!
- **First-Principles Method**: Sneha: 14/(6-u) - 14/(6+u) = 4/5 => 28u/(36 - u^2) = 4/5 => u = 1 km/h. Rita's upstream speed is 5 - 1 = 4 km/h and downstream speed is 5 + 1 = 6 km/h. Average speed for round trip = 2*4*6/(4+6) = 4.8 km/h. Total distance in 100/60 hrs = 4.8 * (5/3) = 8 km.
- **30-Second Exam-Hall Speed Shortcut**: Spot u = 1 km/h by inspection (14/5 - 14/7 = 4/5 hr). Then Rita's round-trip average speed is 2(4)(6)/10 = 4.8 km/h; for 5/3 hr, total distance = 4.8 * 5/3 = 8 km.
- **Trap Alert & Boundary Condition**: The question asks for the TOTAL distance Rita will cover (upstream + downstream = 2d = 8 km), not the one-way distance d = 4 km.

#### CAT2025_S3_QA_Q07 (`CAT_2025_QA_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Time, Speed & Distance (TSD) — *Proportional TSD time-saving identity D = Delta_t * v1 * v2 / Delta_v*
- **Verified Answer**: `(B) 15` (Remaining distance D = (20/60) * v(v+3)/3 = (30/60) * v(v+5)/5 => (v+3)/9 = (v+5)/10 => 10v + 30 = 9v + 45 => v = 15 km/h.)
- **Mental Trigger (`See X -> Do Y`)**: Equate remaining distance D = Delta_t1 * v(v + s1)/s1 = Delta_t2 * v(v + s2)/s2 => (v + s1)/s1 * Delta_t1 = (v + s2)/s2 * Delta_t2!
- **First-Principles Method**: Let remaining distance after the stop be D. Saving 20 min requires +3 km/h, and saving 30 min (20 + 10) requires +5 km/h: D = (20/60)*v(v+3)/3 = (30/60)*v(v+5)/5 => 20(v+3)/3 = 30(v+5)/5 => (v+3)/9 = (v+5)/10 => v = 15.
- **30-Second Exam-Hall Speed Shortcut**: (v + 3)/9 = (v + 5)/10 => v = 15 in 10 seconds (notice the 5 pm to 11 pm window is completely extraneous!).
- **Trap Alert & Boundary Condition**: '10 minutes more' means total stop = 20 + 10 = 30 minutes (not 10 minutes).

#### CAT2025_S3_QA_Q10 (`CAT_2025_QA_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Time & Work, Pipes & Cisterns — *Combined flow rate scaling in Pipes & Cisterns*
- **Verified Answer**: `(C) 73` (Rates A:B:C = 4:9:36 (total = 49). Pipe A (rate 4) takes 15 hours = 900 minutes, so tank volume = 4 * 900 = 3600 units. All 3 pipes together take 3600 / 49 = 73.47 minutes, nearest to 73.)
- **Mental Trigger (`See X -> Do Y`)**: Convert 15 hours to 900 minutes first, then multiply by 4 / (4 + 9 + 36) = 4/49.
- **First-Principles Method**: Total time in minutes = (15 * 60) * 4 / (4 + 9 + 36) = 3600 / 49 = 73.469 minutes, nearest to 73.
- **30-Second Exam-Hall Speed Shortcut**: 3600 / 49 = 73 + 23/49 -> 73.
- **Trap Alert & Boundary Condition**: Pay attention to unit conversion from hours (15 h) to minutes (900 min).

#### CAT2025_S3_QA_Q11 (`CAT_2025_QA_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Time & Work, Pipes & Cisterns — *Individual member efficiency LCM scaling in multi-team work problems*
- **Verified Answer**: `(B) 2` (Per-member hourly work (out of 400 total units): Team A member = 400/(5*40) = 2 units/h; Team B member = 400/(8*50) = 1 unit/h; Team C member = 400/(10*4) = 10 units/h. Initial group (2A + 3B + 1C) does 2(2) + 3(1) + 1(10) = 17 units/h. In 23 hours, they complete 23 * 17 = 391 units, leaving 9 units for the 24th hour. Since 2A + 3B do 7 units/h, 2 additional members from Team B (1 unit/h each) are needed.)
- **Mental Trigger (`See X -> Do Y`)**: Take Total Work = LCM(5*40, 8*50, 10*4) = LCM(200, 400, 40) = 400 units so each B-member has efficiency = 1 unit/hour!
- **First-Principles Method**: Set Total Work = 400 units. Individual efficiencies: a = 400/200 = 2, b = 400/400 = 1, c = 400/40 = 10 units/hr. In 23 hours, (2a + 3b + c) completes 23*(4 + 3 + 10) = 391 units. Remaining 9 units in 1 hour require 2a + (3 + x)b = 4 + 3 + x = 9 => x = 2 additional B-members.
- **30-Second Exam-Hall Speed Shortcut**: 1 member of C (rate 10) equals 10 members of B (rate 1). Over 24 hours, 2A + 3B + 1C would do 24*17 = 408 units (8 units excess). Removing 1C in the last hour loses 10 units, leaving a net deficit of 10 - 8 = 2 units = 2 B-members!
- **Trap Alert & Boundary Condition**: The question asks for ADDITIONAL members from Team B (2), not the total members from Team B (3 + 2 = 5).

#### CAT2025_S3_QA_Q12 (`CAT_2025_QA_Slot_3` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Time, Speed & Distance (TSD) — *Inverse speed-time ratio on fixed segments*
- **Verified Answer**: `444` (Run speed : Walk speed = 1.4 : 1 = 7 : 5, so Run time : Walk time = 5 : 7 on any fixed segment. Given Walk(BC) = 210 min => Run(BC) = 210 * (5/7) = 150 min. Given Run(BA) = 210 min => Walk(AB) = 210 * (7/5) = 294 min. Total = 294 + 150 = 444 min.)
- **Mental Trigger (`See X -> Do Y`)**: Since v_run / v_walk = 7/5, multiply by 7/5 to convert Run time -> Walk time, and by 5/7 to convert Walk time -> Run time!
- **First-Principles Method**: 3 hours 30 minutes = 210 minutes. Since running speed is 7/5 of walking speed, time taken is inversely proportional (5/7). Thus Walk(AB) = (7/5)*Run(BA) = (7/5)*210 = 294 min, and Run(BC) = (5/7)*Walk(BC) = (5/7)*210 = 150 min. Total = 294 + 150 = 444 min.
- **30-Second Exam-Hall Speed Shortcut**: 210 * (7/5 + 5/7) = 210 * (74/35) = 6 * 74 = 444 minutes!
- **Trap Alert & Boundary Condition**: Keep all times in minutes (3 hr 30 min = 210 min).
