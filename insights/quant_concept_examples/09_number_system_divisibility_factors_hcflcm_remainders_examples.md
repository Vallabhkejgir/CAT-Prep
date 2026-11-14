# QA 09 Concept & Formula Examples: Divisibility, Factors, HCF/LCM, Remainders, Factorials & Base Systems

> **Companion Reference**: [`../topic_summaries/quant/09_number_system_divisibility_factors_hcflcm_remainders_bases.md`](../topic_summaries/quant/09_number_system_divisibility_factors_hcflcm_remainders_bases.md) | [`QA_Formula_and_Trigger_Book.md`](../high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md)

Every concept, formula, and pattern trigger from **QA 09** is explained below with plain-English intuition, clean single-concept numbers, a two-way walkthrough (direct formula vs. mental ratio intuition), and the #1 mistake to avoid.

---

## Concept 1: Prime Form $6k \pm 1$ ($p^2 \equiv 1 \pmod{24}$), Special Divisibility ($1001$) & Algebraic Divisibility ($a^n \pm b^n$)

### 1. Concept & Formula in Plain English
1. **Primes $> 3$ ($p = 6k \pm 1 \implies p^2 - 1$ is a multiple of $24$)**: Since any prime $p > 3$ is neither even nor a multiple of $3$, $(p - 1)$ and $(p + 1)$ are two consecutive even numbers (contributing $2 \times 4 = 8$), and one of the three consecutive integers $(p - 1), p, (p + 1)$ must be a multiple of $3$. Thus **$p^2 - 1$ is ALWAYS divisible by $8 \times 3 = 24$**!
2. **Magic Composite $1001 = 7 \times 11 \times 13$**: Repeating any 3-digit number twice ($\overline{abcabc} = \overline{abc} \times 1001$) makes it automatically divisible by **$7, 11,$ and $13$**.
3. **Algebraic Binomial Divisibility**:
   - $a^n - b^n$ is ALWAYS divisible by $(a - b)$, and also by $(a + b)$ when $n$ is **even**.
   - $a^n + b^n$ is divisible by $(a + b)$ when $n$ is **odd** (never by $a - b$).

### 2. When to Use It (Question Cue)
- *"If $p$ is a prime greater than $3$, what is the remainder when $p^2 + 17$ is divided by $24$?"*
- *"Find the remainder when $15^{23} + 23^{23}$ is divided by $19$."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) If $p$ is any prime number greater than $3$, find the remainder when $p^2 + 19$ is divided by $24$.
> (b) Find the remainder when $15^{23} + 23^{23}$ is divided by $19$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: Since $p > 3$ is prime, $p^2 \equiv 1 \pmod{24}$. Therefore:
     $$p^2 + 19 \equiv 1 + 19 = \mathbf{20 \pmod{24}}$$
  2. **Part (b)**: Since the exponent $n = 23$ is odd, $15^{23} + 23^{23}$ is divisible by $(15 + 23) = 38 = 2 \times 19$. Since $38$ is a multiple of $19$, the remainder is $\mathbf{0}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), plug the smallest prime $> 3$, namely $p = 5$: $5^2 + 19 = 44 = 24(1) + \mathbf{20}$. (Try $p = 7$: $49 + 19 = 68 = 24(2) + \mathbf{20}$!)

### 5. The 1 Common Mistake to Avoid
- **Trap**: Applying $p^2 \equiv 1 \pmod{24}$ to $p = 2$ or $p = 3$ (it holds **strictly for primes $p \ge 5$**!).

---

## Concept 2: Counting, Summing & Multiplying Factors ($d(N), \sigma(N), N^{d(N)/2}$) & Restricted Divisors

### 1. Concept & Formula in Plain English
Given the prime factorization $N = 2^a \cdot p^b \cdot q^c$:
- **Total Number of Factors $d(N)$**: Every factor picks an exponent from $\{0, 1, \dots, a\}$ for $2$ ($a+1$ choices), $\{0, \dots, b\}$ for $p$ ($b+1$ choices), etc.:
  $$d(N) = (a + 1)(b + 1)(c + 1)$$
  *(Note: $d(N)$ is **odd** if and only if all exponents $a, b, c$ are even $\iff N$ is a **perfect square**!)*
