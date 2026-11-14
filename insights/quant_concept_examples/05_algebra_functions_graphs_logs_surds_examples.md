# QA 05 Concept & Formula Examples: Functions, Graphs, Functional Equations, Logarithms, Surds & Indices

> **Companion Reference**: [`../topic_summaries/quant/05_algebra_functions_graphs_logs_surds.md`](../topic_summaries/quant/05_algebra_functions_graphs_logs_surds.md) | [`QA_Formula_and_Trigger_Book.md`](../high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md)

Every concept, formula, and pattern trigger from **QA 05** is explained below with plain-English intuition, clean single-concept numbers, a two-way walkthrough (direct formula vs. mental ratio intuition), and the #1 mistake to avoid.

---

## Concept 1: Logarithm Strict Domain Rules & Variable-Base Filtering

### 1. Concept & Formula in Plain English
$\log_b(a) = c$ simply asks: *"To what power $c$ must I raise base $b$ to get $a$?"* ($b^c = a$).
For a logarithm $\log_b(a)$ to exist in the real numbers, **three strict domain laws** must hold simultaneously:
1. **Argument $> 0$**: $a > 0$
2. **Base $> 0$**: $b > 0$
3. **Base $\neq 1$**: $b \neq 1$ (since $1^c = 1$ forever and can never reach other numbers!)

Whenever $x$ appears in the base or argument of a log equation, solve the algebra $a = b^c$, and then **test every candidate root** against all three domain rules!

### 2. When to Use It (Question Cue)
- *"Find all real solutions to $\log_{x-2}(x^2 - 4x + 3) = 2$ (or $\log_{x-1}(\dots) = k$)."*

### 3. General Example (Clean Numbers, Single Concept)
> Solve for all real values of $x$: $\log_{x - 1}(x + 5) = 2$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Write down the domain filters first:
     - Base $> 0 \implies x - 1 > 0 \implies x > 1$
     - Base $\neq 1 \implies x - 1 \neq 1 \implies x \neq 2$
     - Argument $> 0 \implies x + 5 > 0 \implies x > -5$
  2. Convert log to exponent: $(x - 1)^2 = x + 5$.
  3. Expand and solve:
     $$x^2 - 2x + 1 = x + 5 \implies x^2 - 3x - 4 = 0 \implies (x - 4)(x + 1) = 0 \implies x = 4 \text{ or } x = -1$$
  4. Filter against $x > 1, x \neq 2$: Reject $x = -1$ (gives negative base $-2$!). Only $\mathbf{x = 4}$ survives.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Plug $x = 4$ back into $\log_{x-1}(x+5)$: $\log_3(9) = 2$ (works!).
  2. Plug $x = -1$ back in: $\log_{-2}(4)$—a log base can never be negative! So only $\mathbf{x = 4}$ is valid.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using Vieta's formula to report the sum of roots as $4 + (-1) = 3$ without checking that $x = -1$ violates the base $> 0$ condition!

---

## Concept 2: Core Log Identities, Base-Change Chain Rule & Exponent-Swap

### 1. Concept & Formula in Plain English
- **Product / Quotient / Power**: $\log_b(xy) = \log_b x + \log_b y$; $\log_b(x/y) = \log_b x - \log_b y$; $\log_{b^m}(a^n) = \frac{n}{m}\log_b a$.
- **Base-Change & Telescoping Chain Rule**: $\log_b a = \frac{\log a}{\log b} = \frac{1}{\log_a b}$, so in a product of logs, matching arguments and bases cancel diagonally like fractions:
  $$\log_a b \cdot \log_b c \cdot \log_c d = \log_a d$$
- **Exponent-Swap Identity**: You can swap the base of an exponential and the argument of its log exponent without changing the value:
  $$a^{\log_b c} = c^{\log_b a}$$

