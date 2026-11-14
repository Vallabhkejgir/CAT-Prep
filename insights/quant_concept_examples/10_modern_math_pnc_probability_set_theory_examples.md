# QA 10 Concept & Formula Examples: Permutations & Combinations, Probability & Set Theory

> **Companion Reference**: [`../topic_summaries/quant/10_modern_math_pnc_probability_set_theory.md`](../topic_summaries/quant/10_modern_math_pnc_probability_set_theory.md) | [`QA_Formula_and_Trigger_Book.md`](../high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md)

Every concept, formula, and pattern trigger from **QA 10** is explained below with plain-English intuition, clean single-concept numbers, a two-way walkthrough (direct formula vs. mental ratio intuition), and the #1 mistake to avoid.

---

## Concept 1: Fundamental Counting, 'Up to $k$' Selections, Tie Method (Together) & Gap Method (No Two Adjacent)

### 1. Concept & Formula in Plain English
1. **'Optionally / Up to $k$' Selections**: Choosing "up to $k$ toppings out of $n$" means $0, 1, 2, \dots,$ or $k$ toppings: $\binom{n}{0} + \binom{n}{1} + \dots + \binom{n}{k}$ (never forget $\binom{n}{0} = 1$ for the zero-topping choice!).
2. **Tie / String Method ($m$ items MUST be together)**: Tie all $m$ items into **$1$ super-item**. Arrange the $(n - m + 1)$ units in $(n - m + 1)!$ ways, then multiply by $m!$ for internal arrangements inside the tie.
3. **Gap Method (No two of $m$ items can be adjacent)**: First arrange the other $k$ items in $k!$ ways. That creates **$(k + 1)$ safe gaps** (including the two ends). Pick $m$ gaps out of $(k + 1)$ and arrange the $m$ items in them:
   $$k! \times \binom{k + 1}{m} \times m!$$

### 2. When to Use It (Question Cue)
- *"In how many ways can $5$ boys and $3$ girls be seated in a row so that (a) all $3$ girls sit together, or (b) no two girls sit together?"*

### 3. General Example (Clean Numbers, Single Concept)
> In how many ways can $5$ boys and $3$ girls be seated in a row if:
> (a) all $3$ girls sit together?
> (b) no two girls sit adjacent to each other?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a) Tie Method**: Tie the $3$ girls into $1$ block $[GGG]$. Together with the $5$ boys, there are $5 + 1 = 6$ units, arranged in $6!$ ways, times $3!$ inside the girl block:
     $$6! \times 3! = 720 \times 6 = \mathbf{4,320\text{ ways}}$$
  2. **Part (b) Gap Method**: Seat the $5$ boys first in $5!$ ways: `_ B _ B _ B _ B _ B _`, creating $5 + 1 = 6$ gaps.
     Choose $3$ gaps out of $6$ and arrange the $3$ girls:
     $$5! \times \binom{6}{3} \times 3! = 120 \times 20 \times 6 = \mathbf{14,400\text{ ways}}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (b), the 1st girl has $6$ gap choices, the 2nd girl has $5$, and the 3rd girl has $4$, so $120 \times (6 \times 5 \times 4) = \mathbf{14,400}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Subtracting $(n! - \text{All 3 Together})$ to find "No two girls adjacent" when there are $\ge 3$ girls! (Subtracting "all $3$ together" still leaves cases where **$2$ girls are together and $1$ is separate**—always use the **Gap Method** when $\ge 3$ items cannot be adjacent!).

---

## Concept 2: The 4-Box Distribution Matrix & Stars and Bars (Lower Bounds, Upper Bounds & Slack Inequality)

### 1. Concept & Formula in Plain English
Distributing **$n$ identical coins** among **$r$ distinct beggars** ($x_1 + x_2 + \dots + x_r = n$) is the same as arranging $n$ stars and $(r - 1)$ dividing bars:
- **Any beggar can get $0$ ($x_i \ge 0$)**: $\mathbf{\binom{n + r - 1}{r - 1}}$
- **Every beggar gets at least $1$ ($x_i \ge 1$)**: Pre-give $1$ coin to each beggar, leaving $n - r$ coins: $\mathbf{\binom{n - 1}{r - 1}}$
- **Inequality $x_1 + x_2 + \dots + x_r \le n$ ($x_i \ge 0$)**: Add a **"dummy/trash beggar" $s \ge 0$** who takes whatever coins are left over ($x_1 + \dots + x_r + s = n$ with $r + 1$ beggars): $\mathbf{\binom{n + r}{r}}$.
*(If the $n$ items are **distinct** and $r$ boxes are **distinct**, each item has $r$ choices $\implies \mathbf{r^n}$.)*

