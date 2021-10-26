<img src="diagrams/euler-line.png">

**Euler line** is a line passing through <span style="color:blue">orthocenter *H*</span>, <span style="color:red">nine-point center *N*</span>, <span style="color:orange">centroid *G*</span> and <span style="color:green">circumcenter *O*</span>, while *HN* = *NO* and *HG* = 2*GO*. <sup>[1]</sup>

Put *AB* onto x-axis and *C* onto y-axis and set coordinates as *A*(-*a*, 0), *B*(*b*,0), *C*(0,*c*), where *a*, *b* and *c* are positive numbers, then we get all vertices and centers:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A:(-a,0)\\B:(b,0)\\C:(0,c)\\H:(0,\frac{ab}c)\\N:(\frac{b-a}4,\frac{c^2+ab}{4c})\\G:(\frac{b-a}3,\frac{c}3)\\O:(\frac{b-a}2,\frac{c^2-ab}{2c})\end{cases}">

So it's easy to prove that *HNGO* are collinear and *HN* = *NO* and *HG* = 2*GO*.

The incenter, however, doesn't lie on the Euler line, unless the triangle is isosceles. We have:

**Theorem 1** A triangle is isosceles if its incenter lies on its Euler line.

The proof (incenter lies on Euler line → isosceles) is not as easy as above because we should prove *AB* = *AC* or *AB* = *BC* or *AC* = *BC*, and exclude other possibilities.

Let's pick the centroid *G*, the orthocenter *H* (they are simpler than *N* and *O*) and the incenter *I*. The task is to proof that the determinant of collinearity has a form like:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}x_\text{G}&y_\text{G}&1\\x_\text{H}&y_\text{H}&1\\x_\text{I}&y_\text{I}&1\end{matrix}\right]=D{\cdot}E{\cdot}F">

where *D* = 0 iff *AB* = *AC*, *E* = 0 iff *AB* = *BC*, and *F* = 0 iff *AC* = *BC*.

If we choose above coordinates, the incenter will contain many square roots, which makes the determinant too difficult to be factored to *D*, *E* and *F*. So we have to run in a reverse way.

Given an incircle <img src="https://latex.codecogs.com/gif.latex?x^2+y^2-2ry=0"> and two vertices *A*(-*a*,0) and *B*(*b*,0) on x-axis, then the third vertex *C* can be determined by two edges:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}AC:x=ky-a\\BC:x=jx+b\end{cases}">

where AC and BC should be tangent to the incircle. Take the incircle and *AC* as example, eliminate *x* to get the quadratic equation about *y*, then we can solve *k* by setting discriminant to zero. The root *k* = 0 is edge *AB* and the non-zero root is edge *AC*. We use <img src="https://latex.codecogs.com/gif.latex?x=ky-a"> instead of <img src="https://latex.codecogs.com/gif.latex?y=k(x+a)"> because the latter cannot cover the case that *AC* is parallel to y-axis.

A more simple way is to draw a circle orthogonal to the incircle with center *A*, such that two intersections are tangent points on *AB* (the origin) and *AC*. And we can get *BC* in the same way.

Now we have three vertices and three centers:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A:(-a,0)\\B:(b,0)\\C:(\frac{(a-b)r^2}{ab-r^2},\frac{2abr}{ab-r^2})\\G:(\frac{b}3-\frac{a}3+\frac{(a-b)r^2}{3(ab-r^2)},\frac{2abr}{3(r^2-ab)})\\H:(\frac{(a-b)r^2}{ab-r^2},\frac{(a+r)(a-r)(b+r)(b-r)}{2r(ab-r^2)})\\I:(0,r)\end{cases}">

After some factoring work, we get the determinant of collinearity:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}x_\text{G}&y_\text{G}&1\\x_\text{H}&y_\text{H}&1\\x_\text{I}&y_\text{I}&1\end{matrix}\right]=\frac{(b-a)(ar^2+2br^2-ab^2)(2ar^2+br^2-a^2b)}{6r(ab-r^2)^2}=\frac{F{\cdot}D{\cdot}E}{6r(ab-r^2)^2}">

Obviously *F* = 0 iff *AC* = *BC*, but *D* and *E* are not obvious. So we should calculate the isosceles conditions:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}|AB|^2-|AC|^2=\frac{a(r^2-2ab-b^2)(ar^2+2br^2-ab^2)}{(ab-r^2)^2}=\frac{a(r^2-2ab-b^2)D}{(ab-r^2)^2}\\|AB|^2-|BC|^2=\frac{b(r^2-a^2-2ab)(2ar^2+br^2-a^2b)}{(ab-r^2)^2}=\frac{b(r^2-a^2-2ab)E}{(ab-r^2)^2}\\|AC|^2-|BC|^2=\frac{(a-b)(a+b)(ab+r^2)}{ab-r^2}=-\frac{(a+b)(ab+r^2)F}{ab-r^2}\end{cases}">

which follows *D* = 0 iff *AB* = *AC*, *E* = 0 iff *AB* = *BC*, and *F* = 0 iff *AC* = *BC*.

[Here](pythagoras/euler-line.py) is the computational proof process.

[Here](https://blancosilva.github.io/post/2013/07/09/an-automatic-geometric-proof.html) is another computational proof. More proofs can be found [here](https://math.stackexchange.com/questions/97471).

### Note

1. We use the diagram from [here](https://en.wikipedia.org/wiki/Euler_line).