# QA 08 Concept & Formula Examples: 3D Mensuration, Inscribed Solids, Coordinate Geometry & Trigonometry

> **Companion Reference**: [`../topic_summaries/quant/08_geometry_mensuration_3d_coordinate_trig.md`](../topic_summaries/quant/08_geometry_mensuration_3d_coordinate_trig.md) | [`QA_Formula_and_Trigger_Book.md`](../high_recall/cheat_sheets/QA_Formula_and_Trigger_Book.md)

Every concept, formula, and pattern trigger from **QA 08** is explained below with plain-English intuition, clean single-concept numbers, a two-way walkthrough (direct formula vs. mental ratio intuition), and the #1 mistake to avoid.

---

## Concept 1: Cuboid & Cube Mensuration, Edge-Diagonal-TSA Identity & Shortest Ant Path

### 1. Concept & Formula in Plain English
For a cuboid of length $l$, breadth $b$, and height $h$:
- **Volume**: $V = lbh$; **Total Surface Area (TSA)**: $2(lb + bh + hl)$; **Body Diagonal**: $d = \sqrt{l^2 + b^2 + h^2}$.
- **Algebraic Bridge Identity**: Squaring the sum of the 3 dimensions automatically connects the sum of all 12 edges $E = 4(l+b+h)$, the body diagonal $d$, and the TSA:
  $$(l + b + h)^2 = (l^2 + b^2 + h^2) + 2(lb + bh + hl) = d^2 + \text{TSA}$$
- **Shortest Surface Path (Ant on a Cuboid with $l \ge b \ge h$)**: Unfold two faces flat and keep the **largest dimension $l$ separate** so the squared sum is minimized:
  $$D_{\min} = \sqrt{l^2 + (b + h)^2}$$

### 2. When to Use It (Question Cue)
- *"The sum of lengths of all 12 edges of a cuboid is $60\text{ cm}$ and its body diagonal is $9\text{ cm}$. Find its total surface area."*
- *"An ant crawls on the surface of a $6 \times 4 \times 2$ box from one corner to the opposite corner..."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) The sum of the lengths of all $12$ edges of a rectangular box is $60\text{ cm}$, and the length of its longest internal rod (body diagonal) is $9\text{ cm}$. Find the Total Surface Area (TSA) of the box.
> (b) If a box has dimensions $6\text{ cm} \times 4\text{ cm} \times 2\text{ cm}$, what is the shortest surface distance from one corner to the diametrically opposite corner?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: $4(l + b + h) = 60 \implies l + b + h = 15\text{ cm}$, and $d = 9\text{ cm}$.
     Plug into $(l + b + h)^2 = d^2 + \text{TSA}$:
     $$15^2 = 9^2 + \text{TSA} \implies 225 = 81 + \text{TSA} \implies \text{TSA} = \mathbf{144\text{ cm}^2}$$
  2. **Part (b)**: Since $6 \ge 4 \ge 2$, keep $l = 6$ separate:
     $$D_{\min} = \sqrt{6^2 + (4 + 2)^2} = \sqrt{36 + 36} = \mathbf{6\sqrt{2}\text{ cm}}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (b), compare the 3 possible unfoldings: $\sqrt{6^2 + (4+2)^2} = \sqrt{72}$ vs. $\sqrt{4^2 + (6+2)^2} = \sqrt{80}$ vs. $\sqrt{2^2 + (6+4)^2} = \sqrt{104}$. Clearly $\sqrt{72} = \mathbf{6\sqrt{2}}$ is smallest!

### 5. The 1 Common Mistake to Avoid
- **Trap**: Dividing the sum of all edges ($60$) by $3$ instead of **$4$** (a cuboid has $12$ edges: $4$ lengths, $4$ breadths, and $4$ heights!).

---

## Concept 2: Cylinder & Cone Mensuration, Unfolded Spiral Path & Sector-to-Cone Folding