### 2. When to Use It (Question Cue)
- *"How many non-negative integer solutions exist for $x + y + z = 10$ (or $x + y + z \le 10$)?"*

### 3. General Example (Clean Numbers, Single Concept)
> Find the number of integer solutions $(x, y, z)$ to:
> (a) $x + y + z = 10$ with $x, y, z \ge 0$,
> (b) $x + y + z = 10$ with $x, y, z \ge 1$, and
> (c) $x + y + z \le 10$ with $x, y, z \ge 0$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $n = 10$ coins and $r = 3$ variables.
  2. **Part (a) Non-negative ($x_i \ge 0$)**: $\binom{10 + 3 - 1}{3 - 1} = \binom{12}{2} = \mathbf{66}$.
  3. **Part (b) Positive ($x_i \ge 1$)**: $\binom{10 - 1}{3 - 1} = \binom{9}{2} = \mathbf{36}$.
  4. **Part (c) Inequality ($\le 10, x_i \ge 0$)**: $\binom{10 + 3}{3} = \binom{13}{3} = \mathbf{286}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (b), hand $1$ coin to each of $x, y, z$ first ($3$ coins used). The remaining $7$ coins can be distributed freely: $\binom{7 + 3 - 1}{3 - 1} = \binom{9}{2} = \mathbf{36}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using Stars & Bars $\binom{n+r-1}{r-1}$ when the $n$ items are **distinct** (e.g., $10$ distinct chocolates to $3$ children is $3^{10}$, NOT $\binom{12}{2}$!).

---

## Concept 3: Circular Permutations ($(n-1)!$ vs. $\frac{(n-1)!}{2}$) & Unlabeled Equal-Size Group Division

### 1. Concept & Formula in Plain English
1. **Circular Arrangements of $n$ Distinct Objects**: Fix the 1st person as the anchor landmark; the remaining $(n - 1)$ people arrange around them in **$(n - 1)!$** ways.
   - If the circle can be **flipped over** (like a necklace or garland where clockwise and counter-clockwise are the same), divide by $2$: **$\frac{(n - 1)!}{2}$**.
2. **Dividing into Equal-Sized Unlabeled Groups**: When splitting $k \cdot m$ items into $k$ **unlabeled** bundles of size $m$ each, you must divide by **$k!$** to remove the artificial ordering of the $k$ identical-sized bundles:
   $$\text{Unlabeled Equal Groups} = \frac{(km)!}{(m!)^k \cdot \mathbf{k!}}$$

### 2. When to Use It (Question Cue)
- *"In how many ways can $6$ people be seated around a circular table?"*
- *"In how many ways can $6$ players be divided into $3$ unlabeled pairs to play tennis?"*

### 3. General Example (Clean Numbers, Single Concept)
> (a) In how many ways can $6$ people sit around a round table?
> (b) In how many ways can $6$ distinct players be divided into $3$ unlabeled pairs of $2$ players each?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: $(6 - 1)! = 5! = \mathbf{120\text{ ways}}$.
  2. **Part (b)**: Here $k = 3$ pairs of size $m = 2$:
     $$\frac{6!}{(2!)^3 \cdot 3!} = \frac{720}{8 \times 6} = \mathbf{15\text{ ways}}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (b), Player 1 can pick a partner in **$5$ ways**; the next unpaired player can pick a partner in **$3$ ways**; the last $2$ form the final pair in **$1$ way**: $5 \times 3 \times 1 = \mathbf{15\text{ ways}}$!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting to divide by $3!$ when the $3$ groups of $2$ are **unlabeled** (computing $\frac{6!}{2!2!2!} = 90$, which counts named Court 1, Court 2, Court 3 instead of just pairs!).

---

## Concept 4: Derangements ($D_n$) & Partial Derangements ($\binom{n}{k} D_{n-k}$)

