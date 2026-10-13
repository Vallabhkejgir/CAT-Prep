# QA 01: Arithmetic — Percentages, Profit & Loss, Discount, Faulty Weights, SI & CI, Installments

**Canonical Taxonomy Mapping**: `QA > Arithmetic > Percentages & Successive Change`, `Profit, Loss, Discount & Faulty Weights`, `Simple & Compound Interest, Installments`  
**Weightage**: ~15–18% of QA (3–4 questions per slot)  
**Priority Tier**: Tier 1 (High-Yield Core)

---

## 1. 30-Second Concept & Formula Blueprint

### 1.1 Percentages & Successive Change
- **Multiplying Factor (MF)**:
  - Increase by $p\%$: $\text{MF} = 1 + \frac{p}{100}$
  - Decrease by $q\%$: $\text{MF} = 1 - \frac{q}{100}$
  - Validity: $q \le 100$ for non-negative physical quantities.
- **Successive Percentage Change**:
  - Two successive changes of $a\%$ and $b\%$ (with sign):
    $$\text{Net \% Change} = \left(a + b + \frac{ab}{100}\right)\%$$
  - Three successive changes of $a\%, b\%, c\%$:
    $$\text{Net \% Change} = \left(a + b + c + \frac{ab + bc + ca}{100} + \frac{abc}{10000}\right)\%$$
  - Equal increase and decrease by $x\%$: Always a net loss of $\left(\frac{x}{10}\right)^2\% = \frac{x^2}{100}\%$.
- **Product Constancy ($A \times B = \text{Constant}$, e.g., $\text{Price} \times \text{Consumption} = \text{Expenditure}$)**:
  - If $A$ increases by $\frac{a}{b}$, then $B$ must decrease by $\frac{a}{b + a}$ to keep $A \times B$ constant.
  - If $A$ decreases by $\frac{a}{b}$, then $B$ must increase by $\frac{a}{b - a}$ ($b > a$) to keep $A \times B$ constant.
- **Base-Shift Identity**:
  - If $X$ is $\frac{a}{b}$ more than $Y$, then $Y$ is $\frac{a}{a+b}$ less than $X$.
  - Watch the wording: "$X$ is increased **by** $250\%$" means $X_{\text{new}} = 3.5X$; "$X$ is increased **to** $250\%$" means $X_{\text{new}} = 2.5X$.

#### High-Speed Fraction–Percentage Conversion Table
| Fraction | Percentage | Decimal | Fraction | Percentage | Decimal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $1/6$ | $16.66\%$ | $0.1667$ | $1/12$ | $8.33\%$ | $0.0833$ |
| $1/7$ | $14.28\%$ | $0.1429$ | $1/13$ | $7.69\%$ | $0.0769$ |
| $1/8$ | $12.50\%$ | $0.1250$ | $1/14$ | $7.14\%$ | $0.0714$ |
| $1/9$ | $11.11\%$ | $0.1111$ | $1/15$ | $6.66\%$ | $0.0667$ |
| $1/11$ | $9.09\%$ | $0.0909$ | $1/16$ | $6.25\%$ | $0.0625$ |

---

### 1.2 Profit, Loss, Discount & Faulty Weights
- **Core Chain**:
  $$\text{CP} \xrightarrow{+\text{Markup } m\%} \text{MP} = \text{CP}\left(1 + \frac{m}{100}\right) \xrightarrow{-\text{Discount } d\%} \text{SP} = \text{MP}\left(1 - \frac{d}{100}\right)$$
- **Net Profit % from Markup $m\%$ and Discount $d\%$**:
  $$p = m - d - \frac{md}{100}$$
- **CP to MP Direct Ratio** (given Profit $p\%$ and Discount $d\%$):
  $$\frac{\text{CP}}{\text{MP}} = \frac{100 - d}{100 + p}$$
- **Margin vs. Markup**:
  - **Markup / Profit on CP**: $\frac{\text{SP} - \text{CP}}{\text{CP}}$
  - **Gross Margin / Profit on SP**: $\frac{\text{SP} - \text{CP}}{\text{SP}}$
  - Conversion: If profit on CP is $\frac{a}{b}$, profit on SP is $\frac{a}{b+a}$.
