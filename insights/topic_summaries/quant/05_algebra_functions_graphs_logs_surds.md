# QA 05: Algebra — Functions, Graphs, Functional Equations, Logarithms, Surds & Indices

**Canonical Taxonomy Mapping**: `QA > Algebra > Logarithms, Surds & Indices`, `Functions, Graphs & Functional Equations`  
**Weightage**: ~10–14% of QA (2–3 questions per slot)  
**Priority Tier**: Tier 1 (High-Yield Core)

---

## 1. 30-Second Concept & Formula Blueprint

### 1.1 Logarithms (Strict Domain + Core Identities)
- **Strict Domain Conditions for $\log_b(a)$**:
  $$a > 0, \quad b > 0, \quad b \neq 1$$
- **Fundamental Identities** (valid when all bases and arguments satisfy domain rules):
  - $\log_b(xy) = \log_b x + \log_b y, \quad \log_b\left(\frac{x}{y}\right) = \log_b x - \log_b y$
  - $\log_{b^m}\left(a^n\right) = \frac{n}{m}\log_b a$
  - **Base Change & Chain Rule**: $\log_b a = \frac{\log_k a}{\log_k b} = \frac{1}{\log_a b}$, and $\log_a b \cdot \log_b c \cdot \log_c d = \log_a d$
  - **Exponent-Swap Identity**: $a^{\log_b c} = c^{\log_b a}$
- **Logarithmic Inequalities (Base Sign-Flip Rule!)**:
  - If **Base $b > 1$**: $\log_b x > \log_b y \iff x > y > 0$ (direction **preserved**).
  - If **Base $0 < b < 1$**: $\log_b x > \log_b y \iff 0 < x < y$ (direction **REVERSED**!).
- **Characteristic & Mantissa ($\log_{10} N = c + m$, where $c \in \mathbb{Z}$ and $0 \le m < 1$)**:
  - For $N \ge 1$: Number of digits in $N$ in base $10$ is $\lfloor \log_{10} N \rfloor + 1 = c + 1$.
  - For $0 < N < 1$: Number of leading zeros immediately after the decimal point before the first significant digit is $|c| - 1 = \lfloor -\log_{10} N \rfloor$.
  - Standard values to memorize: $\log_{10} 2 \approx 0.30103$, $\log_{10} 3 \approx 0.47712$, $\log_{10} 7 \approx 0.84510$.

---

### 1.2 Surds, Indices & Nested Radicals
- **De-nesting Square Roots ($\sqrt{a \pm 2\sqrt{b}}$)**:
  Find $x \ge y > 0$ such that $x + y = a$ and $xy = b$:
  $$\sqrt{a \pm 2\sqrt{b}} = \sqrt{x} \pm \sqrt{y} \quad (x \ge y)$$
  *Always take the positive root $|\sqrt{x} - \sqrt{y}|$!*
- **Rationalizing Telescoping Sums**:
  $$\frac{1}{\sqrt{k+1} + \sqrt{k}} = \sqrt{k+1} - \sqrt{k}, \quad \frac{d}{\sqrt{a + d} + \sqrt{a}} = \sqrt{a + d} - \sqrt{a}$$
- **Comparison of Surds**:
  - Constant Sum ($a + b = \text{const}$): Larger product $ab \implies$ **Larger** $\sqrt{a} + \sqrt{b}$, and **Smaller** $|\sqrt{a} - \sqrt{b}|$.
  - Powers $a^{1/n}$ vs $b^{1/m}$: Raise both to $\text{LCM}(n, m)$.
- **Exponential Equations $f(x)^{g(x)} = 1$ (3-Case Checklist)**:
  1. **Case 1**: Base $f(x) = 1$ (and $g(x)$ is defined).
  2. **Case 2**: Exponent $g(x) = 0$ AND Base $f(x) \neq 0$.
  3. **Case 3**: Base $f(x) = -1$ AND Exponent $g(x)$ is an **even integer** (or rational with even numerator and odd denominator in lowest terms).

---

### 1.3 Functions, Graphs, GIF & Functional Equations
- **Counting Functions from Set $A$ ($|A|=m$) to Set $B$ ($|B|=n$)**:
  - Total functions: $n^m$
  - Injective (One-to-One): $P(n, m) = \frac{n!}{(n-m)!}$ (if $m \le n$, else $0$)
  - Surjective (Onto) for $m \ge n$: $\sum_{k=0}^{n} (-1)^k \binom{n}{k} (n - k)^m$ (for $n=2$: $2^m - 2$)
  - Bijective ($m = n$): $n!$
