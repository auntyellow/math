### Intersection of tangent planes

> A sphere with center on the plane of the face *ABC* of a tetrahedron *SABC* passes through *A*, *B* and *C*, and meets the edges *SA*, *SB*, *SC* again at *A*<sub>1</sub>, *B*<sub>1</sub>, *C*<sub>1</sub>, respectively. The planes through *A*<sub>1</sub>, *B*<sub>1</sub>, *C*<sub>1</sub> tangent to the sphere meet at a point *O*. Prove that *O* is the circumcenter of the tetrahedron *SA*<sub>1</sub>*B*<sub>1</sub>*C*<sub>1</sub>. <sup>[1]</sup>

Of course we can define the sphere as <img src="https://latex.codecogs.com/gif.latex?x^2+y^2+z^2=r^2">, then pick arbitrary points *A*, *B* and *C* on the equator circle like <img src="https://latex.codecogs.com/gif.latex?A(r,0,0)">, <img src="https://latex.codecogs.com/gif.latex?B(b,\sqrt{r^2-b^2},0)"> and <img src="https://latex.codecogs.com/gif.latex?C(c,\sqrt{r^2-c^2},0)">. However, this will cause many radical calculations later.

So firstly, we define arbitrary points *A*, *B* and *C* on plane *xy* as <img src="https://latex.codecogs.com/gif.latex?A(a,0,0)">, <img src="https://latex.codecogs.com/gif.latex?B(0,b,0)"> and <img src="https://latex.codecogs.com/gif.latex?C(c,0,0)">, then calculate the sphere with equator on plane *xy*:

<img src="https://latex.codecogs.com/gif.latex?x^2+y^2+z^2+gx+hy+k=0\quad\text{(Eq.\,1)}">

Because the sphere passes through *A*, *B* and *C*, parameters *g*, *h* and *k* can be solved by:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{A}g+y_\text{A}h+k=-x_\text{A}^2-y_\text{A}^2-z_\text{A}^2\\x_\text{B}g+y_\text{B}h+k=-x_\text{B}^2-y_\text{B}^2-z_\text{B}^2\\x_\text{C}g+y_\text{C}h+k=-x_\text{C}^2-y_\text{C}^2-z_\text{C}^2\end{cases}">

Next, given an arbitrary point *S*(*d*, *e*, *f*), we have straight line *SA*:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x=x_\text{A}+(x_\text{S}-x_\text{A})t\\y=y_\text{A}+(y_\text{S}-y_\text{A})t\\z=z_\text{A}+(z_\text{S}-z_\text{A})t\end{cases}">

Apply on Eq. 1 then we get a quadratic equation about *t*. Because *t*<sub>0</sub> = 0 is the point *A*, we can reduce the order and get another root *t*<sub>1</sub> for point *A*<sub>1</sub>. Analogously, we can calculate points *B*<sub>1</sub> and *C*<sub>1</sub>.

Now the sphere Eq. 1 and three points *A*<sub>1</sub>, *B*<sub>1</sub> and *C*<sub>1</sub> are all rational expressions about *a*, *b*, *c*, *d*, *e* and *f*. We can convert them to homogeneous coordinates (then all expressions are polynomial) to speed up calculation.

When a quadric surface is denoted as <img src="https://latex.codecogs.com/gif.latex?ax^2+2bxy+cy^2+2dxz+2eyz+fz^2+2gxw+2hyw+2jzw+kw^2=0">, the tangent plane passing through a point <img src="https://latex.codecogs.com/gif.latex?(x_0,y_0,z_0,w_0)"> on the surface is:

<img src="https://latex.codecogs.com/gif.latex?{[ax_0+by_0+dz_0+gw_0,bx_0+cy_0+ez_0+hw_0,dx_0+ey_0+fz_0+jw_0,gx_0+hy_0+jz_0+kw_0]}">

Then it's easy to calculate the intersection *O* of the three tangent planes, and calculate the distance to *S*, *A*<sub>1</sub>, *B*<sub>1</sub> and *C*<sub>1</sub>.

[Here](pythagoras/sphere-12.py) is the computational proof.

### Eight vertices of a hexahedron lie on a sphere

> If seven vertices of a (quadrilaterally-faced) hexahedron lie on a sphere, then so does the eighth vertex. <sup>[2]</sup>

[Proof](pythagoras/sphere-11.py)

### Note

1. https://imomath.com/index.php?options=323, Problem 12
2. https://imomath.com/index.php?options=323, Problem 11