- **Two Items Sold at Same SP ($S_1 = S_2 = S$)**:
  - One at $+x\%$ profit, one at $-x\%$ loss $\implies$ Always net loss of $\left(\frac{x}{10}\right)^2\%$, and:
    $$\text{Loss Amount} = \frac{2S}{\left(\frac{100}{x}\right)^2 - 1}$$
- **Dishonest Dealer & Faulty Weights (Universal Multiplying Factor Method)**:
  $$\text{Overall MF} = \left(\frac{\text{Price Charged}}{\text{Cost Incurred}}\right) \times \left(\frac{\text{True Weight Claimed}}{\text{Actual Weight Dispensed}}\right)$$
  - *Buying cheat*: If a meter scale reads $110\text{ cm}$ when buying $100\text{ cm}$ worth of payment, $\text{MF}_{\text{buy}} = \frac{110}{100}$.
  - *Selling cheat*: If a $1\text{ kg}$ weight actually weighs $800\text{ g}$, the shopkeeper claims $1000\text{ g}$ and gives $800\text{ g}$, so $\text{MF}_{\text{sell}} = \frac{1000}{800} = \frac{5}{4}$ ($+25\%$ profit, NOT $20\%$).

---

### 1.3 Simple Interest (SI), Compound Interest (CI) & Installments
- **Simple Interest**:
  $$\text{SI} = \frac{P \cdot R \cdot T}{100}, \quad A = P\left(1 + \frac{RT}{100}\right)$$
- **Compound Interest** (compounded $k$ times per year at nominal annual rate $R\%$):
  $$A = P\left(1 + \frac{R}{100k}\right)^{kT}, \quad \text{Effective Annual Rate (EAR)} = \left[\left(1 + \frac{R}{100k}\right)^k - 1\right] \times 100\%$$
- **CI vs. SI Difference Shortcuts** (for same $P$ and annual rate $r = \frac{R}{100}$):
  - **2 Years**: $\text{CI}_2 - \text{SI}_2 = P r^2 = \text{SI}_1 \cdot r$
  - **3 Years**: $\text{CI}_3 - \text{SI}_3 = P r^2 (3 + r)$
  - **Ratio for 3 vs. 2 Years**: $\frac{\text{CI}_3 - \text{SI}_3}{\text{CI}_2 - \text{SI}_2} = 3 + r = 3 + \frac{R}{100}$
- **Pascal's Triangle Tree for CI**:
  - 2 years: $2 \cdot (Pr) + 1 \cdot (Pr^2)$
  - 3 years: $3 \cdot (Pr) + 3 \cdot (Pr^2) + 1 \cdot (Pr^3)$
  - 4 years: $4 \cdot (Pr) + 6 \cdot (Pr^2) + 4 \cdot (Pr^3) + 1 \cdot (Pr^4)$
- **Equal Installments (Loan Amortization)**:
  - **CI Installments (Present Value Method — Standard CAT default)**: For $n$ equal installments of $X$ at rate $r = \frac{R}{100}$ per period on principal $P$:
    $$P = \frac{X}{(1+r)^1} + \frac{X}{(1+r)^2} + \dots + \frac{X}{(1+r)^n} = \frac{X}{r}\left[1 - (1+r)^{-n}\right]$$
  - **SI Installments (Total Debt Settlement at End of Term $n$)**:
    $$\text{Total Amount Due } P\left(1 + nr\right) = \sum_{k=1}^{n} X\left[1 + (n-k)r\right] = nX + \frac{n(n-1)}{2}Xr$$

---

## 2. Pattern-Recognition Trigger Table

