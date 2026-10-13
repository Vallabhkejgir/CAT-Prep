# QA 08: Geometry — 3D Mensuration, Inscribed Solids, Coordinate Geometry & Trigonometry

**Canonical Taxonomy Mapping**: `QA > Geometry & Mensuration > 3D Mensuration & Solids`, `Coordinate Geometry & Trigonometry`  
**Weightage**: ~6–10% of QA (1–2 questions per slot)  
**Priority Tier**: Tier 2 (High-Accuracy Scorer)

---

## 1. 30-Second Concept & Formula Blueprint

### 1.1 3D Mensuration & Solids Master Table
| Solid | Volume ($V$) | Lateral / Curved Surface Area | Total Surface Area (TSA) | Key Diagonal / Slant Relation |
| :--- | :--- | :--- | :--- | :--- |
| **Cuboid** ($l, b, h$) | $lbh$ | $2h(l + b)$ | $2(lb + bh + hl)$ | $d = \sqrt{l^2 + b^2 + h^2}$; $(l+b+h)^2 = d^2 + \text{TSA}$ |
| **Cube** ($a$) | $a^3$ | $4a^2$ | $6a^2$ | Body diag $= a\sqrt{3}$; Face diag $= a\sqrt{2}$ |
| **Right Cylinder** ($r, h$) | $\pi r^2 h$ | $2\pi r h$ | $2\pi r(r + h)$ | Max rod $= \sqrt{4r^2 + h^2}$ |
| **Right Cone** ($r, h, l$) | $\frac{1}{3}\pi r^2 h$ | $\pi r l$ | $\pi r(r + l)$ | $l = \sqrt{r^2 + h^2}$ |
| **Frustum of Cone** ($R, r, h$) | $\frac{1}{3}\pi h(R^2 + r^2 + Rr)$ | $\pi(R + r)l$ | $\pi(R+r)l + \pi(R^2 + r^2)$ | $l = \sqrt{h^2 + (R - r)^2}$ |
| **Sphere** ($r$) | $\frac{4}{3}\pi r^3$ | $4\pi r^2$ | $4\pi r^2$ | — |
| **Hemisphere** ($r$) | $\frac{2}{3}\pi r^3$ | $2\pi r^2$ | $3\pi r^2$ (solid) | — |
| **Regular Tetrahedron** ($a$) | $\frac{\sqrt{2}}{12}a^3$ | $\frac{3\sqrt{3}}{4}a^2$ | $\sqrt{3}a^2$ | Height $h = \sqrt{\frac{2}{3}}a$; $R = \frac{\sqrt{6}}{4}a$, $r = \frac{\sqrt{6}}{12}a$ |
| **Right Prism / Pyramid** | $A_{\text{base}} \cdot h$ / $\frac{1}{3}A_{\text{base}} \cdot h$ | $P_{\text{base}} \cdot h$ / $\frac{1}{2}P_{\text{base}} \cdot l$ | $\text{LSA} + 2A_{\text{base}}$ / $\text{LSA} + A_{\text{base}}$ | — |

- **Cone Cut by Planes Parallel to Base**:
  - If heights from apex are in ratio $h_1 : h_2 : h_3$, then radii are in ratio $h_1 : h_2 : h_3$, curved surface areas from apex are in ratio $h_1^2 : h_2^2 : h_3^2$, and volumes from apex are in ratio $h_1^3 : h_2^3 : h_3^3$.
  - For 3 equal-height slices ($1 : 2 : 3$), slice volumes are in ratio $1^3 : (2^3 - 1^3) : (3^3 - 2^3) = \mathbf{1 : 7 : 19}$.
- **Sector-to-Cone Folding**:
  - A circular sector of radius $R_{\text{sector}}$ and central angle $\theta$ (in degrees) folded into a cone has:
    $$\text{Slant height } l = R_{\text{sector}}, \quad \text{Base radius } r = R_{\text{sector}} \times \frac{\theta}{360^\circ}, \quad h = \sqrt{l^2 - r^2}$$
