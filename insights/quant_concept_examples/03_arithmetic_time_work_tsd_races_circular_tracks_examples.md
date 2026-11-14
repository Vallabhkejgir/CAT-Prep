# QA 03 Concept & Formula Examples: Time & Work, Pipes & Cisterns, Time Speed Distance, Races & Circular Tracks

> **Companion Reference**: [`../topic_summaries/quant/03_arithmetic_time_work_tsd_races_circular_tracks.md`](../topic_summaries/quant/03_arithmetic_time_work_tsd_races_circular_tracks.md) | [`QA_Formula_and_Trigger_Book.md`](../high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md)

Every concept, formula, and pattern trigger from **QA 03** is explained below with plain-English intuition, clean single-concept numbers, a two-way walkthrough (direct formula vs. mental ratio intuition), and the #1 mistake to avoid.

---

## Concept 1: LCM Total-Work Method & Man-Days-Hours Equivalence

### 1. Concept & Formula in Plain English
Instead of adding messy fractions like $\frac{1}{12} + \frac{1}{15}$, pretend the job is making **chocolates** where the total number of chocolates is $\text{LCM}(t_1, t_2)$. Then each worker's daily rate is a clean whole number!
For groups of workers with different headcount ($M$), days ($D$), hours/day ($H$), efficiency ($E$), and total work ($W$):
$$\frac{M_1 D_1 H_1 E_1}{W_1} = \frac{M_2 D_2 H_2 E_2}{W_2}$$

### 2. When to Use It (Question Cue)
- *"A can finish a work in $12$ days and B in $15$ days..."*
- *"$15$ men working $8$ hours a day build $2$ walls in $10$ days. How many days will $20$ men working $6$ hours a day take to build $3$ walls?"*