| Question Cue / Wording | Hidden Constraint | Fastest Attack Strategy |
| :--- | :--- | :--- |
| "Price rises by $p\%$; by what $\%$ must consumption drop so expenditure increases by only $k\%$?" | $\text{Exp} = P \times C$ is NOT constant here; $\text{MF}_{\text{Exp}} = 1 + \frac{k}{100}$ | Solve $\left(1+\frac{p}{100}\right) \times \text{MF}_C = 1+\frac{k}{100} \implies \text{MF}_C = \frac{100+k}{100+p}$ |
| "Fresh fruit has $80\%$ water; dry fruit has $20\%$ water..." | Water evaporates; **Pulp/Solid mass is invariant** | Equate solid mass: $M_{\text{fresh}} \times (1 - 0.80) = M_{\text{dry}} \times (1 - 0.20)$ |
| "Shopkeeper gives $n$ articles free on buying $m$ articles after a $d\%$ discount..." | Effective discount acts on $(m+n)$ articles | $\text{MF}_{\text{free}} = \frac{m}{m+n}$; Combine: $\frac{\text{SP}}{\text{MP}} = \frac{m}{m+n} \times \left(1 - \frac{d}{100}\right)$ |
| "After 2% discount profit is $P_1$; after 5% discount profit is $P_2$..." | CP and MP are fixed; $\Delta \text{SP} = \Delta(\text{Discount \%}) \times \text{MP}$ | Directly set $(5\% - 2\%)\text{ of MP} = P_1 - P_2$ to find MP in 5 seconds |
| "Scale expands by $10\%$ in summer / dealer cheats by $x\%$ both ways..." | Buying and selling errors compound multiplicatively, not additively | $\text{MF}_{\text{net}} = \left(\frac{100+x}{100}\right)\left(\frac{100}{100-x}\right)$ if scale reading is manipulated; always check physical grams given vs. claimed |
| "CI for 3rd year vs. CI for 3 years" | "CI for $n$-th year" $= A_n - A_{n-1} = P r (1+r)^{n-1}$, NOT $\text{CI}_n$ | Write $I_1 = Pr, I_2 = Pr(1+r), I_3 = Pr(1+r)^2$; successive year interests form a GP with ratio $(1+r)$ |
| "A sum becomes $k$ times in $t$ years under CI; when does it become $k^m$ times?" | Exponential growth: $(1+r)^t = k$ | Raise to power $m$: $(1+r)^{mt} = k^m \implies$ Time $= m \times t$ years |

---

## 3. Canonical CAT Archetypes & Solved Exemplars

### Archetype 1: Multi-Stage Dishonest Dealer with Markup & Adulteration
> **Problem**: A merchant buys pure milk, adds $20\%$ water (free of cost), marks up the price by $25\%$ above cost price per liter, gives a $10\%$ discount to customers, and uses a faulty measuring vessel that dispenses $900\text{ mL}$ instead of $1\text{ L}$. Find his net profit percentage.

- **First-Principles Method**:
  1. Let CP of $1000\text{ mL}$ of pure milk be Rs. $1000$ (Rs. $1/\text{mL}$).
  2. Adding $20\%$ water gives $1200\text{ mL}$ of mixture at total cost Rs. $1000$.
  3. Nominal MP per $1000\text{ mL}$ claimed $= 1000 \times 1.25 = \text{Rs. } 1250$.
  4. After $10\%$ discount, SP per $1000\text{ mL}$ claimed $= 1250 \times 0.90 = \text{Rs. } 1125$.
  5. Since each "liter" sold actually uses only $900\text{ mL}$ of mixture, $1200\text{ mL}$ of mixture yields $\frac{1200}{900} = \frac{4}{3}$ "claimed liters".
  6. Total Revenue $= \frac{4}{3} \times 1125 = \text{Rs. } 1500$.
  7. Net Profit $\% = \frac{1500 - 1000}{1000} \times 100\% = 50\%$.

- **30-Second Exam-Hall Speed Shortcut (Chain of Multiplying Factors)**:
  $$\text{MF}_{\text{net}} = \underbrace{\frac{6}{5}}_{\text{20\% water}} \times \underbrace{\frac{5}{4}}_{\text{25\% markup}} \times \underbrace{\frac{9}{10}}_{\text{10\% discount}} \times \underbrace{\frac{10}{9}}_{\text{900 mL for 1000 mL}} = \frac{6}{4} = 1.50 \implies \mathbf{50\%\text{ Profit}}$$

