<img src="diagrams/desargues.png">

**Desargues's theorem** states: Two triangles (*A*<sub>1</sub>*B*<sub>1</sub>*C*<sub>1</sub> and *A*<sub>2</sub>*B*<sub>2</sub>*C*<sub>2</sub>) are in perspective axially (i.e. points *bc*, *ab* and *ac* are collinear) if and only if they are in perspective centrally (i.e. lines *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> are concurrent). <sup>[1]</sup>

### Proof by Cartesian coordinates

#### Collinear → Concurrent

Let's put point *ab* onto the origin, put *ac* and *bc* onto y-axis, and denote 6 lines of 2 triangles as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1B_1:y=gx\\A_2B_2:y=hx\\A_1C_1:y=jx+e\\A_2C_2:y=kx+e\\B_1C_1:y=mx+f\\B_2C_2:y=nx+f\end{cases}">

Then we get 6 vertices:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{A1}=e/(g-j)\\y_\text{A1}=eg/(g-j)\\x_\text{A2}=e/(h-k)\\y_\text{A2}=eh/(h-k)\\x_\text{B1}=f/(g-m)\\y_\text{B1}=fg/(g-m)\\x_\text{B2}=f/(h-n)\\y_\text{B2}=fh/(h-n)\\x_\text{C1}=(f-e)/(j-m)\\y_\text{C1}=(fj-em)/(j-m)\\x_\text{C2}=(f-e)/(k-n)\\y_\text{C2}=(fk-en)/(k-n)\end{cases}">

Then we denote lines *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1A_2:(y_\text{A1}-y_\text{A2})x+(x_\text{A2}-x_\text{A1})y+(x_\text{A1}y_\text{A2}-x_\text{A2}y_\text{A1})=0\\B_1B_2:(y_\text{B1}-y_\text{B2})x+(x_\text{B2}-x_\text{B1})y+(x_\text{B1}y_\text{B2}-x_\text{B2}y_\text{B1})=0\\C_1C_2:(y_\text{C1}-y_\text{C2})x+(x_\text{C2}-x_\text{C1})y+(x_\text{C1}y_\text{C2}-x_\text{C2}y_\text{C1})=0\end{cases}">

Finally, we calculate the determinant of 9 coefficients of these 3 lines and get:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}y_\text{A1}-y_\text{A2}&x_\text{A2}-x_\text{A1}&x_\text{A1}y_\text{A2}-x_\text{A2}y_\text{A1}\\y_\text{B1}-y_\text{B2}&x_\text{B2}-x_\text{B1}&x_\text{B1}y_\text{B2}-x_\text{B2}y_\text{B1}\\y_\text{C1}-y_\text{C2}&x_\text{C2}-x_\text{C1}&x_\text{C1}y_\text{C2}-x_\text{C2}y_\text{C1}\end{matrix}\right]=0">

which means *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> are concurrent. <sup>[2]</sup>

#### Concurrent → Collinear

Let's put concurrent point *O* onto the origin, put *A*<sub>1</sub>*A*<sub>2</sub> onto x-axis, and denote lines *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1A_2:y=0\\B_1B_2:y=ex\\C_1C_2:y=fx\end{cases}">

and 6 vertices are:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1:(g,0)\\A_2:(h,0)\\B_1:(j,ej)\\B_2:(k,ek)\\C_1:(m,fm)\\C_2:(n,fn)\end{cases}">

Then we denote 6 lines of 2 triangles as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1B_1:g\cdot%20ej+j\cdot%20y=g\cdot%20y+x\cdot%20ej\\A_1C_1:g\cdot%20fm+m\cdot%20y=g\cdot%20y+x\cdot%20fm\\B_1C_1:x\cdot%20ej+j\cdot%20fm+m\cdot%20y=j\cdot%20y+m\cdot%20ej+x\cdot%20fm\\A_2B_2:h\cdot%20ek+k\cdot%20y=h\cdot%20y+x\cdot%20ek\\A_2C_2:h\cdot%20fn+n\cdot%20y=h\cdot%20y+x\cdot%20fn\\B_2C_2:x\cdot%20ek+k\cdot%20fn+n\cdot%20y=k\cdot%20y+n\cdot%20ek+x\cdot%20fn\end{cases}">

