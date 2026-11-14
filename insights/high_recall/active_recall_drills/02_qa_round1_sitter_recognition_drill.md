# High-Recall Drill 02: QA `Round_1_Sitter` 20-Second Trigger Recognition (30 Questions)

> **Companion Reference**: [`../cheat_sheets/QA_Formula_and_Trigger_Book.md`](../cheat_sheets/QA_Formula_and_Trigger_Book.md) | [`../../quant_concept_examples/README.md`](../../quant_concept_examples/README.md) | [`README.md`](./README.md)

**Instructions**: In Pass 1 of the CAT QA section, your goal is to spot the 8–10 `Round_1_Sitter` questions and solve each in **under 45 seconds** using its direct `See X -> Do Y` trigger. For each prompt below, name the mental trigger and compute the answer before clicking to expand.

---

## Part A: Arithmetic Sitters (Q1–Q10)

<details><summary><b>Q1: Petrol price increases by 28.57% (2/7). By what % must consumption decrease so expenditure remains unchanged?</b></summary>

- **Trigger (`See X -> Do Y`)**: Product constancy $A \uparrow \frac{a}{b} \implies B \downarrow \frac{a}{b+a}$.
- **Solution**: $\frac{2}{7 + 2} = \frac{2}{9} = \mathbf{22.22\%}$.
</details>

<details><summary><b>Q2: A trader allows a 15% discount on MP and still makes a 19% profit on CP. Find CP : MP.</b></summary>

- **Trigger (`See X -> Do Y`)**: Direct ratio $\frac{\text{CP}}{\text{MP}} = \frac{100 - d}{100 + p}$.
- **Solution**: $\frac{100 - 15}{100 + 19} = \frac{85}{119} = \mathbf{5 : 7}$ (dividing by $17$).
</details>

<details><summary><b>Q3: The difference between CI and SI on a sum for 2 years is Rs. 80 and for 3 years is Rs. 250. Find the annual interest rate R%.</b></summary>

- **Trigger (`See X -> Do Y`)**: $\frac{\text{Diff}_3}{\text{Diff}_2} = 3 + r = 3 + \frac{R}{100}$.
- **Solution**: $3 + r = \frac{250}{80} = 3.125 \implies r = 0.125 \implies \mathbf{R = 12.5\%}$.
</details>

<details><summary><b>Q4: A shopkeeper sells at a 10% profit on CP, gives 1 article free on buying 14 articles, and uses an 800 g weight for 1 kg. Find his net profit %.</b></summary>

- **Trigger (`See X -> Do Y`)**: Chain of Multiplying Factors $\text{MF}_{\text{net}} = \text{MF}_{\text{price}} \times \text{MF}_{\text{free}} \times \text{MF}_{\text{weight}}$.
- **Solution**: $\text{MF} = \frac{11}{10} \times \frac{14}{15} \times \frac{1000}{800} = \frac{11}{10} \times \frac{14}{15} \times \frac{5}{4} = \frac{77}{60} \implies \frac{17}{60} \times 100\% = \mathbf{28.33\%}$.
</details>

<details><summary><b>Q5: Vessel A has 20 L pure alcohol and Vessel B has 30 L pure water. Equal volumes x L are swapped simultaneously so both vessels reach identical concentration. Find x.</b></summary>

- **Trigger (`See X -> Do Y`)**: Equilibrium swap volume $x^* = \frac{V_A V_B}{V_A + V_B}$.
- **Solution**: $x^* = \frac{20 \times 30}{20 + 30} = \frac{600}{50} = \mathbf{12\text{ L}}$.
</details>

<details><summary><b>Q6: From a cask of pure milk, 12 L is drawn and replaced with water twice, leaving milk and water in ratio 25 : 11. Find the initial capacity V of the cask.</b></summary>

