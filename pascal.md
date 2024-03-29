<img src="diagrams/pascal.png">

**Pascal's theorem** states that if six arbitrary points are chosen on a conic and joined by line segments in any order (here we choose *A→B→C→D→E→F*) to form a hexagon, then the three pairs of opposite sides (*AB DE*, *BC EF* and *CD AF*) of the hexagon meet at three points (*G*, *H* and *I*) which lie on a straight line.

### Proof by Cartesian coordinates

#### About SymPy

Unlike the analytic geometry proof of [butterfly theorem](butterfly.md) where equations can be simplified by [Vieta's formulas](https://en.wikipedia.org/wiki/Vieta%27s_formulas), most theorems in projective geometry are too complicated to prove by analytic geometry by hand. Instead, we use [SymPy](https://en.wikipedia.org/wiki/SymPy) to do most calculations.

Here are some simple cases:

- [harmonic conjugate](projective/harmonic-c.py)
- [harmonic conjugate of pole-polar](projective/pole-polar-circle-c1.py) and [converse](projective/pole-polar-circle-c2.py) for a circle
- [Menelaus's theorem](projective/menelaus-c1.py) (and its [converse](projective/menelaus-c2.py)) and [Ceva's theorem](projective/ceva-c1.py) (and its [converse](projective/ceva-c2.py))
- [Desargues's theorem](projective/desargues-c1.py) (and its [dual](projective/desargues-c2.py)) and [Pappus's theorem](projective/pappus-c1.py) (and its [dual](projective/pappus-c2.py))
- [Pascal's theorem](projective/pascal-circle-c.py) and [Brianchon's theorem](projective/brianchon-circle-c.py) for a circle, and their [quadrilateral](projective/pascal-brianchon-circle-c4.py) form
- [Brokard's theorem](projective/brokard-c.py)
- [butterfly theorem](projective/butterfly-c.py), an analytic geometry proof without Vieta's formulas

However, it is more complicated to prove Pascal's theorem for a conic in a direct way, which means we don't reduce the conic to a circle by a projective transformation.

#### Pascal's theorem

Let's put point *I* onto the origin, rotate the hexagon to make *BE* parallel to x-axis, denote the conic *ADBFCE* as:

<img src="https://latex.codecogs.com/gif.latex?ax^2+2bxy+cy^2+2dx+2ey+f=0">

and denote *AF*, *CD* and *BE* as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}AF:y=gx\\CD:y=hx\\BE:y=k\end{cases}">

We get two roots by solving the combination of a conic and a straight line. However, SymPy won't tell us whether the first root denotes the point in the left or right side. So we need to guess then verify by numerical evaluation.

Assume the conic is <img src="https://latex.codecogs.com/gif.latex?x^2+y^2-1=0"> and the line *AF* is <img src="https://latex.codecogs.com/gif.latex?y=x">, we should get *A* in quadrant I and *F* in quadrant III. So we should use `F, A = solve(...)` but not `A, F = solve(...)`. Then we get 6 points:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{A}=-\dfrac{d+eg-\sqrt{-af-2bfg-cfg^2+d^2+2deg+e^2g^2}}{a+2bg+cg^2}\\[1em]x_\text{B}=-\dfrac{bk+d+\sqrt{-ack^2-2aek-af+b^2k^2+2bdk+d^2}}a\\[1em]x_\text{C}=-\dfrac{d+eh-\sqrt{-af-2bfh-cfh^2+d^2+2deh+e^2h^2}}{a+2bh+ch^2}\\[1em]x_\text{D}=-\dfrac{d+eh+\sqrt{-af-2bfh-cfh^2+d^2+2deh+e^2h^2}}{a+2bh+ch^2}\\[1em]x_\text{E}=-\dfrac{bk+d-\sqrt{-ack^2-2aek-af+b^2k^2+2bdk+d^2}}a\\[1em]x_\text{F}=-\dfrac{d+eg+\sqrt{-af-2bfg-cfg^2+d^2+2deg+e^2g^2}}{a+2bg+cg^2}\end{cases}\;\text{(Eq.\,1)">

Without further simplification, SymPy can hardly solve the intersections *G* and *H*. (This may be due to too many fraction calculations.<sup>[1]</sup> I don't know if Mathematica or other alternatives can do this.) So we need to replace all square roots with:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}P=\sqrt{-af-2bfg-cfg^2+d^2+2deg+e^2g^2}\\Q=\sqrt{-af-2bfh-cfh^2+d^2+2deh+e^2h^2}\\R=\sqrt{-ack^2-2aek-af+b^2k^2+2bdk+d^2}\end{cases}\;\text{(Eq.\,2)}">

Then the 6 points are simplified as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{A}=-\dfrac{d+eg-P}{a+2bg+cg^2}\\[1em]x_\text{B}=-\dfrac{bk+d+R}a\\[1em]x_\text{C}=-\dfrac{d+eh-Q}{a+2bh+ch^2}\\[1em]x_\text{D}=-\dfrac{d+eh+Q}{a+2bh+ch^2}\\[1em]x_\text{E}=-\dfrac{bk+d-R}a\\[1em]x_\text{F}=-\dfrac{d+eg+P}{a+2bg+cg^2}\end{cases}">

Then we get *AB*, *DE*, *BC* and *EF*, and their intersections *G* and *H*, and the expression <img src="https://latex.codecogs.com/gif.latex?x_\text{G}y_\text{H}-x_\text{H}y_\text{G}"> to check if *G*, *H* and *I* are collinear.

The numerator of this expression contains 422 terms, where so many *P*, *Q* and *R* appear. We replace them back with Eq. 2, then get the final result 0, which means *G*, *H* and *I* are collinear.

[Here](projective/pascal-c.py) is the proof process.

#### Braikenridge-Maclaurin theorem

**Braikenridge-Maclaurin theorem** is the converse to Pascal's theorem.

We use the diagram of Pascal's theorem and put *I* onto the origin again. But here we rotate the hexagon to make *GH* onto y-axis, and denote 6 lines as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}AB:y=jx+g\\DE:y=kx+g\\BC:y=mx+h\\EF:y=nx+h\\AF:y=px\\CD:y=qx\end{cases}">

Let's assume the conic doesn't go through origin *I*, then we need to prove the 6 points:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A:\left(\dfrac{g}{p-j},\dfrac{gp}{p-j}\right)\\[1em]B:\left(\dfrac{h-g}{j-m},\dfrac{hj-gm}{j-m}\right)\\[1em]C:\left(\dfrac{h}{q-m},\dfrac{hq}{q-m}\right)\\[1em]D:\left(\dfrac{g}{q-k},\dfrac{gq}{q-k}\right)\\[1em]E:\left(\dfrac{h-g}{k-n},\dfrac{hk-gn}{k-n}\right)\\[1em]F:\left(\dfrac{h}{p-n},\dfrac{hp}{p-n}\right)\end{cases}">

lie on the a conic.

According to [this rule](https://en.wikipedia.org/wiki/Five_points_determine_a_conic#Construction), we just need to prove:

<img src="https://latex.codecogs.com/gif.latex?{\det\left[\begin{matrix}\dfrac{g^2}{\left(p-j\right)^2}&\dfrac{g^2p}{\left(p-j\right)^2}&\dfrac{g^2p^2}{\left(p-j\right)^2}&\dfrac{g}{p-j}&\dfrac{gp}{p-j}&1\\\dfrac{\left(h-g\right)^2}{\left(j-m\right)^2}&\dfrac{\left(h-g\right)\left(hj-gm\right)}{\left(j-m\right)^2}&\dfrac{\left(hj-gm\right)^2}{\left(j-m\right)^2}&\dfrac{h-g}{j-m}&\dfrac{hj-gm}{j-m}&1\\\dfrac{h^2}{\left(q-m\right)^2}&\dfrac{h^2q}{\left(q-m\right)^2}&\dfrac{h^2q^2}{\left(q-m\right)^2}&\dfrac{h}{q-m}&\dfrac{hq}{q-m}&1\\\dfrac{g^2}{\left(q-k\right)^2}&\dfrac{g^2q}{\left(q-k\right)^2}&\dfrac{g^2q^2}{\left(q-k\right)^2}&\dfrac{g}{q-k}&\dfrac{gq}{q-k}&1\\\dfrac{\left(h-g\right)^2}{\left(k-n\right)^2}&\dfrac{\left(h-g\right)\left(hk-gn\right)}{\left(k-n\right)^2}&\dfrac{\left(hk-gn\right)^2}{\left(k-n\right)^2}&\dfrac{h-g}{k-n}&\dfrac{hk-gn}{k-n}&1\\\dfrac{h^2}{\left(p-n\right)^2}&\dfrac{h^2p}{\left(p-n\right)^2}&\dfrac{h^2p^2}{\left(p-n\right)^2}&\dfrac{h}{p-n}&\dfrac{hp}{p-n}&1\end{matrix}\right]=0}">

[Here](projective/braikenridge-maclaurin-c.py) is the proof process.<sup>[2]</sup>

### Proof by Homogeneous coordinates

Because homogeneous coordinates have many advantages mentioned [here](desargues.md#proof-by-homogeneous-coordinates), we can use SymPy to prove it in a very simple process.

#### Pascal's theorem

[Here](projective/pascal-h.py) we change all Cartesian to homogeneous from Eq. 1 to avoid fraction calculations.

#### Brianchon's theorem

<img src="diagrams/brianchon.png">

**Brianchon's theorem** states that when a hexagon (marked as *ad-db-bf-fc-ce-ea*) is circumscribed around a conic section (where the 6 tangent points are *ADBFCE*), its principal diagonals (*ad-fc*, *db-ce* and *bf-ea*) meet in a single point.

We still use the 6 points in Eq. 1 but this time we draw their 6 tangent lines to form a hexagon.

We apply [derivative of implicit function](https://en.wikipedia.org/wiki/Implicit_function#Implicit_differentiation) on curve <img src="https://latex.codecogs.com/gif.latex?F(x,y)=0">, then the tangent line passing through point <img src="https://latex.codecogs.com/gif.latex?(x_0,y_0)"> is:

<img src="https://latex.codecogs.com/gif.latex?F_x(x_0,y_0)(x-x_0)+F_y(y_0,y_0)(y-y_0)=0">

When the conic is denoted as <img src="https://latex.codecogs.com/gif.latex?F(x,y)=ax^2+2bxy+cy^2+2dx+2ey+f=0">, we have <img src="https://latex.codecogs.com/gif.latex?F_x=2ax+2by+2d"> and <img src="https://latex.codecogs.com/gif.latex?F_y=2bx+2cy+2e">, so the tangent line is:

<img src="https://latex.codecogs.com/gif.latex?(ax_0+by_0+d)x+(bx_0+cy_0+e)y+(dx_0+ey_0+f)=0">

(Note that <img src="https://latex.codecogs.com/gif.latex?ax_0^2+2bx_0y_0+cy_0^2+2dx_0+2ey_0+f=0">.)

In [this proof](projective/brianchon-h.py), each point is denoted as homogeneous coordinate <img src="https://latex.codecogs.com/gif.latex?(x_0,y_0,z_0)">, then the tangent line is:

<img src="https://latex.codecogs.com/gif.latex?[ax_0+by_0+dz_0,bx_0+cy_0+ez_0,dx_0+ey_0+fz_0]">

We start from these 6 tangent lines, then get the 6 vertices of the hexagon, then prove the concurrency of its principal diagonals.

#### Conic equation in Homogeneous coordinates

A conic can be represented as an equation in homogeneous coordinates:

<img src="https://latex.codecogs.com/gif.latex?ax^2+2bxy+cy^2+2dxz+2eyz+fz^2=0">

If a point *P*(*x*,*y*,*z*) is on this conic, it should follow:

<img src="https://latex.codecogs.com/gif.latex?z=\frac{-dx-ey\pm\sqrt{-afx^2-2bfxy-cfy^2+d^2x^2+2dexy+e^2y^2}}{f}">

So we can rewrite the point as:

<img src="https://latex.codecogs.com/gif.latex?P(fx,fy,-dx-ey\pm\sqrt{-afx^2-2bfxy-cfy^2+d^2x^2+2dexy+e^2y^2})">

Either of the two roots can be used in the proof. For example, we can apply positive roots on points *ABCD*, and apply negative roots on points *EF*.

The [proof process](projective/pascal-brianchon-h.py) is very similar to [Pappus's theorem](desargues.md#proof-of-pappuss-theorem), and proves both **Pascal's theorem** and **Brianchon's theorem**, because the conic equation can represent a **point conic** (where *ABCDEF* are 6 points) or a **[line conic](https://en.wikipedia.org/wiki/Conic_section#Line_conics)** (where *ABCDEF* are 6 straight lines).

#### Braikenridge-Maclaurin theorem

We choose 3 arbitrary points *A*, *C* and *E* as 3 of 6 vertices on a hexagon, and set 3 collinear points *GHJ*. Put *E* onto x-axis and *GHJ* onto y-axis to reduce variables, then we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A:(a,b,c)\\C:(d,e,f)\\E:(g,0,h)\\G:(0,j,k)\\H:(0,m,n)\\J:(0,p,q)\end{cases}">

Then we can calculate the other 3 of 6 vertices:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}B=AB{\cap}BC=AG{\cap}HC\\D=CD{\cap}DE=CJ{\cap}GE\\F=EF{\cap}FA=EH{\cap}JA\end{cases}">

After some calculations [here](projective/braikenridge-maclaurin-h.py), we get:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}x_\text{A}^2&x_\text{A}y_\text{A}&y_\text{A}^2&x_\text{A}z_\text{A}&y_\text{A}z_\text{A}&z_\text{A}^2\\x_\text{B}^2&x_\text{B}y_\text{B}&y_\text{B}^2&x_\text{B}z_\text{B}&y_\text{B}z_\text{B}&z_\text{B}^2\\x_\text{C}^2&x_\text{C}y_\text{C}&y_\text{C}^2&x_\text{C}z_\text{C}&y_\text{C}z_\text{C}&z_\text{C}^2\\x_\text{D}^2&x_\text{D}y_\text{D}&y_\text{D}^2&x_\text{D}z_\text{D}&y_\text{D}z_\text{D}&z_\text{D}^2\\x_\text{E}^2&x_\text{E}y_\text{E}&y_\text{E}^2&x_\text{E}z_\text{E}&y_\text{E}z_\text{E}&z_\text{E}^2\\x_\text{F}^2&x_\text{F}y_\text{F}&y_\text{F}^2&x_\text{F}z_\text{F}&y_\text{F}z_\text{F}&z_\text{F}^2\end{matrix}\right]=0">

which implies all 6 vertices lying on a conic.

This process also proves its dual theorem (which is also the converse of Brianchon's theorem).

### Notes

1. More explanations can be found [here](https://docs.sympy.org/latest/tutorial/simplification.html).
2. More details can be found [here](https://math.stackexchange.com/questions/4232539) and [here](https://docs.sympy.org/latest/modules/matrices/matrices.html#sympy.matrices.matrices.MatrixDeterminant.det).