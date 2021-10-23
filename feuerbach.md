### Euler line

<img src="diagrams/euler-line.png">

**Euler line** is a line passing through othocenter *H* (blue), nine-point center *N* (red), centroid *G* (orange) and circumcenter *O* (green), while *HN* = *NO* and *HG* = 2*GO*. <sup>[1]</sup>

Put *AB* onto x-axis and *C* onto y-axis and set coordinates as *A*(-*a*, 0), *B*(*b*,0), *C*(0,*c*), where *a*, *b* and *c* are positive numbers, then we get all vertices and centers:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A(-a,0)\\B(b,0)\\C(0,c)\\H(0,ab/c)\\N((b-a)/4,(c^2+ab)/4c)\\G((b-a)/3,c/3)\\O((b-a)/2,(c^2-ab)/2c)\end{cases}">

So it's easy to prove that *HNGO* are collinear and *HN* = *NO* and *HG* = 2*GO*.

### Feuerbach's theorem

<img src="diagrams/feuerbach.png">

**Feuerbach's theorem** states that the nine-point circle is tangent to the three excircles of the triangle as well as its incircle.

Put *AB* onto x-axis and *C* onto y-axis again:

- The nine-point circle passes through three midpoints *M*<sub>A</sub>, *M*<sub>B</sub>, and *M*<sub>C</sub>;
- The incircle passes through *D*, *E* and *F*, where *AE* = *AF*, *BD* = *BF* and *CD* = *CE*;
- One excircle passes through *G*, *H* and *K*, where *AH* = *AK*, *BG* = *BK* and *CH* = *CG*.

So we can get the equations of these three circles. Take the nine-point circle and the incircle as example, denote their equations as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x^2+y^2+d_\text{N}x+e_\text{N}y+f_\text{N}=0\\x^2+y^2+d_\text{I}x+e_\text{I}y+f_\text{I}=0\end{cases}">

Eliminate *y* or *x* in either of the two equations by the radical line <img src="https://latex.codecogs.com/gif.latex?(d_\text{N}-d_\text{I})x+(e_\text{N}-e_\text{I})y+(f_\text{N}-f_\text{I})=0">, then we get a quadratic equation about *x* or *y*.

Because we need to prove these two circles are tangent (i.e. they have only one common point), the remaining work is just checking if the discriminant of the quadratic equation is zero.

[Here](pythagoras/feuerbach.py) is the proof process.

Another approach is to calculate radii and distance:

- The incircle is inside and internally tangent to the nine-point circle if and only if <img src="https://latex.codecogs.com/gif.latex?|NI|=r_\text{N}-r_\text{I}">;
- One excircle is externally tangent to the nine-point circle if and only if <img src="https://latex.codecogs.com/gif.latex?|NE|=r_\text{N}+r_\text{E}">.

Because all of |*NI*|, *r*<sub>N</sub>, *r*<sub>I</sub> and *r*<sub>E</sub> contain square roots, which are too difficult to calculate, we need to rewrite them to simplify calculation:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}(r_N^2+r_I^2-|NI|^2)^2=4r_N^2r_I^2\\(r_N^2+r_E^2-|NE|^2)^2=4r_N^2r_E^2\end{cases}"> 

Neither of the two approaches can tell us whether two circles are internally or externally tangent. However, the incircle is obviously inside and internally tangent to the nine-point circle, because the incircle is inside the triangle and the nine-point circle intersects all three edges; each excircle is abviously externally tangent to the nine-point circle, because each excircle is outside of the triangle.

Other proofs can be found [here](https://imomath.com/index.php?options=323) (Problem 7) and [here](https://www.cut-the-knot.org/Curriculum/Geometry/FeuerbachProof.shtml).

### Note

1. We use the diagram from [here](https://en.wikipedia.org/wiki/Euler_line).