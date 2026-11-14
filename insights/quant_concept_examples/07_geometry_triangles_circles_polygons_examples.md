# QA 07 Concept & Formula Examples: Lines, Angles, Triangles, Circles, Quadrilaterals & Polygons

> **Companion Reference**: [`../topic_summaries/quant/07_geometry_triangles_circles_polygons.md`](../topic_summaries/quant/07_geometry_triangles_circles_polygons.md) | [`QA_Formula_and_Trigger_Book.md`](../high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md)

Every concept, formula, and pattern trigger from **QA 07** is explained below with plain-English intuition, clean single-concept numbers, a two-way walkthrough (direct formula vs. mental ratio intuition), and the #1 mistake to avoid.

---

## Concept 1: Triangle Existence Inequality, Acute/Right/Obtuse Classification & Counting Integer Triangles

### 1. Concept & Formula in Plain English
For three side lengths $a \le b \le c$ (where $c$ is the longest side) to form a valid triangle:
1. **Triangle Inequality**: The two shorter sides together must beat the longest side: $a + b > c$ (equivalently, $|a - b| < c < a + b$).
2. **Angle Classification (compare $a^2 + b^2$ vs. $c^2$)**:
   - **Acute** (all angles $< 90^\circ$): $a^2 + b^2 > c^2$
   - **Right** (one angle $= 90^\circ$): $a^2 + b^2 = c^2$
   - **Obtuse** (one angle $> 90^\circ$): $a^2 + b^2 < c^2$
3. **Number of Integer-Sided Triangles with Perimeter $P$**:
   - Even $P$: $\text{round}\left(\frac{P^2}{48}\right)$
   - Odd $P$: $\text{round}\left(\frac{(P + 3)^2}{48}\right)$

### 2. When to Use It (Question Cue)
- *"Two sides of an obtuse triangle are $6$ and $8$. How many integer values can the third side $x$ take?"*
- *"How many triangles with integer sides have perimeter $12$?"*

