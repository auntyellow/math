The problem is in section **Definition** in *How to Solve It*:

> Construct the point of intersection of a given straight line and a parabola which the focus and the directrix are given.

This is a [Straightedge and Compass Construction](https://en.wikipedia.org/wiki/Straightedge_and_compass_construction) problem. Although it is impossible to construct a parabola by straightedge and compass, the points of intersection can be found:

> Construct a point *P* on the given straight line *c* at equal distances from the given point *F* and the given straight line *d*.

However, the solution is not given in this book. I'd like to give a coordinate solution, which can be converted to straightedge and compass construction.

### Coordinate Solution

<img src="parabola.png">

We put *F* onto the origin of Cartesian coordinates, then get the equations for *P*(*x*,*y*):

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}y=b-x\tan\alpha\\y+p=\sqrt{x^2+y^2}\end{cases}">

The solutions are:

<img src="https://latex.codecogs.com/gif.latex?x=-p\tan\alpha\pm\sqrt{p(p/\cos^{2}\alpha+2b)}">

Here let <img src="https://latex.codecogs.com/gif.latex?q=p/\cos^{2}\alpha+2b">, then <img src="https://latex.codecogs.com/gif.latex?\sqrt{pq}"> can be constructed by [Geometric Mean Theorem](https://en.wikipedia.org/wiki/Geometric_mean_theorem).

#### Special Cases

There is only a tangent point if *q* = 0, and no intersection or tangent points if *q* < 0.

If *c* is a vertical line, then the equation for *P*(*x*,*y*) (*x* is the distance from *F* to *c*) is <img src="https://latex.codecogs.com/gif.latex?y+p=\sqrt{x^2+y^2}">. The solution is <img src="https://latex.codecogs.com/gif.latex?y=(x^2-p^2)/2p">.

### Synthetic Solutions

Synthetic solutions can be found [here](https://math.stackexchange.com/questions/793125).