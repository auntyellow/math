<img src="diagrams/desargues.png">

**Desargues's theorem** states: Two triangles (*A*<sub>1</sub>*B*<sub>1</sub>*C*<sub>1</sub> and *A*<sub>2</sub>*B*<sub>2</sub>*C*<sub>2</sub>) are in perspective axially (i.e. points *bc*, *ab* and *ac* are collinear) if and only if they are in perspective centrally (i.e. lines *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> are concurrent). <sup>[1]</sup>

### Collinear → Concurrent

Let's put points *ab*, *ac* and *bc* onto y-axis of Cartesian coordinates, and denote 6 lines of 2 triangles as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1B_1:y=gx+d\\A_2B_2:y=hx+d\\A_1C_1:y=jx+e\\A_2C_2:y=kx+e\\B_1C_1:y=mx+f\\B_2C_2:y=nx+f\end{cases}">

Then we get 6 vertices:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{A1}=(e-d)/(g-j)\\y_\text{A1}=(eg-dj)/(g-j)\\x_\text{A2}=(e-d)/(h-k)\\y_\text{A2}=(eh-dk)/(h-k)\\x_\text{B1}=(f-d)/(g-m)\\y_\text{B1}=(fg-dm)/(g-m)\\x_\text{B2}=(f-d)/(h-n)\\y_\text{B2}=(fh-dn)/(h-n)\\x_\text{C1}=(f-e)/(j-m)\\y_\text{C1}=(fj-em)/(j-m)\\x_\text{C2}=(f-e)/(k-n)\\y_\text{C2}=(fk-en)/(k-n)\end{cases}">

Then we denote lines *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1A_2:(x-x_\text{A1})(y_\text{A1}-y_\text{A2})=(x_\text{A1}-x_\text{A2})(y-y_\text{A1})\\B_1B_2:(x-x_\text{B1})(y_\text{B1}-y_\text{B2})=(x_\text{B1}-x_\text{B2})(y-y_\text{B1})\\C_1C_2:(x-x_\text{C1})(y_\text{C1}-y_\text{C2})=(x_\text{C1}-x_\text{C2})(y-y_\text{C1})\end{cases}">

Finally, we get *A*<sub>1</sub>*A*<sub>2</sub> ∩ *B*<sub>1</sub>*B*<sub>2</sub>:

<img src="https://latex.codecogs.com/gif.latex?x=\frac{dj-dk-dm+dn-eg+eh+em-en+fg-fh-fj+fk}{gk-gn-hj+hm+jn-km}">

<img src="https://latex.codecogs.com/gif.latex?y=\frac{djn-dkm-egn+ehm+fgk-fhj}{gk-gn-hj+hm+jn-km}">

The results are the same for *A*<sub>1</sub>*A*<sub>2</sub> ∩ *C*<sub>1</sub>*C*<sub>2</sub> and *B*<sub>1</sub>*B*<sub>2</sub> ∩ *C*<sub>1</sub>*C*<sub>2</sub>, which means *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> are concurrent. <sup>[2]</sup>

### Concurrent → Collinear

Let's put concurrent point *O* onto the origin of Cartesian coordinates, and denote lines *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1A_2:y=dx\\B_1B_2:y=ex\\C_1C_2:y=fx\end{cases}">

and 6 vertices are:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1:(g,dg)\\A_2:(h,dh)\\B_1:(j,ej)\\B_2:(k,ek)\\C_1:(m,fm)\\C_2:(n,fn)\end{cases}">

Then we denote 6 lines of 2 triangles as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1B_1:(x-g)(dg-ej)=(g-j)(y-dg)\\A_1C_1:(x-g)(dg-fm)=(g-m)(y-dg)\\B_1C_1:(x-j)(ej-fm)=(j-m)(y-ej)\\A_2B_2:(x-h)(dh-ek)=(h-k)(y-dh)\\A_2C_2:(x-h)(dh-fn)=(h-n)(y-dh)\\B_2C_2:(x-k)(ek-fn)=(k-n)(y-ek)\end{cases}">

