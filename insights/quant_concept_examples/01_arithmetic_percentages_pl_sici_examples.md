# QA 01 Concept & Formula Examples: Percentages, Profit & Loss, Discount, Faulty Weights, SI & CI, Installments

> **Companion Reference**: [`../topic_summaries/quant/01_arithmetic_percentages_pl_sici.md`](../topic_summaries/quant/01_arithmetic_percentages_pl_sici.md) | [`QA_Formula_and_Trigger_Book.md`](../high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md)

Every concept, formula, and pattern trigger from **QA 01** is explained below with plain-English intuition, clean single-concept numbers, a two-way walkthrough (direct formula vs. mental ratio intuition), and the #1 mistake to avoid.

---

## Concept 1: Multiplying Factor (MF) & Base-Shift Identity

### 1. Concept & Formula in Plain English
Instead of calculating a percentage and then adding or subtracting it in two steps, a **Multiplying Factor (MF)** scales a number in one shot:
- Increase by $p\%$: $\text{MF} = 1 + \frac{p}{100}$
- Decrease by $q\%$: $\text{MF} = 1 - \frac{q}{100}$

When comparing two numbers $X$ and $Y$, if $X$ is $\frac{a}{b}$ **more** than $Y$, then $X = Y\left(1 + \frac{a}{b}\right) = Y\left(\frac{b+a}{b}\right)$. When you flip the question and ask how much **less** $Y$ is than $X$, your comparison base shifts from $Y$ ($b$ parts) to $X$ ($b+a$ parts), while the gap remains $a$ parts:
$$\text{If } X \text{ is } \frac{a}{b} \text{ more than } Y \implies Y \text{ is } \frac{a}{b+a} \text{ less than } X$$

### 2. When to Use It (Question Cue)
- *"A's salary is $25\%$ more than B's salary. By what percentage is B's salary less than A's?"*
- *"A quantity is increased **by** $250\%$ vs. increased **to** $250\%$."*

### 3. General Example (Clean Numbers, Single Concept)
> Rohan's income is $25\%$ more than Sohan's income. By what percentage is Sohan's income less than Rohan's income?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Convert $25\%$ into a fraction: $\frac{a}{b} = \frac{25}{100} = \frac{1}{4}$ (so $a = 1, b = 4$).
  2. Plug $a = 1$ and $b = 4$ into the Base-Shift formula $\frac{a}{b+a}$:
     $$\text{Decrease fraction} = \frac{1}{4 + 1} = \frac{1}{5}$$
  3. Convert $\frac{1}{5}$ back to a percentage: $\frac{1}{5} \times 100\% = \mathbf{20\%}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Assume Sohan's income $= 100$.
  2. Rohan's income is $25\%$ more, so Rohan $= 100 + 25 = 125$.
  3. Sohan is $25$ less than Rohan, and since we are comparing **to Rohan** ($125$), the percentage is $\frac{25}{125} \times 100\% = \frac{1}{5} \times 100\% = \mathbf{20\%}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Dividing the difference ($25$) by Sohan's $100$ again (getting $25\%$) instead of dividing by the new base after the word **"than"** (Rohan's $125$). Also remember: *"increased **by** $250\%$"* means $\times (1 + 2.5) = 3.5X$, whereas *"increased **to** $250\%$"* means $\times 2.5X$.

---

## Concept 2: Successive Percentage Change & Symmetric Loss Rule

### 1. Concept & Formula in Plain English
When a number undergoes two back-to-back percentage changes of $a\%$ and $b\%$, the second percentage acts on top of the first change too, creating an extra cross-term $\frac{ab}{100}$:
$$\text{Net \% Change} = \left(a + b + \frac{ab}{100}\right)\%$$
If a value goes up by $+x\%$ and then drops by $-x\%$ (or vice versa), the $+x$ and $-x$ cancel out, leaving a guaranteed net loss of $\left(\frac{x}{10}\right)^2\% = \frac{x^2}{100}\%$.

