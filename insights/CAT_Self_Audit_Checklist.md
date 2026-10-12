# CAT 40-Minute Sectional Execution & Pre-Submission Self-Audit Checklist

Use this actionable checklist during mock tests, sectionals, and final exam-hall execution across **VARC (40 min)**, **DILR (40 min)**, and **QA (40 min)** to eliminate preventable negative marks, TITA blunders, and time-sink traps.

---

## 1. VARC (40 Minutes) — Execution & Tie-Breaker Protocol

### Time Allocation Blueprint
- **Minutes 00–26 (26 min): 4 RC Passages** (~6.5 min per passage: 3–3.5 min structural read + 3 min for 4 questions).
  - Rank passages in the first 45 seconds by **familiarity of abstract logic + question stem directness** (do not judge by topic keywords alone).
- **Minutes 26–40 (14 min): 8 VA Questions** (~1.5–1.75 min per question).
  - Prioritize **Para-Summary** and **Sentence Placement** (high accuracy if eliminated systematically), followed by **TITA Odd-One-Out** and **TITA Para-Jumbles** (zero negative marking — never leave a TITA blank).

### Pre-Lock Option Audit (The 2-Option Tie-Breaker)
When stuck between two close RC or Para-Summary options ($A$ vs. $B$), run this 5-second filter before clicking **Save & Next**:
- [ ] **Extreme Qualifier Check**: Does either option inject *always, never, only, exclusively, impossible, completely, main, primary* where the author used hedged language (*often, can, suggests, tends to*)?
- [ ] **Fake Comparison Check**: Does the option compare two entities ($X > Y$, *more than*, *less likely than*) when the passage mentioned both independently without ranking them?
- [ ] **Descriptive vs. Normative Shift**: Does the passage describe *what happens* (*is/was*), while the option prescribes *what ought to be done* (*should/must*)?
- [ ] **Tail-End Poison Check**: Did you read the **last 4 words** of the option? (High-difficulty CAT distractors match the passage for the first 80% of the sentence and slip in one false modifier at the end.)
- [ ] **Right Line, Wrong Question Check**: Is the option factually true according to Paragraph 2, but fails to answer the specific question stem (e.g., explains the *cause* when the stem asked for the *consequence*)?

### VA TITA Pre-Submission Check
- [ ] **Para-Jumble (4-digit TITA)**: Did you verify that your chosen opening sentence has **no dangling pronoun/demonstrative** (`this, such, they, however, also`) AND that your mandatory 2-sentence link cannot be reversed?
- [ ] **Odd-One-Out (1-digit TITA)**: Did you actually form a coherent 4-sentence paragraph with the remaining 4 sentences before locking the odd sentence?
- [ ] **Zero Blank TITAs**: Are all TITA questions filled with a valid digit sequence (`1234` format for PJ, single digit `1–5` for OOO) before the 40-minute clock expires?

---

## 2. DILR (40 Minutes) — Set Selection & Constraint Audit Protocol

### Time Allocation Blueprint
- **Minutes 00–04 (4 min): Full 4-Set / 5-Set Scan**
  - Classify every set into:
    - **Bucket A (Pick First)**: Familiar structure (4-Set Venn, Standard Arrangement/Grid, Tournament Table, Direct DI + Logic), $\le 5$ variables, deterministic anchor clues, at least 2 independent/TITA questions doable even with partial table completion.
    - **Bucket B (Attempt Second)**: Medium complexity, 1–2 controlled case splits (max 2–3 sub-cases).
    - **Bucket C (Red-Flag Trap — Skip Initially)**: Unbounded branching, combined optimization + missing data with "cannot be determined" options across all questions, or dense unfamiliar rules taking $>3$ minutes just to parse.
- **Minutes 04–16: Set 1** | **Minutes 16–28: Set 2** | **Minutes 28–40: Set 3 (or High-Yield Partial Questions)**
- **Hard Bail-Out Rule**: If at **Minute 6** into a set you have not placed a single deterministic anchor or reduced cases to $\le 3$, **abort immediately** and switch to your next ranked set.

