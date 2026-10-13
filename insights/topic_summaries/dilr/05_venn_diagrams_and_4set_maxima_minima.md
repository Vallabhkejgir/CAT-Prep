# DILR 05: Venn Diagrams & 3-Set / 4-Set Maxima-Minima Optimization

**Canonical Taxonomy Mapping**: `DILR > Venn Diagrams & Set Theory Optimization (3-Set & 4-Set)`  
**Weightage**: ~15–20% of DILR (1 set every 1–2 slots)  
**Priority Tier**: Tier 1 (High-Yield Core)

---

## 1. Visual & Structural Anatomy

CAT Venn sets come in two distinct flavors:
1. **3-Set / 4-Set Exact Region Reconstruction**: Uses clues about "only A", "both A and B", "A or B", and "neither A nor B" to lock all $2^3 = 8$ (or $2^4 = 16$) elementary regions.
2. **Set Theory Maxima & Minima (Surplus / Layer Optimization)**: Gives fixed set totals $|A|, |B|, |C|, |D|$ and universe $|U|$, then asks for the **maximum or minimum possible number of elements** in "at least $k$ sets", "exactly $k$ sets", or a specific region like $|A \cap B \cap C'|$.

---

## 2. Green Flags vs. Red Flags

- **Green Flags**:
  - Standard 3-set or 4-set survey with explicit set sizes $|A|, |B|, |C|, |D|$ and layer constraints ("number of people in exactly 2 sets is twice those in all 4 sets").
  - **Highest-priority Bucket A pick** because the $E_1, E_2, E_3, E_4$ equations are $100\%$ mechanical and cannot branch uncontrollably.
- **Red Flags**:
  - Venn diagrams combined with changing membership over 3 time periods (e.g., customers switching brands across Jan, Feb, Mar) unless row/column conservation is clear.

---

## 3. Scratchpad Representation Template

### A. 3-Set Venn Diagram ($2^3 = 8$ Regions)
Label the 7 interior regions with single lowercase letters by layer:
- **Exactly 1 ($E_1 = a + b + c$)**: $a$ (only A), $b$ (only B), $c$ (only C).
- **Exactly 2 ($E_2 = d + e + f$)**: $d$ ($A \cap B$ only), $e$ ($B \cap C$ only), $f$ ($C \cap A$ only).
- **Exactly 3 ($E_3 = g$)**: $g$ ($A \cap B \cap C$).
- **Outside ($E_0 = n$)**: Neither A, B, nor C.

### B. 4-Set Venn Grid ($2^4 = 16$ Regions — NEVER Draw 4 Overlapping Circles!)
Four circles cannot represent all $\binom{4}{2} = 6$ pairwise intersections symmetrically. Instead, draw a **$4 \times 4$ Karnaugh Grid** or list the 4 layers explicitly:

```text
+-----------------------------------------------------------------------+
| 4-SET LAYER SYSTEM:                                                   |
| E_1 (4 regions):  only A, only B, only C, only D                      |
| E_2 (6 regions):  AB, AC, AD, BC, BD, CD (each 'only')                |
| E_3 (4 regions):  ABC, ABD, ACD, BCD (each 'only')                    |
| E_4 (1 region):   ABCD (all four)                                     |
| E_0 (1 region):   None                                                |
+-----------------------------------------------------------------------+
| KARNAUGH 4x4 GRID FOR SETS A, B, C, D:                                |
|            |   C & D    |  C & not-D | not-C & D  | not-C & not-D     |
| -----------+------------+------------+------------+------------------ |
| A & B      |  ABCD (E4) |  ABC only  |  ABD only  |   AB only         |
| A & not-B  |  ACD only  |  AC only   |  AD only   |   A only          |
| not-A & B  |  BCD only  |  BC only   |  BD only   |   B only          |
| not-A&not-B|  CD only   |  C only    |  D only    |   None (E0)       |
+-----------------------------------------------------------------------+
```

---

## 4. Anchor Clue & Case-Splitting Rules: Natural Language to Region Mapping