- **Trigger (`See X -> Do Y`)**: $\left(1 - \frac{x}{V}\right)^2 = \frac{\text{Milk}}{\text{Total}} = \frac{25}{25+11} = \frac{25}{36}$ (never $\frac{25}{11}$!).
- **Solution**: $1 - \frac{12}{V} = \frac{5}{6} \implies \frac{12}{V} = \frac{1}{6} \implies \mathbf{V = 72\text{ L}}$.
</details>

<details><summary><b>Q7: A alone takes 16 hours more than (A+B) together to finish a work, and B alone takes 9 hours more than (A+B) together. Find the time taken by (A+B) together.</b></summary>

- **Trigger (`See X -> Do Y`)**: $T_{AB} = \sqrt{a \cdot b}$.
- **Solution**: $T_{AB} = \sqrt{16 \times 9} = \mathbf{12\text{ hours}}$.
</details>

<details><summary><b>Q8: Two trains start simultaneously from P and Q toward each other. After meeting, they take 16 hours and 25 hours to reach Q and P. If the slower train runs at 36 km/hr, find the speed of the faster train.</b></summary>

- **Trigger (`See X -> Do Y`)**: Post-meeting ratio $\frac{S_1}{S_2} = \sqrt{\frac{t_2}{t_1}}$.
- **Solution**: $\frac{S_{\text{fast}}}{S_{\text{slow}}} = \sqrt{\frac{25}{16}} = \frac{5}{4} \implies S_{\text{fast}} = 36 \times \frac{5}{4} = \mathbf{45\text{ km/hr}}$.
</details>

<details><summary><b>Q9: Two runners run in opposite directions around a circular track at speeds 18 m/s and 30 m/s. At how many distinct points on the track do they meet?</b></summary>

- **Trigger (`See X -> Do Y`)**: Reduce speed ratio $\frac{18}{30} = \frac{3}{5}$ to coprime integers first; opposite direction $\implies a + b$.
- **Solution**: $3 + 5 = \mathbf{8\text{ distinct points}}$.
</details>

<details><summary><b>Q10: Walking up an ascending escalator, A takes 50 steps in 20 seconds and B takes 60 steps in 10 seconds. Find the total visible steps N on the escalator.</b></summary>

- **Trigger (`See X -> Do Y`)**: $N = S_p + e \cdot t$.
- **Solution**: $50 + 20e = 60 + 10e \implies 10e = 10 \implies e = 1 \implies N = 60 + 10(1) = \mathbf{70\text{ steps}}$.
</details>

---

## Part B: Algebra Sitters (Q11–Q20)

<details><summary><b>Q11: What is the largest integer that CANNOT be expressed as 8x + 11y for non-negative integers x, y >= 0?</b></summary>

- **Trigger (`See X -> Do Y`)**: Frobenius Coin Theorem $ab - a - b$.
- **Solution**: $8(11) - 8 - 11 = 88 - 19 = \mathbf{69}$.
</details>

<details><summary><b>Q12: How many ordered pairs of positive integers (x, y) satisfy xy + 3x + 5y = 45?</b></summary>

- **Trigger (`See X -> Do Y`)**: Simon's Factoring Trick: add $3 \times 5 = 15$ to both sides $\implies (x+5)(y+3) = 60$.
- **Solution**: Since $x \ge 1, y \ge 1$, we need $x+5 \ge 6$ and $y+3 \ge 4$. Factor pairs of $60$ satisfying this are $(6,10), (10,6), (12,5), (15,4) \implies \mathbf{4\text{ pairs}}$.
</details>

<details><summary><b>Q13: Find the set of real x satisfying |x - 4| + |x + 2| = |2x - 2|.</b></summary>

- **Trigger (`See X -> Do Y`)**: $|A| + |B| = |A + B| \iff A \cdot B \ge 0$.
- **Solution**: $(x - 4)(x + 2) \ge 0 \implies \mathbf{x \in (-\infty, -2] \cup [4, \infty)}$.
</details>

