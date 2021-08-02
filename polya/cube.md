Polya noted the solution for Problem 8 (Axes of a Cube) in *How to Solve It*:

> ... the "average width" of the cube, which is, in fact, 3/2 = 1.5

I guessed two definitions of the "average width":

### Diameter equivalent to an isovolumic sphere

According to the volume of cube and sphere:

<img src="https://latex.codecogs.com/gif.latex?a^3=V=\frac{4\pi%20r^3}{3}">

the solution is:

<img src="https://latex.codecogs.com/gif.latex?2r=\sqrt[3]{\frac{6}{\pi}}a\approx1.2407a">

### Integral over all directions

Here we use spherical coordinates:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x=r\cos\phi\sin\theta\\y=r\sin\phi\sin\theta\\z=r\cos\theta\end{cases}">

Then the average radius can be defined as:

<img src="https://latex.codecogs.com/gif.latex?r_\text{avg}=\frac{1}{4\pi}\int_\Omega%20rd\Omega=\frac{1}{4\pi}\int_\phi\int_\theta%20r\sin\theta%20d\theta%20d\phi">

Here let's choose a cube with edge length 2, centered at the origin, then calculate the average radius (half of width) of one of the symmetric 48 parts of the cube:

<img src="cube.png">

Then this part of the cube is a tetrahedron with 4 planes:

- OAB: *y* = 0, or *φ* = 0
- OAC: *x* = *y*, or *φ* = *π*/4
- OBC: *x* = *z*, or cos*φ* sin*θ* = cos*θ*
- ABC: *z* = 1, or *r* cos*θ* = 1

So we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\phi_\text{OAB}=0\\\phi_\text{OAC}=\pi/4\\\theta_\text{OA}=0\\\theta_\text{OBC}=\text{arccot}\cos\phi\\r_\text{ABC}=1/\cos\theta\end{cases}">

Because of the symmetry, we can just integrate the average radius of the tetrahedron:

<img src="https://latex.codecogs.com/gif.latex?r_\text{avg}=\frac{48}{\4\pi}\int_{\phi_\text{OAB}}^{\phi_\text{OAC}}\int_{\theta_\text{OA}}^{\theta_\text{OBC}}r_\text{ABC}\sin\theta%20d\theta%20d\phi=\frac{12}\pi\int_0^{\pi/4}\int_0^{\text{arccot}\cos\phi}\frac{\sin\theta}{\cos\theta}d\theta%20d\phi">

Let's calculate the integral:

<img src="https://latex.codecogs.com/gif.latex?\int_0^{\text{arccot}\cos\phi}\frac{\sin\theta}{\cos\theta}d\theta=-\ln\cos\theta\bigg\rvert_0^{\text{arccot}\cos\phi}=\ln\sqrt{\cos^2\phi+1}-\ln\cos\phi"> (0 ≤ *φ* ≤ *π*/4)

Although the antiderivative of this function doesn't look analytic, we can get the numeric solution:

<img src="https://latex.codecogs.com/gif.latex?r_\text{avg}=\frac{12}\pi\int_0^{\pi/4}(\ln\sqrt{\cos^2\phi+1}-\ln\cos\phi)d\phi\approx1.2214">

This is close to the isovolumic-sphere definition but far different from Polya's note.