### 1. Concept & Formula in Plain English
- **Cylinder ($r, h$)**: $V = \pi r^2 h$, $\text{CSA} = 2\pi r h$, $\text{TSA} = 2\pi r(r + h)$. Unfolding the curved wall gives a flat rectangle of width $2\pi r$ and height $h$, so a string/ant spiraling once from bottom to top has length $\sqrt{(2\pi r)^2 + h^2}$.
- **Cone ($r, h, l = \sqrt{r^2+h^2}$)**: $V = \frac{1}{3}\pi r^2 h$, $\text{CSA} = \pi r l$, $\text{TSA} = \pi r(r + l)$.
- **Folding a Sector into a Cone**: When a circular sector of radius $R_{\text{sector}}$ and central angle $\theta$ is rolled into a cone:
  - The sector's **radius** becomes the cone's **slant height**: $l = R_{\text{sector}}$.
  - The sector's **arc fraction** $\frac{\theta}{360^\circ}$ becomes the ratio $\frac{r}{l}$:
    $$r = R_{\text{sector}} \times \frac{\theta}{360^\circ}$$

### 2. When to Use It (Question Cue)
- *"A sector of a circle of radius $12\text{ cm}$ and central angle $120^\circ$ is folded into a cone. Find the base radius and height of the cone."*

