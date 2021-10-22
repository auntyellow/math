<img src="diagrams/menelaus.png">

<img src="diagrams/ceva.png">

In a triangle *ABC*: *D*, *E* and *F* are three points on edges *BC*, *CA* and *AB* respectively. <sup>[1]</sup>

**Menelaus's theorem** states that *D*, *E* and *F* are collinear if and only if:

<img src="https://latex.codecogs.com/gif.latex?\frac{\overrightarrow{BD}}{\overrightarrow{CD}}\cdot\frac{\overrightarrow{CE}}{\overrightarrow{AE}}\cdot\frac{\overrightarrow{AF}}{\overrightarrow{BF}}=1">

**Ceva's theorem** states that *AD*, *BE* and *CF* are concurrent if and only if:

<img src="https://latex.codecogs.com/gif.latex?\frac{\overrightarrow{BD}}{\overrightarrow{CD}}\cdot\frac{\overrightarrow{CE}}{\overrightarrow{AE}}\cdot\frac{\overrightarrow{AF}}{\overrightarrow{BF}}=-1">

When all points *ABCDEF* are written as homogeneous coordinates, we use some properties mentioned [here](desargues.md#proof-by-homogeneous-coordinates) and get:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}D=gB+hC\\E=jC+kA\\F=mA+nB\end{cases}">

Then we calculate each ratio:

<img src="https://latex.codecogs.com/gif.latex?\frac{\overrightarrow{BD}}{\overrightarrow{CD}}=\frac{\frac{x_\text{B}}{z_\text{B}}-\frac{x_\text{D}}{z_\text{D}}}{\frac{x_\text{C}}{z_\text{C}}-\frac{x_\text{D}}{z_\text{D}}}=\frac{\frac{x_\text{B}}{z_\text{B}}-\frac{gx_\text{B}+hx_\text{C}}{gz_\text{B}+hz_\text{C}}}{\frac{x_\text{C}}{z_\text{C}}-\frac{gx_\text{B}+hx_\text{C}}{gz_\text{B}+hz_\text{C}}}=\dots=-\frac{hz_\text{C}}{gz_\text{B}}">

Analogously, we have <img src="https://latex.codecogs.com/gif.latex?\overrightarrow{CE}/\overrightarrow{AE}=-kz_\text{A}/jz_\text{C}"> and <img src="https://latex.codecogs.com/gif.latex?\overrightarrow{AF}/\overrightarrow{BF}=-nz_\text{B}/mz_\text{A}">. Then we get:

<img src="https://latex.codecogs.com/gif.latex?\frac{\overrightarrow{BD}}{\overrightarrow{CD}}\cdot\frac{\overrightarrow{CE}}{\overrightarrow{AE}}\cdot\frac{\overrightarrow{AF}}{\overrightarrow{BF}}=-\frac{hkn}{gjm}">

Take (*A*, *B*, *C*) as basis, then *D*, *E* and *F* are collinear if and only if:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}0&g&h\\k&0&j\\m&n&0\end{matrix}\right]=0">

We rewrite it as <img src="https://latex.codecogs.com/gif.latex?-hkn/gjm=1">, which proves Menelaus's theorem. <sup>[2]</sup>

Now let's prove Ceva's theorem.

Let *O* be a point on *AD*, then *AD*, *BE* and *CF* are concurrent if and only if both *BOE* and *COF* are collinear.

When written as homogeneous coordinates, <img src="https://latex.codecogs.com/gif.latex?O=pA+qD=pA+gqB+hqC">, then *AD*, *BE* and *CF* are concurrent if and only if:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}0&1&0\\p&gq&hq\\k&0&j\end{matrix}\right]=0\quad\&\enspace\det\left[\begin{matrix}0&0&1\\p&gq&hq\\m&n&0\end{matrix}\right]=0">

We get <img src="https://latex.codecogs.com/gif.latex?hkn/gjm=1"> by eliminating *p* and *q*. Conversely, <img src="https://latex.codecogs.com/gif.latex?hkn/gjm=1"> means there exists *p* and *q* matching the above two equations. Therefore, Ceva's theorem is proved. <sup>[3]</sup>