### 3. General Example (Clean Numbers, Single Concept)
> (a) A triangle has two sides of lengths $6$ and $8$, and its third side $x$ is the longest side. If the triangle is **obtuse**, how many integer values can $x$ take?
> (b) How many non-congruent integer-sided triangles have a perimeter of $12$?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: For $x$ to be the longest side of a valid triangle, $8 \le x < 6 + 8 = 14$.
     For the triangle to be obtuse, $x^2 > 6^2 + 8^2 = 100 \implies x > 10$.
     Combining $10 < x < 14$ gives $x \in \{11, 12, 13\} \implies \mathbf{3\text{ integers}}$.
  2. **Part (b)**: For even perimeter $P = 12$: $\text{round}\left(\frac{12^2}{48}\right) = \text{round}(3) = \mathbf{3\text{ triangles}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), $(6, 8, 10)$ is a right triangle! Opening the $90^\circ$ angle wider makes it obtuse ($x > 10$) until the sides flatten into a straight line at $6 + 8 = 14$ ($x < 14$).
  2. In (b), list integer triples summing to $12$ with longest side $< 6$: $(4,4,4), (3,4,5), (2,5,5) \implies \mathbf{3\text{ triangles}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: If the question does **not** state that $x$ is the longest side, $8$ could also be the longest side ($x^2 + 6^2 < 8^2 \implies x^2 < 28$ with $x > 8 - 6 = 2 \implies x \in \{3, 4, 5\}$)—always check whether the unknown side or the given side $8$ is longest!

---

## Concept 2: The 5 Triangle Area Formulas, Inradius ($r$) & Circumradius ($R$)

### 1. Concept & Formula in Plain English
Depending on what information a problem gives you, pick the matching area formula (where $s = \frac{a+b+c}{2}$ is the semi-perimeter):
$$\Delta = \frac{1}{2}bh = \frac{1}{2}ab\sin C = \sqrt{s(s-a)(s-b)(s-c)} = r \cdot s = \frac{abc}{4R}$$
- **Right Triangle ($a^2 + b^2 = c^2$)**: $r = \frac{a + b - c}{2}$ and $R = \frac{c}{2}$ (midpoint of hypotenuse!).
- **Equilateral Triangle (side $a$)**: $\Delta = \frac{\sqrt{3}}{4}a^2$, $h = \frac{\sqrt{3}}{2}a$, $r = \frac{a}{2\sqrt{3}}$, $R = \frac{a}{\sqrt{3}}$ ($R = 2r$).

### 2. When to Use It (Question Cue)
- *"Find the inradius $r$ and circumradius $R$ of a triangle with sides $6, 8, 10$ (or $13, 14, 15$)."*

### 3. General Example (Clean Numbers, Single Concept)
> Find the area $\Delta$, inradius $r$, and circumradius $R$ of:
> (a) A right triangle with sides $6, 8, 10$.
> (b) A triangle with sides $13, 14, 15$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a) $(6, 8, 10)$**: $\Delta = \frac{1}{2}(6)(8) = \mathbf{24}$; $r = \frac{6 + 8 - 10}{2} = \mathbf{2}$; $R = \frac{10}{2} = \mathbf{5}$.
  2. **Part (b) $(13, 14, 15)$**: $s = \frac{13+14+15}{2} = 21$.
     - Heron's Area: $\Delta = \sqrt{21(21-13)(21-14)(21-15)} = \sqrt{21 \times 8 \times 7 \times 6} = \mathbf{84}$.
     - Inradius: $r = \frac{\Delta}{s} = \frac{84}{21} = \mathbf{4}$.
     - Circumradius: $R = \frac{abc}{4\Delta} = \frac{13 \times 14 \times 15}{4 \times 84} = \mathbf{\frac{65}{8} = 8.125}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Split the $(13, 14, 15)$ triangle by dropping an altitude of length $12$ to the base $14$: it splits neatly into a $(5, 12, 13)$ right triangle and a $(9, 12, 15)$ right triangle! Area $= \frac{1}{2}(14)(12) = \mathbf{84}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using $r = \frac{a+b-c}{2}$ on a **non-right** triangle! For non-right triangles, always use $r = \frac{\Delta}{s}$.

---

## Concept 3: Right-Triangle Altitude to Hypotenuse Similarity & Inscribed Square

### 1. Concept & Formula in Plain English
1. **Altitude to Hypotenuse ($BD \perp AC$ in right $\triangle ABC$, splitting hypotenuse $c$ into $p$ and $q$)**:
   - $h = BD = \frac{ab}{c}$ (from $\frac{1}{2}ab = \frac{1}{2}ch$)
   - $BD^2 = p \cdot q$, $AB^2 = p \cdot c$, $BC^2 = q \cdot c$.
2. **Square Inscribed in a Right Triangle**:
   - Resting on the two perpendicular legs $a, b$: side $x = \mathbf{\frac{ab}{a + b}}$.
   - Resting on the hypotenuse $c$ (with altitude $h$): side $y = \mathbf{\frac{ch}{c + h}}$.

### 2. When to Use It (Question Cue)
- *"In right $\triangle ABC$ with legs $6$ and $8$, find the length of the altitude to the hypotenuse and the side of the largest inscribed square."*

