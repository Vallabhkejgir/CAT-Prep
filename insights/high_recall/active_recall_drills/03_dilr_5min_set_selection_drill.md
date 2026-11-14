# High-Recall Drill 03: DILR 4-Minute Set Selection & Anchor Lock (10 Scenarios)

> **Companion Reference**: [`../cheat_sheets/DILR_Archetype_Templates.md`](../cheat_sheets/DILR_Archetype_Templates.md) | [`../../dilr_concept_examples/README.md`](../../dilr_concept_examples/README.md) | [`README.md`](./README.md)

**Instructions**: For each DILR set opening below, take **45 seconds** to decide:
1. **Bucket Classification**: **Bucket A** (Sitter — solve immediately), **Bucket B** (Doable — 2 cases, solve 2nd), or **Bucket C** (Trap/Time-Sink — skip initially).
2. **Scratchpad Template**: What exact rows/columns or equations you draw first.
3. **#1 Anchor Clue**: Which clue you plug in first and what it locks in 15 seconds.

---

<details><summary><b>Scenario 1: 6 Friends, 2 Telecom Operators (Xitel: Anu, Bijay; Yocel: Chetan, Deepak, Eshan, Faruq) — Partially Blank Outgoing/Incoming Call Table + 4 Zero-Call Clues (3 TITAs, 1 MCQ, no "CBD").</b></summary>

