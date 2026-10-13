# QA 02: Arithmetic — Ratios, Proportions, Variation, Averages, Mixtures & Alligations

**Canonical Taxonomy Mapping**: `QA > Arithmetic > Ratio, Proportion, Variation & Partnerships`, `Averages, Mixtures & Alligations`  
**Weightage**: ~12–15% of QA (2–4 questions per slot)  
**Priority Tier**: Tier 1 (High-Yield Core)

---

## 1. 30-Second Concept & Formula Blueprint

### 1.1 Ratios, Proportions & Partnerships
- **Equal Ratio Property (Linear Combination Theorem)**:
  If $\frac{a}{b} = \frac{c}{d} = \frac{e}{f} = k$, then for any real scalars $p, q, r$ such that $pb + qd + rf \neq 0$:
  $$\frac{pa + qc + re}{pb + qd + rf} = k$$
  - *Critical Caveat*: If $b + d + f = 0$ (e.g., $\frac{a}{b} = \frac{c}{d} = \frac{e}{f}$ when denominators can sum to zero), then $k$ can take **two** values: the case where $a+c+e \neq 0$ and the case where $a+c+e = 0$.
- **Componendo & Dividendo**:
  $$\frac{a}{b} = \frac{c}{d} \iff \frac{a+b}{a-b} = \frac{c+d}{c-d} \quad (a \neq b,\, c \neq d)$$
- **Effect of Adding Positive Constant $x$ ($x > 0, b > 0$)**:
  - Proper fraction ($0 < a < b$): $\frac{a+x}{b+x} > \frac{a}{b}$ (moves closer to $1$).
  - Improper fraction ($a > b > 0$): $\frac{a+x}{b+x} < \frac{a}{b}$ (moves closer to $1$).
- **Variation Models**:
  - Direct: $y = kx \implies \frac{y_1}{x_1} = \frac{y_2}{x_2}$
  - Inverse: $y = \frac{k}{x} \implies x_1 y_1 = x_2 y_2$
  - Partial / Joint Variation (Classic Train / Hostel Expense Model): $y = a + bx$ or $y = ax + \frac{b}{x}$ (requires 2 data points to solve for constants $a, b$).
- **Partnerships**:
  $$\text{Profit Share Ratio} = (C_1 \times T_1) : (C_2 \times T_2) : (C_3 \times T_3)$$

---

### 1.2 Averages & Assumed Mean Deviation
- **Weighted Average**:
  $$A_{\text{avg}} = \frac{n_1 A_1 + n_2 A_2 + \dots + n_k A_k}{n_1 + n_2 + \dots + n_k}$$
- **Assumed Mean Shortcut**: Pick convenient reference $M$; then:
  $$A_{\text{avg}} = M + \frac{\sum n_i (A_i - M)}{\sum n_i}$$
- **Replacement / Inclusion in a Group of Size $N$**:
  - Member of value $V_{\text{old}}$ replaced by $V_{\text{new}}$:
    $$V_{\text{new}} = V_{\text{old}} + N \cdot \Delta A$$
  - New member joins (group size becomes $N+1$):
    $$V_{\text{new}} = A_{\text{old}} + (N + 1) \cdot \Delta A = A_{\text{new}} + N \cdot \Delta A$$
- **Properties of Arithmetic Progression (AP) Averages**:
  - For any AP, $\text{Average} = \text{Median} = \frac{\text{First Term} + \text{Last Term}}{2}$.
  - Adding $k$ consecutive terms to an AP shifts the average by $\frac{k \cdot d}{2}$.

---

