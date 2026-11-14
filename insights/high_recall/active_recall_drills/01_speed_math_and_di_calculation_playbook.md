# High-Recall Playbook 01: Speed Math, Number Benchmarks & Fast DI Calculation

> **Companion Reference**: [`../cheat_sheets/QA_Formula_and_Trigger_Book.md`](../cheat_sheets/QA_Formula_and_Trigger_Book.md) | [`../cheat_sheets/DILR_Archetype_Templates.md`](../cheat_sheets/DILR_Archetype_Templates.md) | [`README.md`](./README.md)

The on-screen CAT calculator is a mouse-click time sink: clicking $8$ digits takes $12\text{–}15$ seconds, whereas mental fraction and ratio shortcuts take **$2$ seconds**. Memorize the tables and 5 DI comparison techniques below to save $8+$ minutes per paper.

---

## 1. Master Reciprocal-to-Percentage Table ($\frac{1}{2}$ to $\frac{1}{25}$)

| Fraction | Exact % | Decimal | Useful Multiples to Recognize Instantly |
| :---: | :---: | :---: | :--- |
| $\mathbf{1/2}$ | $50.00\%$ | $0.5000$ | $3/2 = 150\%$ |
| $\mathbf{1/3}$ | $33.33\%$ | $0.3333$ | $2/3 = 66.67\%$ |
| $\mathbf{1/4}$ | $25.00\%$ | $0.2500$ | $3/4 = 75\%$ |
| $\mathbf{1/5}$ | $20.00\%$ | $0.2000$ | $2/5 = 40\%,\; 3/5 = 60\%,\; 4/5 = 80\%$ |
| $\mathbf{1/6}$ | $16.67\%$ | $0.1667$ | $5/6 = 83.33\%$ |
| $\mathbf{1/7}$ | $14.28\%$ | $0.1429$ | Cyclic `142857`: $2/7 = 28.57\%,\; 3/7 = 42.86\%,\; 4/7 = 57.14\%,\; 5/7 = 71.43\%$ |
| $\mathbf{1/8}$ | $12.50\%$ | $0.1250$ | $3/8 = 37.5\%,\; 5/8 = 62.5\%,\; 7/8 = 87.5\%$ |
| $\mathbf{1/9}$ | $11.11\%$ | $0.1111$ | $k/9 = (11.11 \times k)\%$ ($2/9 = 22.22\%,\; 4/9 = 44.44\%,\; 7/9 = 77.78\%$) |
| $\mathbf{1/11}$ | $9.09\%$ | $0.0909$ | $k/11 = (9.09 \times k)\%$ ($2/11 = 18.18\%,\; 3/11 = 27.27\%,\; 5/11 = 45.45\%$) |
| $\mathbf{1/12}$ | $8.33\%$ | $0.0833$ | $5/12 = 41.67\%,\; 7/12 = 58.33\%,\; 11/12 = 91.67\%$ |
| $\mathbf{1/13}$ | $7.69\%$ | $0.0769$ | $2/13 = 15.38\%,\; 3/13 = 23.08\%$ ($13 \times 7.7 \approx 100.1$) |
| $\mathbf{1/14}$ | $7.14\%$ | $0.0714$ | Half of $1/7$: $3/14 = 21.43\%,\; 5/14 = 35.71\%$ |
| $\mathbf{1/15}$ | $6.67\%$ | $0.0667$ | $2/15 = 13.33\%,\; 4/15 = 26.67\%,\; 7/15 = 46.67\%$ |
| $\mathbf{1/16}$ | $6.25\%$ | $0.0625$ | $3/16 = 18.75\%,\; 5/16 = 31.25\%,\; 7/16 = 43.75\%$ |
| $\mathbf{1/17}$ | $5.88\%$ | $0.0588$ | $17 \times 6 = 102 \implies 1/17 \approx 5.88\%$ |
| $\mathbf{1/18}$ | $5.56\%$ | $0.0556$ | Half of $1/9$: $5/18 = 27.78\%,\; 7/18 = 38.89\%$ |
| $\mathbf{1/19}$ | $5.26\%$ | $0.0526$ | $19 \times 5.26 \approx 100$ |
| $\mathbf{1/20}$ | $5.00\%$ | $0.0500$ | $1/21 = 4.76\%,\; 1/22 = 4.55\%,\; 1/23 = 4.35\%,\; 1/24 = 4.17\%,\; 1/25 = 4.00\%$ |

---

## 2. Squares ($1 \dots 35$), Cubes ($1 \dots 15$) & Prime Powers