- **Odd Factors**: Force the power of $2$ to be $2^0$ ($1$ choice): $(b + 1)(c + 1)$.
- **Even Factors**: Force the power of $2$ to be $\ge 1$ ($a$ choices): $a(b + 1)(c + 1)$.
- **Perfect Square Factors**: Only pick even exponents $\{0, 2, 4, \dots\}$: $\left(\lfloor \frac{a}{2} \rfloor + 1\right)\left(\lfloor \frac{b}{2} \rfloor + 1\right)\left(\lfloor \frac{c}{2} \rfloor + 1\right)$.
- **Sum of Factors $\sigma(N)$**: $\left(\frac{2^{a+1}-1}{2-1}\right)\left(\frac{p^{b+1}-1}{p-1}\right)\left(\frac{q^{c+1}-1}{q-1}\right)$.
- **Product of Factors**: Pair smallest and largest factors (each pair multiplies to $N$): $\mathbf{N^{d(N)/2}}$.

### 2. When to Use It (Question Cue)
- *"For $N = 360$, find the total number of factors, odd factors, even factors, perfect-square factors, and sum of factors."*

### 3. General Example (Clean Numbers, Single Concept)
> For $N = 72 = 2^3 \times 3^2$, find:
> (a) Total factors $d(72)$,
> (b) Odd factors and Even factors,
> (c) Perfect-square factors, and
> (d) Sum of all factors $\sigma(72)$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Exponents are $a = 3$ (for prime $2$) and $b = 2$ (for prime $3$).
  2. **Total factors**: $(3 + 1)(2 + 1) = 4 \times 3 = \mathbf{12}$.
  3. **Odd factors**: $1 \times (2 + 1) = \mathbf{3}$; **Even factors**: $3 \times (2 + 1) = \mathbf{9}$.
  4. **Perfect-square factors**: $(\lfloor 3/2 \rfloor + 1)(\lfloor 2/2 \rfloor + 1) = (1 + 1)(1 + 1) = \mathbf{4}$ ($\{1, 4, 9, 36\}$).
  5. **Sum of factors**: $(1 + 2 + 4 + 8)(1 + 3 + 9) = 15 \times 13 = \mathbf{195}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Expanding $(2^0 + 2^1 + 2^2 + 2^3)(3^0 + 3^1 + 3^2)$ creates $4 \times 3 = 12$ cross-terms that are literally all $12$ divisors of $72$!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Multiplying $a \times b \times c$ instead of $(a + 1)(b + 1)(c + 1)$ (forgetting the $p^0 = 1$ choice for each prime!).

---

## Concept 3: Coprime Factor Pairs ($2^{k-1}$), Difference of Squares ($x^2 - y^2 = N$) & Unit Fractions ($\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$)

### 1. Concept & Formula in Plain English
1. **Unordered Coprime Factor Pairs $\{u, v\}$ with $u \cdot v = N$ and $\gcd(u, v) = 1$**: You cannot split a prime power $p_i^{\alpha_i}$ between $u$ and $v$ (or else both would share factor $p_i$!). Each of the $k$ distinct prime blocks goes entirely to $u$ or entirely to $v$, giving $\frac{2^k}{2} = \mathbf{2^{k-1}}$ unordered pairs.
2. **Writing $N = x^2 - y^2 = (x - y)(x + y)$ ($x, y \in \mathbb{Z}^+$)**: Since $(x - y) + (x + y) = 2x$ is even, $N$ must be factored into two distinct divisors $u < v$ of the **same parity** (both odd, or both even $\implies N$ is odd or a multiple of $4$).
3. **Unit Fraction Equation $\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$ ($x, y \in \mathbb{Z}^+$)**: Rewrites as $(x - n)(y - n) = n^2$, so the number of ordered positive integer pairs $(x, y)$ is simply **$d(n^2)$**!

### 2. When to Use It (Question Cue)
- *"In how many ways can $180$ be written as a product of two coprime numbers?"*
- *"How many ordered pairs of positive integers $(x, y)$ satisfy $\frac{1}{x} + \frac{1}{y} = \frac{1}{6}$?"*