- **Standard Cauchy Functional Equations** (for continuous/well-behaved functions):

| Functional Equation | Standard Function Family | Quick Value-Plugging Test |
| :--- | :--- | :--- |
| $f(x + y) = f(x) + f(y)$ | $f(x) = kx$ | $f(0) = 0$; $f(n) = n \cdot f(1)$ |
| $f(x + y) = f(x) \cdot f(y)$ | $f(x) = a^x$ | $f(0) = 1$; $f(n) = [f(1)]^n$ |
| $f(xy) = f(x) + f(y)$ | $f(x) = k \log x$ | $f(1) = 0$; $f(a^n) = n \cdot f(a)$ |
| $f(xy) = f(x) \cdot f(y)$ | $f(x) = x^k$ | $f(1) = 1$ |
| $f(x) \cdot f(1/x) = f(x) + f(1/x)$ | $f(x) = 1 \pm x^n$ | Determine sign $\pm$ and $n$ from given point $f(a)$ |
| $f(x) + f(1 - x) = c$ | Symmetric around $x = 1/2$ | Pair terms $f(k/n) + f(1 - k/n) = c$ |

- **Greatest Integer Function $\lfloor x \rfloor$ & Fractional Part $\{x\} = x - \lfloor x \rfloor \in [0, 1)$**:
  - $\lfloor x + n \rfloor = \lfloor x \rfloor + n$ for $n \in \mathbb{Z}$
  - $\lfloor x \rfloor + \lfloor -x \rfloor = \begin{cases} 0 & \text{if } x \in \mathbb{Z} \\ -1 & \text{if } x \notin \mathbb{Z} \end{cases}$
  - $\{x\} + \{-x\} = \begin{cases} 0 & \text{if } x \in \mathbb{Z} \\ 1 & \text{if } x \notin \mathbb{Z} \end{cases}$
  - **Hermite's Identity**: $\lfloor x \rfloor + \left\lfloor x + \frac{1}{n} \right\rfloor + \dots + \left\lfloor x + \frac{n-1}{n} \right\rfloor = \lfloor nx \rfloor$

---

## 2. Pattern-Recognition Trigger Table

| Question Cue / Wording | Hidden Constraint | Fastest Attack Strategy |
| :--- | :--- | :--- |
| "$\log_x(a) + \log_a(x) = k$" | Substitution $t = \log_a(x) \implies t + \frac{1}{t} = k$ | Solve $t^2 - kt + 1 = 0$; product of roots $t_1 t_2 = 1$, sum $t_1 + t_2 = k \implies x_1 x_2 = a^k$ |
| "Sum of all real $x$ satisfying $\log_a(x^2 - bx + c) = d$" | Quadratic $x^2 - bx + c = a^d$; verify $\Delta \ge 0$ | Sum of roots is simply $b$ (provided $b^2 - 4(c - a^d) > 0$) |
| "$f(x) = \frac{a^x}{a^x + \sqrt{a}}$; find $\sum_{k=1}^{n-1} f\left(\frac{k}{n}\right)$" | $f(x) + f(1 - x) = 1$ for all $x$ | Pair $k$ and $n-k$: total sum $= \frac{n-1}{2} \times 1$ |
| "Cycle of composite function $f(f(\dots f(x))) = f^{(n)}(x)$ for $f(x) = \frac{1}{1-x}$ or $\frac{1-x}{1+x}$" | Möbius transformations often have period $2, 3, 4,$ or $6$ | Compute $f^{(1)}(x), f^{(2)}(x), f^{(3)}(x)$ by plugging a simple test number like $x = 2$; use $n \bmod \text{period}$ |
| "Solve $(x^2 - 5x + 5)^{x^2 - 9x + 20} = 1$" | Base $= -1$ with even exponent is often missed | Check all 3 cases: Base $= 1$, Exponent $= 0$ (Base $\neq 0$), and Base $= -1$ (Exponent even) |

---

## 3. Canonical CAT Archetypes & Solved Exemplars

### Archetype 1: Logarithmic Inequality with Base $< 1$
> **Problem**: Find the complete set of real values of $x$ satisfying $\log_{0.5}(x^2 - 5x + 6) \ge -1$.

