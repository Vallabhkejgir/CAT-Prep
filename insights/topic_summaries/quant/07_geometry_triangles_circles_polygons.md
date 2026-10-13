# QA 07: Geometry — Lines, Angles, Triangles, Circles, Quadrilaterals & Polygons

**Canonical Taxonomy Mapping**: `QA > Geometry & Mensuration > Lines, Angles & Triangles`, `Circles`, `Quadrilaterals & Polygons`  
**Weightage**: ~10–14% of QA (2–3 questions per slot)  
**Priority Tier**: Tier 1 (High-Yield Core)

---

## 1. 30-Second Concept & Formula Blueprint

### 1.1 Triangles: Inequalities, Classification, Area & Similarity
- **Existence & Angle Classification** (for sides $a \le b \le c$):
  - **Triangle Inequality**: $a + b > c \iff |a - b| < c < a + b$.
  - **Acute Triangle**: $a^2 + b^2 > c^2$ (must hold for the largest side $c$).
  - **Right Triangle**: $a^2 + b^2 = c^2$.
  - **Obtuse Triangle**: $a^2 + b^2 < c^2$.
  - **Number of Integral Triangles with Perimeter $P$**:
    - If $P$ is even: $\text{round}\left(\frac{P^2}{48}\right)$
    - If $P$ is odd: $\text{round}\left(\frac{(P+3)^2}{48}\right)$
- **Five Essential Area Formulas** (semi-perimeter $s = \frac{a+b+c}{2}$):
  $$\Delta = \frac{1}{2}bh = \frac{1}{2}ab\sin C = \sqrt{s(s-a)(s-b)(s-c)} = r \cdot s = \frac{abc}{4R}$$
  - For an **Equilateral Triangle** of side $a$: $h = \frac{\sqrt{3}}{2}a$, $\Delta = \frac{\sqrt{3}}{4}a^2$, $r = \frac{a}{2\sqrt{3}}$, $R = \frac{a}{\sqrt{3}}$ ($R : r = 2 : 1$).
  - For a **Right Triangle** with legs $a, b$ and hypotenuse $c$: $r = \frac{a + b - c}{2}$, $R = \frac{c}{2}$, altitude to hypotenuse $h = \frac{ab}{c}$.
- **Right-Triangle Altitude to Hypotenuse ($BD \perp AC$, dividing $AC$ into $AD = p, DC = q$)**:
  $$BD^2 = p \cdot q, \quad AB^2 = p \cdot (p + q), \quad BC^2 = q \cdot (p + q), \quad \frac{1}{BD^2} = \frac{1}{AB^2} + \frac{1}{BC^2}$$

---

### 1.2 The 4 Triangle Centers & Cevians
| Center | Intersection of | Key Metric / Ratio Property | Angle at Center (from $\angle A$) |
| :--- | :--- | :--- | :--- |
| **Incenter ($I$)** | Internal Angle Bisectors | Equidistant from **sides** ($r = \Delta/s$); $AI : ID = (b+c) : a$ | $\angle BIC = 90^\circ + \frac{\angle A}{2}$ |
| **Circumcenter ($O$)** | Perpendicular Bisectors | Equidistant from **vertices** ($R = \frac{abc}{4\Delta}$) | $\angle BOC = 2\angle A$ (or $360^\circ - 2\angle A$) |
| **Centroid ($G$)** | Medians | Divides each median in $2:1$; splits $\Delta$ into 6 equal-area sub-triangles | — |
| **Orthocenter ($H$)** | Altitudes | Euler Line: $O, G, H$ collinear with $OG : GH = 1 : 2$ | $\angle BHC = 180^\circ - \angle A$ |

- **Internal Angle Bisector Theorem** ($AD$ bisects $\angle A$, meeting $BC$ at $D$ with $BD = p, DC = q$):
  $$\frac{AB}{AC} = \frac{BD}{DC} \implies \frac{c}{b} = \frac{p}{q}, \quad \text{Length } AD^2 = bc - pq$$
- **Apollonius' Theorem (Median Length $m_a$ to side $a$)**:
  $$b^2 + c^2 = 2\left(m_a^2 + \left(\frac{a}{2}\right)^2\right) \implies m_a = \frac{1}{2}\sqrt{2b^2 + 2c^2 - a^2}$$
