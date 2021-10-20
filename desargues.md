<img src="diagrams/desargues.png">

**Desargues's theorem** states that two triangles (*A*<sub>1</sub>*B*<sub>1</sub>*C*<sub>1</sub> and *A*<sub>2</sub>*B*<sub>2</sub>*C*<sub>2</sub>) are in perspective axially (i.e. points *bc*, *ab* and *ac* are collinear) if and only if they are in perspective centrally (i.e. lines *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> are concurrent). <sup>[1]</sup>

## Proof by Cartesian coordinates

### Collinear → Concurrent

Let's put point *ab* onto the origin, put *ac* and *bc* onto y-axis, and denote 6 lines of 2 triangles as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1B_1:y=gx\\A_2B_2:y=hx\\A_1C_1:y=jx+e\\A_2C_2:y=kx+e\\B_1C_1:y=mx+f\\B_2C_2:y=nx+f\end{cases}">

Then we get 6 vertices:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{A1}=e/(g-j)\\y_\text{A1}=eg/(g-j)\\x_\text{A2}=e/(h-k)\\y_\text{A2}=eh/(h-k)\\x_\text{B1}=f/(g-m)\\y_\text{B1}=fg/(g-m)\\x_\text{B2}=f/(h-n)\\y_\text{B2}=fh/(h-n)\\x_\text{C1}=(f-e)/(j-m)\\y_\text{C1}=(fj-em)/(j-m)\\x_\text{C2}=(f-e)/(k-n)\\y_\text{C2}=(fk-en)/(k-n)\end{cases}">

Then we denote lines *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1A_2:(y_\text{A1}-y_\text{A2})x+(x_\text{A2}-x_\text{A1})y+(x_\text{A1}y_\text{A2}-x_\text{A2}y_\text{A1})=0\\B_1B_2:(y_\text{B1}-y_\text{B2})x+(x_\text{B2}-x_\text{B1})y+(x_\text{B1}y_\text{B2}-x_\text{B2}y_\text{B1})=0\\C_1C_2:(y_\text{C1}-y_\text{C2})x+(x_\text{C2}-x_\text{C1})y+(x_\text{C1}y_\text{C2}-x_\text{C2}y_\text{C1})=0\end{cases}">

Finally, we calculate the determinant of 9 coefficients of these 3 lines and get:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}y_\text{A1}-y_\text{A2}&x_\text{A2}-x_\text{A1}&x_\text{A1}y_\text{A2}-x_\text{A2}y_\text{A1}\\y_\text{B1}-y_\text{B2}&x_\text{B2}-x_\text{B1}&x_\text{B1}y_\text{B2}-x_\text{B2}y_\text{B1}\\y_\text{C1}-y_\text{C2}&x_\text{C2}-x_\text{C1}&x_\text{C1}y_\text{C2}-x_\text{C2}y_\text{C1}\end{matrix}\right]=0">

which means *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> are concurrent. □ <sup>[2]</sup>

### Concurrent → Collinear

Let's put concurrent point *O* onto the origin, put *A*<sub>1</sub>*A*<sub>2</sub> onto x-axis, and denote lines *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1A_2:y=0\\B_1B_2:y=ex\\C_1C_2:y=fx\end{cases}">

and 6 vertices are:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1:(g,0)\\A_2:(h,0)\\B_1:(j,ej)\\B_2:(k,ek)\\C_1:(m,fm)\\C_2:(n,fn)\end{cases}">

Then we denote 6 lines of 2 triangles as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_1B_1:g{\cdot}ej+j{\cdot}y=g{\cdot}y+x{\cdot}ej\\A_1C_1:g{\cdot}fm+m{\cdot}y=g{\cdot}y+x{\cdot}fm\\B_1C_1:x{\cdot}ej+j{\cdot}fm+m{\cdot}y=j{\cdot}y+m{\cdot}ej+x{\cdot}fm\\A_2B_2:h{\cdot}ek+k{\cdot}y=h{\cdot}y+x{\cdot}ek\\A_2C_2:h{\cdot}fn+n{\cdot}y=h{\cdot}y+x{\cdot}fn\\B_2C_2:x{\cdot}ek+k{\cdot}fn+n{\cdot}y=k{\cdot}y+n{\cdot}ek+x{\cdot}fn\end{cases}">

Finally, we get *ab*, *ac* and *bc*:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{ab}=(-ghj+ghk+gjk-hjk)/(gk-hj)\\y_\text{ab}=(egjk-ehjk)/(gk-hj)\\x_\text{ac}=(-ghm+ghn+gmn-hmn)/(gn-hm)\\y_\text{ac}=(fgmn-fhmn)/(gn-hm)\\x_\text{bc}=(-jkm+jkn+jmn-kmn)/(jn-km)\\y_\text{bc}=(-ejkm+ejkn+fjmn-fkmn)/(jn-km)\end{cases}">

