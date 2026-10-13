# QA 09: Number System — Divisibility, Factors, HCF/LCM, Remainders, Factorials & Base Systems

**Canonical Taxonomy Mapping**: `QA > Number System > Classification & Properties`, `Divisibility & Factor Theory`, `HCF & LCM Models`, `Remainders & Modular Arithmetic`, `Factorials, Base Systems & Digits`  
**Weightage**: ~8–12% of QA (2–3 questions per slot)  
**Priority Tier**: Tier 1 (High-Yield Core)

---

## 1. 30-Second Concept & Formula Blueprint

### 1.1 Primes, Divisibility & Factor Theory
- **Prime Form ($p > 3$)**:
  - Every prime $p > 3$ is of the form $6k \pm 1$.
  - Consequently, $p^2 - 1 = (p-1)(p+1)$ is ALWAYS divisible by **$24$** ($p^2 \equiv 1 \pmod{24}$).
- **Special Composite & Divisibility Faktors**:
  - $1001 = 7 \times 11 \times 13 \implies \overline{abcabc} = \overline{abc} \times 1001$ is always divisible by $7, 11, 13$.
  - $111 = 3 \times 37$, $10101 = 3 \times 7 \times 13 \times 37$, $999999 = 999 \times 1001$ (divisible by $3, 7, 9, 11, 13, 27, 37$).
  - **Algebraic Divisibility**:
    - $a^n - b^n$ is ALWAYS divisible by $(a - b)$ for all $n \in \mathbb{Z}^+$, and also by $(a + b)$ when $n$ is **even**.
    - $a^n + b^n$ is divisible by $(a + b)$ when $n$ is **odd** (never by $a - b$ for $a, b > 0$).
- **Factor Theory for $N = p_1^a p_2^b p_3^c \dots$** ($p_1 = 2$ if even):
  - **Total Number of Factors**: $d(N) = (a + 1)(b + 1)(c + 1)\dots$ ($d(N)$ is odd iff $N$ is a perfect square).
  - **Sum of Factors**: $\sigma(N) = \left(\frac{p_1^{a+1}-1}{p_1-1}\right)\left(\frac{p_2^{b+1}-1}{p_2-1}\right)\dots$
  - **Product of All Factors**: $N^{d(N)/2}$.
  - **Odd Factors**: Set exponent of $2$ to $0 \implies (b + 1)(c + 1)\dots$; **Even Factors**: $a(b + 1)(c + 1)\dots$
  - **Perfect Square Factors**: $\left(\lfloor \frac{a}{2} \rfloor + 1\right)\left(\lfloor \frac{b}{2} \rfloor + 1\right)\dots$
  - **Ways to Write $N$ as a Product of Two Positive Integers**:
    - Unordered pairs $\{u, v\}$: $\frac{d(N)}{2}$ (if $N$ is not a square) or $\frac{d(N) + 1}{2}$ (if $N$ is a square; $\frac{d(N) - 1}{2}$ if $u \neq v$).
    - **Coprime Pairs $\{u, v\}$ with $\gcd(u, v) = 1$**: $2^{k-1}$, where $k$ is the number of distinct prime factors of $N$.
  - **Ways to Write $N$ as a Difference of Two Squares ($x^2 - y^2 = N, x, y \in \mathbb{Z}^+$)**:
    - Exists iff $N$ is odd ($N > 1$) or a multiple of $4$ ($N > 4$). (Never possible if $N \equiv 2 \pmod 4$!).
    - Since $(x-y)(x+y) = N$ requires both factors to have the **same parity**:
      - If $N$ is odd: Number of unordered non-identical factor pairs of $N$.
      - If $N = 4M$: Number of unordered non-identical factor pairs of $M$.

---

### 1.2 HCF, LCM & Chinese Remainder Models
- **Two-Number Identity**: For $a = Hx, b = Hy$ with $\gcd(x, y) = 1$:
  $$\text{HCF} = H, \quad \text{LCM} = Hxy, \quad H \times L = a \times b$$
