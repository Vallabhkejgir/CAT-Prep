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
