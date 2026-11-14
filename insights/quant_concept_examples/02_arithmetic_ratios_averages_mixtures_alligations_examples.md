# QA 02 Concept & Formula Examples: Ratios, Proportions, Variation, Averages, Mixtures & Alligations

> **Companion Reference**: [`../topic_summaries/quant/02_arithmetic_ratios_averages_mixtures_alligations.md`](../topic_summaries/quant/02_arithmetic_ratios_averages_mixtures_alligations.md) | [`QA_Formula_and_Trigger_Book.md`](../high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md)

Every concept, formula, and pattern trigger from **QA 02** is explained below with plain-English intuition, clean single-concept numbers, a two-way walkthrough (direct formula vs. mental ratio intuition), and the #1 mistake to avoid.

---

## Concept 1: Equal Ratio Property (Linear Combination Theorem) & Zero-Sum Case

### 1. Concept & Formula in Plain English
If several fractions are all equal to the same multiplier $k$ ($\frac{a}{b} = \frac{c}{d} = \frac{e}{f} = k$), you can add (or take any weighted combination of) their numerators and divide by the exact same combination of their denominators, and the ratio **still equals $k$**—provided the combined denominator is not zero:
$$\frac{a}{b} = \frac{c}{d} = \frac{e}{f} = k \implies \frac{pa + qc + re}{pb + qd + rf} = k \quad (\text{when } pb + qd + rf \neq 0)$$
**Critical Zero-Sum Caveat**: In symmetric equations like $\frac{a}{b+c} = \frac{b}{c+a} = \frac{c}{a+b} = k$, if $a + b + c = 0$, the denominators sum to $0$, so you cannot divide by the sum! Instead, substitute $b + c = -a$ to get the second hidden value $k = \frac{a}{-a} = -1$.

### 2. When to Use It (Question Cue)
- *"If $\frac{a}{b+c} = \frac{b}{c+a} = \frac{c}{a+b} = k$, find all possible values of $k$."*

### 3. General Example (Clean Numbers, Single Concept)
> For non-zero real numbers $a, b, c$, if $\frac{a}{b + c} = \frac{b}{c + a} = \frac{c}{a + b} = k$, find all possible values that $k$ can take.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Case 1 ($a + b + c \neq 0$)**: Add all numerators and denominators using the Equal Ratio Property:
     $$k = \frac{a + b + c}{(b + c) + (c + a) + (a + b)} = \frac{a + b + c}{2(a + b + c)} = \mathbf{\frac{1}{2}}$$
  2. **Case 2 ($a + b + c = 0$)**: Here $b + c = -a$. Substitute into the first fraction:
     $$k = \frac{a}{b + c} = \frac{a}{-a} = \mathbf{-1}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Pick three equal numbers: $a = 1, b = 1, c = 1 \implies k = \frac{1}{1+1} = \mathbf{\frac{1}{2}}$.
  2. Pick three non-zero numbers that add up to zero: $a = 1, b = 1, c = -2 \implies k = \frac{1}{1 + (-2)} = \mathbf{-1}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Cancelling $(a + b + c)$ blindly and reporting only $k = \frac{1}{2}$ while missing $k = -1$ when $a + b + c = 0$ is allowed.

---

## Concept 2: Componendo & Dividendo and Adding a Positive Constant to a Fraction

### 1. Concept & Formula in Plain English
- **Componendo & Dividendo**: If $\frac{a}{b} = \frac{c}{d}$, then the ratio of (Top $+$ Bottom) to (Top $-$ Bottom) on both sides is also equal:
  $$\frac{a + b}{a - b} = \frac{c + d}{c - d}$$
  Applying it a second time to $\frac{x + y}{x - y} = \frac{p}{q}$ immediately isolates $\frac{x}{y} = \frac{p + q}{p - q}$.