---

### Archetype 2: Difference Between 3-Year and 2-Year CI-SI Gaps
> **Problem**: For a certain principal and annual interest rate $R\%$, the difference between Compound Interest and Simple Interest for 2 years is Rs. $120$, and for 3 years is Rs. $378$. Find the Principal $P$.

- **First-Principles Method**:
  1. Given $Pr^2 = 120$ and $Pr^2(3 + r) = 378$, where $r = \frac{R}{100}$.
  2. Divide the second equation by the first: $3 + r = \frac{378}{120} = \frac{63}{20} = 3.15 \implies r = 0.15$ ($R = 15\%$).
  3. Substitute $r = \frac{3}{20}$ into $Pr^2 = 120$: $P \times \frac{9}{400} = 120 \implies P = \frac{48000}{9} = \text{Rs. } 5333.33$.

- **30-Second Exam-Hall Speed Shortcut (Tree Inspection)**:
  - In a 2-year CI tree, the single secondary interest block is $x = 120$.
  - In a 3-year CI tree, the secondary blocks are $3x = 360$, and the tertiary block is $x \cdot r = 378 - 360 = 18$.
  - Thus $r = \frac{18}{120} = \frac{3}{20}$, and $P = \frac{120}{(3/20)^2} = \frac{16000}{3}$.

---

### Archetype 3: Two Equal CI Installments with Present Value Decomposition
> **Problem**: A man borrows Rs. $21,000$ at $10\%$ p.a. compound interest and repays it in two equal annual installments at the end of the 1st and 2nd years. Find the value of each installment $X$.

- **First-Principles Method**:
  $$21000 = \frac{X}{1.1} + \frac{X}{1.1^2} = \frac{10}{11}X + \frac{100}{121}X = \frac{210}{121}X \implies X = \text{Rs. } 12,100$$

- **30-Second Exam-Hall Speed Shortcut (Ratio Scaling)**:
  - Rate $10\% = \frac{1}{10} \implies$ Principal : Installment ratio for Yr 1 is $10 : 11 = 110 : 121$; for Yr 2 is $10^2 : 11^2 = 100 : 121$.
  - Total Principal units $= 110 + 100 = 210$ units, for an installment of $121$ units each.
  - Since $210\text{ units} = 21,000 \implies 1\text{ unit} = 100 \implies X = \mathbf{12,100}$.

---

## 4. Boundary Conditions, Domain Traps & TITA Pitfalls

1. **"Increased BY $k\%$" vs. "Increased TO $k\%$"**:
   - In CAT TITA questions, misreading "increased by $200\%$" as $\times 2$ instead of $\times 3$ is the #1 arithmetic error.
2. **Percentage Change vs. Percentage Points**:
   - Moving from a $20\%$ tax rate to a $25\%$ tax rate is a **$5$ percentage point** increase, but a **$25\%$ relative increase**.
3. **Faulty Balance Base Trap**:
   - Using $800\text{ g}$ instead of $1000\text{ g}$ gives $\frac{200}{800} = 25\%$ profit, NOT $\frac{200}{1000} = 20\%$. Denominator is ALWAYS the **actual quantity parted with** by the seller.
4. **Fractional Years in CI vs. SI**:
   - For $2.5$ years at $R\%$ compounded annually, the compounding factor is $(1 + r)^2 \left(1 + \frac{r}{2}\right)$, NOT $(1+r)^{2.5}$ (unless continuous/fractional power is explicitly specified).
5. **Profit on Selling Price (Gross Margin)**:
   - If a question states "A trader makes a $20\%$ profit on Selling Price", then $\text{Profit} = 0.20\,\text{SP} \implies \text{CP} = 0.80\,\text{SP}$, so true profit on CP is $\frac{0.20}{0.80} = 25\%$.

---

## 5. Active-Recall Drill (10 Prompts)

