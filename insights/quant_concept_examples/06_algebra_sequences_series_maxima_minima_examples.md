# QA 06 Concept & Formula Examples: Sequences, Series, Telescoping Sums & Maxima/Minima

> **Companion Reference**: [`../topic_summaries/quant/06_algebra_sequences_series_maxima_minima.md`](../topic_summaries/quant/06_algebra_sequences_series_maxima_minima.md) | [`QA_Formula_and_Trigger_Book.md`](../high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md)

Every concept, formula, and pattern trigger from **QA 06** is explained below with plain-English intuition, clean single-concept numbers, a two-way walkthrough (direct formula vs. mental ratio intuition), and the #1 mistake to avoid.

---

## Concept 1: Arithmetic Progression (AP): $T_n$, Middle-Term Sum $S_n = n \cdot T_{\text{mid}}$ & Quadratic Sum Signature

### 1. Concept & Formula in Plain English
An **Arithmetic Progression (AP)** adds a constant step $d$ each time ($a,\; a+d,\; a+2d, \dots$):
$$T_n = a + (n - 1)d, \qquad S_n = \frac{n}{2}[2a + (n - 1)d] = \frac{n}{2}(T_1 + T_n) = n \times T_{\text{middle}}$$
- **Middle-Term Shortcut**: For any odd number of terms $n = 2m - 1$, the average of the entire AP is the exact middle term $T_m$, so **$S_{2m-1} = (2m - 1) \cdot T_m$**!
- **Quadratic Sum Signature ($S_n = An^2 + Bn$)**: The sum of the first $n$ terms of a true AP is always a quadratic with **zero constant term**:
  $$\text{First term } a = S_1 = A + B, \qquad \text{Common difference } d = 2A, \qquad T_n = 2An + (B - A)$$

### 2. When to Use It (Question Cue)
- *"If the 5th term of an AP is $14$, find the sum of its first $9$ terms."*
- *"If the sum of the first $n$ terms of an AP is $3n^2 + 4n$, find its $10$th term."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) In an AP, the $5$th term is $14$. Find the sum of the first $9$ terms ($S_9$).
> (b) If $S_n = 3n^2 + 4n$, find the common difference $d$ and the $10$th term $T_{10}$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: Since $T_5$ is the exact middle term of $T_1, \dots, T_9$, use $S_{2m-1} = (2m - 1)T_m$:
     $$S_9 = 9 \times T_5 = 9 \times 14 = \mathbf{126}$$
  2. **Part (b)**: Here $A = 3, B = 4$. Thus $d = 2A = \mathbf{6}$, and $T_{10} = 2(3)(10) + (4 - 3) = \mathbf{61}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), pair $T_1 + T_9 = 2T_5$, $T_2 + T_8 = 2T_5$, etc. Every symmetric pair averages to $T_5 = 14$, so $9$ terms sum to $9 \times 14 = \mathbf{126}$.
  2. In (b), $T_{10} = S_{10} - S_9 = [3(100) + 40] - [3(81) + 36] = 340 - 279 = \mathbf{61}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: If $S_n = 3n^2 + 4n + 5$ has a **non-zero constant $C = 5$**, $T_1 = S_1 = 12$ is a one-off anomaly, while for $n \ge 2$, $T_n = S_n - S_{n-1} = 6n + 1$ ($C$ cancels out for $n \ge 2$!).

---

## Concept 2: AP Ratio of Sums vs. Ratio of Terms & Common Terms of Two APs

### 1. Concept & Formula in Plain English
1. **Sum Ratio to Term Ratio ($\frac{S_{2m-1}}{S'_{2m-1}} = \frac{T_m}{T'_m}$)**: Because $S_{2m-1} = (2m - 1)T_m$, the ratio of the $m$-th terms of two APs equals the ratio of their sums for **$n = 2m - 1$** terms!
2. **Common Terms of Two APs**: If $\text{AP}_1$ has step $d_1$ and $\text{AP}_2$ has step $d_2$, the numbers that appear in **both** sequences form a new AP whose first term is the first shared number and whose common difference is **$D = \text{LCM}(d_1, d_2)$**.

### 2. When to Use It (Question Cue)
- *"The sums of $n$ terms of two APs are in the ratio $(2n + 3) : (5n + 1)$. Find the ratio of their $6$th terms."*
- *"How many terms are common to $3, 7, 11, \dots, 99$ and $2, 5, 8, \dots, 101$?"*