which are collinear, i.e.

<img src="https://latex.codecogs.com/gif.latex?x_\text{ab}y_\text{ac}+x_\text{ac}y_\text{bc}+x_\text{bc}y_\text{ab}=x_\text{ac}y_\text{ab}+x_\text{bc}y_\text{ac}+x_\text{ab}y_\text{bc}"> □ <sup>[3]</sup>

## Proof by Homogeneous coordinates

**Homogeneous coordinates** are widely used in projective geometry. Because of the [Duality](https://en.wikipedia.org/wiki/Homogeneous_coordinates#Line_coordinates_and_duality), both point and straight line can be represented as homogeneous coordinates, and share the same form:

- A point <img src="https://latex.codecogs.com/gif.latex?(x_1,x_2,x_3)"> lies on a straight line <img src="https://latex.codecogs.com/gif.latex?[u_1,u_2,u_3]"> (i.e. a straight line passes through a point) if and only if <img src="https://latex.codecogs.com/gif.latex?x_1u_1+x_2u_2+x_3u_3=0">.
- The straight line passing through two points <img src="https://latex.codecogs.com/gif.latex?(x_1,x_2,x_3)"> and <img src="https://latex.codecogs.com/gif.latex?(x'_1,x'_2,x'_3)"> is <img src="https://latex.codecogs.com/gif.latex?[x_2x'_3-x_3x'_2,x_3x'_1-x_1x'_3,x_1x'_2-x_2x'_1]">.
- The intersection point of two straight lines <img src="https://latex.codecogs.com/gif.latex?[u_1,u_2,u_3]"> and <img src="https://latex.codecogs.com/gif.latex?[u'_1,u'_2,u'_3]"> is <img src="https://latex.codecogs.com/gif.latex?(u_2u'_3-u_3u'_2,u_3u'_1-u_1u'_3,u_1u'_2-u_2u'_1)">.

From linear algebra point of view:

- Two points (straight lines) *A* and *B* are the same point (straight line) if and only if they are they are linear-dependent.
- Three points (straight lines) *A*, *B* and *C* are collinear (concurrent) if and only if they are linear-dependent (in other words, there exists non-zero *m* and *n* such that <img src="https://latex.codecogs.com/gif.latex?A=mB+nC">, this also means their 3 x 3 determinant is zero).
- Four points (straight lines) whether collinear (concurrent) or not, are always linear-dependent.

**Advantages:**

- A theorem and its dual theorem share the same proof process, so no necessary to prove twice.
- There are only additions, subtractions and multiplications during proof process, so all expressions are polynomials, which are simpler than rational functions.

**Disadvantages:**

- Each point needs 3 variables, more than Cartesian coordinates.
- Should use origin and axes carefully, because the origin and axes are dual as lines and points at infinity.

For example, to reduce number of variables, we should carefully put a regular point *P*(*a*,*b*,*c*) onto special places:

- put onto origin as *P*(0,0,1), which may not work for the dual process because line [0,0,1] denotes a line at infinity;
- put onto y-axis as *P*(0,*b*,1), which may not cover the parallel case in "3 lines are parallel or concurrent at point *P*";  
- put onto y-axis as *P*(0,*b*,*c*), which may work well.

**Tricks:**

- Both <img src="https://latex.codecogs.com/gif.latex?(kx_1,kx_2,kx_3)"> and <img src="https://latex.codecogs.com/gif.latex?(x_1,x_2,x_3)"> represent the same point, so divide by their common factor as early as possible to simplify calculation.
- Homogeneous coordinates can be denoted as 3D vectors. The line passing through two points, or the intersection point of two lines, can be determined by [Cross Product](https://en.wikipedia.org/wiki/Cross_product). The collinearity and concurrency can be determined by [Triple Product](https://en.wikipedia.org/wiki/Triple_product).

### Proof

Because *A*<sub>1</sub>*A*<sub>2</sub>, *B*<sub>1</sub>*B*<sub>2</sub> and *C*<sub>1</sub>*C*<sub>2</sub> are concurrent at *O*, we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_2=pO+qA_1\\B_2=rO+sB_1\\C_2=tO+uC_1\end{cases}">

Then we have <img src="https://latex.codecogs.com/gif.latex?rA_2-pB_2=qrA_1-psB_1">, so there exists a point:

<img src="https://latex.codecogs.com/gif.latex?G=rA_2-pB_2=qrA_1-psB_1">

which is collinear to *A*<sub>1</sub>*B*<sub>1</sub> and *A*<sub>2</sub>*B*<sub>2</sub>, i.e. <img src="https://latex.codecogs.com/gif.latex?G=A_1B_1{\cap}A_2B_2=ab">.

Analogously, we have *ac*:

<img src="https://latex.codecogs.com/gif.latex?H=tB_2-rC_2=stB_1-ruC_1">

and *bc*:

<img src="https://latex.codecogs.com/gif.latex?J=pC_2-tA_2=puC_1-qtA_1">

Finally, we get <img src="https://latex.codecogs.com/gif.latex?tG+pH+rJ=0">, which means *ab*, *ac* and *bc* are collinear. □ <sup>[4]</sup>

If *O*, *A*<sub>1</sub>, *B*<sub>1</sub>, *C*<sub>1</sub> represent 4 lines, then *A*<sub>2</sub>, *B*<sub>2</sub>, *C*<sub>2</sub> are 3 lines respectively passing through intersections *OA*<sub>1</sub>, *OB*<sub>1</sub>, *OC*<sub>1</sub>. Then *A*<sub>1</sub> *B*<sub>1</sub> *C*<sub>1</sub> and *A*<sub>2</sub> *B*<sub>2</sub> *C*<sub>2</sub> are 6 edges of two perspective triangles. So the above proof process also means the 3 perspective lines *G*, *H* and *J* are concurrent, which is the dual and converse theorem.

### Proof of Pappus's Theorem

<img src="diagrams/pappus.png">

**Pappus's theorem** states that given two sets of collinear points *AEC* and *DBF*, then the intersection points *G*=*AB*∩*DE*, *H*=*BC*∩*EF* and *J*=*AF*∩*CD* are collinear.

Given 4 arbitrary points *A*, *B*, *C* and *D*, from which no three points are collinear, we can denote *D* as:

<img src="https://latex.codecogs.com/gif.latex?D=A+pB+qC">

*E* is collinear with *A* and *C*:

<img src="https://latex.codecogs.com/gif.latex?E=A+rC">

*F* is collinear with *B* and *D*:

<img src="https://latex.codecogs.com/gif.latex?F=sB+D=A+(p+s)B+qC">

Now let's calculate *G*, *H* and *J*.

*G* is collinear with *A* and *B*:

<img src="https://latex.codecogs.com/gif.latex?G=A+xB">

Take (*A*, *B*, *C*) as basis, then the coefficients' determinant of *D*, *E* and *G* should be zero because they are collinear:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}1&p&q\\1&0&r\\1&x&0\end{matrix}\right]=0">

Solve <img src="https://latex.codecogs.com/gif.latex?x=pr/(r-q)">:

<img src="https://latex.codecogs.com/gif.latex?G=A+\frac{pr}{r-q}B\quad\text{(Eq.\,1)}">

(Note that we cannot denote G again as <img src="https://latex.codecogs.com/gif.latex?G=D+x'E">. However, <img src="https://latex.codecogs.com/gif.latex?G=x'D+x''E"> or <img src="https://latex.codecogs.com/gif.latex?G'=D+x'E=x''G"> are okay and they can get the same result as Eq. 1.)

Next, *H* is collinear with *B* and *C*:

<img src="https://latex.codecogs.com/gif.latex?H=B+yC">

And *H* is also collinear with *E* and *F*:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}1&0&r\\1&p+s&q\\0&1&y\end{matrix}\right]=0">