- **Fractions**: $\text{HCF} = \frac{\text{HCF}(\text{Numerators})}{\text{LCM}(\text{Denominators})}, \quad \text{LCM} = \frac{\text{LCM}(\text{Numerators})}{\text{HCF}(\text{Denominators})}$ (fractions MUST be in reduced form first!).
- **Three Canonical Remainder Models**:
  1. **Same Remainder $r$** when divided by $d_1, d_2, d_3$: $N = k \cdot \text{LCM}(d_1, d_2, d_3) + r$.
  2. **Constant Difference $d_i - r_i = c$**: $N = k \cdot \text{LCM}(d_1, d_2, d_3) - c$.
  3. **General Case (Chinese Remainder Theorem)**: Find smallest solution $N_0$ by stepping through multiples of the largest divisor, then general solution is $N = k \cdot \text{LCM}(d_1, d_2, \dots) + N_0$.

---

### 1.3 Modular Arithmetic, Factorials & Base Systems
- **Euler's Totient Theorem**: For $\gcd(a, n) = 1$, $a^{\phi(n)} \equiv 1 \pmod n$, where $\phi(n) = n \prod \left(1 - \frac{1}{p_i}\right)$.
- **Fermat's Little Theorem** ($p$ prime, $p \nmid a$): $a^{p-1} \equiv 1 \pmod p$.
- **Wilson's Theorem** ($p$ prime):
  $$(p - 1)! \equiv -1 \equiv p - 1 \pmod p, \qquad (p - 2)! \equiv 1 \pmod p, \qquad (p - 3)! \equiv \frac{p - 1}{2} \pmod p$$
- **Legendre's Formula (Highest Power of Prime $p$ Dividing $n!$)**:
  $$E_p(n!) = \sum_{k=1}^{\infty} \left\lfloor \frac{n}{p^k} \right\rfloor = \frac{n - S_p(n)}{p - 1}$$
  where $S_p(n)$ is the sum of digits of $n$ in base $p$.
  - **Trailing Zeros of $n!$ in Base $B$**: Factor $B = p_1^{\alpha_1} p_2^{\alpha_2} \dots$; then $\text{Zeros} = \min_i \left\lfloor \frac{E_{p_i}(n!)}{\alpha_i} \right\rfloor$ (for base $10$, $\lfloor E_5(n!) \rfloor$).
- **Last Two Digits Shortcut ($\bmod 100$)**:
  - Ends in $1$: $(\dots a1)^{\dots b} \equiv \overline{(a \times b \bmod 10)1}$.
  - Ends in $3, 7, 9$: Raise to power $2$ or $4$ so it ends in $1$, then apply the Ends-in-$1$ rule!
  - Powers of $2$: $2^{10} = 1024 \equiv 24 \pmod{100}$; $24^{\text{odd}} \equiv 24$, $24^{\text{even}} \equiv 76 \pmod{100}$, and $76 \times 2^k \equiv 2^k \pmod{100}$ (for $k \ge 2$).

---

## 2. Pattern-Recognition Trigger Table

| Question Cue / Wording | Hidden Constraint | Fastest Attack Strategy |
| :--- | :--- | :--- |
| "Number of ordered pairs $(x, y) \in \mathbb{Z}^+$ satisfying $\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$" | Equivalent to $(x - n)(y - n) = n^2$ | Number of ordered solutions $= d(n^2)$; unordered pairs $\{x, y\} = \frac{d(n^2) + 1}{2}$ |
| "Remainder when $a^k$ is divided by composite $n = p \cdot q$ where $\gcd(a, n) > 1$" | Cannot apply Euler's theorem directly before cancelling common factor! | Cancel common factor $g = \gcd(a^k, n)$ from both dividend and divisor, find remainder $r'$ modulo $n/g$, then multiply final remainder back by $g$: $R = g \cdot r'$ |
| "100 Lockers / Bulbs toggled by every divisor $1, 2, \dots, 100$" | Locker $k$ is toggled $d(k)$ times | Remains open iff $d(k)$ is odd $\iff k$ is a **perfect square** ($\lfloor \sqrt{100} \rfloor = 10$ lockers) |
| "For how many integers $n$ does $n!$ have $k$ trailing zeros?" | $E_5(n!)$ jumps by $+2$ (or $+3$) at multiples of $25$ (or $125$)! | Either **5 consecutive integers** ($5m, \dots, 5m+4$) or **0 integers** if $k$ is skipped at a multiple of $25$ (e.g., $k = 5, 11, 17, 23, 29, 30$ are skipped!) |
| "Number in base $B$ is $\overline{abc}_B$; check divisibility by $(B - 1)$ or $(B + 1)$" | $(B - 1)$ works like $9$ in base $10$; $(B + 1)$ works like $11$ in base $10$ | Divisible by $(B-1)$ iff sum of digits $a+b+c$ is divisible by $(B-1)$; by $(B+1)$ iff alternating sum $c - b + a$ is divisible by $(B+1)$ |