### 1.3 Mixtures, Alligations & Repeated Replacement
- **Alligation / Lever / Seesaw Rule** (mixing quantity $n_1$ at concentration/rate $A_1$ with $n_2$ at $A_2$, where $A_1 \le A_{\text{avg}} \le A_2$):
  $$\frac{n_1}{n_2} = \frac{A_2 - A_{\text{avg}}}{A_{\text{avg}} - A_1}$$
  - **Denominator Rule**: In alligation, the ratio $\frac{n_1}{n_2}$ is ALWAYS the ratio of the **denominator units** of $A_1, A_2$ (e.g., alligating Speeds $\text{km/hr}$ gives ratio of **Times**, NOT distances; alligating Profit $\%$ gives ratio of **Cost Prices**, NOT selling prices).
- **Repeated Removal & Replacement Formula**:
  From a vessel of volume $V$ containing initial concentration $C_0$ of pure liquid, if volume $x$ is drawn out and replaced by water (concentration $0$) $n$ times:
  $$C_{\text{final}} = C_0 \left(1 - \frac{x}{V}\right)^n$$
  - If volumes $x_1, x_2, \dots, x_n$ are replaced in successive operations:
    $$C_{\text{final}} = C_0 \prod_{i=1}^{n} \left(1 - \frac{x_i}{V}\right)$$
  - *Crucial Note*: Only track the **undiluted / non-added component** in the formula $\left(1 - \frac{x}{V}\right)^n$. If water is added, apply the formula to **Milk** fraction, not Water fraction!

---

## 2. Pattern-Recognition Trigger Table

| Question Cue / Wording | Hidden Constraint | Fastest Attack Strategy |
| :--- | :--- | :--- |
| "$\frac{a}{b+c} = \frac{b}{c+a} = \frac{c}{a+b} = k$; find $k$" | $a+b+c$ could be $0$ OR non-zero | Case 1 ($a+b+c \neq 0$): sum numerators/denominators $\implies k = \frac{1}{2}$. Case 2 ($a+b+c = 0$): $b+c = -a \implies k = -1$ |
| "Average of $N$ distinct positive integers is $A$; find the maximum possible value of the largest integer" | All other $N-1$ integers must be minimized ($1, 2, \dots, N-1$) | $\text{Max} = N \cdot A - \frac{(N-1)N}{2}$ |
| "3 vessels of capacities in ratio $p:q:r$ have milk:water in $a_1:b_1, a_2:b_2, a_3:b_3$..." | Total capacities differ across vessels | Multiply $\text{LCM}(a_1+b_1, a_2+b_2, a_3+b_3)$ by $(p, q, r)$ to scale each vessel without fractions |
| "A milkman removes $x\text{ L}$ twice and the final milk:water ratio is $16:9$..." | Ratio of Milk to **Total Volume** is $\frac{16}{16+9} = \frac{16}{25}$, NOT $\frac{16}{9}$ | Set $\left(1 - \frac{x}{V}\right)^2 = \frac{16}{25} \implies 1 - \frac{x}{V} = \frac{4}{5} \implies \frac{x}{V} = \frac{1}{5}$ |
| "Equal quantities taken from two alloys $A$ and $B$ can form a mixture of concentration $C$..." | For 3-component mixtures, $C$ must lie strictly inside the convex hull (min to max) of source concentrations | Check $\min(C_i) < C_{\text{target}} < \max(C_i)$ |
| "Equal amounts of liquid are swapped between Vessel A ($V_A$ L pure milk) and Vessel B ($V_B$ L pure water)..." | Equilibrium swap volume $x^*$ makes concentrations identical in both vessels | Universal Equilibrium Formula: $x^* = \frac{V_A V_B}{V_A + V_B}$ |

---

## 3. Canonical CAT Archetypes & Solved Exemplars

### Archetype 1: Equal Ratio Theorem with Zero-Sum Trap
> **Problem**: If $\frac{x}{y+z-x} = \frac{y}{z+x-y} = \frac{z}{x+y-z} = r$ for non-zero real numbers $x, y, z$, find the sum of all possible values of $r$.

