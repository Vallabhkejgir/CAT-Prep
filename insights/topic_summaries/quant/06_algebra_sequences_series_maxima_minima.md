# QA 06: Algebra — Sequences, Series, Telescoping Sums & Maxima/Minima

**Canonical Taxonomy Mapping**: `QA > Algebra > Sequences & Series`, `Maxima & Minima`  
**Weightage**: ~8–12% of QA (2–3 questions per slot)  
**Priority Tier**: Tier 1 (High-Yield Core)

---

## 1. 30-Second Concept & Formula Blueprint

### 1.1 Arithmetic, Geometric & Harmonic Progressions (AP, GP, HP)
- **Arithmetic Progression (AP)**:
  $$T_n = a + (n-1)d, \quad S_n = \frac{n}{2}[2a + (n-1)d] = \frac{n}{2}(T_1 + T_n) = n \cdot T_{\text{middle}}$$
  - *Quadratic Sum Signature*: A sequence is an AP iff $S_n = An^2 + Bn$ (no constant term!). Then:
    $$\text{First term } a = A + B, \quad \text{Common difference } d = 2A, \quad T_n = 2An + (B - A)$$
  - *Symmetric Term Selections*:
    - 3 terms in AP: $a - d,\; a,\; a + d$
    - 4 terms in AP: $a - 3d,\; a - d,\; a + d,\; a + 3d$ (common difference $= 2d$)
  - *Common Terms of Two APs* (with common differences $d_1, d_2$): Form a new AP with common difference $D = \text{LCM}(d_1, d_2)$.
- **Geometric Progression (GP)**:
  $$T_n = a r^{n-1}, \quad S_n = \frac{a(r^n - 1)}{r - 1} \;\;(r \neq 1), \quad S_\infty = \frac{a}{1 - r} \;\;(|r| < 1)$$
  - Product of $n$ terms of a GP: $P_n = (T_1 \cdot T_n)^{n/2} = (T_{\text{middle}})^n$.
- **Harmonic Progression (HP)**:
  $\frac{1}{T_1}, \frac{1}{T_2}, \dots, \frac{1}{T_n}$ form an AP. Harmonic Mean of two positive numbers: $\text{HM} = \frac{2ab}{a+b}$.
- **Arithmetico-Geometric Progression (AGP)**:
  For $S_n = \sum_{k=1}^{n} [a + (k-1)d]r^{k-1}$ ($r \neq 1$):
  $$S_n = \frac{a}{1 - r} + \frac{dr(1 - r^{n-1})}{(1 - r)^2} - \frac{[a + (n-1)d]r^n}{1 - r}, \quad S_\infty = \frac{a}{1 - r} + \frac{dr}{(1 - r)^2} \quad (|r| < 1)$$

---

### 1.2 Power Sums, Telescoping Series & Method of Differences
- **Standard Power Sums**:
  $$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}, \quad \sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}, \quad \sum_{k=1}^{n} k^3 = \left[\frac{n(n+1)}{2}\right]^2$$
- **Canonical Telescoping Decompositions**:
  1. **Two-Factor Reciprocal**:
     $$\frac{1}{k(k+d)} = \frac{1}{d}\left(\frac{1}{k} - \frac{1}{k+d}\right) \implies \sum_{k=1}^{n} \frac{1}{k(k+1)} = 1 - \frac{1}{n+1} = \frac{n}{n+1}$$
  2. **Three-Factor Reciprocal**:
     $$\frac{1}{k(k+1)(k+2)} = \frac{1}{2}\left[\frac{1}{k(k+1)} - \frac{1}{(k+1)(k+2)}\right] \implies \sum_{k=1}^{n} \frac{1}{k(k+1)(k+2)} = \frac{1}{4} - \frac{1}{2(n+1)(n+2)}$$
  3. **Rising Factorial Products**:
     $$k(k+1)(k+2)\dots(k+m-1) \implies \text{Sum} = \frac{n(n+1)(n+2)\dots(n+m)}{m+1}$$
  4. **Factorial Telescoping**:
     $$k \cdot k! = (k+1)! - k! \implies \sum_{k=1}^{n} k \cdot k! = (n+1)! - 1$$
     $$\frac{k}{(k+1)!} = \frac{1}{k!} - \frac{1}{(k+1)!} \implies \sum_{k=1}^{n} \frac{k}{(k+1)!} = 1 - \frac{1}{(n+1)!}$$
  5. **Perfect-Square Inside Radical ($1 + \frac{1}{k^2} + \frac{1}{(k+1)^2}$)**:
     $$\sqrt{1 + \frac{1}{k^2} + \frac{1}{(k+1)^2}} = 1 + \frac{1}{k} - \frac{1}{k+1}$$