- **Inscribed & Circumscribed 3D Solids**:
  - **Sphere in Cube of side $a$**: $2r = a \implies r = \frac{a}{2}$.
  - **Cube in Sphere of radius $R$**: Body diagonal $a\sqrt{3} = 2R \implies a = \frac{2R}{\sqrt{3}}$.
  - **Sphere in Right Cone ($r, h, l$)**: Cross-section is an isosceles triangle of base $2r$, equal sides $l$, and height $h$:
    $$R_{\text{sphere}} = \frac{\Delta}{s} = \frac{rh}{r + l}$$
  - **Maximum Volume Cylinder inside Cone ($R, H$)**: $r_{\text{cyl}} = \frac{2}{3}R$, $h_{\text{cyl}} = \frac{1}{3}H$, $V_{\text{cyl}} = \frac{4}{27}V_{\text{cone}}$.
  - **Maximum Volume Cone/Cylinder inside Sphere of radius $R$**:
    - Cylinder: $h = \frac{2R}{\sqrt{3}}$, $r = R\sqrt{\frac{2}{3}}$, $V_{\text{cyl}} = \frac{4\pi R^3}{3\sqrt{3}} = \frac{1}{\sqrt{3}}V_{\text{sphere}}$.
    - Cone: $h = \frac{4}{3}R$, $r = \frac{2\sqrt{2}}{3}R$, $V_{\text{cone}} = \frac{8}{27}V_{\text{sphere}}$.

---

### 1.2 Coordinate Geometry
- **Distance & Section Formulas**:
  - Distance $= \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$.
  - Internal division $m:n$: $\left(\frac{mx_2 + nx_1}{m+n}, \frac{my_2 + ny_1}{m+n}\right)$.
- **Triangle Centers in Coordinates** ($A(x_1,y_1), B(x_2,y_2), C(x_3,y_3)$ with sides $a, b, c$):
  - **Centroid**: $G = \left(\frac{x_1+x_2+x_3}{3}, \frac{y_1+y_2+y_3}{3}\right)$
  - **Incenter**: $I = \left(\frac{ax_1+bx_2+cx_3}{a+b+c}, \frac{ay_1+by_2+cy_3}{a+b+c}\right)$
- **Shoelace Formula for Polygon Area** (vertices $(x_1, y_1), \dots, (x_n, y_n)$ in order):
  $$\text{Area} = \frac{1}{2}\Big|\sum_{i=1}^{n} (x_i y_{i+1} - x_{i+1} y_i)\Big| \quad (\text{where }(x_{n+1}, y_{n+1}) = (x_1, y_1))$$
  - For a triangle with one vertex shifted to $(0, 0)$ and others at $(u_1, v_1), (u_2, v_2)$:
    $$\text{Area} = \frac{1}{2}|u_1 v_2 - u_2 v_1|$$
- **Point-to-Line & Reflection Formulas** (Point $P(x_0, y_0)$ and Line $ax + by + c = 0$):
  - **Perpendicular Distance**: $d = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}$
  - **Distance Between Parallel Lines** $ax + by + c_1 = 0$ and $ax + by + c_2 = 0$: $d = \frac{|c_1 - c_2|}{\sqrt{a^2 + b^2}}$
  - **Foot of Perpendicular $(x_f, y_f)$ & Image/Reflection $(x_r, y_r)$**:
    $$\frac{x_f - x_0}{a} = \frac{y_f - y_0}{b} = \frac{-(ax_0 + by_0 + c)}{a^2 + b^2}, \qquad \frac{x_r - x_0}{a} = \frac{y_r - y_0}{b} = \frac{-2(ax_0 + by_0 + c)}{a^2 + b^2}$$
- **Circle Equations**:
  - $(x - h)^2 + (y - k)^2 = r^2$, or $x^2 + y^2 + 2gx + 2fy + c = 0$ with center $(-g, -f)$ and $r = \sqrt{g^2 + f^2 - c}$.
  - Line $ax + by + c = 0$ is **tangent** to circle iff distance from center to line equals radius $r$.