### 2. When to Use It (Question Cue)
- *"Evaluate $\log_2 3 \cdot \log_3 4 \cdot \log_4 5 \cdots \log_{31} 32$."*
- *"Evaluate $5^{\log_3 9}$ or $8^{\log_2 5}$."*
- *"Solve $\log_2 x + \log_x 2 = 2.5$."*

### 3. General Example (Clean Numbers, Single Concept)
> Evaluate:
> (a) $P = \log_2 3 \cdot \log_3 5 \cdot \log_5 16$
> (b) $Q = 7^{\log_3 9} - 9^{\log_3 7}$

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: By the Base-Change Chain Rule, the intermediate $3$s and $5$s cancel:
     $$P = \log_2 16 = \log_2(2^4) = \mathbf{4}$$
  2. **Part (b)**: By the Exponent-Swap Identity $a^{\log_b c} = c^{\log_b a}$, we have $9^{\log_3 7} = 7^{\log_3 9}$, so:
     $$Q = 7^{\log_3 9} - 7^{\log_3 9} = \mathbf{0}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. **Part (a)**: Write each as $\frac{\ln b}{\ln a}$: $\frac{\ln 3}{\ln 2} \cdot \frac{\ln 5}{\ln 3} \cdot \frac{\ln 16}{\ln 5} = \frac{\ln 16}{\ln 2} = \frac{4\ln 2}{\ln 2} = \mathbf{4}$.
  2. **Part (b)**: Since $\log_3 9 = 2$, the first term is $7^2 = 49$. Since $9 = 3^2$, the second term is $(3^2)^{\log_3 7} = (3^{\log_3 7})^2 = 7^2 = 49$. Difference $= 49 - 49 = \mathbf{0}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Adding logs in a product ($\log_2 3 \cdot \log_2 5 \neq \log_2 15$; remember $\log_2 3 + \log_2 5 = \log_2 15$, whereas multiplication only telescopes when bases and arguments match!).

---

## Concept 3: Logarithmic Inequalities & The Base $0 < b < 1$ Sign-Flip Rule

### 1. Concept & Formula in Plain English
When unwrapping a logarithmic inequality $\log_b(f(x)) \ge k$:
- **If Base $b > 1$**: Larger input gives larger output, so the inequality sign **stays the same**: $f(x) \ge b^k$.
- **If Base $0 < b < 1$** (like $\frac{1}{2}$ or $0.2$): Raising a fraction to a bigger power makes it *smaller*, so the inequality sign **FLIPS**, AND you must enforce $f(x) > 0$:
  $$\log_b(f(x)) \ge k \quad (0 < b < 1) \iff 0 < f(x) \le b^k$$

### 2. When to Use It (Question Cue)
- *"Find the number of integers satisfying $\log_{1/3}(x - 2) \ge -2$."*

