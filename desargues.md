<img src="diagrams/desargues.png">

**Desargues's theorem** states: Two triangles (*A*<sub>1</sub>*B*<sub>1</sub>*C*<sub>1</sub> and *A*<sub>2</sub>*B*<sub>2</sub>*C*<sub>2</sub>) are in perspective axially (i.e. points *bc*, *ab* and *ac* are collinear) if and only if they are in perspective centrally (i.e. lines *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> are concurrent). <sup>[1]</sup>

### Collinear → Concurrent

Let's put points *ab*, *ac* and *bc* onto y-axis of Cartesian coordinates, and denote 6 lines of 2 triangles as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1B_1:y=gx+d\\A_2B_2:y=hx+d\\A_1C_1:y=jx+e\\A_2C_2:y=kx+e\\B_1C_1:y=mx+f\\B_2C_2:y=nx+f\end{cases}">

Then we get 6 vertices:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{A1}=(e-d)/(g-j)\\y_\text{A1}=(eg-dj)/(g-j)\\x_\text{A2}=(e-d)/(h-k)\\y_\text{A2}=(eh-dk)/(h-k)\\x_\text{B1}=(f-d)/(g-m)\\y_\text{B1}=(fg-dm)/(g-m)\\x_\text{B2}=(f-d)/(h-n)\\y_\text{B2}=(fh-dn)/(h-n)\\x_\text{C1}=(f-e)/(j-m)\\y_\text{C1}=(fj-em)/(j-m)\\x_\text{C2}=(f-e)/(k-n)\\y_\text{C2}=(fk-en)/(k-n)\end{cases}">

Then we denote lines *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1A_2:xy_\text{A1}+x_\text{A1}y_\text{A2}+x_\text{A2}y=x_\text{A1}y+x_\text{A2}y_\text{A1}+xy_\text{A2}\\B_1B_2:xy_\text{B1}+x_\text{B1}y_\text{B2}+x_\text{B2}y=x_\text{B1}y+x_\text{B2}y_\text{B1}+xy_\text{B2}\\C_1C_2:xy_\text{C1}+x_\text{C1}y_\text{C2}+x_\text{C2}y=x_\text{C1}y+x_\text{C2}y_\text{C1}+xy_\text{C2}\end{cases}">

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

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1B_1:x\cdot%20dg+g\cdot%20ej+j\cdot%20y=g\cdot%20y+j\cdot%20dg+x\cdot%20ej\\A_1C_1:x\cdot%20dg+g\cdot%20fm+m\cdot%20y=g\cdot%20y+m\cdot%20dg+x\cdot%20fm\\B_1C_1:x\cdot%20ej+j\cdot%20fm+m\cdot%20y=j\cdot%20y+m\cdot%20ej+x\cdot%20fm\\A_2B_2:x\cdot%20dh+h\cdot%20ek+k\cdot%20y=h\cdot%20y+k\cdot%20dh+x\cdot%20ek\\A_2C_2:x\cdot%20dh+h\cdot%20fn+n\cdot%20y=h\cdot%20y+n\cdot%20dh+x\cdot%20fn\\B_2C_2:x\cdot%20ek+k\cdot%20fn+n\cdot%20y=k\cdot%20y+n\cdot%20ek+x\cdot%20fn\end{cases}">

Finally, we get *ab*, *ac* and *bc*:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{ab}=(-ghj+ghk+gjk-hjk)/(gk-hj)\\y_\text{ab}=(-dghj+dghk+egjk-ehjk)/(gk-hj)\\x_\text{ac}=(-ghm+ghn+gmn-hmn)/(gn-hm)\\y_\text{ac}=(-dghm+dghn+fgmn-fhmn)/(gn-hm)\\x_\text{bc}=(-jkm+jkn+jmn-kmn)/(jn-km)\\y_\text{bc}=(-ejkm+ejkn+fjmn-fkmn)/(jn-km)\end{cases}">

which are collinear, i.e. <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?x_\text{ab}y_\text{ac}+x_\text{ac}y_\text{bc}+x_\text{bc}y_\text{ab}=x_\text{ac}y_\text{ab}+x_\text{bc}y_\text{ac}+x_\text{ab}y_\text{bc}">

### Notes

1. Here we use the diagram from [Cut the Knot](https://www.cut-the-knot.org/Curriculum/Geometry/Desargues.shtml).
2. These complicated results can be solved by SymPy [here](projective/desargues1.py).
3. This complicated result can be solved by SymPy [here](projective/desargues2.py).