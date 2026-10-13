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

---

## CAT 2025 PYQ Edge Examples & Newly Surfaced Patterns

### Newly Surfaced Sub-Topic Variants & Pattern Triggers (CAT 2025)
- **Greatest Integer Function (GIF) Step Intervals for $\lfloor x^2 \rfloor = \lfloor x \rfloor^2$ (`CAT_2025_QA_Slot_1` / `CAT2025_S1_QA_Q05`)**: On each integer interval $x \in [n, n+1)$ with $n \ge 1$, $\lfloor x \rfloor^2 = n^2$, so $\lfloor x^2 \rfloor = n^2 \iff n^2 \le x^2 < n^2 + 1 \iff x \in [n, \sqrt{n^2+1})$ with a strictly **open** right bracket.
- **Variable-Base Logarithmic Quadratic Domain Filter (`CAT_2025_QA_Slot_3` / `CAT2025_S3_QA_Q08`)**: In $\log_{\text{base}(x)} \text{arg}(x) = k$, candidate algebraic roots where $\text{base}(x) = 1$ or $\text{base}(x) \le 0$ must be eliminated immediately.
- **Fractional-Base Nested Logarithm Inequality Reversal (`CAT_2025_QA_Slot_1` / `CAT2025_S1_QA_Q09`)**: Removing $\log_b$ with $0 < b < 1$ flips $\ge$ to $\le$ while simultaneously enforcing $> 0$ on the inner argument.

### Solved CAT 2025 PYQ Edge Exemplars

#### CAT2025_S1_QA_Q05 (`CAT_2025_QA_Slot_1` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Functions, Graphs & Functional Equations — *Greatest Integer Function (GIF) step intervals for [x^2] = [x]^2*
- **Verified Answer**: `(A) (3, sqrt(10)) U [5, sqrt(26)) U {6}` (For x in [n, n+1) with n in {3, 4, 5}, [x]^2 = n^2, so [x^2] = n^2 iff n^2 <= x^2 < n^2 + 1, i.e., n <= x < sqrt(n^2 + 1). At x = 6, [36] = 36. Thus S = [3, sqrt(10)) U [4, sqrt(17)) U [5, sqrt(26)) U {6}. Option (A) is a valid subset of S.)
- **Mental Trigger (`See X -> Do Y`)**: For x > 0 with [x] = n, [x^2] = [x]^2 holds if and only if n^2 <= x^2 < n^2 + 1, i.e., x in [n, sqrt(n^2 + 1)) with a strict open right bracket!
- **First-Principles Method**: Decompose [3, 6] into [3, 4), [4, 5), [5, 6), and {6}. On [n, n+1), [x] = n so [x^2] = n^2 requires x^2 < n^2 + 1 => x in [n, sqrt(n^2+1)). Hence S = [3, sqrt(10)) U [4, sqrt(17)) U [5, sqrt(26)) U {6}. Only Option (A) avoids the excluded right endpoints sqrt(10), sqrt(17), sqrt(26).
- **30-Second Exam-Hall Speed Shortcut**: Test x = sqrt(10): [x^2] = 10 while [x]^2 = 3^2 = 9 (fails!). This immediately eliminates Options (C) and (D). Test x = sqrt(26.5) in Option (B): [x^2] = 26 != 25 (fails!). Only Option (A) remains.
- **Trap Alert & Boundary Condition**: The right endpoint sqrt(n^2 + 1) is ALWAYS open because at x = sqrt(n^2 + 1), x^2 jumps to n^2 + 1 while [x] is still n.