- **Bucket**: **Bucket A (#1 Sitter!)**
- **Scratchpad Setup**: Two separate conservation blocks: $2 \times 2$ Xitel block and $4 \times 4$ Yocel directed matrix.
- **#1 Anchor Lock**: Since Xitel has *only* Anu and Bijay, Anu's `Incoming from Xitel` IS `Bijay -> Anu` immediately! And $\sum \text{Out}(X \to Y) = \sum \text{In}(Y \leftarrow X)$ locks Anu's outgoing to Yocel in 10 seconds.
</details>

<details><summary><b>Scenario 2: 8 People around a circular table; some face center, some face outward; each likes a different IPL team and holds a different rank (1–8). All 7 clues are relative ("The person who likes CSK sits 2nd to the right of the person ranked 3rd"), and all 4 MCQs have "Cannot be determined" as Option D.</b></summary>

- **Bucket**: **Bucket C (Hard Skip!)**
- **Why Skip**: Unfixed circular orientation (inward/outward unknown) + $3$ attributes ($8 \times 3$) + zero absolute anchors + "Cannot be determined" on every question guarantees $\ge 15\text{–}20$ minutes of branching.
</details>

<details><summary><b>Scenario 3: Survey of 200 households on 4 streaming platforms (A=140, B=130, C=120, D=110). Everyone uses at least 1 platform. Q1 asks for max households using all 4; Q2 asks for min households using at least 3; Q3 gives E_4 = 30, E_1 = 40 and asks for E_2.</b></summary>

- **Bucket**: **Bucket A (Sitter — 4-minute mechanical solve!)**
- **Scratchpad Setup**: Write the Two Master Layer Equations + Surplus Identity:
  $E_1 + E_2 + E_3 + E_4 = 200$ and $E_2 + 2E_3 + 3E_4 = (140+130+120+110) - 200 = 300$.
- **#1 Anchor Lock**: $\max E_4 = \lfloor 300/3 \rfloor = 100$; for Q3, $E_2 + 2E_3 = 300 - 90 = 210$ and $E_2 + E_3 = 200 - 70 = 130 \implies E_3 = 80, E_2 = 50$.
</details>

<details><summary><b>Scenario 4: 6 Balls (B1..B6) tested on 4 Hoops (H1..H4); ball "pings" iff Diameter(Ball) <= Diameter(Hoop). Clue 1: Only B2 pings on H2. Clue 2: All except B3 ping on H1. Clue 3: B4 pings on H3, B1 does not. Clue 4: B1 and B6 ping on H4, B5 does not.</b></summary>

- **Bucket**: **Bucket A (Sitter — 90-second 1D chain!)**
- **Scratchpad Setup**: Single horizontal inequality line (`<=` for ping, `<` for no ping).
- **#1 Anchor Lock**: `B2 <= H2 < B4 <= H3 < B1 <= H4 < B5 <= H1 < B3` (with `H2 < B6 <= H4`). Locks 23 out of 24 cells in the $6 \times 4$ matrix immediately!
</details>

<details><summary><b>Scenario 5: 16-Player Seeded Knockout Tournament (Seeds 1..16). Clue 1: Exactly 3 upsets occurred. Clue 2: Seed 9 reached the Semi-Finals. Clue 3: Seed 2 won the tournament without any upset in Half B.</b></summary>

- **Bucket**: **Bucket A (Sitter!)**
- **Scratchpad Setup**: Standard 16-player top-down bracket tree (`Sum = 17` in R1, `9` in QF, `5` in SF).
- **#1 Anchor Lock**: Since Half B had $0$ upsets, all $3$ upsets happened in Half A! Seed $9$ is in Quarter-Bracket $\{1, 8, 9, 16\}$: for $9$ to reach SF, $9$ beat $8$ in R1 (**Upset #1**) and $9$ beat $1$ (or $16$ who upset $1$) in QF (**Upset #2**).
</details>

<details><summary><b>Scenario 6: 6 Lectures (P, Q, R, S, T, U) scheduled Mon–Sat in 6 rooms (101–106). Clue 1: P is 4 days before Room 105. Clue 2: Room 102 is on Wednesday. Clue 3: Exactly 2 days separate Q (in Room 101) and R.</b></summary>

- **Bucket**: **Bucket A/B (Fast 2-Case Grid)**
- **Scratchpad Setup**: Fix `Mon (1) .. Sat (6)` in Column 1, with `Case 1 | Case 2` sub-columns for Lecture and Room.
- **#1 Anchor Lock**: Clue 1 (`P is 4 days before Room 105`, difference $= 4$) has only **2 possibilities**: `(Mon=P, Fri=105)` or `(Tue=P, Sat=105)`!
</details>

<details><summary><b>Scenario 7: Radar Chart of Import Tariff Rates (%) + Bar Chart of Tariff Revenue ($) across 5 Countries (US, UK, France, India, Japan). 4 MCQs asking for bilateral Exports, Imports, and Trade Surplus/Deficit.</b></summary>

- **Bucket**: **Bucket A (Sitter — Pure Formula Lookup!)**
- **Scratchpad Setup**: Write the single formula at the top of your page: $\text{Export}(Y \to X) = \text{Import}(X \leftarrow Y) = \frac{\text{Tariff Bar of } X \text{ on } Y}{\text{Radar Rate \% of } X \text{ on } Y}$.
- **#1 Anchor Lock**: Do NOT convert all $20$ country pairs into a giant table! Only compute the 3–4 pairs asked in the questions.
</details>

<details><summary><b>Scenario 8: A 3D Rubik-like cube of 64 smaller cubes is painted according to 6 conditional rules depending on prime coordinates (x, y, z), then rotated 3 times and sliced along 2 diagonal planes.</b></summary>

- **Bucket**: **Bucket C (Instant Skip!)**
- **Why Skip**: 3D spatial visualization under non-standard coordinate rules + diagonal plane cuts is high-error and zero-partial-credit. Save for last only if 15 minutes remain.
</details>

<details><summary><b>Scenario 9: 5-Station Train Route (A -> B -> C -> D -> E), capacity 200. Ticket counts are multiples of 10. AB = BD = DE = 0, BC = 40, BE = 30. Segment C--D occupancy is 95% (190 seats). On segment D--E, 4/7 of reserved seats are from stations before C (A and B).</b></summary>

- **Bucket**: **Bucket A (Sitter!)**
- **Scratchpad Setup**: List the $\binom{5}{2} = 10$ origin-destination pairs ($AB, AC, AD, AE, BC, BD, BE, CD, CE, DE$) and cross out $AB=BD=DE=0$.
- **#1 Anchor Lock**: On segment $D\text{--}E$ ($AE + BE + CE$), $\frac{4}{7}$ are $AE + BE = AE + 30$. Since tickets are multiples of $10$ and $AE > 30$, $D\text{--}E$ must be a multiple of $70$ $\le 200$ with $AE + 30 \ge 70 \implies D\text{--}E = 140$, $AE + 30 = 80 \implies AE = 50, CE = 60$!
</details>

<details><summary><b>Scenario 10: 4 Musicians (A, B, C, D) train under 3 Gurus (M, S, R) between 2013 and 2024 (12 years). Span of Gurus is 2, 3, and 4 years. Clue 1: S trains at most 1 student/year. Clue 2: R did NOT train anyone in 2015–2018 or 2021–2024.</b></summary>

- **Bucket**: **Bucket B (High-ROI Structured Scheduling)**
- **Scratchpad Setup**: $12$-row table (`2013` to `2024`) with columns `Guru R | Guru S | Guru M`.
- **#1 Anchor Lock**: Clue 2 leaves R active ONLY in `2013–2014` ($2$ yrs) and `2019–2020` ($2$ yrs) $\implies$ **R's span is 2 years**! Clue 1 ($4$ students across $12$ years, $1$/yr) $\implies$ **S's span is 3 years** (`2013–15, 2016–18, 2019–21, 2022–24`), and **M's span is 4 years**!
</details>