---

### 1.3 Trigonometry, Heights & Distances
- **Pythagorean & Reciprocal Identities**:
  - $\sin^2\theta + \cos^2\theta = 1$; $\sec^2\theta - \tan^2\theta = 1 \iff (\sec\theta - \tan\theta)(\sec\theta + \tan\theta) = 1$; $\csc^2\theta - \cot^2\theta = 1$.
- **Extrema of $a\sin\theta + b\cos\theta$**:
  $$-\sqrt{a^2 + b^2} \le a\sin\theta + b\cos\theta \le +\sqrt{a^2 + b^2}$$
- **Sine & Cosine Rules in $\triangle ABC$**:
  $$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R, \qquad \cos C = \frac{a^2 + b^2 - c^2}{2ab}$$
- **Two-Angle Elevation Shortcut** (Walking distance $d$ toward a tower of height $H$ changes angle of elevation from $\alpha$ to $\beta$):
  $$d = H(\cot\alpha - \cot\beta) \implies H = \frac{d}{\cot\alpha - \cot\beta}$$
  - Special memorized ratios:
    - $30^\circ \to 60^\circ$: $d = H\left(\sqrt{3} - \frac{1}{\sqrt{3}}\right) = \frac{2}{\sqrt{3}}H$, and distance from $60^\circ$ point to base is $\frac{d}{2}$.
    - $30^\circ \to 45^\circ$: $H = \frac{d}{\sqrt{3} - 1} = \frac{d(\sqrt{3}+1)}{2}$.
    - $45^\circ \to 60^\circ$: $H = \frac{d}{1 - 1/\sqrt{3}} = \frac{d\sqrt{3}}{\sqrt{3}-1} = \frac{d(3+\sqrt{3})}{2}$.

---

## 2. Pattern-Recognition Trigger Table

| Question Cue / Wording | Hidden Constraint | Fastest Attack Strategy |
| :--- | :--- | :--- |
| "Sum of lengths of all 12 edges of a cuboid is $E$ and body diagonal is $d$; find TSA" | $E = 4(l+b+h)$ and $(l+b+h)^2 = d^2 + \text{TSA}$ | $\text{TSA} = (E/4)^2 - d^2$ directly without finding $l, b, h$ |
| "Ant crawls on the surface of a cuboid ($l \ge b \ge h$) from one corner to the opposite corner" | Unfold 2 adjacent faces into a flat rectangle to minimize $(x + y)^2 + z^2$ | Keep the **largest dimension** $l$ separate and pair the two smaller ones: $D_{\min} = \sqrt{l^2 + (b + h)^2}$ |
| "Ant crawls once around the curved surface of a cylinder ($r, h$) from bottom to top" | Unfolded cylinder CSA is a rectangle of width $2\pi r$ and height $h$ | $D_{\min} = \sqrt{(2\pi r)^2 + h^2}$ (for $k$ spirals: $\sqrt{(2\pi k r)^2 + h^2}$) |
| "Find the reflection of $(x_0, y_0)$ across the line $x \pm y = k$" | Slope is $\pm 1$ ($45^\circ$ line) $\implies$ swap $x$ and $y$ directly! | Solve for $x_{\text{new}}$ from the line using $y_0$, and $y_{\text{new}}$ from the line using $x_0$: for $x + y = k$, image is $(k - y_0,\; k - x_0)$ |
| "Number of lattice points (integer coordinates) strictly on segment joining $(x_1, y_1)$ and $(x_2, y_2)$" | Depends on $\gcd$ of coordinate differences | $\gcd(|x_2 - x_1|,\; |y_2 - y_1|) + 1$ (including both endpoints) |

---

## 3. Canonical CAT Archetypes & Solved Exemplars