### 3. General Example (Clean Numbers, Single Concept)
> (a) In how many ways can $N = 180$ be expressed as a product of two coprime positive integers?
> (b) How many ordered pairs of positive integers $(x, y)$ satisfy $\frac{1}{x} + \frac{1}{y} = \frac{1}{6}$?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: $180 = 2^2 \times 3^2 \times 5^1$ has $k = 3$ distinct prime factors ($2, 3, 5$).
     Number of unordered coprime pairs $= 2^{k-1} = 2^{3-1} = \mathbf{4\text{ ways}}$.
  2. **Part (b)**: Here $n = 6 \implies n^2 = 36 = 2^2 \times 3^2$.
     Number of ordered pairs $= d(36) = (2 + 1)(2 + 1) = \mathbf{9\text{ pairs}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), the $3$ prime blocks of $180$ are $\{4, 9, 5\}$. The $4$ ways to split them into two coprime piles are: $\{1, 180\}, \{4, 45\}, \{9, 20\}, \{5, 36\}$.
  2. In (b), clear fractions: $6(x + y) = xy \implies (x - 6)(y - 6) = 36$, and $36$ has $9$ positive divisors!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using $d(n)$ instead of **$d(n^2)$** for $\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$ (for $n = 6$, $d(6) = 4$, whereas the true count is $d(36) = 9$!).

---

## Concept 4: HCF & LCM Parameterization ($a = Hx, b = Hy$) & HCF/LCM of Fractions

### 1. Concept & Formula in Plain English
Whenever two positive integers $a$ and $b$ have $\text{HCF}(a, b) = H$, immediately write them as:
$$a = Hx, \quad b = Hy \quad \text{where } \gcd(x, y) = 1 \text{ (coprime!)}$$
Then their LCM is $L = Hxy$, and $a \times b = H \times L$.
For **reduced fractions** $\frac{n_i}{d_i}$:
$$\text{HCF of Fractions} = \frac{\text{HCF of Numerators}}{\text{LCM of Denominators}}, \qquad \text{LCM of Fractions} = \frac{\text{LCM of Numerators}}{\text{HCF of Denominators}}$$

### 2. When to Use It (Question Cue)
- *"The HCF of two numbers is $12$ and their sum is $84$ (or their LCM is $144$). How many such pairs exist?"*

### 3. General Example (Clean Numbers, Single Concept)
> The HCF of two positive integers is $12$ and their sum is $84$. How many unordered pairs of such integers exist?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Write the numbers as $a = 12x$ and $b = 12y$ with $\gcd(x, y) = 1$.
  2. Substitute into $a + b = 84$:
     $$12x + 12y = 84 \implies x + y = 7$$
  3. List unordered pairs $\{x, y\}$ of positive integers summing to $7$ with $\gcd(x, y) = 1$:
     - $\{1, 6\} \implies \{12, 72\}$ ($\gcd = 1$, valid)
     - $\{2, 5\} \implies \{24, 60\}$ ($\gcd = 1$, valid)
     - $\{3, 4\} \implies \{36, 48\}$ ($\gcd = 1$, valid)
  4. Total $= \mathbf{3\text{ pairs}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Since $7$ is prime, every positive integer split of $7$ ($1+6, 2+5, 3+4$) is automatically coprime!

### 5. The 1 Common Mistake to Avoid
- **Trap**: If $x + y = 8$, forgetting to **discard non-coprime pairs** like $\{2, 6\}$ and $\{4, 4\}$ (where $\gcd(x, y) > 1$, which would raise the HCF above $12$!).

---

## Concept 5: The 3 Canonical Remainder Models (Same Remainder, Constant Difference & CRT)

### 1. Concept & Formula in Plain English
When finding numbers $N$ that leave specific remainders when divided by $d_1, d_2, d_3$:
1. **Model 1 — Same Remainder $r$** ($N \equiv r \pmod{d_i}$):
   $$N = k \cdot \text{LCM}(d_1, d_2, d_3) + r$$
2. **Model 2 — Constant Difference $c = d_i - r_i$** ($N \equiv -c \pmod{d_i}$):
   $$N = k \cdot \text{LCM}(d_1, d_2, d_3) - c$$
3. **Model 3 — General Case (Chinese Remainder Theorem)**: Step through multiples of the **largest divisor** ($m \cdot d_{\max} + r_{\max}$) until you find the first number $N_0$ that satisfies the other divisors, then:
   $$N = k \cdot \text{LCM}(d_1, d_2, \dots) + N_0$$

### 2. When to Use It (Question Cue)
- *"Find the smallest number which when divided by $4, 5,$ and $6$ leaves remainders $2, 3,$ and $4$ respectively."*
- *"Find the smallest number that leaves remainder $1$ when divided by $5$ and remainder $3$ when divided by $7$."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) Find the smallest positive integer which when divided by $4, 5,$ and $6$ leaves remainders $2, 3,$ and $4$ respectively.
> (b) Find the smallest positive integer which leaves remainder $1$ when divided by $5$ and remainder $3$ when divided by $7$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a) Constant Difference**: Notice $4 - 2 = 2$, $5 - 3 = 2$, $6 - 4 = 2$ (constant difference $c = 2$).
     $\text{LCM}(4, 5, 6) = 60 \implies N = 60(1) - 2 = \mathbf{58}$.
  2. **Part (b) CRT Stepping**: Start with the larger divisor $7$: numbers leaving remainder $3 \pmod 7$ are $3, 10, 17, 24, 31, \dots$
     Check $\pmod 5$: $3 \equiv 3$; $10 \equiv 0$; $17 \equiv 2$; $24 \equiv 4$; $31 \equiv 1 \pmod 5$ (Match!). Smallest $N_0 = \mathbf{31}$ (general form $35k + 31$).
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), adding $2$ to $N$ makes $N + 2$ perfectly divisible by $4, 5,$ and $6$, so $N + 2 = 60 \implies N = \mathbf{58}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Writing $N = \text{LCM} + c = 62$ instead of $\text{LCM} - c = 58$ in the constant-difference model!

