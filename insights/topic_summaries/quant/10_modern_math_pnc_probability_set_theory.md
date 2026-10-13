# QA 10: Modern Math — Permutations & Combinations, Probability & Set Theory

**Canonical Taxonomy Mapping**: `QA > Modern Math > Permutations & Combinations`, `Probability`, `Set Theory`  
**Weightage**: ~6–10% of QA (2–3 questions per slot)  
**Priority Tier**: Tier 1 (High-Yield Core + DILR Overlap)

---

## 1. 30-Second Concept & Formula Blueprint

### 1.1 Permutations & Combinations (P&C)
- **Distribution & Partition Matrix (The 4-Box Table)**:

| Items ($n$) | Boxes ($r$) | Any Box Can Be Empty | No Box Empty ($n \ge r$) |
| :--- | :--- | :--- | :--- |
| **Distinct** | **Distinct** | $r^n$ | $\sum_{k=0}^{r} (-1)^k \binom{r}{k}(r-k)^n = r! \, S(n, r)$ |
| **Identical** | **Distinct** (Stars & Bars) | $\binom{n + r - 1}{r - 1}$ | $\binom{n - 1}{r - 1}$ |
| **Distinct** | **Identical** | $\sum_{k=1}^{r} S(n, k)$ | Stirling number $S(n, r)$ |
| **Identical** | **Identical** | Partition of $n$ into $\le r$ parts | Partition of $n$ into exactly $r$ parts |

- **Gap Method vs. Tie/String Method**:
  - $m$ objects **together**: Tie them as $1$ super-object $\implies (n - m + 1)! \times m!$ (divide by identical repeats).
  - $m$ objects **no two adjacent** (among $k$ other objects, $k+1 \ge m$): Place $k$ other objects first ($k!$), creating $k+1$ gaps $\implies k! \times \binom{k+1}{m} \times m!$.
- **Circular Permutations ($n$ distinct objects)**:
  - Clockwise $\neq$ Counter-clockwise (e.g., people around a table): $(n - 1)!$
  - Clockwise $=$ Counter-clockwise (flippable necklace/garland): $\frac{(n - 1)!}{2}$ (for $n \ge 3$).
- **Derangements ($D_n$ — no element in its original position)**:
  $$D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!} \implies \mathbf{D_1 = 0,\; D_2 = 1,\; D_3 = 2,\; D_4 = 9,\; D_5 = 44,\; D_6 = 265}$$
  - *Exactly $k$ elements in their right positions*: $\binom{n}{k} \cdot D_{n-k}$.
- **Geometric Counting**:
  - From $n$ points with $m$ collinear:
    - Straight lines $= \binom{n}{2} - \binom{m}{2} + 1$
    - Triangles $= \binom{n}{3} - \binom{m}{3}$
  - On an $m \times n$ grid of unit squares ($m+1$ horizontal lines, $n+1$ vertical lines):
    - Total Rectangles (including squares) $= \binom{m+1}{2} \binom{n+1}{2}$
    - Total Squares $= \sum_{k=1}^{\min(m,n)} (m - k + 1)(n - k + 1)$ (for $n \times n$ chessboard: $\frac{n(n+1)(2n+1)}{6}$; for $8 \times 8$: $1296$ rectangles, $204$ squares).

---

### 1.2 Probability, Bayes' Theorem & Expected Value
- **Addition & Multiplication Rules**:
  - $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
  - Independent events: $P(A \cap B) = P(A)P(B)$, and $P(\text{at least one}) = 1 - P(A')P(B')$.
  - Mutually exclusive events: $P(A \cap B) = 0$ (Note: Non-zero mutually exclusive events are **NEVER** independent!).
- **Conditional Probability & Bayes' Theorem**:
  $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(E_i \mid A) = \frac{P(E_i) P(A \mid E_i)}{\sum_{j} P(E_j) P(A \mid E_j)}$$
