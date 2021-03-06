<img src="diagrams/butterfly.png">

The **butterfly theorem** can be stated as: Let *M* be the midpoint of a chord *AB* of a circle, through which two other chords *PQ* and *RS* are drawn; *PS* and *QR* intersect chord *AB* at *C* and *D* correspondingly. Then *M* is the midpoint of *CD*. <sup>[1]</sup>

This theorem can be generalized in two forms:

1. Generalize the circle to any conic section;
2. Generalize the condition *MA* = *MB* and *MC* = *MD* to <img src="https://latex.codecogs.com/gif.latex?\frac{1}{MA}-\frac{1}{MB}=\frac{1}{MC}-\frac{1}{MD}"> or <img src="https://latex.codecogs.com/gif.latex?\frac{1}{\overrightarrow{MA}}+\frac{1}{\overrightarrow{MB}}=\frac{1}{\overrightarrow{MC}}+\frac{1}{\overrightarrow{MD}}">.

### Proof by Analytic Geometry

Here we try to prove the combination of 2 generalized forms. <sup>[2]</sup>

We put *M* onto the origin of Cartesian coordinates and *B* onto positive x-axis.

#### Step 1

The conic *APRBQS* can be represented as:

<img src="https://latex.codecogs.com/gif.latex?ax^2+bxy+cy^2+dx+ey+f=0">

(Let's assume *M* not on the conic so that *f* ≠ 0.)

The coordinates of *A* and *B* are:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{A}=\overrightarrow{MA}\\y_\text{A}=0\\x_\text{B}=\overrightarrow{MB}\\y_\text{B}=0\end{cases}">

Make *y* = 0 then we get <img src="https://latex.codecogs.com/gif.latex?ax^2+dx+f=0">. So *x*<sub>A</sub> and *x*<sub>B</sub> are two roots of this equation.

Then we get:

<img src="https://latex.codecogs.com/gif.latex?\frac{1}{\overrightarrow{MA}}+\frac{1}{\overrightarrow{MB}}=\frac{1}{x_\text{A}}+\frac{1}{x_\text{B}}=\frac{x_\text{A}+x_\text{B}}{x_\text{A}x_\text{B}}=-\frac{d}f">

#### Step 2a

The coordinates of *C* and *D* can be calculated by:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{C}y_\text{P}+x_\text{P}y_\text{S}+x_\text{S}y_\text{C}=x_\text{P}y_\text{C}+x_\text{S}y_\text{P}+x_\text{C}y_\text{S}\\x_\text{D}y_\text{Q}+x_\text{Q}y_\text{R}+x_\text{R}y_\text{D}=x_\text{Q}y_\text{D}+x_\text{R}y_\text{Q}+x_\text{D}y_\text{R}\end{cases}\;\text{(Eq.\,2a)}">

Let's assume that neither *PQ* nor *RS* is perpendicular to *AB*, then *PQ* and *RS* can be represented as *y* = *qx* and *y* = *rx*. (We also assume *PQ* and *RS* not coinciding so that *q* ≠ *r*.)

(The case either *PQ* or *RS* perpendicular to *AB* will be proved in Step 2b.)

Then all y-coordinates can be replaced with 0 or x-coordinates:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}y_\text{C}=0\\y_\text{D}=0\\y_\text{P}=qx_\text{P}\\y_\text{Q}=qx_\text{Q}\\y_\text{R}=rx_\text{R}\\y_\text{S}=rx_\text{S}\end{cases}">

We solve *x*<sub>C</sub> and *x*<sub>D</sub> as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{C}=\dfrac{(q-r)x_\text{P}x_\text{S}}{qx_\text{P}-rx_\text{S}}\\[1em]x_\text{D}=\dfrac{(q-r)x_\text{Q}x_\text{R}}{qx_\text{Q}-rx_\text{R}}\end{cases}">

(Here *x*<sub>C</sub> and *x*<sub>D</sub> should exist because *y*<sub>P</sub> ≠ *y*<sub>S</sub> and *y*<sub>Q</sub> ≠ *y*<sub>R</sub>.)

Then we get:

<img src="https://latex.codecogs.com/gif.latex?\frac{1}{\overrightarrow{MC}}+\frac{1}{\overrightarrow{MD}}=\frac{1}{x_\text{C}}+\frac{1}{x_\text{D}}=\frac{x_\text{C}+x_\text{D}}{x_\text{C}x_\text{D}}=\frac{qx_\text{P}x_\text{Q}(x_\text{R}+x_\text{S})-r(x_\text{P}+x_\text{Q})x_\text{R}x_\text{S}}{(q-r)x_\text{P}x_\text{Q}x_\text{R}x_\text{S}}">

#### Step 3a

Note that *x*<sub>P</sub> and *x*<sub>Q</sub> are two roots of equations:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}ax^2+bxy+cy^2+dx+ey+f=0\\y=qx\end{cases}">

So we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{P}x_\text{Q}=\dfrac{f}Q\\x_\text{P}+x_\text{Q}=-\dfrac{d+eq}Q\end{cases}\;\text{(Eq.\,3a)}">

