# QA Mistake Patterns, Domain Traps & TITA Edge-Case Compendium

Every year in CAT, 99%ilers lose 9 to 15 raw marks in Quantitative Ability not from lack of conceptual knowledge, but from **domain omissions, degenerate boundary cases, and TITA wording traps**. Review this compendium before every mock and before exam day.

---

## 1. Number Set & Domain Terminology Traps

| Exact Term in Question Stem | Mathematical Set | Critical Boundary Element | Classic Trap |
| :--- | :--- | :--- | :--- |
| **Natural Numbers / Positive Integers** | $\{1, 2, 3, \dots\}$ | Starts at **$1$** ($0$ is EXCLUDED!) | Including $0$ in Stars & Bars or factor pairs |
| **Whole Numbers / Non-Negative Integers** | $\{0, 1, 2, 3, \dots\}$ | Starts at **$0$** ($0$ is INCLUDED!) | Forgetting $x = 0$ is a valid solution |
| **Integers ($\mathbb{Z}$)** | $\{\dots, -2, -1, 0, 1, 2, \dots\}$ | Includes **Negatives & $0$** | Missing negative divisors when solving $(x-2)(y-3) = 6 \implies (-1)(-6), (-2)(-3)$ |
| **Non-Positive Integers** | $\{\dots, -3, -2, -1, 0\}$ | **$0$ is INCLUDED** ($0$ is neither positive nor negative!) | Treating "non-positive" as "negative" |
| **Prime Numbers** | $\{2, 3, 5, 7, 11, \dots\}$ | **$1$ is NOT prime**; **$2$ is the ONLY even prime** | Including $1$ as prime or forgetting $p = 2$ breaks odd-prime parity |
| **Rational Numbers ($\mathbb{Q}$)** | $\frac{p}{q}$ ($p, q \in \mathbb{Z}, q \neq 0$) | Includes $0$ and negative fractions | Assuming $\Delta \ge 0$ is enough for rational roots (must have $\Delta = \text{perfect square}$!) |
| **Real Numbers ($\mathbb{R}$)** | Continuous $(-\infty, \infty)$ | Non-integers allowed! | Assuming $x, y$ must be integers when maximizing $xy$ given $x + y = 10$ |

---

## 2. Algebraic & Functional Domain Traps

1. **Cancellation of Variable Factors ($A \cdot B = A \cdot C$)**:
   - **Trap**: Dividing both sides of $(x - 3)(x + 5) = 2(x - 3)$ by $(x - 3)$ loses the root $x = 3$.
   - **Fix**: Always factor as $(x - 3)(x + 3) = 0$.
2. **Cross-Multiplication in Inequalities ($\frac{f(x)}{g(x)} < k$)**:
   - **Trap**: Writing $f(x) < k \cdot g(x)$ assumes $g(x) > 0$ and loses or inverts the negative branch.
   - **Fix**: Bring $k$ to the LHS: $\frac{f(x) - k \cdot g(x)}{g(x)} < 0$ and apply Wavy Curve.
3. **Even-Multiplicity Roots in Wavy Curve**:
   - **Trap**: In $(x - 2)^2(x - 5) \le 0$, students write $x \le 5$ and forget that for strict $< 0$, $x = 2$ must be **excluded**, while for $(x - 2)^2(x - 5) \ge 0$, the solution is $[5, \infty) \cup \{2\}$ (missing the isolated point $x = 2$!).
4. **Degenerate Leading Coefficient ($a = 0$) in "Quadratic-Looking" Expressions**:
   - **Trap**: "Find all values of $k$ for which $(k-3)x^2 + 2(k-3)x + 4 > 0$ for all $x \in \mathbb{R}$." Applying only $a > 0, \Delta < 0$ misses $k = 3$ (which reduces the expression to $4 > 0$, always true!).
   - **Exception**: If the prompt explicitly says *"the **quadratic** equation $(k-3)x^2 + \dots = 0$"*, then $k \neq 3$ is required by the definition of quadratic.