<details><summary>Q1: If A's income is 37.5% more than B's, by what percentage is B's income less than A's?</summary>
A: 37.5% = 3/8. Since A = B(1 + 3/8) = (11/8)B, B is 3/(8+3) = 3/11 = 27.27% less than A.
</details>

<details><summary>Q2: What is the single equivalent discount for three successive discounts of 10%, 20%, and 25%?</summary>
A: Multiply remaining factors: 0.90 * 0.80 * 0.75 = 0.54. Equivalent discount = 1 - 0.54 = 46%.
</details>

<details><summary>Q3: The CP of 15 articles equals the SP of 12 articles, and the discount on 8 articles equals the profit on 6 articles. Find the difference between Profit% and Discount%.</summary>
A: CP/SP = 12/15 = 4/5 -> Profit = 1 unit on CP = 4 (Profit% = 25%). Since 8D = 6P -> D/P = 3/4 = 0.75 unit -> MP = SP + D = 5 + 0.75 = 5.75. Discount% = (0.75/5.75)*100 = 300/23 = 13.04%. Difference = 25% - 13.04% = 11.96%.
</details>

<details><summary>Q4: A shopkeeper claims to sell at a 10% loss on CP, but uses a weight that gives 25% less than the marked weight. What is his actual profit or loss percentage?</summary>
A: MF = (90/100) * (100/75) = (9/10) * (4/3) = 6/5 = 1.20 -> 20% profit.
</details>

<details><summary>Q5: Compound interest on a sum for the 2nd year is Rs. 440 and for the 4th year is Rs. 532.40. Find the annual rate of interest.</summary>
A: Interests of individual years form a GP: I_4 / I_2 = (1 + r)^2 = 532.40 / 440 = 1.21 -> 1 + r = 1.1 -> R = 10%.
</details>

<details><summary>Q6: Two horses are sold for Rs. 19,550 each. On one the seller gains 15% and on the other he loses 15%. Find the net loss in Rupees.</summary>
A: Net loss % = (15/10)^2 = 2.25% = 9/400. Total SP represents 400 - 9 = 391 parts. Total SP = 2 * 19550 = 39100. Loss = (9/391) * 39100 = Rs. 900.
</details>

<details><summary>Q7: Fresh grapes contain 90% water by weight while dried grapes contain 20% water. How many kg of dried grapes are obtained from 40 kg of fresh grapes?</summary>
A: Solid pulp invariant: 40 * (1 - 0.90) = M_dry * (1 - 0.20) -> 4 = 0.8 * M_dry -> M_dry = 5 kg.
</details>

<details><summary>Q8: What is the CP:MP ratio when a trader offers a 16% discount and still earns a 20% profit?</summary>
A: CP / MP = (100 - d) / (100 + p) = (100 - 16) / (100 + 20) = 84 / 120 = 7 : 10.
</details>

<details><summary>Q9: If the difference between CI and SI on Rs. 10,000 for 3 years is Rs. 310, find the annual rate R%.</summary>
A: P * r^2 * (3 + r) = 310 -> 10000 * r^2 * (3 + r) = 310 -> r^2(3 + r) = 0.031 = (0.1)^2 * (3.1) -> r = 0.10 -> R = 10%.
</details>

<details><summary>Q10: A loan of Rs. 940 is to be repaid in 4 equal annual installments at 5% p.a. Simple Interest. Find each installment X.</summary>
A: Total due at end of 4 yrs = 940 * (1 + 4 * 0.05) = 940 * 1.20 = 1128. Sum of installments with SI = X[1 + 1.05 + 1.10 + 1.15] = 4.30X. Thus X = 1128 / 4.30 (or for Rs. 860 principal -> 860*1.2/4.3 = 240; here 1128 / 4.3 = Rs. 262.33).
</details>

---

## CAT 2025 PYQ Edge Examples & Newly Surfaced Patterns

