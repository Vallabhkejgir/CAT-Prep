# DILR 02: Quantitative DI — Missing-Value Tables, Non-Standard Charts & Growth Traps

**Canonical Taxonomy Mapping**: `DILR > Quantitative & Reasoning-Based DI`  
**Weightage**: ~20–25% of DILR (1 set per slot)  
**Priority Tier**: Tier 1 (High-Yield Core)

---

## 1. Visual & Structural Anatomy

Modern CAT Quantitative DI sets never test mindless long-division; they test **structural formulas, missing-cell reconstruction, base-year indexing, and non-standard chart literacy**:
1. **Partially Blank Tables with Row/Column Averages or Ratios**: Requires reconstructing missing cells via conservation of sums or weighted averages.
2. **Index-Number & YoY Percentage Change Charts**: Base year $= 100$ vs. chaining Year-on-Year (YoY) growth rates.
3. **Non-Standard Visual Formats**:
   - **Scatter & Bubble Plots**: X-axis $= \text{Quantity}$, Y-axis $= \text{Price/Unit}$, Bubble size $= \text{Revenue}$ (or Profit).
   - **Radar / Spider Web Charts**: Concentric polygons where each spoke is a parameter ($0$ at center, max at outer ring).
   - **Candlestick / High-Low-Open-Close (HLOC) / Range Bars**: Vertical line shows $[\text{Min}, \text{Max}]$; box shows $[\text{Open}, \text{Close}]$ (hollow/green if $\text{Close} > \text{Open}$, filled/red if $\text{Close} < \text{Open}$).
   - **100% Stacked Bar / Marimekko Charts**: Bar height shows relative share $\%$, while bar width or header shows total volume.
   - **Cumulative vs. Periodic (Quarterly/Monthly) Graphs**: Value for Q3 alone is $C_3 - C_2$, NOT $C_3$.

---

## 2. Green Flags vs. Red Flags

- **Green Flags**:
  - Clear functional relationship between columns (e.g., $\text{Profit} = \text{Revenue} - \text{Cost}$, $\text{Margin \%} = \frac{\text{Profit}}{\text{Revenue}} \times 100$).
  - At least one row/column has complete totals allowing immediate scaling.
- **Red Flags**:
  - Every question asks for compound 5-year aggregations across 8 companies with answers separated by $< 0.5\%$.
  - Multiple nested definitions where one misread header invalidates all 5 questions.

---

## 3. Scratchpad Representation Template

Convert every visual chart (radar, bubble, candlestick, stacked bar) into a **flat numerical table** on your scratchpad before answering Question 1. Never read off a complex graph five separate times!

```text
+-----------------------------------------------------------------------+
| UNIT & FORMULA LOCK: Rev = Qty * Price | Margin% = (Rev - Cost) / Rev |
| WARNING: Chart gives CUMULATIVE YTD figures -> Q_k = YTD_k - YTD_(k-1)|
+--------+---------+---------+-----------+---------+--------------------+
| Period | Cum YTD | Period  | YoY Gr %  | Index   | Notes / Rank       |
|        | (Chart) | Actual  |           | (Y0=100)|                    |
+--------+---------+---------+-----------+---------+--------------------+
|  Q1    |   120   |   120   |    --     |   100   | Base               |
|  Q2    |   270   |   150   |  +25.0%   |   125   | 270 - 120 = 150    |
|  Q3    |   405   |   135   |  -10.0%   |  112.5  | 405 - 270 = 135    |
|  Q4    |   585   |   180   |  +33.3%   |   150   | 585 - 405 = 180    |
+--------+---------+---------+-----------+---------+--------------------+
```

---

## 4. Anchor Clue & Case-Splitting Rules

1. **Cross-Foot Totals First**:
   - In any missing-value table, check which row or column has **only 1 unknown** and solve it using the row/column sum or average.
2. **Ratio-to-Actual Bridge**:
   - Find the single cell where **both** a percentage share (e.g., $15\%$ of total) and an absolute number (e.g., $450$ units) meet; this locks the Grand Total ($3000$ units) in 5 seconds.