### 2. When to Use It (Question Cue)
- *"The price of a stock rises by $20\%$ in January and falls by $10\%$ in February. What is the net percentage change?"*
- *"Length of a rectangle increases by $30\%$ and breadth decreases by $30\%$. Find the percentage change in area."*

### 3. General Example (Clean Numbers, Single Concept)
> A town's population increases by $20\%$ in the first year and decreases by $10\%$ in the second year. What is the net percentage change in population over the two years? (Also: what if it increased by $20\%$ and then decreased by $20\%$?)

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Identify $a = +20$ and $b = -10$ (use a negative sign for a decrease).
  2. Substitute into $a + b + \frac{ab}{100}$:
     $$\text{Net \% Change} = 20 + (-10) + \frac{(20)(-10)}{100} = 10 - 2 = \mathbf{+8\%}$$
  3. For $+20\%$ and $-20\%$, plug $x = 20$ into $-\left(\frac{x}{10}\right)^2\% = -\left(\frac{20}{10}\right)^2\% = \mathbf{-4\%}$ (a $4\%$ loss).
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Start with a population of $100$.
  2. After $+20\%$, population becomes $100 + 20 = 120$.
  3. Next, $-10\%$ of $120$ is $12$, so population becomes $120 - 12 = 108$.
  4. From $100$ to $108$ is a net increase of $\mathbf{8\%}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Adding percentages naively ($+20\% - 10\% = +10\%$, or $+20\% - 20\% = 0\%$) and forgetting that the second percentage applies to the **new** base ($120$), not the original $100$.

---

## Concept 3: Product Constancy ($A \times B = k$) & Non-Constant Expenditure Shift

### 1. Concept & Formula in Plain English
Whenever two quantities multiply to give a total ($\text{Price} \times \text{Consumption} = \text{Expenditure}$, or $\text{Speed} \times \text{Time} = \text{Distance}$):
- **Constant Total**: If $A$ increases by fraction $\frac{a}{b}$ (becoming $\frac{b+a}{b}$ of original), $B$ must be multiplied by the reciprocal $\frac{b}{b+a}$ (a decrease of $\frac{a}{b+a}$) so their product stays $1$.
- **Shifted Total:** If Price rises by $p$ and Expenditure is allowed to rise by $k$, then: $\text{MF}_{\text{Price}} \times \text{MF}_{\text{Consumption}} = \text{MF}_{\text{Expenditure}} \implies \text{MF}_{\text{Consumption}} = \frac{100 + k}{100 + p}$



### 2. When to Use It (Question Cue)
- *"Petrol price rises by $25\%$. By what percentage must a car owner reduce consumption so expenditure remains unchanged (or rises by only $10\%$)?"*