### Newly Surfaced Sub-Topic Variants & Pattern Triggers (CAT 2025)
- **Composite Asset Alligation under Linear Allocation Constraints (`CAT_2025_QA_Slot_1` / `CAT2025_S1_QA_Q01`)**: When two assets in a portfolio have a fixed allocation ratio (e.g., Bonds $= 25\%$ of Gold $\implies 1:4$), collapse them into a single synthetic asset with weighted return $\frac{1(6\%) + 4(8\%)}{5} = 7.6\%$ and apply 2-component Alligation against the remaining asset.
- **Discount-Doubling Profit Sensitivity & Equal Rate Equilibrium (`CAT_2025_QA_Slot_2` / `CAT2025_S2_QA_Q12`)**: When doubling the discount amount reduces profit from $P_1$ to $P_2$, the initial discount is exactly $D = P_1 - P_2$; when discount $\%$ equals profit $\%$ ($r$), apply $\frac{\text{CP}}{\text{MP}} = \frac{100-r}{100+r}$ directly.
- **Semi-Annual CI Extraction from Multi-Period SI Gap (`CAT_2025_QA_Slot_1` / `CAT2025_S1_QA_Q04`)**: Extract annual $\text{SI}_1 = \frac{A(t_2)-A(t_1)}{t_2-t_1}$ first, recover Principal $P$ and nominal rate $R\%$, then apply 4-period Pascal expansion $(4, 6, 4, 1)$ at half-yearly rate $R/2\%$.

### Solved CAT 2025 PYQ Edge Exemplars

#### CAT2025_S1_QA_Q01 (`CAT_2025_QA_Slot_1` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Percentages & Successive Change — *Weighted percentage returns with linear portfolio allocation constraints*
- **Verified Answer**: `900` (Let Gold = 4B, Bonds = B, Stocks = 100000 - 5B. Total return: 0.10(100000 - 5B) + 0.06B + 0.08(4B) = 8200 => 10000 - 0.12B = 8200 => B = 15000. Bond return = 6% of 15000 = Rs 900.)
- **Mental Trigger (`See X -> Do Y`)**: When two components have a fixed ratio (Bonds : Gold = 1 : 4), combine them into a single composite asset with weighted return (1*6% + 4*8%)/5 = 7.6% and apply Alligation against Stocks (10%).
- **First-Principles Method**: Set B = 0.25G => G = 4B and S = 100000 - 5B. Substitute into 0.10S + 0.06B + 0.08G = 8200 to get 10000 - 0.12B = 8200 => B = 15000, so gain from bonds = 0.06 * 15000 = 900.
- **30-Second Exam-Hall Speed Shortcut**: Composite rate of (Bonds+Gold) in 1:4 ratio is (6+32)/5 = 7.6%. Overall rate is 8.2%. By Alligation between Stocks (10%) and (B+G) (7.6%): weight of (B+G) is (10 - 8.2)/(10 - 7.6) = 1.8/2.4 = 3/4 of 100000 = 75000. Bonds = 1/5 of 75000 = 15000; 6% of 15000 = 900.
- **Trap Alert & Boundary Condition**: Do not report the bond principal (15000) instead of the bond gain (900). Always re-read the final noun phrase in TITA questions.

#### CAT2025_S1_QA_Q04 (`CAT_2025_QA_Slot_1` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Simple & Compound Interest, Installments — *Simple interest rate extraction followed by semi-annual compound interest accumulation*
- **Verified Answer**: `(B) 3221` (SI for 3.5 years = 18960 - 13920 = 5040 => SI per year = 1440. Principal P = 13920 - 3(1440) = 9600. Annual rate R = 1440/9600 = 15%. Semi-annual rate = 7.5% for 4 periods: CI = 9600*(1.075^4 - 1) = 3220.50 -> nearest to 3221.)
- **Mental Trigger (`See X -> Do Y`)**: Difference of two SI amounts divided by difference of times gives annual SI; then for 4 periods at 7.5%, use two successive 2-period effective rates: 7.5 + 7.5 + 0.5625 = 15.5625%, then 15.5625*2 + (15.5625)^2/100 = 33.547%.
- **First-Principles Method**: SI_1yr = (18960 - 13920)/(6.5 - 3) = 5040/3.5 = 1440. Principal P = 13920 - 3*1440 = 9600. Rate R = (1440/9600)*100 = 15% p.a. Under 6-monthly compounding for 2 years (n=4, r=7.5%), CI = 9600*((1.075)^4 - 1) = 3220.50375, nearest to 3221.
- **30-Second Exam-Hall Speed Shortcut**: 4-period SI at 7.5% is 2880. Add 6*P*r^2 = 6*9600*(0.075)^2 = 324 -> 3204. Add 4*P*r^3 = 4*9600*(0.00422) = 16.2 -> 3220.2, plus r^4 term ~0.3 -> 3220.5 -> 3221.
- **Trap Alert & Boundary Condition**: 6 years and 6 months is 6.5 years (not 6.6 years). Compounding every 6 months for 2 years means 4 compounding periods at 7.5%, not 2 periods at 15%.