- **First-Principles Method**:
  1. **Domain Condition (Argument $> 0$)**:
     $$x^2 - 5x + 6 > 0 \iff (x - 2)(x - 3) > 0 \implies x \in (-\infty, 2) \cup (3, \infty)$$
  2. **Inequality Unwrapping (Base $0.5 < 1 \implies$ Flip Sign!)**:
     $$x^2 - 5x + 6 \le (0.5)^{-1} = 2 \iff x^2 - 5x + 4 \le 0 \iff (x - 1)(x - 4) \le 0 \implies x \in [1, 4]$$
  3. **Intersection of Domain and Inequality**:
     $$[1, 4] \cap \big((-\infty, 2) \cup (3, \infty)\big) = \mathbf{[1, 2) \cup (3, 4]}$$

- **30-Second Exam-Hall Speed Shortcut**:
  - Combine into a single sandwich inequality in one step whenever Base $b \in (0, 1)$ and $\log_b(f(x)) \ge k$:
    $$0 < f(x) \le b^k \implies 0 < x^2 - 5x + 6 \le 2$$

---

### Archetype 2: Cauchy Functional Equation with Summation
> **Problem**: A function $f: \mathbb{Z}^+ \to \mathbb{R}$ satisfies $f(x + y) = f(x)f(y)$ for all positive integers $x, y$, and $f(1) = 3$. If $\sum_{k=1}^{n} f(a + k) = 3279 \times 27$, where $a$ is a positive integer and $n = 6$, find $a$.

- **First-Principles Method**:
  1. From $f(x+y) = f(x)f(y)$ and $f(1) = 3$, we have $f(m) = 3^m$.
  2. The sum is $\sum_{k=1}^{6} 3^{a+k} = 3^{a+1}(1 + 3 + 3^2 + \dots + 3^5) = 3^{a+1} \cdot \frac{3^6 - 1}{3 - 1} = 3^{a+1} \cdot \frac{728}{2} = 364 \times 3^{a+1}$.
  3.Wait: for $n = 7$, $\frac{3^7 - 1}{2} = \frac{2186}{2} = 1093$, and $3279 = 3 \times 1093$. So with $n = 7$:
     $$\sum_{k=1}^{7} f(a+k) = 3^{a+1} \times 1093 = 3279 \times 27 = 1093 \times 3^4 \implies 3^{a+1} = 3^4 \implies a = 3$$

- **30-Second Exam-Hall Speed Shortcut**:
  - Immediately replace $f(m)$ with $3^m$, factor out $3^{a+1}$, and match the power of $3$ on both sides!

---

### Archetype 3: Greatest Integer & Fractional Part Simultaneous Equation
> **Problem**: Find the number of real solutions to $2\lfloor x \rfloor = x + \{x\} + 3$.

- **First-Principles Method**:
  1. Write $x = \lfloor x \rfloor + \{x\}$, where $n = \lfloor x \rfloor \in \mathbb{Z}$ and $f = \{x\} \in [0, 1)$.
  2. Substitute into the equation:
     $$2n = (n + f) + f + 3 \implies n - 3 = 2f \implies f = \frac{n - 3}{2}$$
  3. Apply the strict fractional part domain $0 \le f < 1$:
     $$0 \le \frac{n - 3}{2} < 1 \iff 0 \le n - 3 < 2 \iff 3 \le n < 5$$
  4. Since $n \in \mathbb{Z}$, $n \in \{3, 4\}$:
     - $n = 3 \implies f = 0 \implies x = 3.0$
     - $n = 4 \implies f = 0.5 \implies x = 4.5$
  5. Total $= \mathbf{2\text{ real solutions}}$.

- **30-Second Exam-Hall Speed Shortcut**:
  - Always substitute $x = n + f$, isolate $f$ in terms of integer $n$, and bound $0 \le f < 1$ to count integers $n$ directly!

---

## 4. Boundary Conditions, Domain Traps & TITA Pitfalls

1. **Pulling Even Powers Out of Logs ($\log(x^2) = 2\log|x|$)**:
   - Writing $\log_2(x^2) = 2\log_2(x)$ artificially destroys negative roots ($x < 0$). Conversely, rewriting $2\log_2(x - 1)$ as $\log_2((x-1)^2)$ introduces extraneous roots where $x - 1 < 0$. Always write down the **original domain** before applying log laws!
2. **Variable Base in Logs ($\log_{x-1}(\dots)$)**:
   - Besides $x - 1 > 0$, you MUST enforce $x - 1 \neq 1 \implies x \neq 2$. CAT routinely plants an extraneous quadratic root at $x = 2$!
