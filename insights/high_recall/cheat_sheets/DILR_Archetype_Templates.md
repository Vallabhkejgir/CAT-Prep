# Last-Mile Rapid-Revision Cheat Sheet: DILR Archetype Templates & Invariants

Draw these exact scratchpad templates and invariant equations in the first 60 seconds of each DILR set.

---

## 1. The 4-Minute Set-Selection & 6-Minute Bail-Out Checklist

1. **Bucket A (Solve First — Target 2 Sets in Min 04–26)**:
   - Familiar mathematical skeleton (3/4-Set Venn, Knockout Bracket, Round-Robin Table, Flow Network, Direct 2D Assignment Grid $\le 6 \times 4$).
   - Strong conservation law or $\ge 2$ deterministic anchors.
2. **Hard 6-Minute Bail-Out Gate**:
   - If at Minute $6$ into a set you have not locked $\ge 30\%$ of the grid or reduced branching to $\le 3$ parallel columns, **STOP and switch sets immediately**.

---

## 2. Template 1: 3-Set & 4-Set Venn Optimization

### Master Layer Equations
$$\text{(1) Headcount:} \quad E_1 + E_2 + E_3 + E_4 = U - E_0$$
$$\text{(2) Ticket Sum:} \quad E_1 + 2E_2 + 3E_3 + 4E_4 = S = |A| + |B| + |C| + |D|$$
$$\text{(3) Surplus Identity (Eq 2 } - \text{ Eq 1):} \quad \mathbf{E_2 + 2E_3 + 3E_4 = S - (U - E_0)}$$

### Instant Extrema Formulas (for Fixed $U - E_0 = N$ and Ticket Sum $S$)
- **3-Set ($E_2 + 2E_3 = S - N$)**:
  - $E_{3,\max} = \min\left(\left\lfloor \frac{S - N}{2} \right\rfloor,\; |A|,\; |B|,\; |C|\right)$
  - $E_{3,\min} = \max(0,\; S - 2N)$
- **4-Set ($E_2 + 2E_3 + 3E_4 = S - N$)**:
  - $E_{4,\max} = \min\left(\left\lfloor \frac{S - N}{3} \right\rfloor,\; |A|,\; |B|,\; |C|,\; |D|\right)$
  - $E_{4,\min} = \max(0,\; S - 3N)$
  - $(E_3 + E_4)_{\min} = \max(0,\; S - 2N)$ (pack surplus into $E_2$ with $E_1 = E_4 = 0$).

---

## 3. Template 2: Games & Tournaments (Knockout & Round-Robin)

### A. Seeded Knockout Bracket ($N = 2^k$ Players)
- **Total Matches** $= N - 1$; **Rounds** $= k$.
- **Pairing Invariant in Round with $M$ Players Remaining**:
  $$\text{Seed}_A + \text{Seed}_B = M + 1$$
  - **16-Player Quarters**:
    - $Q_1: \{1, 16, 8, 9\}$ | $Q_2: \{4, 13, 5, 12\}$ $\longrightarrow$ **Half A**
    - $Q_3: \{2, 15, 7, 10\}$ | $Q_4: \{3, 14, 6, 11\}$ $\longrightarrow$ **Half B**
- **Upset Rule**: When worse seed $W$ beats better seed $B$ ($W > B$), $W$ **inherits $B$'s exact bracket slot** for the rest of the tournament.

### B. Round-Robin League ($n$ Teams, $M = \binom{n}{2}$ Matches)
- $\sum W = \sum L = M - D$, while $\sum (\text{Draws Column}) = 2D$.
- $\sum \text{GF} = \sum \text{GA} \implies \sum \text{GD} = 0$.
- **Total Points**:
  - $2\text{–}1\text{–}0$ system: $\sum \text{Pts} = 2M$.
  - $3\text{–}1\text{–}0$ system: $\sum \text{Pts} = 3M - D$.
- **Top-$k$ Qualification Extrema ($n$ teams, 1 match each, no draws)**:
  - Max wins and STILL fail to be in Top $k$: $\left\lfloor (n - k - 1) + \frac{k}{2} \right\rfloor$ (Guarantee $= \text{this} + 1$).
  - Min wins to POSSIBLY qualify in Top $k$: $\left\lceil \frac{n - k}{2} \right\rceil$.

---

## 4. Template 3: Arrangements, Matrices & Scheduling