#### CAT2025_S1_QA_Q07 (`CAT_2025_QA_Slot_1` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Profit, Loss, Discount & Faulty Weights — *Successive multiplying factors combining discount and free-article promotional schemes*
- **Verified Answer**: `175` (Total CP of 13 chairs = 1300. Total SP for 26% profit = 1300 * 1.26 = 1638. Customer pays discounted price of 12 chairs = 12 * 0.78 * MP = 1638 => MP = 1638 / 9.36 = 175.)
- **Mental Trigger (`See X -> Do Y`)**: Giving 13 articles for the price of 12 multiplies effective SP per article by 12/13. Apply: CP * (1 + Profit%) = MP * (1 - Discount%) * (12/13).
- **First-Principles Method**: For 13 chairs, total CP = 13 * 100 = 1300 and required revenue = 1300 * 1.26 = 1638. Revenue equals 12 chairs at 22% discount: 12 * (0.78 * MP) = 1638 => MP = 175.
- **30-Second Exam-Hall Speed Shortcut**: 100 * (126/100) = MP * (78/100) * (12/13) => MP = (126 * 13) / (78 * 12) * 100 = (21 * 13) / (13 * 12) * 100 = (21/12) * 100 = 175.
- **Trap Alert & Boundary Condition**: Giving 13 chairs for the price of 12 means the shopkeeper parts with 13 chairs (denominator is 13, not 12).

#### CAT2025_S2_QA_Q09 (`CAT_2025_QA_Slot_2` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Simple & Compound Interest, Installments — *Two-year compound interest amortization schedule*
- **Verified Answer**: `(C) 8%` (Present value equation: 530/(1+r) + 594/(1+r)^2 = 1000. At r = 8% (1+r = 1.08): after Year 1, principal 1000 grows to 1080; paying 530 leaves 550; after Year 2, 550 * 1.08 = 594, which is paid off exactly!)
- **Mental Trigger (`See X -> Do Y`)**: Notice 594 = 550 * 1.08 and 1000 * 1.08 - 530 = 550! Always test Year-1 balance (1000*(1+r) - 530)*(1+r) = 594.
- **First-Principles Method**: After 1 year at rate r, balance is 1000(1 + r) - 530. After 2 years, (1000(1 + r) - 530)(1 + r) = 594. Testing r = 0.08 gives (1080 - 530)(1.08) = 550 * 1.08 = 594.
- **30-Second Exam-Hall Speed Shortcut**: Factor 594 = 54 * 11 = 27 * 22. Since 1 + r = 1 + R/100 has factor 27 when R = 8 (1.08 = 27/25), R = 8% is immediate!
- **Trap Alert & Boundary Condition**: Never equate simple sum of installments to 1000*(1+r)^2; each installment is discounted by its own time period.