- **First-Principles Method**:
  1. **Case 1**: $x + y + z \neq 0$. By Equal Ratio Property, summing all numerators and denominators gives:
     $$r = \frac{x + y + z}{(y+z-x) + (z+x-y) + (x+y-z)} = \frac{x+y+z}{x+y+z} = 1$$
  2. **Case 2**: $x + y + z = 0 \implies y + z = -x$. Substituting into the first ratio:
     $$r = \frac{x}{-x - x} = -\frac{1}{2}$$
  3. Sum of all possible values of $r = 1 + \left(-\frac{1}{2}\right) = \frac{1}{2}$.

- **30-Second Exam-Hall Speed Shortcut**:
  - Set $x = y = z = 1 \implies r = 1$.
  - Set $x = 1, y = 1, z = -2$ (sum zero) $\implies r = \frac{1}{1 - 2 - 1} = -\frac{1}{2}$. Sum $= \mathbf{0.5}$.

---

### Archetype 2: Partial Replacement vs. Full Replacement
> **Problem**: A jar contains a mixture of two liquids $A$ and $B$ in the ratio $4:1$. When $10\text{ L}$ of the mixture is replaced with $10\text{ L}$ of liquid $B$, the ratio becomes $2:3$. How many liters of liquid $A$ was present in the jar initially?

- **First-Principles Method**:
  1. Liquid $A$ is only removed and never added back; track $A$'s concentration: $C_0 = \frac{4}{5}$, $C_{\text{final}} = \frac{2}{5}$.
  2. Using $C_{\text{final}} = C_0 \left(1 - \frac{x}{V}\right)$:
     $$\frac{2}{5} = \frac{4}{5}\left(1 - \frac{10}{V}\right) \implies 1 - \frac{10}{V} = \frac{1}{2} \implies V = 20\text{ L}$$
  3. Initial quantity of $A = \frac{4}{5} \times 20 = 16\text{ L}$.

- **30-Second Exam-Hall Speed Shortcut (Invariant Scaling)**:
  - Before adding $10\text{ L}$ of $B$, the remaining mixture has $A:B = 4:1$. After adding $10\text{ L}$ of $B$, $A:B = 2:3 = 4:6$.
  - Since $A$ didn't change during the addition step, $B$ increased by $6 - 1 = 5\text{ units} = 10\text{ L} \implies 1\text{ unit} = 2\text{ L}$.
  - Final total volume $= (4 + 6) \times 2 = 20\text{ L}$ (same as initial volume). Initial $A = \frac{4}{5} \times 20 = \mathbf{16\text{ L}}$.

---

### Archetype 3: Moving Averages & Consecutive Outlier Shifts
> **Problem**: The average of $15$ distinct positive integers is $40$. When the smallest and largest integers are removed, the average of the remaining $13$ integers becomes $38$. If the largest integer is at most $85$, what is the minimum possible value of the smallest integer?

- **First-Principles Method**:
  1. Sum of $15$ integers $= 15 \times 40 = 600$.
  2. Sum of remaining $13$ integers $= 13 \times 38 = 494$.
  3. Therefore, $x_{\min} + x_{\max} = 600 - 494 = 106$.
  4. To minimize $x_{\min}$, maximize $x_{\max}$. Since $x_{\max} \le 85$, set $x_{\max} = 85 \implies x_{\min} = 106 - 85 = 21$.
  5. Check feasibility: Can $13$ distinct integers between $22$ and $84$ average to $38$? Minimum sum of $22 + 23 + \dots + 34 = \frac{13 \times 56}{2} = 364 \le 494$ (valid!). Thus $x_{\min} = \mathbf{21}$.

- **30-Second Exam-Hall Speed Shortcut (Deviation Balance)**:
  - The 2 removed items carry $2 \times 40 + 13 \times (40 - 38) = 80 + 26 = 106$.
  - Subtract max cap $85$: $106 - 85 = \mathbf{21}$.

---

## 4. Boundary Conditions, Domain Traps & TITA Pitfalls

1. **Ratio to Fraction Trap in Replacement Problems**:
   - When the final ratio of Milk : Water is given as $81 : 175$, $\left(1 - \frac{x}{V}\right)^n$ equals $\frac{81}{81 + 175} = \frac{81}{256}$, **never** $\frac{81}{175}$.