<details><summary><b>Q14: Find the minimum value of |x - 2| + |x - 4| + |x - 7| + |x - 11| + |x - 15|.</b></summary>

- **Trigger (`See X -> Do Y`)**: Minimum at the median ($x = 7$); pair outer differences inward.
- **Solution**: $(15 - 2) + (11 - 4) + 0 = 13 + 7 = \mathbf{20}$.
</details>

<details><summary><b>Q15: Find the area enclosed by |x - 3| + |y + 1| <= 5 and the number of integer points (x, y) on its boundary.</b></summary>

- **Trigger (`See X -> Do Y`)**: Diamond area $= 2r^2$; boundary lattice points $= 4r$.
- **Solution**: $\text{Area} = 2(5^2) = \mathbf{50}$; boundary integer points $= 4(5) = \mathbf{20}$.
</details>

<details><summary><b>Q16: Find all real x satisfying log_(0.2)(x - 3) >= -1.</b></summary>

- **Trigger (`See X -> Do Y`)**: Base $0.2 \in (0, 1) \implies$ flip inequality AND enforce argument $> 0$: $0 < x - 3 \le (0.2)^{-1} = 5$.
- **Solution**: $\mathbf{x \in (3, 8]}$.
</details>

<details><summary><b>Q17: If f(x + y) = f(x)f(y) for all real x, y and f(2) = 16 (with f(x) > 0), find f(5).</b></summary>

- **Trigger (`See X -> Do Y`)**: Cauchy exponential form $f(x) = a^x$.
- **Solution**: $a^2 = 16 \implies a = 4 \implies f(5) = 4^5 = \mathbf{1024}$.
</details>

<details><summary><b>Q18: The ratio of the sums of the first n terms of two APs is (4n + 1) : (3n + 7). Find the ratio of their 8th terms.</b></summary>

- **Trigger (`See X -> Do Y`)**: Plug $n = 2m - 1 = 2(8) - 1 = 15$ into the sum ratio.
- **Solution**: $\frac{4(15) + 1}{3(15) + 7} = \mathbf{\frac{61}{52}}$.
</details>

<details><summary><b>Q19: Evaluate sum_{k=1}^{19} sqrt(1 + 1/k^2 + 1/(k+1)^2).</b></summary>

- **Trigger (`See X -> Do Y`)**: Each radical is $1 + \frac{1}{k} - \frac{1}{k+1}$; sum from $1$ to $n$ is $n + 1 - \frac{1}{n+1}$.
- **Solution**: $19 + 1 - \frac{1}{20} = \mathbf{19.95}$.
</details>

<details><summary><b>Q20: Given x, y > 0 and 3x + 2y = 20, find the maximum value of x^3 * y^2.</b></summary>

- **Trigger (`See X -> Do Y`)**: Weighted AM-GM split: $\frac{3x}{3} = \frac{2y}{2} = \frac{20}{3 + 2} = 4 \implies x = 4, y = 4$.
- **Solution**: $\text{Max} = 4^3 \times 4^2 = 4^5 = \mathbf{1024}$.
</details>

---

## Part C: Geometry, Number System & Modern Math Sitters (Q21–Q30)

<details><summary><b>Q21: In a right triangle with legs 12 cm and 15 cm, find the side length of the inscribed square resting on the two legs.</b></summary>

- **Trigger (`See X -> Do Y`)**: $x = \frac{ab}{a + b}$.
- **Solution**: $x = \frac{12 \times 15}{12 + 15} = \frac{180}{27} = \mathbf{\frac{20}{3}\text{ cm}}$.
</details>

<details><summary><b>Q22: In trapezium ABCD (AB || CD), diagonals intersect at O with Area(AOB) = 16 and Area(COD) = 36. Find the total area of the trapezium.</b></summary>

- **Trigger (`See X -> Do Y`)**: $\text{Area} = (\sqrt{A_{\text{top}}} + \sqrt{A_{\text{bottom}}})^2$.
- **Solution**: $(4 + 6)^2 = \mathbf{100}$.
</details>