### Archetype 1: Sphere Inscribed in a Right Circular Cone
> **Problem**: A sphere is inscribed inside a right circular cone of base radius $6\text{ cm}$ and height $8\text{ cm}$ such that it touches the base and the curved surface. Find the ratio of the volume of the sphere to the volume of the cone.

- **First-Principles Method**:
  1. Slant height of cone $l = \sqrt{6^2 + 8^2} = 10\text{ cm}$.
  2. Vertical cross-section is an isosceles triangle of base $2r = 12$, sides $10, 10$, and height $8$.
  3. The inscribed sphere's cross-section is the incircle of this triangle:
     $$R_{\text{sphere}} = \frac{r \cdot h}{r + l} = \frac{6 \times 8}{6 + 10} = \frac{48}{16} = 3\text{ cm}$$
  4. Volume Ratio:
     $$\frac{V_{\text{sphere}}}{V_{\text{cone}}} = \frac{\frac{4}{3}\pi (3)^3}{\frac{1}{3}\pi (6)^2 (8)} = \frac{4 \times 27}{36 \times 8} = \frac{108}{288} = \mathbf{\frac{3}{8}}$$

- **30-Second Exam-Hall Speed Shortcut**:
  - Memorize $R_{\text{sphere}} = \frac{rh}{r+l}$ and $\frac{V_{\text{sphere}}}{V_{\text{cone}}} = \frac{4 R_{\text{sphere}}^3}{r^2 h}$!

---

### Archetype 2: Reflection of a Point Across a General Line
> **Problem**: Find the coordinates of the reflection of point $P(4, -13)$ across the line $5x + y + 6 = 0$.

- **First-Principles Method**:
  1. Using the reflection formula $\frac{x_r - x_0}{a} = \frac{y_r - y_0}{b} = \frac{-2(ax_0 + by_0 + c)}{a^2 + b^2}$:
     $$\frac{x_r - 4}{5} = \frac{y_r + 13}{1} = \frac{-2(5(4) + 1(-13) + 6)}{5^2 + 1^2} = \frac{-2(13)}{26} = -1$$
  2. Therefore:
     $$x_r = 4 + 5(-1) = -1, \quad y_r = -13 + 1(-1) = -14 \implies \mathbf{(-1, -14)}$$

- **30-Second Exam-Hall Speed Shortcut (Midpoint + Slope Check on Options)**:
  - Midpoint of $(4, -13)$ and $(-1, -14)$ is $(1.5, -13.5)$; plug into $5(1.5) - 13.5 + 6 = 0$ (True!).

---

### Archetype 3: Triangle Area via Shift-to-Origin Shoelace
> **Problem**: Find the area of the triangle formed by the vertices $A(3, 5)$, $B(7, 11)$, and $C(9, 2)$.

- **First-Principles Method / Speed Shortcut**:
  1. Subtract $A(3, 5)$ from all vertices to shift $A$ to $(0, 0)$:
     $$B' = (7 - 3, 11 - 5) = (4, 6), \quad C' = (9 - 3, 2 - 5) = (6, -3)$$
  2. Apply 2D cross-product formula $\frac{1}{2}|u_1 v_2 - u_2 v_1|$:
     $$\text{Area} = \frac{1}{2}|4(-3) - 6(6)| = \frac{1}{2}|-12 - 36| = \mathbf{24\text{ sq. units}}$$

---

## 4. Boundary Conditions, Domain Traps & TITA Pitfalls

1. **Cutting a Solid into $k$ Pieces Increases TSA by $2(k-1)$ Cross-Sectional Areas**:
   - Cutting a sphere into 4 equal hemispheres/quarters along two perpendicular planes adds $4 \times \pi r^2$ to the original $4\pi r^2$, making the total surface area of all 4 pieces $8\pi r^2$ ($2\pi r^2$ per quarter-sphere)!