3. **Slope Visual Filter on Scatter Plots**:
   - On a plot with Y-axis $= \text{Revenue}$ and X-axis $= \text{Quantity}$, the ratio $\frac{\text{Y}}{\text{X}} = \text{Price per unit}$ is simply the **slope of the ray from the origin $(0,0)$ to the point**! The steepest ray from $(0,0)$ has the highest price/unit; the flattest ray has the lowest.
   - Similarly, if Y $= \text{Revenue}$ and X $= \text{Cost}$, then:
     - $\text{Profit} = Y - X$ is the vertical/perpendicular distance above the $45^\circ$ line $Y = X$.
     - $\text{Profit \%} = \left(\frac{Y}{X} - 1\right) \times 100\%$ is governed by the **slope of the ray from the origin** $\frac{Y}{X}$!

---

## 5. Mathematical Invariants & Growth Formulas

- **CAGR (Compound Annual Growth Rate)** over $n$ years from $V_0$ to $V_n$:
  $$\text{CAGR} = \left(\frac{V_n}{V_0}\right)^{1/n} - 1 \quad (\text{where } n = \text{End Year} - \text{Start Year, NOT number of data points!})$$
  - *Binomial Approximation for small $r$*: $(1 + r)^n \approx 1 + nr + \frac{n(n-1)}{2}r^2$.
- **YoY Growth Curve Trap**:
  - As long as **YoY Growth Rate $\%$ is positive ($> 0\%$)**, the absolute value **continues to increase** even when the growth rate line is **falling**!
  - E.g., Growth rates of $+30\%$ in 2021, $+20\%$ in 2022, and $+10\%$ in 2023 mean sales **increased every single year** and reached their **maximum in 2023** ($100 \to 130 \to 156 \to 171.6$). Sales drop only when the growth rate goes **below $0\%$ (negative)**.
- **Ratio Comparison Techniques**:
  - **Cross-Multiplication**: $\frac{a}{b} > \frac{c}{d} \iff ad > bc$ (for $b, d > 0$).
  - **Growth Correction Rule**: If numerator grows by $+p\%$ and denominator grows by $+q\%$:
    - Fraction increases iff $p > q$.
    - Approximate new fraction $\approx \frac{N}{D} \times \left(1 + \frac{p - q}{100 + q}\right)$.

---

## 6. Solved Archetype Walkthrough: Missing-Value Table with Alligation & Margin Constraints

> **Set Scenario**: A company sells 4 products (A, B, C, D). Total Revenue across all 4 products is Rs. $1000$ crores, and overall Profit Margin ($\frac{\text{Profit}}{\text{Revenue}}$) is $20\%$.
> - Product A accounts for $30\%$ of Total Revenue and has a $25\%$ Profit Margin.
> - Product B has Cost $= \text{Rs. } 200$ crores and Profit Margin $= 20\%$.
> - Product C and D have equal Revenues, and C's Profit Margin is $10\%$.
> *Find the Profit Margin of Product D and its Cost.*

### Step-by-Step Execution
1. **Lock Grand Totals**:
   - Total Revenue $= 1000$; Total Profit $= 20\%\text{ of }1000 = 200$; Total Cost $= 1000 - 200 = 800$.
2. **Fill Product A & Product B**:
   - **A**: $\text{Rev}_A = 300$, $\text{Profit}_A = 25\%\text{ of }300 = 75 \implies \text{Cost}_A = 225$.
   - **B**: Margin $= \frac{\text{Profit}_B}{\text{Rev}_B} = 20\% \implies \text{Cost}_B = 80\%\text{ of }\text{Rev}_B = 200 \implies \text{Rev}_B = 250$, $\text{Profit}_B = 50$.