5. **Squaring Both Sides ($\sqrt{f(x)} = g(x)$)**:
   - **Trap**: Squaring introduces extraneous roots where $g(x) < 0$.
   - **Fix**: Immediately impose $g(x) \ge 0$ before squaring, or plug every candidate root back into the original radical equation.
6. **Logarithm Triple-Check ($\log_{b(x)} a(x)$)**:
   - Every candidate root MUST satisfy: (i) $a(x) > 0$, (ii) $b(x) > 0$, and (iii) **$b(x) \neq 1$**.
   - When solving $\log_b f(x) < k$ for **$0 < b < 1$**, flip the inequality sign AND bound from below by zero: $0 < f(x) > b^k$ (for $\log_{0.5} f(x) > k \implies 0 < f(x) < 0.5^k$).
7. **AM-GM Equality & Positivity Trap**:
   - AM-GM applies ONLY when terms are strictly positive.
   - If the equality point $x^*$ falls **outside** the given domain (e.g., $\min(x + \frac{4}{x})$ for $x \ge 3$), the minimum occurs at the **boundary** $x = 3$, NOT at $2\sqrt{4} = 4$.

---

## 3. Arithmetic & Number System Traps

1. **Base Shift & Wording Traps**:
   - "Increased **by** $300\%$" $\implies \times 4$; "Increased **to** $300\%$" $\implies \times 3$.
   - "Profit of $25\%$ on Selling Price" $\implies \text{CP} = 0.75\,\text{SP} \implies$ Profit on CP is $33.33\%$.
   - "Final ratio of Milk to Water is $9:16$" $\implies$ Remaining Milk fraction is $\frac{9}{25}$, NOT $\frac{9}{16}$.
2. **Equal Ratio Property Zero-Denominator Case**:
   - If $\frac{a}{b+c} = \frac{b}{c+a} = \frac{c}{a+b} = k$, besides $k = \frac{1}{2}$ (when $a+b+c \neq 0$), always check $a+b+c = 0 \implies k = -1$.
3. **Circular Track Unreduced Ratio Trap**:
   - Number of distinct meeting points for speeds $v_1 = 20\text{ m/s}$ and $v_2 = 15\text{ m/s}$ requires reducing $20:15$ to **$4:3$** first ($4 - 3 = 1$ point in same direction, $4 + 3 = 7$ points in opposite direction).
4. **Remainder Cancellation Trap**:
   - When dividing $2^{50}$ by $48$, cancelling $16$ gives $2^{46} \div 3$ (remainder $1$). You MUST multiply that remainder by the cancelled factor $16$ to get the true remainder $16 \times 1 = 16$!

---

## 4. Geometry & Mensuration Traps

1. **Ambiguous Non-Scale Configurations**:
   - **Two parallel chords in a circle**: Can lie on the **same side** ($d = |d_1 - d_2|$) or **opposite sides** ($d = d_1 + d_2$) of the center.
   - **Altitude of a triangle**: Can fall **inside** (acute triangle, $a = p + q$) or **outside** (obtuse triangle, $a = |p - q|$) the base.
2. **Triangle Inequality Verification**:
   - After solving for unknown side $x$ using perimeter, area, or cosine rule, verify $|a - b| < x < a + b$.
3. **Secant Segment Length ($PA \cdot PB = PT^2$)**:
   - $PB$ is the **entire secant length from external point $P$ to the far intersection $B$** ($PA + AB$), NOT the internal chord length $AB$!

---

## 5. Pre-Submission TITA 5-Second Audit

Before clicking **Save & Next** on any QA TITA question:
1. Re-read the **last 6 words** of the question: Did it ask for $x$, $2x$, the *sum* of roots, the *number* of solutions, or the *percentage*?
2. Check **units**: $\text{km/hr}$ vs. $\text{m/s}$, hours vs. minutes, Rupees vs. thousands/lakhs.
3. Verify whether $0$, $1$, or negative integers should be included or excluded.
