# Last-Mile Rapid-Revision Cheat Sheet: QA Formula & Trigger Book

Ultra-dense, single-pass reference of every high-yield CAT Quantitative Ability formula, identity, number triplet, and **`IF YOU SEE [X] -> IMMEDIATELY DO [Y]`** trigger.

---

## 1. Arithmetic Rapid Formulas & Triggers

| Sub-Topic | Core Formula / Identity | Exam-Hall Speed Trigger (`See X -> Do Y`) |
| :--- | :--- | :--- |
| **Successive % Change** | $\left(a + b + \frac{ab}{100}\right)\%$ | $+x\%$ then $-x\%$ is ALWAYS a net loss of $\left(\frac{x}{10}\right)^2\%$ |
| **Product Constancy ($A \times B = k$)** | $A \uparrow \text{ by } \frac{a}{b} \implies B \downarrow \text{ by } \frac{a}{b+a}$ | Price $\uparrow 25\% (1/4) \implies$ Consumption $\downarrow 20\% (1/5)$ |
| **CP : MP Ratio** | $\frac{\text{CP}}{\text{MP}} = \frac{100 - d}{100 + p}$ | Instant ratio without finding SP |
| **Dishonest Scale MF** | $\text{MF} = \frac{\text{Price Charged}}{\text{Cost}} \times \frac{\text{True Weight Claimed}}{\text{Actual Weight Dispensed}}$ | Giving $800\text{ g}$ for $1\text{ kg}$ is $\frac{1000}{800} = +25\%$ profit |
| **CI - SI Difference** | 2 Yr: $Pr^2$; 3 Yr: $Pr^2(3 + r)$ | Ratio $\frac{\text{Diff}_3}{\text{Diff}_2} = 3 + r = 3 + \frac{R}{100}$ |
| **Equal CI Installment ($X$)** | $P = \sum_{k=1}^n \frac{X}{(1+r)^k}$ | For 2 yrs at $10\%$: $P : X = (110 + 100) : 121 = 210 : 121$ |
| **Alligation Lever Rule** | $\frac{n_1}{n_2} = \frac{A_2 - A_{\text{avg}}}{A_{\text{avg}} - A_1}$ | Ratio $n_1:n_2$ is ALWAYS the ratio of the **denominator units** |
| **Repeated Replacement** | $C_{\text{final}} = C_0 \left(1 - \frac{x}{V}\right)^n$ | Track ONLY the undiluted liquid as a fraction of **Total Volume** |
| **Vessel Equilibrium Swap** | $x^* = \frac{V_A V_B}{V_A + V_B}$ | Volume swapped so both vessels reach identical concentration |
| **Extra Time Over Combined** | $T_{AB} = \sqrt{a \cdot b}$ | $A$ takes $a$ more, $B$ takes $b$ more than $(A+B)$ together |
| **Post-Meeting Times ($t_A, t_B$)** | $\frac{S_A}{S_B} = \sqrt{\frac{t_B}{t_A}}, \quad t_{\text{meet}} = \sqrt{t_A t_B}$ | Use whenever "after meeting, A and B take $t_A, t_B$ to finish" |
| **Escalator Steps ($N$)** | $N = S_{\text{person}} \pm e \cdot t$ | $+$ when walking **with** escalator; $-$ when walking **against** |
| **Circular Track ($\frac{v_1}{v_2} = \frac{a}{b}$ coprime)** | Distinct points $= |a \mp b|$ | $-$ for Same Direction, $+$ for Opposite Direction (reduce $\frac{v_1}{v_2}$ first!) |

---

## 2. Algebra Rapid Formulas & Triggers

