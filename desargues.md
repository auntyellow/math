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

From linear algebra (or vector space) point of view:

- Two points (straight lines) *A* and *B* are the same point (straight line) if and only if they are they are linear-dependent.
- Three points (straight lines) *A*, *B* and *C* are collinear (concurrent) if and only if they are linear-dependent (in other words, there exists non-zero *m* and *n* such that <img src="https://latex.codecogs.com/gif.latex?A=mB+nC">, this also means their 3 x 3 determinant is zero).
- Four points (straight lines) whether collinear (concurrent) or not, are always linear-dependent.

According to the duality, dual incidence propositions share the same proof process, so no necessary to prove twice.

Another advantage is that only additions, subtractions and multiplications appear in the proof process, so all expressions are polynomials, which are simpler than rational functions.

### Tricks

1. Both <img src="https://latex.codecogs.com/gif.latex?(kx_1,kx_2,kx_3)"> and <img src="https://latex.codecogs.com/gif.latex?(x_1,x_2,x_3)"> represent the same point, so divide by their common factor as early as possible to simplify calculation.
2. The first three non-collinear free points (*A*, *B*, *C*) can be taken as basis, then
    - a. the forth non-collinear free point can be represented as <img src="https://latex.codecogs.com/gif.latex?D=A+B+C"> (adjust *B* and *C*), and the later non-collinear free points can be represented as <img src="https://latex.codecogs.com/gif.latex?P_n=A+p_nB+q_nC">, or
    - b. the forth semi-free point lying on *AB* can be represented as <img src="https://latex.codecogs.com/gif.latex?D=A+B"> (adjust *B*), and the fifth non-collinear free point can be represented as <img src="https://latex.codecogs.com/gif.latex?E=A+pB+C"> (adjust *C*), and the later non-collinear free points can be represented as <img src="https://latex.codecogs.com/gif.latex?P_n=A+p_nB+q_nC">, or
    - c. the forth semi-free point lying on *AB* can be represented as <img src="https://latex.codecogs.com/gif.latex?D=A+B"> (adjust *B*), and the fifth semi-free point lying on *AC* can be represented as <img src="https://latex.codecogs.com/gif.latex?E=A+C"> (adjust *C*), and the later non-collinear free points can be represented as <img src="https://latex.codecogs.com/gif.latex?P_n=A+p_nB+q_nC">.
3. For two points <img src="https://latex.codecogs.com/gif.latex?E=aA+bB+cC"> and <img src="https://latex.codecogs.com/gif.latex?F=dA+eB+fC">, line *EF* matches the equation <img src="https://latex.codecogs.com/gif.latex?(bf-ce)x+(cd-af)y+(ae-bd)z=0">, where <img src="https://latex.codecogs.com/gif.latex?xA+yB+zC"> is a point on line *EF*.
4. For two lines <img src="https://latex.codecogs.com/gif.latex?ax+by+cz=0"> and <img src="https://latex.codecogs.com/gif.latex?dx+ey+fz=0">, where (*x*, *y*, *z*) are coefficients on basis (*A*, *B*, *C*), their intersection is <img src="https://latex.codecogs.com/gif.latex?(bf-ce)A+(cd-af)B+(ae-bd)C">.

### Proof

Given 4 arbitrary points *A*<sub>1</sub>, *B*<sub>1</sub>, *C*<sub>1</sub> and *O*, from which no three points are collinear, we can denote *O*, *A*<sub>2</sub>, *B*<sub>2</sub> and *C*<sub>2</sub> by Trick 2a (we can also take (*O*, *A*<sub>1</sub>, *B*<sub>1</sub>) as basis and denote the other points by Trick 2b or 2c) as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}O=A_1+B_1+C_1\\A_2=aA_1+O=(a+1)A_1+B_1+C_1\\B_2=bB_1+O=A_1+(b+1)B_1+C_1\\C_2=cC_1+O=A_1+B_1+(c+1)C_1\end{cases}">

Now let's calculate *G*(*ab*), *H*(*ac*) and *J*(*bc*) by Trick 3 and 4:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}G=A_1B_1{\cap}A_2B_2=aA_1-bB_1\\H=A_1C_1{\cap}A_2C_2=-aA_1+cC_1\\J=B_1C_1{\cap}B_2C_2=bB_1-cC_1\end{cases}">

They are obviously linear dependent, which means *ab*, *ac* and *bc* are collinear. □ <sup>[4]</sup>

If *O*, *A*<sub>1</sub>, *B*<sub>1</sub>, *C*<sub>1</sub> represent 4 lines, then *A*<sub>2</sub>, *B*<sub>2</sub>, *C*<sub>2</sub> are 3 lines respectively passing through intersections *OA*<sub>1</sub>, *OB*<sub>1</sub>, *OC*<sub>1</sub>. Then *A*<sub>1</sub> *B*<sub>1</sub> *C*<sub>1</sub> and *A*<sub>2</sub> *B*<sub>2</sub> *C*<sub>2</sub> are 6 edges of two perspective triangles. So the above proof process also means the 3 perspective lines *G*, *H* and *J* are concurrent, which is the dual and converse theorem.

### Proof of Pappus's Theorem

<img src="diagrams/pappus.png">

**Pappus's theorem** states that given two sets of collinear points *AEC* and *DBF*, then the intersection points *G*=*AB*∩*DE*, *H*=*BC*∩*EF* and *J*=*AF*∩*CD* are collinear.

Given 4 arbitrary points *A*, *B*, *C* and *D*, from which no three points are collinear, we can denote *D*, *E* and *F* by Trick 2a as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}D=A+B+C\\E=A+mC\\F=(n-1)B+D=A+nB+C\end{cases}">

Now let's calculate *G*, *H* and *J* by Trick 3 and 4:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}G=AB{\cap}DE=(m-1)A+mB\\H=BC{\cap}EF=-nB+(m-1)C\\J=CD{\cap}FA=-nA-nB-C\end{cases}">

Then calculate the coefficients' determinant of *G*, *H* and *J*:

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}m-1&m&0\\0&-n&m-1\\-n&-n&-1\end{matrix}\right]=0">

which means they are collinear. □ <sup>[5]</sup>

If *A*, *C*, *E* represent 3 concurrent lines and *B*, *D*, *F* represent another 3 concurrent lines, then the 3 lines *G*, *H*, *J*, respectively passing through *A*∩*B* and *D*∩*E*, *B*∩*C* and *E*∩*F*, *A*∩*F* and *C*∩*D*, are concurrent, which is the [dual theorem](https://en.wikipedia.org/wiki/Pappus%27s_hexagon_theorem#Dual_theorem).

### Notes

1. Here we use the diagram from [Cut the Knot](https://www.cut-the-knot.org/Curriculum/Geometry/Desargues.shtml).
2. This complicated result can be solved by SymPy [here](projective/desargues-c1.py).
3. This complicated result can be solved by SymPy [here](projective/desargues-c2.py).
4. For Desargues's theorem, [here](projective/desargues-v.py) is a vector space proof.
5. For Pappus's theorem, [here](projective/pappus-v.py) is a vector space proof, and [here](projective/pappus-c1.py) and [here](projective/pappus-c2.py) are proofs by Cartesian coordinates.