### Pre-Lock Constraint & Misread Audit
Before locking any DILR set's answers, spend 30 seconds checking these 6 classic set-breakers:
- [ ] **"Must Be True" vs. "Can Be True"**: Did you answer a *Definitely True* question using only one of two valid cases?
- [ ] **"At Least" vs. "At Most" vs. "Exactly"**: Re-read every numerical constraint in the prompt header.
- [ ] **Zero / Empty Slot Assumption**: Did the prompt state *non-zero integers* or *positive integers*? If not, is $0$ allowed in a cell/bucket?
- [ ] **Unstated Uniqueness Trap**: Did the prompt explicitly say all values are *distinct*? Never assume distinctness unless stated.
- [ ] **Row vs. Column / Unit Swap**: In DI tables/charts, verify whether headers are in **lakhs vs. crores**, **percentages vs. percentage points**, or **cumulative vs. periodic (quarterly/annual)** figures.
- [ ] **Conservation Check**: Does the sum of your filled row/column entries match the grand total ($\sum \text{Wins} = \sum \text{Losses}$, $\sum \text{Inflow} = \sum \text{Outflow}$, $\sum T = E_1 + 2E_2 + 3E_3 + 4E_4$)?

---

## 3. QA (40 Minutes) — A-B-C Round Strategy & Domain Audit Protocol

### Time Allocation Blueprint (The 15–15–10 A-B-C Split)
- **Round 1 (Minutes 00–15) — Sitters Only ("A" Questions)**:
  - Scan all 22 questions sequentially. Solve **only** questions where the exact solution path is clear within 15 seconds and takes $< 90$ seconds to execute.
  - Mark doable-but-lengthy questions as **Mark for Review** (Round 2) and skip unfamiliar/heavy-algebra questions immediately.
- **Round 2 (Minutes 15–30) — Doable Mediums ("B" Questions)**:
  - Jump directly to Marked-for-Review questions. Use **Exam-Hall Speed Shortcuts** (value plugging, option elimination, ratio leverage, symmetry) before committing to long algebra.
- **Round 3 (Minutes 30–40) — Selected Hard / TITA sweeps ("C" Questions)**:
  - Pick 2–3 high-confidence remaining questions and ensure **every TITA question** has an entered numeric guess.

### Pre-Lock Mathematical Domain & Trap Audit
Before clicking **Save & Next** on any QA question, run this 10-second verification:
- [ ] **Target Variable Check**: Did you solve for $x$, when the question asked for $2x + 3$, the *remaining* work, the *percentage increase*, or the *number of possible values* of $x$?
- [ ] **Domain & Integer Type Check**:
  - **Natural numbers / Positive integers**: $\{1, 2, 3, \dots\}$ ($0$ is **excluded**).
  - **Whole numbers / Non-negative integers**: $\{0, 1, 2, 3, \dots\}$ ($0$ is **included**).
  - **Integers**: $\{\dots, -2, -1, 0, 1, 2, \dots\}$ (check **negative** divisors/roots!).
  - **Real numbers**: Do not assume variables are integers in AM-GM, quadratic, or inequality problems unless stated!
- [ ] **Logarithm & Denominator Validity**:
  - For $\log_b(f(x))$: Did you verify $f(x) > 0$, $b > 0$, and $b \neq 1$ for every root you found?
  - For rational equations $\frac{P(x)}{Q(x)} = 0$: Did you discard extraneous roots where $Q(x) = 0$?
  - For squaring both sides $\sqrt{f(x)} = g(x)$: Did you check $g(x) \ge 0$?
- [ ] **Geometry Non-Scale & Obtuse Check**:
  - Is a second configuration possible (e.g., **obtuse-angled triangle** where the altitude or circumcenter falls *outside* the triangle, or chords on the **same side vs. opposite sides** of the circle center)?
  - Did you verify the **Triangle Inequality** ($a + b > c$) before counting valid integral triangles?
- [ ] **TITA Entry Audit**:
  - Check units (hours vs. minutes, km vs. meters, $\text{cm}^2$ vs. $\text{m}^2$).
  - Double-check mental arithmetic on the final step (no options exist in TITA to catch a $\times 2$ or sign slip).