- **Stewart's Theorem** (any cevian $d$ to side $a$ split into $m, n$):
  $$b^2 m + c^2 n = a(d^2 + mn) \quad (\text{"man + dad = bmb + cnc"})$$
- **Ceva's & Menelaus' Theorems** (Replaced in 15 seconds by **Mass Point Geometry**):
  - Assign point masses $m_A, m_B, m_C$ to vertices so each fulcrum balances: $m_A \cdot d_A = m_B \cdot d_B$, with fulcrum mass $= m_A + m_B$.

---

### 1.3 Circles, Chords, Tangents & Polygons
- **Power of a Point (Intersecting Chords & Secants/Tangents from $P$)**:
  - Two chords intersecting at $P$: $PA \cdot PB = PC \cdot PD$.
  - Secant $PAB$ and Tangent $PT$: $PT^2 = PA \cdot PB = PO^2 - R^2$.
- **Alternate Segment Theorem**:
  Angle between tangent $PT$ and chord $TA$ equals the angle subtended by chord $TA$ in the alternate segment ($\angle PTA = \angle TBA$).
- **Common Tangents Between Two Circles** (centers distance $d$, radii $r_1 \ge r_2$):
  - **Direct Common Tangent**: $L_{\text{DCT}} = \sqrt{d^2 - (r_1 - r_2)^2}$ (when circles touch externally, $d = r_1 + r_2 \implies L_{\text{DCT}} = 2\sqrt{r_1 r_2}$).
  - **Transverse Common Tangent**: $L_{\text{TCT}} = \sqrt{d^2 - (r_1 + r_2)^2}$.
- **Cyclic Quadrilaterals** ($\angle A + \angle C = 180^\circ$):
  - **Ptolemy's Theorem**: $AC \cdot BD = AB \cdot CD + BC \cdot AD$.
  - **Brahmagupta's Area Formula**: $\Delta = \sqrt{(s-a)(s-b)(s-c)(s-d)}$.
- **Trapezium (Parallel sides $a, b$)**:
  - Diagonals divide trapezium into 4 triangles with areas $A_{\text{top}}, A_{\text{bottom}}, A_{\text{left}}, A_{\text{right}}$ where:
    $$A_{\text{left}} = A_{\text{right}} = \sqrt{A_{\text{top}} \cdot A_{\text{bottom}}}, \quad \text{Total Area} = \left(\sqrt{A_{\text{top}}} + \sqrt{A_{\text{bottom}}}\right)^2$$
  - Segment parallel to bases through intersection of diagonals has length **Harmonic Mean** $\frac{2ab}{a+b}$.
- **Regular Polygon ($n$ sides of length $a$)**:
  - Sum of interior angles $= (n-2)180^\circ$; Each interior angle $= 180^\circ - \frac{360^\circ}{n}$; Number of diagonals $= \frac{n(n-3)}{2}$.
  - **Regular Hexagon ($n=6$, side $a$)**: Decomposes into $6$ equilateral triangles of side $a$. Area $= \frac{3\sqrt{3}}{2}a^2$; short diagonal $= a\sqrt{3}$; long diagonal $= 2a$.

---

## 2. Pattern-Recognition Trigger Table

| Question Cue / Wording | Hidden Constraint | Fastest Attack Strategy |
| :--- | :--- | :--- |
| "Square inscribed in a right triangle of legs $a, b$ and hypotenuse $c$" | Two orientations exist: resting on legs vs. resting on hypotenuse | On legs: side $x = \frac{ab}{a+b}$ (larger!). On hypotenuse: side $y = \frac{ch}{c+h} = \frac{abc}{c^2 + ab}$ |
| "Three mutually tangent circles of radii $r_1, r_2$, and small circle $r$ wedged between them and their common tangent" | Ford Circle / Descartes Tangent Relation | $\frac{1}{\sqrt{r}} = \frac{1}{\sqrt{r_1}} + \frac{1}{\sqrt{r_2}}$ |
| "Series of circles inscribed inside a $60^\circ$ angle (or in an equilateral triangle)" | Radii form a Geometric Progression with common ratio $r_{k+1}/r_k = \frac{1 - \sin(\theta/2)}{1 + \sin(\theta/2)}$ | For $60^\circ$ ($\sin 30^\circ = 1/2$): radii are in GP with ratio $\frac{1}{3}$ (areas in ratio $\frac{1}{9}$) |
| "Cevian ratios given on two sides: $AD:DB = 2:3$ and $AE:EC = 4:1$; find $BF:FC$ and $AO:OF$" | Mass Point Geometry avoids all Menelaus algebra | Put mass $6$ at $A \implies m_B = 4, m_C = 24 \implies BF:FC = 24:4 = 6:1$, $AO:OF = (4+24):6 = 14:3$ |
| "Two parallel chords of lengths $2a$ and $2b$ in a circle of radius $R$ are distance $d$ apart" | Chords can be on the **same side** OR **opposite sides** of the center | Perpendiculars from center are $\sqrt{R^2-a^2}$ and $\sqrt{R^2-b^2}$; $d = |\sqrt{R^2-a^2} \mp \sqrt{R^2-b^2}|$ |