### 1. Concept & Formula in Plain English
A **Derangement ($D_n$)** is an arrangement of $n$ items into $n$ matching slots (like $n$ letters into $n$ addressed envelopes) such that **zero items land in their own correct slot**:
$$D_1 = 0,\quad D_2 = 1,\quad D_3 = 2,\quad D_4 = 9,\quad D_5 = 44,\quad D_6 = 265$$
If a question asks for **exactly $k$ items in their correct slots**, first choose which $k$ items go right ($\binom{n}{k}$ ways) and derange the remaining $(n - k)$ items:
$$\text{Ways for exactly } k \text{ correct} = \binom{n}{k} \times D_{n - k}$$

### 2. When to Use It (Question Cue)
- *"In how many ways can $5$ letters be placed into $5$ addressed envelopes so that (a) none goes into the right envelope, or (b) exactly $2$ go into the right envelopes?"*

### 3. General Example (Clean Numbers, Single Concept)
> $5$ letters are placed at random into $5$ addressed envelopes. Find the number of ways in which:
> (a) no letter goes into its own correct envelope, and
> (b) exactly $2$ letters go into their own correct envelopes.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: From the memorized derangement sequence, $D_5 = \mathbf{44}$.
  2. **Part (b)**: Choose $2$ correct letters in $\binom{5}{2}$ ways and derange the other $3$ letters in $D_3 = 2$ ways:
     $$\binom{5}{2} \times D_3 = 10 \times 2 = \mathbf{20\text{ ways}}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Memorize the recursive shortcut $D_n = n \cdot D_{n-1} + (-1)^n$:
     $D_1 = 0 \to D_2 = 1 \to D_3 = 3(1)-1 = 2 \to D_4 = 4(2)+1 = 9 \to D_5 = 5(9)-1 = \mathbf{44}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Computing "no letter in its right envelope" as $5! - 1 = 119$ (that means *not all $5$ are right*, i.e., *at least one is wrong*, whereas derangement $D_5 = 44$ means **every single one is wrong**!).

---

## Concept 5: Geometric Counting (Collinear Points & Grid Rectangles/Squares) & Dictionary Rank

### 1. Concept & Formula in Plain English
1. **Points in a Plane ($n$ points, of which $m$ are collinear on one line)**:
   - **Straight Lines**: Every pair of points forms a line ($\binom{n}{2}$), except the $\binom{m}{2}$ pairs on the collinear line collapse into **$1$ single line**:
     $$\text{Lines} = \binom{n}{2} - \binom{m}{2} + 1$$
   - **Triangles**: Every triple forms a triangle ($\binom{n}{3}$), minus the $\binom{m}{3}$ collinear triples (which form **$0$** triangles):
     $$\text{Triangles} = \binom{n}{3} - \binom{m}{3}$$
2. **Grid of $m \times n$ Unit Squares ($m+1$ horizontal lines, $n+1$ vertical lines)**:
   - **Rectangles**: Pick any $2$ horizontal lines and any $2$ vertical lines: $\binom{m+1}{2}\binom{n+1}{2}$.
   - **Squares**: $\sum_{k=1}^{\min(m,n)} (m - k + 1)(n - k + 1)$.

### 2. When to Use It (Question Cue)
- *"There are $10$ points in a plane, $4$ of which are collinear. How many straight lines and triangles can be formed?"*
- *"How many rectangles and squares are there on a $4 \times 3$ grid?"*

### 3. General Example (Clean Numbers, Single Concept)
> (a) Out of $10$ points in a plane, $4$ are collinear. How many straight lines and how many triangles can be formed?
> (b) How many rectangles (including squares) and how many squares exist in a $4 \times 3$ grid of unit squares?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**:
     - Lines $= \binom{10}{2} - \binom{4}{2} + 1 = 45 - 6 + 1 = \mathbf{40\text{ lines}}$.
     - Triangles $= \binom{10}{3} - \binom{4}{3} = 120 - 4 = \mathbf{116\text{ triangles}}$.
  2. **Part (b)**: A $4 \times 3$ grid has $4 + 1 = 5$ vertical lines and $3 + 1 = 4$ horizontal lines.
     - Rectangles $= \binom{5}{2} \times \binom{4}{2} = 10 \times 6 = \mathbf{60\text{ rectangles}}$.
     - Squares $= (4 \times 3) + (3 \times 2) + (2 \times 1) = 12 + 6 + 2 = \mathbf{20\text{ squares}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), you can also count lines by cases: lines using $2$ non-collinear points ($\binom{6}{2} = 15$) $+$ lines joining $1$ non-collinear and $1$ collinear point ($6 \times 4 = 24$) $+$ the $1$ collinear line itself $= 15 + 24 + 1 = \mathbf{40}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting to add **$+1$** in the straight-line formula $\binom{n}{2} - \binom{m}{2} + 1$ (the $m$ collinear points still form $1$ line!), or falsely adding $+1$ in the triangle formula!