| English Wording in Prompt | Exact Algebraic Region Translation (3-Set) |
| :--- | :--- |
| **"A"** | $a + d + f + g$ (Entire circle A) |
| **"Only A"** | $a$ |
| **"A and B"** / **"Both A and B"** | $d + g$ (Includes $g$ unless "only" or "not C" is stated!) |
| **"Only A and B"** / **"A and B but not C"** | $d$ |
| **"A or B"** | $a + b + d + e + f + g = |A \cup B \cup C| - c$ |
| **"Only A or B"** (i.e., not C) | $a + b + d$ |
| **"At least 2 sets"** | $E_2 + E_3 (+ E_4) = d + e + f + g$ |
| **"At most 2 sets"** | $E_0 + E_1 + E_2 = U - E_3 (- E_4)$ |
| **"More than 1 set"** | $E_2 + E_3 (+ E_4)$ |

---

## 5. Mathematical Invariants: The Master Layer Equations & Surplus Optimization

### 5.1 The Two Master Equations (4-Set General Form)
Let $U$ be the total universe, $E_0$ be "None", and $S = |A| + |B| + |C| + |D|$ be the sum of the individual set sizes:
$$\text{(Eq 1: Headcount Conservation)} \quad E_1 + E_2 + E_3 + E_4 = U - E_0$$
$$\text{(Eq 2: Membership Ticket Sum)} \quad E_1 + 2E_2 + 3E_3 + 4E_4 = S = |A| + |B| + |C| + |D|$$

**Subtracting $(\text{Eq } 2) - (\text{Eq } 1)$ gives the Golden Surplus Identity**:
$$\mathbf{E_2 + 2E_3 + 3E_4 = S - (U - E_0)}$$
*(For 3 sets, simply set $E_4 = 0$: $\mathbf{E_2 + 2E_3 = S - (U - E_0)}$.)*

---

### 5.2 Maxima & Minima of $E_k$ Given Fixed $(U - E_0)$ and $S$
Suppose $U - E_0 = 100$ (everyone belongs to at least 1 set) and $S = |A| + |B| + |C| = 190$.
Then the surplus is $E_2 + 2E_3 = 190 - 100 = 90$:
1. **To MAXIMIZE $E_3$ (all 3 sets)**:
   - Make $E_2$ as small as possible ($E_2 = 0$, provided $2E_3 \le 90$ and $E_3 \le \min(|A|,|B|,|C|)$):
     $$E_{3,\max} = \min\left(\left\lfloor \frac{S - (U - E_0)}{2} \right\rfloor,\; |A|,\; |B|,\; |C|\right) = \left\lfloor \frac{90}{2} \right\rfloor = 45$$
   - *(Note: If $E_0$ is NOT fixed and can be $> 0$, then to maximize $E_3$ across all possible $E_0$, $E_{3,\max} = \min(|A|, |B|, |C|)$ or bounded by $3E_3 + E_1 + 2E_2 = S$.)*
2. **To MINIMIZE $E_3$ (all 3 sets)**:
   - Make $E_2$ as large as possible. Since $E_1 + E_2 + E_3 = 100 \implies E_2 \le 100 - E_3$ (at $E_1 = 0$):
     $$E_{3,\min} = \max\big(0,\; S - 2(U - E_0)\big) = \max(0, 190 - 200) = 0$$
3. **In a 4-Set System with $E_2 + 2E_3 + 3E_4 = \text{Surplus}$**:
   - **Maximum of $E_4$** (when $E_0 = 0$ is fixed): $\left\lfloor \frac{S - U}{3} \right\rfloor$ (capped by $\min(|A|,|B|,|C|,|D|)$).
   - **Minimum of $E_4$**: $\max(0,\; S - 3U)$.

---

## 6. Solved Archetype Walkthrough: 4-Set Survey Optimization

> **Set Scenario**: In a survey of $150$ investors, every investor invests in at least one of 4 asset classes: Stocks ($S = 100$), Bonds ($B = 90$), Gold ($G = 80$), and Real Estate ($R = 70$).
> 1. What is the **maximum** possible number of investors who invested in **all 4** asset classes ($E_4$)?
> 2. What is the **minimum** possible number of investors who invested in **at least 3** asset classes ($E_3 + E_4$)?
> 3. If exactly $20$ investors invested in all 4 asset classes and $30$ invested in exactly 1 asset class, find $E_2$ and $E_3$.