### 3. General Example (Clean Numbers, Single Concept)
> Find all integer values of $x$ that satisfy $\log_{1/3}(x - 2) \ge -2$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Since base $b = \frac{1}{3} \in (0, 1)$, apply the sandwich inequality $0 < f(x) \le b^k$:
     $$0 < x - 2 \le \left(\frac{1}{3}\right)^{-2} \implies 0 < x - 2 \le 9 \implies 2 < x \le 11$$
  2. Integers in $(2, 11]$ are $\{3, 4, 5, 6, 7, 8, 9, 10, 11\} \implies \mathbf{9\text{ integers}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Rewrite base $\frac{1}{3} = 3^{-1}$: $\log_{3^{-1}}(x - 2) = -\log_3(x - 2) \ge -2$.
  2. Multiply by $-1$ (which flips $\ge$ to $\le$): $\log_3(x - 2) \le 2 \implies 0 < x - 2 \le 3^2 = 9 \implies \mathbf{2 < x \le 11}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting the left-hand boundary $x - 2 > 0$ (which would falsely allow $x \le 2$ all the way to $-\infty$!), or forgetting to flip $\ge$ to $\le$ when the base is between $0$ and $1$.

---

## Concept 4: Characteristic & Mantissa (Counting Digits & Leading Zeros)

### 1. Concept & Formula in Plain English
Every base-$10$ logarithm $\log_{10} N$ splits into an integer part $c = \lfloor \log_{10} N \rfloor$ (**Characteristic**) and a fractional part $m \in [0, 1)$ (**Mantissa**):
- Since $\log_{10}(100) = 2$ (3 digits) and $\log_{10}(999) \approx 2.999$ (3 digits), the **number of digits** in any integer $N \ge 1$ is:
  $$\text{Number of Digits} = \lfloor \log_{10} N \rfloor + 1 = c + 1$$
- For a tiny decimal $0 < N < 1$, the number of **zeros immediately after the decimal point** before the first non-zero digit is $|c| - 1 = \lfloor -\log_{10} N \rfloor$.

### 2. When to Use It (Question Cue)
- *"Given $\log_{10} 2 = 0.30103$, find the number of digits in $2^{50}$."*

### 3. General Example (Clean Numbers, Single Concept)
> Given $\log_{10} 2 \approx 0.3010$, find the number of digits in $2^{40}$ when written out in base $10$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Compute $\log_{10}(2^{40}) = 40 \times \log_{10} 2 = 40 \times 0.3010 = 12.04$.
  2. Characteristic $c = \lfloor 12.04 \rfloor = 12$.
  3. Number of digits $= c + 1 = 12 + 1 = \mathbf{13\text{ digits}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Remember $2^{10} = 1024 \approx 10^3$.
  2. Therefore, $2^{40} = (2^{10})^4 = (1.024 \times 10^3)^4 \approx 1.10 \times 10^{12}$.
  3. $10^{12}$ is a $1$ followed by $12$ zeros ($\mathbf{13\text{ digits}}$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Reporting $\lfloor \log_{10} N \rfloor = 12$ instead of adding $+1$ ($12 + 1 = 13$ digits).

---

## Concept 5: De-nesting Nested Square Roots ($\sqrt{a \pm 2\sqrt{b}} = |\sqrt{x} \pm \sqrt{y}|$)

### 1. Concept & Formula in Plain English
When you see a square root inside a square root like $\sqrt{a \pm 2\sqrt{b}}$, it is the square of $(\sqrt{x} \pm \sqrt{y})$ in disguise! Since $(\sqrt{x} \pm \sqrt{y})^2 = (x + y) \pm 2\sqrt{xy}$, you just need to find two numbers $x \ge y > 0$ whose **sum is $a$** and whose **product is $b$**:
$$\sqrt{(x + y) \pm 2\sqrt{xy}} = \sqrt{x} \pm \sqrt{y} \quad (x \ge y > 0)$$
*(Make sure there is an exact **$2$** in front of the inner square root first!)*

### 2. When to Use It (Question Cue)
- *"Find the positive square root of $7 - 4\sqrt{3}$ (or simplify $\sqrt{9 + 2\sqrt{14}}$)."*

### 3. General Example (Clean Numbers, Single Concept)
> Simplify $\sqrt{8 - 2\sqrt{15}}$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Verify there is a $2$ outside the inner root: $\sqrt{8 - 2\sqrt{15}}$ has $a = 8$ and $b = 15$.
  2. Find two numbers $x \ge y$ such that $x + y = 8$ and $xy = 15$: clearly $x = 5$ and $y = 3$.
  3. Plug into $\sqrt{x} - \sqrt{y}$ (putting the larger number first so the result is positive):
     $$\sqrt{8 - 2\sqrt{15}} = \mathbf{\sqrt{5} - \sqrt{3}}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Rewrite $8$ as $5 + 3$ and $2\sqrt{15}$ as $2\sqrt{5}\sqrt{3}$:
     $$(\sqrt{5})^2 - 2\sqrt{5}\sqrt{3} + (\sqrt{3})^2 = (\sqrt{5} - \sqrt{3})^2 \implies \text{root is } \mathbf{\sqrt{5} - \sqrt{3}}$$

### 5. The 1 Common Mistake to Avoid
- **Trap**: Writing $\sqrt{3} - \sqrt{5}$ (which is negative! The principal square root $\sqrt{\dots}$ is **always non-negative**, so always put the larger root $\sqrt{5}$ first).

---

## Concept 6: Rationalizing Surd Denominators & Telescoping Surd Sums

### 1. Concept & Formula in Plain English
To get rid of square roots in the denominator of $\frac{1}{\sqrt{k+1} + \sqrt{k}}$, multiply top and bottom by the conjugate $(\sqrt{k+1} - \sqrt{k})$. Since $(\sqrt{k+1})^2 - (\sqrt{k})^2 = (k + 1) - k = 1$, the denominator vanishes:
$$\frac{1}{\sqrt{k+1} + \sqrt{k}} = \sqrt{k+1} - \sqrt{k}$$
When you sum a chain of these terms from $k = 1$ to $n$, every middle term cancels out, leaving only the **Last largest root minus the First smallest root**!

### 2. When to Use It (Question Cue)
- *"Evaluate $\frac{1}{\sqrt{1} + \sqrt{2}} + \frac{1}{\sqrt{2} + \sqrt{3}} + \dots + \frac{1}{\sqrt{99} + \sqrt{100}}$."*

### 3. General Example (Clean Numbers, Single Concept)
> Find the exact value of $\frac{1}{1 + \sqrt{2}} + \frac{1}{\sqrt{2} + \sqrt{3}} + \frac{1}{\sqrt{3} + \sqrt{4}} + \dots + \frac{1}{\sqrt{15} + \sqrt{16}}$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Replace each fraction $\frac{1}{\sqrt{k} + \sqrt{k+1}}$ with $\sqrt{k+1} - \sqrt{k}$:
     $$S = (\sqrt{2} - \sqrt{1}) + (\sqrt{3} - \sqrt{2}) + (\sqrt{4} - \sqrt{3}) + \dots + (\sqrt{16} - \sqrt{15})$$
  2. All middle roots cancel, leaving:
     $$S = \sqrt{16} - \sqrt{1} = 4 - 1 = \mathbf{3}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Check the first 3 terms ($1$ to $\sqrt{4}$): sum is $\sqrt{4} - 1 = 2 - 1 = 1$.
  2. By the same pattern up to $\sqrt{16}$, the sum is $\sqrt{16} - \sqrt{1} = 4 - 1 = \mathbf{3}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: If the gap inside the roots is $d$ instead of $1$ (e.g., $\frac{1}{\sqrt{5} + \sqrt{3}}$), rationalizing leaves a denominator of $5 - 3 = 2$, so remember to divide the final telescoped difference by **$d$**!

---

## Concept 7: Comparing Surds & Solving $f(x)^{g(x)} = 1$ (The 3-Case Checklist)

### 1. Concept & Formula in Plain English
When does a variable base raised to a variable power equal $1$, i.e., $f(x)^{g(x)} = 1$? There are **three distinct ways** this can happen, and you must check all three:
1. **Case 1 (Base $= 1$)**: $f(x) = 1$ ($1^{\text{anything}} = 1$).
2. **Case 2 (Exponent $= 0$ with non-zero base)**: $g(x) = 0$ AND $f(x) \neq 0$ ($\text{non-zero}^0 = 1$).
3. **Case 3 (Base $= -1$ with even exponent)**: $f(x) = -1$ AND $g(x)$ is an **even integer** ($(-1)^{\text{even}} = 1$).

### 2. When to Use It (Question Cue)
- *"Find the number (or sum) of all integer solutions to $(x - 3)^{x^2 - 16} = 1$."*

### 3. General Example (Clean Numbers, Single Concept)
> Find all real integer solutions $x$ to the equation $(x - 3)^{x^2 - 4} = 1$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in (3-Case Checklist)**:
  1. **Case 1 (Base $= 1$)**: $x - 3 = 1 \implies \mathbf{x = 4}$.
  2. **Case 2 (Exponent $= 0$, Base $\neq 0$)**: $x^2 - 4 = 0 \implies \mathbf{x = 2}$ or $\mathbf{x = -2}$ (at both values, base $x - 3 \neq 0$).
  3. **Case 3 (Base $= -1$, Exponent even)**: $x - 3 = -1 \implies x = 2$. Check exponent at $x = 2$: $2^2 - 4 = 0$ (which is even, already counted in Case 2!).
  4. Distinct solutions are $x \in \{-2, 2, 4\} \implies \mathbf{3\text{ solutions}}$ (sum $= 4$).
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Plug in small integers around $x = 3$ (where base is $0$, $1$, or $-1$) and around $x = \pm 2$ (where power is $0$): $x=4 \to 1^{12}=1$; $x=2 \to (-1)^0=1$; $x=-2 \to (-5)^0=1$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting **Case 3 (Base $= -1$ with an even power)** or forgetting to discard roots where $0^0$ occurs!

---

## Concept 8: Counting Functions (Total, One-to-One / Injective, Onto / Surjective, Bijective)

### 1. Concept & Formula in Plain English
Think of a function $f: A \to B$ (where $|A| = m$ items and $|B| = n$ boxes) as sending each of the $m$ items in $A$ to exactly one box in $B$:
- **Total Functions**: Each of the $m$ elements in $A$ has $n$ choices $\implies \mathbf{n^m}$.
- **One-to-One (Injective)**: No two elements in $A$ can land in the same box in $B$ ($m \le n$) $\implies n \times (n-1) \times \dots \times (n-m+1) = \mathbf{P(n, m)}$.
- **Onto (Surjective)**: Every box in $B$ must receive at least one arrow ($m \ge n$). For $n = 2$ boxes, subtract the $2$ functions where all arrows go into just one box: $\mathbf{2^m - 2}$.
- **Bijective (Both One-to-One & Onto)**: Requires $m = n$, giving $\mathbf{n!}$.

### 2. When to Use It (Question Cue)
- *"If set A has $4$ elements and set B has $2$ elements, how many total functions and how many onto (surjective) functions exist from A to B?"*

### 3. General Example (Clean Numbers, Single Concept)
> Let $A = \{1, 2, 3, 4\}$ and $B = \{a, b\}$. Find:
> (a) Total number of functions from $A$ to $B$.
> (b) Number of onto (surjective) functions from $A$ to $B$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $m = |A| = 4$ and $n = |B| = 2$.
  2. **Part (a) Total Functions**: $n^m = 2^4 = \mathbf{16}$.
  3. **Part (b) Onto Functions**: $2^m - 2 = 2^4 - 2 = 16 - 2 = \mathbf{14}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Each of the $4$ numbers $\{1, 2, 3, 4\}$ can be mapped to either $a$ or $b$ ($2 \times 2 \times 2 \times 2 = 16$ ways).
  2. The only ways to *fail* to cover both $\{a, b\}$ are sending everything to $a$ ($1$ way) or sending everything to $b$ ($1$ way). Removing those $2$ bad cases leaves $16 - 2 = \mathbf{14}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Mixing up $n^m$ ($2^4 = 16$) with $m^n$ ($4^2 = 16$ happens to match here, but for $|A|=3, |B|=2$, it is $2^3 = 8$, NOT $3^2 = 9$—always remember $(\text{Target Choices})^{\text{Source Items}}$!).

---

## Concept 9: Standard Cauchy Functional Equations & Symmetric Pairing

### 1. Concept & Formula in Plain English
Instead of doing abstract algebra on functional equations, immediately substitute the standard function family that obeys that law:
- $f(x + y) = f(x) + f(y) \implies \mathbf{f(x) = kx}$ (Linear)
- $f(x + y) = f(x) \cdot f(y) \implies \mathbf{f(x) = a^x}$ (Exponential)
- $f(xy) = f(x) + f(y) \implies \mathbf{f(x) = k\log x}$ (Logarithmic)
- $f(x) \cdot f(1/x) = f(x) + f(1/x) \implies \mathbf{f(x) = 1 \pm x^n}$
- **Symmetric Pairing**: If $f(x) + f(1 - x) = c$, pair the first and last terms of $\sum_{k=1}^{n-1} f(k/n)$ into pairs that each sum to $c$.

### 2. When to Use It (Question Cue)
- *"If $f(x + y) = f(x) + f(y)$ for all $x, y$ and $f(3) = 15$, find $f(10)$."*
- *"If $f(x) \cdot f(1/x) = f(x) + f(1/x)$ and $f(2) = 9$, find $f(3)$."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) A function satisfies $f(x + y) = f(x) + f(y)$ for all real $x, y$. If $f(3) = 15$, find $f(10)$.
> (b) A polynomial function satisfies $f(x) \cdot f\left(\frac{1}{x}\right) = f(x) + f\left(\frac{1}{x}\right)$ and $f(2) = 9$. Find $f(3)$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: Substitute $f(x) = kx$. Since $f(3) = 3k = 15 \implies k = 5$. Thus $f(10) = 5(10) = \mathbf{50}$.
  2. **Part (b)**: Substitute $f(x) = 1 \pm x^n$. Given $f(2) = 1 \pm 2^n = 9 \implies +2^n = 8 \implies n = 3$ with $+$ sign. Thus $f(x) = 1 + x^3 \implies f(3) = 1 + 3^3 = \mathbf{28}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), $f(3) = f(1 + 1 + 1) = 3f(1) = 15 \implies f(1) = 5$, so $f(10) = 10f(1) = \mathbf{50}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: In $f(x) = 1 \pm x^n$, forgetting the $1 +$ in front and writing $f(3) = 27$ instead of $1 + 27 = 28$.

---

## Concept 10: Periodic Composite Functions $f^{(n)}(x)$ & Domain of Composite Rational Functions

### 1. Concept & Formula in Plain English
1. **Periodic Compositions ($f(f(\dots f(x)))$)**: Fractional functions like $f(x) = \frac{1}{1-x}$ or $\frac{1-x}{1+x}$ cycle back to $x$ after $2, 3,$ or $4$ steps! Just plug in the given number for step $1, 2, 3, \dots$ until it repeats, then reduce the huge exponent modulo the cycle length.
2. **Domain of $f(g(x))$**: You must exclude **both** values of $x$ that break the inner function $g(x)$ (zero denominator) **and** values of $x$ where the output $g(x)$ equals a forbidden input of the outer function $f$!

### 2. When to Use It (Question Cue)
- *"If $f(x) = \frac{1}{1 - x}$, find $f^{(100)}(2)$."*
- *"If $f(x) = \frac{1}{x - 2}$ and $g(x) = \frac{1}{x - 3}$, find all excluded values of $x$ for $f(g(x))$."*

### 3. General Example (Clean Numbers, Single Concept)
> Let $f(x) = \frac{1}{1 - x}$ and define $f^{(n)}(x) = f(f^{(n-1)}(x))$. Find the value of $f^{(100)}(2)$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in (Cycle Detection)**:
  1. Step 1: $f^{(1)}(2) = \frac{1}{1 - 2} = -1$.
  2. Step 2: $f^{(2)}(2) = f(-1) = \frac{1}{1 - (-1)} = \frac{1}{2}$.
  3. Step 3: $f^{(3)}(2) = f(1/2) = \frac{1}{1 - 1/2} = 2$ (Back to start! Period $= 3$).
  4. Divide $100$ by period $3$: $100 = 3(33) + 1$ (remainder $1$).
  5. Therefore, $f^{(100)}(2) = f^{(1)}(2) = \mathbf{-1}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Every $3$ applications do nothing ($2 \to -1 \to \frac{1}{2} \to 2$), so $99$ applications land back on $2$, and the $100$th step lands on $\mathbf{-1}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: When finding the domain of $f(g(x)) = \frac{1}{\frac{1}{x-3} - 2} = \frac{x-3}{7 - 2x}$, looking only at the simplified final fraction (which excludes $x = 3.5$) and forgetting to also exclude the inner denominator root **$x = 3$**!

---

## Concept 11: Greatest Integer Function $\lfloor x \rfloor$, Fractional Part $\{x\}$, Hermite's Identity & $\lfloor x^2 \rfloor = \lfloor x \rfloor^2$

### 1. Concept & Formula in Plain English
Every real number $x$ splits uniquely into its **integer floor** $n = \lfloor x \rfloor \in \mathbb{Z}$ and its **fractional part** $f = \{x\} \in [0, 1)$:
$$x = \lfloor x \rfloor + \{x\}$$
- **Negative Floor Guard**: $\lfloor -2.3 \rfloor = -3$ (the integer to the **left** on the number line, NOT $-2$), and $\{-2.3\} = -2.3 - (-3) = +0.7$ (always $\ge 0$).
- **Hermite's Identity**: $\lfloor x \rfloor + \lfloor x + \frac{1}{n} \rfloor + \dots + \lfloor x + \frac{n-1}{n} \rfloor = \lfloor nx \rfloor$.
- **Step Interval for $\lfloor x^2 \rfloor = \lfloor x \rfloor^2$ ($x \ge 1$)**: On each integer interval $[n, n+1)$, $\lfloor x \rfloor^2 = n^2$, so $\lfloor x^2 \rfloor = n^2$ holds iff $n^2 \le x^2 < n^2 + 1 \iff x \in \mathbf{[n, \sqrt{n^2 + 1})}$ with a strictly **open** right bracket!

### 2. When to Use It (Question Cue)
- *"Solve $\lfloor x \rfloor + 2\{x\} = 3.4$."*
- *"Find the set of real values of $x \in [2, 4]$ satisfying $\lfloor x^2 \rfloor = \lfloor x \rfloor^2$."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) Find $x$ if $\lfloor x \rfloor + 2\{x\} = 4.6$.
> (b) Find all real $x \in [2, 3)$ such that $\lfloor x^2 \rfloor = \lfloor x \rfloor^2$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: Let $\lfloor x \rfloor = n \in \mathbb{Z}$ and $\{x\} = f \in [0, 1)$. Then $n + 2f = 4.6 \implies 2f = 4.6 - n$.
     - Since $0 \le 2f < 2$, we need $0 \le 4.6 - n < 2 \implies n \in \{3, 4\}$.
     - If $n = 4$: $2f = 0.6 \implies f = 0.3 \implies x = 4 + 0.3 = \mathbf{4.3}$.
     - If $n = 3$: $2f = 1.6 \implies f = 0.8 \implies x = 3 + 0.8 = \mathbf{3.8}$.
  2. **Part (b)**: On $[2, 3)$, $n = 2$, so the formula $[n, \sqrt{n^2+1})$ immediately gives $\mathbf{[2, \sqrt{5})}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (b), for $x \in [2, 3)$, $\lfloor x \rfloor = 2$, so the RHS is $2^2 = 4$.
  2. For the LHS $\lfloor x^2 \rfloor$ to also equal $4$, $x^2$ must lie in $[4, 5)$, which means $\mathbf{2 \le x < \sqrt{5}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Including the right endpoint $\sqrt{5}$ in $[2, \sqrt{5}]$—at $x = \sqrt{5}$, $\lfloor x^2 \rfloor = \lfloor 5 \rfloor = 5$ whereas $\lfloor \sqrt{5} \rfloor^2 = 2^2 = 4$ ($5 \neq 4$)!
