# QA 04 Concept & Formula Examples: Linear & Diophantine Equations, Polynomials, Inequalities & Modulus

> **Companion Reference**: [`../topic_summaries/quant/04_algebra_equations_polynomials_inequalities_modulus.md`](../topic_summaries/quant/04_algebra_equations_polynomials_inequalities_modulus.md) | [`QA_Formula_and_Trigger_Book.md`](../high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md)

Every concept, formula, and pattern trigger from **QA 04** is explained below with plain-English intuition, clean single-concept numbers, a two-way walkthrough (direct formula vs. mental ratio intuition), and the #1 mistake to avoid.

---

## Concept 1: Consistency of 2-Variable Linear Systems & Indeterminate Block Substitution

### 1. Concept & Formula in Plain English
Two linear equations $a_1 x + b_1 y = c_1$ and $a_2 x + b_2 y = c_2$ represent two straight lines in a plane:
- **Unique Solution** (lines cross at 1 point, different slopes): $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$
- **No Solution** (parallel lines, same slope, different intercepts): $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$
- **Infinitely Many Solutions** (the exact same line scaled): $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$

**Block Variable Trigger**: When given $2$ equations in $3$ variables $(a, b, c)$ and asked for a specific combination, check if the coefficients of two variables stay in the same ratio (or set one free variable $c = 0$).

### 2. When to Use It (Question Cue)
- *"For what value of $k$ does the system $kx + 3y = k - 3$ and $12x + ky = k$ have no solution?"*
- *"If $2a + 3b - 3c = 10$ and $a - 6b + 6c = 2$, find $a + b - c$."*

### 3. General Example (Clean Numbers, Single Concept)
> Find the value of $k$ for which the pair of equations $kx + 2y = 5$ and $3x + y = 1$ has **no solution**.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Apply the No-Solution condition $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$:
     $$\frac{k}{3} = \frac{2}{1} \neq \frac{5}{1}$$
  2. From $\frac{k}{3} = 2$, we get $k = \mathbf{6}$ (and clearly $2 \neq 5$, so the lines are parallel and distinct).
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Double the second equation ($3x + y = 1$) to match the $2y$ in the first equation: $6x + 2y = 2$.
  2. If $k = 6$, the first equation asks for $6x + 2y = 5$ while the second says $6x + 2y = 2$—impossible! So $k = \mathbf{6}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Solving $\frac{a_1}{a_2} = \frac{b_1}{b_2}$ (e.g., $k^2 = 36 \implies k = \pm 6$) and forgetting to **reject** the root where $\frac{b_1}{b_2} = \frac{c_1}{c_2}$ (which gives *infinitely many* solutions, not *no* solution).

---

## Concept 2: Linear Diophantine Equations ($ax + by = c$) & Step-Shifting

### 1. Concept & Formula in Plain English
When $x$ and $y$ must be integers (e.g., number of pens and notebooks) in $ax + by = c$ with $\gcd(a, b) = 1$, you only need to find **one** starting solution $(x_0, y_0)$ by inspection. After that, to keep the total sum $c$ unchanged, every time $x$ increases by $b$, $y$ must decrease by $a$:
$$x = x_0 + k \cdot b, \qquad y = y_0 - k \cdot a \quad (k \in \mathbb{Z})$$

### 2. When to Use It (Question Cue)
- *"How many positive (or non-negative) integer pairs $(x, y)$ satisfy $3x + 5y = 47$?"*