---

## Concept 6: Common-Factor Cancellation in Remainders, Euler's Totient & Fermat's Little Theorem

### 1. Concept & Formula in Plain English
1. **Common-Factor Cancellation Rule**: If dividend $A$ and divisor $D$ share a common factor $g$, you can divide both by $g$, find the remainder $r'$ of $\frac{A}{g} \pmod{\frac{D}{g}}$, and then **multiply the remainder back by $g$**:
   $$\text{True Remainder} = g \times r'$$
2. **Fermat's Little Theorem** ($p$ prime, $p \nmid a$): $a^{p-1} \equiv 1 \pmod p$.
3. **Euler's Totient Theorem** ($\gcd(a, n) = 1$): $a^{\phi(n)} \equiv 1 \pmod n$, where $\phi(n) = n\prod\left(1 - \frac{1}{p_i}\right)$.

### 2. When to Use It (Question Cue)
- *"Find the remainder when $2^{50}$ is divided by $24$."*
- *"Find the remainder when $3^{100}$ is divided by $7$."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) Find the remainder when $2^{50}$ is divided by $24$.
> (b) Find the remainder when $3^{100}$ is divided by $7$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: Factor $24 = 8 \times 3 = 2^3 \times 3$. Cancel $g = 2^3 = 8$:
     $$\frac{2^{50}}{24} = \frac{2^{47}}{3}$$
     Modulo $3$: $2^{47} \equiv (-1)^{47} = -1 \equiv 2 \pmod 3$, so $r' = 2$.
     Multiply back by $g = 8$: True Remainder $= 8 \times 2 = \mathbf{16}$.
  2. **Part (b)**: By Fermat's Little Theorem with prime $p = 7$, $3^6 \equiv 1 \pmod 7$.
     Since $100 = 6(16) + 4$, $3^{100} \equiv 3^4 = 81 = 7(11) + 4 \equiv \mathbf{4 \pmod 7}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), powers of $2$ modulo $24$ cycle for $n \ge 3$: $2^3 = 8$, $2^4 = 16$, $2^5 = 32 \equiv 8$, $2^6 = 64 \equiv 16, \dots$ Every odd power $\ge 3$ leaves $8$, and every even power $\ge 4$ leaves $\mathbf{16}$!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Cancelling $g = 8$ to get $r' = 2$ and reporting $2$ as the final answer instead of multiplying back by the cancelled factor ($8 \times 2 = 16$).

---

## Concept 7: Wilson's Factorial Remainder Theorem

### 1. Concept & Formula in Plain English
Whenever a factorial is divided by a **prime number $p$** just above it, every integer from $2$ to $p - 2$ pairs up with its modular inverse so their product is $1 \pmod p$:
1. $(p - 1)! \equiv -1 \equiv \mathbf{p - 1 \pmod p}$
2. $(p - 2)! \equiv \mathbf{1 \pmod p}$
3. $(p - 3)! \equiv \mathbf{\frac{p - 1}{2} \pmod p}$