### 3. General Example (Clean Numbers, Single Concept)
> $15$ men working $8$ hours a day can dig $2$ trenches in $10$ days. How many days will $20$ men working $6$ hours a day take to dig $3$ identical trenches?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Group 1: $M_1 = 15, D_1 = 10, H_1 = 8, W_1 = 2$.
  2. Group 2: $M_2 = 20, D_2 = ?, H_2 = 6, W_2 = 3$.
  3. Substitute into $\frac{M_1 D_1 H_1}{W_1} = \frac{M_2 D_2 H_2}{W_2}$:
     $$\frac{15 \times 10 \times 8}{2} = \frac{20 \times D_2 \times 6}{3} \implies 600 = 40 D_2 \implies D_2 = \mathbf{15\text{ days}}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Group 1 puts in $15 \times 10 \times 8 = 1,200\text{ man-hours}$ for $2$ trenches, so **$600\text{ man-hours}$ per trench**.
  2. $3$ trenches require $3 \times 600 = 1,800\text{ man-hours}$.
  3. Group 2 supplies $20 \times 6 = 120\text{ man-hours per day}$, taking $\frac{1800}{120} = \mathbf{15\text{ days}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Putting the work done ($W_1, W_2$) in the **numerator** instead of the **denominator** (more work requires *more* man-hours, so $W$ divides $M \cdot D \cdot H$).

---

## Concept 2: Extra Time Over Combined Work Time ($T_{AB} = \sqrt{ab}$)

### 1. Concept & Formula in Plain English
If $A$ and $B$ working together finish a job in $T$ days, and working alone $A$ takes $a$ days **more** than $T$ ($T + a$) while $B$ takes $b$ days **more** than $T$ ($T + b$), the combined time is simply the geometric mean of the two extra times:
$$T_{AB} = \sqrt{a \cdot b}$$

### 2. When to Use It (Question Cue)
- *"A alone takes $4$ days more than A and B together, while B alone takes $9$ days more than A and B together. In how many days can they finish it together?"*

### 3. General Example (Clean Numbers, Single Concept)
> Working alone, Pipe A takes $4$ hours more than Pipes $(A + B)$ together to fill a tank, and Pipe B takes $9$ hours more than $(A + B)$ together. Find the time taken by $(A + B)$ together, and by Pipe A alone.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Identify extra times $a = 4$ and $b = 9$.
  2. Plug into $T_{AB} = \sqrt{a \cdot b}$:
     $$T_{AB} = \sqrt{4 \times 9} = \mathbf{6\text{ hours}}$$
  3. Pipe A alone takes $T_{AB} + a = 6 + 4 = \mathbf{10\text{ hours}}$ (and Pipe B takes $6 + 9 = 15\text{ hours}$).
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Let combined time be $T$. In $T$ hours, $A$ and $B$ finish the tank.
  2. When $A$ works alone for $T + 4$ hours, the extra $4$ hours of $A$'s work replaces what $B$ would have done in $T$ hours ($\implies 4e_A = T e_B$).
  3. Similarly for $B$, $9e_B = T e_A$. Multiplying the two equations gives $36 e_A e_B = T^2 e_A e_B \implies T = \mathbf{6\text{ hours}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Applying $\sqrt{ab}$ when $a$ and $b$ are the **total** times ($10$ and $15$) instead of the **extra** times ($4$ and $9$) over the combined time.

---

## Concept 3: Alternating Positive & Negative Work (Monkey Climb / Cistern Trap)

### 1. Concept & Formula in Plain English
When an inlet pipe adds $+p$ units in hour 1 and an outlet pipe drains $-q$ units in hour 2 (or a monkey climbs $+p$ meters and slips $-q$ meters), as soon as the water reaches the top capacity $W$ during a positive turn, **the task is finished** and the outlet pipe never gets a chance to drain it back down!
Therefore, always **subtract the positive jump $p$ from $W$ first**, run complete 2-step cycles of net gain $(p - q)$ to reach $W - p$, and add the final positive step:
$$N_{\text{cycles}} = \left\lceil \frac{W - p}{p - q} \right\rceil$$

### 2. When to Use It (Question Cue)
- *"A monkey climbs $5\text{ m}$ in the first minute and slips $3\text{ m}$ in the second minute on a $21\text{ m}$ pole..."*
- *"Pipe A fills in $6\text{ hrs}$ and Pipe B empties in $8\text{ hrs}$; opened alternatively starting with A..."*

### 3. General Example (Clean Numbers, Single Concept)
> A monkey climbs $5\text{ m}$ up a greased pole in the 1st minute and slips down $3\text{ m}$ in the 2nd minute. If the pole is $21\text{ m}$ high, in how many minutes will the monkey touch the top of the pole for the first time?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $W = 21\text{ m}$, positive step $p = 5\text{ m}$, negative step $q = 3\text{ m}$, net 2-min gain $p - q = 2\text{ m}$.
  2. Reserve the final jump: $W - p = 21 - 5 = 16\text{ m}$.
  3. Number of 2-minute cycles $= \left\lceil \frac{16}{2} \right\rceil = 8\text{ cycles} = 16\text{ minutes}$ (reaching $16\text{ m}$).
  4. In the $17$th minute, the monkey climbs $+5\text{ m}$ ($16 + 5 = 21\text{ m}$) and touches the top. Total time $= \mathbf{17\text{ minutes}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. After $16$ minutes ($8$ pairs of minutes), the monkey is at $8 \times (5 - 3) = 16\text{ m}$.
  2. At the start of Minute $17$, it climbs $5\text{ m}$ straight to $21\text{ m}$ and grabs the top! Answer: $\mathbf{17\text{ minutes}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Dividing full height $21$ by net gain $2$ ($\approx 20.6$ minutes) without reserving the final $+5\text{ m}$ upward jump.

---

## Concept 4: Proportionality Laws in TSD & Breakdown Delay Localization

### 1. Concept & Formula in Plain English
For a **constant distance $D$**, Speed and Time are inversely proportional: if you travel at $\frac{a}{b}$ of your usual speed, you take $\frac{b}{a}$ of your usual time, so the time difference $\Delta T$ equals $|b - a|$ parts while usual time is $a$ parts!
In **Train Breakdown problems** ("if the breakdown had occurred $d\text{ km}$ further, the train would have been $\Delta t$ less late"), both scenarios are identical before the first breakdown point and after the second breakdown point—so the entire time difference $\Delta t$ happens **exclusively over the $d\text{ km}$ segment** between the two points!

### 2. When to Use It (Question Cue)
- *"Walking at $\frac{3}{4}$ of his usual speed, a man reaches his office $15$ minutes late. Find his usual time."*
- *"Had the accident occurred $30\text{ km}$ further on, the train would have reached $15$ minutes earlier..."*

### 3. General Example (Clean Numbers, Single Concept)
> Walking at $\frac{3}{4}$ of her usual speed, Meera reaches her office $15$ minutes late. What is her usual time to reach the office?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Speed ratio $S_{\text{new}} : S_{\text{usual}} = 3 : 4 \implies$ Time ratio $T_{\text{new}} : T_{\text{usual}} = 4 : 3$.
  2. Extra time $= 4 - 3 = 1\text{ part} = 15\text{ minutes}$.
  3. Usual time $= 3\text{ parts} = 3 \times 15 = \mathbf{45\text{ minutes}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Speed dropped by $\frac{1}{4}$, so time increased by $\frac{1}{4 - 1} = \frac{1}{3}$ of usual time.
  2. Since $\frac{1}{3}$ of usual time is $15\text{ min}$, usual time $= 3 \times 15 = \mathbf{45\text{ minutes}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Multiplying $15\text{ min} \times 4 = 60\text{ min}$ (which is the **late** time $T_{\text{new}}$, not the **usual** time $T_{\text{usual}} = 45\text{ min}$).

---

## Concept 5: Average Speed (Harmonic vs. Arithmetic Mean) & Bus Stoppage Formula

### 1. Concept & Formula in Plain English
$$\text{Average Speed} = \frac{\text{Total Distance}}{\text{Total Time}}$$
- **Equal Distances** at $s_1$ and $s_2$: You spend *more time* at the slower speed, so average speed is pulled down to the **Harmonic Mean**: $S_{\text{avg}} = \frac{2s_1 s_2}{s_1 + s_2}$.
- **Equal Time Intervals** at $s_1$ and $s_2$: Average speed is the simple **Arithmetic Mean**: $S_{\text{avg}} = \frac{s_1 + s_2}{2}$.
- **Bus Stoppages**: If a vehicle travels at $S_{\text{fast}}$ without stops and averages $S_{\text{slow}}$ with stops, the fraction of every hour spent stopped is $\frac{S_{\text{fast}} - S_{\text{slow}}}{S_{\text{fast}}}$.

### 2. When to Use It (Question Cue)
- *"A car goes from A to B at $40\text{ km/hr}$ and returns from B to A at $60\text{ km/hr}$. Find its average speed."*
- *"Excluding stoppages, the speed of a bus is $60\text{ km/hr}$, and including stoppages it is $45\text{ km/hr}$. For how many minutes does the bus stop per hour?"*

### 3. General Example (Clean Numbers, Single Concept)
> (a) A driver travels from Town P to Town Q at $40\text{ km/hr}$ and returns from Q to P at $60\text{ km/hr}$. Find the average speed for the round trip.
> (b) A bus travels at $60\text{ km/hr}$ without stoppages and averages $45\text{ km/hr}$ with stoppages. How many minutes per hour does it stop?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: Equal distances $\implies S_{\text{avg}} = \frac{2s_1 s_2}{s_1 + s_2} = \frac{2(40)(60)}{40 + 60} = \frac{4800}{100} = \mathbf{48\text{ km/hr}}$.
  2. **Part (b)**: Stoppage fraction $= \frac{60 - 45}{60} = \frac{15}{60}\text{ hr} = \mathbf{15\text{ minutes/hour}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. **Part (a)**: Pick a convenient distance $D = \text{LCM}(40, 60) = 120\text{ km}$ each way ($240\text{ km}$ round trip). Going takes $\frac{120}{40} = 3\text{ hrs}$; returning takes $\frac{120}{60} = 2\text{ hrs}$. Total $= \frac{240\text{ km}}{5\text{ hrs}} = \mathbf{48\text{ km/hr}}$.
  2. **Part (b)**: In $1$ hour, the bus only covers $45\text{ km}$ instead of $60\text{ km}$. At its running speed of $60\text{ km/hr}$ ($1\text{ km/min}$), covering $45\text{ km}$ takes $45$ minutes—so it stood still for the remaining $60 - 45 = \mathbf{15\text{ minutes}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Averaging $40$ and $60$ as $\frac{40+60}{2} = 50\text{ km/hr}$ when the **distances** (not times) are equal.

---

## Concept 6: Radha–Shyam Post-Meeting Theorem

### 1. Concept & Formula in Plain English
When two travelers $A$ and $B$ start **at the same time** from opposite ends $P$ and $Q$, meet at some point $M$ after time $t_{\text{meet}}$, and then take $t_A$ and $t_B$ hours respectively to finish their remaining journeys ($M \to Q$ and $M \to P$):
$$\frac{S_A}{S_B} = \sqrt{\frac{t_B}{t_A}}, \qquad t_{\text{meet}} = \sqrt{t_A \cdot t_B}$$
Why? Before meeting, $A$ and $B$ covered $PM$ and $MQ$ in time $t_{\text{meet}}$. After meeting, $A$ covers $MQ$ in $t_A$ and $B$ covers $PM$ in $t_B$. Equating the distance ratio $\frac{PM}{MQ} = \frac{S_A}{S_B} = \frac{t_{\text{meet}}}{t_B} = \frac{t_A}{t_{\text{meet}}}$ gives both formulas immediately!

### 2. When to Use It (Question Cue)
- *"Two trains start at the same time from A and B toward each other. After passing each other, they take $4$ hours and $9$ hours to reach B and A..."*

### 3. General Example (Clean Numbers, Single Concept)
> Two trains $A$ and $B$ start simultaneously from stations $X$ and $Y$ toward each other. After meeting on the way, Train $A$ takes $9$ hours to reach $Y$ and Train $B$ takes $4$ hours to reach $X$. If Train $A$'s speed is $40\text{ km/hr}$, find Train $B$'s speed and the total time taken to meet.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Given $t_A = 9\text{ hrs}$, $t_B = 4\text{ hrs}$, and $S_A = 40\text{ km/hr}$.
  2. Speed ratio: $\frac{S_A}{S_B} = \sqrt{\frac{t_B}{t_A}} = \sqrt{\frac{4}{9}} = \frac{2}{3} \implies S_B = 40 \times \frac{3}{2} = \mathbf{60\text{ km/hr}}$.
  3. Time to meet: $t_{\text{meet}} = \sqrt{t_A \cdot t_B} = \sqrt{9 \times 4} = \mathbf{6\text{ hours}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. The second half of $A$'s trip took $9\text{ hrs}$ at $40\text{ km/hr} = 360\text{ km}$ (which is segment $MY$).
  2. Before meeting, $B$ covered that same segment $MY = 360\text{ km}$ in $t_{\text{meet}}$ hours, and after meeting $B$ covered $XM = 40 \times t_{\text{meet}}$ in $4\text{ hrs}$.
  3. Thus $S_B = \frac{360}{t_{\text{meet}}} = \frac{40 t_{\text{meet}}}{4} \implies t_{\text{meet}}^2 = 36 \implies t_{\text{meet}} = \mathbf{6\text{ hrs}}$ and $S_B = \mathbf{60\text{ km/hr}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Writing $\frac{S_A}{S_B} = \sqrt{\frac{t_A}{t_B}}$ instead of flipping the fraction under the square root ($\sqrt{\frac{t_B}{t_A}}$—whoever takes *less* time after meeting is the *faster* traveler!).

---

## Concept 7: Trains Crossing Poles, Platforms & Moving Observers

### 1. Concept & Formula in Plain English
A train has physical length $L_{\text{train}}$. To completely pass an object:
- **Zero-length object** (pole, standing man, or moving man): $\text{Distance} = L_{\text{train}}$.
- **Extended object** (bridge, platform, tunnel, or another train): $\text{Distance} = L_{\text{train}} + L_{\text{object}}$.
- **Relative Speed**: Same direction $\implies |S_1 - S_2|$; Opposite direction $\implies S_1 + S_2$.
- **Unit Conversion**: $\text{km/hr} \times \frac{5}{18} = \text{m/s}$.

### 2. When to Use It (Question Cue)
- *"A $150\text{ m}$ long train running at $54\text{ km/hr}$ crosses a platform in $20$ seconds..."*

### 3. General Example (Clean Numbers, Single Concept)
> A train $150\text{ m}$ long is running at $54\text{ km/hr}$. How many seconds will it take to cross:
> (a) a telegraph pole?
> (b) a $210\text{ m}$ long platform?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Convert speed to $\text{m/s}$: $S = 54 \times \frac{5}{18} = 15\text{ m/s}$.
  2. **Part (a) Pole**: $t = \frac{L_{\text{train}}}{S} = \frac{150}{15} = \mathbf{10\text{ seconds}}$.
  3. **Part (b) Platform**: $t = \frac{L_{\text{train}} + L_{\text{platform}}}{S} = \frac{150 + 210}{15} = \frac{360}{15} = \mathbf{24\text{ seconds}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. The train covers its own $150\text{ m}$ length in $10\text{ s}$ ($15\text{ m}$ per second).
  2. Crossing the $210\text{ m}$ platform just requires covering an extra $210\text{ m}$ ($\frac{210}{15} = 14\text{ s}$) plus its own length ($10\text{ s}$) $= \mathbf{24\text{ seconds}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting to add the train's own length ($150\text{ m}$) when crossing a platform, or forgetting to multiply $\text{km/hr}$ by $\frac{5}{18}$.

---

## Concept 8: Boats & Streams Upstream/Downstream Decomposition

### 1. Concept & Formula in Plain English
If a boat's speed in still water is $u$ and the river's current speed is $v$:
- **Downstream Speed** (with the current): $S_D = u + v$
- **Upstream Speed** (against the current): $S_U = u - v$
Given $S_D$ and $S_U$, you can recover $u$ and $v$ instantly as their average and half-difference:
$$u = \frac{S_D + S_U}{2}, \qquad v = \frac{S_D - S_U}{2}$$

### 2. When to Use It (Question Cue)
- *"A boat goes $30\text{ km}$ downstream in $2$ hours and $18\text{ km}$ upstream in $3$ hours. Find the speed of the boat in still water and the speed of the stream."*

### 3. General Example (Clean Numbers, Single Concept)
> A rower covers $30\text{ km}$ downstream in $2$ hours and returns $18\text{ km}$ upstream in $3$ hours. Find the speed of the boat in still water ($u$) and the speed of the river current ($v$).

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Compute $S_D = \frac{30}{2} = 15\text{ km/hr}$ and $S_U = \frac{18}{3} = 6\text{ km/hr}$.
  2. Boat speed $u = \frac{15 + 6}{2} = \mathbf{10.5\text{ km/hr}}$.
  3. Stream speed $v = \frac{15 - 6}{2} = \mathbf{4.5\text{ km/hr}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. $10.5$ is halfway between $6$ and $15$, and the river pushes $+4.5$ one way and pulls $-4.5$ the other way.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Subtracting $S_D - S_U = 15 - 6 = 9\text{ km/hr}$ and forgetting to **divide by $2$** to get the stream speed $v = 4.5\text{ km/hr}$.

---

## Concept 9: Escalators — Visible Steps Invariant

### 1. Concept & Formula in Plain English
When an escalator has $N$ steps visible between the bottom and top landings and moves at $e$ steps/sec:
- Walking **with** the escalator: You take $S_p$ steps yourself while the escalator carries you an extra $e \cdot t$ steps in time $t$, so together they add up to the full escalator length $N$:
  $$N = S_p + e \cdot t$$
- Walking **against** the escalator: You have to walk $N$ steps *plus* overcome the $e \cdot t$ steps the escalator pushes you back:
  $$N = S_p - e \cdot t$$

### 2. When to Use It (Question Cue)
- *"Walking up an ascending escalator, A takes $40$ steps in $20$ seconds, while B takes $48$ steps in $12$ seconds. Find the number of visible steps $N$."*

### 3. General Example (Clean Numbers, Single Concept)
> A and B walk up an ascending escalator. A takes $40$ steps and reaches the top in $20$ seconds, while B walks faster, taking $48$ steps to reach the top in $12$ seconds. How many steps are visible on the escalator when it is stationary?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Both walk **with** the escalator: $N = S_p + e \cdot t$.
  2. For A: $N = 40 + 20e$.
  3. For B: $N = 48 + 12e$.
  4. Equate: $40 + 20e = 48 + 12e \implies 8e = 8 \implies e = 1\text{ step/sec}$.
  5. Substitute $e = 1$: $N = 40 + 20(1) = \mathbf{60\text{ steps}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. A took $8$ fewer personal steps than B ($48 - 40 = 8$) because A stayed on the escalator for $8$ extra seconds ($20 - 12 = 8\text{ s}$) and let the escalator carry him!
  2. So the escalator supplies $\frac{8\text{ steps}}{8\text{ seconds}} = 1\text{ step/sec}$.
  3. In A's $20$ seconds, the escalator supplied $20$ steps on top of A's $40$ steps $= \mathbf{60\text{ steps}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using $+$ instead of $-$ when a person walks **down** an upward-moving escalator ($N = S_p - e \cdot t$).

---

## Concept 10: Linear Races (Start of Distance $d$ / Time $t$) & Chained Race Ratios

### 1. Concept & Formula in Plain English
In a race of length $L$:
- **"$A$ beats $B$ by $d$ meters"**: In the exact same time that $A$ runs $L$ meters, $B$ runs $(L - d)$ meters:
  $$\frac{S_A}{S_B} = \frac{L}{L - d}$$
- **"$A$ beats $B$ by $d$ meters or $t$ seconds"**: When $A$ crosses the finish line, $B$ is $d$ meters behind and takes $t$ more seconds to cover that remaining $d$ meters—so **$B$'s speed is immediately $S_B = \frac{d}{t}$**!

### 2. When to Use It (Question Cue)
- *"In a $100\text{ m}$ race, A beats B by $10\text{ m}$ (or $2$ seconds), and B beats C by $10\text{ m}$. By how many meters does A beat C?"*

### 3. General Example (Clean Numbers, Single Concept)
> In a $100\text{ m}$ race, A beats B by $10\text{ m}$ (or $2\text{ seconds}$), and in a $100\text{ m}$ race, B beats C by $10\text{ m}$. Find B's speed and the distance by which A beats C in the $100\text{ m}$ race.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. B covers the final $d = 10\text{ m}$ in $t = 2\text{ s} \implies S_B = \frac{10}{2} = \mathbf{5\text{ m/s}}$.
  2. Speed ratios: $\frac{S_A}{S_B} = \frac{100}{90} = \frac{10}{9}$ and $\frac{S_B}{S_C} = \frac{100}{90} = \frac{10}{9}$.
  3. Multiply to chain: $\frac{S_A}{S_C} = \frac{10}{9} \times \frac{10}{9} = \frac{100}{81}$.
  4. When A runs $100\text{ m}$, C runs $81\text{ m}$, so A beats C by $100 - 81 = \mathbf{19\text{ m}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. When B runs $100\text{ m}$, C runs $90\text{ m}$ ($90\%$ of B's distance).
  2. When A finishes at $100\text{ m}$, B is at $90\text{ m}$, so C is at $90\%$ of $90\text{ m} = 81\text{ m}$ ($\mathbf{19\text{ m}}$ behind A).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Adding the lead distances ($10\text{ m} + 10\text{ m} = 20\text{ m}$) instead of multiplying the distance ratios ($\frac{9}{10} \times \frac{9}{10} = \frac{81}{100} \implies 19\text{ m}$).

---

## Concept 11: Shuttle Runs Between Two Towns ($k$-th Meeting)

### 1. Concept & Formula in Plain English
When two runners start simultaneously from **opposite ends** $P$ and $Q$ (distance $D$ apart) and shuttle back and forth:
- To meet for the **1st time**, together they cover **$1D$**.
- Between the 1st meeting and the 2nd meeting, they walk to the opposite walls and come back together, covering **$+2D$** combined.
- Therefore, at the **$k$-th head-on meeting**, their total combined distance is:
  $$D_{\text{total}} = (2k - 1)D, \qquad D_A = (2k - 1)D \times \frac{S_A}{S_A + S_B}$$
*(If they start from the **same end**, combined distance at the $k$-th head-on meeting is $2kD$.)*

### 2. When to Use It (Question Cue)
- *"A and B start from opposite ends X and Y ($600\text{ m}$ apart) at speeds $3\text{ m/s}$ and $2\text{ m/s}$ and shuttle back and forth. Where do they meet for the 3rd time?"*

### 3. General Example (Clean Numbers, Single Concept)
> Runners A and B start simultaneously from opposite ends X and Y of a $500\text{ m}$ track at speeds $3\text{ m/s}$ and $2\text{ m/s}$ respectively, reversing direction each time they reach an end. At what distance from X do they meet for the 3rd time?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. For the $k = 3$rd meeting from opposite ends, combined distance $= (2(3) - 1) \times 500 = 5 \times 500 = 2500\text{ m}$.
  2. Distance run by A $= 2500 \times \frac{3}{3 + 2} = 1500\text{ m}$.
  3. Break $1500\text{ m}$ into $500\text{ m}$ laps: $1500 = 3 \times 500\text{ m}$ (Lap 1: $X \to Y$; Lap 2: $Y \to X$; Lap 3: $X \to Y$).
  4. At $1500\text{ m}$, A is right at end Y, which is $\mathbf{500\text{ m from X}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In every $500\text{ m}$ combined ($1D$), A covers $300\text{ m}$ and B covers $200\text{ m}$.
  2. At the 3rd meeting ($5D$ combined), A covers $5 \times 300 = 1500\text{ m} = 3$ full track lengths, landing at Y ($\mathbf{500\text{ m from X}}$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using $k \cdot D$ ($3D$) instead of $(2k - 1)D$ ($5D$) for the $k$-th meeting from opposite ends.

---

## Concept 12: Circular Tracks (First Meeting, Start Reunion & Distinct Points $|a \mp b|$)

### 1. Concept & Formula in Plain English
For two runners on a circular track of length $L$ with speeds $v_1 > v_2$ whose **reduced coprime ratio** is $\frac{v_1}{v_2} = \frac{a}{b}$ ($\gcd(a, b) = 1$):
1. **Time for 1st Meeting Anywhere**: $\frac{L}{v_1 - v_2}$ (Same direction) or $\frac{L}{v_1 + v_2}$ (Opposite direction).
2. **Time for 1st Meeting at the Starting Point**: $\text{LCM}\left(\frac{L}{v_1}, \frac{L}{v_2}\right)$ (each runner must finish a whole number of laps).
3. **Number of Distinct Meeting Points on the Track**:
   - **Same Direction**: $a - b$ distinct points.
   - **Opposite Direction**: $a + b$ distinct points.

### 2. When to Use It (Question Cue)
- *"Two runners run around a $400\text{ m}$ circular track at $6\text{ m/s}$ and $4\text{ m/s}$. When do they first meet, when do they meet at the start, and at how many distinct points on the track do they meet?"*

### 3. General Example (Clean Numbers, Single Concept)
> A and B start simultaneously from the same point on a $600\text{ m}$ circular track with speeds $15\text{ m/s}$ and $10\text{ m/s}$. Find:
> (a) Time of 1st meeting (if running in the same direction),
> (b) Time of 1st meeting at the starting point,
> (c) Number of distinct meeting points on the track (same direction vs. opposite direction).

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: $t_{\text{meet}} = \frac{L}{v_1 - v_2} = \frac{600}{15 - 10} = \mathbf{120\text{ seconds}}$.
  2. **Part (b)**: Lap times are $\frac{600}{15} = 40\text{ s}$ and $\frac{600}{10} = 60\text{ s}$. Start reunion $= \text{LCM}(40, 60) = \mathbf{120\text{ seconds}}$.
  3. **Part (c)**: Reduce speed ratio to coprime integers: $\frac{15}{10} = \frac{3}{2}$ ($a = 3, b = 2$).
     - Same direction: $a - b = 3 - 2 = \mathbf{1\text{ distinct point}}$.
     - Opposite direction: $a + b = 3 + 2 = \mathbf{5\text{ distinct points}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. While A completes $3$ laps ($120\text{ s}$), B completes $2$ laps ($120\text{ s}$).
  2. In the same direction, A gains $3 - 2 = 1$ full lap on B right as both arrive back at the starting line—so they meet **only at the starting point ($1$ point)**!
  3. In opposite directions, together they complete $3 + 2 = 5$ laps per cycle, meeting $5$ equally spaced times around the circle ($\mathbf{5\text{ points}}$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting to **reduce the speed ratio to lowest coprime terms** first (e.g., computing $15 - 10 = 5$ points instead of reducing $15:10 \to 3:2$ and computing $3 - 2 = 1$ point).

---

## Concept 13: Clocks & Relative Angular Speed

### 1. Concept & Formula in Plain English
A clock face is a $360^\circ$ circular track:
- Minute hand moves $360^\circ$ in $60\text{ min} \implies \mathbf{6^\circ/\text{min}}$.
- Hour hand moves $30^\circ$ in $60\text{ min} \implies \mathbf{0.5^\circ/\text{min}}$.
- **Relative Angular Speed**: $6^\circ - 0.5^\circ = \mathbf{5.5^\circ/\text{min}} = \frac{11}{2}^\circ/\text{min}$.
- Angle between hands at $H$ hours and $M$ minutes: $\theta = \left|30H - \frac{11}{2}M\right|$.
- Hands coincide every $\frac{360^\circ}{11/2} = \frac{720}{11} = 65\frac{5}{11}\text{ minutes}$ ($11$ times in $12$ hours, $22$ times in $24$ hours).

### 2. When to Use It (Question Cue)
- *"Find the angle between the hour hand and minute hand at 4:20."*
- *"At what time between 3 o'clock and 4 o'clock do the hands of a clock coincide?"*

### 3. General Example (Clean Numbers, Single Concept)
> (a) What is the angle between the minute hand and the hour hand of a clock at 4:20?
> (b) At what exact time between 3:00 and 4:00 do the hands coincide?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: Plug $H = 4, M = 20$ into $\theta = \left|30H - \frac{11}{2}M\right|$:
     $$\theta = \left|30(4) - \frac{11}{2}(20)\right| = |120 - 110| = \mathbf{10^\circ}$$
  2. **Part (b)**: Set $\theta = 0$ with $H = 3$: $30(3) = \frac{11}{2}M \implies M = \frac{180}{11} = \mathbf{16\frac{4}{11}\text{ minutes past 3}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. **Part (a)**: At 4:20, the minute hand is right on the `4` ($120^\circ$). Meanwhile, in $20$ minutes the hour hand has crept forward from the `4` by $20 \times 0.5^\circ = \mathbf{10^\circ}$.
  2. **Part (b)**: At 3:00, the hour hand has a $90^\circ$ head start. The minute hand catches up at $\frac{11}{2}^\circ/\text{min}$, taking $\frac{90}{11/2} = \frac{180}{11} = \mathbf{16\frac{4}{11}\text{ minutes}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Saying the angle at 4:20 is $0^\circ$ by forgetting that the hour hand moves $0.5^\circ$ every single minute!