2. **Alligation Denominator Mismatch**:
   - Alligating two alloys by **weight percentage of gold** gives the ratio of **weights** of the two alloys; alligating two solutions by **cost per liter** gives the ratio of **volumes**; alligating two investments by **ROI %** gives the ratio of **principals invested**.
3. **"Distinct Positive Integers" vs. "Integers" in Average Extrema**:
   - If the problem states "distinct positive integers", the minimum pack for $k$ numbers is $1, 2, \dots, k$ (sum $= \frac{k(k+1)}{2}$), NOT $1, 1, \dots, 1$. Also verify that the second-largest element doesn't collide with the largest element when minimizing!
4. **Partial Replacement Volume Shift**:
   - If $20\text{ L}$ of mixture is removed and only $10\text{ L}$ of water is added back, the total volume changes at each step! Do NOT use $\left(1 - \frac{x}{V}\right)^n$; track absolute quantity of Milk at each step.

---

## 5. Active-Recall Drill (10 Prompts)

<details><summary>Q1: If a:b = 2:3, b:c = 4:5, and c:d = 6:7, find a:b:c:d.</summary>
A: Multiply down columns: a = 2*4*6 = 48, b = 3*4*6 = 72, c = 3*5*6 = 90, d = 3*5*7 = 105. Divide by 3 -> 16 : 24 : 30 : 35.
</details>

<details><summary>Q2: The value of a diamond varies directly as the square of its weight. A diamond breaks into 3 pieces with weights in ratio 1:2:3, causing a loss of Rs. 44,000. Find the original value of the diamond.</summary>
A: Total weight = 1 + 2 + 3 = 6 units. Original value = 6^2 = 36k. Broken value = 1^2 + 2^2 + 3^2 = 14k. Loss = 36k - 14k = 22k = 44,000 -> k = 2,000. Original value = 36 * 2,000 = Rs. 72,000.
</details>

<details><summary>Q3: A bowler's bowling average is 12.4 runs/wicket. He takes 5 wickets for 26 runs in the next match, improving his average by 0.4. Find the number of wickets before the last match.</summary>
A: Alligate runs/wicket: Group 1 = 12.4, Group 2 = 26/5 = 5.2, Combined = 12.0. Ratio of wickets W_old : 5 = (12.0 - 5.2) : (12.4 - 12.0) = 6.8 : 0.4 = 17 : 1 -> W_old = 17 * 5 = 85 wickets.
</details>

<details><summary>Q4: From an 80 L cask of pure wine, 16 L is drawn and replaced with water. This is done 3 times in total. How much wine remains?</summary>
A: Remaining wine = 80 * (1 - 16/80)^3 = 80 * (4/5)^3 = 80 * 64 / 125 = 40.96 L.
</details>

<details><summary>Q5: Vessel A has 40 L of pure milk and Vessel B has 60 L of pure water. Equal quantities x L are drawn from each and poured into the other so both vessels have the same milk concentration. Find x.</summary>
A: Equilibrium swap volume x = (V_A * V_B) / (V_A + V_B) = (40 * 60) / (40 + 60) = 2400 / 100 = 24 L.
</details>

<details><summary>Q6: The average of 7 consecutive odd integers is M. If the next 3 odd integers are included, by how much does the average increase?</summary>
A: Common difference d = 2. Adding k = 3 consecutive terms increases the average of an AP by (k * d)/2 = (3 * 2)/2 = 3.
</details>

<details><summary>Q7: Two solutions have acid concentrations of 30% and 75%. In what ratio should they be mixed to get a solution which, when sold at CP of pure acid, yields 100% profit?</summary>
A: Wait—if mixed together, to get 50% acid concentration: (75 - 50) : (50 - 30) = 25 : 20 = 5 : 4.
</details>