### 3. General Example (Clean Numbers, Single Concept)
> A circular sector of radius $12\text{ cm}$ with a central angle of $120^\circ$ is rolled up so its straight edges join to form a right circular cone. Find the base radius $r$, slant height $l$, and vertical height $h$ of the cone.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Slant height $l = R_{\text{sector}} = \mathbf{12\text{ cm}}$.
  2. Base radius $r = 12 \times \frac{120^\circ}{360^\circ} = 12 \times \frac{1}{3} = \mathbf{4\text{ cm}}$.
  3. Vertical height $h = \sqrt{l^2 - r^2} = \sqrt{12^2 - 4^2} = \sqrt{128} = \mathbf{8\sqrt{2}\text{ cm}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Equate the circumference of the cone's base ($2\pi r$) to the arc length of the $120^\circ$ sector ($\frac{1}{3} \times 2\pi(12)$): $2\pi r = 8\pi \implies r = \mathbf{4\text{ cm}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Setting the sector radius $12\text{ cm}$ equal to the cone's **vertical height $h$** instead of its **slant height $l$**!

---

## Concept 3: Cone Sliced Parallel to Base ($1 : 7 : 19$ Ratio) & Frustum of a Cone

### 1. Concept & Formula in Plain English
When a cone is cut by planes parallel to its base at distances $h_1 : h_2 : h_3$ **measured from the top apex**, the top sub-cones are all 3D similar figures:
- **Linear dimensions** ($r, h, l$): ratio $h_1 : h_2 : h_3$
- **Curved Surface Areas from apex**: ratio $h_1^2 : h_2^2 : h_3^2$
- **Volumes from apex**: ratio $h_1^3 : h_2^3 : h_3^3$
  - For $3$ equal height slices ($1 : 2 : 3$ from apex), the individual slice volumes from top to bottom are $1^3 : (2^3 - 1^3) : (3^3 - 2^3) = \mathbf{1 : 7 : 19}$!
- **Frustum Volume Formula** (radii $R, r$, height $h$): $V = \frac{1}{3}\pi h(R^2 + r^2 + Rr)$.

### 2. When to Use It (Question Cue)
- *"A cone is cut into $3$ parts of equal height by planes parallel to the base. Find the ratio of the volumes of the $3$ parts."*

### 3. General Example (Clean Numbers, Single Concept)
> A right circular cone of volume $270\text{ cm}^3$ is cut into three pieces of equal height by two planes parallel to its base. Find the volume of the middle piece (frustum).

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Heights from the apex are in the ratio $1 : 2 : 3$, so volumes of the three cones from the apex are $1^3 : 2^3 : 3^3 = 1 : 8 : 27$.
  2. Individual piece volumes are $1 : (8 - 1) : (27 - 8) = 1 : 7 : 19$ (total $27$ parts).
  3. Since $27\text{ parts} = 270\text{ cm}^3$, the middle frustum ($7$ parts) has volume $\mathbf{70\text{ cm}^3}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Top 2/3 of the cone has volume $\left(\frac{2}{3}\right)^3 \times 270 = \frac{8}{27} \times 270 = 80\text{ cm}^3$.
  2. Top 1/3 of the cone has volume $\left(\frac{1}{3}\right)^3 \times 270 = \frac{1}{27} \times 270 = 10\text{ cm}^3$.
  3. Subtracting gives the middle slice: $80 - 10 = \mathbf{70\text{ cm}^3}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Measuring height ratios **from the bottom base** instead of **from the top apex** (similarity only holds for cones starting at the apex!).

---

## Concept 4: Sphere, Hemisphere, Solid Cutting Surface Gain & Regular Tetrahedron

### 1. Concept & Formula in Plain English
- **Sphere ($r$)**: $V = \frac{4}{3}\pi r^3$, $\text{TSA} = 4\pi r^2$.
- **Solid Hemisphere ($r$)**: $V = \frac{2}{3}\pi r^3$, $\text{CSA} = 2\pi r^2$, $\text{TSA} = 3\pi r^2$ (curved dome $2\pi r^2$ $+$ flat circular base $\pi r^2$).
- **Cutting a Sphere / Cube**: Every flat planar cut through the center of a sphere exposes **two new circular faces** of area $\pi r^2$ each ($+2\pi r^2$ per cut!).
- **Regular Tetrahedron (4 equilateral triangle faces of side $a$)**:
  $$\text{TSA} = \sqrt{3}a^2, \qquad \text{Height } h = \sqrt{\frac{2}{3}}a, \qquad \text{Volume } V = \frac{\sqrt{2}}{12}a^3$$

### 2. When to Use It (Question Cue)
- *"A solid sphere of radius $r$ is cut into $4$ identical quarter-spheres. Find the percentage increase in total surface area."*

### 3. General Example (Clean Numbers, Single Concept)
> A solid sphere of radius $7\text{ cm}$ is cut into $4$ identical pieces by two perpendicular planar cuts passing through its center. What is the ratio of the total surface area of all $4$ pieces combined to the surface area of the original sphere?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Original sphere TSA $= 4\pi r^2$.
  2. Each planar cut through the center adds $2\pi r^2$ of new flat area. Two perpendicular cuts add $2 \times 2\pi r^2 = 4\pi r^2$.
  3. New combined TSA $= 4\pi r^2 + 4\pi r^2 = 8\pi r^2$.
  4. Ratio $= 8\pi r^2 : 4\pi r^2 = \mathbf{2 : 1}$ (a $100\%$ increase!).
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Each quarter-sphere has $\frac{1}{4}$ of the curved outer skin ($\pi r^2$) plus two flat semicircles ($2 \times \frac{1}{2}\pi r^2 = \pi r^2$), totaling $2\pi r^2$ per piece ($4 \times 2\pi r^2 = 8\pi r^2$).

### 5. The 1 Common Mistake to Avoid
- **Trap**: Using $2\pi r^2$ instead of **$3\pi r^2$** for the Total Surface Area of a solid hemisphere!

---

## Concept 5: Inscribed 3D Solids (Sphere in Cone, Max Cylinder in Cone, Cube in Sphere)

### 1. Concept & Formula in Plain English
 slices through the center of 3D solids turn 3D problems into simple 2D geometry:
- **Sphere Inscribed in a Cone ($r, h, l$)**: The 2D vertical cross-section is an isosceles triangle of base $2r$, slant sides $l, l$, and height $h$. The sphere's radius is simply the 2D **inradius** $r_{\text{in}} = \frac{\Delta}{s}$:
  $$R_{\text{sphere}} = \frac{\frac{1}{2}(2r)h}{\frac{2r + l + l}{2}} = \mathbf{\frac{rh}{r + l}}$$
- **Maximum Volume Cylinder Inscribed in a Cone ($R, H$)**: Occurs when cylinder radius is $\frac{2}{3}R$ and cylinder height is $\frac{1}{3}H$, giving $V_{\text{cyl}} = \mathbf{\frac{4}{27}V_{\text{cone}}}$.
- **Largest Cube Inside a Sphere of Radius $R$**: The cube's 3D body diagonal equals the sphere's diameter: $a\sqrt{3} = 2R$.

### 2. When to Use It (Question Cue)
- *"Find the radius of the largest sphere that can be inscribed in a cone of base radius $3\text{ cm}$ and height $4\text{ cm}$."*

### 3. General Example (Clean Numbers, Single Concept)
> A right circular cone has base radius $r = 3\text{ cm}$ and vertical height $h = 4\text{ cm}$. Find:
> (a) the radius of the inscribed sphere, and
> (b) the maximum volume of a cylinder that can be inscribed inside this cone.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Slant height $l = \sqrt{3^2 + 4^2} = 5\text{ cm}$.
  2. **Part (a) Sphere Radius**: $R_{\text{sphere}} = \frac{rh}{r + l} = \frac{3 \times 4}{3 + 5} = \frac{12}{8} = \mathbf{1.5\text{ cm}}$.
  3. **Part (b) Max Cylinder Volume**: $V_{\text{cone}} = \frac{1}{3}\pi (3^2)(4) = 12\pi$, so $V_{\text{cyl, max}} = \frac{4}{27}(12\pi) = \mathbf{\frac{16}{9}\pi\text{ cm}^3}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Slice the cone down the middle: you see a triangle of base $6$, sides $5, 5$, and height $4$ (area $= 12$, semi-perimeter $s = \frac{6+5+5}{2} = 8$). Its inradius is $\frac{12}{8} = \mathbf{1.5\text{ cm}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: When inscribing a cube inside a sphere of diameter $2R$, setting the cube's face diagonal $a\sqrt{2} = 2R$ instead of its **3D body diagonal $a\sqrt{3} = 2R$**.

---

## Concept 6: Coordinate Distance, Section Formula, Parallelogram Vertex Rule & Segment Lattice Points

### 1. Concept & Formula in Plain English
- **Internal Section Formula ($m : n$)**: Divides segment from $(x_1, y_1)$ to $(x_2, y_2)$ at $\left(\frac{mx_2 + nx_1}{m+n}, \frac{my_2 + ny_1}{m+n}\right)$.
- **Parallelogram 4th Vertex Rule**: Because diagonals $PR$ and $QS$ of parallelogram $PQRS$ share the exact same midpoint, opposite vertices have the same coordinate sum:
  $$P + R = Q + S \implies \mathbf{S = P + R - Q}$$
- **Integer Lattice Points on a Segment**: The number of integer-coordinate points $(x, y)$ on the segment joining $(x_1, y_1)$ and $(x_2, y_2)$ (including both endpoints) is:
  $$\gcd(|x_2 - x_1|,\; |y_2 - y_1|) + 1$$

### 2. When to Use It (Question Cue)
- *"Three consecutive vertices of parallelogram $PQRS$ are $P(1, 2), Q(4, 6), R(7, 5)$. Find $S$."*
- *"How many points with integer coordinates lie on the segment joining $(1, 2)$ and $(9, 8)$?"*

### 3. General Example (Clean Numbers, Single Concept)
> (a) Find the fourth vertex $S$ of parallelogram $PQRS$ if $P(1, 2)$, $Q(4, 6)$, and $R(7, 5)$ are taken in order.
> (b) How many integer-coordinate points lie on the line segment joining $(1, 2)$ and $(9, 8)$ (including endpoints)?

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: $S = P + R - Q = (1 + 7 - 4,\; 2 + 5 - 6) = \mathbf{(4, 1)}$.
  2. **Part (b)**: $\text{Count} = \gcd(|9 - 1|,\; |8 - 2|) + 1 = \gcd(8, 6) + 1 = 2 + 1 = \mathbf{3\text{ points}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (a), moving from $Q(4,6)$ to $P(1,2)$ shifts by $(-3, -4)$; applying the same shift to $R(7,5)$ gives $(7-3, 5-4) = \mathbf{(4, 1)}$.
  2. In (b), the segment goes from $(1, 2)$ to $(9, 8)$ with midpoint $(5, 5)$—those $3$ points are the only integer points!

### 5. The 1 Common Mistake to Avoid
- **Trap**: If the question says **"strictly between"** the endpoints (excluding both endpoints), subtract $1$ instead of adding $1$: $\gcd(\Delta x, \Delta y) - 1$.

---

## Concept 7: Triangle Coordinate Centers ($G, I$) & Shift-to-Origin Shoelace Area

### 1. Concept & Formula in Plain English
For a triangle with vertices $A(x_1, y_1), B(x_2, y_2), C(x_3, y_3)$ and opposite side lengths $a, b, c$:
- **Centroid ($G$)**: Average of the 3 vertices: $\left(\frac{x_1+x_2+x_3}{3},\; \frac{y_1+y_2+y_3}{3}\right)$.
- **Incenter ($I$)**: Weighted average by opposite side lengths: $\left(\frac{ax_1+bx_2+cx_3}{a+b+c},\; \frac{ay_1+by_2+cy_3}{a+b+c}\right)$.
- **Shift-to-Origin Area Shortcut**: Subtract vertex $A(x_1, y_1)$ from $B$ and $C$ to get shifted vectors $(u_1, v_1)$ and $(u_2, v_2)$, then:
  $$\text{Area} = \frac{1}{2}|u_1 v_2 - u_2 v_1|$$

### 2. When to Use It (Question Cue)
- *"Find the area of the triangle with vertices $(2, 3), (5, 7),$ and $(8, 4)$."*

### 3. General Example (Clean Numbers, Single Concept)
> Find the centroid $G$ and the area of the triangle with vertices $A(2, 3)$, $B(5, 7)$, and $C(8, 5)$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Centroid**: $G = \left(\frac{2+5+8}{3},\; \frac{3+7+5}{3}\right) = \mathbf{(5, 5)}$.
  2. **Area (Shift $A(2,3) \to (0,0)$)**:
     - $B' = (5 - 2,\; 7 - 3) = (3, 4)$
     - $C' = (8 - 2,\; 5 - 3) = (6, 2)$
     - $\text{Area} = \frac{1}{2}|3(2) - 6(4)| = \frac{1}{2}|6 - 24| = \mathbf{9\text{ sq. units}}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Enclose $\triangle ABC$ in a $6 \times 4$ bounding box ($x \in [2, 8], y \in [3, 7]$, area $= 24$) and subtract the $3$ corner right triangles ($\frac{1}{2}(3)(4) + \frac{1}{2}(3)(2) + \frac{1}{2}(6)(2) = 6 + 3 + 6 = 15$): $24 - 15 = \mathbf{9}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Forgetting the $\frac{1}{2}$ in front of $|u_1 v_2 - u_2 v_1|$ (without $\frac{1}{2}$, you get the area of the parallelogram, $18$, instead of the triangle, $9$!).

---

## Concept 8: Point-to-Line Distance, Parallel Line Distance & Reflection Across a Line

### 1. Concept & Formula in Plain English
Given a point $P(x_0, y_0)$ and a line written in general form $ax + by + c = 0$:
1. **Perpendicular Distance from $P$ to Line**: $d = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}$.
2. **Distance Between Parallel Lines** $ax + by + c_1 = 0$ and $ax + by + c_2 = 0$: $d = \frac{|c_1 - c_2|}{\sqrt{a^2 + b^2}}$.
3. **Foot of Perpendicular $(x_f, y_f)$ & Reflection Image $(x_r, y_r)$**:
   $$\frac{x - x_0}{a} = \frac{y - y_0}{b} = k, \quad \text{where } k = \frac{-(ax_0 + by_0 + c)}{a^2 + b^2} \text{ (Foot) or } \frac{-2(ax_0 + by_0 + c)}{a^2 + b^2} \text{ (Reflection)}$$
   - **$45^\circ$ Line Shortcut ($x \pm y = k$)**: Just plug $y_0$ into the line to find $x_r$, and plug $x_0$ into the line to find $y_r$!

### 2. When to Use It (Question Cue)
- *"Find the reflection of $(1, 2)$ across the line $x + 2y - 10 = 0$."*

### 3. General Example (Clean Numbers, Single Concept)
> Find the perpendicular distance from $P(1, 2)$ to the line $x + 2y - 10 = 0$, the foot of the perpendicular, and the reflection of $P$ across the line.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Here $a = 1, b = 2, c = -10$, and $ax_0 + by_0 + c = 1(1) + 2(2) - 10 = -5$, with $a^2 + b^2 = 1^2 + 2^2 = 5$.
  2. **Perpendicular Distance**: $d = \frac{|-5|}{\sqrt{5}} = \mathbf{\sqrt{5}}$.
  3. **Foot of Perpendicular**: $k_f = \frac{-(-5)}{5} = +1 \implies (1 + 1(1),\; 2 + 2(1)) = \mathbf{(2, 4)}$.
  4. **Reflection Image**: $k_r = 2k_f = +2 \implies (1 + 1(2),\; 2 + 2(2)) = \mathbf{(3, 6)}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Notice $(2, 4)$ lies on the line $x + 2y = 10$ ($2 + 8 = 10$), and stepping from $P(1, 2)$ to $(2, 4)$ adds $(+1, +2)$; stepping once more by $(+1, +2)$ lands on the reflection $\mathbf{(3, 6)}$!

### 5. The 1 Common Mistake to Avoid
- **Trap**: When finding the distance between $3x + 4y = 10$ and $6x + 8y = 35$, subtracting $|10 - 35|$ before **making the $x, y$ coefficients identical** (divide the second line by $2$ first: $3x + 4y = 17.5$!).

---

## Concept 9: Circle Coordinate Equation & Tangent Condition

### 1. Concept & Formula in Plain English
A circle with center $(h, k)$ and radius $r$ has equation $(x - h)^2 + (y - k)^2 = r^2$.
When expanded as $x^2 + y^2 + 2gx + 2fy + c = 0$, the center is $(-g, -f)$ and the radius is $r = \sqrt{g^2 + f^2 - c}$.
**Golden Tangent Rule**: Never substitute $y = mx + c$ into the circle and expand a messy quadratic! A line is **tangent** to a circle if and only if the **perpendicular distance from the circle's center to the line equals the radius $r$**:
$$\frac{|ah + bk + c|}{\sqrt{a^2 + b^2}} = r$$

### 2. When to Use It (Question Cue)
- *"For what values of $c$ is the line $3x + 4y + c = 0$ tangent to the circle $x^2 + y^2 - 2x - 4y - 4 = 0$?"*

### 3. General Example (Clean Numbers, Single Concept)
> Find the values of $c$ for which the line $3x + 4y + c = 0$ is tangent to the circle $(x - 1)^2 + (y - 2)^2 = 9$.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. Circle center is $(h, k) = (1, 2)$ and radius is $r = \sqrt{9} = 3$.
  2. Set perpendicular distance from $(1, 2)$ to $3x + 4y + c = 0$ equal to $r = 3$:
     $$\frac{|3(1) + 4(2) + c|}{\sqrt{3^2 + 4^2}} = 3 \implies \frac{|11 + c|}{5} = 3 \implies |11 + c| = 15$$
  3. Solve $11 + c = \pm 15 \implies \mathbf{c = 4 \text{ or } c = -26}$.
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. Through center $(1, 2)$, $3x + 4y = 11$. Shifting a $3$-$4$-$5$ line by distance $3$ shifts its constant by $\pm 3 \times 5 = \pm 15$, giving $3x + 4y = 11 \pm 15 \in \{26, -4\}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Taking the radius of $(x - 1)^2 + (y - 2)^2 = 9$ as $9$ instead of $\sqrt{9} = 3$.

---

## Concept 10: Trigonometric Identities, Extrema of $a\sin\theta + b\cos\theta$, Sine/Cosine Rules & Two-Angle Elevation

### 1. Concept & Formula in Plain English
1. **Conjugate Reciprocal Pair**: Since $\sec^2\theta - \tan^2\theta = 1$, $(\sec\theta + \tan\theta)$ and $(\sec\theta - \tan\theta)$ are reciprocals: if $\sec\theta + \tan\theta = k$, then $\sec\theta - \tan\theta = \frac{1}{k}$.
2. **Wave Extrema**: For any real $\theta$, $a\sin\theta + b\cos\theta$ oscillates between **$-\sqrt{a^2 + b^2}$ and $+\sqrt{a^2 + b^2}$**.
3. **Cosine Rule**: $c^2 = a^2 + b^2 - 2ab\cos C$ (finds the 3rd side or angle in any non-right triangle).
4. **Two-Angle Tower Elevation**: Walking distance $d$ toward a tower of height $H$ changes the angle of elevation from $\alpha$ to $\beta$:
   $$d = H(\cot\alpha - \cot\beta)$$
   In particular, for **$30^\circ \to 60^\circ$**, the remaining distance from the $60^\circ$ point to the base of the tower is simply **half of $d$** ($\frac{d}{2}$), and $H = \frac{\sqrt{3}}{2}d$!

### 2. When to Use It (Question Cue)
- *"Find the maximum value of $3\sin\theta - 4\cos\theta + 10$."*
- *"Walking $40\text{ m}$ toward a tower changes the angle of elevation of its top from $30^\circ$ to $60^\circ$. Find the height of the tower."*

### 3. General Example (Clean Numbers, Single Concept)
> (a) Find the maximum and minimum values of $3\sin\theta - 4\cos\theta + 10$.
> (b) Walking $40\text{ m}$ straight toward a vertical tower changes the angle of elevation of its top from $30^\circ$ to $60^\circ$. Find the height $H$ of the tower.

### 4. Step-by-Step Walkthrough (Two Ways)
- **Way 1 — Direct Formula Plug-in**:
  1. **Part (a)**: Amplitude $= \sqrt{3^2 + (-4)^2} = 5$. Thus max $= 10 + 5 = \mathbf{15}$ and min $= 10 - 5 = \mathbf{5}$.
  2. **Part (b)**: Plug $d = 40, \alpha = 30^\circ, \beta = 60^\circ$ into $d = H(\cot 30^\circ - \cot 60^\circ)$:
     $$40 = H\left(\sqrt{3} - \frac{1}{\sqrt{3}}\right) = H\left(\frac{2}{\sqrt{3}}\right) \implies H = \mathbf{20\sqrt{3}\text{ m}}$$
- **Way 2 — Common-Sense / Ratio Intuition**:
  1. In (b), let the two points be $A$ ($30^\circ$) and $B$ ($60^\circ$) and the tower top be $T$. Exterior angle $\angle TBM = 60^\circ = \angle TAB (30^\circ) + \angle ATB \implies \angle ATB = 30^\circ$!
  2. So $\triangle ABT$ is isosceles with $BT = AB = 40\text{ m}$! In the $30^\circ$-$60^\circ$-$90^\circ$ triangle $BMT$ with hypotenuse $BT = 40\text{ m}$, height $H = 40\sin 60^\circ = \mathbf{20\sqrt{3}\text{ m}}$.

### 5. The 1 Common Mistake to Avoid
- **Trap**: Applying $-\sqrt{a^2+b^2}$ to $a\sin^2\theta + b\cos^2\theta$ (for **squared** $\sin^2\theta$ and $\cos^2\theta$, since $\sin^2\theta + \cos^2\theta = 1$, the expression simply ranges between $\min(a, b)$ and $\max(a, b)$!).