---

### 1.3 Maxima & Minima (AM-GM-HM, Weighted Splitting & Cauchy-Schwarz)
- **AM-GM-HM Inequality (STRICT DOMAIN: $x_1, x_2, \dots, x_n > 0$ — Positive Reals ONLY!)**:
  $$\frac{x_1 + x_2 + \dots + x_n}{n} \ge \sqrt[n]{x_1 x_2 \dots x_n} \ge \frac{n}{\frac{1}{x_1} + \frac{1}{x_2} + \dots + \frac{1}{x_n}}$$
  - Equality holds iff $x_1 = x_2 = \dots = x_n$.
  - For $x > 0$: $x + \frac{1}{x} \ge 2$; for $x < 0$: $x + \frac{1}{x} \le -2$.
- **Weighted Term-Splitting for Constrained Optimization**:
  - **Given Sum $a x + b y + c z = S$, maximize Product $x^p y^q z^r$**:
    Split $ax$ into $p$ equal parts of $\frac{ax}{p}$, $by$ into $q$ equal parts of $\frac{by}{q}$, $cz$ into $r$ equal parts of $\frac{cz}{r}$. Equality occurs when:
    $$\frac{ax}{p} = \frac{by}{q} = \frac{cz}{r} = \frac{S}{p + q + r}$$
  - **Given Variable Cancellation Needed (e.g., minimize $x^2 + \frac{16}{x}$ for $x > 0$)**:
    Split $\frac{16}{x} = \frac{8}{x} + \frac{8}{x}$ so the product $x^2 \cdot \frac{8}{x} \cdot \frac{8}{x} = 64$ is independent of $x$:
    $$x^2 + \frac{8}{x} + \frac{8}{x} \ge 3\sqrt[3]{64} = 12 \quad (\text{at } x^2 = \frac{8}{x} \implies x = 2)$$
- **Cauchy-Schwarz / Titu's Lemma** (for all $a_i \in \mathbb{R}$ and $b_i > 0$):
  $$(a_1^2 + a_2^2 + \dots + a_n^2)(b_1^2 + b_2^2 + \dots + b_n^2) \ge (a_1 b_1 + a_2 b_2 + \dots + a_n b_n)^2$$
  $$\frac{a_1^2}{b_1} + \frac{a_2^2}{b_2} + \dots + \frac{a_n^2}{b_n} \ge \frac{(a_1 + a_2 + \dots + a_n)^2}{b_1 + b_2 + \dots + b_n}$$

---

## 2. Pattern-Recognition Trigger Table

| Question Cue / Wording | Hidden Constraint | Fastest Attack Strategy |
| :--- | :--- | :--- |
| "Ratio of sums of $n$ terms of two APs is $\frac{S_n}{S'_n} = \frac{an+b}{cn+d}$; find ratio of $m$-th terms $\frac{T_m}{T'_m}$" | $S_{2m-1} = (2m-1) \cdot T_m$ | Substitute $n = 2m - 1$ directly into the sum ratio! |
| "If $T_p = q$ and $T_q = p$ in an AP, find $T_n$ and $S_{p+q}$" | Slope $d = \frac{p-q}{q-p} = -1$ | $T_n = p + q - n$; $T_{p+q} = 0$; $S_{p+q} = \frac{p+q}{2}(p+q-1)$ |
| "Sequence $3, 7, 13, 21, 31, \dots$; find $T_{20}$" | First differences $4, 6, 8, 10$ form an AP $\implies T_n$ is quadratic $An^2 + Bn + C$ | Second difference $2A = 2 \implies A = 1$; fit $n=1, 2$ to get $T_n = n^2 + n + 1$ in 10 seconds |
| "Evaluate $\sum_{k=1}^{99} \sqrt{1 + \frac{1}{k^2} + \frac{1}{(k+1)^2}}$" | Inside radical is $\left(1 + \frac{1}{k} - \frac{1}{k+1}\right)^2$ | Sum $= 99(1) + \left(1 - \frac{1}{100}\right) = 99.99$ |
| "Given $2x + 3y + 4z = 36$ ($x, y, z > 0$), maximize $x^2 y^3 z^4$" | Exponents match coefficients ($2, 3, 4$)! | Set $\frac{2x}{2} = \frac{3y}{3} = \frac{4z}{4} = \frac{36}{2+3+4} = 4 \implies x=y=z=4 \implies \text{Max} = 4^9$ |