<details><summary><b>Q23: A rhombus has side length 10 cm and area 96 sq. cm. Find the positive difference between the lengths of its diagonals |d1 - d2|.</b></summary>

- **Trigger (`See X -> Do Y`)**: $|d_1 - d_2| = 2\sqrt{a^2 - \text{Area}}$.
- **Solution**: $2\sqrt{100 - 96} = 2\sqrt{4} = \mathbf{4\text{ cm}}$ (diagonals are $16$ and $12$).
</details>

<details><summary><b>Q24: Find the shortest surface path for an ant to crawl between opposite corners of a 12 cm x 5 cm x 4 cm cuboid.</b></summary>

- **Trigger (`See X -> Do Y`)**: Keep largest dimension $l = 12$ separate: $\sqrt{l^2 + (b + h)^2}$.
- **Solution**: $\sqrt{12^2 + (5 + 4)^2} = \sqrt{144 + 81} = \sqrt{225} = \mathbf{15\text{ cm}}$.
</details>

<details><summary><b>Q25: Find the area of the triangle with vertices A(4, 7), B(9, 10), and C(6, 15).</b></summary>

- **Trigger (`See X -> Do Y`)**: Shift $A(4,7) \to (0,0)$: $B'=(5,3), C'=(2,8)$; $\text{Area} = \frac{1}{2}|u_1 v_2 - u_2 v_1|$.
- **Solution**: $\frac{1}{2}|5(8) - 2(3)| = \frac{1}{2}|40 - 6| = \mathbf{17}$.
</details>

<details><summary><b>Q26: How many ordered pairs of positive integers (x, y) satisfy 1/x + 1/y = 1/10?</b></summary>

- **Trigger (`See X -> Do Y`)**: Number of ordered positive solutions is $d(n^2) = d(100)$.
- **Solution**: $100 = 2^2 \times 5^2 \implies d(100) = (2+1)(2+1) = \mathbf{9\text{ pairs}}$.
</details>

<details><summary><b>Q27: Find the remainder when 3^82 is divided by 81? Wait: find the remainder when 3^82 is divided by 54.</b></summary>

- **Trigger (`See X -> Do Y`)**: Cancel common factor $g = 27 = 3^3$ from $3^{82}$ and $54 = 27 \times 2$, find remainder $\bmod 2$, and multiply back by $27$.
- **Solution**: $\frac{3^{82}}{54} = \frac{3^{79}}{2}$. Since $3^{79} \equiv 1^{79} = 1 \pmod 2$, true remainder $= 27 \times 1 = \mathbf{27}$.
</details>

<details><summary><b>Q28: Find the remainder when 21! is divided by 23.</b></summary>

- **Trigger (`See X -> Do Y`)**: Wilson's Theorem corollary: for prime $p$, $(p - 2)! \equiv 1 \pmod p$.
- **Solution**: Since $23$ is prime and $21 = 23 - 2$, remainder is $\mathbf{1}$.
</details>

<details><summary><b>Q29: In how many ways can 5 letters be placed into 5 addressed envelopes so that exactly 1 letter goes into its right envelope?</b></summary>

- **Trigger (`See X -> Do Y`)**: $\binom{n}{k} \times D_{n-k}$ with $D_4 = 9$.
- **Solution**: $\binom{5}{1} \times D_4 = 5 \times 9 = \mathbf{45\text{ ways}}$.
</details>

<details><summary><b>Q30: In a survey of 100 people, 80 like A, 75 like B, 85 like C, and 70 like D. What is the minimum possible number of people who like all four?</b></summary>

- **Trigger (`See X -> Do Y`)**: $k$-Set Surplus Rule: $\max(0,\; \sum |A_i| - (k - 1)|U|)$.
- **Solution**: $(80 + 75 + 85 + 70) - 3(100) = 310 - 300 = \mathbf{10}$.
</details>
