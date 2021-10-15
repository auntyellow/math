### Construction of the Symmedian

<img src="diagrams/symmedian.png">

Construct a point *D* by intersecting the tangents from B and C to the circumcircle of triangle *ABC*, then AD is the **symmedian** of the triangle ABC, which implies ∠*BAM* = ∠*CAD*, where *AM* is the median.

Let's put the circumcenter onto the origin, rotate the triangle to make *BC* parallel to y-axis, then we get the equations of the circumcircle and line *AD*:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x^2+y^2=r^2\\y=\sqrt{r^2-a^2}(r^2-bx)/(ab+r^2)\end{cases}">

We can solve intersection *E* by eliminating *y*:

<img src="https://latex.codecogs.com/gif.latex?(2ab+b^2+r^2)x^2-2(r^2-a^2)bx-a(ab^2+ar^2+2br^2)=0">

Here we use Vieta's formula because we already know a root *x*<sub>A</sub>:

<img src="https://latex.codecogs.com/gif.latex?x_\text{E}=\frac{2(r^2-a^2)b}{2ab+b^2+r^2}-x_\text{A}=\frac{ab^2+ar^2+2br^2}{2ab+b^2+r^2}">

Reflect *E* about x-axis at *E'* to make ∠*BAE'* = ∠*CAE*, then we have <img src="https://latex.codecogs.com/gif.latex?x_\text{E'}=x_\text{E}"> and

<img src="https://latex.codecogs.com/gif.latex?y_\text{E'}=\frac{\sqrt{r^2-a^2}(b^2-r^2)}{2ab+b^2+r^2}">

After some calculations, we get:

<img src="https://latex.codecogs.com/gif.latex?x_\text{A}y_\text{M}+x_\text{M}y_\text{E'}+x_\text{E'}y_\text{A}=x_\text{M}y_\text{A}+x_\text{E'}y_\text{M}+x_\text{A}y_\text{E'}">

which implies *AME'* are collinear, so ∠*BAM* = ∠*CAD*. □

Other proofs can be found [here](https://en.wikipedia.org/wiki/Symmedian#Construction_of_the_symmedian).

### Construction of the Isogonal Conjugate

<img src="diagrams/isogonal.png">

*P* is an arbitrary point in triangle *ABC*. Construct the pedal trangle *DEF* and its circumcenter *M*. Reflect *P* about *M* at point *Q*, then *Q* is the **Isogonal Conjugate** of *P*.

[Here](pythagoras/isogonal.py) proves <img src="https://latex.codecogs.com/gif.latex?\cos^2\angle{PAB}=\cos^2\angle{QAC}"> but not <img src="https://latex.codecogs.com/gif.latex?\cos\angle{PAB}=\cos\angle{QAC}">, because *P* may be a point outside the triangle, where we may have <img src="https://latex.codecogs.com/gif.latex?\angle{PAB}+\angle{QAC}=\pi"> instead of <img src="https://latex.codecogs.com/gif.latex?\angle{PAB}=\angle{QAC}">.

Other proofs can be found [here](https://blog.evanchen.cc/2014/11/30/three-properties-of-isogonal-conjugates/) (section 3) and [here](http://www.cut-the-knot.org/Curriculum/Geometry/OrthologicPedal.shtml).