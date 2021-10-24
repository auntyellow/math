<img src="diagrams/euler-line.png">

**Euler line** is a line passing through othocenter *H* (blue), nine-point center *N* (red), centroid *G* (orange) and circumcenter *O* (green), while *HN* = *NO* and *HG* = 2*GO*. <sup>[1]</sup>

Put *AB* onto x-axis and *C* onto y-axis and set coordinates as *A*(-*a*, 0), *B*(*b*,0), *C*(0,*c*), where *a*, *b* and *c* are positive numbers, then we get all vertices and centers:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A:(-a,0)\\B:(b,0)\\C:(0,c)\\H:(0,\frac{ab}c)\\N:(\frac{b-a}4,\frac{c^2+ab}{4c})\\G:(\frac{b-a}3,\frac{c}3)\\O:(\frac{b-a}2,\frac{c^2-ab}{2c})\end{cases}">

So it's easy to prove that *HNGO* are collinear and *HN* = *NO* and *HG* = 2*GO*.

The incenter, however, doesn't lie on the Euler line, unless the triangle is isosceles. The proof (incenter lies on Euler line → isosceles) is not as easy as above because we should prove *AB* = *AC* or *AB* = *BC* or *AC* = *BC*, and exclude other possibilities.

Let's pick the centroid *G*, the othocenter *H* (they are simpler than *N* and *O*) and the incenter *I*. The task is to proof that the determinant of collinearity has a form like:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}x_\text{G}&y_\text{G}&1\\x_\text{H}&y_\text{H}&1\\x_\text{I}&y_\text{I}&1\end{matrix}\right]=D{\cdot}E{\cdot}F">

where *D* = 0 iff *AB* = *AC*, *E* = 0 iff *AB* = *BC*, and *F* = 0 iff *AC* = *BC*.

If we choose above coordinates, the incenter will contain many square roots, which makes the determinant too difficult to be factored to *D*, *E* and *F*. So we have to run in a reverse way.

Given an incircle <img src="https://latex.codecogs.com/gif.latex?x^2+y^2-2rx=0"> and two vertices *A*(0,*a*) and *B*(0,-*b*) on y-axis, then the third vertex *C* can be determined by two edges:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}AC:y=kx+a\\BC:y=jx-b\end{cases}">

where AC and BC should be tangent to the incircle. Take the incircle and *AC* as example, eliminate *y* to get the quadratic equation:

<img src="https://latex.codecogs.com/gif.latex?(k^2+1)x^2+(2ak-2r)x+a^2=0">

The discriminant should be zero:

<img src="https://latex.codecogs.com/gif.latex?\Delta=-a^2(k^2+1)+(ak-2r)^2=0">

We get <img src="https://latex.codecogs.com/gif.latex?k=r/2a-a/2r">. Analogously, <img src="https://latex.codecogs.com/gif.latex?j=b/2r-r/2b">.

Then we get three vertices and three centers:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A:(0,a)\\B:(0,-b)\\C:(\frac{2abr}{ab-r^2},\frac{(b-a)r^2}{ab-r^2})\\G:(\frac{2abr}{3(r^2-ab)},\frac{a}3-\frac{b}3+\frac{(b-a)r^2}{3(ab-r^2)})\\H:(\frac{(a+r)(a-r)(b+r)(b-r)}{2r(ab-r^2)},\frac{(b-a)r^2}{ab-r^2})\\I:(r,0)\end{cases}">

After some factoring work, the determinant of collinearity is:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}x_\text{G}&y_\text{G}&1\\x_\text{H}&y_\text{H}&1\\x_\text{I}&y_\text{I}&1\end{matrix}\right]=\frac{(b-a)(ar^2+2br^2-ab^2)(2ar^2+br^2-a^2b)}{6r(ab-r^2)^2}=\frac{F{\cdot}D{\cdot}E}{6r(ab-r^2)^2}">

Obviously *F* = 0 iff *AC* = *BC*, but *D* and *E* are not obvious. So we should calculate the isosceles conditions:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}|AB|^2-|AC|^2=\frac{a(r^2-2ab-b^2)(ar^2+2br^2-ab^2)}{(ab-r^2)^2}=\frac{a(r^2-2ab-b^2)D}{(ab-r^2)^2}\\|AB|^2-|BC|^2=\frac{b(r^2-a^2-2ab)(2ar^2+br^2-a^2b)}{(ab-r^2)^2}=\frac{b(r^2-a^2-2ab)E}{(ab-r^2)^2}\\|AC|^2-|BC|^2=\frac{(a-b)(a+b)(ab+r^2)}{ab-r^2}=-\frac{(a+b)(ab+r^2)F}{ab-r^2}\end{cases}">

which follows *D* = 0 iff *AB* = *AC*, *E* = 0 iff *AB* = *BC*, and *F* = 0 iff *AC* = *BC*.

[Here](pythagoras/euler-line.py) is the computational proof process.

[Here](https://blancosilva.github.io/post/2013/07/09/an-automatic-geometric-proof.html) is another computational proof. More proofs can be found [here](https://math.stackexchange.com/questions/97471).

### Note

1. We use the diagram from [here](https://en.wikipedia.org/wiki/Euler_line).