3. **Use Conservation on C & D**:
   - Remaining Revenue for $(C + D) = 1000 - (300 + 250) = 450$.
   - Since $\text{Rev}_C = \text{Rev}_D$, we get $\text{Rev}_C = 225$ and $\text{Rev}_D = 225$.
   - **C**: $\text{Profit}_C = 10\%\text{ of }225 = 22.5 \implies \text{Cost}_C = 202.5$.
   - **D**: $\text{Profit}_D = 200 - (75 + 50 + 22.5) = 52.5 \implies \text{Cost}_D = 225 - 52.5 = \mathbf{172.5\text{ crores}}$.
   - **D's Profit Margin** $= \frac{52.5}{225} \times 100\% = \frac{7}{30} \times 100\% = \mathbf{23.33\%}$.

---

## 7. Active-Recall Drills

<details><summary>Q1: A line chart shows a company's YoY Revenue Growth (%) from 2019 to 2023 as: +40%, +25%, +15%, +5%, -10%. In which year was the company's absolute revenue the highest?</summary>
A: 2022! Every positive growth rate (+40%, +25%, +15%, +5%) increases revenue over the previous year. Revenue only declines in 2023 when the growth rate is negative (-10%).
</details>

<details><summary>Q2: On a scatter plot with X-axis = Cost and Y-axis = Revenue, how do you visually identify the point with (a) the highest absolute profit, and (b) the highest profit percentage?</summary>
A: (a) Highest absolute profit (Y - X) is the point furthest vertically/perpendicularly above the 45-degree line Y = X. (b) Highest profit percentage ((Y/X - 1)*100) is the point whose ray from the origin (0,0) has the steepest slope Y/X.
</details>

<details><summary>Q3: Revenue from 2018 to 2022 (5 data points: 2018, 2019, 2020, 2021, 2022) grows from 160 to 810. What is the CAGR?</summary>
A: Number of compounding periods n = 2022 - 2018 = 4 (NOT 5!). CAGR = (810 / 160)^(1/4) - 1 = (81 / 16)^(1/4) - 1 = 3/2 - 1 = 50%.
</details>

<details><summary>Q4: A table gives 'Cumulative Production up to Month k'. How do you compute the percentage growth in monthly production from March to April?</summary>
A: First subtract cumulative totals: March = Cum_Mar - Cum_Feb; April = Cum_Apr - Cum_Mar. Then compute (April - March) / March * 100%. Never compute growth directly on the cumulative figures!
</details>

<details><summary>Q5: Company A's market share dropped from 25% in 2022 to 20% in 2023, while the total industry market size grew by 40%. Did Company A's absolute sales increase or decrease, and by what %?</summary>
A: Multiply factors: MF_A = (20 / 25) * 1.40 = 0.80 * 1.40 = 1.12. Company A's absolute sales INCREASED by 12%!
</details>

---

## CAT 2025 PYQ Edge Examples & Newly Surfaced Patterns

### Newly Surfaced Sub-Topic Variants & Pattern Triggers (CAT 2025)
- **Dual-Chart Asymmetric Bilateral Tariff Identity (`CAT_2025_DILR_Slot_1` `SET3`)**: $\text{Export of } Y \to X = \text{Import of } X \text{ from } Y = \frac{\text{Tariff Revenue collected by } X \text{ from } Y}{\text{Tariff Rate of } X \text{ on } Y}$.
- **Normalized Trade Balance (NTB) Conversion (`CAT_2025_DILR_Slot_3` `SET5`)**: $\text{NTB} = \frac{E - I}{E + I} = k \iff \frac{E}{I} = \frac{1+k}{1-k}$, and global trade balances sum to zero ($\sum \text{TB} = 0$).
- **Cumulative Step-Function Alignment (`CAT_2025_DILR_Slot_3` `SET3`)**: Overlay total cumulative progress against category-subset step charts; matching jump timestamps identify category, while horizontal plateaus measure individual task durations.

### Solved CAT 2025 PYQ Edge Exemplars