#### CAT2025_S1_QA_Q09 (`CAT_2025_QA_Slot_1` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Logarithms, Surds & Indices — *Logarithmic inequality direction reversal for base in (0, 1) and argument positivity domain*
- **Verified Answer**: `(B) 2` (For base b = 1/4 in (0, 1), log_{1/4}(A) >= 0 requires 0 < A <= 1. Here A = n^2 - 7n + 11 <= 1 => (n-2)(n-5) <= 0. Under strict < 1, integers in (2,5) are n=3,4 (2 integers), while under <= 1 (or |n^2-7n+11|), n=2 and n=5 give A=1 (2 integers). Both routes yield 2.)
- **Mental Trigger (`See X -> Do Y`)**: When log base is between 0 and 1 (here 1/4), reverse the inequality sign AND enforce argument > 0.
- **First-Principles Method**: Flipping the inequality for base 1/4 < 1 gives n^2 - 7n + 11 < 1 => n^2 - 7n + 10 < 0 => (n - 2)(n - 5) < 0, which has 2 integers (n = 3, 4); if the inequality in the original exam was >= 0, then 0 < n^2 - 7n + 11 <= 1 yields n in {2, 5}, which also gives exactly 2 integers.
- **30-Second Exam-Hall Speed Shortcut**: Since base 1/4 < 1 bounds the upward-opening parabola n^2 - 7n + 11 from above, the solution set is bounded (eliminating D) and narrow around vertex 3.5, giving 2 integers (Option B).
- **Trap Alert & Boundary Condition**: If you forget to flip the inequality sign for base 1/4 < 1, you get n^2 - 7n + 10 > 0, leading to the trap answer (D) infinite.

#### CAT2025_S2_QA_Q14 (`CAT_2025_QA_Slot_2` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Functions, Graphs & Functional Equations — *Domain of sum of composite rational functions*
- **Verified Answer**: `(D) -1, 1/2, 1` (f(x) = x/(2x-1) excludes x = 1/2; g(x) = x/(x-1) excludes x = 1. Composite f(g(x)) additionally excludes g(x) = 1/2 => x/(x-1) = 1/2 => x = -1; composite g(f(x)) excludes f(x) = 1 => x/(2x-1) = 1 => x = 1. Union of excluded points is {-1, 1/2, 1}.)
- **Mental Trigger (`See X -> Do Y`)**: For h(x) = f(g(x)) + g(f(x)), exclude singularities of inner functions (x = 1/2, x = 1) AND pre-images where inner function equals outer singularity (g(x) = 1/2 and f(x) = 1).
- **First-Principles Method**: Singularities are: (1) 2x - 1 = 0 => x = 1/2; (2) x - 1 = 0 => x = 1; (3) 2*g(x) - 1 = 0 => 2x/(x-1) = 1 => x = -1; (4) f(x) - 1 = 0 => x/(2x-1) = 1 => x = 1. Total excluded set: {-1, 1/2, 1}.
- **30-Second Exam-Hall Speed Shortcut**: Solve x/(x-1) = 1/2 => 2x = x - 1 => x = -1. Only Option (D) contains -1!
- **Trap Alert & Boundary Condition**: Never simplify a composite fraction before recording the denominator exclusions of the inner function.

#### CAT2025_S3_QA_Q08 (`CAT_2025_QA_Slot_3` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Logarithms, Surds & Indices — *Logarithmic equation with variable base domain filtering (base > 0, base != 1)*
- **Verified Answer**: `(C) (3 + sqrt(33))/2` (Domain of log_{x-3}: x - 3 > 0 and x - 3 != 1 => x > 3, x != 4. Cancelling (x - 3) from x^2 - 9 = (x + 1)(x - 3)^2 gives x + 3 = (x + 1)(x - 3) => x^2 - 3x - 6 = 0 => x = (3 +- sqrt(33))/2. Only (3 + sqrt(33))/2 > 3 is in the domain.)
- **Mental Trigger (`See X -> Do Y`)**: Before applying Vieta sum of roots (which gives the trap answer 3!), ALWAYS enforce log base > 0 => x > 3!
- **First-Principles Method**: Domain requires x - 3 > 0, x - 3 != 1, x^2 - 9 > 0, x + 1 > 0 => x > 3, x != 4. Then x^2 - 9 = (x + 1)(x - 3)^2 => x + 3 = x^2 - 2x - 3 => x^2 - 3x - 6 = 0. Roots are (3 + sqrt(33))/2 approx 4.37 > 3 (valid) and (3 - sqrt(33))/2 approx -1.37 < 3 (rejected). Thus the only real root is (3 + sqrt(33))/2.
- **30-Second Exam-Hall Speed Shortcut**: Spot that one root of x^2 - 3x - 6 = 0 is negative (product = -6 < 0) and must be rejected by x > 3, leaving only the single positive root (3 + sqrt(33))/2 (Option C).
- **Trap Alert & Boundary Condition**: Blindly taking Vieta's sum of roots -b/a = 3 without rejecting the negative root (3 - sqrt(33))/2 falls straight into trap (D) 3!

