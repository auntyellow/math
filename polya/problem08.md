Note to Problem 20 in *How to Solve It*:

> ... the "average width" of the cube, which is, in fact, 3/2 = 1.5

Let's calculate the average radius (have of width) of one of the symmetric 1/48 parts of the cube:

<img src="problem08.png">

Let's set the radius of the inscribed sphere is 1, then this part of the cube is a tetrahedren with these planes:

- OAB: *y* = 0
- OAC: *x* = *y*
- OBC: *x* = *z*
- ABC: *z* = 1

We use spherical coordinates

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x=r\cos\phi\sin\theta\\y=r\sin\phi\sin\theta\\z=r\cos\theta\end{cases}">

to integral the average radius:

<img src="https://latex.codecogs.com/gif.latex?r_{Avg}=\frac{1}{\4\pi}\int_\Omega%20rd\Omega=\frac{1}{\4\pi}\int_\phi\int_\theta%20r\sin\theta%20d\theta%20d\phi">