---

## 3. Canonical CAT Archetypes & Solved Exemplars

### Archetype 1: Mass Point Geometry on Intersecting Cevians
> **Problem**: In $\triangle ABC$, $D$ lies on $BC$ such that $BD : DC = 2 : 3$, and $E$ lies on $AC$ such that $AE : EC = 3 : 4$. $AD$ and $BE$ intersect at $P$, and $CP$ extended meets $AB$ at $F$. Find the ratios $AP : PD$ and $AF : FB$.

- **First-Principles Method / Mass Point Shortcut**:
  1. Assign point masses $(m_A, m_B, m_C)$ so $D$ is the center of mass of $B$ and $C$, and $E$ is the center of mass of $A$ and $C$.
  2. Since $BD : DC = 2 : 3$, we need $m_B : m_C = 3 : 2$.
  3. Since $AE : EC = 3 : 4$, we need $m_A : m_C = 4 : 3$.
  4. Choose $m_C = 6 \implies m_B = 9$ and $m_A = 8$.
  5. Then mass at $D$ is $m_D = m_B + m_C = 9 + 6 = 15$.
  6. Along segment $AD$, fulcrum $P$ balances $m_A = 8$ and $m_D = 15$:
     $$AP : PD = m_D : m_A = \mathbf{15 : 8}$$
  7. Along segment $AB$, fulcrum $F$ balances $m_A = 8$ and $m_B = 9$:
     $$AF : FB = m_B : m_A = \mathbf{9 : 8}$$

---

### Archetype 2: Trapezium Diagonal Triangle Areas
> **Problem**: In trapezium $ABCD$ with $AB \parallel CD$, diagonals $AC$ and $BD$ intersect at $O$. If $\text{Area}(\triangle AOB) = 25\text{ cm}^2$ and $\text{Area}(\triangle COD) = 16\text{ cm}^2$, find the total area of trapezium $ABCD$.

- **First-Principles Method**:
  1. Since $AB \parallel CD$, $\triangle AOB \sim \triangle COD$ with area ratio $\frac{25}{16} \implies$ linear ratio $\frac{AO}{OC} = \frac{BO}{OD} = \frac{5}{4}$.
  2. $\triangle AOD$ and $\triangle COD$ share the same vertex $D$, so $\frac{\text{Area}(\triangle AOD)}{\text{Area}(\triangle COD)} = \frac{AO}{OC} = \frac{5}{4} \implies \text{Area}(\triangle AOD) = 20\text{ cm}^2 = \text{Area}(\triangle BOC)$.
  3. Total Area $= 25 + 16 + 20 + 20 = \mathbf{81\text{ cm}^2}$.

- **30-Second Exam-Hall Speed Shortcut**:
  $$\text{Area} = \left(\sqrt{A_1} + \sqrt{A_2}\right)^2 = (\sqrt{25} + \sqrt{16})^2 = (5 + 4)^2 = \mathbf{81\text{ cm}^2}$$

---

### Archetype 3: Angle Bisector Length & Stewart's Formula
> **Problem**: In $\triangle ABC$, $AB = 10\text{ cm}$, $AC = 15\text{ cm}$, and $BC = 20\text{ cm}$. The internal angle bisector of $\angle A$ meets $BC$ at $D$. Find the length of $AD$.