2. **Hollow Pipe vs. Solid Cylinder**:
   - TSA of a hollow cylindrical pipe (radii $R > r$, height $h$) includes outer CSA ($2\pi Rh$), inner CSA ($2\pi rh$), AND two annular rings $2\pi(R^2 - r^2) = 2\pi(R+r)(R + h - r)$.
3. **Rolling a $a \times b$ Rectangle vs. Folding into a Cylinder**:
   - Without overlap, if side $a$ becomes the circumference ($2\pi r = a \implies r = \frac{a}{2\pi}$) and $b$ becomes the height, $V = \frac{a^2 b}{4\pi}$. Rolling along the **longer side** gives a **larger** volume by the factor $\frac{a}{b}$.

---

## 5. Active-Recall Drill (10 Prompts)

<details><summary>Q1: A cone of height 24 cm is cut into 3 parts by two planes parallel to its base at heights 8 cm and 16 cm from the base. Find the ratio of the volume of the middle frustum to the original cone.</summary>
A: Heights from apex are 8, 16, 24 (ratio 1:2:3). Volumes from apex are 1^3 : 2^3 : 3^3 = 1 : 8 : 27. Middle frustum volume = 8 - 1 = 7 parts out of 27. Ratio = 7 : 27.
</details>

<details><summary>Q2: Find the shortest surface path for an ant on a 3m x 4m x 5m cuboid to travel between two opposite corners.</summary>
A: Keep largest dimension 5 separate: sqrt(5^2 + (3 + 4)^2) = sqrt(25 + 49) = sqrt(74) m.
</details>

<details><summary>Q3: Find the reflection of the point (3, 8) across the line x + y = 5.</summary>
A: Using the +/-1 slope shortcut for x + y = k: image is (k - y_0, k - x_0) = (5 - 8, 5 - 3) = (-3, 2).
</details>

<details><summary>Q4: Find the distance between the parallel lines 3x - 4y + 7 = 0 and 6x - 8y - 16 = 0.</summary>
A: First make coefficients of x and y identical: divide second line by 2 -> 3x - 4y - 8 = 0. Distance = |7 - (-8)| / sqrt(3^2 + (-4)^2) = 15 / 5 = 3 units.
</details>

<details><summary>Q5: A semicircular sheet of metal of diameter 28 cm is bent into an open conical cup. Find the depth (height) of the cup.</summary>
A: Sector radius l = 14 cm, angle = 180 deg -> cone base radius r = 14 * (180/360) = 7 cm. Height h = sqrt(14^2 - 7^2) = 7*sqrt(3) cm.
</details>

<details><summary>Q6: If sec(theta) + tan(theta) = 3, find the value of sin(theta).</summary>
A: Since sec(theta) - tan(theta) = 1/3, adding gives 2*sec(theta) = 10/3 -> sec(theta) = 5/3 -> cos(theta) = 3/5 and sin(theta) = 4/5.
</details>

<details><summary>Q7: Find the maximum and minimum values of 5*sin(x) - 12*cos(x) + 7.</summary>
A: Since 5*sin(x) - 12*cos(x) ranges from -13 to +13, adding 7 gives Maximum = 20 and Minimum = -6.
</details>

<details><summary>Q8: How many points with integer coordinates lie on the line segment joining (2, -3) and (14, 15), including both endpoints?</summary>
A: gcd(|14 - 2|, |15 - (-3)|) + 1 = gcd(12, 18) + 1 = 6 + 1 = 7 points.
</details>

<details><summary>Q9: Find the incenter of the triangle with vertices A(0, 0), B(6, 0), and C(0, 8).</summary>
A: Right triangle with legs 6, 8 and hypotenuse 10; inradius r = (6 + 8 - 10)/2 = 2. Since legs lie on positive x and y axes, incenter is (r, r) = (2, 2).
</details>

<details><summary>Q10: A regular tetrahedron has edge length 6 cm. Find its volume.</summary>
A: V = (sqrt(2)/12) * a^3 = (sqrt(2)/12) * 216 = 18*sqrt(2) cm^3.
</details>
