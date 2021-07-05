The problem is in section **Auxiliary Elements** in *How to Solve It*:

> Construct a triangle, being given one angle, the altitude drawn from the vertex of the given angle, and the perimeter of the triangle.

<img src="triangle.png">

The equations are:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x+y+z=p\\x^2=y^2+z^2-2yz\cos%20A\\xh=yz\sin%20A\end{cases}">

Replace with *u*<sup>2</sup> = *yz* (here we use *u*<sup>2</sup> to ensure all variables have the same dimension) and *v* = *y* + *z*, then the equations can be simplified to:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}(p-v)^2=(v^2-2u^2)-2u^2\cos%20A\\(p-v)h=u^2\sin%20A\end{cases}">

The solutions are:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}u=\sqrt{h\cdot%20p^2/2(h+h\cos%20A+p\sin%20A)}\\v=p-u^2\sin%20A/h\end{cases}">

Here let *q* = 2(*h* + *h* cos *A* + *p* sin *A*), then *r* = *p*<sup>2</sup> / *q* can be constructed by [Intercept Theorem](https://en.wikipedia.org/wiki/Intercept_theorem), and <img src="https://latex.codecogs.com/gif.latex?u=\sqrt{h\cdot%20r}"> can be constructed by [Geometric Mean Theorem](https://en.wikipedia.org/wiki/Geometric_mean_theorem). Finally, we have:

<img src="https://latex.codecogs.com/gif.latex?y,z=\frac{v\pm\sqrt{(v+2u)(v-2u)}}2">

### Test Cases

Case 1: Problem 15 in *How to Solve It*: *h* = 12 and *p* = 60, then *x* = 25, *y* = 20 and *z* = 15 (or *y* = 15 and *z* = 20).

Case 2: If

<img src="https://latex.codecogs.com/gif.latex?\frac{p}h=\frac{2(1+\sin\frac{A}2)}{\cos\frac{A}2}">

then we get an isosceles triangle:

<img src="https://latex.codecogs.com/gif.latex?y=z=\frac{h}{\cos\frac{A}2}">