---

## Concept 6: Probability Rules, Independent vs. Mutually Exclusive Events & 'At Least One' Complement

### 1. Concept & Formula in Plain English
- **Union Rule**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
- **Mutually Exclusive (Disjoint)**: Cannot happen together $\implies P(A \cap B) = 0$.
- **Independent Events**: One happening does not affect the other $\implies P(A \cap B) = P(A) \cdot P(B)$.
- **'At Least One' Complement Shortcut**: For independent tries, the fastest way to find $P(\text{at least one succeeds})$ is $1 - P(\text{ALL fail})$:
  $$P(A \cup B) = 1 - P(A')P(B')$$

### 2. When to Use It (Question Cue)
- *"A and B independently try to solve a problem with probabilities $\frac{1}{2}$ and $\frac{1}{3}$. What is the probability that the problem is solved?"*

### 3. General Example (Clean Numbers, Single Concept)
> Three students $A, B, C$ independently attempt to solve a puzzle with success probabilities $\frac{1}{2}, \frac{1}{3},$ and $\frac{1}{4}$ respectively. What is the probability that the puzzle is solved (i.e., at least one student succeeds)?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in (Complement)**:
  1. Failure probabilities are $P(A') = \frac{1}{2}$, $P(B') = \frac{2}{3}$, and $P(C') = \frac{3}{4}$.
  2. Probability all three fail $= \frac{1}{2} \times \frac{2}{3} \times \frac{3}{4} = \frac{1}{4}$.
  3. Probability at least one solves it $= 1 - \frac{1}{4} = \mathbf{\frac{3}{4}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Out of $2 \times 3 \times 4 = 24$ equally weighted outcome branches, only $1 \times 2 \times 3 = 6$ branches have all three failing, so $24 - 6 = 18$ branches succeed ($\frac{18}{24} = \mathbf{\frac{3}{4}}$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Adding $P(A) + P(B) + P(C) = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} = \frac{13}{12} > 1$ (never add probabilities without subtracting overlaps—and remember non-zero mutually exclusive events are **never** independent!).

---

## Concept 7: Conditional Probability & Bayes' Theorem (Tree / 100-Sample Intuition)

### 1. Concept & Formula in Plain English
**Bayes' Theorem** flips a conditional probability around: given that an outcome $A$ was observed, what is the probability that it came from Cause $E_1$ rather than Cause $E_2$?
$$P(E_1 \mid A) = \frac{\text{Branch}(E_1 \text{ and } A)}{\text{Branch}(E_1 \text{ and } A) + \text{Branch}(E_2 \text{ and } A)} = \frac{P(E_1)P(A \mid E_1)}{P(E_1)P(A \mid E_1) + P(E_2)P(A \mid E_2)}$$

### 2. When to Use It (Question Cue)
- *"Bag 1 has $3$ red, $2$ blue balls; Bag 2 has $1$ red, $4$ blue balls. A bag is chosen at random and a red ball is drawn. What is the probability it came from Bag 1?"*

### 3. General Example (Clean Numbers, Single Concept)
> Box 1 contains $3$ Red and $2$ Blue balls ($60\%$ Red). Box 2 contains $1$ Red and $4$ Blue balls ($20\%$ Red). A fair coin is tossed to pick a box, and a ball drawn from it turns out to be Red. Find the probability that it came from Box 1.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. $P(B_1) = \frac{1}{2},\; P(R \mid B_1) = \frac{3}{5}$; and $P(B_2) = \frac{1}{2},\; P(R \mid B_2) = \frac{1}{5}$.
  2. Plug into Bayes' Theorem:
     $$P(B_1 \mid R) = \frac{\frac{1}{2} \times \frac{3}{5}}{\frac{1}{2} \times \frac{3}{5} + \frac{1}{2} \times \frac{1}{5}} = \frac{3}{3 + 1} = \mathbf{\frac{3}{4}}$$
- **Way 2 — Common-Sense / Ratio Intuition ($100$-Trial Count)**:
  1. Imagine $10$ draws: $5$ from Box 1 (giving **$3$ Red** balls) and $5$ from Box 2 (giving **$1$ Red** ball).
  2. Out of the $3 + 1 = 4$ Red balls drawn in total, $3$ came from Box 1 $\implies \mathbf{\frac{3}{4}}$!

### 5. The 1 Common Mistake to Avoid
- **Trap**: If a 6-sided die is rolled and a liar ($20\%$ lie rate) specifically reports *"It's a 6"*, when the roll is NOT a 6 ($\frac{5}{6}$ prior), the liar must both choose to lie ($20\%$) **AND** pick `"6"` out of the $5$ false numbers ($20\% \times \frac{1}{5}$)!

---

## Concept 8: Binomial Probability, Odd/Even Successes & Infinite Alternating Geometric Game

### 1. Concept & Formula in Plain English
1. **Binomial Formula ($r$ successes in $n$ trials)**: $P(X = r) = \binom{n}{r} p^r q^{n-r}$ ($q = 1 - p$).
2. **Odd vs. Even Number of Successes**:
   $$P(\text{Even}) = \frac{1 + (q - p)^n}{2}, \qquad P(\text{Odd}) = \frac{1 - (q - p)^n}{2}$$
   *(For a fair coin $p = q = \frac{1}{2}$, both are always $\frac{1}{2}$!)*
3. **Infinite Alternating Turn Game**: If $A$ and $B$ take turns trying to hit a target (win probabilities $p_A, p_B$, miss probabilities $q_A, q_B$) starting with $A$:
   $$P(A \text{ wins}) = \frac{p_A}{1 - q_A q_B}, \qquad P(B \text{ wins}) = \frac{q_A p_B}{1 - q_A q_B}$$

### 2. When to Use It (Question Cue)
- *"A and B alternately toss a coin, starting with A. The first to get a Head wins. Find their probabilities of winning."*

### 3. General Example (Clean Numbers, Single Concept)
> $A$ and $B$ take turns tossing a fair coin, starting with $A$. The first player to toss a Head wins the game. Find the probability that $A$ wins and the probability that $B$ wins.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $p_A = p_B = \frac{1}{2}$ and $q_A = q_B = \frac{1}{2}$.
  2. Plug into $P(A\text{ wins}) = \frac{p_A}{1 - q_A q_B}$:
     $$P(A\text{ wins}) = \frac{1/2}{1 - (1/2)(1/2)} = \frac{1/2}{3/4} = \mathbf{\frac{2}{3}}, \qquad P(B\text{ wins}) = 1 - \frac{2}{3} = \mathbf{\frac{1}{3}}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. If $A$ misses on Turn 1 ($\frac{1}{2}$ chance), $B$ is now in the exact same position $A$ started in!
  2. So $P(B) = \frac{1}{2} P(A)$ ($A$ is twice as likely to win as $B$). Since $P(A) + P(B) = 1$, $P(A) = \mathbf{\frac{2}{3}}$ and $P(B) = \mathbf{\frac{1}{3}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Thinking a fair coin means both players have a $\frac{1}{2}$ chance of winning—going **first** always gives player $A$ a strict advantage!

---

## Concept 9: 3-Set Inclusion-Exclusion & 'Exactly $k$ Sets' Layer Equations ($E_1, E_2, E_3$)

### 1. Concept & Formula in Plain English
Instead of labeling all $7$ individual Venn diagram regions when you only care about **how many sets** an element belongs to, define:
- $E_1 =$ elements in **exactly $1$** set
- $E_2 =$ elements in **exactly $2$** sets
- $E_3 =$ elements in **exactly $3$** sets ($|A \cap B \cap C|$)

Then two universal accounting equations solve 90% of CAT Venn problems in two lines:
1. **Headcount Equation**: $E_1 + E_2 + E_3 = |A \cup B \cup C| = N - E_0$
2. **Ticket/Badge Sum Equation**: $E_1 + 2E_2 + 3E_3 = |A| + |B| + |C|$
Subtracting $(2) - (1)$ immediately gives **$E_2 + 2E_3 = (|A| + |B| + |C|) - |A \cup B \cup C|$**!

### 2. When to Use It (Question Cue)
- *"In a club of $100$ members, $60$ play Cricket, $50$ play Football, $40$ play Tennis, and every member plays at least one sport. If $10$ play all three, how many play exactly two sports?"*

### 3. General Example (Clean Numbers, Single Concept)
> In a group of $100$ students, every student plays at least one of three games: $60$ play Cricket, $50$ play Football, and $40$ play Tennis. If $10$ students play all three games, how many students play **exactly two** games, and how many play **exactly one** game?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in (Layer Equations)**:
  1. Given $E_1 + E_2 + E_3 = 100$, $|A| + |B| + |C| = 60 + 50 + 40 = 150$, and $E_3 = 10$.
  2. Subtract the two layer equations:
     $$E_2 + 2E_3 = 150 - 100 = 50$$
  3. Substitute $E_3 = 10$: $E_2 + 2(10) = 50 \implies E_2 = \mathbf{30\text{ students}}$ (play *at least*... wait: play **exactly two** games!).
  4. Then $E_1 = 100 - E_2 - E_3 = 100 - 30 - 10 = \mathbf{60\text{ students}}$ (play **exactly one** game).
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. There are $100$ students holding $60 + 50 + 40 = 150$ club memberships ($50$ extra memberships).
  2. Each of the $10$ three-sport students holds $2$ extra memberships ($10 \times 2 = 20$ extras).
  3. The remaining $50 - 20 = \mathbf{30}$ extra memberships belong to the **$30$ students who play exactly $2$ sports**!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Confusing **"play both A and B"** ($|A \cap B|$, which *includes* $E_3$) with **"play A and B only"** (which *excludes* $E_3$). Also, if a question states *"some students chose all 3"* ($E_3 \ge 1$), never set $E_3 = 0$ when optimizing!

---

## Concept 10: $k$-Set Intersection Minimum (Surplus Rule) & Maximum

### 1. Concept & Formula in Plain English
Given the sizes of $k$ sets $|A_1|, |A_2|, \dots, |A_k|$ inside a universe of size $|U|$:
- **Maximum possible intersection $\max |A_1 \cap \dots \cap A_k|$**: Pack all sets on top of each other—limited only by the **smallest** set:
  $$\text{Max Intersection} = \min(|A_1|, |A_2|, \dots, |A_k|)$$
- **Minimum possible intersection $\min |A_1 \cap \dots \cap A_k|$ (Surplus / Non-Member Rule)**: Spread the non-members $|A'_i| = |U| - |A_i|$ completely apart so they never overlap! Thus the maximum number of people who can miss at least one set is $\sum (|U| - |A_i|)$, leaving:
  $$\text{Min Intersection} = \max\Big(0,\; \sum_{i=1}^k |A_i| - (k - 1)|U|\Big)$$

### 2. When to Use It (Question Cue)
- *"In a survey of $100$ people, $85$ like A, $80$ like B, and $75$ like C. Find the minimum and maximum number of people who like all three."*

### 3. General Example (Clean Numbers, Single Concept)
> In a survey of $100$ consumers, $85$ like Brand A, $80$ like Brand B, and $75$ like Brand C. Find the **minimum** and **maximum** possible number of consumers who like all three brands.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $k = 3$ sets and $|U| = 100$.
  2. **Minimum Intersection**:
     $$\sum |A_i| - (k - 1)|U| = (85 + 80 + 75) - (3 - 1)(100) = 240 - 200 = \mathbf{40}$$
  3. **Maximum Intersection**: $\min(85, 80, 75) = \mathbf{75}$.
- **Way 2 — Common-Sense / Ratio Intuition (Count the Haters!)**:
  1. Number of people who *dislike* A is $100 - 85 = 15$; dislike B is $20$; dislike C is $25$.
  2. Even if all those haters are completely different people, at most $15 + 20 + 25 = 60$ people dislike at least one brand.
  3. Therefore, at least $100 - 60 = \mathbf{40\text{ people}}$ must like **all three** brands!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Subtracting $k \cdot |U|$ instead of **$(k - 1)|U|$** in the minimum intersection formula!