---

## 3. Canonical CAT Archetypes & Solved Exemplars

### Archetype 1: Remainder via Common-Factor Cancellation
> **Problem**: Find the remainder when $2^{96}$ is divided by $96$.

- **First-Principles Method / Speed Shortcut**:
  1. Factor $96 = 32 \times 3 = 2^5 \times 3$.
  2. Cancel the common factor $g = 2^5 = 32$ from both $2^{96}$ and $96$:
     $$\frac{2^{96}}{96} = \frac{2^{91}}{3}$$
  3. Find the remainder of $2^{91} \pmod 3$:
     $$2^{91} \equiv (-1)^{91} \equiv -1 \equiv 2 \pmod 3$$
  4. Multiply the reduced remainder $r' = 2$ back by the cancelled factor $g = 32$:
     $$\text{True Remainder } R = 32 \times 2 = \mathbf{64}$$

---

### Archetype 2: Trailing Zeros in Non-Decimal Base
> **Problem**: Find the number of trailing zeros when $100!$ is written in base $12$.

- **First-Principles Method**:
  1. Prime factorize the base: $12 = 2^2 \times 3^1$.
  2. Compute $E_2(100!)$ and $E_3(100!)$ using Legendre's formula:
     $$E_3(100!) = \lfloor 100/3 \rfloor + \lfloor 100/9 \rfloor + \lfloor 100/27 \rfloor + \lfloor 100/81 \rfloor = 33 + 11 + 3 + 1 = 48$$
     $$E_2(100!) = 50 + 25 + 12 + 6 + 3 + 1 = 97$$
  3. Number of complete $12 = 2^2 \times 3^1$ groups is:
     $$\min\left(\left\lfloor \frac{E_2(100!)}{2} \right\rfloor,\; \frac{E_3(100!)}{1}\right) = \min\left(\left\lfloor \frac{97}{2} \right\rfloor,\; 48\right) = \min(48, 48) = \mathbf{48\text{ zeros}}$$

- **30-Second Exam-Hall Speed Shortcut**:
  - Usually the largest prime factor of $B$ limits $E_p(n!)$, EXCEPT when a smaller prime has a high exponent (like $12 = 2^2 \times 3$ or $24 = 2^3 \times 3$). Always check both $\lfloor E_2/\alpha_2 \rfloor$ and $\lfloor E_3/\alpha_3 \rfloor$!

---

### Archetype 3: Counting Ordered Pairs in $\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$
> **Problem**: How many ordered pairs of positive integers $(x, y)$ satisfy $\frac{1}{x} + \frac{1}{y} = \frac{1}{12}$?

- **First-Principles Method**:
  1. Clear fractions: $12(x + y) = xy \iff xy - 12x - 12y = 0 \iff (x - 12)(y - 12) = 144$.
  2. Since $x, y > 12$ for positive unit fractions, $(x - 12)$ can be any positive factor of $144 = 2^4 \times 3^2$.
  3. Total number of ordered pairs $(x, y) = d(144) = (4 + 1)(2 + 1) = \mathbf{15\text{ pairs}}$.

- **30-Second Exam-Hall Speed Shortcut**:
  - Memorize: For $\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$, ordered positive integer solutions $= d(n^2)$; if all integer solutions $(x, y \neq 0)$ are allowed, $= 2 \cdot d(n^2) - 1$ (subtracting $x = y = 0$).