| Sub-Topic | Core Formula / Identity | Exam-Hall Speed Trigger (`See X -> Do Y`) |
| :--- | :--- | :--- |
| **Frobenius Coin Theorem** | Max unattainable $= ab - a - b$ ($x,y \ge 0$) | For $x, y \ge 1$: Max unattainable $= ab$; count $= \frac{(a-1)(b-1)}{2}$ |
| **Simon's Factoring Trick** | $xy + ax + by = c \iff (x+b)(y+a) = c + ab$ | Add $ab$ to both sides and count divisor pairs of $(c+ab)$ |
| **Quadratic Always $> 0$** | $a > 0$ AND $\Delta = b^2 - 4ac < 0$ | Also check degenerate $a = 0$ if "quadratic" is not specified! |
| **Root Between $k$** | $a \cdot f(k) < 0$ | Guarantees $\alpha < k < \beta$ in a single inequality |
| **Sum of Modulus $\sum |x - a_i|$** | Minimum at **Median** of $\{a_i\}$ | Odd $n$: unique $x$; Even $n$: flat minimum on $[a_{n/2}, a_{n/2+1}]$ |
| **Modulus Equality** | $|A| + |B| = |A + B| \iff A \cdot B \ge 0$ | $|A| + |B| = |A - B| \iff A \cdot B \le 0$ |
| **Diamond Area $|x| + |y| \le r$** | $\text{Area} = 2r^2$ | Lattice points $= 2r^2 + 2r + 1$ (boundary $= 4r$) |
| **Log Inequality ($0 < b < 1$)** | $\log_b f(x) \ge k \iff 0 < f(x) \le b^k$ | Flip inequality AND enforce $f(x) > 0$ |
| **De-nesting Surds** | $\sqrt{(x+y) \pm 2\sqrt{xy}} = |\sqrt{x} \pm \sqrt{y}|$ | Factor inner surd as $2\sqrt{xy}$ first |
| **Cauchy Equations** | $f(x+y)=f(x)f(y) \implies a^x$; $f(x)f(1/x)=f(x)+f(1/x) \implies 1\pm x^n$ | Substitute functional form immediately |
| **AP Sum vs Term Ratio** | $\frac{S_{2m-1}}{S'_{2m-1}} = \frac{T_m}{T'_m}$ | Plug $n = 2m - 1$ into $\frac{S_n}{S'_n}$ to get ratio of $m$-th terms |
| **Telescoping Radicals** | $\sqrt{1 + \frac{1}{k^2} + \frac{1}{(k+1)^2}} = 1 + \frac{1}{k} - \frac{1}{k+1}$ | Sum from $1$ to $n$ is $n + 1 - \frac{1}{n+1}$ |
| **AM-GM Weighted Split** | Maximize $x^p y^q$ given $ax + by = S$ | Set $\frac{ax}{p} = \frac{by}{q} = \frac{S}{p+q}$ (strictly $x, y > 0$) |

---

## 3. Geometry & Mensuration Rapid Formulas & Triggers

- **Memorized Pythagorean Triplets**:
  `(3, 4, 5)`, `(5, 12, 13)`, `(7, 24, 25)`, `(8, 15, 17)`, `(9, 40, 41)`, `(11, 60, 61)`, `(12, 35, 37)`, `(20, 21, 29)`
- **Standard Heron's Integer-Area Triangles**:
  - `(13, 14, 15)` $\implies \text{Area} = 84$, altitude to $14$ is $12$, $r = 4$, $R = \frac{65}{8} = 8.125$.
  - `(10, 17, 21)` $\implies \text{Area} = 84$ (split into $6$-$8$-$10$ and $8$-$15$-$17$).
- **Key Triangle & Circle Formulas**:
  - $\Delta = r \cdot s = \frac{abc}{4R}$; Right triangle: $r = \frac{a+b-c}{2}, R = \frac{c}{2}, h = \frac{ab}{c}$.
  - Angle Bisector Length: $l^2 = bc - pq$; Median Length: $m_a = \frac{1}{2}\sqrt{2b^2 + 2c^2 - a^2}$.
  - Euler Line: $OG : GH = 1 : 2$; Right-triangle inscribed square on legs: $x = \frac{ab}{a+b}$.
  - Trapezium Diagonal Areas: $\text{Area} = (\sqrt{A_{\text{top}}} + \sqrt{A_{\text{bottom}}})^2$; Parallel segment through diagonal intersection $= \frac{2ab}{a+b}$.
  - Direct Common Tangent $= \sqrt{d^2 - (r_1 - r_2)^2}$; Ford Tangent Circle: $\frac{1}{\sqrt{r}} = \frac{1}{\sqrt{r_1}} + \frac{1}{\sqrt{r_2}}$.
- **3D & Coordinate Formulas**:
  - Frustum Volume $= \frac{1}{3}\pi h(R^2 + r^2 + Rr)$; Regular Tetrahedron Volume $= \frac{\sqrt{2}}{12}a^3$, Height $= \sqrt{\frac{2}{3}}a$.
  - Sphere in Cone ($r, h, l$): $R_{\text{sphere}} = \frac{rh}{r + l}$; Max Cylinder in Cone: $V_{\text{cyl}} = \frac{4}{27}V_{\text{cone}}$.
  - Cuboid Shortest Surface Path ($l \ge b \ge h$): $\sqrt{l^2 + (b + h)^2}$.
  - Shoelace Area from $(0,0), (u_1,v_1), (u_2,v_2)$: $\frac{1}{2}|u_1 v_2 - u_2 v_1|$.
  - Reflection of $(x_0, y_0)$ in $ax + by + c = 0$: $\frac{x_r - x_0}{a} = \frac{y_r - y_0}{b} = \frac{-2(ax_0 + by_0 + c)}{a^2 + b^2}$.

---

## 4. Number System & Modern Math Rapid Formulas & Triggers

- **Factors of $N = 2^a p^b q^c$**:
  - $d(N) = (a+1)(b+1)(c+1)$; Sum $\sigma(N) = \prod \frac{p_i^{\alpha_i+1}-1}{p_i-1}$; Product $= N^{d(N)/2}$.
  - Coprime factor pairs $\{u, v\} = 2^{k-1}$ ($k =$ number of distinct primes).
  - Ordered positive solutions to $\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$ is $d(n^2)$.
- **Modular & Factorial Theorems**:
  - Prime $p > 3 \implies p^2 \equiv 1 \pmod{24}$; $1001 = 7 \times 11 \times 13$.
  - Euler: $a^{\phi(n)} \equiv 1 \pmod n$; Wilson: $(p-1)! \equiv p-1 \pmod p$ and $(p-2)! \equiv 1 \pmod p$.
  - Legendre: $E_p(n!) = \sum \lfloor \frac{n}{p^k} \rfloor = \frac{n - S_p(n)}{p - 1}$.
- **P&C, Probability & Set Theory**:
  - Stars & Bars: $\binom{n+r-1}{r-1}$ (non-negative $x_i \ge 0$); $\binom{n-1}{r-1}$ (positive $x_i \ge 1$); $\binom{n+r}{r}$ (inequality $\sum_{i=1}^r x_i \le n$).
  - Derangements: $D_1 = 0, D_2 = 1, D_3 = 2, D_4 = 9, D_5 = 44, D_6 = 265$.
  - Grid ($m \times n$ squares): Rectangles $= \binom{m+1}{2}\binom{n+1}{2}$; Squares $= \sum (m-k+1)(n-k+1)$.
  - $k$-Set Intersection Minimum (Surplus Rule): $\max\big(0,\; \sum_{i=1}^k |A_i| - (k-1)|U|\big)$.

---

## 5. CAT 2025 Newly Surfaced QA Triggers & Edge Traps

| CAT 2025 Source | Pattern / Trigger Seen in Question | Instant 30-Second Action & Trap Guard |
| :--- | :--- | :--- |
| `CAT2025_S1_QA_Q05` (`CAT_2025_QA_Slot_1`) | $\lfloor x^2 \rfloor = \lfloor x \rfloor^2$ on $[3, 6]$ | On $[n, n+1)$, solution is $[n, \sqrt{n^2+1})$ with an **open** right bracket at $\sqrt{10}, \sqrt{17}, \sqrt{26}$ |
| `CAT2025_S1_QA_Q09` (`CAT_2025_QA_Slot_1`) | Nested log inequality with base $b \in (0, 1)$ | Flip inequality direction at every $0<b<1$ layer AND enforce inner argument $> 0$ |
| `CAT2025_S3_QA_Q08` (`CAT_2025_QA_Slot_3`) | Variable base in $\log_{g(x)} f(x) = k$ | Solve $f(x) = g(x)^k$, then **discard** any root where $g(x) \le 0$ or $g(x) = 1$ |
| `CAT2025_S3_QA_Q06` (`CAT_2025_QA_Slot_3`) | $x + \frac{1}{x} = 4\sqrt{3}$, find $x^7 + \frac{1}{x^7}$ | Use Newton recurrence $S_7 = S_3 S_4 - S_1$ ($S_2=46, S_3=180\sqrt{3}, S_4=2114$) |
| `CAT2025_S2_QA_Q01` (`CAT_2025_QA_Slot_2`) | 3-term GP with $\sum a_i$ and $\sum_{i<j} a_i a_j$ given | Divide directly: $\frac{a_1 a_2 + a_2 a_3 + a_3 a_1}{a_1 + a_2 + a_3} = a_2$ (since $a_1 a_3 = a_2^2$) |
| `CAT2025_S2_QA_Q06` (`CAT_2025_QA_Slot_2`) | $\log_4 x + \log_8 y + \log_{16} z$ with AM-GM | Reduce all bases to $2^k$ ($\frac{1}{2}\log_2 x + \frac{1}{3}\log_2 y + \frac{1}{4}\log_2 z$) before AM-GM |
| `CAT2025_S2_QA_Q15` (`CAT_2025_QA_Slot_2`) | Count divisors of $N$ of form $3r+1$ | Drop $3^k$; primes $\equiv 1 \pmod 3$ take any exponent; primes $\equiv 2 \pmod 3$ require an **even** total exponent |
| `CAT2025_S2_QA_Q18` (`CAT_2025_QA_Slot_2`) | Integer solutions $(a, b \in \mathbb{Z})$ to $ab + 3a - 2b = 18$ | Factor $(a-2)(b+3) = 12$ (or $-12$) and test **both positive and negative** divisor pairs |
| `CAT2025_S3_QA_Q02` (`CAT_2025_QA_Slot_3`) | Right trapezium circumscribing a circle of radius $r$ | Height $h = 2r$ and Pitot theorem $AB + CD = h + BC$; use $(CD-AB)^2 + h^2 = BC^2$ |
| `CAT2025_S3_QA_Q04` (`CAT_2025_QA_Slot_3`) | 3-Set Venn optimization with 'some students in all 3' | Express regions in terms of $x = |A \cap B \cap C|$ and enforce **$x \ge 1$** (not $x = 0$) |