### 2. When to Use It (Question Cue)
- *"Find the remainder when $16!$ is divided by $17$ (or $15!$ is divided by $17$)."*

### 3. General Example (Clean Numbers, Single Concept)
> Find the remainders when $16!$, $15!$, and $14!$ are each divided by the prime number $17$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $p = 17$ is prime.
  2. $16! = (17 - 1)! \equiv p - 1 = \mathbf{16 \pmod{17}}$.
  3. $15! = (17 - 2)! \equiv \mathbf{1 \pmod{17}}$.
  4. $14! = (17 - 3)! \equiv \frac{17 - 1}{2} = \mathbf{8 \pmod{17}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Since $16! = 16 \times 15! \equiv (-1) \times 15! \equiv -1 \pmod{17}$, cancelling $(-1)$ gives $15! \equiv 1 \pmod{17}$.
  2. Next, $15 \times 14! \equiv (-2) \times 14! \equiv 1 \equiv 18 \pmod{17} \implies 14! \equiv -9 \equiv \mathbf{8 \pmod{17}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Applying Wilson's Theorem when the modulus $n$ is **composite** (for composite $n > 4$, $(n - 1)! \equiv 0 \pmod n$, NOT $n - 1$!).

---

## Concept 8: Legendre's Formula for $E_p(n!)$ & Trailing Zeros of $n!$ in Base $10$ and Base $B$

### 1. Concept & Formula in Plain English
To find the highest power of a prime $p$ that divides $n!$ (denoted $E_p(n!)$), repeatedly divide $n$ by $p$ and add the integer quotients:
$$E_p(n!) = \left\lfloor \frac{n}{p} \right\rfloor + \left\lfloor \frac{n}{p^2} \right\rfloor + \left\lfloor \frac{n}{p^3} \right\rfloor + \dots = \frac{n - S_p(n)}{p - 1}$$
- **Trailing Zeros in Base $10$**: Each trailing zero comes from $10 = 2 \times 5$. Since $5$s are scarcer than $2$s in $n!$, the number of trailing zeros is simply **$E_5(n!)$**.
- **Trailing Zeros in Base $B = p_1^{\alpha_1} p_2^{\alpha_2}$**: Compute $\min\left(\left\lfloor \frac{E_{p_1}(n!)}{\alpha_1} \right\rfloor,\; \left\lfloor \frac{E_{p_2}(n!)}{\alpha_2} \right\rfloor\right)$.

### 2. When to Use It (Question Cue)
- *"Find the number of trailing zeros at the end of $100!$ in base $10$ (or in base $18$)."*

### 3. General Example (Clean Numbers, Single Concept)
> Find the number of trailing zeros at the end of $60!$ when written in:
> (a) standard decimal base $10$, and
> (b) base $9$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a) Base $10 = 2 \times 5$**:
     $$E_5(60!) = \left\lfloor \frac{60}{5} \right\rfloor + \left\lfloor \frac{60}{25} \right\rfloor = 12 + 2 = \mathbf{14\text{ zeros}}$$
  2. **Part (b) Base $9 = 3^2$**:
     First find $E_3(60!) = \lfloor 60/3 \rfloor + \lfloor 60/9 \rfloor + \lfloor 60/27 \rfloor = 20 + 6 + 2 = 28$.
     Since each $9$ needs **two** $3$s ($3^2$), trailing zeros in base $9$ $= \left\lfloor \frac{28}{2} \right\rfloor = \mathbf{14\text{ zeros}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In $1 \times 2 \times \dots \times 60$, the $12$ multiples of $5$ each supply one $5$, and the $2$ multiples of $25$ ($25$ and $50$) each supply an **extra** $5$, giving $12 + 2 = \mathbf{14}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting to divide $E_p(n!)$ by the prime's exponent $\alpha$ when the base contains a prime power like $9 = 3^2$, $12 = 2^2 \times 3$, or $24 = 2^3 \times 3$.

---

## Concept 9: Last Two Digits ($\bmod 100$) Shortcuts & Base System Divisibility by $(B - 1)$ and $(B + 1)$

### 1. Concept & Formula in Plain English
1. **Last Two Digits ($\bmod 100$)**:
   - **Number ending in $1$**: The units digit is always $1$, and the tens digit is the units digit of $(\text{tens digit of base}) \times (\text{units digit of exponent})$:
     $$(\dots a1)^{\dots b} \equiv \overline{(a \times b \bmod 10)1} \pmod{100}$$
   - **Number ending in $3, 7, 9$**: Raise to power $2$ or $4$ first so it ends in $1$ ($3^4 = 81$, $7^4 = 2401 \equiv 01$, $9^2 = 81$).
2. **Base-$B$ Divisibility Rules**:
   - **$(B - 1)$ Rule** (like $9$ in base $10$): A base-$B$ number is divisible by $(B - 1)$ iff the **sum of its digits** is divisible by $(B - 1)$.
   - **$(B + 1)$ Rule** (like $11$ in base $10$): Divisible by $(B + 1)$ iff the **alternating sum of its digits** is divisible by $(B + 1)$.

### 2. When to Use It (Question Cue)
- *"Find the last two digits of $31^{47}$ (or $3^{82}$)."*
- *"Find the remainder when $(12345)_8$ is divided by $7$."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) Find the last two digits of $31^{47}$.
> (b) Find the remainder when the base-$8$ number $(2345)_8$ is divided by $7$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: Base ends in $1$ with tens digit $a = 3$, and exponent ends in $b = 7$.
     Tens digit $= (3 \times 7) \bmod 10 = 21 \bmod 10 = 1$; Units digit $= 1 \implies \mathbf{11}$.
  2. **Part (b)**: Since $7 = 8 - 1 = B - 1$, the remainder modulo $7$ equals the sum of the base-$8$ digits modulo $7$:
     $$2 + 3 + 4 + 5 = 14 \equiv \mathbf{0 \pmod 7}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), write $31^{47} = (1 + 30)^{47} \equiv 1 + 47(30) = 1 + 1410 \equiv \mathbf{11 \pmod{100}}$ by Binomial Theorem!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Multiplying the tens digit of the base by the *tens* digit of the exponent instead of the **units digit of the exponent** ($3 \times 7$, not $3 \times 4$).