Finally, we get *ab*, *ac* and *bc*:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{ab}=(-ghj+ghk+gjk-hjk)/(gk-hj)\\y_\text{ab}=(-dghj+dghk+egjk-ehjk)/(gk-hj)\\x_\text{ac}=(-ghm+ghn+gmn-hmn)/(gn-hm)\\y_\text{ac}=(-dghm+dghn+fgmn-fhmn)/(gn-hm)\\x_\text{bc}=(-jkm+jkn+jmn-kmn)/(jn-km)\\y_\text{bc}=(-ejkm+ejkn+fjmn-fkmn)/(jn-km)\end{cases}">

which are collinear, i.e. <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?x_\text{ab}y_\text{ac}+x_\text{ac}y_\text{bc}+x_\text{bc}y_\text{ab}=x_\text{ac}y_\text{ab}+x_\text{bc}y_\text{ac}+x_\text{ab}y_\text{bc}">

### Notes

1\. Here we use the diagram from [Cut the Knot](https://www.cut-the-knot.org/Curriculum/Geometry/Desargues.shtml).

2\. These complicated results can be solved by SymPy:

```python
from sympy import *

d, e, f, g, h, j, k, m, n, x, y = symbols('d, e, f, g, h, j, k, m, n, x, y')
xy = x, y
A1B1 = Eq(y, g * x + d)
A2B2 = Eq(y, h * x + d)
A1C1 = Eq(y, j * x + e)
A2C2 = Eq(y, k * x + e)
B1C1 = Eq(y, m * x + f)
B2C2 = Eq(y, n * x + f)
A1 = solve([A1B1, A1C1], xy)
A2 = solve([A2B2, A2C2], xy)
B1 = solve([A1B1, B1C1], xy)
B2 = solve([A2B2, B2C2], xy)
C1 = solve([A1C1, B1C1], xy)
C2 = solve([A2C2, B2C2], xy)
print("A1:", A1)
print("A2:", A2)
print("B1:", B1)
print("B2:", B2)
print("C1:", C1)
print("C2:", C2)
A1A2 = Eq((x - A1[x]) * (A1[y] - A2[y]), (A1[x] - A2[x]) * (y - A1[y]))
B1B2 = Eq((x - B1[x]) * (B1[y] - B2[y]), (B1[x] - B2[x]) * (y - B1[y]))
C1C2 = Eq((x - C1[x]) * (C1[y] - C2[y]), (C1[x] - C2[x]) * (y - C1[y]))
print(solve([A1A2, B1B2], xy))
print(solve([A1A2, C1C2], xy))
print(solve([B1B2, C1C2], xy))
```

3\. This complicated result can be solved by SymPy:

```python
from sympy import *

d, e, f, g, h, j, k, m, n, x, y = symbols('d, e, f, g, h, j, k, m, n, x, y')
xy = x, y
A1B1 = Eq((x - g) * (d * g - e * j), (g - j) * (y - d * g))
A1C1 = Eq((x - g) * (d * g - f * m), (g - m) * (y - d * g))
B1C1 = Eq((x - j) * (e * j - f * m), (j - m) * (y - e * j))
A2B2 = Eq((x - h) * (d * h - e * k), (h - k) * (y - d * h))
A2C2 = Eq((x - h) * (d * h - f * n), (h - n) * (y - d * h))
B2C2 = Eq((x - k) * (e * k - f * n), (k - n) * (y - e * k))
ab = solve([A1B1, A2B2], xy)
ac = solve([A1C1, A2C2], xy)
bc = solve([B1C1, B2C2], xy)
print("ab:", ab)
print("ac:", ac)
print("bc:", bc)
print(simplify(ab[x] * ac[y] + ac[x] * bc[y] + bc[x] * ab[y] - ac[x] * ab[y] - bc[x] * ac[y] - ab[x] * bc[y]))
```