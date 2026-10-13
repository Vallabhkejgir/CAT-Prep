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