Solve <img src="https://latex.codecogs.com/gif.latex?y=(q-r)/(p+s)">:

<img src="https://latex.codecogs.com/gif.latex?H=B+\frac{q-r}{p+s}C\quad\text{(Eq.\,2)}">

Next, *J* is collinear with *C* and *D*:

<img src="https://latex.codecogs.com/gif.latex?J=zC+D=A+pB+(z+q)C">

And *J* is also collinear with *A* and *F*:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}1&0&0\\1&p+s&q\\1&p&z+q\end{matrix}\right]=0">

Solve <img src="https://latex.codecogs.com/gif.latex?z=-qs/(p+s)">:

<img src="https://latex.codecogs.com/gif.latex?J=A+pB+\frac{pq}{p+s}C\quad\text{(Eq.\,3)}">

Now let's calculate the coefficients' determinant of *G*, *H* and *J* from Eq. 1, 2 and 3:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}1&\frac{pr}{r-q}&0\\0&1&\frac{q-r}{p+s}\\1&p&\frac{pq}{p+s}\end{matrix}\right]=0">

which means *G*, *H* and *J* are collinear. □ <sup>[5]</sup>

If *A*, *C*, *E* represent 3 concurrent lines and *B*, *D*, *F* represent another 3 concurrent lines, then the 3 lines *G*, *H*, *J*, respectively passing through *A*∩*B* and *D*∩*E*, *B*∩*C* and *E*∩*F*, *A*∩*F* and *C*∩*D*, are concurrent, which is the [dual theorem](https://en.wikipedia.org/wiki/Pappus%27s_hexagon_theorem#Dual_theorem).

### 3D vector proof of Desargues's theorem

Denote points *O*, *A*<sub>1</sub>, *B*<sub>1</sub>, *C*<sub>1</sub> as **O**, **A**<sub>1</sub>, **B**<sub>1</sub>, **C**<sub>1</sub>, then we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{A_2}=p\mathbf{O}+q\mathbf{A_1}\\\mathbf{B_2}=r\mathbf{O}+s\mathbf{B_1}\\\mathbf{C_2}=t\mathbf{O}+u\mathbf{C_1}\end{cases}">

And we denote intersection *ab* as: <sup>[6]</sup>

<img src="https://latex.codecogs.com/gif.latex?{\mathbf{G}=(\mathbf{A_1}\times\mathbf{B_1})\times(\mathbf{A_2}\times\mathbf{B_2})=[(\mathbf{A_1}\times\mathbf{B_1})\cdot\mathbf{B_2}]\mathbf{A_2}-[(\mathbf{A_1}\times\mathbf{B_1})\cdot\mathbf{A_2}]\mathbf{B_2}=\dots=[(\mathbf{A_1}\times\mathbf{B_1})\cdot\mathbf{O}](qr\mathbf{A_1}-ps\mathbf{B_1})}">

Analogously, we have *ac*:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{H}=[(\mathbf{C_1}\times\mathbf{A_1})\cdot\mathbf{O}](pu\mathbf{C_1}-qt\mathbf{A_1})">

and *bc*:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J}=[(\mathbf{B_1}\times\mathbf{C_1})\cdot\mathbf{O}](st\mathbf{B_1}-ru\mathbf{C_1})">

