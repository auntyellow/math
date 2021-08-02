The [diagram](https://en.wikipedia.org/wiki/File:Butterfly_theorem.svg) from [Wikipedia](https://en.wikipedia.org/wiki/Butterfly_theorem) is wrong because M is not the midpoint of PQ and XY.

Here we use the diagram from [Mathoman's website](http://www.mathoman.com/de/index.php/1529-verschiedene-sehnen-in-einem-kreis):

<img src="diagrams/butterfly.png">

The **butterfly theorem** can be stated as: Let M be the midpoint of a chord AB of a circle, through which two other chords PQ and RS are drawn; PS and QR intersect chord AB at C and D correspondingly. Then M is the midpoint of CD.

The theorem can be generalized in two ways:

1. Change the circle to any conic curve;
2. Change the condition *MA* = *MB* and *MC* = *MD* to 1/*MA* - 1/*MB* = 1/*MC* - 1/*MD*.

### Proof by Analytic Geometry

Here we prove the combination of 2 generalized forms.

We put *M* onto the origin of Cartesian coordinates and *B* onto positive x-axis.

#### Step 1

The conic curve *APRBQS* can be represented as:

<img src="https://latex.codecogs.com/gif.latex?ax^2+bxy+cy^2+dx+ey+f=0">

The coordinates of *A* and *B* are:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{A}=-MA\\y_\text{A}=0\\x_\text{B}=MB\\y_\text{B}=0\end{cases}">

Make *y* = 0 then we get <img src="https://latex.codecogs.com/gif.latex?ax^2+dx+f=0">. So *x*<sub>A</sub> and *x*<sub>B</sub> are two roots of this equation.

<img src="https://latex.codecogs.com/gif.latex?\frac{1}{MA}-\frac{1}{MB}=-\frac{1}{x_\text{A}}-\frac{1}{x_\text{B}}=-\frac{x_\text{A}+x_\text{B}}{x_\text{A}x_\text{B}}=\frac{d}f">

#### Step 2

The coordinates of *C* and *D* can be calculated by <img src="https://latex.codecogs.com/gif.latex?\frac{y_\text{C}-y_\text{P}}{x_\text{C}-x_\text{P}}=\frac{y_\text{C}-y_\text{S}}{x_\text{C}-x_\text{S}}"> and <img src="https://latex.codecogs.com/gif.latex?\frac{y_\text{D}-y_\text{Q}}{x_\text{D}-x_\text{Q}}=\frac{y_\text{D}-y_\text{R}}{x_\text{D}-x_\text{R}}">.

If *PS* or *QR* can be perpendicular to *AB*, the above equations should be written as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}({y_\text{C}-y_\text{P}})({x_\text{C}-x_\text{S}})=({y_\text{C}-y_\text{S}})({x_\text{C}-x_\text{P}})\\({y_\text{D}-y_\text{Q}})({x_\text{D}-x_\text{R}})=({y_\text{D}-y_\text{Q}})({x_\text{D}-x_\text{R}})\end{cases}">

Represent lines *PQ* and *RS* as *y* = *qx* and *y* = *rx*, then all y-coordinates can be replaced with 0 or x-coordinates:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}y_\text{C}=0\\y_\text{D}=0\\y_\text{P}=qx_\text{P}\\y_\text{Q}=qx_\text{Q}\\y_\text{R}=rx_\text{R}\\y_\text{S}=rx_\text{S}\\\end{cases}">

...

A similar proof can be found [here](https://www.cut-the-knot.org/pythagoras/Butterfly.shtml) (Proof 18).