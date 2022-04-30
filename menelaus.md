<img src="diagrams/menelaus.png">

<img src="diagrams/ceva.png">

In a triangle *ABC*: *D*, *E* and *F* are three points on edges *BC*, *CA* and *AB* respectively. <sup>[1]</sup>

**Menelaus's theorem** states that *D*, *E* and *F* are collinear if and only if:

<img src="https://latex.codecogs.com/gif.latex?\frac{\overrightarrow{BD}}{\overrightarrow{CD}}\cdot\frac{\overrightarrow{CE}}{\overrightarrow{AE}}\cdot\frac{\overrightarrow{AF}}{\overrightarrow{BF}}=1">

**Ceva's theorem** states that *AD*, *BE* and *CF* are concurrent if and only if:

<img src="https://latex.codecogs.com/gif.latex?\frac{\overrightarrow{BD}}{\overrightarrow{CD}}\cdot\frac{\overrightarrow{CE}}{\overrightarrow{AE}}\cdot\frac{\overrightarrow{AF}}{\overrightarrow{BF}}=-1">

When all points *ABCDEF* are written as homogeneous coordinates, we use some properties mentioned [here](desargues.md#tricks) (Trick 2c) and get:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}D=B+C\\E=C+A\\F=A+nB\end{cases}">

Then we calculate each ratio:

<img src="https://latex.codecogs.com/gif.latex?\frac{\overrightarrow{BD}}{\overrightarrow{CD}}=\frac{\dfrac{x_\text{B}}{z_\text{B}}-\dfrac{x_\text{D}}{z_\text{D}}}{\dfrac{x_\text{C}}{z_\text{C}}-\dfrac{x_\text{D}}{z_\text{D}}}=\frac{\dfrac{x_\text{B}}{z_\text{B}}-\dfrac{x_\text{B}+x_\text{C}}{z_\text{B}+z_\text{C}}}{\dfrac{x_\text{C}}{z_\text{C}}-\dfrac{x_\text{B}+x_\text{C}}{z_\text{B}+z_\text{C}}}=\dots=-\frac{z_\text{C}}{z_\text{B}}">

Analogously, we have <img src="https://latex.codecogs.com/gif.latex?\overrightarrow{CE}/\overrightarrow{AE}=-z_\text{A}/z_\text{C}"> and <img src="https://latex.codecogs.com/gif.latex?\overrightarrow{AF}/\overrightarrow{BF}=-nz_\text{B}/z_\text{A}">. Then we get:

<img src="https://latex.codecogs.com/gif.latex?\frac{\overrightarrow{BD}}{\overrightarrow{CD}}\cdot\frac{\overrightarrow{CE}}{\overrightarrow{AE}}\cdot\frac{\overrightarrow{AF}}{\overrightarrow{BF}}=-n">

Take (*A*, *B*, *C*) as basis, then *D*, *E* and *F* are collinear if and only if:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}0&1&1\\1&0&1\\1&n&0\end{matrix}\right]=0">

i.e. *n* = -1, which proves Menelaus's theorem. <sup>[2]</sup>

To prove Ceva's theorem, we should calculate *AD*, *BE* and *CF* by [Trick 3](desargues.md#tricks):

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}AD:-y+z=0\\BE:x-z=0\\CF:-nx+y=0\end{cases}">

where (*x*, *y*, *z*) are coefficients on basis (*A*, *B*, *C*).

Then they are concurrent if and only if:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}0&-1&1\\1&0&-1\\-n&1&0\end{matrix}\right]=0">

i.e. *n* = 1. <sup>[3]</sup>

### Duality

It is not obvious that Menelaus's theorem and Ceva's theorem are dual. Let's start from this theorem:

**Theorem 1** A straight line intersects a triangle *ABC*'s three edges *BC*, *CA* and *AB* at point *D*<sub>0</sub>, *E*<sub>0</sub> and *F*<sub>0</sub> respectively. Take another three points *D*, *E* and *F* on *BC*, *CA* and *AB* respectively, then *D*, *E* and *F* are collinear if and only if:

