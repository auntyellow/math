<img src="diagrams/brianchon.png">

**Brianchon's theorem** states that when a hexagon is circumscribed around a conic section, its principal diagonals (those connecting opposite vertices) meet in a single point. <sup>[1]</sup>

### The Proof

Let's put point *A*(*g*,0) onto positive x-axis, put points *C*(*h*,0) and *E*(*j*,0) onto y-axis, and donate the conic as:

<img src="https://latex.codecogs.com/gif.latex?ax^2+bxy+cy^2+dx+ey+f=0">

#### Step 1

To find a line <img src="https://latex.codecogs.com/gif.latex?y-y_\text{P}=k(x-x_\text{P})"> through a given point *P* tangent to a conic, the following equations should have a repeated root:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}ax^2+bxy+cy^2+dx+ey+f=0\\y=kx+m\end{cases}">

where <img src="https://latex.codecogs.com/gif.latex?m=y_\text{P}-kx_\text{P}">.

So the [discriminant](https://en.wikipedia.org/wiki/Quadratic_equation#Discriminant) of the quadratic equation (*y* is eliminated):

<img src="https://latex.codecogs.com/gif.latex?(a+bk+ck^2)x^2+(bm+2ckm+d+ek)x+(cm^2+em+f)=0">

should be 0, which means:

<img src="https://latex.codecogs.com/gif.latex?\Delta=(bm+2ckm+d+ek)^2-4(a+bk+ck^2)(cm^2+em+f)=0">

Then we solve *k*<sub>12</sub> and get 2 lines <img src="https://latex.codecogs.com/gif.latex?y-y_\text{P}=k_{12}(x-x_\text{P})">.

However, SymPy won't tell us whether the first root denotes the straight line in the left or right side. So we need to guess then verify by numerical evaluation.

Assume the conic is <img src="https://latex.codecogs.com/gif.latex?x^2+y^2-1=0"> and 3 points are *A*(5/4,0), *C*(0,5/4) and *E*(0,-5/4). We should get *AB* with negative *k* and *AF* with positive *k*. So we should use `AB, AF = solve(...)` but not `AF, AB = solve(...)`.

[Here](projective/brianchon1.py) we get 6 edges of the hexagon:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}AF:y=(2aeg-bdg-2bf+de+2RS)(x-g)/(4acg^2-b^2g^2-2beg+4cdg+4cf-e^2)\\AB:y=(2aeg-bdg-2bf+de-2RS)(x-g)/(4acg^2-b^2g^2-2beg+4cdg+4cf-e^2)\\BC:y=(-beh-2bf+2cdh+de+2PS)x/(4cf-e^2)+h\\CD:y=(-beh-2bf+2cdh+de-2PS)x/(4cf-e^2)+h\\DE:y=(-bej-2bf+2cdj+de+2QS)x/(4cf-e^2)+j\\EF:y=(-bej-2bf+2cdj+de-2QS)x/(4cf-e^2)+j\end{cases}">

where:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}P=\sqrt{ch^2+eh+f}\\Q=\sqrt{cj^2+ej+f}\\R=\sqrt{ag^2+dg+f}\\S=\sqrt{-4acf+ae^2+b^2f-bde+cd^2}\end{cases}">

If *S* is imaginary, we can flip all coefficients of the conic to guarantee a real *S*. Under this circumstance, imaginary *P*, *Q* or *R* means the tangent line doesn't exist. For example, imaginary *R* means *A* may be inside an ellipse.

### Notes

1. Here we use the diagram from [百度百科](https://baike.baidu.com/item/%E5%B8%83%E5%88%A9%E5%AE%89%E6%A1%91%E5%AE%9A%E7%90%86).