3. **De-nesting $\sqrt{x^2 - 6x + 9} = |x - 3|$, NOT $(x - 3)$**:
   - Whenever simplifying $\sqrt{A^2}$, wrap it in absolute value bars $|A|$ before testing intervals.
4. **Onto (Surjective) vs. All Functions**:
   - Number of onto functions from a 5-element set to a 2-element set is $2^5 - 2 = 30$, NOT $2^5 = 32$.

---

## 5. Active-Recall Drill (10 Prompts)

<details><summary>Q1: Solve for x: log_(x+1)(x^2 - 3x + 5) = 2.</summary>
A: (x + 1)^2 = x^2 - 3x + 5 -> x^2 + 2x + 1 = x^2 - 3x + 5 -> 5x = 4 -> x = 4/5 = 0.8. Check base: x + 1 = 1.8 (> 0 and != 1), argument = (1.8)^2 > 0. Valid: x = 0.8.
</details>

<details><summary>Q2: How many digits does 6^50 have in base 10? (Given log_10(2) = 0.30103, log_10(3) = 0.47712)</summary>
A: log_10(6^50) = 50 * (0.30103 + 0.47712) = 50 * 0.77815 = 38.9075. Number of digits = floor(38.9075) + 1 = 39 digits.
</details>

<details><summary>Q3: Simplify sqrt(11 - 6*sqrt(2)) + sqrt(7 + 4*sqrt(3)).</summary>
A: sqrt(11 - 2*sqrt(18)) = sqrt(9) - sqrt(2) = 3 - sqrt(2). sqrt(7 + 2*sqrt(12)) = sqrt(4) + sqrt(3) = 2 + sqrt(3). Sum = 5 - sqrt(2) + sqrt(3).
</details>

<details><summary>Q4: Find the sum of all integer solutions to (x^2 - 7x + 11)^(x^2 - 13x + 42) = 1.</summary>
A: Case 1 (Base = 1): x^2 - 7x + 10 = 0 -> x = 2, 5. Case 2 (Exp = 0): x^2 - 13x + 42 = 0 -> x = 6, 7 (base != 0 at both). Case 3 (Base = -1, Exp even): x^2 - 7x + 12 = 0 -> x = 3, 4; at x=3, exp = 12 (even); at x=4, exp = 6 (even). All 6 roots {2, 3, 4, 5, 6, 7} are valid! Sum = 27.
</details>

<details><summary>Q5: If f(x) * f(1/x) = f(x) + f(1/x) for all non-zero real x and f(3) = 28, find f(2).</summary>
A: Standard Cauchy form f(x) = 1 +/- x^n. Since f(3) = 1 + 3^3 = 28, f(x) = 1 + x^3. Therefore f(2) = 1 + 2^3 = 9.
</details>

<details><summary>Q6: Find the value of log_3(4) * log_4(5) * log_5(6) * ... * log_80(81).</summary>
A: Telescoping chain rule gives log_3(81) = log_3(3^4) = 4.
</details>

<details><summary>Q7: How many onto (surjective) functions exist from A = {1, 2, 3, 4} to B = {a, b, c}?</summary>
A: Using inclusion-exclusion: C(3,0)*3^4 - C(3,1)*2^4 + C(3,2)*1^4 = 81 - 3(16) + 3(1) = 81 - 48 + 3 = 36.
</details>

<details><summary>Q8: If f(x) = (x - 1)/(x + 1), find f^(2024)(3), where f^(n) denotes n-fold composition.</summary>
A: f^(1)(3) = 2/4 = 1/2; f^(2)(3) = (-1/2)/(3/2) = -1/3; f^(3)(3) = (-4/3)/(2/3) = -2; f^(4)(3) = (-3)/(-1) = 3. Period is 4! Since 2024 is divisible by 4, f^(2024)(3) = 3.
</details>

<details><summary>Q9: Evaluate floor(1/3) + floor(1/3 + 1/50) + floor(1/3 + 2/50) + ... + floor(1/3 + 49/50).</summary>
A: By Hermite's Identity with x = 1/3 and n = 50, the sum equals floor(50 * 1/3) = floor(16.66) = 16.
</details>

<details><summary>Q10: Solve for x: 9^x - 10 * 3^x + 9 = 0.</summary>
A: Let t = 3^x -> t^2 - 10t + 9 = 0 -> (t - 1)(t - 9) = 0 -> 3^x = 1 or 3^x = 9 -> x = 0 or x = 2.
</details>