<details><summary>Q8: A and B start a business with Rs. 60,000 and Rs. 80,000. After 4 months, C joins with Rs. 90,000 and A withdraws Rs. 15,000. Find the annual profit-sharing ratio A:B:C.</summary>
A: Track capital-months (in thousands): A = 60*4 + 45*8 = 240 + 360 = 600; B = 80*12 = 960; C = 90*8 = 720. Ratio 600 : 960 : 720 = 5 : 8 : 6.
</details>

<details><summary>Q9: A batsman's average in 20 innings is 45. His highest and lowest scores differ by 110. Excluding these two innings, the average of the remaining 18 innings is 42. Find his highest score.</summary>
A: H + L = 2*45 + 18*(45 - 42) = 90 + 54 = 144. Given H - L = 110 -> H = (144 + 110)/2 = 127.
</details>

<details><summary>Q10: From a container of pure acid, 10 L is replaced with water, and then 10 L of mixture is replaced with water again, leaving acid and water in ratio 9:16. Find the container capacity V.</summary>
A: Final acid fraction = 9 / (9 + 16) = 9/25. Thus (1 - 10/V)^2 = 9/25 -> 1 - 10/V = 3/5 -> 10/V = 2/5 -> V = 25 L.
</details>

---

## CAT 2025 PYQ Edge Examples & Newly Surfaced Patterns

### Newly Surfaced Sub-Topic Variants & Pattern Triggers (CAT 2025)
- **Alternating Dilution & Enrichment Replacement Operator (`CAT_2025_QA_Slot_1` / `CAT2025_S1_QA_Q20`)**: When water replacement (dilution) alternates with pure-acid replacement (enrichment), track the **complement component** during enrichment so both steps become pure multiplicative scaling ($\times \frac{2}{3}$ per step).
- **Two-Vessel Symmetric Swap Conservation (`CAT_2025_QA_Slot_3` / `CAT2025_S3_QA_Q03`)**: Moving $x$ liters from pure vessel $A$ ($V_A$) to pure vessel $B$ ($V_B$) and returning $x$ liters of the mixture yields a final ratio in $A$ equal to $V_B : x$ directly.
- **Sliding-Window Prefix/Suffix Sum Difference (`CAT_2025_QA_Slot_2` / `CAT2025_S2_QA_Q08`)**: $\text{Sum}(1..9) - \text{Sum}(2..9)$ isolates Day 1 in a single subtraction without solving for individual intermediate days.

### Solved CAT 2025 PYQ Edge Exemplars

#### CAT2025_S1_QA_Q13 (`CAT_2025_QA_Slot_1` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Averages, Mixtures & Alligations — *Two-component linear mixture / alligation*
- **Verified Answer**: `15` (Value of B and C = 3300 - 10*120 = 2100 across 20 shares. 90b + 150(20 - b) = 2100 => 60b = 900 => b = 15.)
- **Mental Trigger (`See X -> Do Y`)**: Subtract fixed component A (1200) first, then apply Alligation on the remaining 20 shares at average price 2100/20 = 105 between B (90) and C (150).
- **First-Principles Method**: 10*120 + 90b + 150(20 - b) = 3300 => 4200 - 60b = 3300 => b = 15.
- **30-Second Exam-Hall Speed Shortcut**: If all 20 shares were C (150), value would be 3000. Excess = 3000 - 2100 = 900. Each swap from C to B saves 60, so B = 900 / 60 = 15.
- **Trap Alert & Boundary Condition**: None; straightforward 20-second sitter.