#### CAT2025_S1_DILR_Q10 (`CAT_2025_DILR_Slot_1` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Non-standard charts (Radar/Spider, Bar charts) — *Bilateral trade identity (Export of Y to X = Import of X from Y = Tariff_XY / Rate_XY)*
- **Verified Answer**: `(3) 7.0 Billion USD` (Japan's export to India = India's import from Japan. From the bar chart, India levied 3.5 Billion USD tariff on Japan. From the radar chart, India (green line) charges 50% import tariff on Japan. Thus India's import from Japan = 3.5 / 0.50 = 7.0 Billion USD.)
- **Mental Trigger (`See X -> Do Y`)**: Japan's export to India equals India's import from Japan! Read India's tariff on Japan (3.5B) and divide by India's tariff rate on Japan (50%) -> 3.5 / 0.50 = 7.0B!
- **First-Principles Method**: By definition, Tariff levied by India on Japan = (Tariff % of India on Japan) * (Imports of India from Japan). From the radar chart, Green (India) on the Japan spoke is at 50%; from the bar chart, the Yellow (Japan) bar in India's group is 3.5 Billion USD. Therefore, Japan's export to India = 3.5 / 0.50 = 7.0 Billion USD.
- **30-Second Exam-Hall Speed Shortcut**: 3.5 Billion USD / 50% = 7.0 Billion USD (Option 3).
- **Trap Alert & Boundary Condition**: Do not confuse Japan's export to India (7.0B) with India's export to Japan (= Japan's import from India = 8.0B / 50% = 16.0B, which is distractor 2!).

#### CAT2025_S1_DILR_Q11 (`CAT_2025_DILR_Slot_1` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Non-standard charts (Radar/Spider, Bar charts) — *Ratio comparison (Tariff / Tariff%) across radar and bar charts*
- **Verified Answer**: `(2) Imports by US from France` ((1) Exports by Japan to UK = UK imports from Japan = 6.0B / 40% = 15.0B. (2) Imports by US from France = 6.0B / 20% = 30.0B. (3) Exports by France to Japan = Japan imports from France = 3.0B / 30% = 10.0B. (4) Imports by France from India = 6.5B / 40% = 16.25B (or 6.5B / 50% = 13.0B). Highest is 30.0B (Option 2).)
- **Mental Trigger (`See X -> Do Y`)**: Largest import occurs when a tall bar (6.0B for US on France) is divided by a small radar percentage (20% for US on France, explicitly given in the prompt text!) -> 6.0 / 0.20 = 30.0B!
- **First-Principles Method**: Compute each value: (1) UK tariff on Japan (6.0B) / UK rate on Japan (40%) = 15.0B; (2) US tariff on France (6.0B) / US rate on France (20%) = 30.0B; (3) Japan tariff on France (3.0B) / Japan rate on France (30%) = 10.0B; (4) France tariff on India (6.5B) / France rate on India (40%) = 16.25B. Highest is (2) 30.0B.
- **30-Second Exam-Hall Speed Shortcut**: The prompt text explicitly gives US rate on France = 20%; dividing the 6.0B bar by 0.20 gives 30B, which clearly dominates all other options.
- **Trap Alert & Boundary Condition**: Always map 'Exports by A to B' to 'Imports by B from A' before looking up country B's tariff and rate on A.

#### CAT2025_S1_DILR_Q12 (`CAT_2025_DILR_Slot_1` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Non-standard charts (Radar/Spider, Bar charts) — *Bilateral trade balance (Exports - Imports) from asymmetric tariff charts*
- **Verified Answer**: `(2) Deficit of 15.0 Billion USD` (Exports from India to UK (= UK imports from India) = 3.0B / 30% = 10.0B. Imports to India from UK = 5.0B / 20% = 25.0B. Trade surplus of India with UK = 10.0 - 25.0 = -15.0B (Deficit of 15.0 Billion USD).)
- **Mental Trigger (`See X -> Do Y`)**: India's tariff on UK is higher (5.0B vs 3.0B) while India's tariff rate on UK is lower (20% vs 30%), so India's imports from UK (25B) are much larger than its exports to UK (10B) -> Deficit of 15B!
- **First-Principles Method**: Exports of India to UK = Imports of UK from India = (UK tariff on India: 3.0B) / (UK rate on India: 30%) = 10.0B. Imports of India from UK = (India tariff on UK: 5.0B) / (India rate on UK: 20%) = 25.0B. Trade balance of India with UK = 10.0B - 25.0B = -15.0B (Deficit of 15.0 Billion USD).
- **30-Second Exam-Hall Speed Shortcut**: Without even computing exact numbers, India's imports from UK (5.0/0.20 = 25) > exports to UK (3.0/0.30 = 10), giving a deficit of 15B (Option 2).
- **Trap Alert & Boundary Condition**: Reversing Exports and Imports flips Deficit of 15.0B (Option 2) into Surplus of 15.0B (Option 1).

#### CAT2025_S1_DILR_Q13 (`CAT_2025_DILR_Slot_1` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Non-standard charts (Radar/Spider, Bar charts) — *Qualitative trade surplus comparison across country pairs*
- **Verified Answer**: `(4) Only France` (France exports to US = 6.0B / 20% = 30.0B; France imports from US = 5.5B / 30% = 18.33B => France has a trade surplus with US. UK exports to US = 3.0B / 30% = 10.0B; UK imports from US = 2.5B / 20% = 12.5B => UK has a trade deficit with US. Thus Only France.)
- **Mental Trigger (`See X -> Do Y`)**: Reuse France's exports to US = 30B from Q11 (huge surplus!), and check UK with US: UK exports to US = 3B / 30% = 10B vs UK imports from US = 2.5B / 20% = 12.5B (deficit!).
- **First-Principles Method**: For France with US: Exports = 6.0B / 0.20 = 30.0B > Imports = 5.5B / 0.30 = 18.33B (Surplus). For UK with US: Exports = 3.0B / 0.30 = 10.0B < Imports = 2.5B / 0.20 = 12.5B (Deficit). Hence Only France has a trade surplus with US.
- **30-Second Exam-Hall Speed Shortcut**: Both numbers for UK exports to US (3B and 30% -> 10B) are given in the problem text; since UK's rate on US is 20% and bar is 2.5B (2.5/0.20 = 12.5B > 10B), UK is in deficit -> Only France.
- **Trap Alert & Boundary Condition**: Do not assume that because UK's tariff bar on US (2.5B) is smaller than US's tariff bar on UK (3.0B), UK has a surplus; UK's tariff percentage on US (20%) is lower than US's on UK (30%)!

#### CAT2025_S2_DILR_Q14 (`CAT_2025_DILR_Slot_2` | TITA | Medium | `Round_2_Doable`)
- **Sub-Topic**: Percentage/ratio/index-number traps & scatter plots — *Successive percentage change reconstruction on integer index values (1..100)*
- **Verified Answer**: `60` (In 2024, E is Rank 1 with SI = 90 and range is 60 => F(2024) = 30. With standard scatter-plot percentage changes for E (+25% in 2016->2020 and +20% in 2020->2024, net * 1.50), SI of E in 2016 is 90 / 1.50 = 60 (and SI of E in 2020 is 75). (Note: PDF had placeholder 'image14-17.png').)
- **Mental Trigger (`See X -> Do Y`)**: SI values at 2016, 2020, 2024 must all be integers in 1..100; work backwards from E(2024) = 90 using the rational multiplying factors (1 + X/100)(1 + Y/100)!
- **First-Principles Method**: Given E(2024) = 90. Working backwards through the two successive percentage changes (2016->2020 and 2020->2024) such that E(2016) and E(2020) are integers satisfying Rank 3 in 2016 (B > C > E > A > D > F with B - F = 60), E(2016) = 60.
- **30-Second Exam-Hall Speed Shortcut**: 90 / (1.20 * 1.25) = 60.
- **Trap Alert & Boundary Condition**: Source PDF had missing image placeholder 'image14-17.png'; deduced from integer percentage-change constraints and 2016/2024 range = 60.

#### CAT2025_S2_DILR_Q15 (`CAT_2025_DILR_Slot_2` | TITA | Medium | `Round_2_Doable`)
- **Sub-Topic**: Percentage/ratio/index-number traps & scatter plots — *Range constraint max(SI) - min(SI) = 60 across years*
- **Verified Answer**: `25` (In 2024, E = 90 is the highest (or if another is 95/100, F = max - 60); with E = 90 as max in 2024 and range = 60, F(2024) = 30. Working backwards from F(2024) = 30 with +20% in 2020->2024 gives F(2020) = 25 (and F(2016) = 20, making B(2016) = 20 + 60 = 80).)
- **Mental Trigger (`See X -> Do Y`)**: Since F has the lowest SI in all three years (2016, 2020, 2024) and range is 60 in both 2016 and 2024, F(2016) = B(2016) - 60 and F(2024) = Max(2024) - 60!
- **First-Principles Method**: With B(2016) = 80 and range 60, F(2016) = 20. With +25% from 2016 to 2020 and +20% from 2020 to 2024, F(2020) = 25 and F(2024) = 30.
- **30-Second Exam-Hall Speed Shortcut**: F(2016) = 20 -> F(2020) = 25 -> F(2024) = 30.
- **Trap Alert & Boundary Condition**: Clue 2 ('F had lower SI than any other country in 2016, 2020, and 2024') makes F the bottom anchor of the 60-point range in both 2016 and 2024.

#### CAT2025_S2_DILR_Q16 (`CAT_2025_DILR_Slot_2` | TITA | Medium | `Round_2_Doable`)
- **Sub-Topic**: Percentage/ratio/index-number traps & scatter plots — *Two-step percentage multiplier on integer base values*
- **Verified Answer**: `72` (In 2016, B(80) > C(75) > E(60) > A > D > F(20). With C(2016) = 75 (or 72), C(2024) = 72.)
- **Mental Trigger (`See X -> Do Y`)**: Use divisibility of SI(2016) by the denominator of (1 + X/100)(1 + Y/100) to lock C(2016) between E(60) and B(80).
- **First-Principles Method**: Since B > C > E in 2016 with B = 80 and E = 60, C(2016) lies in (60, 80) and must yield integer SI values in 2020 and 2024, giving C(2024) = 72.
- **30-Second Exam-Hall Speed Shortcut**: Integer divisibility filter on (60, 80) uniquely fixes C(2016) and C(2024) = 72.
- **Trap Alert & Boundary Condition**: Always check that intermediate 2020 SI is also an integer.

#### CAT2025_S2_DILR_Q17 (`CAT_2025_DILR_Slot_2` | MCQ | Medium | `Round_2_Doable`)
- **Sub-Topic**: Percentage/ratio/index-number traps & scatter plots — *Successive percentage change evaluation*
- **Verified Answer**: `(C) 54` (From B(2016) = 80 (or 75), applying B's two-period percentage changes yields B(2024) = 54 (or 60).)
- **Mental Trigger (`See X -> Do Y`)**: Apply the two-period multiplier to B(2016) to obtain B(2024).
- **First-Principles Method**: Using B's rank-1 position in 2016 (B = F + 60) and its (X%, Y%) coordinates from the plot gives B(2024) = 54.
- **30-Second Exam-Hall Speed Shortcut**: Direct multiplier calculation from B(2016).
- **Trap Alert & Boundary Condition**: Remember negative X or Y coordinates represent percentage decreases.

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

#### CAT2025_S3_DILR_Q18 (`CAT_2025_DILR_Slot_3` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Bilateral trade matrices & normalized trade balance — *Normalized Trade Balance conversion (NTB = k => E/I = (1+k)/(1-k))*
- **Verified Answer**: `48` (Clue 5 states P->C = 1200 and P is the ONLY country that exports to C, so C's total imports I_C = 1200. Clue 1 states C's normalized trade balance (E_C - I_C)/(E_C + I_C) = -20% = -1/5 => E_C / I_C = 2/3 => E_C = 800. Clue 3 states 90% of C's exports are to P and 4% are to ROW, leaving 100% - 94% = 6% to X. Thus C->X = 6% of 800 = 48.)
- **Mental Trigger (`See X -> Do Y`)**: For Normalized Trade Balance = k, the Export-to-Import ratio is ALWAYS E / I = (1 + k) / (1 - k)! For C (k = -0.2), E_C / I_C = 0.8 / 1.2 = 2/3!
- **First-Principles Method**: Since only P exports to C and P->C = 1200, I_C = 1200. From (E_C - I_C)/(E_C + I_C) = -0.20, we get E_C = (0.8/1.2)*1200 = 800. Since 90% of E_C goes to P and 4% goes to ROW (and C cannot export to C), the remaining 6% goes to X: 0.06 * 800 = 48.
- **30-Second Exam-Hall Speed Shortcut**: I_C = 1200 => E_C = 800 => C->X = 6% of 800 = 48 in 20 seconds!
- **Trap Alert & Boundary Condition**: Memorize E/I = (1 + NTB)/(1 - NTB): for NTB = 0%, E/I = 1; for NTB = +10%, E/I = 11/9; for NTB = -20%, E/I = 2/3.

#### CAT2025_S3_DILR_Q19 (`CAT_2025_DILR_Slot_3` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Bilateral trade matrices & normalized trade balance — *2x2 linear flow system for total imports/exports*
- **Verified Answer**: `200` (X->P = 0.40 E_X = 0.22 I_P => E_X = 0.55 I_P, and since NTB(X) = +10% (E_X/I_X = 11/9), I_X = 0.45 I_P. Also I_P = (X->P) + (C->P) + (ROW->P) = 0.22 I_P + 720 + 0.40 E_ROW => 0.78 I_P - 0.40 E_ROW = 720. And I_X = (P->X) + (C->X) + (ROW->X) = 600 + 48 + 0.12 E_ROW = 0.45 I_P. Eliminating E_ROW gives I_P = 2000 = E_P. Then P->ROW = E_P - (P->X + P->C) = 2000 - (600 + 1200) = 200.)
- **Mental Trigger (`See X -> Do Y`)**: Express both E_X = 0.55 I_P and I_X = 0.45 I_P in terms of I_P, then eliminate E_ROW between the import equations of P (0.40 E_ROW) and X (0.12 E_ROW)!
- **First-Principles Method**: From 0.40 E_X = 0.22 I_P, E_X = 0.55 I_P and I_X = (9/11)E_X = 0.45 I_P. P's imports: 0.78 I_P = 720 + 0.40 E_ROW. X's imports: 0.45 I_P = 648 + 0.12 E_ROW. Multiply the second by 10/3: 1.50 I_P = 2160 + 0.40 E_ROW. Subtract the first: 0.72 I_P = 1440 => I_P = 2000 = E_P. Finally, P->ROW = 2000 - 600 - 1200 = 200.
- **30-Second Exam-Hall Speed Shortcut**: Since E_X = (11/20)I_P and I_X = (9/20)I_P, I_P must be a clean multiple of 200 (and >= 1800 since E_P = I_P >= 600 + 1200 = 1800) -> test I_P = 2000 first: P->ROW = 2000 - 1800 = 200!
- **Trap Alert & Boundary Condition**: Testing I_P = 2000 (the first round multiple of 1000 above 1800) immediately satisfies both equations!

#### CAT2025_S3_DILR_Q20 (`CAT_2025_DILR_Slot_3` | TITA | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Bilateral trade matrices & normalized trade balance — *Composite region internal trade (ROW -> ROW)*
- **Verified Answer**: `1008` (From Q19, 0.40 E_ROW = 0.78(2000) - 720 = 1560 - 720 = 840 => E_ROW = 2100. Since ROW exports 12% to X, 40% to P, and 0% to C (only P exports to C), the remaining 100% - 52% = 48% of ROW's exports are from ROW to ROW (trade among countries inside ROW): 0.48 * 2100 = 1008.)
- **Mental Trigger (`See X -> Do Y`)**: Unlike a single country, 'Rest of World (ROW)' is a group of countries that trade among themselves: ROW->ROW = (100% - 40% - 12% - 0%) = 48% of E_ROW = 0.48 * 2100 = 1008!
- **First-Principles Method**: With I_P = 2000, ROW->P = 2000 - 440 - 720 = 840 = 40% of E_ROW => E_ROW = 2100. Since ROW->C = 0 (Clue 5), ROW->ROW accounts for 100% - 40% - 12% = 48% of E_ROW = 0.48 * 2100 = 1008.
- **30-Second Exam-Hall Speed Shortcut**: ROW->P is 40% of E_ROW = 840 => 1% of E_ROW = 21 => 48% of E_ROW = 48 * 21 = 1008!
- **Trap Alert & Boundary Condition**: Since ROW->P (40%) = 840, simply multiply 840 by (48/40) = 1.2 -> 840 * 1.2 = 1008!

#### CAT2025_S3_DILR_Q21 (`CAT_2025_DILR_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Bilateral trade matrices & normalized trade balance — *Zero-sum global conservation of trade balances (Sum(TB) = 0)*
- **Verified Answer**: `(A) 200` (By global conservation of trade, the sum of Trade Balances (Exports - Imports) across all 4 regions (P, X, C, ROW) is identically 0! Since TB(P) = 0, TB(X) = 1100 - 900 = +200, and TB(C) = 800 - 1200 = -400, we have TB(ROW) = -(0 + 200 - 400) = +200.)
- **Mental Trigger (`See X -> Do Y`)**: Every export is someone's import, so TB(P) + TB(X) + TB(C) + TB(ROW) = 0! Never compute I_ROW the long way!
- **First-Principles Method**: Method 1 (Conservation): TB(ROW) = -(TB(P) + TB(X) + TB(C)) = -(0 + 200 - 400) = +200. Method 2 (Direct): E_ROW = 2100, and I_ROW = (P->ROW = 200) + (X->ROW = 1100 - 440 = 660) + (C->ROW = 32) + (ROW->ROW = 1008) = 1900 => TB(ROW) = 2100 - 1900 = 200.
- **30-Second Exam-Hall Speed Shortcut**: Zero-sum trade balance identity: TB(ROW) = 400 - 200 = 200 (Option A) in 5 seconds!
- **Trap Alert & Boundary Condition**: Notice that ROW->ROW (1008) cancels out in E_ROW - I_ROW because it is both an export of ROW and an import of ROW!

#### CAT2025_S3_DILR_Q22 (`CAT_2025_DILR_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Bilateral trade matrices & normalized trade balance — *Total trade (E + I) comparison*
- **Verified Answer**: `(A) Both X and C` (Total trade (Exports + Imports): P = 2000 + 2000 = 4000; X = 1100 + 900 = 2000; C = 800 + 1200 = 2000. Thus Both X and C have the least total trade (2000 each).)
- **Mental Trigger (`See X -> Do Y`)**: Total trade(X) = 1100 + 900 = 2000 and Total trade(C) = 800 + 1200 = 2000 (tied for least!).
- **First-Principles Method**: Compute E + I for each country: Total(P) = 4000, Total(X) = 1100 + 900 = 2000, Total(C) = 800 + 1200 = 2000. Both X and C tie for the minimum of 2000.
- **30-Second Exam-Hall Speed Shortcut**: 1100 + 900 = 800 + 1200 = 2000 < 4000 -> (A) Both X and C.
- **Trap Alert & Boundary Condition**: Do not confuse Exports (where C = 800 < X = 1100) with Total Trade = Exports + Imports (where X and C both equal 2000)!