- **Binomial Trials ($n$ independent trials, success $p$, failure $q = 1 - p$)**:
  $$P(X = r) = \binom{n}{r} p^r q^{n-r}$$
  - **Odd/Even Successes Shortcut**:
    $$P(\text{Even successes}) = \frac{1 + (q - p)^n}{2}, \qquad P(\text{Odd successes}) = \frac{1 - (q - p)^n}{2}$$
- **Infinite Alternating Geometric Game** ($A$ goes first with win prob $p_A$, then $B$ with $p_B$):
  $$P(A \text{ wins}) = \frac{p_A}{1 - q_A q_B}, \qquad P(B \text{ wins}) = \frac{q_A p_B}{1 - q_A q_B}$$

---

### 1.3 Set Theory & Inclusion-Exclusion
- **3-Set Inclusion-Exclusion**:
  $$|A \cup B \cup C| = \sum |A| - \sum |A \cap B| + |A \cap B \cap C|$$
- **"Exactly $k$ Sets" Layer Equations** ($E_k =$ elements in *exactly* $k$ sets; $N =$ total universe; $E_0 =$ none):
  $$E_1 + E_2 + E_3 = N - E_0$$
  $$E_1 + 2E_2 + 3E_3 = |A| + |B| + |C|$$
  - Subtracting the two equations immediately eliminates $E_1$:
    $$E_2 + 2E_3 = (|A| + |B| + |C|) - (N - E_0)$$
- **Set Intersection Minima / Surplus Rule**:
  - For $k$ sets inside universe $U$:
    $$\min |A_1 \cap A_2 \cap \dots \cap A_k| = \max\Big(0,\; \sum_{i=1}^{k} |A_i| - (k - 1)|U|\Big)$$
  - Maximum of $|A_1 \cap \dots \cap A_k| = \min(|A_1|, |A_2|, \dots, |A_k|)$.

---

## 2. Pattern-Recognition Trigger Table