---

## 3. Canonical CAT Archetypes & Solved Exemplars

### Archetype 1: Common Terms of Three Arithmetic Progressions
> **Problem**: Find the number of common terms in the three sequences:
> $S_1: 3, 7, 11, 15, \dots, 403$
> $S_2: 2, 5, 8, 11, \dots, 404$
> $S_3: 1, 6, 11, 16, \dots, 401$

- **First-Principles Method**:
  1. By inspection, the first common term across all three APs is $a = 11$.
  2. Common difference of the intersection sequence is $D = \text{LCM}(d_1, d_2, d_3) = \text{LCM}(4, 3, 5) = 60$.
  3. Upper bound is the smallest last term of the three sequences: $\min(403, 404, 401) = 401$.
  4. General common term: $11 + 60(k - 1) \le 401 \implies 60(k - 1) \le 390 \implies k - 1 \le 6.5 \implies k - 1 \in \{0, 1, 2, 3, 4, 5, 6\}$.
  5. Total common terms $= \mathbf{7}$.

- **30-Second Exam-Hall Speed Shortcut**:
  - Spot first match $11$, take $\text{LCM}(4, 3, 5) = 60$, compute $\left\lfloor \frac{401 - 11}{60} \right\rfloor + 1 = 6 + 1 = \mathbf{7}$.

---

### Archetype 2: AM-GM Term Splitting with Shifted Denominator
> **Problem**: For $x > 3$, find the minimum possible value of $f(x) = x + \frac{16}{x - 3}$.

- **First-Principles Method**:
  1. The denominator is $(x - 3) > 0$. Subtract and add $3$ to match the denominator:
     $$f(x) = (x - 3) + \frac{16}{x - 3} + 3$$
  2. Apply AM-GM to the two positive terms $(x - 3)$ and $\frac{16}{x - 3}$:
     $$(x - 3) + \frac{16}{x - 3} \ge 2\sqrt{(x - 3) \cdot \frac{16}{x - 3}} = 2 \times 4 = 8$$
  3. Equality holds at $x - 3 = \frac{16}{x - 3} \implies x - 3 = 4 \implies x = 7 > 3$ (valid!).
  4. Minimum value $= 8 + 3 = \mathbf{11}$.

- **30-Second Exam-Hall Speed Shortcut**:
  - Set $(x - 3)^2 = 16 \implies x - 3 = 4 \implies x = 7$, plug in: $7 + \frac{16}{4} = \mathbf{11}$.

---

### Archetype 3: Telescoping Series via $n = 1, 2$ Small-Case Pattern Check
> **Problem**: Evaluate $S_{20} = \sum_{k=1}^{20} \frac{2k + 1}{k^2 (k + 1)^2}$.

- **First-Principles Method**:
  1. Notice that $2k + 1 = (k + 1)^2 - k^2$.
  2. Split the general term:
     $$\frac{(k+1)^2 - k^2}{k^2(k+1)^2} = \frac{1}{k^2} - \frac{1}{(k+1)^2}$$
  3. Summing from $k = 1$ to $20$ telescopes to:
     $$S_{20} = \frac{1}{1^2} - \frac{1}{21^2} = 1 - \frac{1}{441} = \mathbf{\frac{440}{441}}$$

- **30-Second Exam-Hall Speed Shortcut ($n = 1, 2$ Substitution)**:
  - $S_1 = \frac{3}{4} = 1 - \frac{1}{2^2}$; $S_2 = \frac{3}{4} + \frac{5}{36} = \frac{32}{36} = \frac{8}{9} = 1 - \frac{1}{3^2}$.
  - Pattern is unmistakably $S_n = 1 - \frac{1}{(n+1)^2} \implies S_{20} = \mathbf{\frac{440}{441}}$.

---

## 4. Boundary Conditions, Domain Traps & TITA Pitfalls