- **Put the Ordered Dimension in Column 1**: Always fix `Time/Day (Mon..Fri)`, `Rank (1..N)`, or `Floor (1..N)` in the leftmost column; add side-by-side `Case 1 | Case 2` sub-columns rather than erasing.
- **Gap Translation**: "$k$ slots between $A$ and $B$" $\implies |\text{Pos}(A) - \text{Pos}(B)| = k + 1$ (block span $= k + 2$).
- **Circular Linearization**: Break circle at Seat $1$ (facing inward) and write $1..N$ horizontally; for even $N$, opposite of Seat $i$ is $i \pm \frac{N}{2}$.

---

## 5. Template 4: Networks, Flows, Quantitative DI & Puzzles

- **Kirchhoff Node Conservation**: $\sum \text{Inflow}(v) = \sum \text{Outflow}(v) + \text{Demand}(v)$, and $\sum \text{Supply} = \sum \text{Demand}$.
- **Max-Flow Min-Cut**: Maximum flow from $S$ to $T$ equals the minimum capacity sum of forward edges across any cut separating $S$ from $T$.
- **Moving-Average Telescope ($w$-period window)**:
  $$x_{t+w} - x_t = w \cdot (A_{t+1} - A_t)$$
- **Scatter Plot Visual Ratios**:
  - On Y vs. X plot, ratio $\frac{Y}{X}$ is the **slope of the ray from the origin $(0,0)$**; difference $Y - X$ is vertical height above the $45^\circ$ line $Y = X$.
- **Unique Partition Sums from $\{1..9\}$**:
  - 2 numbers: $3=\{1,2\}$, $4=\{1,3\}$, $16=\{7,9\}$, $17=\{8,9\}$.
  - 3 numbers: $6=\{1,2,3\}$, $7=\{1,2,4\}$, $23=\{6,8,9\}$, $24=\{7,8,9\}$.

---

## 6. CAT 2025 Newly Surfaced DILR Set Templates & Triggers

| CAT 2025 Set | Archetype Variant | Instant Equation / Grid Setup & Trap Guard |
| :--- | :--- | :--- |
| `CAT2025_S1_DILR_SET1` & `S3_SET4` | Circular 7-Chair Ring / Modular Buck Game | Index seats $0..6 \pmod 7$; clockwise $+k$ and counterclockwise $-k$ satisfy $+3 \equiv -4 \pmod 7$ |
| `CAT2025_S1_DILR_SET3` | Radar + Bar Bilateral Tariff Charts | $\text{Export}(Y \to X) = \text{Import}(X \leftarrow Y) = \frac{\text{Tariff Revenue}_{X \leftarrow Y}}{\text{Tariff Rate}_{X \leftarrow Y}}$ |
| `CAT2025_S1_DILR_SET4` | 5-Station Train Segment Flow ($A\text{--}E$) | Segment occupancy $F(B\text{--}C) = F(A\text{--}B) - \text{Alight}(B) + \text{Board}(B)$; destination sum $\sum_{O} f(O, D) = \text{Alight}(D)$ |
| `CAT2025_S2_DILR_SET1` | Ball-Hoop Threshold Interval Ordering | Pass without ping $\implies d_B < d_H$; Ping $\implies d_B = d_H$; Stuck $\implies d_B > d_H$; sort rows/cols by ping/pass counts |
| `CAT2025_S2_DILR_SET3` | 4-Author Multi-Paper Hypergraph | $\sum_{\text{authors}} (\text{papers with } k \text{ authors}) = k \times (\text{Total } k\text{-author papers})$ |
| `CAT2025_S3_DILR_SET1` | Bipartite Call-Flow Conservation Table | $\sum \text{Out}(X \to Y) = \sum \text{In}(Y \leftarrow X)$ and $\sum \text{Out}(X \to X) = \sum \text{In}(X \leftarrow X)$ |
| `CAT2025_S3_DILR_SET3` | Cumulative Step-Function Progress Charts | Vertical slice at $t = t_0$ gives cumulative solved count; matching step-up timestamps between Total and Category charts identifies task type |
| `CAT2025_S3_DILR_SET5` | Normalized Trade Balance (NTB) Matrix | $\text{NTB} = \frac{E - I}{E + I} = k \implies \frac{E}{I} = \frac{1+k}{1-k}$ and $\sum_{\text{all}} (E_i - I_i) = 0$ |