#### CAT2025_S1_QA_Q17 (`CAT_2025_QA_Slot_1` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Ratio, Proportion, Variation & Partnerships — *Total-invariance under internal transfer and cross-multiplication in ratios*
- **Verified Answer**: `(D) 99` (Initial 13x : 9x (sum 22x); after internal transfer of 21, ratio is 19 : 14 (sum 33y). Equating total: LCM(22, 33) = 66k => 39k - 38k = 21 => k = 21 => shifts become 798 and 588. Adding 3m and 8m gives (798+3m)/(588+8m) = 5/4 => m = 9 => total joined = 11m = 99.)
- **Mental Trigger (`See X -> Do Y`)**: New students join in ratio 3 : 8, so total new students MUST be a multiple of 3 + 8 = 11 (eliminating B=12). Also internal transfer keeps total students constant!
- **First-Principles Method**: (13x - 21)/(9x + 21) = 19/14 => x = 63, so shifts have 798 and 588 students. Next, (798 + 3m)/(588 + 8m) = 5/4 => 3192 + 12m = 2940 + 40m => 28m = 252 => m = 9. Total new students = 11m = 99.
- **30-Second Exam-Hall Speed Shortcut**: Scale 13:9 (sum 22) by 3 -> 39:27 (sum 66) and 19:14 (sum 33) by 2 -> 38:28 (sum 66). 1 unit = 21 students! Then 38*21 = 798, 28*21 = 588, and 11m = 99.
- **Trap Alert & Boundary Condition**: Report 11m = 99 (total new students), not m = 9.

#### CAT2025_S1_QA_Q20 (`CAT_2025_QA_Slot_1` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Averages, Mixtures & Alligations — *Alternating dilution (water) and enrichment (pure acid) replacement operations*
- **Verified Answer**: `(B) 27` (Initial acid = 30%. After 20% water replacement: 30% * 0.8 = 24%. After 10% pure acid replacement: 24% * 0.9 + 10% = 31.6%. After 15% water replacement: 31.6% * 0.85 = 26.86%, nearest to 27%.)
- **Mental Trigger (`See X -> Do Y`)**: When replacing with pure acid, track WATER fraction (which gets multiplied by 0.9), or add 10% directly to 0.9 * c_acid; ignore the 200L volume completely!
- **First-Principles Method**: Start with c0 = 30%. Step 1 (replace 20% with water): c1 = 30% * 0.8 = 24%. Step 2 (replace 10% with 100% acid): c2 = 24% * 0.9 + 100% * 0.1 = 31.6%. Step 3 (replace 15% with water): c3 = 31.6% * 0.85 = 26.86%, nearest to 27.
- **30-Second Exam-Hall Speed Shortcut**: Never multiply by 200 litres; work purely in percentages: 30 -> 24 -> 31.6 -> 26.86 -> 27.
- **Trap Alert & Boundary Condition**: In Step 2, replacing 10% of solution with pure acid does NOT multiply acid by 1.10 (which would give 26.4 * 0.85 = 22.44 -> trap D=23).

#### CAT2025_S2_QA_Q05 (`CAT_2025_QA_Slot_2` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Ratio, Proportion, Variation & Partnerships — *Chained ratio scaling with Income = Expenditure + Savings*
- **Verified Answer**: `(B) 3 : 5` (Set E_L = 14, E_M = 21 (ratio 2:3). Then I_L = (6/7)*E_M = 18. Saving S_L = I_L - E_L = 18 - 14 = 4. Since S_L : S_M = 4 : 9, S_M = 9. Thus I_M = E_M + S_M = 21 + 9 = 30. Ratio I_L : I_M = 18 : 30 = 3 : 5.)
- **Mental Trigger (`See X -> Do Y`)**: Since E_L : E_M = 2 : 3 and I_L : E_M = 6 : 7, scale E_M to LCM(3, 7) = 21 so all quantities are integers!
- **First-Principles Method**: Let E_M = 21k. Then E_L = 14k and I_L = 18k. Lakshmi's savings S_L = 18k - 14k = 4k. Since S_L : S_M = 4 : 9, S_M = 9k. Meenakshi's income I_M = E_M + S_M = 21k + 9k = 30k. Ratio I_L : I_M = 18k : 30k = 3 : 5.
- **30-Second Exam-Hall Speed Shortcut**: With E_M = 21, E_L = 14, I_L = 18 => S_L = 4 => S_M = 9 => I_M = 30 => 18:30 = 3:5.
- **Trap Alert & Boundary Condition**: Read carefully that 6 : 7 is the ratio of Income of Lakshmi to Expenditure of Meenakshi (not Income of Lakshmi to Income of Meenakshi).