1. **AM-GM Equality Attainability Trap ($\min(x + 1/x)$ on Restricted Intervals)**:
   - For $f(x) = x + \frac{9}{x}$ where $x \ge 5$, AM-GM gives $\ge 6$ at $x = 3$. Since $x = 3$ is **outside** the allowed domain $x \ge 5$, and $x + \frac{a}{x}$ is strictly increasing for $x > \sqrt{a}$, the true minimum on $[5, \infty)$ occurs at the boundary $x = 5$: $5 + \frac{9}{5} = 6.8$, NOT $6$!
2. **Integer Constraint vs. Real Constraint in AM-GM**:
   - If $x + y = 11$ and $x, y$ are **positive integers**, the maximum of $xy$ occurs at $\{5, 6\} \implies 30$, NOT $(5.5)^2 = 30.25$.
3. **Fake AP Sum with Constant Term ($S_n = An^2 + Bn + C, C \neq 0$)**:
   - If $S_n = 3n^2 + 2n + 5$, then $T_1 = S_1 = 10$, while for $n \ge 2$, $T_n = S_n - S_{n-1} = 6n - 1$ ($T_2 = 11, T_3 = 17, \dots$). The sequence is an AP **only from the 2nd term onward** ($T_1$ is anomalous!). Always use $T_n = S_n - S_{n-1}$ for $n \ge 2$.

---

## 5. Active-Recall Drill (10 Prompts)

<details><summary>Q1: The sum of the first n terms of two APs are in the ratio (3n + 8) : (7n + 15). Find the ratio of their 12th terms.</summary>
A: Substitute n = 2(12) - 1 = 23 into the sum ratio: (3*23 + 8) / (7*23 + 15) = 77 / 176 = 7 / 16.
</details>

<details><summary>Q2: Evaluate the infinite AGP sum: S = 1 + 2/3 + 3/9 + 4/27 + 5/81 + ...</summary>
A: Here a = 1, d = 1, r = 1/3. Using S_inf = a/(1-r) + dr/(1-r)^2 = 1/(2/3) + (1/3)/(4/9) = 3/2 + 3/4 = 9/4 = 2.25.
</details>

<details><summary>Q3: Find the sum of the series: 1/(1*4) + 1/(4*7) + 1/(7*10) + ... + 1/(28*31).</summary>
A: (1/3) * (1/1 - 1/31) = (1/3) * (30/31) = 10/31.
</details>

<details><summary>Q4: For positive real numbers a, b, c, find the minimum value of (a + b + c)(1/a + 1/b + 1/c).</summary>
A: By AM >= HM (or Cauchy-Schwarz), (a + b + c)(1/a + 1/b + 1/c) >= 3^2 = 9 (attained at a = b = c).
</details>

<details><summary>Q5: If x, y > 0 and x + y = 12, find the maximum value of x^3 * y.</summary>
A: Split x into 3 equal parts: (x/3) + (x/3) + (x/3) + y = 12. Equality when x/3 = y = 12/4 = 3 -> x = 9, y = 3. Maximum value = 9^3 * 3 = 2187.
</details>

<details><summary>Q6: Evaluate 1*1! + 2*2! + 3*3! + ... + 10*10!.</summary>
A: Using k*k! = (k+1)! - k!, the sum telescopes to 11! - 1! = 11! - 1.
</details>

<details><summary>Q7: In a sequence, S_n = 2n^2 + 3n + 4. Find T_1 and T_5.</summary>
A: T_1 = S_1 = 2 + 3 + 4 = 9. For n >= 2, T_n = S_n - S_(n-1) = 4n + 1 (since C = 4 cancels for n >= 2). Thus T_5 = 4(5) + 1 = 21.
</details>

<details><summary>Q8: Find the minimum value of 4*sin^2(theta) + 9*csc^2(theta) for sin(theta) != 0.</summary>
A: AM-GM gives >= 2*sqrt(4*9) = 12, which requires 4*sin^2 = 9/sin^2 -> sin^2(theta) = 9/4 = 2.25 > 1 (IMPOSSIBLE!). Since sin^2(theta) <= 1, the minimum occurs at the boundary sin^2(theta) = 1, giving 4(1) + 9(1) = 13.
</details>

<details><summary>Q9: If the 5th term of a GP is 3, find the product of its first 9 terms.</summary>
A: Since T_5 is the middle term of the first 9 terms, P_9 = (T_5)^9 = 3^9 = 19,683.
</details>

<details><summary>Q10: Find the 15th term of the sequence: 2, 5, 10, 17, 26, ...</summary>
A: Notice T_n = n^2 + 1. Thus T_15 = 15^2 + 1 = 226.
</details>