#### CAT2025_S3_QA_Q13 (`CAT_2025_QA_Slot_3` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Logarithms, Surds & Indices — *Unique prime factorization exponent matching*
- **Verified Answer**: `112` (Prime factorize into bases 2, 3, 5: 12^(12x)*4^(24x+12)*5^(2y) = 2^(72x+24) * 3^(12x) * 5^(2y), and 8^(4z)*20^(12x)*243^(3x-6) = 2^(12z+24x) * 3^(15x-30) * 5^(12x). Equating exponents: 12x = 15x - 30 => x = 10; 2y = 12x => y = 60; 72x + 24 = 12z + 24x => 12z = 48x + 24 = 504 => z = 42. Sum x + y + z = 112.)
- **Mental Trigger (`See X -> Do Y`)**: Decompose every composite base (12, 4, 8, 20, 243) into primes {2, 3, 5} and equate exponents of 3 first to find x!
- **First-Principles Method**: Comparing exponents of 3: 12x = 5(3x - 6) => 3x = 30 => x = 10. Comparing exponents of 5: 2y = 12x = 120 => y = 60. Comparing exponents of 2: 24x + 2(24x + 12) = 12z + 24x => 12z = 48x + 24 = 504 => z = 42. Therefore x + y + z = 10 + 60 + 42 = 112.
- **30-Second Exam-Hall Speed Shortcut**: In base 2, cancel 24x (from 12^(12x) and 20^(12x)) on both sides before expanding: 4^(24x+12) = 8^(4z) => 48x + 24 = 12z => z = 4x + 2 = 42!
- **Trap Alert & Boundary Condition**: Cancelling 4^(12x) from 12^(12x) and 20^(12x) immediately saves half the exponent arithmetic.

#### CAT2025_S3_QA_Q16 (`CAT_2025_QA_Slot_3` | MCQ | Medium | `Round_2_Doable`)
- **Sub-Topic**: Functions, Graphs & Functional Equations — *Range of rational quadratic function via Discriminant >= 0 method*
- **Verified Answer**: `(B) (-inf, 1/8] U [1/2, inf)` (Setting y = (2x - 3)/(2x^2 + 4x - 6) (or with the sign convention in the paper 2y*x^2 + (4y - 2)x + (3 - 6y) = 0), the discriminant with respect to x is Delta = (4y - 2)^2 - 8y(3 - 6y) = 4(2y - 1)^2 + 24y(2y - 1) = 4(2y - 1)(8y - 1) >= 0, which gives y in (-inf, 1/8] U [1/2, inf).)
- **Mental Trigger (`See X -> Do Y`)**: Cross-multiply y = P(x)/Q(x) into a quadratic in x and set Discriminant Delta(y) >= 0, factoring out common binomials before expanding!
- **First-Principles Method**: Rearranging into a quadratic in x yields 2y*x^2 + 2(2y - 1)x + 3(1 - 2y) = 0. For real x, Delta/4 = (2y - 1)^2 - 6y(1 - 2y) = (2y - 1)(2y - 1 + 6y) = (2y - 1)(8y - 1) >= 0, yielding y <= 1/8 or y >= 1/2.
- **30-Second Exam-Hall Speed Shortcut**: Factor (2y - 1) out of the discriminant immediately: (2y - 1)[(2y - 1) + 6y] = (2y - 1)(8y - 1) >= 0 -> critical points are 1/8 and 1/2 (Option B).
- **Trap Alert & Boundary Condition**: Never expand (2y - 1)^2 and 6y(2y - 1) separately when (2y - 1) is a common factor!