#### CAT2025_S2_QA_Q08 (`CAT_2025_QA_Slot_2` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Averages, Mixtures & Alligations — *Sliding-window average difference (Sum(1..9) - Sum(2..9) = Day 1)*
- **Verified Answer**: `49` (Sum(1..7) = 420, Sum(1..8) = 504 => Day 8 = 84. Day 9 = 84 - 11 = 73. Sum(1..9) = 504 + 73 = 577. Given Sum(2..9) = 8 * 66 = 528. Thus Day 1 = 577 - 528 = 49.)
- **Mental Trigger (`See X -> Do Y`)**: Day 8 raises the 7-day average from 60 to 63 (+3 across 8 days) => Day 8 = 60 + 8*3 = 84; then shifting the 8-day window from (1..8) to (2..9) raises average from 63 to 66 (+3 across 8 days) => Day 9 - Day 1 = 8*3 = 24!
- **First-Principles Method**: S_7 = 420, S_8 = 504 => d_8 = 84 => d_9 = 73. Also S_{2..9} = 8 * 66 = 528. Therefore d_1 = S_8 + d_9 - S_{2..9} = 504 + 73 - 528 = 49.
- **30-Second Exam-Hall Speed Shortcut**: d_8 = 60 + 8(3) = 84 => d_9 = 73. Window shift (2..9) vs (1..8): d_9 - d_1 = 8(66 - 63) = 24 => d_1 = 73 - 24 = 49!
- **Trap Alert & Boundary Condition**: Days 2 to 9 inclusive is 8 days (not 7 or 9 days).

#### CAT2025_S2_QA_Q20 (`CAT_2025_QA_Slot_2` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Averages, Mixtures & Alligations — *Linear interpolation of mixture cost vs concentration*
- **Verified Answer**: `(B) 5` (Cost increases linearly with coffee%: from 16% (Rs 240) to 36% (Rs 320), a 20% increase in coffee raises price by Rs 80 (Rs 4 per 1% coffee). At Rs 376 (+Rs 56 above 320), coffee% = 36% + 56/4 = 50%. In 10 kg, coffee = 5 kg.)
- **Mental Trigger (`See X -> Do Y`)**: Mixture cost is an affine function of concentration: Delta(Price)/Delta(Coffee%) = (320 - 240)/(36 - 16) = Rs 4 per 1% coffee.
- **First-Principles Method**: Let pure coffee cost C and pure cocoa cost K. Then 0.16C + 0.84K = 240 and 0.36C + 0.64K = 320 => C - K = 400 and K = 176. For a mixture costing 376: K + p(C - K) = 176 + 400p = 376 => p = 0.50. In 10 kg, coffee = 0.50 * 10 = 5 kg.
- **30-Second Exam-Hall Speed Shortcut**: Slope is Rs 4 per 1% coffee. From Rs 320 (36%) to Rs 376 (+56), add 56/4 = 14% -> 50% of 10 kg = 5 kg.
- **Trap Alert & Boundary Condition**: Notice 376 > 320 means the new mixture has a higher coffee percentage than both given mixtures (an external alligation / pure ingredient extrapolation).

