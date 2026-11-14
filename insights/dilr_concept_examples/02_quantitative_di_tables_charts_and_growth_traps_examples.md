# DILR 02 Concept & Grid-Evolution Examples: Quantitative DI, Non-Standard Charts & Growth Traps

> **Companion Reference**: [`../topic_summaries/dilr/02_quantitative_di_tables_charts_and_growth_traps.md`](../topic_summaries/dilr/02_quantitative_di_tables_charts_and_growth_traps.md) | [`DILR_Archetype_Templates.md`](../high_recall/cheat_sheets/DILR_Archetype_Templates.md)

---

## Concept 1: Missing-Value Tables — Cross-Footing Sums & Ratio-to-Actual Bridges

### 1. Concept & Invariant in Plain English
In any partially blank table where rows and columns add up to totals:
1. **Cross-Footing Invariant**: $\sum (\text{Row Totals}) = \sum (\text{Column Totals}) = \text{Grand Total}$.
2. **One-Unknown Rule**: Always scan for a row or column that has **only 1 blank cell** left, subtract the known cells from the total, and watch the rest of the table fall like dominoes.
3. **Bipartite Group Conservation**: When entities are split into Group X and Group Y, total outgoing from X to Y equals total incoming to Y from X ($\sum \text{Out}(X \to Y) = \sum \text{In}(Y \leftarrow X)$).

### 2. When to Use It (Set / Question Cue)
- A table with missing entries (`?` or blanks) alongside Row Totals, Column Averages, or Percentage Shares.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Three stores (A, B, C) sell shirts and trousers:
> - Store A sold $40$ shirts, and its total items sold was $100$.
> - Store B sold $50$ trousers.
> - Store C sold $30$ shirts and $40$ trousers.
> - Across all three stores, the total number of shirts sold equaled the total number of trousers sold.
> *Reconstruct the complete table.*

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Stage 0 (Empty Table with Given Numbers) $\to$ Stage 1 (Row A & Row C Sums)**:
  ```text
  Store | Shirts | Trousers | Total
  ------+--------+----------+-------
    A   |   40   |  [60] (1)|  100
    B   |  [80]  |    50    | [130]
    C   |   30   |    40    | [ 70] (2)
  ------+--------+----------+-------
  Total | [150]  | [150] (3)| [300]
  ```
  1. **Row A**: Trousers $= 100 - 40 = \mathbf{60}$.
  2. **Row C**: Total $= 30 + 40 = \mathbf{70}$.
  3. **Trousers Column**: Total Trousers $= 60 + 50 + 40 = \mathbf{150}$.
  4. **Equal Column Totals**: Total Shirts $=$ Total Trousers $= \mathbf{150} \implies$ Store B Shirts $= 150 - (40 + 30) = \mathbf{80}$, and Store B Total $= 80 + 50 = \mathbf{130}$.
- **30-Second Invariant / Ratio Shortcut**:
  - To find Store B's shirts directly: $\text{Shirts}_B - \text{Trousers}_B = (\text{Trousers}_A - \text{Shirts}_A) + (\text{Trousers}_C - \text{Shirts}_C) = (60 - 40) + (40 - 30) = +30 \implies \text{Shirts}_B = 50 + 30 = \mathbf{80}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Introducing $x, y, z$ algebra variables when a single row/column subtraction locks the missing number in 3 seconds.

---

## Concept 2: YoY Growth Rate Curve vs. Absolute Peak & CAGR $(n - 1)$ Period Trap

### 1. Concept & Invariant in Plain English
1. **The Falling Growth-Rate Illusion**: When a chart plots **Year-on-Year (YoY) Percentage Growth Rate** on the Y-axis, **any point above $0\%$ means the absolute value is GROWING**! If growth rates are $+40\%$ in 2021, $+20\%$ in 2022, and $+5\%$ in 2023, the line on the chart slopes downward, but **actual sales went UP every single year** and peaked in **2023**! Sales only drop when the growth rate dips **below the $0\%$ axis (negative)**.
2. **CAGR Interval Count ($n = \text{End Year} - \text{Start Year}$)**: Across 5 listed years (2020, 2021, 2022, 2023, 2024), there are **$2024 - 2020 = 4$ annual jumps**, NOT $5$:
   $$\text{CAGR} = \left(\frac{V_{\text{end}}}{V_{\text{start}}}\right)^{1/(\text{End} - \text{Start})} - 1$$