<img src="https://latex.codecogs.com/gif.latex?(B,C;D,D_0)\cdot(C,A;E,E_0)\cdot(A,B;F,F_0)=1">

A simple proof uses the lemma that if four different collinear points are represented in homogeneous coordinates as *A*, *B*, *C*=*A*+*mB* and *D*=*A*+*nB* (*m* and *n* are not zero), then <img src="https://latex.codecogs.com/gif.latex?(A,B;C,D)=m/n">. <sup>[4]</sup>

When we write *D*<sub>0</sub>, *E*<sub>0</sub>, *F*<sub>0</sub>, *D*, *E* and *F* as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}D_0=B+kC\\E_0=C+mA\\F_0=A+nB\\D=B+pC\\E=C+qA\\F=A+rB\end{cases}">

it's easy to prove that *D*<sub>0</sub>, *E*<sub>0</sub> and *F*<sub>0</sub> are collinear if and only if <img src="https://latex.codecogs.com/gif.latex?kmn=-1">, and *D*, *E* and *F* are collinear if and only if <img src="https://latex.codecogs.com/gif.latex?pqr=-1">. Then we get the product of three cross-ratios and finish the proof. <sup>[5]</sup>

When *D*<sub>0</sub>, *E*<sub>0</sub> and *F*<sub>0</sub> are at infinity, we get Menelaus's theorem.

The dual theorem states as:

**Theorem 1'** Three line *d*<sub>0</sub>, *e*<sub>0</sub> and *f*<sub>0</sub> passing through a triangle *abc*'s 3 vertices *A*=*b*∩*c*, *B*=*c*∩*a* and *C*=*a*∩*b* respectively and meet at a point. Take another three lines *d*, *e* and *f* passing through *A*, *B* and *C* respectively, then *d*, *e* and *f* meet at another point if and only if:

<img src="https://latex.codecogs.com/gif.latex?(b,c;d,d_0)\cdot(c,a;e,e_0)\cdot(a,b;f,f_0)=1">

When *d*<sub>0</sub>, *e*<sub>0</sub> and *f*<sub>0</sub> meet at the incenter, which means <img src="https://latex.codecogs.com/gif.latex?\widehat{bd_0}=-\widehat{cd_0}">, <img src="https://latex.codecogs.com/gif.latex?\widehat{ce_0}=-\widehat{ae_0}"> and <img src="https://latex.codecogs.com/gif.latex?\widehat{af_0}=-\widehat{bf_0}">, we get another form of Ceva's theorem: <sup>[6]</sup>

<img src="https://latex.codecogs.com/gif.latex?\frac{\sin\widehat{bd}}{\sin\widehat{cd}}\cdot\frac{\sin\widehat{ce}}{\sin\widehat{ae}}\cdot\frac{\sin\widehat{af}}{\sin\widehat{bf}}=-1">

[Here](https://www.heldermann-verlag.de/jgg/jgg11/j11h1beni.pdf) is a similar explanation of the duality. [Here](https://staff.imsa.edu/~fogel/ModGeo/PDF/24%20Menelaus%20Ceva.pdf) is an explanation by barycentric coordinates.

### Notes

1. We use the diagrams from [here](https://en.wikipedia.org/wiki/Menelaus%27s_theorem) and [here](https://en.wikipedia.org/wiki/Ceva%27s_theorem).
2. [Here](projective/menelaus-c1.py) and [here](projective/menelaus-c2.py) are proofs of Menelaus's theorem by Cartesian coordinates.
3. [Here](projective/ceva-c1.py) and [here](projective/ceva-c2.py) are proofs of Ceva's theorem by Cartesian coordinates.
4. [Here](projective/cross-ratio.py) is the proof.
5. [Here](projective/menelaus-ceva-v1.py) and [here](projective/menelaus-ceva-v2.py) are vector space proofs.
6. [Here](https://www.cut-the-knot.org/triangle/TrigCeva.shtml) is the explanation.