- **First-Principles Method**:
  1. By Angle Bisector Theorem, $BD : DC = AB : AC = 10 : 15 = 2 : 3$.
  2. Since $BC = 20$, $BD = p = 8\text{ cm}$ and $DC = q = 12\text{ cm}$.
  3. Using the angle bisector length formula $AD^2 = AB \cdot AC - BD \cdot DC$:
     $$AD^2 = 10 \times 15 - 8 \times 12 = 150 - 96 = 54 \implies AD = \mathbf{3\sqrt{6}\text{ cm}}$$

- **30-Second Exam-Hall Speed Shortcut**:
  - Memorize $l_a^2 = bc - pq$ alongside $p = \frac{ac}{b+c}, q = \frac{ab}{b+c}$: takes 10 seconds flat!

---

## 4. Boundary Conditions, Domain Traps & TITA Pitfalls

1. **"Isosceles Triangle with Sides 4 and 9"**:
   - The third side MUST be $9$, NOT $4$, because $4 + 4 = 8 \ngtr 9$ violates the Triangle Inequality!
2. **Obtuse vs. Acute Configuration when Two Sides & One Non-Included Angle (SSA) or Altitude Are Given**:
   - If in $\triangle ABC$, $AB = 15, AC = 13$, and altitude $AD = 12$, then $BD = \sqrt{15^2 - 12^2} = 9$ and $DC = \sqrt{13^2 - 12^2} = 5$. Thus $BC$ can be **either** $9 + 5 = 14$ (acute) **or** $9 - 5 = 4$ (obtuse)!
3. **Regular Polygon Interior Angle Bounds**:
   - An interior angle $\theta$ of a regular $n$-gon must yield an integer $n = \frac{360^\circ}{180^\circ - \theta} \ge 3$.

---

## 5. Active-Recall Drill (10 Prompts)

<details><summary>Q1: How many non-congruent triangles with integer side lengths have perimeter 15?</summary>
A: For odd perimeter P = 15: round((15 + 3)^2 / 48) = round(324 / 48) = round(6.75) = 7 triangles.
</details>