### Duality

It is not obvious that Menelaus's theorem and Ceva's theorem are dual. But please look at this theorem:

A straight line intersects a triangle *ABC*'s three edges *BC*, *CA* and *AB* at point *D*<sub>0</sub>, *E*<sub>0</sub> and *F*<sub>0</sub> respectively. Take another three points *D*, *E* and *F* on *BC*, *CA* and *AB* respectively, then *D*, *E* and *F* are collinear if and only if:

<img src="https://latex.codecogs.com/gif.latex?(B,C;D,D_0)\cdot(C,A;E,E_0)\cdot(A,B;F,F_0)=1">

A simple proof uses the lemma that if four different collinear points are represented in homogeneous coordinates as *A*, *B*, *C*(*A*+*mB*) and *D*(*A*+*nB*) (*m* and *n* are not zero), then <img src="https://latex.codecogs.com/gif.latex?(A,B;C,D)=m/n">.

When we write *D*<sub>0</sub>, *E*<sub>0</sub>, *F*<sub>0</sub>, *D*, *E* and *F* as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}D_0=B+kC\\E_0=C+mA\\F_0=A+nB\\D=B+pC\\E=C+qA\\F=A+rB\end{cases}">

it's easy to prove that *D*<sub>0</sub>, *E*<sub>0</sub> and *F*<sub>0</sub> are collinear if and only if <img src="https://latex.codecogs.com/gif.latex?kmn=-1">, and *D*, *E* and *F* are collinear if and only if <img src="https://latex.codecogs.com/gif.latex?pqr=-1">. Then we get the product of three cross-ratios and complete the proof. <sup>[4]</sup>

When *D*<sub>0</sub>, *E*<sub>0</sub> and *F*<sub>0</sub> are at infinity, we get Menelaus's theorem.

The dual theorem states as:

Three line *d*<sub>0</sub>, *e*<sub>0</sub> and *f*<sub>0</sub> passing through a triangle *abc*'s 3 vertices *A*=*b*∩*c*, *B*=*c*∩*a* and *C*=*a*∩*b* respectively and meet at a point. Take another three lines *d*, *e* and *f* passing through *A*, *B* and *C* respectively, then *d*, *e* and *f* meet at another point if and only if:

<img src="https://latex.codecogs.com/gif.latex?(b,c;d,d_0)\cdot(c,a;e,e_0)\cdot(a,b;f,f_0)=1">

When *d*<sub>0</sub>, *e*<sub>0</sub> and *f*<sub>0</sub> meet at the incenter, which means <img src="https://latex.codecogs.com/gif.latex?\widehat{bd_0}=-\widehat{cd_0}">, <img src="https://latex.codecogs.com/gif.latex?\widehat{ce_0}=-\widehat{ae_0}"> and <img src="https://latex.codecogs.com/gif.latex?\widehat{af_0}=-\widehat{bf_0}">, we get another form of Ceva's theorem:

<img src="https://latex.codecogs.com/gif.latex?\frac{\sin\widehat{bd}}{\sin\widehat{cd}}\cdot\frac{\sin\widehat{ce}}{\sin\widehat{ae}}\cdot\frac{\sin\widehat{af}}{\sin\widehat{bf}}=-1"> <sup>[5]</sup>

### Notes

1. We use the diagrams from [here](https://en.wikipedia.org/wiki/Menelaus%27s_theorem) and [here](https://en.wikipedia.org/wiki/Ceva%27s_theorem).
2. [Here](projective/menelaus-c1.py) and [here](projective/menelaus-c2.py) are proofs of Menelaus's theorem by Cartesian coordinates.
3. [Here](projective/ceva-c1.py) and [here](projective/ceva-c2.py) are proofs of Ceva's theorem by Cartesian coordinates.
4. [Here](projective/menelaus-ceva-h1.py) and [here](projective/menelaus-ceva-h2.py) are proofs by homogeneous coordinates.
5. [Here](https://www.cut-the-knot.org/triangle/TrigCeva.shtml) is the explanation.