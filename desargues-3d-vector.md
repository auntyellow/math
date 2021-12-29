Homogeneous coordinates can be denoted as 3D vectors. The line passing through two points, or the intersection point of two lines, can be determined by [Cross Product](https://en.wikipedia.org/wiki/Cross_product). The collinearity and concurrency can be determined by [Triple Product](https://en.wikipedia.org/wiki/Triple_product).

### 3D vector proof of Desargues's theorem

Denote points *O*, *A*<sub>1</sub>, *B*<sub>1</sub>, *C*<sub>1</sub> as **O**, **A**<sub>1</sub>, **B**<sub>1</sub>, **C**<sub>1</sub>, then we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{A_2}=p\mathbf{O}+q\mathbf{A_1}\\\mathbf{B_2}=r\mathbf{O}+s\mathbf{B_1}\\\mathbf{C_2}=t\mathbf{O}+u\mathbf{C_1}\end{cases}">

And we denote intersection *ab* as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?{\mathbf{G}=(\mathbf{A_1}\times\mathbf{B_1})\times(\mathbf{A_2}\times\mathbf{B_2})=[(\mathbf{A_1}\times\mathbf{B_1})\cdot\mathbf{B_2}]\mathbf{A_2}-[(\mathbf{A_1}\times\mathbf{B_1})\cdot\mathbf{A_2}]\mathbf{B_2}=\dots=[(\mathbf{A_1}\times\mathbf{B_1})\cdot\mathbf{O}](qr\mathbf{A_1}-ps\mathbf{B_1})}">

Analogously, we have *ac*:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{H}=[(\mathbf{C_1}\times\mathbf{A_1})\cdot\mathbf{O}](pu\mathbf{C_1}-qt\mathbf{A_1})">

and *bc*:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J}=[(\mathbf{B_1}\times\mathbf{C_1})\cdot\mathbf{O}](st\mathbf{B_1}-ru\mathbf{C_1})">

Note that triple products in **G**, **H** and **I** are scalars, so we can simplify them as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}a=(\mathbf{B_1}\times\mathbf{C_1})\cdot\mathbf{O}\\b=(\mathbf{C_1}\times\mathbf{A_1})\cdot\mathbf{O}\\c=(\mathbf{A_1}\times\mathbf{B_1})\cdot\mathbf{O}\end{cases}">

Then we get:

<img src="https://latex.codecogs.com/gif.latex?{\mathbf{H}\times\mathbf{J}=ab(pu\mathbf{C_1}-qt\mathbf{A_1})\times(st\mathbf{B_1}-ru\mathbf{C_1})=ab(pstu\mathbf{C_1}\times\mathbf{B_1}-qst^2\mathbf{A_1}\times\mathbf{B_1}+qrtu\mathbf{A_1}\times\mathbf{C_1})}">

by using <img src="https://latex.codecogs.com/gif.latex?\mathbf{C_1}\times\mathbf{C_1}=0">.

Finally, by using <img src="https://latex.codecogs.com/gif.latex?\mathbf{A_1}\cdot(\mathbf{A_1}\times\mathbf{B_1})=0">, <img src="https://latex.codecogs.com/gif.latex?\mathbf{B_1}\cdot(\mathbf{A_1}\times\mathbf{B_1})=0"> and <img src="https://latex.codecogs.com/gif.latex?\mathbf{A_1}\cdot(\mathbf{C_1}\times\mathbf{B_1})=\mathbf{B_1}\cdot(\mathbf{A_1}\times\mathbf{C_1})">, we get:

<img src="https://latex.codecogs.com/gif.latex?\begin{array}{l}\mathbf{G}\cdot(\mathbf{H}\times\mathbf{J})=abc(qr\mathbf{A_1}-ps\mathbf{B_1})\cdot(pstu\mathbf{C_1}\times\mathbf{B_1}-qst^2\mathbf{A_1}\times\mathbf{B_1}+qrtu\mathbf{A_1}\times\mathbf{C_1})=\\abc[pqrstu\mathbf{A_1}\cdot(\mathbf{C_1}\times\mathbf{B_1})-pqrstu\mathbf{B_1}\cdot(\mathbf{A_1}\times\mathbf{C_1})]=0\end{array}">

which means *ab*, *ac* and *bc* are collinear.

### 3D vector proof of Pappus's Theorem

Given 4 arbitrary points **A**, **B**, **C** and **D**, from which no three points are collinear, we can denote D as:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{D}=\mathbf{A}+p\mathbf{B}+q\mathbf{C}">

**E** is collinear with **A** and **C**:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{E}=\mathbf{A}+r\mathbf{C}">

**F** is collinear with **B** and **D**:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F}=s\mathbf{B}+\mathbf{D}=\mathbf{A}+(p+s)\mathbf{B}+q\mathbf{C}">

Now let's calculate **G**:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{G}={(\mathbf{A}\times\mathbf{B})\times(\mathbf{D}\times\mathbf{E})=[(\mathbf{A}\times\mathbf{B})\cdot\mathbf{E}]\mathbf{D}-[(\mathbf{A}\times\mathbf{B})\cdot\mathbf{D}]\mathbf{E}=\left[(\mathbf{A}\times\mathbf{B})\cdot\mathbf{C}\right](r\mathbf{D}-q\mathbf{E})}">

And denote the triple product as <img src="https://latex.codecogs.com/gif.latex?t=(\mathbf{A}\times\mathbf{B})\cdot\mathbf{C}">:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{G}=t(r\mathbf{D}-q\mathbf{E})=t[(r-q)\mathbf{A}+pr\mathbf{B}]">

Analogously, we have:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{H}=(\mathbf{B}\times\mathbf{C})\times(\mathbf{E}\times\mathbf{F})=\dots=-t[(p+s)\mathbf{B}+(q-r)\mathbf{C}]">

and

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J}=(\mathbf{C}\times\mathbf{D})\times(\mathbf{F}\times\mathbf{A})=\dots=-t[(p+s)\mathbf{A}+p(p+s)\mathbf{B}+pq\mathbf{C}]">

Then we get:

<img src="https://latex.codecogs.com/gif.latex?{\mathbf{H}\times\mathbf{J}=t^2[(p+s)^2\mathbf{B}\times\mathbf{A}+pr(p+s)\mathbf{B}\times\mathbf{C}+(p+s)(q-r)\mathbf{C}\times\mathbf{A}]">

Finally, we get:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{G}\cdot(\mathbf{H}\times\mathbf{J})=t^3[pr(p+s)(r-q)\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})+pr(p+s)(q-r)\mathbf{B}\cdot(\mathbf{C}\times\mathbf{A})]=0">

which means **G**, **H** and **J** are collinear.

### Note

1. Here we should use some [vector formulas](diagrams/vector-formulas.png) (copied from the first page in John David Jackson's *Classical Electrodynamics*).