where <img src="https://latex.codecogs.com/gif.latex?Q=a+bq+cq^2">. (Here we don't consider *Q* = 0 because the line intersects the conic at two different points.)

Analogously, we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{R}x_\text{S}=\dfrac{f}R\\x_\text{R}+x_\text{S}=-\dfrac{d+er}R\end{cases}">

where <img src="https://latex.codecogs.com/gif.latex?R=a+br+cr^2">.

Finally, we get: <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?{\frac{1}{\overrightarrow{MC}}+\frac{1}{\overrightarrow{MD}}=\frac{q(x_\text{P}x_\text{Q})(x_\text{R}+x_\text{S})-r(x_\text{P}+x_\text{Q})(x_\text{R}x_\text{S})}{(q-r)(x_\text{P}x_\text{Q})(x_\text{R}x_\text{S})}=-\frac{d}f=\frac{1}{\overrightarrow{MA}}+\frac{1}{\overrightarrow{MB}}}">

#### Step 2b

If *RS* is perpendicular to *AB*, we can still use Eq. 2a but keep *y*<sub>R</sub> and *y*<sub>S</sub> not replaced:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}y_\text{C}=0\\y_\text{D}=0\\y_\text{P}=qx_\text{P}\\y_\text{Q}=qx_\text{Q}\\x_\text{R}=0\\x_\text{S}=0\end{cases}">

We solve *x*<sub>C</sub> and *x*<sub>D</sub> as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{C}=\dfrac{x_\text{P}y_\text{S}}{y_\text{S}-qx_\text{P}}\\[1em]x_\text{D}=\dfrac{x_\text{Q}y_\text{R}}{y_\text{R}-qx_\text{Q}}\end{cases}">

(Here *x*<sub>C</sub> and *x*<sub>D</sub> should exist because *y*<sub>P</sub> ≠ *y*<sub>S</sub> and *y*<sub>Q</sub> ≠ *y*<sub>R</sub>.)

Then we get:

<img src="https://latex.codecogs.com/gif.latex?\frac{1}{\overrightarrow{MC}}+\frac{1}{\overrightarrow{MD}}=\frac{1}{x_\text{C}}+\frac{1}{x_\text{D}}=\frac{x_\text{C}+x_\text{D}}{x_\text{C}x_\text{D}}=\frac{(x_\text{P}+x_\text{Q})y_\text{R}y_\text{S}-qx_\text{P}x_\text{Q}(y_\text{R}+y_\text{S})}{x_\text{P}x_\text{Q}y_\text{R}y_\text{S}}">

#### Step 3b

Note that *y*<sub>R</sub> and *y*<sub>S</sub> are two roots of equations:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}ax^2+bxy+cy^2+dx+ey+f=0\\x=0\end{cases}">

So we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}y_\text{R}y_\text{S}=\dfrac{f}c\\y_\text{R}+y_\text{S}=-\dfrac{e}c\end{cases}">

And we still have Eq. 3a.

Finally, we get:

<img src="https://latex.codecogs.com/gif.latex?\frac{1}{\overrightarrow{MC}}+\frac{1}{\overrightarrow{MD}}=\frac{(x_\text{P}+x_\text{Q})(y_\text{R}y_\text{S})-q(x_\text{P}x_\text{Q})(y_\text{R}+y_\text{S})}{(x_\text{P}x_\text{Q})(y_\text{R}y_\text{S})}=-\frac{d}f=\frac{1}{\overrightarrow{MA}}+\frac{1}{\overrightarrow{MB}}">

### Degenerate Conic

The generalized butterfly theorem still holds if the conic is degenerated to two lines.

In the below special case, *AB* is a chord of two lines *ASQ* and *BPR*, and *M* is a point on *AB*, through which two other lines *MPQ* and *MSR* are drawn; *PS* and *QR* intersect chord *AB* at the same point *C* (lines *AB*, *PS* and *QR* are concurrent at point *C*).

<img src="diagrams/harmonic.png">

According to the generalized butterfly theorem:

<img src="https://latex.codecogs.com/gif.latex?\frac{1}{\overrightarrow{MA}}+\frac{1}{\overrightarrow{MB}}=\frac{2}{\overrightarrow{MC}}">

In other words, (*M*, *C*) and (*A*, *B*) are [harmonic conjugates](https://en.wikipedia.org/wiki/Projective_harmonic_conjugate): <sup>[4]</sup>

<img src="https://latex.codecogs.com/gif.latex?(M,C;A,B)=\frac{\overrightarrow{MA}\overrightarrow{CB}}{\overrightarrow{MB}\overrightarrow{CA}}=-1">

### Notes

1. Here we use the diagram from [Mathoman's website](http://www.mathoman.com/de/index.php/1529-verschiedene-sehnen-in-einem-kreis). The [diagram](https://en.wikipedia.org/wiki/File:Butterfly_theorem.svg) from [Wikipedia](https://en.wikipedia.org/wiki/Butterfly_theorem) is wrong because M is not the midpoint of PQ and XY.
2. A similar proof (but not generalized forms) can be found [here](https://www.cut-the-knot.org/pythagoras/Butterfly.shtml) (Proof 18).
3. [Here](projective/butterfly.py) is a proof by SymPy without Vieta's formulas.
4. A simple proof of projective harmonic conjugate can be found [here](https://imomath.com/index.cgi?page=problemsInProjectiveGeometry) (Problem 1).