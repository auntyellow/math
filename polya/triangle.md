The problem is in section **Auxiliary Elements** in *How to Solve It*:

> Construct a triangle, being given one angle, the altitude drawn from the vertex of the given angle, and the perimeter of the triangle.

<img src="triangle.png">

### Solution

The equations are:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x+y+z=p\\x^2=y^2+z^2-2yz\cos%20A\\xh=yz\sin%20A\end{cases}">

Replace with *u*<sup>2</sup> = *yz* and 2*v* = *y* + *z* (*u* and *v* are geometric and arithmetic mean of *y* and *z*), then the equations can be simplified to:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}(p-2v)^2=(4v^2-2u^2)-2u^2\cos%20A\\(p-2v)h=u^2\sin%20A\end{cases}">

The solutions are:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}u^2=h\cdot%20p^2/2(h+h\cos%20A+p\sin%20A)\\2v=p-u^2\sin%20A/h\end{cases}">

Here let *q* = 2(*h* + *h* cos *A* + *p* sin *A*), then *r* = *p*<sup>2</sup> / *q* can be constructed by [Intercept Theorem](https://en.wikipedia.org/wiki/Intercept_theorem), and <img src="https://latex.codecogs.com/gif.latex?u=\sqrt{h\cdot%20r}"> can be constructed by [Geometric Mean Theorem](https://en.wikipedia.org/wiki/Geometric_mean_theorem). Finally, we have:

<img src="https://latex.codecogs.com/gif.latex?y,z=v\pm\sqrt{v^2-u^2}">

### Verification

Here we use [SymPy](https://en.wikipedia.org/wiki/SymPy) to verify our result:

```python
from sympy import *

h, p, A = symbols("h p A")
u = sqrt(h * p * p / 2 / (h + h * cos(A) + p * sin(A)))
v = (p - u * u * sin(A) / h) / 2
y = v + sqrt(v * v - u * u)
z = v - sqrt(v * v - u * u)
x = y * z * sin(A) / h
print("x + y + z =", simplify(x + y + z))
x = sqrt(y * y + z * z - 2 * y * z * cos(A))
print("x + y + z =", simplify(x + y + z))
```

We get:

```
x + y + z = p
x + y + z = (-p**2*sin(A)/2 + (4*p + 2*sqrt(p**4*sin(A)**2/(h*cos(A) + h + p*sin(A))**2))*(h*cos(A) + h + p*sin(A))/4)/(h*cos(A) + h + p*sin(A))
```

The verification of <img src="https://latex.codecogs.com/gif.latex?xh=yz\sin%20A"> looks well.

However, the verification of <img src="https://latex.codecogs.com/gif.latex?x^2=y^2+z^2-2yz\cos%20A"> looks a bit complicated. So we should continue simplifying it:

```python
from sympy import *

h, p, A = symbols("h p A", positive=True)
xyz = (-p**2*sin(A)/2 + (4*p + 2*sqrt(p**4*sin(A)**2/(h*cos(A) + h + p*sin(A))**2))*(h*cos(A) + h + p*sin(A))/4)/(h*cos(A) + h + p*sin(A))
xyz = refine(xyz, Q.positive(sin(A)))
xyz = refine(xyz, Q.positive(h + h * cos(A) + p * sin(A)))
print("x + y + z =", simplify(xyz))
```

Finally we get `x + y + z = p`.

### Special Cases

If <img src="https://latex.codecogs.com/gif.latex?\frac{p}h=\frac{2(1+\sin\frac{A}2)}{\cos\frac{A}2}">, then we get an isosceles triangle <img src="https://latex.codecogs.com/gif.latex?y=z=\frac{h}{\cos\frac{A}2}">.

If <img src="https://latex.codecogs.com/gif.latex?\frac{p}h<\frac{2(1+\sin\frac{A}2)}{\cos\frac{A}2}">, then the triangle cannot be constructed.