---

## Concept 10: Recurring Decimals to Fractions & Decimal Borrow Propagation ($10^m + 10^n - k$)

### 1. Concept & Formula in Plain English
1. **Recurring Decimal Conversion**: To convert $0.a\overline{bc}$ (where $a$ does not repeat and $bc$ repeats) into a fraction:
   - **Numerator**: $(\text{Entire digits } abc) - (\text{Non-repeating digits } a)$.
   - **Denominator**: Put one `$9$` for each repeating digit followed by one `$0$` for each non-repeating decimal digit:
     $$0.a\overline{bc} = \frac{abc - a}{990}$$
2. **Decimal Borrow Propagation in $10^n - k$**: When a $d$-digit number $k$ is subtracted from $10^n$ ($n > d$), the result has **$n$ digits total**: the first $(n - d)$ digits are all **`9`s**, followed by the $d$-digit complement $(10^d - k)$!

### 2. When to Use It (Question Cue)
- *"Express $0.1\overline{25}$ as a fraction in lowest terms."*
- *"Find the sum of the digits of $10^{30} - 45$."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) Convert $0.1\overline{25}$ ($0.1252525\dots$) into a fraction.
> (b) Find the sum of all digits of the integer $10^{20} - 36$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: Numerator $= 125 - 1 = 124$. Denominator has two `9`s (for `25`) and one `0` (for `1`) $= 990$:
     $$0.1\overline{25} = \frac{124}{990} = \mathbf{\frac{62}{495}}$$
  2. **Part (b)**: Here $n = 20$ and $k = 36$ ($d = 2$ digits).
     $10^{20} - 36$ has $(20 - 2) = 18$ nines followed by $100 - 36 = 64$.
     Sum of digits $= 18 \times 9 + 6 + 4 = 162 + 10 = \mathbf{172}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), let $x = 0.12525\dots \implies 10x = 1.2525\dots$ and $1000x = 125.2525\dots \implies 990x = 124 \implies x = \mathbf{\frac{62}{495}}$.
  2. In (b), test small $n = 3$: $10^3 - 36 = 964$ (which has $3 - 2 = 1$ nine followed by $64$). So $n = 20$ has $18$ nines followed by $64$!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Putting $20$ nines instead of **$(20 - 2) = 18$ nines** when subtracting a 2-digit number from $10^{20}$.