### 3. General Example (Clean Numbers, Single Concept)
> (a) The ratio of the sums of the first $n$ terms of two APs is $\frac{2n + 3}{5n + 1}$. Find the ratio of their $6$th terms.
> (b) Find the number of common terms in $S_1 = \{3, 7, 11, \dots, 99\}$ and $S_2 = \{2, 5, 8, 11, \dots, 101\}$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: For the $m = 6$th term, plug $n = 2(6) - 1 = 11$ into $\frac{2n+3}{5n+1}$:
     $$\frac{T_6}{T'_6} = \frac{2(11) + 3}{5(11) + 1} = \frac{25}{56} = \mathbf{25 : 56}$$
  2. **Part (b)**: First common term $= 11$. Common difference $D = \text{LCM}(4, 3) = 12$.
     Smallest upper bound $= \min(99, 101) = 99$.
     Solve $11 + 12(k - 1) \le 99 \implies 12(k - 1) \le 88 \implies k - 1 \le 7 \implies k = \mathbf{8\text{ common terms}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), $\frac{S_{11}}{S'_{11}} = \frac{11 \cdot T_6}{11 \cdot T'_6} = \frac{T_6}{T'_6}$, which is why plugging $n = 11$ cancels the $11$ and leaves $\frac{T_6}{T'_6}$ directly!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Plugging $n = 6$ (or $n = 2m = 12$) instead of **$n = 2m - 1 = 11$** when converting a sum ratio into an $m$-th term ratio!

---

## Concept 3: Geometric Progression (GP), Infinite GP & 3-Term Pairwise Identity

### 1. Concept & Formula in Plain English
A **Geometric Progression (GP)** multiplies by a constant ratio $r$ each step ($a,\; ar,\; ar^2, \dots$):
$$T_n = a r^{n-1}, \qquad S_n = \frac{a(r^n - 1)}{r - 1}, \qquad S_\infty = \frac{a}{1 - r} \;\;(|r| < 1)$$
- **Product of $n$ terms**: $P_n = (T_{\text{middle}})^n$.
- **3-Term GP Pairwise Product Identity**: For any three terms $a_1, a_2, a_3$ in GP, $a_1 a_3 = a_2^2$. Therefore:
  $$a_1 a_2 + a_2 a_3 + a_3 a_1 = a_1 a_2 + a_2 a_3 + a_2^2 = a_2(a_1 + a_2 + a_3) \implies a_2 = \frac{a_1 a_2 + a_2 a_3 + a_3 a_1}{a_1 + a_2 + a_3}$$

### 2. When to Use It (Question Cue)
- *"A ball dropped from $60\text{ m}$ rebounds to $\frac{2}{3}$ of its height each bounce. Find total distance traveled."*
- *"Three numbers in GP have sum $21$ and sum of pairwise products $126$. Find the middle term."*

### 3. General Example (Clean Numbers, Single Concept)
> Three numbers $a_1, a_2, a_3$ are in a decreasing Geometric Progression such that $a_1 + a_2 + a_3 = 21$ and $a_1 a_2 + a_2 a_3 + a_3 a_1 = 126$. Find the three numbers and the infinite sum of the GP.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Divide the pairwise product sum by the linear sum to get the middle term $a_2$ immediately:
     $$a_2 = \frac{126}{21} = \mathbf{6}$$
  2. Now $a_1 + a_3 = 21 - 6 = 15$ and $a_1 a_3 = a_2^2 = 36$.
  3. Two numbers with sum $15$ and product $36$ (decreasing) are $a_1 = 12$ and $a_3 = 3$.
  4. Common ratio $r = \frac{6}{12} = \frac{1}{2}$, so $S_\infty = \frac{a_1}{1 - r} = \frac{12}{1 - 1/2} = \mathbf{24}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Factor $a_2$ out of $a_1 a_2 + a_2^2 + a_2 a_3$ (since $a_3 a_1 = a_2^2$): it is literally $a_2 \times (\text{sum of the three terms})$!

### 5. The 1 Common Mistake to Avoid
- **Trap**: In bouncing-ball infinite GP problems, forgetting that the first drop of $H$ occurs **once**, while every rebound height occurs **twice** (up and down): $\text{Total Distance} = H + 2H\left(\frac{r}{1-r}\right) = H\left(\frac{1+r}{1-r}\right)$.

---

## Concept 4: Harmonic Progression (HP) & Arithmetico-Geometric Progression (AGP)

### 1. Concept & Formula in Plain English
- **Harmonic Progression (HP)**: A sequence is an HP if its **reciprocals** form an AP ($\frac{1}{T_n} = a + (n-1)d$). Never try to work on an HP directly—flip every term into an AP, find the needed term in the AP, and flip it back!
- **Arithmetico-Geometric Progression (AGP)**: Each term is an AP term multiplied by a GP power, like $1 + 2x + 3x^2 + 4x^3 + \dots$. For $|r| < 1$:
  $$S_\infty = \frac{a}{1 - r} + \frac{dr}{(1 - r)^2}$$

### 2. When to Use It (Question Cue)
- *"If the 3rd term of an HP is $\frac{1}{7}$ and the 7th term is $\frac{1}{15}$, find the 10th term."*
- *"Find the infinite sum $S = 1 + \frac{2}{2} + \frac{3}{4} + \frac{4}{8} + \frac{5}{16} + \dots$"*

### 3. General Example (Clean Numbers, Single Concept)
> Evaluate the infinite Arithmetico-Geometric series: $S = 1 + \frac{2}{2} + \frac{3}{4} + \frac{4}{8} + \frac{5}{16} + \dots$

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Numerators $1, 2, 3, 4, \dots$ form an AP with $a = 1, d = 1$.
  2. Multipliers $1, \frac{1}{2}, \frac{1}{4}, \dots$ form a GP with $r = \frac{1}{2}$.
  3. Plug into $S_\infty = \frac{a}{1 - r} + \frac{dr}{(1 - r)^2}$:
     $$S_\infty = \frac{1}{1 - 1/2} + \frac{1 \cdot (1/2)}{(1 - 1/2)^2} = 2 + \frac{1/2}{1/4} = 2 + 2 = \mathbf{4}$$
- **Way 2 — Common-Sense / Ratio Intuition (Shift & Subtract)**:
  1. Write $S = 1 + \frac{2}{2} + \frac{3}{4} + \frac{4}{8} + \dots$
  2. Multiply by $\frac{1}{2}$ and shift one column right: $\frac{1}{2}S = \frac{1}{2} + \frac{2}{4} + \frac{3}{8} + \dots$
  3. Subtract: $\frac{1}{2}S = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \dots = \frac{1}{1 - 1/2} = 2 \implies S = \mathbf{4}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Trying to sum an HP using an AP sum formula (there is no closed-form formula for the sum of an HP!).

---

## Concept 5: Standard Power Sums ($\sum k, \sum k^2, \sum k^3$, Odd Prefix Sum) & Finite Differences

### 1. Concept & Formula in Plain English
- **First $n$ Naturals**: $\sum_{k=1}^n k = \frac{n(n+1)}{2}$
- **First $n$ Odd Numbers**: $1 + 3 + 5 + \dots + (2n - 1) = \mathbf{n^2}$
- **First $n$ Squares**: $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$
- **First $n$ Cubes**: $\sum_{k=1}^n k^3 = \left[\frac{n(n+1)}{2}\right]^2$
- **Method of Finite Differences**: If the gaps between consecutive terms ($T_2 - T_1,\; T_3 - T_2, \dots$) form an AP, then $T_n$ is a quadratic $An^2 + Bn + C$ where $2A$ equals the constant 2nd difference!

### 2. When to Use It (Question Cue)
- *"Find the sum $1^2 + 2^2 + \dots + 10^2$."*
- *"Find the $10$th term of $2, 5, 10, 17, 26, \dots$"*

### 3. General Example (Clean Numbers, Single Concept)
> Evaluate $1^2 + 2^2 + 3^2 + \dots + 10^2$, and find the sum of the first $20$ odd positive integers.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. For $n = 10$ squares:
     $$\sum_{k=1}^{10} k^2 = \frac{10(11)(21)}{6} = \mathbf{385}$$
  2. For the first $m = 20$ odd integers: $\text{Sum} = m^2 = 20^2 = \mathbf{400}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Worth memorizing $\sum_{k=1}^{10} k^2 = 385$ and $\sum_{k=1}^{20} k^2 = 2870$ as instant CAT benchmarks!

### 5. The 1 Common Mistake to Avoid
- **Trap**: When summing $1 + 3 + 5 + \dots + 39$, squaring the last term $39^2$ instead of squaring the **number of terms** $m = \frac{39 + 1}{2} = 20 \implies 20^2 = 400$.

---

## Concept 6: Telescoping Partial Fractions ($\frac{1}{k(k+d)}$ and $\frac{1}{k(k+1)(k+2)}$)

### 1. Concept & Formula in Plain English
When a denominator is a product of two numbers that differ by $d$, split the fraction into a subtraction of two simpler fractions so that middle terms cancel out (telescope):
$$\frac{1}{k(k + d)} = \frac{1}{d}\left(\frac{1}{k} - \frac{1}{k + d}\right)$$
For three consecutive factors:
$$\frac{1}{k(k+1)(k+2)} = \frac{1}{2}\left[\frac{1}{k(k+1)} - \frac{1}{(k+1)(k+2)}\right]$$

### 2. When to Use It (Question Cue)
- *"Find the sum $\frac{1}{1 \times 3} + \frac{1}{3 \times 5} + \frac{1}{5 \times 7} + \dots + \frac{1}{19 \times 21}$."*

### 3. General Example (Clean Numbers, Single Concept)
> Evaluate $S = \frac{1}{1 \times 3} + \frac{1}{3 \times 5} + \frac{1}{5 \times 7} + \dots + \frac{1}{19 \times 21}$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here the gap in each denominator is $d = 3 - 1 = 2$.
  2. Factor out $\frac{1}{d} = \frac{1}{2}$ and split each term:
     $$S = \frac{1}{2}\left[\left(\frac{1}{1} - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{5}\right) + \dots + \left(\frac{1}{19} - \frac{1}{21}\right)\right]$$
  3. All interior terms cancel, leaving:
     $$S = \frac{1}{2}\left(1 - \frac{1}{21}\right) = \frac{1}{2} \times \frac{20}{21} = \mathbf{\frac{10}{21}}$$
- **Way 2 — Common-Sense / Ratio Intuition ($n = 1, 2$ Pattern Check)**:
  1. 1st term $= \frac{1}{3}$; sum of first 2 terms $= \frac{1}{3} + \frac{1}{15} = \frac{6}{15} = \frac{2}{5}$; sum of first 3 terms $= \frac{2}{5} + \frac{1}{35} = \frac{3}{7}$.
  2. Pattern for $n$ terms is $\frac{n}{2n + 1}$. Here there are $10$ terms, so $S = \mathbf{\frac{10}{21}}$!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting the $\frac{1}{d} = \frac{1}{2}$ multiplier in front when the denominator factors differ by $d = 2$ (writing $1 - \frac{1}{21} = \frac{20}{21}$ instead of $\frac{10}{21}$).

---

## Concept 7: Factorial Telescoping & Telescoping Radicals

### 1. Concept & Formula in Plain English
Three classic non-obvious telescoping disguises appear repeatedly in CAT:
1. **Multiplying Factorials**: $k \cdot k! = (k + 1 - 1)k! = (k + 1)! - k! \implies \sum_{k=1}^n k \cdot k! = (n + 1)! - 1$.
2. **Dividing Factorials**: $\frac{k}{(k+1)!} = \frac{(k+1) - 1}{(k+1)!} = \frac{1}{k!} - \frac{1}{(k+1)!} \implies \sum_{k=1}^n \frac{k}{(k+1)!} = 1 - \frac{1}{(n+1)!}$.
3. **Telescoping Radical**:
   $$\sqrt{1 + \frac{1}{k^2} + \frac{1}{(k+1)^2}} = 1 + \frac{1}{k} - \frac{1}{k+1}$$

### 2. When to Use It (Question Cue)
- *"Evaluate $\sqrt{1 + \frac{1}{1^2} + \frac{1}{2^2}} + \sqrt{1 + \frac{1}{2^2} + \frac{1}{3^2}} + \dots + \sqrt{1 + \frac{1}{9^2} + \frac{1}{10^2}}$."*

### 3. General Example (Clean Numbers, Single Concept)
> Find the exact value of $\sum_{k=1}^{9} \sqrt{1 + \frac{1}{k^2} + \frac{1}{(k+1)^2}}$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Replace each square root with $1 + \frac{1}{k} - \frac{1}{k+1}$:
     $$S = \sum_{k=1}^{9} \left(1 + \frac{1}{k} - \frac{1}{k+1}\right)$$
  2. TheNine $1$s add up to $9$, and the fractions telescope to $\frac{1}{1} - \frac{1}{10}$:
     $$S = 9 + \left(1 - \frac{1}{10}\right) = 9 + 0.9 = \mathbf{9.9} \quad \left(\frac{99}{10}\right)$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Evaluate just the first radical ($k = 1$): $\sqrt{1 + 1 + \frac{1}{4}} = \sqrt{\frac{9}{4}} = \frac{3}{2} = 1 + \left(1 - \frac{1}{2}\right)$.
  2. Evaluate the second radical ($k = 2$): $\sqrt{1 + \frac{1}{4} + \frac{1}{9}} = \sqrt{\frac{49}{36}} = \frac{7}{6} = 1 + \left(\frac{1}{2} - \frac{1}{3}\right)$.
  3. Summing $9$ terms clearly gives $9 + 1 - \frac{1}{10} = \mathbf{9.9}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting to add the $n$ copies of $1$ (reporting $1 - \frac{1}{10} = 0.9$ instead of $9 + 0.9 = 9.9$).

---

## Concept 8: AM-GM-HM Inequality & Shifted-Denominator Balancing

### 1. Concept & Formula in Plain English
For **strictly positive real numbers** ($x_i > 0$):
$$\text{AM} \ge \text{GM} \ge \text{HM}, \quad \text{with equality iff all terms are equal.}$$
In particular, when two positive terms have a constant product $P$, their sum is minimized when the two terms are equal ($A + B \ge 2\sqrt{AB}$).
If you need to minimize $x + \frac{a}{x - c}$ for $x > c$, first subtract and add $c$ so the variable part $(x - c)$ matches the denominator and cancels out in the product!

### 2. When to Use It (Question Cue)
- *"For $x > 2$, find the minimum value of $x + \frac{9}{x - 2}$."*

### 3. General Example (Clean Numbers, Single Concept)
> Find the minimum value of $f(x) = x + \frac{9}{x - 2}$ for $x > 2$, and the value of $x$ where this minimum occurs.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Rewrite $x$ as $(x - 2) + 2$ to match the denominator $(x - 2) > 0$:
     $$f(x) = (x - 2) + \frac{9}{x - 2} + 2$$
  2. Apply AM-GM to the two positive terms $(x - 2)$ and $\frac{9}{x - 2}$:
     $$(x - 2) + \frac{9}{x - 2} \ge 2\sqrt{(x - 2) \cdot \frac{9}{x - 2}} = 2\sqrt{9} = 6$$
  3. Add back the $+2$: Minimum value $= 6 + 2 = \mathbf{8}$, attained when $x - 2 = \frac{9}{x - 2} \implies x - 2 = 3 \implies \mathbf{x = 5}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Plug in clean integers above $2$ so $(x - 2)$ divides $9$:
     - $x = 3 \implies 3 + 9/1 = 12$
     - $x = 5 \implies 5 + 9/3 = \mathbf{8}$
     - $x = 11 \implies 11 + 9/9 = 12$. Minimum is $\mathbf{8}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Applying AM-GM without checking if the equality point $x = 5$ is actually inside the allowed domain (e.g., if the domain were $x \ge 6$, $x = 5$ is forbidden, so the minimum on $[6, \infty)$ would be at the boundary $x = 6 \implies 6 + \frac{9}{4} = 8.25$, NOT $8$!).

---

## Concept 9: Weighted AM-GM Term Splitting (Maximizing $x^p y^q$ & Cancelling Powers)

### 1. Concept & Formula in Plain English
1. **Maximizing $x^p y^q$ given $ax + by = S$ ($x, y > 0$)**: Split $ax$ into $p$ equal pieces of $\frac{ax}{p}$ and $by$ into $q$ equal pieces of $\frac{by}{q}$. By AM-GM, the product is maximized when all $(p + q)$ pieces are equal:
   $$\frac{ax}{p} = \frac{by}{q} = \frac{S}{p + q}$$
2. **Minimizing $x^2 + \frac{a}{x}$ ($x > 0$)**: To make $x$ cancel in the product, split $\frac{a}{x}$ into **two equal halves** $\frac{a}{2x} + \frac{a}{2x}$ so that $x^2 \cdot \frac{a}{2x} \cdot \frac{a}{2x} = \frac{a^2}{4}$ is constant!

### 2. When to Use It (Question Cue)
- *"If $x, y > 0$ and $2x + 3y = 10$, find the maximum value of $x^2 y^3$."*
- *"For $x > 0$, find the minimum value of $x^2 + \frac{54}{x}$."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) If $x, y > 0$ and $x + y = 10$, find the maximum value of $x^3 y^2$.
> (b) For $x > 0$, find the minimum value of $x^2 + \frac{54}{x}$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: Here $a = 1, b = 1, p = 3, q = 2, S = 10$.
     Set $\frac{x}{3} = \frac{y}{2} = \frac{10}{3 + 2} = 2 \implies x = 6,\; y = 4$.
     Max value $= 6^3 \times 4^2 = 216 \times 16 = \mathbf{3,456}$.
  2. **Part (b)**: Split $\frac{54}{x}$ into two equal terms $\frac{27}{x} + \frac{27}{x}$:
     $$x^2 + \frac{27}{x} + \frac{27}{x} \ge 3\sqrt[3]{x^2 \cdot \frac{27}{x} \cdot \frac{27}{x}} = 3\sqrt[3]{27^2} = 3 \times 9 = \mathbf{27} \quad (\text{at } x = 3)$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), $x$ has weight $3$ and $y$ has weight $2$, so split the sum $10$ in the ratio $3 : 2 \implies x = 6, y = 4$.
  2. In (b), set the split terms equal: $x^2 = \frac{27}{x} \implies x^3 = 27 \implies x = 3$, giving $3^2 + \frac{54}{3} = 9 + 18 = \mathbf{27}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Applying 2-term AM-GM to $x^2 + \frac{54}{x} \ge 2\sqrt{54x}$—since $x$ is still inside the square root, $2\sqrt{54x}$ is NOT a constant minimum! You must split $\frac{54}{x}$ into two halves so $x$ cancels completely.

