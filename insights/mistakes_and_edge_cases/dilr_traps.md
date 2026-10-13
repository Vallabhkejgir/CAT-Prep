# DILR Constraint Misinterpretations, Edge Cases & Trap Manual

In CAT DILR, a single misread constraint in Minute 2 can invalidate 12 minutes of work or cause a 4-question wipeout (`-4` instead of `+12`). Master these 12 recurring DILR traps to bulletproof your set execution.

---

## 1. Logical Quantifier & Constraint Traps

### Trap 1: "Must Be True" (Definitely True) vs. "Can Be True" (Possibly True)
- **The Trap**: Your grid narrows down to **2 valid cases** (Case 1 and Case 2). You look only at Case 1 and mark an option for *"Which of the following MUST be true?"*
- **The Rule**:
  - **MUST be true / Definitely true**: True in **EVERY** valid case ($\text{Case 1} \cap \text{Case 2}$).
  - **CAN be true / May be true**: True in **AT LEAST ONE** valid case ($\text{Case 1} \cup \text{Case 2}$).
  - **Definitely FALSE**: False in **EVERY** valid case.

### Trap 2: Asymmetric Conditional ("If A, then B" $\neq$ "If B, then A")
- **The Trap**: The prompt states *"Whenever Team X plays on Monday, Team Y plays on Tuesday"* ($X_{\text{Mon}} \implies Y_{\text{Tue}}$). You see Team Y playing on Tuesday and falsely conclude Team X played on Monday!
- **The Rule**:
  - $P \implies Q$ allows only two valid deductions:
    1. **Modus Ponens**: $P \text{ is true} \implies Q \text{ is true}$.
    2. **Contrapositive**: $Q \text{ is FALSE} \implies P \text{ is FALSE}$ (If Y does NOT play on Tuesday, X did NOT play on Monday).
  - Never assume the converse ($Q \implies P$) unless the prompt says *"if and only if"*!

### Trap 3: "Only" Placement (`Only A is in B` vs. `A is only in B`)
- **"Only engineers are in Club X"**: If someone is in Club X, they MUST be an engineer ($\text{Club X} \subseteq \text{Engineers}$), though some engineers may not be in Club X.
- **"Engineers are only in Club X"**: Every engineer is in Club X and nowhere else ($\text{Engineers} \subseteq \text{Club X}$), though Club X may also contain non-engineers.

### Trap 4: "Neither A nor B" vs. "Not Both A and B"
- **"Neither A nor B is selected"**: $0$ of $\{A, B\}$ selected ($\bar{A} \cap \bar{B}$).
- **"A and B are not both selected"** (or *"At most one of A and B"*): Either $0$ or $1$ of $\{A, B\}$ is selected ($\overline{A \cap B}$).

---

## 2. Numerical & Structural Assumptions Traps

### Trap 5: The Unstated "Zero / Empty Slot" Trap
- **The Trap**: A problem says *"20 coins are distributed among 4 boxes A, B, C, D such that A gets more than B..."* Students assume every box has $\ge 1$ coin.
- **The Rule**: Check whether the prompt states **"at least one" / "positive integer"** or allows **$0$ (empty box)**! In Venn diagrams and games, $0$ is frequently the hidden key to maxima/minima questions.

### Trap 6: The Unstated "Distinctness" Trap
- **The Trap**: *"Five students scored integer marks between 1 and 10 with an average of 7."* Students assume all 5 marks are distinct.
- **The Rule**: Never assume values are distinct unless the prompt explicitly states **"distinct"**, **"different"**, or **"no two scored the same"**! Conversely, when the prompt *does* state "distinct", circle `DISTINCT!` at the top of your scratchpad so you eliminate collisions immediately.

### Trap 7:Question-Local Condition Carry-Over (Contaminating the Master Table)
- **The Trap**: Question 2 says *"If P sits in Seat 4, who sits in Seat 1?"* You write `P = Seat 4` directly inside your master table, and then use `P = Seat 4` to answer Question 3 (*"Who sits in Seat 2?"*)!
- **The Rule**: **NEVER write question-stem `If...` conditions inside your Master Grid.** Draw a separate mini-column labeled `Q2 Only` for question-specific assumptions.

---

## 3. Data Interpretation & Chart-Reading Traps

### Trap 8: Declining Positive Growth Rate vs. Declining Absolute Value
- **The Trap**: A line graph shows YoY Revenue Growth Rate dropping from $+25\%$ in 2021 to $+15\%$ in 2022 to $+8\%$ in 2023. Students think revenue fell from 2021 to 2023.
- **The Rule**: Any positive growth rate ($> 0\%$) means the quantity **increased**! Revenue only decreases when the YoY growth rate is **negative ($< 0\%$)**.

### Trap 9: Cumulative (YTD) vs. Periodic Data
- **The Trap**: A table reports *"Cumulative Rainfall from Jan 1 to End of Month $k$"* ($10, 25, 45, 50\text{ cm}$), and asks for the month with the highest rainfall.
- **The Rule**: Subtract consecutive cumulative rows ($10, 15, 20, 5\text{ cm}$) before ranking or computing percentages!

### Trap 10: Base-Swap in Percentage Comparisons
- **The Trap**: Computing $\frac{\text{Exports} - \text{Imports}}{\text{Exports}}$ when "Trade Deficit as a % of Imports" requires **Imports** in the denominator.
- **The Rule**: Whatever follows the word **"of"** or **"than"** (*"as a percentage **of** X"*, *"more **than** Y"*) is ALWAYS the denominator.

### Trap 11: CAGR Period Count ($N$ Years vs. $N - 1$ Intervals)
- **The Trap**: Data is shown for `2019, 2020, 2021, 2022, 2023` (5 columns). Students divide or take the $5\text{th}$ root instead of $2023 - 2019 = \mathbf{4}$ compounding intervals!

### Trap 12: Round-Robin "Draws Column Sum" vs. "Number of Drawn Matches"
- **The Trap**: In a league table, summing the `Draws (D)` column across all teams gives $12$, so the student thinks $12$ matches were drawn.
- **The Rule**: Every drawn match involves **2 teams**, adding $+1$ to both teams' Draw counts. Thus:
  $$\text{Number of Drawn Matches} = \frac{\sum \text{Draws Column}}{2}$$