### Step-by-Step Execution
1. **Write the Two Master Equations**:
   - $U - E_0 = 150 \implies E_1 + E_2 + E_3 + E_4 = 150$
   - Total tickets $S = 100 + 90 + 80 + 70 = 340 \implies E_1 + 2E_2 + 3E_3 + 4E_4 = 340$
   - Subtracting gives the **Surplus Equation**:
     $$E_2 + 2E_3 + 3E_4 = 340 - 150 = 190$$
2. **Question 1 (Maximize $E_4$)**:
   - From $3E_4 \le 190 \implies E_4 \le \lfloor 190 / 3 \rfloor = 63$.
   - Also check individual set cap: $E_4 \le \min(100, 90, 80, 70) = 70$.
   - At $E_4 = 63$, $E_2 + 2E_3 = 190 - 189 = 1 \implies E_2 = 1, E_3 = 0$, and $E_1 = 150 - (1 + 0 + 63) = 86 \ge 0$ (and each set has enough remaining capacity).
   - Thus $\mathbf{E_{4,\max} = 63}$.
3. **Question 2 (Minimize $E_3 + E_4$)**:
   - To minimize $(E_3 + E_4)$, pack as much surplus as possible into $E_2$ (by setting $E_1 = 0$ and $E_4 = 0$):
     - $E_2 + E_3 = 150 \implies E_2 = 150 - E_3$.
     - Substitute into Surplus: $(150 - E_3) + 2E_3 = 190 \implies E_3 = 40$.
   - Thus $\mathbf{(E_3 + E_4)_{\min} = 40}$.
4. **Question 3 ($E_4 = 20$ and $E_1 = 30$)**:
   - From Headcount: $E_2 + E_3 = 150 - (30 + 20) = 100$.
   - From Surplus: $E_2 + 2E_3 = 190 - 3(20) = 130$.
   - Subtracting: $\mathbf{E_3 = 30}$ and $\mathbf{E_2 = 70}$.

---

## 7. Active-Recall Drills

<details><summary>Q1: How many elementary regions exist in a 4-set Venn diagram (including Outside/None)?</summary>
A: 2^4 = 16 regions: 1 (None) + 4 (Exactly 1) + 6 (Exactly 2) + 4 (Exactly 3) + 1 (All 4) = 16.
</details>

<details><summary>Q2: In a group of 100 students, everyone plays at least one of Cricket (70), Football (60), and Tennis (50). What is the maximum and minimum number of students who play all three sports?</summary>
A: Surplus: E_2 + 2E_3 = (70 + 60 + 50) - 100 = 80. Max E_3 = min(floor(80/2), 50) = 40. Min E_3 = max(0, 180 - 200) = 0.
</details>

<details><summary>Q3: In the same group of 100 students (C=70, F=60, T=50, None=0), if 'None' was NOT fixed at 0 (i.e., some students could play 0 sports), what would be the maximum possible number of students playing all 3 sports?</summary>
A: Without the E_0 = 0 restriction, E_0 can increase up to 30 (since C = 70 <= 70). Setting E_3 = 50 (the size of the smallest set T) is possible with E_0 = 30,only C = 10, C&F only = 10, and F only = 0! Wait: if E_3 = 50, C+F+T remaining = 20 + 10 + 0 = 30 -> E_1 = 30, total = 80, E_0 = 20 -> Valid! So Max E_3 = 50.
</details>

<details><summary>Q4: What is the difference between 'Students who like Physics and Chemistry' vs 'Students who like only Physics and Chemistry' in a 3-set (P, C, M) diagram?</summary>
A: 'Physics and Chemistry' is P intersect C (includes those who also like Math, i.e., d + g). 'Only Physics and Chemistry' excludes Math (d only).
</details>

<details><summary>Q5: In a 4-set Venn problem with U = 200, E_0 = 10, and |A|+|B|+|C|+|D| = 420, what is the value of E_2 + 2E_3 + 3E_4?</summary>
A: S - (U - E_0) = 420 - (200 - 10) = 420 - 190 = 230.
</details>