#### CAT2025_S3_QA_Q03 (`CAT_2025_QA_Slot_3` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Averages, Mixtures & Alligations — *Two-vessel symmetric transfer invariant (final ratio in A equals 60 : v)*
- **Verified Answer**: `16` (After pouring v litres of alcohol from A into B (60L water), B has v alcohol and 60 water, which is in ratio v : 60. When v litres of this mixture are poured back into A, the ratio of alcohol to water in A is 60 : v. Given 60 : v = 15 : 4 => v = 16.)
- **Mental Trigger (`See X -> Do Y`)**: When v litres are transferred from pure vessel A (volume V) to pure vessel B (volume V) and v litres are transferred back, the final ratio of A-liquid to B-liquid in A is ALWAYS V : v!
- **First-Principles Method**: After step 1, A has (60 - v) alcohol; B has v alcohol and 60 water. Step 2 transfers v*(60/(60+v)) water into A, leaving 60v/(60+v) water and 3600/(60+v) alcohol in A. Their ratio is 3600 : 60v = 60 : v = 15 : 4 => v = 16.
- **30-Second Exam-Hall Speed Shortcut**: By the V : v symmetric transfer identity, 60 : v = 15 : 4 => v = 16 in 5 seconds!
- **Trap Alert & Boundary Condition**: Do not use the repeated-replacement formula (which applies when vessel A stays at constant volume 60 during both steps); here B's volume temporarily becomes 60 + v.

#### CAT2025_S3_QA_Q09 (`CAT_2025_QA_Slot_3` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Ratio, Proportion, Variation & Partnerships — *Total-invariance scaling in two-box internal transfers*
- **Verified Answer**: `272` (Initial ratio 17:7 (sum 24); after shifting 108, ratio is 37:20 (sum 57). Scale to LCM(24, 57) = 456: initial is 17*19 : 7*19 = 323 : 133; after shift is 37*8 : 20*8 = 296 : 160. Shift of 323 - 296 = 27 units = 108 coins => 1 unit = 4 coins. To reach 1:1 (228 : 228), shift 296 - 228 = 68 units = 68 * 4 = 272 coins.)
- **Mental Trigger (`See X -> Do Y`)**: Equate total units before and after internal transfer: 17+7 = 24, 37+20 = 57; LCM(24, 57) = 456 (since 24=3*8, 57=3*19), and 1:1 target is 456/2 = 228 units!
- **First-Principles Method**: (17x - 108)/(7x + 108) = 37/20 => 81x = 6156 => x = 76. Total coins = 24 * 76 = 1824, so 1:1 means 912 coins each. Box A currently has 17(76) - 108 = 1184 coins, so 1184 - 912 = 272 more coins must be shifted.
- **30-Second Exam-Hall Speed Shortcut**: In 456-unit scale: A drops from 323 -> 296 (27 units = 108 => 1 unit = 4 coins) and needs to reach 228 (68 units * 4 = 272 coins).
- **Trap Alert & Boundary Condition**: The question asks how many coins need to be shifted FURTHER (272), not total shifted from the start (108 + 272 = 380).

#### CAT2025_S3_QA_Q20 (`CAT_2025_QA_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Averages, Mixtures & Alligations — *Weighted percentage contribution to overall mean shift*
- **Verified Answer**: `(B) 54000` (A 20% increase in managers' total salary raises the overall company salary bill by 5%, so managers account for 5% / 20% = 1/4 = 25% of the total salary bill, while the 25 engineers account for 75% of the total salary bill (0.75 * 30 * 60000 = 1350000). Average engineer salary = 1350000 / 25 = 54000.)
- **Mental Trigger (`See X -> Do Y`)**: If a 20% raise for managers produces a 5% raise in the overall mean, managers hold 5/20 = 25% of the total wage pool, so engineers hold 75% of the total wage pool!
- **First-Principles Method**: Total initial salary = 30 * 60000 = 1800000. Increase = 5% of 1800000 = 90000 = 20% of managers' total salary => managers' total = 450000. Engineers' total = 1800000 - 450000 = 1350000 across 25 engineers => average = 1350000 / 25 = 54000.
- **30-Second Exam-Hall Speed Shortcut**: Engineers get 75% of total pay while being 25/30 = 5/6 of the headcount, so their average is (3/4) / (5/6) * 60000 = (9/10) * 60000 = 54000!
- **Trap Alert & Boundary Condition**: None; 15-second sitter.
