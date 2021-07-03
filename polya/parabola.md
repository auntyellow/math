The problem is in section **Definition** in *How to Solve It*:

> Construct the point of intersection of a given straight line and a parabola which the focus and the directrix are given.

This is a [Straightedge and Compass Construction](https://en.wikipedia.org/wiki/Straightedge_and_compass_construction) problem. Although it is impossible to construct a parabola by straightedge and compass, the points of intersection can be found:

> Construct a point *P* on the given straight line *c* at equal distances from the given point *F* and the given straight line *d*.

However, the solution is not given in this book. I'd like to give an analytic geometry solution, which can be converted to straightedge and compass construction.

<img src=parabola.png>

We put *F* onto the origin of Cartesian coordinates, then get equations for *P*(*x*,*y*):

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}y=b-x\tan\alpha\\y+p=\sqrt{x^2+y^2}\end{cases}">

The solution is:

<img src="https://latex.codecogs.com/gif.latex?x=-p\tan\alpha\pm\sqrt{p(p/\cos^{2}\alpha+2b)}">

Here let <img src="https://latex.codecogs.com/gif.latex?q=p/\cos^{2}\alpha+2b">, then <img src="https://latex.codecogs.com/gif.latex?\sqrt{pq}"> can be constructed by [Geometric Mean Theorem](https://en.wikipedia.org/wiki/Geometric_mean_theorem).

Constructions without analytic geometry can be found [here](https://math.stackexchange.com/questions/793125).