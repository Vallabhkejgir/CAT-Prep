# DILR 01: Set Selection & The 4-Minute Scanning Framework

**Canonical Taxonomy Mapping**: `DILR > Cross-Archetype Execution & Set Selection`  
**Target Percentile Benchmarks**:
- **95%ile**: ~1.5 Sets (7–8 net correct questions)
- **99%ile**: ~2.0–2.5 Sets (10–12 net correct questions)
- **99.8+%ile**: ~3.0+ Sets (14–16 net correct questions)

---

## 1. Visual & Structural Anatomy

In a 40-minute CAT DILR section (typically 4 sets of 5 questions or 5 sets of 4 questions = 20 questions), **set selection accounts for 70% of your percentile outcome**. Even a 99.9%iler cannot brute-force a poorly chosen trap set in under 18 minutes, whereas picking the two cleanest sets guarantees a 99%ile+ score with 10+ minutes to spare.

### The 40-Minute Clock Architecture
```text
[Min 00–04]  Full-Section Radar Scan (Classify all sets into Bucket A / B / C)
[Min 04–15]  Set #1 (Bucket A Sitter) -> Check 6-Min Bailout Gate at Min 10!
[Min 15–27]  Set #2 (Bucket A/B Doable) -> Check 6-Min Bailout Gate at Min 21!
[Min 27–37]  Set #3 (Full solve OR cherry-pick 2 independent/TITA questions)
[Min 37–40]  Zero-Blank TITA Sweep + Conservation/Constraint Audit
```

---

## 2. Green Flags vs. Red Flags (The 60-Second Per-Set Triage)

| Feature | GREEN FLAGS (Bucket A — Attack First) | RED FLAGS (Bucket C — Skip Initially) |
| :--- | :--- | :--- |
| **Archetype Familiarity** | Standard 3/4-Set Venn, Seeded Knockout Bracket, Round-Robin Points Table, Missing-Value Conservation Table, 2D Bi-directional Grid ($\le 5 \times 5$) | Unfamiliar multi-stage game rules, recursive state transitions, 3D spatial folding, or custom rules taking $>3$ min just to understand |
| **Variable Count & Domain** | 2–3 attributes, small finite integer domains (e.g., $\{1, 2, 3, 4, 5\}$), explicit **distinctness** or **row/column sums** | $\ge 5$ loosely coupled attributes, continuous/unbounded numbers, or missing totals with no conservation law |
| **Clue Density & Anchors** | At least 2 **absolute/deterministic anchors** ("A sits at #1 and scores 40") plus strong negative/extreme constraints ("F scores the highest") | All clues are conditional ("If A is in P, then either B or C is in Q") with 4+ initial branches |
| **Question Stem Structure** | Independent "If..." questions or TITA questions solvable from partial table completion | Every MCQ has **"Cannot be determined"** as Option D, AND questions ask "How many arrangements are possible?" |

---

## 3. Scratchpad Representation Template

Never start jotting disorganized clues on rough paper. Reserve **one full clean page per DILR set** divided into 3 zones:

```text
+-----------------------------------------------------------------------+
| ZONE 1: INVARIANTS & DOMAIN HEADER (Top 15% of Page)                  |
| Entities: A, B, C, D, E, F | Domain: {10, 20, 30, 40, 50, 60} (Sum=210)|
| Key Rule: No two adjacent sum to 70; Distinct = YES; Zero allowed = NO|
+--------------------------------------------------+--------------------+
| ZONE 2: MASTER GRID / PARALLEL CASE TABLE (65%)  | ZONE 3: SYMBOLIC   |
|                                                  | SECONDARY CLUES    |
| Entity | Attr 1 | Attr 2 | Case 1   | Case 2     | (20% Right Margin) |
| -------+--------+--------+----------+----------- |                    |
|   A    |        |        |          |            | [1] B > D + 20     |
|   B    |        |        |          |            | [2] C != Slot 3    |
|   C    |        |        |          |            | [3] E <-> F adj    |
|   D    |        |        |          |            | (Cross off each    |
|   E    |        |        |          |            |  clue once merged  |
|   F    |        |        |          |            |  into Zone 2!)     |
| -------+--------+--------+----------+----------- |                    |
| TOTAL  |  210   |        |          |            |                    |
+--------------------------------------------------+--------------------+
```

---

## 4. Anchor Clue & Case-Splitting Rules

1. **The Golden Anchor Selection Rule**:
   - Scan all numbered clues before writing anything. Pick the **most connected entity** (appears in 3+ clues) or the **most restricted sum/product clue** (e.g., "C's score is a perfect square $> 50$").
2. **Parallel Column Splitting (Never Erase!)**:
   - When a key anchor narrows to 2 possibilities ($X = 20$ or $X = 40$), **do not guess one and mentally hold the other**. Immediately draw two sub-columns (`Case 1` | `Case 2`) inside the same master table and propagate both until one hits a contradiction.
3. **The 6-Minute Hard Bail-Out Rule**:
   - Check the clock **6 minutes** after starting a set.
   - **Continue** if and only if: (a) your master table is drawn, (b) all clues are translated into symbols, and (c) at least 30–40% of cells are locked or narrowed to $\le 2$ cases.
   - **Bail Out Immediately** if: you are still re-reading the prompt, have $> 4$ open cases, or realized you misread a foundational rule.