Finally, we get *ab*, *ac* and *bc*:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{ab}=(-ghj+ghk+gjk-hjk)/(gk-hj)\\y_\text{ab}=(egjk-ehjk)/(gk-hj)\\x_\text{ac}=(-ghm+ghn+gmn-hmn)/(gn-hm)\\y_\text{ac}=(fgmn-fhmn)/(gn-hm)\\x_\text{bc}=(-jkm+jkn+jmn-kmn)/(jn-km)\\y_\text{bc}=(-ejkm+ejkn+fjmn-fkmn)/(jn-km)\end{cases}">

which are collinear, i.e. <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?x_\text{ab}y_\text{ac}+x_\text{ac}y_\text{bc}+x_\text{bc}y_\text{ab}=x_\text{ac}y_\text{ab}+x_\text{bc}y_\text{ac}+x_\text{ab}y_\text{bc}">

### Proof by Homogeneous coordinates

**Homogeneous coordinates** are widely used in projective geometry. Because of the [Duality](https://en.wikipedia.org/wiki/Homogeneous_coordinates#Line_coordinates_and_duality), both point and straight line can be represented as homogeneous coordinates, and share the same form:

- The straight line passing through 2 points <img src="https://latex.codecogs.com/gif.latex?(x_1,x_2,x_3)"> and <img src="https://latex.codecogs.com/gif.latex?(x'_1,x'_2,x'_3)"> is <img src="https://latex.codecogs.com/gif.latex?[x_2x'_3-x_3x'_2,x_3x'_1-x_1x'_3,x_1x'_2-x_2x'_1]">
- The intersection point of 2 straight lines <img src="https://latex.codecogs.com/gif.latex?[u_1,u_2,u_3]"> and <img src="https://latex.codecogs.com/gif.latex?[u'_1,u'_2,u'_3]"> is <img src="https://latex.codecogs.com/gif.latex?(u_2u'_3-u_3u'_2,u_3u'_1-u_1u'_3,u_1u'_2-u_2u'_1)">
- Three points <img src="https://latex.codecogs.com/gif.latex?(x_1,x_2,x_3)">, <img src="https://latex.codecogs.com/gif.latex?(x'_1,x'_2,x'_3)"> and <img src="https://latex.codecogs.com/gif.latex?(x''_1,x''_2,x''_3)"> are collinear if and only if <img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}x_1&x_2&x_3\\x'_1&x'_2&x'_3\\x''_1&x''_2&x''_3\end{matrix}\right]=0">
- Three straight lines <img src="https://latex.codecogs.com/gif.latex?[u_1,u_2,u_3]">, <img src="https://latex.codecogs.com/gif.latex?[u'_1,u'_2,u'_3]"> and <img src="https://latex.codecogs.com/gif.latex?[u''_1,u''_2,u''_3]"> are concurrent if and only if <img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}u_1&u_2&u_3\\u'_1&u'_2&u'_3\\u''_1&u''_2&u''_3\end{matrix}\right]=0">

#### Advantages

- A theorem and its dual theorem share the same proof process, so no necessary to prove twice.
- There are only additions, subtractions and multiplications during proof process, so all expressions are polynomials, which are simpler than rational functions.

#### Disadvantages

- Each point needs 3 variables, more than Cartesian coordinates.
- Should use origin and axes carefully, because the origin and axes are dual as lines and points at infinity.

For example, to reduce number of variables, we should carefully put a regular point *P*(*a*,*b*,*c*) onto special places:
- put onto origin as *P*(0,0,1), which may not work for the dual process because line [0,0,1] denotes a line at infinity;
- put onto y-axis as *P*(0,*b*,1), which may not cover the parallel case in "3 lines are parallel or concurrent at point *P*";  
- put onto y-axis as *P*(0,*b*,*c*), which may work well.

#### Trick

- Both <img src="https://latex.codecogs.com/gif.latex?(kx_1,kx_2,kx_3)"> and <img src="https://latex.codecogs.com/gif.latex?(x_1,x_2,x_3)"> denote the same point, so divide by their common factor as early as possible to simplify calculation.

#### Proof

[ ] TODO

### Notes

1. Here we use the diagram from [Cut the Knot](https://www.cut-the-knot.org/Curriculum/Geometry/Desargues.shtml).
2. This complicated result can be solved by SymPy [here](projective/desargues1.py).
3. This complicated result can be solved by SymPy [here](projective/desargues2.py).