### 2.1 Squares ($11^2 \dots 35^2$)
- **11 to 20**: $11^2=121,\; 12^2=144,\; 13^2=169,\; 14^2=196,\; 15^2=225,\; 16^2=256,\; 17^2=289,\; 18^2=324,\; 19^2=361,\; 20^2=400$.
- **21 to 30**: $21^2=441,\; 22^2=484,\; 23^2=529,\; 24^2=576,\; 25^2=625,\; 26^2=676,\; 27^2=729,\; 28^2=784,\; 29^2=841,\; 30^2=900$.
- **31 to 35**: $31^2=961,\; 32^2=1024,\; 33^2=1089,\; 34^2=1156,\; 35^2=1225$.
- **Mental Squaring Shortcuts**:
  - **Ending in $5$**: $(10a + 5)^2 = \overline{[a(a+1)]25}$ (e.g., $65^2 \to 6 \times 7 = 42 \implies \mathbf{4225}$; $85^2 \to 8 \times 9 = 72 \implies \mathbf{7225}$).
  - **Near $50$ ($50 \pm k$)**: $(25 \pm k) \times 100 + k^2$ (e.g., $47^2 = (25-3)\text{ hundred} + 3^2 = \mathbf{2209}$; $54^2 = (25+4)\text{ hundred} + 4^2 = \mathbf{2916}$).
  - **Near $100$ ($100 \pm k$)**: $(100 \pm 2k) \times 100 + k^2$ (e.g., $96^2 = (100-8)\text{ hundred} + 4^2 = \mathbf{9216}$; $106^2 = \mathbf{11236}$).

### 2.2 Cubes ($1^3 \dots 15^3$) & Powers
- **Cubes**: $1^3=1,\; 2^3=8,\; 3^3=27,\; 4^3=64,\; 5^3=125,\; 6^3=216,\; 7^3=343,\; 8^3=512,\; 9^3=729,\; 10^3=1000,\; 11^3=1331,\; 12^3=1728,\; 13^3=2197,\; 14^3=2744,\; 15^3=3375$.
- **Powers of 2**: $2^7=128,\; 2^8=256,\; 2^9=512,\; 2^{10}=1024,\; 2^{11}=2048,\; 2^{12}=4096$.
- **Powers of 3 & 5**: $3^4=81,\; 3^5=243,\; 3^6=729;\quad 5^4=625,\; 5^5=3125,\; 5^6=15625$.

---

## 3. Fast DI Fraction Comparison & Percentage-Change Techniques

### Technique 1: $10\%$ + $1\%$ Base Decomposition (Never Divide!)
To find what percentage $273$ is of $780$:
- $10\%$ of $780 = 78$, so $30\% = 3 \times 78 = 234$.
- Remaining gap $= 273 - 234 = 39$, which is **exact half of $10\%$ ($78$)** $= 5\%$!
- Total $= 30\% + 5\% = \mathbf{35.0\%}$ in 4 seconds!

### Technique 2: Cross-Multiplication vs. Component Growth Rule (Comparing $\frac{a}{b}$ vs. $\frac{c}{d}$)
Suppose you want to know whether $\frac{142}{410}$ or $\frac{158}{450}$ is larger:
- Look at the **growth from left fraction to right fraction**:
  - Numerator grew by $158 - 142 = +16$ on $142$ ($\mathbf{> 11\%}$, since $10\%$ is $14.2$).
  - Denominator grew by $450 - 410 = +40$ on $410$ ($\mathbf{< 10\%}$, since $10\%$ is $41$).
- **Rule**: Whenever the **Numerator grows by a larger $\%$ than the Denominator**, the fraction **INCREASES** ($\frac{158}{450} > \frac{142}{410}$)!

### Technique 3: Denominator Shift Approximation ($\frac{N}{D \pm d} \approx \frac{N}{D} \mp \frac{d}{D}\%$)
To convert $\frac{74}{245}$ into a percentage:
- Scale denominator by $+2\%$ ($+5$ out of $250$) to reach clean $250$.
- Scale numerator by the same $+2\%$ ($+2\%$ of $74 \approx +1.5 \to 75.5$):
- $\frac{75.5}{250} = \frac{75.5 \times 4}{1000} = \mathbf{30.2\%}$ (exact value is $30.204\%$!).

---

## 4. Timed Speed-Math Active-Recall Drill (15 Prompts — Target: 5 Minutes)

<details><summary><b>Drill 1: Express 5/16 and 7/12 as exact percentages.</b></summary>
A: 1/16 = 6.25% -> 5/16 = 31.25%. 1/12 = 8.33% -> 7/12 = 58.33% (or 1/2 + 1/12 = 50% + 8.33% = 58.33%).
</details>