### 3. General Example (Clean Numbers, Single Concept)
> In a right-angled triangle with legs $a = 6\text{ cm}$ and $b = 8\text{ cm}$, find:
> (a) the altitude $h$ to the hypotenuse, and
> (b) the side length $x$ of the square inscribed with one corner at the right angle.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Hypotenuse $c = \sqrt{6^2 + 8^2} = 10\text{ cm}$.
  2. **Part (a) Altitude**: $h = \frac{ab}{c} = \frac{6 \times 8}{10} = \mathbf{4.8\text{ cm}}$.
  3. **Part (b) Inscribed Square**: $x = \frac{ab}{a + b} = \frac{6 \times 8}{6 + 8} = \frac{48}{14} = \mathbf{\frac{24}{7}\text{ cm}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. For the inscribed square of side $x$, the small top right triangle has height $(6 - x)$ and base $x$, which is similar to the big $(6, 8)$ triangle: $\frac{6 - x}{x} = \frac{6}{8} \implies 48 - 8x = 6x \implies x = \mathbf{\frac{24}{7}\text{ cm}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Confusing the inscribed square side $\frac{ab}{a+b}$ with the altitude $\frac{ab}{c}$ (denominator is $a + b$ for the square, and hypotenuse $c$ for the altitude!).

---

## Concept 4: The 4 Triangle Centers ($I, O, G, H$), Euler Line & Center Angle Formulas

### 1. Concept & Formula in Plain English
Every student should know what each center is and the angle it forms at the center opposite vertex $A$:
- **Incenter ($I$)**: Intersection of **angle bisectors** (equidistant from sides). Angle: $\mathbf{\angle BIC = 90^\circ + \frac{\angle A}{2}}$. Also $AI : ID = (b + c) : a$.
- **Circumcenter ($O$)**: Intersection of **perpendicular bisectors** (equidistant from vertices). Angle: $\mathbf{\angle BOC = 2\angle A}$.
- **Centroid ($G$)**: Intersection of **medians**. Divides each median in **$2 : 1$** ratio and divides the triangle into **$6$ equal-area triangles**.
- **Orthocenter ($H$)**: Intersection of **altitudes**. Angle: $\mathbf{\angle BHC = 180^\circ - \angle A}$.
- **Euler Line**: In any triangle, $O, G, H$ lie on a straight line with **$OG : GH = 1 : 2$**.

### 2. When to Use It (Question Cue)
- *"In $\triangle ABC$, $\angle A = 50^\circ$. Find the angles subtended by $BC$ at the incenter $I$, circumcenter $O$, and orthocenter $H$."*

### 3. General Example (Clean Numbers, Single Concept)
> In an acute triangle $ABC$ with $\angle A = 50^\circ$, find $\angle BIC$ (at the incenter), $\angle BOC$ (at the circumcenter), and $\angle BHC$ (at the orthocenter).

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Incenter**: $\angle BIC = 90^\circ + \frac{50^\circ}{2} = \mathbf{115^\circ}$.
  2. **Circumcenter**: $\angle BOC = 2 \times 50^\circ = \mathbf{100^\circ}$.
  3. **Orthocenter**: $\angle BHC = 180^\circ - 50^\circ = \mathbf{130^\circ}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. **Incenter**: Since $\angle B + \angle C = 180^\circ - 50^\circ = 130^\circ$, the half-angles $\frac{\angle B}{2} + \frac{\angle C}{2} = 65^\circ$, leaving $\angle BIC = 180^\circ - 65^\circ = \mathbf{115^\circ}$.
  2. **Orthocenter**: In the quadrilateral formed by $A$ and the two $90^\circ$ altitude feet on $AB$ and $AC$, the opposite angles sum to $180^\circ \implies 180^\circ - 50^\circ = \mathbf{130^\circ}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using $\angle BIC = 2\angle A$ for the Incenter (that is the Circumcenter $O$; the Incenter is always obtuse: $90^\circ + \frac{\angle A}{2}$!).

---

## Concept 5: Internal Angle Bisector Theorem & Length Formula ($AD^2 = bc - pq$)

### 1. Concept & Formula in Plain English
When the internal bisector of $\angle A$ meets opposite side $BC$ at $D$ (splitting $BC = a$ into $BD = p$ and $DC = q$):
1. **Side-Split Ratio**: The base segments $p$ and $q$ are in the exact same ratio as the adjacent sides $c = AB$ and $b = AC$:
   $$\frac{BD}{DC} = \frac{AB}{AC} \iff \frac{p}{q} = \frac{c}{b}$$
2. **Bisector Length**: The square of the bisector length $AD$ is the product of the two sides minus the product of the two base segments:
   $$AD^2 = b \cdot c - p \cdot q$$

### 2. When to Use It (Question Cue)
- *"In $\triangle ABC$, $AB = 6$, $AC = 8$, and $BC = 7$. The bisector of $\angle A$ meets $BC$ at $D$. Find $BD$ and $AD$."*

### 3. General Example (Clean Numbers, Single Concept)
> In $\triangle ABC$, $AB = 6\text{ cm}$, $AC = 8\text{ cm}$, and $BC = 7\text{ cm}$. If the internal angle bisector of $\angle A$ meets $BC$ at $D$, find the lengths of $BD$, $DC$, and $AD$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Ratio $BD : DC = AB : AC = 6 : 8 = 3 : 4$.
  2. Since $BC = 7\text{ cm} = 3 + 4$ parts, we get $p = BD = \mathbf{3\text{ cm}}$ and $q = DC = \mathbf{4\text{ cm}}$.
  3. Bisector length: $AD^2 = bc - pq = (8 \times 6) - (3 \times 4) = 48 - 12 = 36 \implies AD = \mathbf{6\text{ cm}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Notice $\frac{BD}{AB} = \frac{3}{6} = \frac{1}{2}$ and $\frac{DC}{AC} = \frac{4}{8} = \frac{1}{2}$, so each base segment is half its adjacent side, making $AD^2 = 48 - 12 = 36 \implies AD = \mathbf{6\text{ cm}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Equating $AD$ to the median formula instead of using $AD^2 = bc - pq$ (an angle bisector only equals the median when the triangle is isosceles, $b = c$!).

---

## Concept 6: Apollonius' Median Theorem & Stewart's Cevian Theorem

### 1. Concept & Formula in Plain English
- **Apollonius' Theorem (Median $m_a$ to side $a$)**: When $D$ is the **midpoint** of $BC$, the sum of squares of the two sides relates to the median $m_a$ and half-base $\frac{a}{2}$:
  $$b^2 + c^2 = 2\left(m_a^2 + \left(\frac{a}{2}\right)^2\right) \implies m_a = \frac{1}{2}\sqrt{2b^2 + 2c^2 - a^2}$$
- **Stewart's Theorem (Any Cevian $d$ splitting side $a$ into $m$ and $n$)**:
  $$b^2 m + c^2 n = a(d^2 + mn) \quad \text{(Mnemonic: "man + dad = bmb + cnc")}$$

### 2. When to Use It (Question Cue)
- *"In $\triangle ABC$, $AB = 7$, $AC = 9$, and $BC = 8$. Find the length of the median $AD$ to side $BC$."*

### 3. General Example (Clean Numbers, Single Concept)
> In $\triangle ABC$, $AB = 7\text{ cm}$, $AC = 9\text{ cm}$, and $BC = 8\text{ cm}$. Find the length of the median $AD$ drawn from $A$ to the midpoint $D$ of $BC$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $c = 7, b = 9$, and $a = 8$ (so half-base $\frac{a}{2} = 4$).
  2. Plug into $b^2 + c^2 = 2(m_a^2 + (a/2)^2)$:
     $$9^2 + 7^2 = 2(m_a^2 + 4^2) \implies 81 + 49 = 2(m_a^2 + 16) \implies 130 = 2(m_a^2 + 16)$$
  3. Divide by $2$: $65 = m_a^2 + 16 \implies m_a^2 = 49 \implies m_a = \mathbf{7\text{ cm}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Using $\frac{1}{2}\sqrt{2(81) + 2(49) - 64} = \frac{1}{2}\sqrt{162 + 98 - 64} = \frac{1}{2}\sqrt{196} = \frac{14}{2} = \mathbf{7\text{ cm}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting the factor of **$2$** in front of $m_a^2$ in $b^2 + c^2 = 2(m_a^2 + (a/2)^2)$.

---

## Concept 7: Mass Point Geometry (Replacing Ceva's & Menelaus' Theorems)

### 1. Concept & Formula in Plain English
Whenever cevians (lines from vertices to opposite sides) intersect at a point $P$ inside a triangle, imagine placing weights $m_A, m_B, m_C$ at vertices $A, B, C$ so that each side and cevian balances like a seesaw:
$$\text{Weight}_1 \times \text{Arm}_1 = \text{Weight}_2 \times \text{Arm}_2 \iff \frac{\text{Arm}_1}{\text{Arm}_2} = \frac{\text{Weight}_2}{\text{Weight}_1}$$
And the combined weight sitting at the fulcrum of two points is simply the **sum of their weights** ($m_D = m_B + m_C$)!

### 2. When to Use It (Question Cue)
- *"In $\triangle ABC$, $BD : DC = 1 : 2$ and $AE : EC = 1 : 3$. $AD$ and $BE$ intersect at $P$. Find $AP : PD$ and $BP : PE$."*

### 3. General Example (Clean Numbers, Single Concept)
> In $\triangle ABC$, point $D$ on $BC$ satisfies $BD : DC = 1 : 2$, and point $E$ on $AC$ satisfies $AE : EC = 1 : 3$. If $AD$ and $BE$ intersect at $P$, find the ratio $AP : PD$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in (Mass Points)**:
  1. Assign weight $m_C = 1$ at the shared corner $C$.
  2. To balance $BC$ at $D$ ($BD : DC = 1 : 2$), we need $m_B \times 1 = m_C \times 2 \implies m_B = 2$, and total fulcrum mass at $D$ is $m_D = m_B + m_C = 2 + 1 = 3$.
  3. To balance $AC$ at $E$ ($AE : EC = 1 : 3$), we need $m_A \times 1 = m_C \times 3 \implies m_A = 3$.
  4. Now look at segment $AD$: vertex $A$ has weight $m_A = 3$ and point $D$ has weight $m_D = 3$, so fulcrum $P$ balances them in ratio:
     $$AP : PD = m_D : m_A = 3 : 3 = \mathbf{1 : 1}$$
- **Way 2 — Common-Sense / Ratio Intuition (Parallel Line / Area Ratio)**:
  1. Draw a line from $D$ parallel to $BE$ meeting $AC$ at $M$. Since $BD : DC = 1 : 2$, $EM : MC = 1 : 2$, so $EC = 3$ parts ($EM = 1, MC = 2$).
  2. Since $AE : EC = 1 : 3$, $AE = 1$ part $= EM$!
  3. In $\triangle ADM$, $E$ is the midpoint of $AM$ and $EP \parallel DM \implies P$ is the midpoint of $AD$ ($AP : PD = \mathbf{1 : 1}$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Writing $AP : PD = m_A : m_D$ instead of flipping to the inverse lever ratio **$m_D : m_A$** (the heavier end is always *closer* to the fulcrum!).

---

## Concept 8: Circle Chords, Power of a Point ($PA \cdot PB = PT^2$) & Alternate Segment Theorem

### 1. Concept & Formula in Plain English
1. **Perpendicular from Center to Chord**: Bisects the chord! A chord of length $2a$ at distance $d$ from the center satisfies $d^2 + a^2 = R^2$.
2. **Power of a Point $P$**:
   - **Inside the circle** (two chords $AB$ and $CD$ crossing at $P$): $PA \cdot PB = PC \cdot PD$.
   - **Outside the circle** (tangent $PT$ and secant $PAB$): $PT^2 = PA \cdot PB$ (where $PB = PA + AB$ is the **full** distance from $P$ to the far intersection $B$!).
3. **Alternate Segment Theorem**: The angle between a tangent $PT$ and a chord $TA$ at the point of contact $T$ equals the angle subtended by $TA$ at any point on the opposite arc ($\angle PTA = \angle TBA$).

### 2. When to Use It (Question Cue)
- *"From an external point $P$, a tangent $PT$ and secant $PAB$ are drawn with $PA = 4$ and $AB = 12$. Find $PT$."*

### 3. General Example (Clean Numbers, Single Concept)
> From a point $P$ outside a circle, a secant line intersects the circle at $A$ and $B$ such that $PA = 4\text{ cm}$ and chord $AB = 12\text{ cm}$. Find the length of the tangent segment $PT$ from $P$ to the circle.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Find the full distance from $P$ to the far point $B$: $PB = PA + AB = 4 + 12 = 16\text{ cm}$.
  2. Apply Tangent-Secant Power of a Point:
     $$PT^2 = PA \times PB = 4 \times 16 = 64 \implies PT = \mathbf{8\text{ cm}}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. By the Alternate Segment Theorem, $\angle PTA = \angle PBT$, so $\triangle PTA \sim \triangle PBT$.
  2. Therefore $\frac{PT}{PB} = \frac{PA}{PT} \implies PT = \sqrt{4 \times 16} = \mathbf{8\text{ cm}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Multiplying $PA \times AB = 4 \times 12 = 48$ instead of $PA \times PB = 4 \times (4 + 12) = 64$ (both distances must be measured **from the external point $P$**!).

---

## Concept 9: Direct & Transverse Common Tangents, Ford Circle & Third-Tangent Center Angle

### 1. Concept & Formula in Plain English
For two circles of radii $r_1 \ge r_2$ whose centers are distance $d$ apart:
- **Direct Common Tangent (DCT)**: $L_{\text{DCT}} = \sqrt{d^2 - (r_1 - r_2)^2}$. (When the two circles touch externally, $d = r_1 + r_2 \implies L_{\text{DCT}} = \mathbf{2\sqrt{r_1 r_2}}$.)
- **Transverse Common Tangent (TCT)**: $L_{\text{TCT}} = \sqrt{d^2 - (r_1 + r_2)^2}$.
- **Ford Wedge Circle**: If two circles ($r_1, r_2$) touch externally and a small circle $r$ is wedged between them and their direct common tangent:
  $$\frac{1}{\sqrt{r}} = \frac{1}{\sqrt{r_1}} + \frac{1}{\sqrt{r_2}}$$
- **Third-Tangent Center Angle**: If a third tangent segment $AB$ cuts across two tangents $PQ, PR$ from external point $P$ to a circle with center $O$, then $\mathbf{\angle AOB = 90^\circ - \frac{1}{2}\angle P}$.

### 2. When to Use It (Question Cue)
- *"Two circles of radii $9\text{ cm}$ and $4\text{ cm}$ touch externally. Find the length of their direct common tangent and the radius of the small circle touching both and the tangent."*

### 3. General Example (Clean Numbers, Single Concept)
> Two circles of radii $r_1 = 9\text{ cm}$ and $r_2 = 4\text{ cm}$ touch each other externally. Find:
> (a) the length of their direct common tangent, and
> (b) the radius $r$ of the smaller circle that touches both circles and their common tangent.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: For externally touching circles, $L_{\text{DCT}} = 2\sqrt{r_1 r_2} = 2\sqrt{9 \times 4} = \mathbf{12\text{ cm}}$.
  2. **Part (b)**: Using $\frac{1}{\sqrt{r}} = \frac{1}{\sqrt{9}} + \frac{1}{\sqrt{4}} = \frac{1}{3} + \frac{1}{2} = \frac{5}{6} \implies \sqrt{r} = \frac{6}{5} \implies r = \mathbf{\frac{36}{25} = 1.44\text{ cm}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. For (a), draw a right triangle between the two centers: hypotenuse is $d = 9 + 4 = 13$, vertical leg is $r_1 - r_2 = 9 - 4 = 5$, so the horizontal tangent length is $\sqrt{13^2 - 5^2} = \mathbf{12\text{ cm}}$.
  2. For (b), the horizontal tangent segment $12\text{ cm}$ is the sum of two smaller tangent segments: $2\sqrt{9r} + 2\sqrt{4r} = 12 \implies 6\sqrt{r} + 4\sqrt{r} = 12 \implies 10\sqrt{r} = 12 \implies r = \mathbf{1.44\text{ cm}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using $(r_1 + r_2)^2$ instead of $(r_1 - r_2)^2$ for the **Direct** Common Tangent (remember: **D**irect uses **D**ifference $r_1 - r_2$; **T**ransverse uses **T**otal $r_1 + r_2$).

---

## Concept 10: Cyclic Quadrilaterals (Ptolemy & Brahmagupta) & Tangential Quadrilaterals (Pitot)

### 1. Concept & Formula in Plain English
1. **Cyclic Quadrilateral** (vertices lie **on** a circle; opposite angles sum to $180^\circ$):
   - **Ptolemy's Theorem**: $AC \cdot BD = AB \cdot CD + BC \cdot AD$.
   - **Brahmagupta's Area**: $\Delta = \sqrt{(s-a)(s-b)(s-c)(s-d)}$.
2. **Tangential Quadrilateral** (a circle is inscribed **inside** the quadrilateral, touching all 4 sides):
   - **Pitot's Theorem**: Sums of opposite sides are equal ($AB + CD = BC + AD$) because tangent segments from each corner are equal in pairs!

### 2. When to Use It (Question Cue)
- *"A circle is inscribed in quadrilateral $ABCD$ with $AB = 8$, $BC = 7$, $CD = 6$. Find $AD$."*
- *"Find the area of a cyclic quadrilateral with sides $2, 3, 4, 5$."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) A circle is inscribed inside quadrilateral $ABCD$. If $AB = 8\text{ cm}$, $BC = 7\text{ cm}$, and $CD = 6\text{ cm}$, find $AD$.
> (b) Find the area of a cyclic quadrilateral with side lengths $2, 3, 4, 5$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a) Pitot's Theorem**: $AB + CD = BC + AD \implies 8 + 6 = 7 + AD \implies AD = \mathbf{7\text{ cm}}$.
  2. **Part (b) Brahmagupta's Formula**: $s = \frac{2+3+4+5}{2} = 7$.
     $$\Delta = \sqrt{(7-2)(7-3)(7-4)(7-5)} = \sqrt{5 \times 4 \times 3 \times 2} = \sqrt{120} = \mathbf{2\sqrt{30}}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), label the 4 corner tangent lengths $w, x, y, z$: $(w+x) + (y+z) = (x+y) + (z+w)$, which is why opposite sides always have the exact same sum!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Adding adjacent sides ($AB + BC = CD + DA$) instead of **opposite sides** ($AB + CD = BC + DA$) in Pitot's theorem.

---

## Concept 11: Trapezium Diagonal Triangle Areas & Harmonic Mean Segment

### 1. Concept & Formula in Plain English
When the diagonals of a trapezium (parallel bases $a$ and $b$) cross at $O$, they cut the trapezium into $4$ triangles:
1. **Top & Bottom Triangles** ($A_{\text{top}}$ and $A_{\text{bottom}}$): Similar in ratio $a : b$, so area ratio is $a^2 : b^2$.
2. **Left & Right Wing Triangles**: Always have **equal area**, and each equals the geometric mean $\sqrt{A_{\text{top}} \cdot A_{\text{bottom}}}$!
   $$\text{Total Trapezium Area} = A_{\text{top}} + A_{\text{bottom}} + 2\sqrt{A_{\text{top}} A_{\text{bottom}}} = \left(\sqrt{A_{\text{top}}} + \sqrt{A_{\text{bottom}}}\right)^2$$
3. **Parallel Segment Through $O$**: The segment parallel to the bases passing through diagonal intersection $O$ has length equal to the **Harmonic Mean** $\frac{2ab}{a + b}$.

### 2. When to Use It (Question Cue)
- *"Diagonals of a trapezium divide it into 4 triangles. If the triangles on the parallel sides have areas $9$ and $16$, find the total area of the trapezium."*

### 3. General Example (Clean Numbers, Single Concept)
> In trapezium $ABCD$ ($AB \parallel CD$), the diagonals intersect at $O$. If $\text{Area}(\triangle AOB) = 9\text{ cm}^2$ and $\text{Area}(\triangle COD) = 16\text{ cm}^2$, find the area of each wing triangle and the total area of the trapezium.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Wing triangles: $A_{\text{left}} = A_{\text{right}} = \sqrt{9 \times 16} = \mathbf{12\text{ cm}^2}$.
  2. Total Area $= (\sqrt{9} + \sqrt{16})^2 = (3 + 4)^2 = \mathbf{49\text{ cm}^2}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Area ratio of $\triangle AOB$ to $\triangle COD$ is $9 : 16$, so segment ratio $AO : OC = 3 : 4$.
  2. Since $\triangle AOB$ ($9$) and $\triangle BOC$ share the same height from $B$ on line $AC$, their areas are in ratio $AO : OC = 3 : 4 \implies \text{Area}(\triangle BOC) = 12$. Total $= 9 + 16 + 12 + 12 = \mathbf{49\text{ cm}^2}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Adding only one wing triangle $\sqrt{A_1 A_2}$ instead of **both** wing triangles $2\sqrt{A_1 A_2}$!

---

## Concept 12: Rhombus Diagonal-Side Identity & Regular Polygon / Hexagon Properties

### 1. Concept & Formula in Plain English
1. **Rhombus (side $a$, diagonals $d_1, d_2$)**: Because the diagonals bisect each other at $90^\circ$, the half-diagonals form a right triangle of hypotenuse $a$:
   $$d_1^2 + d_2^2 = 4a^2, \qquad \text{Area} = \frac{1}{2} d_1 d_2, \qquad |d_1 - d_2| = 2\sqrt{a^2 - \text{Area}}$$
2. **Regular $n$-gon**:
   - Exterior angle $= \frac{360^\circ}{n}$, Interior angle $= 180^\circ - \frac{360^\circ}{n}$.
   - Number of diagonals $= \frac{n(n - 3)}{2}$.
3. **Regular Hexagon ($n = 6$, side $a$)**: Made of **$6$ equilateral triangles** of side $a$:
   - Area $= 6 \times \frac{\sqrt{3}}{4}a^2 = \frac{3\sqrt{3}}{2}a^2$, Short diagonal $= a\sqrt{3}$, Long diagonal $= 2a$.

### 2. When to Use It (Question Cue)
- *"A rhombus has side $5\text{ cm}$ and area $24\text{ cm}^2$. Find the sum and difference of its diagonals."*
- *"Find the number of diagonals and area of a regular hexagon of side $4\text{ cm}$."*

### 3. General Example (Clean Numbers, Single Concept)
> A rhombus has side length $a = 5\text{ cm}$ and area $A = 24\text{ cm}^2$. Find $d_1 + d_2$ and $|d_1 - d_2|$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. $d_1^2 + d_2^2 = 4a^2 = 4(25) = 100$, and $2d_1 d_2 = 4 \times \text{Area} = 96$.
  2. $(d_1 + d_2)^2 = 100 + 96 = 196 \implies d_1 + d_2 = \mathbf{14\text{ cm}}$.
  3. $(d_1 - d_2)^2 = 100 - 96 = 4 \implies |d_1 - d_2| = \mathbf{2\text{ cm}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Each quarter of the rhombus is a right triangle with hypotenuse $5$ and area $\frac{24}{4} = 6$, which is the classic $(3, 4, 5)$ right triangle!
  2. Half-diagonals are $3$ and $4$, so full diagonals are $6$ and $8$ (Sum $= \mathbf{14}$, Difference $= \mathbf{2}$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Writing $d_1^2 + d_2^2 = a^2$ (rectangle/square diagonal) instead of **$4a^2$** for a rhombus (since $\left(\frac{d_1}{2}\right)^2 + \left(\frac{d_2}{2}\right)^2 = a^2$).