#### CAT2025_S2_QA_Q12 (`CAT_2025_QA_Slot_2` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Profit, Loss, Discount & Faulty Weights — *Linear sensitivity of profit to discount doubling and equal profit-discount rate equilibrium*
- **Verified Answer**: `(C) 14` (CP = 1650. Initial profit = 20% of 1650 = 330 (SP = 1980). When discount is doubled, profit drops to 110, so discount amount = 330 - 110 = 220, and MP = 1980 + 220 = 2200. For profit% = discount% = k%: 1650(1 + k/100) = 2200(1 - k/100) => 3(100 + k) = 4(100 - k) => 7k = 100 => k = 14.29% -> 14.)
- **Mental Trigger (`See X -> Do Y`)**: Doubling the discount reduces SP (and profit) by exactly 1x the original discount D; then for Profit% = Discount% = k%, use k = 100*(MP - CP)/(MP + CP)!
- **First-Principles Method**: Initial profit = 0.20 * 1650 = 330. Doubling discount reduces profit from 330 to 110, so initial discount D = 220 and MP = 1650 + 330 + 220 = 2200. Equating CP(1 + k/100) = MP(1 - k/100) gives k = 100*(2200 - 1650)/(2200 + 1650) = 100/7 = 14.285%, nearest to 14.
- **30-Second Exam-Hall Speed Shortcut**: Universal identity: Profit% = Discount% = k% <=> k = 100*(MP - CP)/(MP + CP) = 100*(4 - 3)/(4 + 3) = 100/7 = 14.28%.
- **Trap Alert & Boundary Condition**: Remember profit% is on CP (1650) while discount% is on MP (2200).

#### CAT2025_S2_QA_Q13 (`CAT_2025_QA_Slot_2` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Percentages & Successive Change — *Successive remainder percentages*
- **Verified Answer**: `(B) 5 : 8` (Assume Total = 100. Pinu = 20. Remaining = 80; Meena = 40% of 80 = 32. Seema = 0.8 * 20 = 16. Rinu = 100 - (20 + 32 + 16) = 32. Ratio Pinu : Rinu = 20 : 32 = 5 : 8.)
- **Mental Trigger (`See X -> Do Y`)**: Set Total = 100 and compute shares sequentially: P = 20, M = 32, S = 16 => R = 32.
- **First-Principles Method**: With Total = 100, P = 20, M = 0.40 * (100 - 20) = 32, S = 0.80 * 20 = 16, leaving R = 100 - 68 = 32. Thus P : R = 20 : 32 = 5 : 8.
- **30-Second Exam-Hall Speed Shortcut**: 10-second mental arithmetic with Total = 100 -> 20 : 32 = 5 : 8.
- **Trap Alert & Boundary Condition**: Meena gets 40% of the REMAINING amount (40% of 80 = 32), not 40% of total.

#### CAT2025_S3_QA_Q17 (`CAT_2025_QA_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Profit, Loss, Discount & Faulty Weights — *Weighted revenue aggregation across multi-period discount rates*
- **Verified Answer**: `(A) 525` (Total units = 120 + 135 + 150 + 165 = 570. Total CP = 570 * 240 = 136800. Total SP = 136800 + 138825 = 275625. Effective MP units sold = 120(0.8) + 135(0.9) + 150(0.95) + 165(1.0) = 96 + 121.5 + 142.5 + 165 = 525. Thus MP = 275625 / 525 = 525.)
- **Mental Trigger (`See X -> Do Y`)**: Notice monthly sales (120, 135, 150, 165) form an AP with mean 142.5 (total = 4 * 142.5 = 570), and effective MP coefficient is 96 + 121.5 + 142.5 + 165 = 525!
- **First-Principles Method**: Total Cost = (120 + 135 + 150 + 165) * 240 = 570 * 240 = 136800. Total Revenue = 136800 + 138825 = 275625. Also Total Revenue = MP * (120*0.80 + 135*0.90 + 150*0.95 + 165*1.00) = 525 * MP. Hence MP = 275625 / 525 = 525.
- **30-Second Exam-Hall Speed Shortcut**: Since 525 * MP = 275625 ends in 25 and 525 = 21 * 25, test MP = 525: 525^2 = (52 * 53) concatenated with 25 = 275625! Exact match!
- **Trap Alert & Boundary Condition**: Recognizing 275625 = 525^2 via the (n*10 + 5)^2 shortcut makes the final division instantaneous.