### 2. When to Use It (Set / Question Cue)
- Line charts showing *"Annual % Change / YoY Growth %"* or questions asking for *"Compound Annual Growth Rate from Year X to Year Y"*.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> A company's revenue in 2020 was Rs. $100$ crores. Its YoY revenue growth rates for 2021, 2022, 2023, and 2024 were $+50\%$, $+20\%$, $+10\%$, and $-10\%$ respectively.
> (a) In which year was the company's absolute revenue the highest?
> (b) If another firm grew from Rs. $100$ crores in 2020 to Rs. $207.36$ crores in 2024, what was its CAGR over 2020–2024?

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Step-by-Step Conversion Table**:
  ```text
  Year | YoY Growth % | Direction of Revenue | Absolute Revenue (Rs. Cr)
  -----+--------------+----------------------+--------------------------
  2020 |     Base     |          --          | 100.0
  2021 |     +50%     |      Increasing      | 100 * 1.50 = 150.0
  2022 |     +20%     |      Increasing      | 150 * 1.20 = 180.0
  2023 |     +10%     |  Increasing (PEAK!)  | 180 * 1.10 = 198.0
  2024 |     -10%     |      Decreasing      | 198 * 0.90 = 178.2
  ```
  - **Part (a)**: Highest absolute revenue is in **2023** (Rs. $198$ Cr), right before the growth rate turned negative in 2024!
  - **Part (b)**: Number of intervals $n = 2024 - 2020 = 4$. Since $\frac{207.36}{100} = 2.0736 = (1.2)^4$, $\text{CAGR} = 1.2 - 1 = \mathbf{20\%}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Looking at the highest point on a YoY Growth $\%$ chart (`+50%` in 2021) and picking **2021** as the year of maximum revenue!

---

## Concept 3: Cumulative (YTD / Step-Function) vs. Periodic Charts

### 1. Concept & Invariant in Plain English
When a chart or table reports **Cumulative figures** (e.g., *Year-to-Date sales up to Quarter $k$*, or *Total puzzles solved by minute $t$*), the value for Period $k$ alone is the **step difference** between Period $k$ and Period $k - 1$:
$$\text{Actual}_k = \text{Cumulative}_k - \text{Cumulative}_{k-1}$$
On a **cumulative step-function progress chart** (where total tasks solved jumps up by $+1$ each time a task finishes), the **horizontal width of a flat step** between jump $(k-1)$ and jump $k$ is the exact time spent solving Task $k$!

### 2. When to Use It (Set / Question Cue)
- Charts titled *"Cumulative Revenue / YTD Output"* or step charts showing *"Number of tasks completed by time $t$"*.

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> A factory's **cumulative** output from Q1 to Q4 is: `Q1 = 100`, `Q2 = 250`, `Q3 = 370`, `Q4 = 550`. Find the quarter with the highest standalone production and the percentage growth in quarterly production from Q2 to Q3.

### 4. Step-by-Step Grid Evolution (Two Ways)
- **De-cumulation Table (Always write the `Standalone` column first!)**:
  ```text
  Quarter | Cumulative (Given) | Standalone = Cum(k) - Cum(k-1)
  --------+--------------------+--------------------------------
    Q1    |        100         | 100
    Q2    |        250         | 250 - 100 = 150
    Q3    |        370         | 370 - 250 = 120
    Q4    |        550         | 550 - 370 = 180 (Highest!)
  ```
  - Highest standalone quarter: **Q4 ($180$ units)**.
  - Growth from Q2 ($150$) to Q3 ($120$): $\frac{120 - 150}{150} \times 100\% = \mathbf{-20\%}$ (a $20\%$ decrease!).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Computing Q2-to-Q3 growth on the cumulative numbers ($\frac{370 - 250}{250} = +48\%$) instead of the standalone quarterly numbers ($\frac{120 - 150}{150} = -20\%$).

---

## Concept 4: Scatter Plots — Visual Origin-Ray Slope ($Y/X$) & $45^\circ$ Diagonal Distance ($Y - X$)

### 1. Concept & Invariant in Plain English
When a scatter plot puts one variable on the X-axis (e.g., $\text{Quantity}$ or $\text{Cost}$) and another on the Y-axis (e.g., $\text{Revenue}$):
1. **Ratio $\frac{Y}{X}$ (e.g., $\text{Price} = \frac{\text{Revenue}}{\text{Quantity}}$, or $\frac{\text{Revenue}}{\text{Cost}} = 1 + \text{Profit \%}$)**: Equals the **slope of the straight ray drawn from the Origin $(0, 0)$ to that point**! You don't need to divide 6 pairs of numbers—just lay your pen through $(0, 0)$ and sweep counter-clockwise: the **steepest ray** has the highest $\frac{Y}{X}$ ratio!
2. **Difference $Y - X$ (e.g., $\text{Profit} = \text{Revenue} - \text{Cost}$)**: Draw the $45^\circ$ line $Y = X$; points **above** the line have $Y > X$ (profit), and the point **furthest vertically above** the $Y = X$ line has the largest absolute difference $Y - X$!