---

## 4. Boundary Conditions, Domain Traps & TITA Pitfalls

1. **HCF/LCM Product Trap for 3 or More Numbers**:
   - $\text{HCF}(a, b, c) \times \text{LCM}(a, b, c) \neq a \cdot b \cdot c$! The product law holds strictly for **two** numbers (unless all three are pairwise coprime).
2. **Negative Remainders Must Be Converted Back to $[0, d-1]$**:
   - If your modular arithmetic gives $-17 \pmod{23}$, the CAT TITA answer is $23 - 17 = 6$, never $-17$.
3. **Skipped Values of Trailing Zeros in $n!$**:
   - $24!$ has $4$ zeros and $25!$ jumps directly to $6$ zeros. There is **no** integer $n$ for which $n!$ ends in $5$ zeros!

---

## 5. Active-Recall Drill (10 Prompts)

<details><summary>Q1: Find the number of even factors and perfect-square factors of N = 2^5 * 3^4 * 5^2.</summary>
A: Even factors = 5 * (4 + 1) * (2 + 1) = 75. Perfect-square factors = (floor(5/2) + 1) * (floor(4/2) + 1) * (floor(2/2) + 1) = 3 * 3 * 2 = 18.
</details>

<details><summary>Q2: In how many ways can 720 be written as a product of two coprime positive integers {a, b}?</summary>
A: Prime factorization: 720 = 2^4 * 3^2 * 5^1 has k = 3 distinct prime factors. Number of unordered coprime pairs = 2^(k-1) = 2^2 = 4.
</details>

<details><summary>Q3: Find the remainder when 29! is divided by 31.</summary>
A: Since 31 is prime, by Wilson's Theorem (p - 2)! === 1 (mod p). Here 29 = 31 - 2, so 29! === 1 (mod 31). Remainder = 1.
</details>

<details><summary>Q4: Find the last two digits of 7^2024.</summary>
A: 7^4 = 2401 === 01 (mod 100). Since 2024 is a multiple of 4 (2024 = 4 * 506), 7^2024 = (7^4)^506 === 01^506 === 01 (mod 100).
</details>

<details><summary>Q5: Find the smallest four-digit number which when divided by 5, 6, and 8 leaves remainders 3, 4, and 6 respectively.</summary>
A: Constant difference d_i - r_i = 2. LCM(5, 6, 8) = 120. General form = 120k - 2. For smallest 4-digit number, k = 9 gives 120(9) - 2 = 1078.
</details>

<details><summary>Q6: If HCF(a, b) = 15 and a + b = 150, how many unordered pairs of positive integers {a, b} exist?</summary>
A: Let a = 15x, b = 15y with gcd(x, y) = 1. Then x + y = 10. Coprime pairs {x, y} summing to 10 are {1, 9} and {3, 7} -> 2 pairs.
</details>

<details><summary>Q7: How many positive integer pairs (x, y) satisfy x^2 - y^2 = 120?</summary>
A: Since 120 = 4 * 30 is a multiple of 4, count non-identical factor pairs of M = 30 = 2 * 3 * 5. d(30) = 8 -> 8 / 2 = 4 pairs.
</details>

<details><summary>Q8: Find the remainder when 16^3 + 17^3 + 18^3 + 19^3 is divided by 70.</summary>
A: Pair (16^3 + 19^3) and (17^3 + 18^3): both are divisible by (16 + 19) = 35. Also there are two odd and two even cubes, so the sum is even (divisible by 2). Since gcd(2, 35) = 1, the sum is divisible by 70 -> Remainder = 0.
</details>

<details><summary>Q9: Find the highest power of 2 that divides 128!.</summary>
A: Since 128 = 2^7 has sum of binary digits S_2(128) = 1, E_2(128!) = (128 - 1)/(2 - 1) = 127.
</details>

<details><summary>Q10: Convert the recurring decimal 0.2353535... (where 35 repeats) into a reduced fraction.</summary>
A: (235 - 2) / 990 = 233 / 990.
</details>
