<img src="diagrams/feuerbach.png">

**Feuerbach's theorem** states that the nine-point circle is tangent to the three excircles of the triangle as well as its incircle.

### Start from Triangle

Put *AB* onto x-axis and *C* onto y-axis:

- The nine-point circle passes through three midpoints *M*<sub>A</sub>, *M*<sub>B</sub>, and *M*<sub>C</sub>;
- The incircle passes through *D*, *E* and *F*, where *AE* = *AF*, *BD* = *BF* and *CD* = *CE*;
- One excircle passes through *G*, *H* and *K*, where *AH* = *AK*, *BG* = *BK* and *CH* = *CG*.

So we can get the equations of these three circles. Take the nine-point circle and the incircle as example, denote their equations as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x^2+y^2+d_\text{N}x+e_\text{N}y+f_\text{N}=0\\x^2+y^2+d_\text{I}x+e_\text{I}y+f_\text{I}=0\end{cases}">

Eliminate *y* or *x* in either of the two equations by the radical line <img src="https://latex.codecogs.com/gif.latex?(d_\text{N}-d_\text{I})x+(e_\text{N}-e_\text{I})y+(f_\text{N}-f_\text{I})=0">, then we get a quadratic equation about *x* or *y*.

Because we need to prove these two circles are tangent (i.e. they have only one common point), the remaining work is just checking if the discriminant of the quadratic equation is zero.

[Here](pythagoras/feuerbach.py) is the proof process.

Another approach is to calculate radii and distance:

- The incircle is inside and internally tangent to the nine-point circle if and only if <img src="https://latex.codecogs.com/gif.latex?|NI|=r_\text{N}-r_\text{I}">;
- One excircle is externally tangent to the nine-point circle if and only if <img src="https://latex.codecogs.com/gif.latex?|NE|=r_\text{N}+r_\text{E}">.

Because all of |*NI*|, *r*<sub>N</sub>, *r*<sub>I</sub> and *r*<sub>E</sub> contain square roots, which are too difficult to calculate, we need to rewrite them to simplify calculation:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}(r_N^2+r_I^2-|NI|^2)^2=4r_N^2r_I^2\\(r_N^2+r_E^2-|NE|^2)^2=4r_N^2r_E^2\end{cases}">

Neither of the two approaches can tell us whether two circles are internally or externally tangent. However, the incircle is obviously inside and internally tangent to the nine-point circle, because the incircle is inside the triangle and the nine-point circle intersects all three edges; each excircle is abviously externally tangent to the nine-point circle, because each excircle is outside of the triangle.

### Start from Incircle

If we use the coordinates mentioned [here](euler-line.md) (proof of Theorem 1), it is possible to finish the proof by hand. Given an incircle:

<img src="https://latex.codecogs.com/gif.latex?x^2+y^2-2ry=0\quad\text{(Eq.\,1)}">

and two vertices *A*(-*a*,0) and *B*(*b*,0) on x-axis, then *C* is <img src="https://latex.codecogs.com/gif.latex?\left(\frac{(a-b)r^2}{ab-r^2},\frac{2abr}{ab-r^2}\right)">. And the nine-point equation is:

<img src="https://latex.codecogs.com/gif.latex?{x^2+y^2-\frac{(a-b)(3r^2-ab)x}{2(ab-r^2)}-\frac{(ab-ar+br+r^2)(ab+ar-br+r^2)y}{4(ab-r^2)r}-\frac{(a-b)^2r^2}{2(ab-r^2)}=0\quad\text{(Eq.\,2)}">

The equation set of two circles (Eq. 1 and Eq. 2) has only one root (because of its zero discriminant), which proves the tangency of two circles.

An interesting thing is that Eq. 1 can also be an excircle of trangle *ABC* if we set <img src="https://latex.codecogs.com/gif.latex?ab<r^2">. So the the tangency of nine-point circle and excircle is also proved.

The tangency can also be proved by calculating the nine-point circle's center:

<img src="https://latex.codecogs.com/gif.latex?N=\left(\frac{(a-b)(3r^2-ab)}{4(ab-r^2)},\frac{(ab-ar+br+r^2)(ab+ar-br+r^2)}{8r(ab-r^2)}\right)">

and radius:

<img src="https://latex.codecogs.com/gif.latex?r_N^2=\frac{(a^2+r^2)^2(b^2+r^2)^2}{64r^2(ab-r^2)^2}">

And the distance between the two circles' centers should be:

<img src="https://latex.codecogs.com/gif.latex?|NI(E)|^2=\frac{(a^2b^2+a^2r^2-8abr^2+b^2r^2+9r^4)^2}{64r^2(ab-r^2)^2}">

For the incircle case (<img src="https://latex.codecogs.com/gif.latex?ab>r^2">), we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}r_N=\dfrac{(a^2+r^2)(b^2+r^2)}{8r(ab-r^2)}\\r_I=r\\|NI|=\dfrac{a^2b^2+a^2r^2-8abr^2+b^2r^2+9r^4}{8r(ab-r^2)}\end{cases}">

So we get <img src="https://latex.codecogs.com/gif.latex?|NI|=r_\text{N}-r_\text{I}">, which means the incircle is inside and internally tangent to the nine-point circle.

For the excircle case (<img src="https://latex.codecogs.com/gif.latex?ab<r^2">), we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}r_N=\dfrac{(a^2+r^2)(b^2+r^2)}{8r(r^2-ab)}\\r_E=r\\|NE|=\dfrac{a^2b^2+a^2r^2-8abr^2+b^2r^2+9r^4}{8r(r^2-ab)}\end{cases}">

So we get <img src="https://latex.codecogs.com/gif.latex?|NE|=r_\text{N}+r_\text{E}">, which means the excircle is externally tangent to the nine-point circle.

Other proofs can be found [here](https://imomath.com/index.cgi?page=inversion) (Problem 7) and [here](https://www.cut-the-knot.org/Curriculum/Geometry/FeuerbachProof.shtml).

### Theorems related to the Feuerbach Point

**Theorem 1** The circle through the [feet of the internal bisectors](https://mathworld.wolfram.com/IncentralTriangle.html) *I*<sub>A</sub>*I*<sub>B</sub>*I*<sub>C</sub> of a triangle *ABC* passes through the Feuerbach point.

[Here](pythagoras/feuerbach-1.py) is the computational proof *starting from incircle*.

**Theorem 2** The Feuerbach point of a triangle *ABC* is the [anti-Steiner point](https://artofproblemsolving.com/community/c1646h1025320s3_antisteiner_point) of the Euler line of the [intouch triangle](https://mathworld.wolfram.com/ContactTriangle.html) *C*<sub>A</sub>*C*<sub>B</sub>*C*<sub>C</sub> with respect to the same intouch triangle *C*<sub>A</sub>*C*<sub>B</sub>*C*<sub>C</sub>.

[Here](pythagoras/feuerbach-2.py) is the computational proof *starting from incircle*.

Other proofs of the two theorems can be found [here](http://blancosilva.github.io/post/2013/07/15/some-results-related-to-the-feuerbach-point.html) (computational) and [here](https://forumgeom.fau.edu/FG2012volume12/FG201205.pdf) (synthetic).

**Theorem 3** Let *F*<sub>A</sub>, *F*<sub>B</sub>, *F*<sub>C</sub> be the touch points of the nine-point circle with the *A*-, *B*-, *C*- excircles, respectively. The lines *AF*<sub>A</sub>, *BF*<sub>B</sub>, *CF*<sub>C</sub> meet at *X*(12), the harmonic conjugate of the Feuerbach point *F*<sub>I</sub> with respect to the incenter *I* and the nine-point center *N*. <sup>[1](https://www.cut-the-knot.org/Curriculum/Geometry/FeuerbachIncidence.shtml)</sup>

[Here](pythagoras/feuerbach-3.py) is the computational proof *starting from incircle*.

This theorem can also be proved by [Monge's theorem](monge.md#monges-theorem) (proposition 2).