### 2. When to Use It (Set / Question Cue)
- Any scatter plot asking *"Which company has the highest Revenue per Employee / Profit Margin % / Absolute Profit?"*

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> On a scatter plot of X = Cost (Rs. Lakh) and Y = Revenue (Rs. Lakh), four firms are plotted at:
> `A(20, 30)`, `B(50, 70)`, `C(80, 105)`, `D(40, 50)`.
> Without computing all 4 percentages, identify which firm has (a) the highest absolute profit, and (b) the highest profit percentage on cost.

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Table & Visual Ray Comparison**:
  ```text
  Firm | Cost (X) | Rev (Y) | Profit (Y - X) [Height above Y=X] | Slope Y/X [Ray from (0,0)]
  -----+----------+---------+-----------------------------------+----------------------------
   A   |    20    |   30    | 30 - 20 = 10                      | 30/20 = 1.50 (+50% MAX!)
   B   |    50    |   70    | 70 - 50 = 20                      | 70/50 = 1.40 (+40%)
   C   |    80    |  105    | 105 - 80 = 25 (MAX Profit!)       | 105/80 = 1.31 (+31.25%)
   D   |    40    |   50    | 50 - 40 = 10                      | 50/40 = 1.25 (+25%)
  ```
  - **Highest Absolute Profit ($Y - X$)**: **Firm C (Rs. $25$ Lakh)**.
  - **Highest Profit $\%$ ($\frac{Y}{X} - 1$)**: **Firm A ($+50\%$)** (steepest ray from $(0,0)$!).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Confusing the highest point on the chart (`C` at $Y = 105$) with the steepest slope from the origin (`A` at $\frac{30}{20} = 1.50$).

---

## Concept 5: Radar / Spider Charts, Candlestick (HLOC) Charts & Asymmetric Bilateral Trade

### 1. Concept & Invariant in Plain English
1. **Radar / Spider Charts**: Each spoke radiates from the center ($0$) outward (max). If Country X's polygon hits $40\%$ on the "Japan" spoke, that represents **X's rate on Japan** (NOT Japan's rate on X!).
2. **Bilateral Trade Identity**: In any trade matrix between countries, **Exports from $Y$ to $X$ are identical to Imports of $X$ from $Y$**:
   $$\text{Export}(Y \to X) = \text{Import}(X \leftarrow Y) = \frac{\text{Tariff Collected by } X \text{ on } Y}{\text{Tariff Rate of } X \text{ on } Y}$$
3. **Normalized Trade Balance ($\text{NTB} = \frac{E - I}{E + I} = k$)**: By Componendo & Dividendo, $\frac{\text{Exports } E}{\text{Imports } I} = \frac{1 + k}{1 - k}$, and across a closed world, $\sum (\text{Exports} - \text{Imports}) = 0$.

### 2. When to Use It (Set / Question Cue)
- Radar charts + Bar charts of tariffs/trade, or Normalized Trade Balance tables (`CAT 2025 DILR Slot 1 Set 3` & `Slot 3 Set 5`).

### 3. General Mini-Set Example (Clean Numbers, Single Concept)
> Country A charges a $25\%$ import tariff on goods imported from Country B, and collects Rs. $50$ Billion in tariff revenue from Country B. Meanwhile, Country B charges a $20\%$ import tariff on goods imported from Country A, and collects Rs. $30$ Billion in tariff revenue from Country A. Find Country A's trade balance (Exports $-$ Imports) with Country B.

### 4. Step-by-Step Grid Evolution (Two Ways)
- **Step-by-Step Bilateral Table**:
  ```text
  Flow Direction          | Who Collects Tariff? | Tariff Collected | Tariff Rate | Trade Value = Tariff / Rate
  ------------------------+----------------------+------------------+-------------+----------------------------
  A's Imports from B      | Country A            |   50 Billion     |     25%     | 50 / 0.25 = 200 Billion
  A's Exports to B        | Country B            |   30 Billion     |     20%     | 30 / 0.20 = 150 Billion
  (= B's Imports from A!) |                      |                  |             |
  ```
  - **Country A's Trade Balance with B** $= \text{Exports}(A \to B) - \text{Imports}(A \leftarrow B) = 150 - 200 = \mathbf{-50\text{ Billion}}$ (a Trade Deficit of $50$ Billion).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Looking up **Country A's** tariff to find Country A's **exports**—remember that **imports** are taxed by the receiving country, so A's exports to B are taxed by **Country B**!