---

## Concept 10: Cauchy-Schwarz / Titu's Lemma & Parabola Vertex Extrema

### 1. Concept & Formula in Plain English
- **Titu's Lemma (Engel Form of Cauchy-Schwarz)**: For any real numerators $a_i$ and positive denominators $b_i > 0$:
  $$\frac{a_1^2}{b_1} + \frac{a_2^2}{b_2} + \frac{a_3^2}{b_3} \ge \frac{(a_1 + a_2 + a_3)^2}{b_1 + b_2 + b_3}$$
  Equality holds when $\frac{a_1}{b_1} = \frac{a_2}{b_2} = \frac{a_3}{b_3}$.
- **Parabola Vertex Extrema**: For $f(x) = ax^2 + bx + c$, the vertex occurs at $x = -\frac{b}{2a}$ with extreme value $c - \frac{b^2}{4a}$ (minimum if $a > 0$, maximum if $a < 0$).

### 2. When to Use It (Question Cue)
- *"If $x, y, z > 0$ and $x + y + z = 9$, find the minimum value of $\frac{1}{x} + \frac{4}{y} + \frac{9}{z}$."*

### 3. General Example (Clean Numbers, Single Concept)
> Given positive real numbers $x, y, z$ such that $x + y + z = 9$, find the minimum possible value of $\frac{1}{x} + \frac{4}{y} + \frac{9}{z}$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in (Titu's Lemma)**:
  1. Write numerators as squares: $\frac{1^2}{x} + \frac{2^2}{y} + \frac{3^2}{z}$ ($a_1 = 1, a_2 = 2, a_3 = 3$).
  2. Apply Titu's Lemma:
     $$\frac{1^2}{x} + \frac{2^2}{y} + \frac{3^2}{z} \ge \frac{(1 + 2 + 3)^2}{x + y + z} = \frac{6^2}{9} = \frac{36}{9} = \mathbf{4}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Equality holds when denominators are proportional to $a_i$: $x : y : z = 1 : 2 : 3$.
  2. Scaling $1 : 2 : 3$ to sum to $9$ gives $x = 1.5,\; y = 3,\; z = 4.5$.
  3. Plugging in gives $\frac{1}{1.5} + \frac{4}{3} + \frac{9}{4.5} = \frac{2}{3} + \frac{4}{3} + 2 = \mathbf{4}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Adding the numerators as $(1 + 4 + 9)^2$ instead of taking their **square roots** first: $(\sqrt{1} + \sqrt{4} + \sqrt{9})^2 = (1 + 2 + 3)^2 = 36$.