---

## 5. Mathematical Invariants (The Hidden Key in 80% of CAT DILR Sets)

Whenever a set appears to have "too few clues", look for one of these 5 mathematical invariants:
1. **Total Sum Conservation**: $\sum \text{Row Totals} = \sum \text{Column Totals} = \text{Grand Total}$.
2. **Unique Partition Sums**: e.g., $3$ distinct numbers from $\{1, 2, 3, 4, 5, 6, 7, 8, 9\}$ summing to $6$ MUST be $\{1, 2, 3\}$; summing to $24$ MUST be $\{7, 8, 9\}$.
3. **Parity & Divisibility**: Even $+$ Even $=$ Even; a mean of $k$ integers being an integer requires the sum to be a multiple of $k$.
4. **Extreme-Value Squeeze (Sandwich Principle)**: If $\sum_{i=1}^5 x_i = 50$ and each $x_i \le 12$, then even if four variables take their maximum ($4 \times 12 = 48$), the fifth variable MUST be $\ge 2$.
5. **Question-Stem Reverse Engineering**: Sometimes Question 1 says *"What is the sum of scores of B and D?"* with options `35, 37, 39, 41`, while Question 3 says *"If A scores 15..."* — telling you that A's score is **not uniquely fixed** by the base clues alone, so don't waste 5 minutes trying to force a unique value for A!

---

## 6. Solved Archetype Walkthrough: The 4-Minute Triage & Unique-Sum Lock

> **Mini-Set Scenario**: Five friends (P, Q, R, S, T) each pick 3 distinct balls from a bag containing 15 balls numbered $1$ to $15$ (no ball is replaced).
> - P's balls are all primes and sum to $10$.
> - Q's balls are consecutive integers summing to $42$.
> - R's balls are all multiples of $4$.
> - S's lowest ball is $9$ and T's highest ball is $7$.
> *Find the exact balls picked by each person.*

### Step-by-Step Execution
1. **Invariant & Domain Header**: Universe $= \{1, 2, \dots, 15\}$, partitioned into 5 disjoint triples. Grand sum $= \frac{15 \times 16}{2} = 120$.
2. **Lock Deterministic Partition Clues First**:
   - **P (3 distinct primes summing to 10)**: Primes in $\{1..15\}$ are $\{2, 3, 5, 7, 11, 13\}$. Unique triple summing to $10$ is $\mathbf{\{2, 3, 5\}}$!
   - **Q (3 consecutive integers summing to 42)**: Middle integer $= \frac{42}{3} = 14 \implies \mathbf{\{13, 14, 15\}}$!
   - **R (3 multiples of 4 in $\{1..15\}$)**: Only three multiples of $4$ exist in $\{1..15\}$: $\mathbf{\{4, 8, 12\}}$!
3. **Remaining Universe**: $\{1, 6, 7, 9, 10, 11\}$ (6 numbers left for S and T).
4. **Apply Extreme Boundary Clues**:
   - S's lowest ball is $9 \implies$ all 3 of S's balls are $\ge 9$. From $\{1, 6, 7, 9, 10, 11\}$, the only three numbers $\ge 9$ are $\mathbf{\{9, 10, 11\}}$!
   - T gets the remaining three numbers: $\mathbf{\{1, 6, 7\}}$ (check: T's highest is $7$ — matches!).
- **Total Solve Time**: **90 seconds** for all 5 questions!

---

## 7. Active-Recall Drills

<details><summary>Q1: During the 4-minute scan, you notice all 5 MCQs in Set 2 have 'Cannot be determined' as Option D. How does this change your solving strategy?</summary>
A: It signals that the base constraints intentionally leave 2+ valid configurations open. Do NOT waste time trying to force a single unique table; keep parallel cases open and check whether the queried cell is invariant across cases or varies (making 'Cannot be determined' the correct answer).
</details>

<details><summary>Q2: Four distinct numbers from {1, 2, 3, 4, 5, 6, 7, 8, 9} sum to 11. Which numbers are definitely included?</summary>
A: Minimum sum of 4 numbers is 1 + 2 + 3 + 4 = 10. To get 11, only the 4 can increase by +1 to 5. Thus the 4 numbers are uniquely {1, 2, 3, 5}, so 1, 2, 3, and 5 are all definitely included.
</details>

<details><summary>Q3: What is the 6-Minute Bail-Out Rule in DILR?</summary>
A: If at 6 minutes into a set you have not placed a single deterministic anchor or narrowed the possibilities to at most 2-3 manageable cases, abort immediately and move to your next ranked set.
</details>

<details><summary>Q4: Five distinct positive integers have an average of 8 and the median is 9. What is the maximum possible value of the largest integer?</summary>
A: Total sum = 5 * 8 = 40. To maximize x_5 with x_3 = 9, minimize x_1, x_2, and x_4: set x_1 = 1, x_2 = 2, x_3 = 9, x_4 = 10 -> x_5 = 40 - (1 + 2 + 9 + 10) = 18.
</details>

<details><summary>Q5: When a DILR question stem starts with 'If B sits in chair 3, then...', what mistake must you avoid on the next question?</summary>
A: Never carry over a question-specific condition ('If B sits in chair 3') into subsequent questions! Write question-local conditions on a separate scratch line, never inside your master base table.
</details>
