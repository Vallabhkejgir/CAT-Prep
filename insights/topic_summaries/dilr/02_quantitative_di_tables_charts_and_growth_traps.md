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