<details><summary><b>Drill 2: Compute 75^2 and 94^2 mentally in 5 seconds.</b></summary>
A: 75^2 -> 7*8 = 56 -> 5625. 94^2 (6 below 100) -> (94 - 6) = 88 hundred + 6^2 = 8836.
</details>

<details><summary><b>Drill 3: What percentage is 312 of 650?</b></summary>
A: 50% of 650 is 325. Difference = 325 - 312 = 13, which is 2% of 650 (since 1% is 6.5). Thus 50% - 2% = 48%.
</details>

<details><summary><b>Drill 4: Without dividing, which fraction is larger: 185/520 or 207/590?</b></summary>
A: From 185 to 207, numerator grows by +22 (22/185 < 12%, since 10%=18.5, 2%=3.7 -> +11.9%). Denominator grows from 520 to 590 by +70 (70/520 > 13%, since 10%=52, 3%=15.6 -> +13.5%). Since denominator grew faster than numerator, the fraction DECREASED -> 185/520 is larger!
</details>

<details><summary><b>Drill 5: Approximate 87 / 294 as a percentage to 1 decimal place.</b></summary>
A: Increase denominator 294 by +2% (+6) to 300; increase numerator 87 by +2% (+1.74) to 88.74. Divide by 3: 88.74 / 3 = 29.58% -> 29.6% (exact: 29.59%).
</details>

<details><summary><b>Drill 6: Revenue grew by +14.28% in Year 1 and +12.5% in Year 2, then fell by -11.11% in Year 3. Find the net percentage change over the 3 years.</b></summary>
A: Convert to fractions: (1 + 1/7) * (1 + 1/8) * (1 - 1/9) = (8/7) * (9/8) * (8/9) = 8/7 = 1 + 1/7 = +14.28% net increase!
</details>

<details><summary><b>Drill 7: Evaluate 53^2 - 47^2 mentally.</b></summary>
A: Use (a + b)(a - b) = (53 + 47)(53 - 47) = 100 * 6 = 600.
</details>

<details><summary><b>Drill 8: A company's sales grew from 240 in 2019 to 486 in 2023. Find its exact CAGR.</b></summary>
A: Number of periods n = 2023 - 2019 = 4. Ratio = 486 / 240 = 81 / 40? Wait: 486 / 96 = 81 / 16 (or from 320 to 1620 -> 81/16). For 320 to 1620 in 4 years: (1620/320)^(1/4) = (81/16)^(1/4) = 3/2 = 1.50 -> 50% CAGR. (For 240 to 486: 486/240 = 2.025 -> (2.025)^(1/4) ~ 19.3%,since 1.2^4 = 2.0736).
</details>

<details><summary><b>Drill 9: Multiply 44 x 37.5% x 64 / 11 mentally.</b></summary>
A: 44/11 = 4, and 37.5% = 3/8. Thus 4 * (3/8) * 64 = 4 * 3 * 8 = 96.
</details>

<details><summary><b>Drill 10: What is 625^2?</b></summary>
A: Using (100a + 25)^2: 6 * 6.5 = 39 -> append 0625 -> 390,625.
</details>

<details><summary><b>Drill 11: Recognize the decimal 0.42857... as a reduced fraction.</b></summary>
A: Cyclic 142857 family (multiples of 1/7 = 0.142857...): since 42 / 14 = 3, it is 3/7.
</details>

<details><summary><b>Drill 12: Recognize the percentage 41.67% as a reduced fraction.</b></summary>
A: Split as 50% - 8.33% = 1/2 - 1/12 = 5/12 (or 25% + 16.67% = 1/4 + 1/6 = 5/12).
</details>

<details><summary><b>Drill 13: What is the cube root of 2197 and 2744?</b></summary>
A: 2197 ends in 7 (3^3 = 27 ends in 7) and lies between 10^3(1000) and 20^3(8000) -> 13. 2744 ends in 4 (4^3 = 64 ends in 4) -> 14.
</details>

<details><summary><b>Drill 14: If Numerator increases by +20% and Denominator increases by +25%, by what % does the fraction change?</b></summary>
A: New fraction multiplier = 1.20 / 1.25 = 24 / 25 = 96 / 100 -> decreases by 4%!
</details>

<details><summary><b>Drill 15: Factor 1001, 111, and 2^10 - 1 into prime factors.</b></summary>
A: 1001 = 7 * 11 * 13; 111 = 3 * 37; 2^10 - 1 = 1023 = (2^5 - 1)(2^5 + 1) = 31 * 33 = 3 * 11 * 31.
</details>
