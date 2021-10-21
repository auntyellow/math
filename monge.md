Radical center and Monge's theorem can be easily proved by Euclidean geometry. However, here we use coordinate approach to cover these cases:

- The intersections of two circles may be imaginary points, but there exists a straight line passing through them.
- The tangent lines to two circles may be imaginary lines, but their intersection point is real.

### Radical line

The radical line of two circles can be defined as the straight line passing through their intersections, whatever the two circles intersect or not. This is because any two circles can be denoted as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x^2+y^2+ax+by+c=0\\x^2+y^2+dx+ey+f=0\end{cases}">

Whatever the two roots are real or imaginary, we can always get a straight line by subtracting above two equations:

<img src="https://latex.codecogs.com/gif.latex?(a-d)x+(b-e)y+(c-f)=0">

such that the two roots are on this line.

For example, one circle is inside another:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x^2+y^2=9\\x^2+(y+1)^2=1\end{cases}">

The two intersections are imaginary: <img src="https://latex.codecogs.com/gif.latex?(\pm{3}\sqrt{5}i/2,-9/2)">, but the straight line passing through them are real: <img src="https://latex.codecogs.com/gif.latex?y=-9/2">.

### Radical center

<img src="diagrams/radical-center.gif">

The radical lines of three circles are concurrent at a point called **radical center** or **power center**. <sup>[1]</sup>

Let's denote these three circles as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}Q_1:x^2+y^2+ax+by+c=0\\Q_2:x^2+y^2+dx+ey+f=0\\Q_3:x^2+y^2+gx+hy+j=0\end{cases}">

Then the three radical lines are:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}q_2q_3:(d-g)x+(e-h)y+(f-j)=0\\q_3q_1:(g-a)x+(h-b)y+(j-c)=0\\q_1q_2:(a-d)x+(b-e)y+(c-f)=0\end{cases}">

They are obviously concurrent because their determinant of coefficients is zero:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}d-g&e-h&f-j\\g-a&h-b&j-c\\a-d&b-e&c-f\end{matrix}\right]=0">

### Intersection of tangent lines to two circles

Here we are only interested in the intersection of two external tangent lines (later we call it *external intersection*) and the intersection of two internal ones (later we call it *internal intersection*), which means the intersection of an external one and an internal one is not considered.

Let's put two centers *A* and *B* onto y-axis, and denote these two circles as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x^2+(y-a)^2=R^2\\x^2+(y-b)^2=r^2\end{cases}\;(a>b,\,R\ge{r}>0)">

Because of the symmetry about y-axis, a pair of either external or internal tangent lines can be denoted as:

<img src="https://latex.codecogs.com/gif.latex?y=h\pm{kx}">

The intersection is (0, *h*), so we are only interested in *h* but not *k*.

When eliminating *y* with the first circle, we have:

<img src="https://latex.codecogs.com/gif.latex?x^2+(h\pm{kx}-a)^2=b^2">

which can be written as:

<img src="https://latex.codecogs.com/gif.latex?(k^2+1)x^2\pm{2}k(h-a)x+(h-a)^2-R^2=0">

Because a tangent line has only one common point with each circle, the discriminant should be zero, i.e.

<img src="https://latex.codecogs.com/gif.latex?\Delta=k^2(h-a)^2-(k^2+1)((h-a)^2-R^2)=0">

which can be written as:

<img src="https://latex.codecogs.com/gif.latex?(k^2+1)R^2=(h-a)^2">

Analogously, when tangent to the second circle, we have:

<img src="https://latex.codecogs.com/gif.latex?(k^2+1)r^2=(h-b)^2">

We get below equation by eliminating <img src="https://latex.codecogs.com/gif.latex?k^2+1">:

<img src="https://latex.codecogs.com/gif.latex?\frac{R}{r}=\pm\frac{h-a}{h-b}">

The first solution is:

<img src="https://latex.codecogs.com/gif.latex?h=\frac{Rb-ra}{R-r}=b-\frac{r(a-b)}{R-r}">

which is less than *b*, and should be infinity if *R* = *r* (two tangent lines parallel to y-axis). So it should be the external intersection. Denote it as *H*, then we have:

<img src="https://latex.codecogs.com/gif.latex?\frac{\overrightarrow{HA}}{\overrightarrow{HB}}=\frac{a-h}{b-h}=\frac{R}r\quad\text{(Eq.\,1)}">

The second solution is:

<img src="https://latex.codecogs.com/gif.latex?h'=\frac{ra+Rb}{r+R}">

which is between *a* and *b*. So it should be the internal intersection. Denote it as *H'*, then we have:

<img src="https://latex.codecogs.com/gif.latex?\frac{\overrightarrow{H'A}}{\overrightarrow{BH'}}=\frac{a-h'}{h'-b}=\frac{R}r\quad\text{(Eq.\,2)}">

For example, one circle is inside another:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x^2+y^2=9\\x^2+(y+1)^2=1\end{cases}">

The two external tangent lines are <img src="https://latex.codecogs.com/gif.latex?y=\pm\sqrt{3}ix/2-3/2"> (tangent points are <img src="https://latex.codecogs.com/gif.latex?(\pm{3}\sqrt{3}i,-6)"> and <img src="https://latex.codecogs.com/gif.latex?(\pm\sqrt{3}i,-3)">), and their intersection is <img src="https://latex.codecogs.com/gif.latex?(0,-3/2)">.

The two internal tangent lines are <img src="https://latex.codecogs.com/gif.latex?y=\pm\sqrt{15}ix/4-3/4"> (tangent points are <img src="https://latex.codecogs.com/gif.latex?(\pm{3}\sqrt{15}i,-12)"> and <img src="https://latex.codecogs.com/gif.latex?(\pm\sqrt{15}i,3)">), and their intersection is <img src="https://latex.codecogs.com/gif.latex?(0,-3/4)">.

### Monge's theorem

<img src="diagrams/monge.png">

**Monge's theorem** states that for any three circles in a plane, the intersection points of each of the three pairs of external tangent lines are collinear. This still holds even if one circle is completely inside another.

Let's apply Eq. 1 onto three external intersections *D*, *E* and *F*:

<img src="https://latex.codecogs.com/gif.latex?\frac{\overrightarrow{DA}}{\overrightarrow{DB}}\cdot\frac{\overrightarrow{EC}}{\overrightarrow{EA}}\cdot\frac{\overrightarrow{FB}}{\overrightarrow{FC}}=\frac{r_A}{r_B}\cdot\frac{r_C}{r_A}\cdot\frac{r_B}{r_C}=1">

According to Menelaus's theorem, *D*, *E* and *F* are collinear.

The three internal intersections *D'*, *E'* and *F'* have a similar property. Let's apply Eq. 2 onto them:

<img src="https://latex.codecogs.com/gif.latex?\frac{\overrightarrow{D'A}}{\overrightarrow{BD'}}\cdot\frac{\overrightarrow{E'C}}{\overrightarrow{AE'}}\cdot\frac{\overrightarrow{F'B}}{\overrightarrow{CF'}}=\frac{r_A}{r_B}\cdot\frac{r_C}{r_A}\cdot\frac{r_B}{r_C}=1">

According to Ceva's theorem, *CD'*, *BE'* and *AF'* are concurrent.

### Note

1. We use the diagram from [here](https://mathworld.wolfram.com/RadicalCenter.html).