### 3. General Example (Clean Numbers, Single Concept)
> The price of sugar increases by $25\%$.
> (a) By what percentage must a family reduce consumption so that total expenditure remains the same?
> (b) By what percentage must consumption drop if the family can afford at most a $10\%$ increase in expenditure?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: Price increases by $25\% = \frac{1}{4}$ ($a = 1, b = 4$). Consumption must drop by $\frac{a}{b+a} = \frac{1}{4+1} = \frac{1}{5} = \mathbf{20\%}$.
  2. **Part (b)**: Plug $p = 25$ and $k = 10$ into $\text{MF}_{\text{Consumption}} = \frac{100+k}{100+p} = \frac{110}{125} = \frac{22}{25} = \frac{88}{100}$, which is a $100\% - 88\% = \mathbf{12\%}$ reduction.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Assume original Price $= \text{Rs. } 100/\text{kg}$ and Consumption $= 1\text{ kg}$, so Expenditure $= \text{Rs. } 100$.
  2. New Price $= \text{Rs. } 125/\text{kg}$.
  3. In (a), with Rs. $100$, the family can buy $\frac{100}{125} = 0.80\text{ kg}$ (a $\mathbf{20\%}$ drop from $1\text{ kg}$).
  4. In (b), with Rs. $110$, the family can buy $\frac{110}{125} = 0.88\text{ kg}$ (a $\mathbf{12\%}$ drop from $1\text{ kg}$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Subtracting percentages directly ($25\% - 10\% = 15\%$) instead of dividing the new expenditure ($110$) by the new price ($125$).

---

## Concept 4: Solid / Pulp Mass Invariance in Evaporation

### 1. Concept & Formula in Plain English
When fresh fruit dries into dry fruit, **only water evaporates**—the dry solid pulp inside neither evaporates nor grows. Therefore, the absolute weight of the non-water part (pulp) before drying equals the weight of the pulp after drying:
$$M_{\text{fresh}} \times (1 - \% \text{Water}_{\text{fresh}}) = M_{\text{dry}} \times (1 - \% \text{Water}_{\text{dry}})$$

### 2. When to Use It (Question Cue)
- *"Fresh grapes contain $80\%$ water while dry grapes contain $20\%$ water. How many kg of dry grapes can be obtained from $100\text{ kg}$ of fresh grapes?"*

### 3. General Example (Clean Numbers, Single Concept)
> Fresh berries contain $80\%$ water by weight, whereas dried berries contain $20\%$ water by weight. How many kilograms of dried berries can be obtained from $60\text{ kg}$ of fresh berries?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Identify $M_{\text{fresh}} = 60$, $\% \text{Water}_{\text{fresh}} = 0.80$, and $\% \text{Water}_{\text{dry}} = 0.20$.
  2. Equate solid pulp mass:
     $$60 \times (1 - 0.80) = M_{\text{dry}} \times (1 - 0.20)$$
  3. Solve: $60 \times 0.20 = 0.80 \times M_{\text{dry}} \implies 12 = 0.80 M_{\text{dry}} \implies M_{\text{dry}} = \mathbf{15\text{ kg}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In $60\text{ kg}$ of fresh berries, $20\%$ is solid pulp $= 12\text{ kg}$ of pulp.
  2. In dried berries, that same $12\text{ kg}$ of pulp makes up $80\%$ ($100\% - 20\%$) of the total weight.
  3. Since $80\% = \frac{4}{5}$ of dried weight is $12\text{ kg}$, full dried weight $= 12 \times \frac{5}{4} = \mathbf{15\text{ kg}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Equating water percentages ($60 \times 80\%$) instead of the **invariant solid pulp** ($20\%$ vs. $80\%$).

---

## Concept 5: Markup, Discount & Direct CP-to-MP Ratio

### 1. Concept & Formula in Plain English
A shopkeeper starts at Cost Price ($\text{CP}$), marks it up by $m\%$ to set the Marked Price ($\text{MP}$), and then gives a discount of $d\%$ on $\text{MP}$ to reach the Selling Price ($\text{SP}$). Because $\text{SP}$ equals both $\text{CP}\left(1 + \frac{p}{100}\right)$ and $\text{MP}\left(1 - \frac{d}{100}\right)$, equating the two gives a direct bridge between $\text{CP}$ and $\text{MP}$ without ever calculating $\text{SP}$:
$$p = m - d - \frac{md}{100}, \qquad \frac{\text{CP}}{\text{MP}} = \frac{100 - d}{100 + p}$$

### 2. When to Use It (Question Cue)
- *"A trader marks his goods $40\%$ above CP and allows a $10\%$ discount. Find his profit percentage."*
- *"Even after giving a $20\%$ discount, a shopkeeper makes a $25\%$ profit. Find the ratio of CP to MP."*

### 3. General Example (Clean Numbers, Single Concept)
> A merchant offers a $20\%$ discount on the marked price of a jacket and still earns a $25\%$ profit on his cost price. Find the ratio $\text{CP} : \text{MP}$ and the percentage by which the jacket was marked up above $\text{CP}$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Given discount $d = 20$ and profit $p = 25$.
  2. Plug into $\frac{\text{CP}}{\text{MP}} = \frac{100 - d}{100 + p}$:
     $$\frac{\text{CP}}{\text{MP}} = \frac{100 - 20}{100 + 25} = \frac{80}{125} = \mathbf{\frac{16}{25}} \quad (16 : 25)$$
  3. Markup above CP $= \frac{25 - 16}{16} \times 100\% = \frac{9}{16} \times 100\% = \mathbf{56.25\%}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Let $\text{CP} = 100$. For a $25\%$ profit, $\text{SP} = 125$.
  2. This $\text{SP} = 125$ is $80\%$ of $\text{MP}$ (after $20\%$ discount): $0.80 \times \text{MP} = 125 \implies \text{MP} = 156.25$.
  3. Ratio $\text{CP} : \text{MP} = 100 : 156.25 = 16 : 25$, and Markup $= 56.25\%$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Inverting the ratio as $\frac{100+p}{100-d}$ for $\frac{\text{CP}}{\text{MP}}$—remember that $\text{CP}$ is smaller than $\text{MP}$, so $(100 - d)$ stays on top with $\text{CP}$.

---

## Concept 6: Gross Margin (Profit on SP) vs. Markup (Profit on CP)

### 1. Concept & Formula in Plain English
Standard profit percentage is measured on Cost Price ($\frac{\text{Profit}}{\text{CP}}$), whereas **Gross Margin** (or "profit on selling price") is measured on Selling Price ($\frac{\text{Profit}}{\text{SP}}$). Since $\text{SP} = \text{CP} + \text{Profit}$, if profit on $\text{CP}$ is $\frac{a}{b}$ (meaning $\text{Profit} = a$ and $\text{CP} = b$), then $\text{SP} = b + a$, so:
$$\text{Profit on CP} = \frac{a}{b} \iff \text{Profit on SP (Margin)} = \frac{a}{b + a}$$

### 2. When to Use It (Question Cue)
- *"A retailer calculates his profit percentage on the selling price and finds it to be $20\%$. What is his actual profit percentage on cost price?"*

### 3. General Example (Clean Numbers, Single Concept)
> A store owner states that he makes a $20\%$ profit on the selling price of an item. What is his true profit percentage on the cost price?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Profit on SP $= 20\% = \frac{1}{5} = \frac{a}{b+a}$. Here $a = 1$ (profit) and $b + a = 5$ (SP), so $b = 4$ (CP).
  2. True profit on CP $= \frac{a}{b} = \frac{1}{4} = \mathbf{25\%}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Assume $\text{SP} = 100$.
  2. Profit is $20\%$ of $\text{SP} = 20$.
  3. Therefore, $\text{CP} = \text{SP} - \text{Profit} = 100 - 20 = 80$.
  4. True profit $\%$ on $\text{CP} = \frac{20}{80} \times 100\% = \mathbf{25\%}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Adding $20\%$ to $\text{CP}$ instead of subtracting $20\%$ from $\text{SP} = 100$ to find $\text{CP} = 80$.

---

## Concept 7: Two Articles Sold at the Same Selling Price ($S_1 = S_2$)

### 1. Concept & Formula in Plain English
When two items have the **same Cost Price** and one is sold at $+x\%$ profit while the other is sold at $-x\%$ loss, the dollar gain and dollar loss are equal, so there is $0\%$ net change.
However, when two items have the **same Selling Price ($S_1 = S_2 = S$)**, the item sold at a loss had a *larger* Cost Price than the item sold at a profit! Thus the loss outweighs the gain, resulting in a guaranteed net loss:
$$\text{Net Loss \%} = \left(\frac{x}{10}\right)^2\%, \qquad \text{Net Loss Amount} = \frac{2S}{\left(\frac{100}{x}\right)^2 - 1}$$

### 2. When to Use It (Question Cue)
- *"Two watches are sold for Rs. $1,980$ each. On one the seller gains $10\%$ and on the other he loses $10\%$. Find his overall gain or loss."*

### 3. General Example (Clean Numbers, Single Concept)
> A dealer sells two chairs for Rs. $990$ each. On the first chair he gains $10\%$, and on the second chair he loses $10\%$. Find his net loss percentage and the exact rupee loss.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Plug $x = 10$ into Net Loss $\% = \left(\frac{10}{10}\right)^2\% = \mathbf{1\%\text{ loss}}$.
  2. Plug $S = 990$ and $x = 10$ into Loss Amount:
     $$\text{Loss Amount} = \frac{2 \times 990}{\left(\frac{100}{10}\right)^2 - 1} = \frac{1980}{100 - 1} = \frac{1980}{99} = \mathbf{\text{Rs. } 20}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Chair 1 ($+10\%$ profit): $1.10 \times \text{CP}_1 = 990 \implies \text{CP}_1 = \text{Rs. } 900$.
  2. Chair 2 ($-10\%$ loss): $0.90 \times \text{CP}_2 = 990 \implies \text{CP}_2 = \text{Rs. } 1,100$.
  3. Total $\text{CP} = 900 + 1100 = \text{Rs. } 2,000$; Total $\text{SP} = 990 + 990 = \text{Rs. } 1,980$.
  4. Loss $= 2000 - 1980 = \mathbf{\text{Rs. } 20}$, which is $\frac{20}{2000} = \mathbf{1\%}$ of total CP.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Answering "No profit, no loss" by confusing **equal Selling Prices** ($S_1 = S_2$) with **equal Cost Prices** ($\text{CP}_1 = \text{CP}_2$).

---

## Concept 8: Promotional Free Articles ("Buy $m$ Get $n$ Free") & Discount Sensitivity

### 1. Concept & Formula in Plain English
When a shopkeeper says *"Buy $m$ articles and get $n$ articles free"*, the customer walks away with $(m + n)$ articles from the shopkeeper's stock but only pays the price of $m$ articles. Thus the effective revenue multiplier per article is $\frac{m}{m + n}$. If there is also a cash discount of $d\%$, both multipliers chain together:
$$\frac{\text{Effective SP per article}}{\text{MP per article}} = \left(\frac{m}{m + n}\right) \times \left(1 - \frac{d}{100}\right)$$
Also, when $\text{CP}$ and $\text{MP}$ are fixed, any change in discount directly changes profit dollar-for-dollar: $\Delta \text{Profit} = -\Delta \text{Discount} = -\Delta(d\%) \times \text{MP}$.

### 2. When to Use It (Question Cue)
- *"A shopkeeper gives $1$ article free on buying $4$ articles and also offers a $10\%$ discount..."*
- *"With a $2\%$ discount the profit is Rs. $180$; with a $5\%$ discount the profit is Rs. $120$. Find MP."*

### 3. General Example (Clean Numbers, Single Concept)
> A trader gives $1$ shirt free on the purchase of $4$ shirts and also allows an additional $10\%$ cash discount. What is the single equivalent discount percentage offered to the customer?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $m = 4$ (paid), $n = 1$ (free), and $d = 10$.
  2. Effective SP/MP multiplier:
     $$\text{MF} = \frac{4}{4 + 1} \times \left(1 - \frac{10}{100}\right) = \frac{4}{5} \times \frac{9}{10} = \frac{36}{50} = \frac{72}{100}$$
  3. Paying $72\%$ of Marked Price means an equivalent discount of $100\% - 72\% = \mathbf{28\%}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Let each shirt have $\text{MP} = \text{Rs. } 100$.
  2. The customer takes $4 + 1 = 5$ shirts home (Total $\text{MP} = \text{Rs. } 500$).
  3. He is billed for $4$ shirts ($\text{Rs. } 400$) minus $10\%$ discount $= \text{Rs. } 360$.
  4. Getting Rs. $500$ worth of shirts for Rs. $360$ saves Rs. $140$ on Rs. $500$, which is $\frac{140}{500} \times 100\% = \mathbf{28\%}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Treating "Buy $4$ get $1$ free" as a $\frac{1}{4} = 25\%$ discount instead of $\frac{1}{4+1} = \frac{1}{5} = 20\%$ (the denominator is always the **total items handed over**, $m+n$).

---

## Concept 9: Dishonest Dealer & Faulty Weights (Universal Multiplying Factor)

### 1. Concept & Formula in Plain English
Whenever a merchant manipulates prices, adulterates goods with water, or uses a rigged weighing scale, every stage is just a ratio of **what the merchant gains** to **what leaves the merchant's pocket**:
$$\text{Overall MF} = \left(\frac{\text{Price Charged}}{\text{Cost Incurred}}\right) \times \left(\frac{\text{True Weight Claimed to Customer}}{\text{Actual Physical Weight Dispensed}}\right)$$
If $\text{Overall MF} = \frac{5}{4} = 1.25$, the merchant makes a $+25\%$ net profit.

### 2. When to Use It (Question Cue)
- *"A shopkeeper professes to sell at cost price (or at a $10\%$ loss) but uses a weight of $800\text{ g}$ instead of $1\text{ kg}$."*

### 3. General Example (Clean Numbers, Single Concept)
> A grocer claims to sell rice at a $10\%$ loss on cost price, but uses a faulty weight that weighs only $750\text{ g}$ for every $1\text{ kg}$ ($1000\text{ g}$) shown on the scale. Find his actual profit percentage.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Price multiplier (selling at $10\%$ loss): $\frac{\text{Price Charged}}{\text{Cost}} = \frac{90}{100} = \frac{9}{10}$.
  2. Weight multiplier (claiming $1000\text{ g}$ while giving $750\text{ g}$): $\frac{1000}{750} = \frac{4}{3}$.
  3. Multiply the two factors:
     $$\text{Overall MF} = \frac{9}{10} \times \frac{4}{3} = \frac{36}{30} = \frac{6}{5} = 1.20 \implies \mathbf{20\%\text{ Profit}}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Assume $1\text{ g}$ of rice costs Re. $1$.
  2. The grocer physically hands over $750\text{ g}$, so his actual cost out of pocket is **Rs. $750$**.
  3. He tells the customer it is $1000\text{ g}$ (worth Rs. $1000$) sold at a $10\%$ loss, so he collects **Rs. $900$**.
  4. Profit on Rs. $750$ cost $= \frac{900 - 750}{750} \times 100\% = \frac{150}{750} \times 100\% = \mathbf{20\%}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Dividing the $250\text{ g}$ weight cheat by $1000\text{ g}$ (getting $25\%$) instead of dividing by the **actual weight dispensed** ($750\text{ g}$).

---

## Concept 10: Simple Interest (SI), Compound Interest (CI) & Effective Annual Rate (EAR)

### 1. Concept & Formula in Plain English
- **Simple Interest (SI)** pays interest only on the original Principal $P$ every year: $\text{SI} = \frac{P \cdot R \cdot T}{100}$ (linear growth).
- **Compound Interest (CI)** adds each period's interest back to the principal so interest earns interest (exponential growth):
  $$A = P\left(1 + \frac{R}{100k}\right)^{kT}, \qquad \text{EAR} = \left[\left(1 + \frac{R}{100k}\right)^k - 1\right] \times 100\%$$
  where $k$ is the number of compounding periods per year ($k=2$ for half-yearly, $k=4$ for quarterly).

### 2. When to Use It (Question Cue)
- *"A sum is invested at $20\%$ per annum compounded half-yearly for $1$ year. What is the effective annual rate of interest?"*

### 3. General Example (Clean Numbers, Single Concept)
> Find the compound interest on Rs. $10,000$ at $20\%$ per annum for $1$ year when compounded half-yearly, and state the Effective Annual Rate (EAR).

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $P = 10,000$, $R = 20\%$, $T = 1$ year, and $k = 2$ (half-yearly).
  2. Rate per half-year $= \frac{R}{k} = \frac{20\%}{2} = 10\%$, and number of periods $= kT = 2$.
  3. Amount $A = 10,000 \left(1 + \frac{10}{100}\right)^2 = 10,000 \times 1.21 = \text{Rs. } 12,100$.
  4. $\text{CI} = 12,100 - 10,000 = \mathbf{\text{Rs. } 2,100}$, and $\text{EAR} = (1.1^2 - 1) \times 100\% = \mathbf{21\%}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Two half-years at $10\%$ each is simply two successive $+10\%$ increases: $10 + 10 + \frac{10 \times 10}{100} = \mathbf{21\%}$.
  2. $21\%$ of Rs. $10,000 = \mathbf{\text{Rs. } 2,100}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Dividing the time by $2$ instead of **halving the rate** ($20\% \to 10\%$) and **doubling the periods** ($1 \text{ yr} \to 2 \text{ half-years}$).

---

## Concept 11: CI vs. SI 2-Year & 3-Year Difference Shortcuts & Pascal Tree

### 1. Concept & Formula in Plain English
Why is Compound Interest bigger than Simple Interest? Only because prior years' interest earns extra interest!
- In **2 years**, Year 1's interest ($Pr$) earns interest for 1 year at rate $r$, creating a gap of $Pr \cdot r = Pr^2$.
- In **3 years**, the gap is $3$ blocks of $Pr^2$ plus $1$ block of $Pr^3$:
  $$\text{Diff}_2 = \text{CI}_2 - \text{SI}_2 = Pr^2, \qquad \text{Diff}_3 = \text{CI}_3 - \text{SI}_3 = Pr^2(3 + r), \qquad \frac{\text{Diff}_3}{\text{Diff}_2} = 3 + r$$
  where $r = \frac{R}{100}$.

### 2. When to Use It (Question Cue)
- *"The difference between CI and SI on a certain sum at $10\%$ p.a. for $2$ years is Rs. $50$ (or for $3$ years is Rs. $155$). Find the principal."*

### 3. General Example (Clean Numbers, Single Concept)
> On a certain principal at $10\%$ per annum, the difference between Compound Interest and Simple Interest for $3$ years is Rs. $310$. Find the $2$-year difference and the Principal $P$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Given $R = 10\% \implies r = \frac{10}{100} = 0.10$, and $\text{Diff}_3 = 310$.
  2. Using $\frac{\text{Diff}_3}{\text{Diff}_2} = 3 + r = 3.10$:
     $$\text{Diff}_2 = \frac{310}{3.10} = \mathbf{\text{Rs. } 100}$$
  3. Using $\text{Diff}_2 = Pr^2$:
     $$100 = P \times (0.10)^2 = 0.01 P \implies P = \mathbf{\text{Rs. } 10,000}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Assume $P = 1,000$. At $10\%$, 3-year SI is $100 + 100 + 100 = 300$.
  2. 3-year CI adds Pascal tree interest-on-interest: $3 \times (10\%\text{ of }100) + 1 \times (10\%\text{ of }10) = 30 + 1 = 31$.
  3. Since a gap of $31$ corresponds to $P = 1,000$, a gap of $310$ ($10\times$ larger) corresponds to $P = \mathbf{\text{Rs. } 10,000}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Plugging $R = 10$ instead of the decimal $r = \frac{10}{100} = 0.10$ into $3 + r$ (writing $3 + 10 = 13$ instead of $3 + 0.10 = 3.10$).

---

## Concept 12: CI for the $n$-th Year vs. CI for $n$ Years & Exponential Doubling

### 1. Concept & Formula in Plain English
- **"CI for $n$ years"** means the total accumulated interest across all $n$ years: $P[(1+r)^n - 1]$.
- **"CI for the $n$-th year"** means the interest earned in that **single year alone**:
  $$I_n = A_n - A_{n-1} = Pr(1+r)^{n-1}$$
  Notice that each single year's interest is just $(1+r)$ times the previous year's interest ($I_1, I_2, I_3, \dots$ form a Geometric Progression!).
- Similarly, if a principal becomes $k$ times in $t$ years under CI ($(1+r)^t = k$), it becomes $k^m$ times in **$m \times t$ years**.

### 2. When to Use It (Question Cue)
- *"The compound interest for the 2nd year is Rs. $500$ and for the 3rd year is Rs. $550$. Find the rate of interest."*
- *"A sum doubles in $4$ years at CI. In how many years will it become $8$ times itself?"*

### 3. General Example (Clean Numbers, Single Concept)
> (a) A sum invested at CI earns Rs. $600$ as interest in the 2nd year and Rs. $660$ as interest in the 3rd year. Find the annual rate $R\%$ and the Principal $P$.
> (b) If a sum doubles in $5$ years under CI, in how many years will it become $8$ times itself?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: $\frac{I_3}{I_2} = \frac{Pr(1+r)^2}{Pr(1+r)^1} = 1 + r = \frac{660}{600} = 1.10 \implies r = 0.10 \implies R = \mathbf{10\%}$.
     Then $I_2 = P(0.10)(1.10) = 600 \implies 0.11P = 600 \implies P = \mathbf{\text{Rs. }\frac{60,000}{11}}$.
  2. **Part (b)**: $8 = 2^3$ ($k = 2, m = 3$). Time $= m \times t = 3 \times 5 = \mathbf{15\text{ years}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. **Part (a)**: The extra Rs. $60$ earned in Year 3 ($660 - 600$) is simply 1 year's interest on Year 2's Rs. $600$: $\frac{60}{600} = \mathbf{10\%}$.
  2. **Part (b)**: Under CI, the money doubles every $5$ years: $1 \xrightarrow{5\text{ yr}} 2 \xrightarrow{+5\text{ yr}} 4 \xrightarrow{+5\text{ yr}} 8$ ($5 + 5 + 5 = \mathbf{15\text{ years}}$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Treating "CI for the 3rd year is Rs. $660$" as the total 3-year CI instead of the single-year slice $A_3 - A_2$.

---

## Concept 13: Equal Installments (CI Present Value vs. SI End-of-Term Debt)

### 1. Concept & Formula in Plain English
- **Compound Interest Installments (Standard CAT Default)**: Each installment $X$ paid at the end of year $k$ is discounted back to Day 0 by dividing by $(1+r)^k$. The sum of these Present Values equals the Principal borrowed:
  $$P = \frac{X}{(1+r)^1} + \frac{X}{(1+r)^2} + \dots + \frac{X}{(1+r)^n}$$
- **Simple Interest Installments**: Under SI, interest is never charged on unpaid interest. We compare the **final value at the end of year $n$**: the principal would have grown to $P(1 + nr)$, and each installment $X$ paid at year $k$ earns SI for the remaining $(n - k)$ years:
  $$P(1 + nr) = \sum_{k=1}^n X[1 + (n-k)r] = nX + \frac{n(n-1)}{2}Xr$$

### 2. When to Use It (Question Cue)
- *"A loan of Rs. $4,200$ at $10\%$ p.a. compound interest is to be repaid in $2$ equal annual installments. Find each installment."*

### 3. General Example (Clean Numbers, Single Concept)
> A borrower takes a loan of Rs. $4,200$ at $10\%$ per annum compound interest and repays it in two equal annual installments at the end of the 1st and 2nd years. Find the amount of each installment $X$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Given $P = 4200$, $r = 0.10$ ($1 + r = 1.1 = \frac{11}{10}$), and $n = 2$.
  2. Substitute into the Present Value equation:
     $$4200 = \frac{X}{11/10} + \frac{X}{(11/10)^2} = \frac{10}{11}X + \frac{100}{121}X$$
  3. Common denominator $121$:
     $$4200 = \frac{110X + 100X}{121} = \frac{210}{121}X \implies X = 4200 \times \frac{121}{210} = 20 \times 121 = \mathbf{\text{Rs. } 2,420}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. At $10\% = \frac{1}{10}$, Rs. $10$ becomes Rs. $11$ in 1 year (scale by $11 \to$ Rs. $110$ today settles Rs. $121$ in Yr 1).
  2. In 2 years, Rs. $10^2 = 100$ today settles Rs. $11^2 = 121$ in Yr 2.
  3. Thus, a total Principal of $110 + 100 = 210$ units is paid off by two equal installments of $121$ units each.
  4. Since $210\text{ units} = \text{Rs. } 4,200$ ($\times 20$), each installment is $121 \times 20 = \mathbf{\text{Rs. } 2,420}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Equating $2X = P(1+r)^2$ (which falsely ignores the fact that the first installment $X$ was paid at the end of Year 1 and stopped accruing interest in Year 2!).