Finally, we get <img src="https://latex.codecogs.com/gif.latex?\mathbf{G}\cdot(\mathbf{H}\times\mathbf{J})=\mathbf{0}">, which means *ab*, *ac* and *bc* are collinear. □

### 3D vector proof of Pappus's Theorem

Given 4 arbitrary points **A**, **B**, **C** and **D**, then **E** and **F** can be denoted as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{E}=p\mathbf{A}+q\mathbf{C}\\\mathbf{F}=r\mathbf{B}+s\mathbf{D}\end{cases}">

Then we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{G}=(\mathbf{A}\times\mathbf{B})\times(\mathbf{D}\times\mathbf{E})=\dots=dq\mathbf{D}-cp\mathbf{A}-cq\mathbf{C}\\\mathbf{H}=(\mathbf{B}\times\mathbf{C})\times(\mathbf{E}\times\mathbf{F})=\dots=aps\mathbf{A}+aqs\mathbf{C}-dpr\mathbf{B}-dps\mathbf{D}\\\mathbf{J}=(\mathbf{C}\times\mathbf{D})\times(\mathbf{F}\times\mathbf{A})=\dots=br\mathbf{B}+bs\mathbf{D}-ar\mathbf{A}\end{cases}">

where

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}a=(\mathbf{B}\times\mathbf{C})\cdot\mathbf{D}\\b=(\mathbf{A}\times\mathbf{C})\cdot\mathbf{D}\\c=(\mathbf{A}\times\mathbf{B})\cdot\mathbf{D}\\d=(\mathbf{A}\times\mathbf{B})\cdot\mathbf{C}\end{cases}">

After some calculations, we get <img src="https://latex.codecogs.com/gif.latex?\mathbf{G}\cdot(\mathbf{H}\times\mathbf{J})=\mathbf{0}">, which means *G*, *H* and *J* are collinear. □

### Notes

1. Here we use the diagram from [Cut the Knot](https://www.cut-the-knot.org/Curriculum/Geometry/Desargues.shtml).
2. This complicated result can be solved by SymPy [here](projective/desargues-c1.py).
3. This complicated result can be solved by SymPy [here](projective/desargues-c2.py).
4. [Here](projective/desargues-h.py) is a proof of Desargues's theorem by homogeneous coordinates without linear algebra.
5. [Here](projective/pappus-h.py) is a proof of Pappus's theorem by homogeneous coordinates without linear algebra; [here](projective/pappus-c1.py) and [here](projective/pappus-c2.py) are proofs by Cartesian coordinates.
6. Here we should use some [vector formulas](diagrams/vector-formulas.png) (copied from the first page in John David Jackson's *Classical Electrodynamics*).