- **Adding $x > 0$ to Both Terms**: Adding the same positive number $x$ to both numerator and denominator pulls any positive fraction **closer to $1$**:
  - Proper fraction ($0 < a < b$): $\frac{a+x}{b+x} > \frac{a}{b}$ (increases toward $1$).
  - Improper fraction ($a > b > 0$): $\frac{a+x}{b+x} < \frac{a}{b}$ (decreases toward $1$).

### 2. When to Use It (Question Cue)
- *"If $\frac{3x + 4y}{3x - 4y} = \frac{7}{3}$, find $\frac{x}{y}$."*
- *"Which is larger: $\frac{3}{5}$ or $\frac{3+2}{5+2} = \frac{5}{7}$?"*

### 3. General Example (Clean Numbers, Single Concept)
> Solve for $\frac{x}{y}$ given that $\frac{x + y}{x - y} = \frac{7}{3}$. Also determine whether $\frac{7 + 5}{3 + 5}$ is greater than or less than $\frac{7}{3}$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Apply Componendo & Dividendo to $\frac{x+y}{x-y} = \frac{7}{3}$:
     $$\frac{(x+y) + (x-y)}{(x+y) - (x-y)} = \frac{7 + 3}{7 - 3} \implies \frac{2x}{2y} = \frac{10}{4} \implies \frac{x}{y} = \mathbf{\frac{5}{2}}$$
  2. Since $\frac{7}{3} > 1$ is an improper fraction, adding $+5$ to top and bottom moves it closer to $1$: $\frac{12}{8} = 1.5 < \frac{7}{3} \approx 2.33$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Think of $x + y = 7$ and $x - y = 3$. Then $x$ is the average $\frac{7+3}{2} = 5$ and $y$ is the half-gap $\frac{7-3}{2} = 2$, so $\frac{x}{y} = \mathbf{\frac{5}{2}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Assuming adding a positive number to top and bottom *always* increases a fraction—it increases proper fractions ($\frac{2}{3} \to \frac{3}{4}$) but **decreases** improper fractions ($\frac{3}{2} \to \frac{4}{3}$).

---

## Concept 3: Direct, Inverse & Joint/Partial Variation

### 1. Concept & Formula in Plain English
- **Direct Variation ($y \propto x$)**: $y = kx$ (double $x \implies$ double $y$).
- **Inverse Variation ($y \propto \frac{1}{x}$)**: $xy = k$ (double $x \implies$ halve $y$).
- **Partial / Joint Variation**: Many real-world costs have a **fixed component** $a$ plus a **variable component** $bx$ (e.g., $y = a + bx$). You cannot use simple cross-multiplication on total cost; you must subtract the two data points first to find the slope $b$.

### 2. When to Use It (Question Cue)
- *"Hostel expenses are partly fixed and partly vary directly with the number of boarders..."*

### 3. General Example (Clean Numbers, Single Concept)
> A hostel's monthly cost is partly fixed and partly varies directly with the number of students. When there are $20$ students, the total cost is Rs. $10,000$; when there are $30$ students, the total cost is Rs. $13,000$. Find the total cost when there are $50$ students.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Write the model $C = a + bN$.
  2. Plug in $(20, 10000)$ and $(30, 13000)$:
     $$a + 20b = 10,000 \quad \text{and} \quad a + 30b = 13,000$$
  3. Subtract: $10b = 3,000 \implies b = 300$, and $a = 10,000 - 20(300) = 4,000$.
  4. For $N = 50$: $C = 4,000 + 300(50) = \mathbf{\text{Rs. } 19,000}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Adding $10$ extra students ($20 \to 30$) raised the cost by Rs. $3,000$, so each extra student costs **Rs. $300$**.
  2. Going from $30$ students to $50$ students adds $20$ more students, costing $20 \times 300 = \text{Rs. } 6,000$ extra.
  3. Total cost $= 13,000 + 6,000 = \mathbf{\text{Rs. } 19,000}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Cross-multiplying $\frac{10,000}{20} \times 50 = 25,000$ as if the entire cost were directly proportional to the number of students.

---

## Concept 4: Partnership Capital-Time Ratio

### 1. Concept & Formula in Plain English
In a business partnership, profit is shared in the ratio of **Capital $\times$ Time** invested by each partner (measured in Rupee-Months):
$$\text{Profit Ratio} = (C_1 \times T_1) : (C_2 \times T_2) : (C_3 \times T_3)$$
If a partner changes their capital mid-year, simply add the Rupee-Months of each period ($C_{\text{first}} T_{\text{first}} + C_{\text{second}} T_{\text{second}}$).

### 2. When to Use It (Question Cue)
- *"A starts a business with Rs. $40,000$. After $3$ months, B joins with Rs. $60,000$. How should they divide the annual profit?"*

### 3. General Example (Clean Numbers, Single Concept)
> A starts a business with Rs. $50,000$. After $4$ months, B joins with Rs. $75,000$. At the end of $1$ year ($12$ months), they earn a profit of Rs. $33,000$. Find B's share of the profit.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. A's capital stays for $T_1 = 12$ months; B's capital stays for $T_2 = 12 - 4 = 8$ months.
  2. $\text{Profit Ratio } A : B = (50,000 \times 12) : (75,000 \times 8)$.
  3. Divide capitals by $25,000$ ($2 : 3$) and times by $4$ ($3 : 2$):
     $$A : B = (2 \times 3) : (3 \times 2) = 6 : 6 = 1 : 1$$
  4. Wait—let's check: $50,000 \times 12 = 600,000$ and $75,000 \times 8 = 600,000$, so $A : B = 1 : 1$, meaning B gets $\frac{1}{2} \times 33,000 = \mathbf{\text{Rs. } 16,500}$!
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. B puts in $1.5\times$ as much money as A ($\frac{75}{50} = \frac{3}{2}$), but keeps it in for $\frac{2}{3}$ of the time ($\frac{8}{12} = \frac{2}{3}$).
  2. Since $\frac{3}{2} \times \frac{2}{3} = 1$, their effective contributions are identical ($1:1$), so B gets half the profit $= \mathbf{\text{Rs. } 16,500}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Multiplying B's capital by $4$ months ("joined after $4$ months") instead of the **$12 - 4 = 8$ months** B's money actually stayed in the business.

---

## Concept 5: Weighted Average & Assumed Mean Deviation Shortcut

### 1. Concept & Formula in Plain English
Instead of multiplying huge numbers to find a weighted average $A_{\text{avg}} = \frac{\sum n_i A_i}{\sum n_i}$, pick any convenient round number $M$ (the **Assumed Mean**) and only average the small surpluses/deficits $(A_i - M)$:
$$A_{\text{avg}} = M + \frac{\sum n_i (A_i - M)}{\sum n_i}$$

### 2. When to Use It (Question Cue)
- *"In a school, $30$ students of Section A average $78$ marks, and $20$ students of Section B average $83$ marks. Find the combined average."*

### 3. General Example (Clean Numbers, Single Concept)
> Section A has $30$ students with an average score of $78$, and Section B has $20$ students with an average score of $83$. Find the combined average score of all $50$ students.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Pick Assumed Mean $M = 78$ (and reduce student counts $30 : 20$ to weights $n_1 = 3, n_2 = 2$).
  2. Plug into $A_{\text{avg}} = M + \frac{n_1(A_1 - M) + n_2(A_2 - M)}{n_1 + n_2}$:
     $$A_{\text{avg}} = 78 + \frac{3(78 - 78) + 2(83 - 78)}{3 + 2} = 78 + \frac{0 + 10}{5} = \mathbf{80}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Direct weighted sum with reduced weights $3$ and $2$: $\frac{3(78) + 2(83)}{3 + 2} = \frac{234 + 166}{5} = \frac{400}{5} = \mathbf{80}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Taking the simple unweighted average $\frac{78 + 83}{2} = 80.5$ when the group sizes ($30$ and $20$) are unequal.

---

## Concept 6: Average Shift on Member Replacement or Inclusion

### 1. Concept & Formula in Plain English
Think of the average as every person holding an equal stack of coins:
- **Replacement** (group size stays $N$): If a person with $V_{\text{old}}$ leaves and a new person with $V_{\text{new}}$ enters, raising everyone's average by $\Delta A$, the new person had to match $V_{\text{old}}$ **plus** hand out $\Delta A$ to all $N$ members:
  $$V_{\text{new}} = V_{\text{old}} + N \cdot \Delta A$$
- **Inclusion** (group size grows from $N$ to $N+1$): The newcomer must bring the old average $A_{\text{old}}$ for themselves **plus** $\Delta A$ for all $(N + 1)$ members:
  $$V_{\text{new}} = A_{\text{old}} + (N + 1)\Delta A$$

### 2. When to Use It (Question Cue)
- *"The average weight of $10$ oarsmen increases by $1.5\text{ kg}$ when a $60\text{ kg}$ man is replaced by a new man..."*
- *"The average age of $11$ players is $25$ years. When the coach is included, the average increases by $1$ year..."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) The average weight of $10$ students increases by $2\text{ kg}$ when a student weighing $50\text{ kg}$ is replaced by a new student. Find the weight of the new student.
> (b) If instead a teacher joins the $10$ students (whose initial average was $50\text{ kg}$) and raises the group average by $2\text{ kg}$, find the teacher's weight.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a) Replacement**: $V_{\text{new}} = V_{\text{old}} + N \cdot \Delta A = 50 + 10(2) = \mathbf{70\text{ kg}}$.
  2. **Part (b) Inclusion**: $V_{\text{new}} = A_{\text{old}} + (N + 1)\Delta A = 50 + (10 + 1)(2) = \mathbf{72\text{ kg}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), total weight of $10$ people went up by $10 \times 2 = 20\text{ kg}$, so the newcomer is $20\text{ kg}$ heavier than the $50\text{ kg}$ person who left ($50 + 20 = \mathbf{70\text{ kg}}$).
  2. In (b), $10$ students totaled $10 \times 50 = 500\text{ kg}$; with the teacher, $11$ people average $52\text{ kg}$ for a total of $11 \times 52 = 572\text{ kg}$. Teacher $= 572 - 500 = \mathbf{72\text{ kg}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using $N$ instead of $(N + 1)$ when a new member **joins** the group without replacing anyone.

---

## Concept 7: Arithmetic Progression (AP) Average & Outlier Maximization

### 1. Concept & Formula in Plain English
- **AP Average = Middle Term**: For any Arithmetic Progression (like consecutive integers, odd numbers, or multiples), the average is simply the median $\frac{\text{First} + \text{Last}}{2}$. Appending $k$ next consecutive terms shifts the average up by $\frac{k \cdot d}{2}$.
- **Maximizing One Member of $N$ Distinct Positive Integers**: If the average of $N$ **distinct positive integers** is $A$ (so total sum $= N \cdot A$), to make one integer as large as possible, make the other $(N - 1)$ integers as small as possible: $1, 2, 3, \dots, (N - 1)$:
  $$\text{Max Possible Value} = N \cdot A - \frac{(N - 1)N}{2}$$

### 2. When to Use It (Question Cue)
- *"The average of $5$ distinct positive integers is $20$. What is the maximum possible value of the largest integer?"*

### 3. General Example (Clean Numbers, Single Concept)
> The average of $5$ distinct positive integers is $20$. Find the maximum possible value of the largest integer.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Given $N = 5$ and $A = 20$.
  2. Plug into $\text{Max} = N \cdot A - \frac{(N-1)N}{2}$:
     $$\text{Max} = 5(20) - \frac{4 \times 5}{2} = 100 - 10 = \mathbf{90}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Total sum of the $5$ integers $= 5 \times 20 = 100$.
  2. Since they must be *distinct* positive integers, the smallest the first $4$ integers can be is $1, 2, 3, 4$, which sum to $10$.
  3. That leaves $100 - 10 = \mathbf{90}$ for the 5th integer.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Setting the other $4$ integers to $1, 1, 1, 1$ (giving $96$) when the question specifies **distinct** positive integers.

---

## Concept 8: Alligation Seesaw / Lever Rule & The Denominator Unit Law

### 1. Concept & Formula in Plain English
When two groups with averages $A_1$ and $A_2$ are mixed to form a combined average $A_{\text{avg}}$, the quantities $n_1$ and $n_2$ balance like weights on a seesaw—the group **closer** to $A_{\text{avg}}$ has the **larger** weight:
$$\frac{n_1}{n_2} = \frac{A_2 - A_{\text{avg}}}{A_{\text{avg}} - A_1}$$
**The Golden Denominator Rule**: The ratio $n_1 : n_2$ is ALWAYS the ratio of the **denominator units** of $A_1, A_2$:
- Alligating **Rs./kg** gives the ratio of **kg**.
- Alligating **Profit $\%$ ($\text{Profit}/\text{CP}$)** gives the ratio of **Cost Prices ($\text{CP}$)**.
- Alligating **Speeds ($\text{km}/\text{hr}$)** gives the ratio of **Hours (Time)**, NEVER Distance!

### 2. When to Use It (Question Cue)
- *"A man travels partly at $30\text{ km/hr}$ and partly at $60\text{ km/hr}$, averaging $40\text{ km/hr}$ for the whole trip. Find the ratio of time (and distance) spent at each speed."*

### 3. General Example (Clean Numbers, Single Concept)
> A commuter covers a $120\text{ km}$ journey in $3\text{ hours}$ partly by bus at $30\text{ km/hr}$ and partly by train at $60\text{ km/hr}$. Find the time and distance traveled by bus.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Overall average speed $A_{\text{avg}} = \frac{120}{3} = 40\text{ km/hr}$, with $A_1 = 30$ and $A_2 = 60$.
  2. Apply the Alligation Rule to get the ratio of **Times** (since speed is $\text{km}/\mathbf{hr}$):
     $$\frac{t_{\text{bus}}}{t_{\text{train}}} = \frac{60 - 40}{40 - 30} = \frac{20}{10} = \frac{2}{1}$$
  3. Out of $3\text{ hours}$ total, $t_{\text{bus}} = \mathbf{2\text{ hours}}$, and Distance by bus $= 30 \times 2 = \mathbf{60\text{ km}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. If all $3\text{ hours}$ were by bus ($30\text{ km/hr}$), he would cover $90\text{ km}$.
  2. He actually covered $120\text{ km}$ ($+30\text{ km}$ extra). Each hour shifted from bus to train gains $60 - 30 = 30\text{ km}$.
  3. Thus $t_{\text{train}} = \frac{30}{30} = 1\text{ hr}$, leaving $t_{\text{bus}} = \mathbf{2\text{ hrs}}$ ($60\text{ km}$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Treating the alligation ratio $2 : 1$ of speeds as the ratio of **distances** ($\frac{2}{3} \times 120 = 80\text{ km}$) instead of the ratio of **times** ($2\text{ hrs} : 1\text{ hr}$).

---

## Concept 9: Combining Vessels with Different Capacities & Concentrations

### 1. Concept & Formula in Plain English
When vessels with Milk : Water ratios $a_1 : b_1$ and $a_2 : b_2$ are mixed in volume ratio $p : q$, you cannot add $a_1 + a_2$ directly until both ratios share the **same total unit size**. First scale each ratio to $\text{LCM}(a_1 + b_1,\; a_2 + b_2)$ so both represent equal volumes, and then multiply by the desired volume weights $p$ and $q$.

### 2. When to Use It (Question Cue)
- *"Two vessels of capacities in ratio $2 : 3$ contain milk and water in ratios $3 : 1$ and $2 : 3$. They are poured into a large drum. Find the final milk-to-water ratio."*

### 3. General Example (Clean Numbers, Single Concept)
> Vessel A and Vessel B have capacities in the ratio $2 : 3$. Vessel A contains milk and water in the ratio $3 : 1$, while Vessel B contains milk and water in the ratio $2 : 3$. If both are emptied into a third vessel, find the final ratio of milk to water.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in (LCM Scaling)**:
  1. Sum of parts: Vessel A has $3 + 1 = 4$ parts; Vessel B has $2 + 3 = 5$ parts.
  2. $\text{LCM}(4, 5) = 20$ units per base volume.
  3. Multiply by capacity weights $p = 2$ and $q = 3$:
     - Vessel A ($2 \times 20 = 40$ units): Scale $3:1$ by $\frac{40}{4} = 10 \implies 30\text{ Milk},\; 10\text{ Water}$.
     - Vessel B ($3 \times 20 = 60$ units): Scale $2:3$ by $\frac{60}{5} = 12 \implies 24\text{ Milk},\; 36\text{ Water}$.
  4. Total Milk : Total Water $= (30 + 24) : (10 + 36) = 54 : 46 = \mathbf{27 : 23}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Milk fraction in A is $\frac{3}{4}$ and in B is $\frac{2}{5}$.
  2. Weighted milk out of $2 + 3 = 5$ liters: $2\left(\frac{3}{4}\right) + 3\left(\frac{2}{5}\right) = \frac{3}{2} + \frac{6}{5} = \frac{27}{10}\text{ L}$ out of $5\text{ L} = \frac{50}{10}\text{ L}$.
  3. If $27$ parts out of $50$ are Milk, the remaining $50 - 27 = 23$ parts are Water $\implies \mathbf{27 : 23}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Multiplying $3:1$ by $2$ ($\to 6:2$) and $2:3$ by $3$ ($\to 6:9$) without first equalizing their base sums ($4$ and $5$) to $\text{LCM}(4,5) = 20$.

---

## Concept 10: Repeated Removal & Replacement (Dilution & Enrichment)

### 1. Concept & Formula in Plain English
Every time you remove $x$ liters from a $V$-liter vessel and replace it with water, you remove a fraction $\frac{x}{V}$ of whatever pure milk was sitting inside, leaving $\left(1 - \frac{x}{V}\right)$ of the milk behind. After $n$ identical replacements:
$$\text{Final Fraction of Undiluted Component } C_{\text{final}} = C_0 \left(1 - \frac{x}{V}\right)^n$$
**Crucial Rule**: Always apply this formula to the component that is **only being removed** (never added). If a step replaces mixture with *pure acid* ($100\%$), apply the multiplicative factor to the **water** fraction during that step!

### 2. When to Use It (Question Cue)
- *"From a $50\text{ L}$ cask of pure milk, $10\text{ L}$ is drawn out and replaced with water twice. Find the final milk-to-water ratio."*

### 3. General Example (Clean Numbers, Single Concept)
> From a container full of pure milk, $8\text{ L}$ is drawn out and replaced with water. This operation is performed one more time ($2$ times in total). The final ratio of milk to water in the container is $16 : 9$. Find the capacity $V$ of the container.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Final Milk : Water $= 16 : 9 \implies$ Final Milk **fraction of total volume** is $C_{\text{final}} = \frac{16}{16 + 9} = \frac{16}{25}$.
  2. Initial pure milk means $C_0 = 1$, $x = 8$, and $n = 2$:
     $$\left(1 - \frac{8}{V}\right)^2 = \frac{16}{25} \implies 1 - \frac{8}{V} = \frac{4}{5} \implies \frac{8}{V} = \frac{1}{5} \implies V = \mathbf{40\text{ L}}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Out of $16 + 9 = 25$ parts total, Milk shrank from $25$ to $16$ in two equal percentage steps.
  2. Since $\sqrt{\frac{16}{25}} = \frac{4}{5}$, each step kept $\frac{4}{5}$ of the liquid and removed $\frac{1}{5}$ of the container.
  3. Since $\frac{1}{5}$ of the container is $8\text{ L}$, full container $= 5 \times 8 = \mathbf{40\text{ L}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Setting $\left(1 - \frac{x}{V}\right)^2 = \frac{16}{9}$ instead of $\frac{16}{16 + 9} = \frac{16}{25}$ (the formula always gives Milk divided by **Total Volume**, not Milk divided by Water!).

---

## Concept 11: Two-Vessel Equilibrium Swap & Symmetric Transfer Invariant

### 1. Concept & Formula in Plain English
1. **Simultaneous Equilibrium Swap ($x^* = \frac{V_A V_B}{V_A + V_B}$)**: If Vessel A has $V_A\text{ L}$ of pure milk and Vessel B has $V_B\text{ L}$ of pure water, and $x\text{ L}$ are drawn from each simultaneously and swapped so both vessels end up with the **exact same concentration**, the required swap volume is half the harmonic mean:
   $$x^* = \frac{V_A V_B}{V_A + V_B}$$
2. **Sequential Back-and-Forth Transfer ($V : v$ Invariant)**: If two vessels $A$ (pure alcohol, volume $V$) and $B$ (pure water, volume $V$) have equal initial volume $V$, and you pour $v\text{ L}$ from $A \to B$, mix well, and pour $v\text{ L}$ back from $B \to A$, the final ratio of Alcohol : Water in $A$ is simply **$V : v$**.

### 2. When to Use It (Question Cue)
- *"Vessel A has $30\text{ L}$ milk and Vessel B has $20\text{ L}$ water. Equal quantities $x$ are swapped so both have the same concentration. Find $x$."*
- *"Two $60\text{ L}$ jars hold pure alcohol and pure water. $v\text{ L}$ is poured from A into B, and then $v\text{ L}$ of the mixture is poured back into A..."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) Vessel A contains $30\text{ L}$ of pure milk and Vessel B contains $20\text{ L}$ of pure water. What volume $x$ must be simultaneously swapped between them so both vessels reach the same milk concentration?
> (b) If both vessels initially hold $60\text{ L}$ ($A$ pure alcohol, $B$ pure water), and $15\text{ L}$ is poured from $A \to B$ and then $15\text{ L}$ of the mixture in $B$ is poured back into $A$, what is the final ratio of alcohol to water in $A$?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: $x^* = \frac{V_A V_B}{V_A + V_B} = \frac{30 \times 20}{30 + 20} = \frac{600}{50} = \mathbf{12\text{ L}}$.
  2. **Part (b)**: By the Sequential Symmetric Transfer Identity $V : v$, the final ratio in $A$ is $60 : 15 = \mathbf{4 : 1}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. **Part (a)**: When both vessels reach identical concentration, it is the same as pouring all $30\text{ L}$ milk and $20\text{ L}$ water into one giant $50\text{ L}$ vat ($\frac{30}{50} = 60\%$ milk) and refilling the $20\text{ L}$ Vessel B with $60\%$ milk. So Vessel B must end up with $60\%$ of $20\text{ L} = \mathbf{12\text{ L}}$ of milk—which came directly from the swap $x$!
  2. **Part (b)**: After pouring $15\text{ L}$ into $B$, $B$ has $15\text{ L}$ alcohol and $60\text{ L}$ water (ratio $1:4$). Pouring $15\text{ L}$ back into $A$ carries $\frac{1}{5}(15) = 3\text{ L}$ alcohol and $\frac{4}{5}(15) = 12\text{ L}$ water. So $A$ has $(60 - 15 + 3) = 48\text{ L}$ alcohol and $12\text{ L}$ water $\implies 48 : 12 = \mathbf{4 : 1}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Confusing the **simultaneous swap** ($x^* = \frac{V_A V_B}{V_A + V_B}$) with the **sequential pour-and-return** (where $B$'s volume temporarily expands to $V + v$ before pouring back).
