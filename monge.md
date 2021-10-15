Radical center and Monge's theorem can be easily proved by Euclidean geometry. However, here we use coordinate approach to cover these cases:

- The intersections of two circles may be imaginary points, but there exists a straight line passing through them.
- The tangent lines to two circles may be imaginary lines, but there intersection point is real.

### Radical line

The radical line of two circles can be defined as the straight line passing through their intersections, whatever the two circles intersect or not. This is because any two circles can be denoted as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x^2+y^2+ax+by+c=0\\x^2+y^2+dx+ey+f=0\end{cases}">

Whatever the two roots are real or imaginary, we can always get a straight line by subtracting above two equations:

<img src="https://latex.codecogs.com/gif.latex?(a-d)x+(b-e)y+(c-f)=0">

such that the two roots are on this line.

### Radical center

<img src="diagrams/radical-center.gif">

The radical lines of three circles are concurrent at a point called **radical center** or **power center**. <sup>[1]</sup>

Let's denote these three circles as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}Q_1:x^2+y^2+ax+by+c=0\\Q_2:x^2+y^2+dx+ey+f=0\\Q_3:x^2+y^2+gx+hy+j=0\end{cases}">

Then the three radical lines are:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}q_2q_3:(d-g)x+(e-h)y+(f-j)=0\\q_3q_1:(g-a)x+(h-b)y+(j-c)=0\\q_1q_2:(a-d)x+(b-e)y+(c-f)=0\end{cases}">

They are obviously concurrent because their determinant of coefficients is zero:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}d-g&e-h&f-j\\g-a&h-b&j-c\\a-d&b-e&c-f\end{matrix}\right]=0">

### Tangent lines to two circles

Let's put centers of two circles onto y-axis, then any two circles can be denoted as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x^2+(y-a)^2=b^2\\x^2+(y-c)^2=d^2\end{cases}">

A pair of tangent lines can be denoted as <img src="https://latex.codecogs.com/gif.latex?y=h\pm{kx}">

### Monge's theorem

<img src="diagrams/monge.png">

**Monge's theorem** states that for any three circles in a plane, the intersection points of each of the three pairs of external tangent lines are collinear. This still holds even if one circle is completely inside another.

### Notes

1. We use the diagram from [here](https://mathworld.wolfram.com/RadicalCenter.html).