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

### Notes

1. We use the diagrams from [here](https://en.wikipedia.org/wiki/Menelaus%27s_theorem) and [here](https://en.wikipedia.org/wiki/Ceva%27s_theorem).
2. [Here](projective/menelaus-c1.py) and [here](projective/menelaus-c2.py) are proofs of Menelaus's theorem by Cartesian coordinates.
3. [Here](projective/ceva-c1.py) and [here](projective/ceva-c2.py) are proofs of Ceva's theorem by Cartesian coordinates.