<details><summary>Q2: In a right triangle with legs 6 cm and 8 cm, find the distance between its incenter I and circumcenter O.</summary>
A: Hypotenuse c = 10. Place right angle at origin (0,0): inradius r = (6 + 8 - 10)/2 = 2 -> I = (2, 2). Circumcenter O is midpoint of hypotenuse = (3, 4). Distance OI = sqrt((3-2)^2 + (4-2)^2) = sqrt(5) cm (also Euler's formula OI^2 = R^2 - 2Rr = 25 - 2(5)(2) = 5).
</details>

<details><summary>Q3: Two circles of radii 9 cm and 4 cm touch each other externally. Find the radius of the small circle that touches both circles and their direct common tangent.</summary>
A: Using 1/sqrt(r) = 1/sqrt(9) + 1/sqrt(4) = 1/3 + 1/2 = 5/6 -> sqrt(r) = 6/5 -> r = 36/25 = 1.44 cm.
</details>

<details><summary>Q4: In triangle ABC, medians AD = 9, BE = 12, and CF = 15 intersect at right angles or form a right-angled median triangle. Find the area of triangle ABC.</summary>
A: Area of triangle ABC = (4/3) * Area(triangle formed by medians). Since 9, 12, 15 is a right triangle of area (1/2)*9*12 = 54, Area(ABC) = (4/3) * 54 = 72.
</details>

<details><summary>Q5: A secant PAB from external point P intersects a circle at A and B such that PA = 4 and AB = 5. Find the length of the tangent PT from P to the circle.</summary>
A: Note that PB = PA + AB = 4 + 5 = 9 (NOT 5!). PT^2 = PA * PB = 4 * 9 = 36 -> PT = 6.
</details>

<details><summary>Q6: In a regular hexagon ABCDEF of side 6 cm, find the area of triangle ACE.</summary>
A: Triangle ACE is an equilateral triangle containing 3/6 = 1/2 of the hexagon's area. Total hexagon area = 6 * (sqrt(3)/4) * 36 = 54*sqrt(3). Thus Area(ACE) = 27*sqrt(3) cm^2.
</details>

<details><summary>Q7: Find the length of the segment parallel to the bases (lengths 6 and 12) of a trapezium that passes through the intersection of its diagonals.</summary>
A: Harmonic mean of the bases: 2 * 6 * 12 / (6 + 12) = 144 / 18 = 8.
</details>

<details><summary>Q8: In a circle of radius 13 cm, two parallel chords have lengths 10 cm and 24 cm. Find the distance between the chords if they lie on opposite sides of the center.</summary>
A: Half-chords are 5 and 12. Distances from center are sqrt(13^2 - 5^2) = 12 and sqrt(13^2 - 12^2) = 5. On opposite sides, total distance = 12 + 5 = 17 cm.
</details>

<details><summary>Q9: How many diagonals does a regular polygon have if each interior angle is 156 degrees?</summary>
A: Exterior angle = 180 - 156 = 24 degrees -> n = 360 / 24 = 15 sides. Number of diagonals = 15*(15 - 3)/2 = 90.
</details>

<details><summary>Q10: A triangle has sides 13, 14, and 15. Find its inradius r and circumradius R.</summary>
A: Semi-perimeter s = 21. Area = sqrt(21 * 8 * 7 * 6) = 84. Thus r = Area / s = 84 / 21 = 4, and R = abc / (4 * Area) = (13 * 14 * 15) / (4 * 84) = 65 / 8 = 8.125.
</details>

---

## CAT 2025 PYQ Edge Examples & Newly Surfaced Patterns

### Newly Surfaced Sub-Topic Variants & Pattern Triggers (CAT 2025)
- **Third-Tangent Center Angle Theorem (`CAT_2025_QA_Slot_2` / `CAT2025_S2_QA_Q02`)**: A tangent segment $AB$ intercepted between two tangents $PA, PB$ from external point $P$ to a circle with center $O$ subtends $\angle AOB = 90^\circ - \frac{1}{2}\angle APB$.
- **Tangential Right-Trapezium Pitot Identity (`CAT_2025_QA_Slot_3` / `CAT2025_S3_QA_Q02`)**: A trapezium with an inscribed circle satisfies $AB + CD = AD + BC$ and height $h = 2r$; if right-angled at $A$ and $D$, the inclined leg is $BC = a + b - 2r$.
- **Circumcircle Secant Similarity in Isosceles Triangles (`CAT_2025_QA_Slot_3` / `CAT2025_S3_QA_Q05`)**: Extending median/cevian $AD$ to meet the circumcircle at $E$ gives $\triangle ABD \sim \triangle AEB \implies AB^2 = AD \cdot AE$.

### Solved CAT 2025 PYQ Edge Exemplars

#### CAT2025_S1_QA_Q12 (`CAT_2025_QA_Slot_1` | MCQ | Medium | `Round_2_Doable`)
- **Sub-Topic**: Circles — *Parallel chords on opposite sides of a circle center and trapezium area*
- **Verified Answer**: `(A) 20(3 + sqrt(14))` (Radius R = 6*sqrt(2). In isosceles triangle PCQ with angle PQC = 45 deg, perp distance d1 = R*sin(45) = 6 cm and chord PQ = 12 cm. Since d1:d2 = 3:2, d2 = 4 cm. Half-chord of SR = sqrt(72 - 16) = 2*sqrt(14) => SR = 4*sqrt(14). Area of trapezium PQRS = (1/2)*(12 + 4*sqrt(14))*(6 + 4) = 20(3 + sqrt(14)).)
- **Mental Trigger (`See X -> Do Y`)**: Separated by a diameter means the two parallel chords lie on opposite sides of center C, so trapezium height h = d1 + d2 (not |d1 - d2|).
- **First-Principles Method**: In triangle CPQ, CP = CQ = 6*sqrt(2) and angle PQC = 45 deg, so angle PCQ = 90 deg, distance d1 = 6, and PQ = 12. From d1 : d2 = 3 : 2, d2 = 4. Then SR = 2*sqrt((6*sqrt(2))^2 - 4^2) = 4*sqrt(14). Since PQ and SR are separated by a diameter, height = d1 + d2 = 10, so Area = 0.5*(12 + 4*sqrt(14))*10 = 20(3 + sqrt(14)).
- **30-Second Exam-Hall Speed Shortcut**: Once d2 = 4 and R^2 = 72 give sqrt(72 - 16) = sqrt(56) = 2*sqrt(14), only Options (A) and (C) contain sqrt(14); since h = 6 + 4 = 10 (not 6 - 4 = 2), Option (A) with factor 20 wins.
- **Trap Alert & Boundary Condition**: Taking height as d1 - d2 = 2 instead of d1 + d2 = 10 gives the trap answer (C) 4(3 + sqrt(14)).

#### CAT2025_S1_QA_Q18 (`CAT_2025_QA_Slot_1` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Quadrilaterals & Polygons — *Rhombus diagonal-side identity d1^2 + d2^2 = 4a^2 and area (1/2)d1*d2*
- **Verified Answer**: `60` (In a rhombus, d1^2 + d2^2 = 4a^2 = 4*(36^2) = 5184 and d1*d2 = 2*Area = 792. Thus (d1 - d2)^2 = 5184 - 2(792) = 3600 => |d1 - d2| = 60.)
- **Mental Trigger (`See X -> Do Y`)**: Whenever rhombus side a and area A are given, use |d1 - d2| = sqrt(4a^2 - 4A) directly without solving for d1 and d2 separately.
- **First-Principles Method**: Since diagonals of a rhombus bisect each other at 90 deg, (d1/2)^2 + (d2/2)^2 = a^2 => d1^2 + d2^2 = 4a^2 = 5184. Also (1/2)d1*d2 = 396 => 2d1*d2 = 1584. Hence (d1 - d2)^2 = 5184 - 1584 = 3600 => |d1 - d2| = 60.
- **30-Second Exam-Hall Speed Shortcut**: |d1 - d2| = 2*sqrt(a^2 - A) = 2*sqrt(1296 - 396) = 2*sqrt(900) = 60.
- **Trap Alert & Boundary Condition**: Memorize |d1 - d2| = 2*sqrt(a^2 - Area) and d1 + d2 = 2*sqrt(a^2 + Area) for any rhombus.

#### CAT2025_S2_QA_Q02 (`CAT_2025_QA_Slot_2` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Circles — *Third-tangent theorem for angle subtended at the center of a circle*
- **Verified Answer**: `80` (Let AB touch the circle at M. Then OA bisects angle QOM and OB bisects angle ROM, so angle QOR = 2 * angle AOB = 100 deg. In quadrilateral PQOR, angle OQP = angle ORP = 90 deg, so angle APB = 180 - angle QOR = 80 deg.)
- **Mental Trigger (`See X -> Do Y`)**: When tangent segment AB intercepted between two tangents PQ and PR subtends angle AOB at center O, use angle AOB = 90 - (1/2) angle APB => angle APB = 180 - 2 * angle AOB.
- **First-Principles Method**: Let AB touch the circle at M. By tangent symmetry, triangle OQA is congruent to triangle OMA and triangle ORB is congruent to triangle OMB. Thus angle QOR = 2 * angle AOB = 100 deg. Since OQ perp PQ and OR perp PR, angle APB = 180 - 100 = 80 deg.
- **30-Second Exam-Hall Speed Shortcut**: Apply the standard identity angle APB = 180 - 2(50) = 80 in 5 seconds.
- **Trap Alert & Boundary Condition**: Do not confuse angle AOB (50 deg) with angle QOR (100 deg); taking 180 - 50 = 130 is the classic trap.

#### CAT2025_S2_QA_Q03 (`CAT_2025_QA_Slot_2` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Quadrilaterals & Polygons — *Regular hexagon decomposition into equilateral triangles and midline scaling*
- **Verified Answer**: `(B) 5 : 24` (Set regular hexagon side = 2. Area(ABCDEF) = 6 * sqrt(3). In trapezium PBCQ, BC = 2, PB = QC = 1, interior angles at B and C are 120 deg, so PQ = 2 + 2*(1*cos 60) = 3 and height h = 1*sin 60 = sqrt(3)/2. Area(PBCQ) = 0.5*(2 + 3)*(sqrt(3)/2) = (5/4)*sqrt(3). Ratio = (5/4) : 6 = 5 : 24.)
- **Mental Trigger (`See X -> Do Y`)**: In a regular hexagon of side 2a, the long diagonal CF has length 4a; since P and Q are midpoints of AB and CD, PQ is the mid-segment of trapezium ABCF, so PQ = (2a + 4a)/2 = 3a!
- **First-Principles Method**: Half the hexagon (trapezium ABCF) has parallel sides AB = 2a and CF = 4a, and area = 3 equilateral triangles = 12 sub-triangles. Since P and Q are midpoints of the slant sides AB and CD (symmetric to BC and AD), PQ has length (2a + 3a)... wait: BC = 2a, AD = 4a, and P, Q are midpoints of AB, CD, so PQ is the midline of trapezium ABCD! Thus PQ = (BC + AD)/2 = 3a, height is half the height of ABCD, and Area(PBCQ)/Area(ABCD) = ((2a + 3a)/2) / ((2a + 4a)/2) * (1/2) = 5/12 of half-hexagon = 5/24 of full hexagon!
- **30-Second Exam-Hall Speed Shortcut**: Trapezium ABCD is half the hexagon (12/24). Midline PQ divides trapezium ABCD (bases 2 and 4, midline 3) into two strips of area ratio (2+3) : (3+4) = 5 : 7. So PBCQ is (5/12) * (1/2) = 5/24 of the hexagon!
- **Trap Alert & Boundary Condition**: Remember trapezium ABCD is HALF the hexagon (not the whole hexagon), so multiply 5/12 by 1/2 to get 5/24.

#### CAT2025_S2_QA_Q19 (`CAT_2025_QA_Slot_2` | MCQ | Medium | `Round_2_Doable`)
- **Sub-Topic**: Lines, Angles & Triangles — *Mass Point Geometry / Menelaus theorem on intersecting cevians*
- **Verified Answer**: `(B) 11 : 4` (AT : TD = 3 : 1 and BT : TE = 4 : 1. By Mass Point Geometry on triangle ABC with cevians AD and BE intersecting at T: m_A : (m_B + m_C) = 1 : 3 and m_B : (m_A + m_C) = 1 : 4. Setting m_A = 4 gives m_B + m_C = 12 and 4m_B = 4 + m_C => m_B = 16/5, m_C = 44/5. Thus BD : CD = m_C : m_B = 44 : 16 = 11 : 4.)
- **Mental Trigger (`See X -> Do Y`)**: Intersecting cevians AD and BE with given internal ratios AT:TD and BT:TE -> apply Mass Point Geometry (note that point F with DF || BE is a red herring!).
- **First-Principles Method**: Since DF || BE, by Thales theorem in triangle BCE, EF : FC = BD : CD, and in triangle ADF, TE || DF gives AT : TD = AE : EF = 3 : 1. Alternatively by Mass Points: AT/TD = (m_B + m_C)/m_A = 3/1 and BT/TE = (m_A + m_C)/m_B = 4/1. Solving gives m_A : m_B : m_C = 20 : 16 : 44 = 5 : 4 : 11, so BD : CD = m_C : m_B = 11 : 4.
- **30-Second Exam-Hall Speed Shortcut**: Using DF || BE: let AT = 3, TD = 1 => AE = 3x, EF = x. Then in triangle BCE, DF / BE = 1/3? No, in triangle ADF, TE/DF = AT/AD = 3/4, and BT/TE = 4/1 => BT : TE : DF = 12 : 3 : 4 => BE : DF = 15 : 4 => BC : DC = 15 : 4 => BD : CD = (15 - 4) : 4 = 11 : 4!
- **Trap Alert & Boundary Condition**: BC : CD is 15 : 4 (distractor A), whereas the question asks for BD : CD = (15 - 4) : 4 = 11 : 4 (Option B)!

#### CAT2025_S3_QA_Q02 (`CAT_2025_QA_Slot_3` | MCQ | Medium | `Round_1_Sitter`)
- **Sub-Topic**: Quadrilaterals & Polygons — *Tangential right-trapezium properties (Pitot's theorem AB + CD = AD + BC)*
- **Verified Answer**: `(C) 48` (Height AD = 2r = 6 cm. Let DC = x, AB = 3x. By Pitot's theorem for tangential quadrilateral ABCD, BC + AD = AB + DC => BC = 4x - 6. By Pythagoras on right triangle with legs 6 and 2x: (4x - 6)^2 = 36 + 4x^2 => 12x^2 - 48x = 0 => x = 4. Area = 0.5*(4 + 12)*6 = 48.)
- **Mental Trigger (`See X -> Do Y`)**: In ANY right trapezium circumscribing a circle of radius r with parallel bases a and b, the perpendicular leg is h = 2r and harmonic mean of bases is 2ab/(a+b) = 2r? Even faster: Drop tangents from C and B to get r + x? Wait: at right angles A and D, tangent lengths from A and D along AB and DC are r = 3! So DC = 3 + t1 and AB = 3 + t2 with t1*t2 = r^2 = 9!
- **First-Principles Method**: Height AD = 2r = 6. Let DC = x and AB = 3x. Since a circle is inscribed in ABCD, opposite sides sum equally: AB + DC = AD + BC => 4x = 6 + BC => BC = 4x - 6. Dropping an altitude from C to AB gives (4x - 6)^2 = 6^2 + (2x)^2 => 12x^2 = 48x => x = 4. Area = 0.5*(16)*6 = 48.
- **30-Second Exam-Hall Speed Shortcut**: Since AD perp AB and DC, tangent segments at A and D have length r = 3. Let remaining tangent segments at C and B be t1, t2; then t1*t2 = r^2 = 9, DC = 3 + t1, AB = 3 + t2 = 3(3 + t1) => t1 = 1, t2 = 9 => DC = 4, AB = 12 => Area = 8 * 6 = 48!
- **Trap Alert & Boundary Condition**: Remember the identity t1 * t2 = r^2 for the two non-perpendicular corners of a right tangential trapezium.

#### CAT2025_S3_QA_Q05 (`CAT_2025_QA_Slot_3` | MCQ | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Lines, Angles & Triangles — *Circumcircle chord-secant similarity (AB^2 = AD * AE in isosceles triangle)*
- **Verified Answer**: `(A) 18` (Since AB = AC = 12, angle ABC = angle ACB = angle AEB. In triangles ABD and AEB, angle BAE is common and angle ABD = angle AEB. Thus triangle ABD ~ triangle AEB, giving AB/AE = AD/AB => AE = AB^2 / AD = 144 / 8 = 18.)
- **Mental Trigger (`See X -> Do Y`)**: In isosceles triangle ABC (AB = AC) with E on the circumcircle (angle ACB = angle AEB), ALWAYS use AB^2 = AD * AE!
- **First-Principles Method**: Since AB = AC, angle ABD = angle ACB. Given angle ACB = angle AEB, we have angle ABD = angle AEB. With common angle BAD = angle EAB, triangle ABD is similar to triangle AEB by AA similarity. Therefore AB/AE = AD/AB => AE = 12^2 / 8 = 18.
- **30-Second Exam-Hall Speed Shortcut**: Direct theorem: AB^2 = AD * AE => 144 = 8 * AE => AE = 18.
- **Trap Alert & Boundary Condition**: Do not confuse AE (18) with DE = AE - AD = 10.

#### CAT2025_S3_QA_Q18 (`CAT_2025_QA_Slot_3` | TITA | Easy | `Round_1_Sitter`)
- **Sub-Topic**: Lines, Angles & Triangles — *Altitudes of an isosceles triangle via area invariance (a*h_a = b*h_b = c*h_c = 2*Area)*
- **Verified Answer**: `126` (In isosceles triangle ABC (50, 50, 80), altitude to base 80 is sqrt(50^2 - 40^2) = 30 cm, and Area = 0.5 * 80 * 30 = 1200 sq cm. Altitudes to the two equal sides of 50 cm are each 2*1200 / 50 = 48 cm. Sum of altitudes = 30 + 48 + 48 = 126 cm.)
- **Mental Trigger (`See X -> Do Y`)**: Split the 50-50-80 triangle into two 30-40-50 right triangles; then h_b = h_c = (80 * 30)/50 = 48!
- **First-Principles Method**: Drop altitude h_a to BC = 80: by Pythagoras on half-base 40 and hypotenuse 50, h_a = 30 cm. By area invariance, 50 * h_b = 50 * h_c = 80 * 30 = 2400 => h_b = h_c = 48 cm. Sum = 30 + 48 + 48 = 126 cm.
- **30-Second Exam-Hall Speed Shortcut**: h_a = 30, h_b = h_c = 48 -> 30 + 96 = 126.
- **Trap Alert & Boundary Condition**: Remember there are THREE altitudes (count both equal altitudes of length 48).
