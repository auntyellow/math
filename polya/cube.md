Note to Problem 20 in *How to Solve It*:

> ... the "average width" of the cube, which is, in fact, 3/2 = 1.5

If use spherical coordinates:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x=r\cos\phi\sin\theta\\y=r\sin\phi\sin\theta\\z=r\cos\theta\end{cases}">

the average radius can be defined as:

<img src="https://latex.codecogs.com/gif.latex?r_{Avg}=\frac{1}{\4\pi}\int_\Omega%20rd\Omega=\frac{1}{\4\pi}\int_\phi\int_\theta%20r\sin\theta%20d\theta%20d\phi">

Here let's choose a cube with edge length 2, centered at the origin, then calculate the average radius (half of width) of one of the symmetric 48 parts of the cube:

<img src="cube.png">

Then this part of the cube is a tetrahedren with 4 planes:

- OAB: *y* = 0, or *φ* = 0
- OAC: *x* = *y*, or *φ* = π / 4
- OBC: *x* = *z*, or cos*φ* sin*θ* = cos*θ*
- ABC: *z* = 1, or *r* cos*θ* = 1

So we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\phi_{OAB}=0\\\phi_{OAC}=\pi/4\\\theta_{OA}=0\\\theta_{OBC}=\text{arccot}\cos\phi\\r_{ABC}=1/\cos\theta\end{cases}">

Because of the symmetry, we can just integral the average radius of the tetrahedren:

<img src="https://latex.codecogs.com/gif.latex?r_{Avg}=\frac{48}{\4\pi}\int_{\phi_{OAB}}^{\phi_{OAC}}\int_{\theta_{OA}}^{\theta_{OBC}}r_{ABC}\sin\theta%20d\theta%20d\phi=\frac{12}{\pi}\int_0^{\pi/4}\int_0^{\text{arccot}\cos\phi}\frac{\sin\theta}{\cos\theta}d\theta%20d\phi">