### 3. General Example (Clean Numbers, Single Concept)
> How many pairs of **positive integers** $(x, y)$ satisfy the equation $3x + 5y = 47$?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Test small $y \ge 1$ until $47 - 5y$ is a multiple of $3$:
     - $y = 1 \implies 3x = 42 \implies x = 14$. Starting solution: $(x_0, y_0) = (14, 1)$.
  2. Shift $x$ down by steps of $b = 5$ and $y$ up by steps of $a = 3$:
     - $k = 0: (14, 1)$
     - $k = 1: (14 - 5,\; 1 + 3) = (9, 4)$
     - $k = 2: (9 - 5,\; 4 + 3) = (4, 7)$
     - Next step gives $x = 4 - 5 = -1$ (not positive).
  3. Total valid pairs $= \mathbf{3\text{ pairs}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Notice $3x = 47 - 5y$. Look at remainders when divided by $3$: $47 \equiv 2 \pmod 3$, so $5y \equiv 2 \pmod 3 \implies y \in \{1, 4, 7, 10, \dots\}$.
  2. Since $5y < 47$ (so $x > 0$), $y$ can be at most $9$. Thus $y \in \{1, 4, 7\} \implies \mathbf{3\text{ solutions}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Mixing up **"positive integers"** ($x, y \ge 1$) with **"non-negative integers"** ($x, y \ge 0$, which allows $x = 0$ or $y = 0$).

---

## Concept 3: Frobenius Coin / Postage Stamp Theorem

### 1. Concept & Formula in Plain English
If you have an unlimited supply of two coprime coin denominations $a$ and $b$ ($\gcd(a, b) = 1$):
- **Non-negative coins ($x, y \ge 0$)**: The largest amount you **cannot** pay is $ab - a - b$, and the total number of unpayable positive amounts is $\frac{(a-1)(b-1)}{2}$.
- **At least one of each coin ($x, y \ge 1$)**: The largest amount you **cannot** form is $ab$.

### 2. When to Use It (Question Cue)
- *"A shop has only Rs. $5$ and Rs. $7$ stamps. What is the largest postage amount that cannot be formed?"*

### 3. General Example (Clean Numbers, Single Concept)
> An ATM dispenses only $5$-dollar and $7$-dollar tokens. What is the largest integer dollar amount that **cannot** be dispensed, and how many positive integer amounts cannot be dispensed?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $a = 5$ and $b = 7$ ($\gcd(5, 7) = 1$, and $x, y \ge 0$ since 0 tokens of one type is allowed).
  2. Largest unattainable amount $= ab - a - b = 5(7) - 5 - 7 = 35 - 12 = \mathbf{23}$.
  3. Count of unattainable amounts $= \frac{(a - 1)(b - 1)}{2} = \frac{4 \times 6}{2} = \mathbf{12\text{ amounts}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Group numbers by their remainder modulo $5$. Using $7$s, the smallest multiples we can reach for each remainder $\pmod 5$ are:
     - $0 \pmod 5$: $0$
     - $2 \pmod 5$: $7$
     - $4 \pmod 5$: $14$
     - $1 \pmod 5$: $21$
     - $3 \pmod 5$: $28$ (so the last unreachable $3 \pmod 5$ number is $28 - 5 = \mathbf{23}$!).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using $ab - a - b$ when the question states you must use **at least one** of each denomination ($x, y \ge 1 \implies \text{max unattainable is } ab = 35$).

---

## Concept 4: Simon's Favorite Factoring Trick ($xy + ax + by = c$)

### 1. Concept & Formula in Plain English
Whenever an integer equation has a product term $xy$ plus linear terms $ax + by = c$, you can factor the left side into a clean rectangle by adding $ab$ to both sides:
$$xy + ax + by = c \iff xy + ax + by + ab = c + ab \iff (x + b)(y + a) = c + ab$$
Then simply list the factor pairs of the number $(c + ab)$!

### 2. When to Use It (Question Cue)
- *"How many positive integer pairs $(x, y)$ (or integer pairs) satisfy $xy + 2x + 3y = 18$?"*

### 3. General Example (Clean Numbers, Single Concept)
> Find all ordered pairs of **positive integers** $(x, y)$ that satisfy $xy + 2x + 3y = 18$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $a = 2, b = 3, c = 18$. Add $ab = 2 \times 3 = 6$ to both sides:
     $$xy + 2x + 3y + 6 = 18 + 6 \implies (x + 3)(y + 2) = 24$$
  2. Since $x \ge 1$ and $y \ge 1$, we need $x + 3 \ge 4$ and $y + 2 \ge 3$.
  3. List factor pairs of $24$ where first factor $\ge 4$ and second factor $\ge 3$:
     - $(4, 6) \implies x = 1, y = 4$
     - $(6, 4) \implies x = 3, y = 2$
     - $(8, 3) \implies x = 5, y = 1$
  4. Total $= \mathbf{3\text{ positive integer pairs}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Isolate $x$: $x(y + 2) = 18 - 3y \implies x = \frac{18 - 3y}{y + 2}$.
  2. Plug $y = 1, 2, 3, 4$: $y=1 \to x=5$; $y=2 \to x=3$; $y=3 \to x=9/5$ (no); $y=4 \to x=1$; $y \ge 5 \to x \le 0$. Same $\mathbf{3\text{ pairs}}$!

### 5. The 1 Common Mistake to Avoid
- **Trap**: If the question says **$x, y$ are integers** (not *positive* integers), do NOT stop at positive divisors of $24$—you must also test negative divisor pairs like $(-1, -24), (-2, -12), \dots$!

---

## Concept 5: Vieta's Root-Coefficient Relations, Power Sums & Reciprocal Newton Recurrence

### 1. Concept & Formula in Plain English
For a quadratic $ax^2 + bx + c = 0$ with roots $\alpha, \beta$:
$$S = \alpha + \beta = -\frac{b}{a}, \qquad P = \alpha\beta = \frac{c}{a}$$
From $S$ and $P$ alone, you can find any symmetric power sum without finding the roots:
- $\alpha^2 + \beta^2 = S^2 - 2P$
- $|\alpha - \beta| = \sqrt{S^2 - 4P}$
- $\alpha^3 + \beta^3 = S^3 - 3SP$
- **Reciprocal Power Sums ($S_n = x^n + \frac{1}{x^n}$ given $S_1 = x + \frac{1}{x} = k$)**:
  $$S_2 = k^2 - 2, \quad S_3 = k^3 - 3k, \quad S_{m+n} = S_m S_n - S_{|m-n|} \quad (\text{e.g., } S_7 = S_4 S_3 - S_1)$$

### 2. When to Use It (Question Cue)
- *"If $\alpha, \beta$ are roots of $2x^2 - 6x + 3 = 0$, find $\alpha^2 + \beta^2$ and $\alpha^3 + \beta^3$."*
- *"If $x + \frac{1}{x} = 3$, find $x^5 + \frac{1}{x^5}$."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) If $\alpha$ and $\beta$ are the roots of $x^2 - 5x + 3 = 0$, find $\alpha^2 + \beta^2$ and $\alpha^3 + \beta^3$.
> (b) If $x + \frac{1}{x} = 3$, find $x^5 + \frac{1}{x^5}$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: $S = 5, P = 3$.
     - $\alpha^2 + \beta^2 = S^2 - 2P = 5^2 - 2(3) = \mathbf{19}$.
     - $\alpha^3 + \beta^3 = S^3 - 3SP = 5^3 - 3(5)(3) = 125 - 45 = \mathbf{80}$.
  2. **Part (b)**: Here $S_1 = 3$.
     - $S_2 = 3^2 - 2 = 7$.
     - $S_3 = 3^3 - 3(3) = 18$.
     - $S_5 = S_3 S_2 - S_1 = (18)(7) - 3 = 126 - 3 = \mathbf{123}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Multiply $\left(x^2 + \frac{1}{x^2}\right)\left(x^3 + \frac{1}{x^3}\right) = x^5 + \frac{1}{x^5} + \left(x + \frac{1}{x}\right)$, so $7 \times 18 = S_5 + 3 \implies S_5 = \mathbf{123}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Assuming $S_5 = S_2 \times S_3 = 7 \times 18 = 126$ and forgetting to subtract the cross-term $S_{3-2} = S_1 = 3$.

---

## Concept 6: Quadratic Constant-Sign Condition ($ax^2 + bx + c > 0$) & Degenerate $a = 0$ Check

### 1. Concept & Formula in Plain English
A parabola $y = ax^2 + bx + c$ stays strictly **above the x-axis** for all real $x$ ($ax^2 + bx + c > 0 \;\forall x \in \mathbb{R}$) if and only if:
1. It opens upward: **$a > 0$**, AND
2. It never touches or crosses the x-axis (no real roots): **$\Delta = b^2 - 4ac < 0$**.
**Degenerate Check**: If the leading coefficient contains a parameter (like $(m - 2)x^2 + \dots$) and the question does not force it to be quadratic, also test whether $a = 0$ leaves a true constant inequality!

### 2. When to Use It (Question Cue)
- *"Find the values of $k$ for which $x^2 - (k - 2)x + 9 > 0$ for all real values of $x$."*

### 3. General Example (Clean Numbers, Single Concept)
> For what range of real values of $k$ is the expression $x^2 - kx + 9$ strictly positive ($> 0$) for all real $x$?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Leading coefficient $a = 1 > 0$ (already satisfied).
  2. Enforce $\Delta = b^2 - 4ac < 0$:
     $$(-k)^2 - 4(1)(9) < 0 \implies k^2 - 36 < 0 \implies (k - 6)(k + 6) < 0 \implies \mathbf{k \in (-6, 6)}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Complete the square: $x^2 - kx + 9 = \left(x - \frac{k}{2}\right)^2 + \left(9 - \frac{k^2}{4}\right)$.
  2. The minimum value occurs at the vertex $x = \frac{k}{2}$, where the value is $9 - \frac{k^2}{4}$. For this minimum to be $> 0$, we need $\frac{k^2}{4} < 9 \implies \mathbf{-6 < k < 6}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using $\Delta > 0$ instead of $\Delta < 0$ ("always positive" means the graph **never crosses the x-axis**, so it has **no real roots**, $\Delta < 0$!).

---

## Concept 7: Location of Roots Relative to a Number $k$ ($a \cdot f(k) < 0$)

### 1. Concept & Formula in Plain English
When does a number $k$ lie strictly **between** the two roots $\alpha$ and $\beta$ of $f(x) = ax^2 + bx + c = 0$ ($\alpha < k < \beta$)?
Think of the parabola: if it opens upward ($a > 0$), the only part of the curve that dips **below** the x-axis ($f(x) < 0$) is the valley strictly between the two roots! Thus one single inequality guarantees both real roots and $\alpha < k < \beta$:
$$a \cdot f(k) < 0$$

### 2. When to Use It (Question Cue)
- *"For what values of $m$ does $x^2 - mx + 3 = 0$ have one root smaller than $2$ and the other root greater than $2$?"*

### 3. General Example (Clean Numbers, Single Concept)
> Find the set of values of $m$ for which the quadratic equation $x^2 - mx + 3 = 0$ has one root strictly less than $2$ and the other root strictly greater than $2$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $a = 1 > 0$ and the separator number is $k = 2$.
  2. Apply $a \cdot f(2) < 0$:
     $$1 \cdot (2^2 - m(2) + 3) < 0 \implies 7 - 2m < 0 \implies \mathbf{m > 3.5}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. At the boundary where $x = 2$ is itself a root, $2^2 - 2m + 3 = 0 \implies m = 3.5$ (roots are $2$ and $1.5$).
  2. Increasing $m$ (say $m = 4$) spreads the roots apart ($x^2 - 4x + 3 = 0 \implies$ roots $1$ and $3$, which straddle $2$!). Thus $\mathbf{m > 3.5}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Wasting time also solving $\Delta = m^2 - 12 > 0$—whenever $a \cdot f(k) < 0$ holds, the parabola is already opposite in sign to $a$ at $x = k$, which *automatically* guarantees $\Delta > 0$!

---

## Concept 8: Polynomial Remainder & Factor Theorems + Coefficient Sums

### 1. Concept & Formula in Plain English
- **Remainder Theorem**: When any polynomial $P(x)$ is divided by $(x - a)$, the remainder is simply $P(a)$.
- **Quadratic Divisor $(x - a)(x - b)$**: Since the divisor has degree $2$, the remainder is a linear expression $R(x) = px + q$. Just plug $x = a$ and $x = b$ into $P(a) = pa + q$ and $P(b) = pb + q$!
- **Coefficient Sums**:
  - Sum of all coefficients $= P(1)$
  - Constant term $= P(0)$
  - Sum of even-power coefficients $= \frac{P(1) + P(-1)}{2}$
  - Sum of odd-power coefficients $= \frac{P(1) - P(-1)}{2}$

### 2. When to Use It (Question Cue)
- *"A polynomial $P(x)$ leaves remainder $4$ when divided by $(x - 1)$ and remainder $10$ when divided by $(x - 3)$. Find the remainder when $P(x)$ is divided by $(x - 1)(x - 3)$."*

### 3. General Example (Clean Numbers, Single Concept)
> A polynomial $P(x)$ leaves a remainder of $4$ when divided by $(x - 1)$ and a remainder of $10$ when divided by $(x - 3)$. Find the remainder when $P(x)$ is divided by $(x - 1)(x - 3)$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Write $P(x) = Q(x)(x - 1)(x - 3) + (px + q)$.
  2. Plug in $x = 1$: $P(1) = p(1) + q = 4$.
  3. Plug in $x = 3$: $P(3) = 3p + q = 10$.
  4. Subtract: $2p = 6 \implies p = 3$ and $q = 4 - 3 = 1$. Remainder is $\mathbf{3x + 1}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. We just need a straight line $y = px + q$ passing through $(1, 4)$ and $(3, 10)$.
  2. Slope $p = \frac{10 - 4}{3 - 1} = 3$, so the line is $3(x - 1) + 4 = \mathbf{3x + 1}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Assuming the remainder when dividing by a quadratic $(x-1)(x-3)$ is a single constant number $c$ instead of a linear expression $px + q$.

---

## Concept 9: Wavy Curve Method of Intervals (Odd vs. Even Multiplicity)

### 1. Concept & Formula in Plain English
To solve a factored rational inequality like $\frac{(x - a)^2 (x - b)^3}{x - c} \le 0$:
1. Make sure every factor starts with $+x$.
2. Mark all roots on the number line; to the right of the largest root, the sign is $+$.
3. Moving left across each root:
   - **Odd exponent** $(1, 3, 5, \dots) \implies$ Sign **flips** ($+ \leftrightarrow -$).
   - **Even exponent** $(2, 4, 6, \dots) \implies$ Sign **bounces (stays the same)**!
4. **Sticky-Note Guard**: Never include denominator roots (division by zero!), and for $\le 0$ or $\ge 0$, manually include numerator even-power roots even if they sit in a wrong-sign interval!

### 2. When to Use It (Question Cue)
- *"How many integer values of $x$ satisfy $\frac{(x - 2)^2 (x - 5)}{x + 1} \le 0$?"*

### 3. General Example (Clean Numbers, Single Concept)
> Find all integer values of $x$ that satisfy $\frac{(x - 2)^2 (x - 5)}{x + 1} \le 0$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in (Wavy Curve)**:
  1. Domain exclusion: $x \neq -1$ (denominator).
  2. Critical points in order: $-1$ (odd power $1$), $2$ (even power $2$), $5$ (odd power $1$).
  3. Sign from right to left:
     - $(5, \infty)$: $+$
     - $(2, 5)$: $-$ (flipped across odd root $5$)
     - $(-1, 2)$: $-$ (stayed $-$ across even root $2$)
     - $(-\infty, -1)$: $+$ (flipped across odd root $-1$)
  4. For $\le 0$, take the $-$ intervals plus numerator zeros $\{2, 5\}$ and exclude $\{-1\}$: $x \in (-1, 5]$.
  5. Integers in $(-1, 5]$: $\{0, 1, 2, 3, 4, 5\} \implies \mathbf{6\text{ integers}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Since $(x - 2)^2 \ge 0$ everywhere, $x = 2$ automatically satisfies $\le 0$ (gives $0 \le 0$).
  2. For $x \neq 2$, divide out $(x - 2)^2 > 0$: we just need $\frac{x - 5}{x + 1} \le 0$, which holds between $-1$ and $5$ ($-1 < x \le 5$).
  3. Combining gives $(-1, 5] \implies \{0, 1, 2, 3, 4, 5\}$ ($\mathbf{6\text{ integers}}$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: If the inequality is **strict** ($\frac{(x - 2)^2 (x - 5)}{x + 1} < 0$), $x = 2$ makes the numerator $0$ (which is NOT $< 0$), so you must **remove $x = 2$** from $(-1, 5)$, leaving only $5$ integers!

---

## Concept 10: Modulus Triangle Inequalities & Equality Conditions

### 1. Concept & Formula in Plain English
Normally, $|A| + |B| \ge |A + B|$. When are they **exactly equal**?
- $|A| + |B| = |A + B|$ holds if and only if $A$ and $B$ never fight each other in sign—meaning they have the **same sign (or one is zero)**:
  $$|A| + |B| = |A + B| \iff A \cdot B \ge 0$$
- Similarly, $|A| + |B| = |A - B|$ holds if and only if $A$ and $B$ have **opposite signs (or one is zero)**:
  $$|A| + |B| = |A - B| \iff A \cdot B \le 0$$

### 2. When to Use It (Question Cue)
- *"Find the set of values of $x$ satisfying $|x - 2| + |x - 5| = |2x - 7|$."*

### 3. General Example (Clean Numbers, Single Concept)
> Solve for real $x$: $|x - 2| + |x - 5| = |2x - 7|$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Notice that $(x - 2) + (x - 5) = 2x - 7$, so the equation has the exact form $|A| + |B| = |A + B|$ with $A = x - 2$ and $B = x - 5$.
  2. Apply the identity $A \cdot B \ge 0$:
     $$(x - 2)(x - 5) \ge 0 \implies \mathbf{x \in (-\infty, 2] \cup [5, \infty)}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Test a point between $2$ and $5$, say $x = 3$: LHS $= |1| + |-2| = 3$, while RHS $= |-1| = 1$ ($3 \neq 1$, fails!).
  2. Outside $(2, 5)$, both $(x-2)$ and $(x-5)$ are either both positive ($x \ge 5$) or both negative ($x \le 2$), so their absolute values add up without cancellation!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using strict $> 0$ instead of $\ge 0$ and losing the boundary roots $x = 2$ and $x = 5$ where one term is $0$.

---

## Concept 11: Sum of Absolute Deviations ($\sum |x - a_i|$) — Median Minimization Rule

### 1. Concept & Formula in Plain English
Think of $|x - a_1| + |x - a_2| + \dots + |x - a_n|$ as the total walking distance from a meeting point $x$ to $n$ houses located at $a_1 \le a_2 \le \dots \le a_n$ on a straight street.
- To minimize total distance, place $x$ at the **Median (middle house)**:
  - **Odd number of points ($n = 2m + 1$)**: Unique minimum at the middle point $x = a_{m+1}$.
  - **Even number of points ($n = 2m$)**: Any $x$ in the middle interval $[a_m, a_{m+1}]$ gives the exact same minimum value!
- **Minimum Value**: Pair the outermost houses inward: $(a_n - a_1) + (a_{n-1} - a_2) + \dots$.

### 2. When to Use It (Question Cue)
- *"Find the minimum value of $|x - 1| + |x - 3| + |x - 6| + |x - 10|$ and the integer values of $x$ where the minimum is attained."*

### 3. General Example (Clean Numbers, Single Concept)
> Find the minimum value of $f(x) = |x - 1| + |x - 3| + |x - 6| + |x - 10|$, and state how many integer values of $x$ achieve this minimum.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Sorted points: $a_1 = 1,\; a_2 = 3,\; a_3 = 6,\; a_4 = 10$ ($n = 4$, even).
  2. Minimum occurs for all $x \in [a_2, a_3] = [3, 6]$, which contains $6 - 3 + 1 = \mathbf{4\text{ integers}}$ ($\{3, 4, 5, 6\}$).
  3. Minimum value $= (a_4 - a_1) + (a_3 - a_2) = (10 - 1) + (6 - 3) = 9 + 3 = \mathbf{12}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. For any $x$ between $1$ and $10$, the distance to $1$ plus the distance to $10$ is always $10 - 1 = 9$.
  2. For any $x$ also between $3$ and $6$, the distance to $3$ plus the distance to $6$ is always $6 - 3 = 3$.
  3. Total minimum distance $= 9 + 3 = \mathbf{12}$ everywhere on $[3, 6]$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Thinking the minimum occurs at the **mean** ($\frac{1+3+6+10}{4} = 5$ only) instead of the entire **median plateau** $[3, 6]$.

---

## Concept 12: Diamond / Rhombus Region ($|x - h| + |y - k| \le r$) Area & Lattice Points

### 1. Concept & Formula in Plain English
The graph of $|x - h| + |y - k| = r$ is a **diamond (rotated square)** centered at $(h, k)$ with vertices $r$ units Left, Right, Up, and Down:
- Each diagonal has length $2r$, and each side has length $r\sqrt{2}$.
- **Area enclosed**: $\frac{1}{2} d_1 d_2 = \frac{1}{2}(2r)(2r) = \mathbf{2r^2}$.
- **Integer Lattice Points $(x, y)$** (when $h, k, r \in \mathbb{Z}$):
  - Strictly on the boundary ($|x| + |y| = r$): **$4r$** points (for $r \ge 1$).
  - Inside and on the boundary ($|x| + |y| \le r$): **$2r^2 + 2r + 1$** points.

### 2. When to Use It (Question Cue)
- *"Find the area enclosed by $|x - 2| + |y + 3| \le 5$ and the number of integer pairs $(x, y)$ satisfying it."*

### 3. General Example (Clean Numbers, Single Concept)
> For the region $|x| + |y| \le 3$:
> (a) Find the area enclosed by the graph in the $xy$-plane.
> (b) Find the number of integer pairs $(x, y)$ that satisfy the inequality.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $r = 3$.
  2. **Part (a) Area**: $2r^2 = 2(3^2) = \mathbf{18\text{ sq. units}}$.
  3. **Part (b) Integer Lattice Points**: $2r^2 + 2r + 1 = 2(9) + 2(3) + 1 = \mathbf{25\text{ integer pairs}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. **Area**: In Quadrant I ($x, y \ge 0$), $x + y \le 3$ is a right triangle of base $3$ and height $3$, so area $= \frac{1}{2}(3)(3) = 4.5$. Across all $4$ symmetric quadrants, Total Area $= 4 \times 4.5 = \mathbf{18}$.
  2. **Lattice Points**: Slice by $x$ from $-3$ to $+3$: for $x = \pm 3$ ($1$ value of $y$ each); $x = \pm 2$ ($3$ values each); $x = \pm 1$ ($5$ values each); $x = 0$ ($7$ values). Sum $= 1 + 3 + 5 + 7 + 5 + 3 + 1 = \mathbf{25}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using $\pi r^2$ (circle) or $4r^2$ (axis-aligned square) instead of **$2r^2$** for the diamond $|x| + |y| \le r$.

---

## Concept 13: Nested Modulus Equations ($\big||x - a| - b\big| = c$) & W-Graph Root Counting

### 1. Concept & Formula in Plain English
To solve $\big||x - a| - b\big| = c$ (with $b > 0$), peel the absolute value bars from the **outside in**:
1. Outer peel: $|x - a| - b = \pm c \implies |x - a| = b + c$ or $|x - a| = b - c$.
2. Inner peel: Any branch where the right-hand side is $> 0$ gives **$2$ roots**; if $= 0$ it gives **$1$ root** ($x = a$); if $< 0$ it gives **$0$ roots**!
3. **Symmetry Shortcut**: Because the graph is symmetric around $x = a$, every pair of roots $a \pm d$ adds up to $2a$. So if there are $k$ roots, their sum is $k \times a$!

### 2. When to Use It (Question Cue)
- *"Find the number of real roots and the sum of all real roots of $\big||x - 4| - 5\big| = 2$."*

### 3. General Example (Clean Numbers, Single Concept)
> Find the number of distinct real roots and the sum of all real roots of the equation $\big||x - 4| - 5\big| = 2$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in (Outside-In Peeling)**:
  1. Peel outer bars: $|x - 4| - 5 = 2$ or $|x - 4| - 5 = -2$.
  2. This gives $|x - 4| = 7$ or $|x - 4| = 3$.
  3. Since both $7 > 0$ and $3 > 0$, each branch yields $2$ roots:
     - $x - 4 = \pm 7 \implies x \in \{11, -3\}$
     - $x - 4 = \pm 3 \implies x \in \{7, 1\}$
  4. Total $= \mathbf{4\text{ real roots}}$, and their sum is $11 + (-3) + 7 + 1 = \mathbf{16}$.
- **Way 2 — Common-Sense / Ratio Intuition (Symmetry)**:
  1. Since $0 < c < b$ ($0 < 2 < 5$), the horizontal line $y = 2$ cuts all $4$ arms of the W-shaped graph centered at $x = 4$.
  2. By symmetry around $x = 4$, the average of the $4$ roots is $4$, so their sum is immediately $4 \times 4 = \mathbf{16}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Assuming $\big||x - 4| - 5\big| = 8$ also has $4$ roots—here $|x - 4| = 5 - 8 = -3$ is impossible (negative!), so only $|x - 4| = 13$ survives, giving just **$2$ roots**!