| Question Cue / Wording | Hidden Constraint | Fastest Attack Strategy |
| :--- | :--- | :--- |
| "Number of integral solutions to $x_1 + x_2 + x_3 + x_4 = 20$ with $x_i \ge k_i$" | Lower bounds $k_i$ can be absorbed by pre-giving $k_i$ coins to beggar $i$ | Replace $N \leftarrow N - \sum k_i$ and apply non-negative Stars & Bars $\binom{N' + r - 1}{r - 1}$ |
| "Number of non-negative integral solutions to $x + y + z \le n$" | Inequality $\le n$ is equivalent to adding a **slack beggar** $s \ge 0$ such that $x+y+z+s = n$ | Directly compute $\binom{n + (r+1) - 1}{(r+1) - 1} = \binom{n + r}{r}$! |
| "Divide $2n$ distinct players into $n$ unlabeled pairs (or teams of equal size)" | Order among identical-sized groups does not matter! | Divide by $k!$ for $k$ groups of equal size: for $2n$ into $n$ pairs, $\frac{(2n)!}{(2!)^n \cdot n!}$ |
| "Dictionary rank of a word (e.g., `MOTHER` or `SUCCESS`)" | Count permutations of remaining letters strictly preceding each target letter | Write alphabetical weights $(0, 1, 2, \dots)$ above letters, multiply by $(n-1)!, (n-2)!, \dots$ (dividing by duplicates to the right), and add $+1$ |
| "Probability that a stick broken at 2 random points forms a triangle" | Each piece must be $< L/2$ | Classic geometric probability area ratio $= \mathbf{\frac{1}{4}}$ |

---

## 3. Canonical CAT Archetypes & Solved Exemplars

### Archetype 1: Stars & Bars with Both Lower and Upper Bounds
> **Problem**: Find the number of non-negative integer solutions to $x + y + z = 15$ such that $x \le 6$, $y \le 7$, and $z \le 8$.

- **First-Principles Method (Inclusion-Exclusion on Upper Bounds)**:
  1. Total unrestricted non-negative solutions $= \binom{15 + 3 - 1}{3 - 1} = \binom{17}{2} = 136$.
  2. Subtract cases violating at least one upper bound:
     - $x \ge 7$: give $7$ to $x \implies \binom{8 + 2}{2} = \binom{10}{2} = 45$
     - $y \ge 8$: give $8$ to $y \implies \binom{7 + 2}{2} = \binom{9}{2} = 36$
     - $z \ge 9$: give $9$ to $z \implies \binom{6 + 2}{2} = \binom{8}{2} = 28$
  3. Add back double violations:
     - $x \ge 7$ and $y \ge 8$ (sum $\ge 15$): $\binom{0 + 2}{2} = 1$
     - $x \ge 7$ and $z \ge 9$ (sum $\ge 16 > 15$): $0$
     - $y \ge 8$ and $z \ge 9$ (sum $\ge 17 > 15$): $0$
  4. Valid solutions $= 136 - (45 + 36 + 28) + 1 = 136 - 109 + 1 = \mathbf{28}$.

- **30-Second Exam-Hall Speed Shortcut (Dual / Inversion Substitution)**:
  - Let $x' = 6 - x \ge 0$, $y' = 7 - y \ge 0$, $z' = 8 - z \ge 0$.
  - Summing gives $x' + y' + z' = (6 + 7 + 8) - 15 = 6$.
  - Since $6 \le \min(6, 7, 8)$, the upper bounds never bind on the inverted variables!
  - Directly compute $\binom{6 + 3 - 1}{3 - 1} = \binom{8}{2} = \mathbf{28}$ in 10 seconds!

---

### Archetype 2: Bayes' Theorem — Truth-Teller / Witness Credibility
> **Problem**: A speaks the truth in $75\%$ of cases and B speaks the truth in $80\%$ of cases. Look at two variants:
> (a) What is the probability that they **contradict** each other in stating the same fact?
> (b) A die is rolled. Both A and B report that a $6$ appeared. Find the probability that it is actually a $6$ (assuming that when lying, each reports one of the other 5 numbers equally likely).

- **First-Principles Method**:
  - **Part (a)**: Contradiction $= P(A\text{ true}, B\text{ false}) + P(A\text{ false}, B\text{ true}) = \frac{3}{4}\cdot\frac{1}{5} + \frac{1}{4}\cdot\frac{4}{5} = \frac{7}{20} = \mathbf{35\%}$.
  - **Part (b)**:
    - Prior: $P(6) = \frac{1}{6}$, $P(\text{not }6) = \frac{5}{6}$.
    - Likelihood given $6$: both tell the truth $= \frac{3}{4} \times \frac{4}{5} = \frac{12}{20}$.
    - Likelihood given NOT $6$: both lie AND specifically pick "$6$" out of the 5 false faces:
      $$P(\text{both say }6 \mid \text{not }6) = \left(\frac{1}{4} \times \frac{1}{5}\right) \times \left(\frac{1}{5} \times \frac{1}{5}\right) = \frac{1}{500}$$
    - By Bayes' Theorem:
      $$P(6 \mid \text{both say }6) = \frac{\frac{1}{6} \times \frac{12}{20}}{\frac{1}{6} \times \frac{12}{20} + \frac{5}{6} \times \frac{1}{500}} = \frac{\frac{12}{120}}{\frac{12}{120} + \frac{1}{600}} = \frac{60}{60 + 1} = \mathbf{\frac{60}{61}}$$

- **30-Second Exam-Hall Speed Shortcut (Odds Ratio Method)**:
  $$\text{Posterior Odds} = \text{Prior Odds} \times \text{Likelihood Ratio} = \frac{1}{5} \times \frac{(3/4)(4/5)}{(1/20)(1/25)} = \frac{1}{5} \times 300 = \frac{60}{1} \implies P = \mathbf{\frac{60}{61}}$$

---

## 4. Boundary Conditions, Domain Traps & TITA Pitfalls

1. **Equal-Size Unlabeled Group Division Trap**:
   - Dividing $12$ distinct toys among $3$ **children** equally $= \frac{12!}{4!4!4!}$.
   - Dividing $12$ distinct toys into $3$ **unlabeled parcels** of $4$ each $= \frac{12!}{4!4!4! \times \mathbf{3!}}$.
2. **Leading Zero in Digit-Formation Problems**:
   - When forming $4$-digit numbers (or $4$-digit even numbers) from $\{0, 1, 2, 3, 4, 5\}$ without repetition, **ALWAYS split into two cases**: Case 1 (Units digit $= 0$) and Case 2 (Units digit $\in \{2, 4\}$) so the thousands digit restriction ($\neq 0$) does not clash with the units digit!
3. **Bayes' Theorem Multi-Choice Lie Factor ($1/5$)**:
   - In a 6-sided die problem, if the question says "B reports whether it is a 6 or not" (binary yes/no), the lie probability is $1 - p$. If it says "B reports the number that appeared" (1 to 6), the probability of falsely reporting "$6$" when a non-6 rolled is $\frac{1 - p}{5}$!

---

## 5. Active-Recall Drill (10 Prompts)

<details><summary>Q1: In how many ways can 6 letters be placed into 6 addressed envelopes such that exactly 2 letters go into their correct envelopes?</summary>
A: Choose 2 correct letters in C(6, 2) = 15 ways, and derange the remaining 4 letters in D_4 = 9 ways. Total = 15 * 9 = 135 ways.
</details>

<details><summary>Q2: How many non-negative integral solutions exist for x + y + z <= 10?</summary>
A: Introduce slack variable s >= 0 so x + y + z + s = 10. Using Stars & Bars: C(10 + 4 - 1, 4 - 1) = C(13, 3) = 286.
</details>

<details><summary>Q3: There are 12 points in a plane, of which 5 are collinear. How many triangles can be formed using these points as vertices?</summary>
A: C(12, 3) - C(5, 3) = 220 - 10 = 210 triangles.
</details>

<details><summary>Q4: How many rectangles that are NOT squares exist on a standard 8x8 chessboard?</summary>
A: Total rectangles = C(9, 2) * C(9, 2) = 36 * 36 = 1296. Total squares = 8*9*17/6 = 204. Non-square rectangles = 1296 - 204 = 1092.
</details>

<details><summary>Q5: How many 4-digit even numbers can be formed using digits {0, 1, 2, 3, 4, 5} without repetition?</summary>
A: Case 1 (ends in 0): 5 * 4 * 3 * 1 = 60. Case 2 (ends in 2 or 4): 4 * 4 * 3 * 2 = 96. Total = 60 + 96 = 156.
</details>

<details><summary>Q6: In a survey of 100 students, 80 like Tea, 75 like Coffee, 70 like Milk, and 85 like Juice. What is the minimum number of students who like all four beverages?</summary>
A: Surplus formula: max(0, (80 + 75 + 70 + 85) - 3*100) = 310 - 300 = 10 students.
</details>

<details><summary>Q7: A fair coin is tossed 8 times. What is the probability of getting an odd number of heads?</summary>
A: For any fair coin (p = q = 1/2), P(odd heads) = (1 - (q - p)^n)/2 = 1/2.
</details>

<details><summary>Q8: A and B take turns rolling a pair of dice, starting with A. The first to roll a sum of 7 wins. Find A's probability of winning.</summary>
A: P(sum = 7) = 6/36 = 1/6, so q = 5/6. P(A wins) = (1/6) / (1 - (5/6)*(5/6)) = (1/6) / (11/36) = 6/11.
</details>

<details><summary>Q9: In how many ways can 10 distinct books be divided equally among 2 students vs. into 2 unlabeled bundles?</summary>
A: Among 2 distinct students: 10! / (5! * 5!) = 252 ways. Into 2 unlabeled bundles: 252 / 2! = 126 ways.
</details>

<details><summary>Q10: Find the dictionary rank of the word 'RANK' when all permutations of its letters are arranged alphabetically.</summary>
A: Alphabetical order: A(1), K(2), N(3), R(4). For 'RANK': before R are {A, K, N} -> 3 * 3! = 18; next is A (0 * 2! = 0); next is N, before N is K -> 1 * 1! = 1; last is K -> +1. Rank = 18 + 0 + 1 + 1 = 20.
</details>

---

## CAT 2025 PYQ Edge Examples & Newly Surfaced Patterns

### Newly Surfaced Sub-Topic Variants & Pattern Triggers (CAT 2025)
- **3-Set Inclusion-Exclusion Extrema with Strict Positivity Constraint (`CAT_2025_QA_Slot_3` / `CAT2025_S3_QA_Q04`)**: When a Venn region $x = |A \cap B \cap C|$ is stated to be *some students* ($x \ge 1$), maximizing an expression in $-x$ requires setting $x = 1$ (NOT $x = 0$) while checking non-negativity of all 7 region expressions.
- **'Up to $k$' Combinatorial Case Summation (`CAT_2025_QA_Slot_1` / `CAT2025_S1_QA_Q08`)**: 'Up to 2 sauces from 10' equals $\binom{10}{0} + \binom{10}{1} + \binom{10}{2} = 1 + 10 + 45 = 56$; never omit the zero-selection case $\binom{n}{0} = 1$.

### Solved CAT 2025 PYQ Edge Exemplars

#### CAT2025_S1_QA_Q08 (`CAT_2025_QA_Slot_1` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Permutations & Combinations — *Fundamental multiplication rule with 'up to k' combination cases*
- **Verified Answer**: `(C) 880` (5 sandwiches * 4 breads * 2 sizes * (6C0 + 6C1 + 6C2 sauces) = 40 * (1 + 6 + 15) = 40 * 22 = 880.)
- **Mental Trigger (`See X -> Do Y`)**: 'Optionally add up to 2 out of 6 sauces' means 0, 1, or 2 sauces: C(6,0) + C(6,1) + C(6,2) = 1 + 6 + 15 = 22.
- **First-Principles Method**: Choices for sandwich type = 5, bread = 4, size = 2. For sauces, 'up to 2' includes 0 sauces (1 way), 1 sauce (6 ways), or 2 sauces (15 ways), totaling 22 ways. Total orders = 5 * 4 * 2 * 22 = 880.
- **30-Second Exam-Hall Speed Shortcut**: Since 1 + 6 + 15 = 22 is a multiple of 11, the total number of orders must be divisible by 11. Among (A) 600, (B) 840, (C) 880, (D) 800, only 880 is divisible by 11!
- **Trap Alert & Boundary Condition**: Forgetting the 0-sauce case ('Optionally... up to 2') gives 40 * 21 = 840 (distractor B).

#### CAT2025_S3_QA_Q04 (`CAT_2025_QA_Slot_3` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Set Theory — *3-Set Inclusion-Exclusion optimization with strict positive intersection constraint*
- **Verified Answer**: `(C) 35` (Let |P n C| = |C n M| = k, |P n M| = 2k, and |P n M n C| = x >= 1. By Inclusion-Exclusion: 150 = 75 + 111 + 40 - 4k + x => 4k - x = 76. To maximize |P \ M| = 75 - 2k, minimize k. Since x = 4k - 76 >= 1, 4k >= 77 => k >= 20 (at k=20, x=4, all regions >= 0). Thus max(75 - 2k) = 75 - 40 = 35.)
- **Mental Trigger (`See X -> Do Y`)**: Write |P \ M| = |P| - |P n M| = 75 - 2k; to maximize 75 - 2k, minimize k subject to x = 4k - 76 >= 1!
- **First-Principles Method**: Sum of singletons = 75 + 111 + 40 = 226. Sum of pairwise intersections = k + k + 2k = 4k. By PIE, 150 = 226 - 4k + x => x = 4k - 76. Since x >= 1 and k is an integer, 4k >= 77 => k >= 20. At k = 20, x = 4, and |P \ M| = 75 - 2(20) = 35.
- **30-Second Exam-Hall Speed Shortcut**: 4k = 76 + x with x >= 1 => smallest multiple of 4 above 76 is 80 (k = 20, x = 4) => 75 - 2(20) = 35.
- **Trap Alert & Boundary Condition**: Ignoring 'at least one student chose all three subjects' (x >= 1) sets x = 0, k = 19, giving the trap answer 75 - 38 = 37 (or if k=20 -> 35).
