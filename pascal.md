<img src="diagrams/pascal.png">

**Pascal's theorem** states that if six arbitrary points are chosen on a conic and joined by line segments in any order (here we choose *A→B→C→D→E→F*) to form a hexagon, then the three pairs of opposite sides (*AB DE*, *BC EF* and *CD AF*) of the hexagon meet at three points (*G*, *H* and *I*) which lie on a straight line. <sup>[1]</sup>

### About SymPy

Unlike the analytic geometry proof of [butterfly theorem](butterfly.md) where equations can be simplified by [Vieta's formulas](https://en.wikipedia.org/wiki/Vieta%27s_formulas), most theorems in projective geometry are too complicated to prove by analytic geometry by hand. Instead, we use [SymPy](https://en.wikipedia.org/wiki/SymPy) to do most calculations.

Here are some simple cases:

- [harmonic conjugate](projective/harmonic.py)
- [harmonic conjugate of pole and polar](projective/pole-polar.py)
- [Desargues's theorem](desargues.md)
- [Pappus's theorem](projective/pappus.py)
- [butterfly theorem](projective/butterfly.py), an analytic geometry proof without Vieta's formulas
- [Braikenridge-Maclaurin theorem](projective/braikenridge-maclaurin.py), with some tricks mentioned [here](https://math.stackexchange.com/a/4236022/919440)

However, the proof of Pascal's theorem is more complicated.

### The Proof

Let's put point *I* onto the origin, rotate the hexagon to make *BE* parallel to x-axis, denote the conic *ADBFCE* as:

<img src="https://latex.codecogs.com/gif.latex?ax^2+bxy+cy^2+dx+ey+f=0">

and denote *AF*, *CD* and *BE* as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}AF:y=gx\\CD:y=hx\\BE:y=k\end{cases}">

#### Step 1

Two points can be solved by a conic and a straight line. However, SymPy won't tell us whether the first root denotes the point in the left or right side. So we need to guess then verify by numerical evaluation.

Assume the conic is <img src="https://latex.codecogs.com/gif.latex?x^2+y^2-1=0"> and the line *AF* is <img src="https://latex.codecogs.com/gif.latex?y=x">, we should get *A* in quadrant I and *F* in quadrant III. So we should use `F, A = solve(...)` but not `A, F = solve(...)`.

[Here](projective/pascal1.py) we get 6 points:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{A}=-(d+eg-\sqrt{-4af-4bfg-4cfg^2+d^2+2deg+e^2g^2})/2(a+bg+cg^2)\\x_\text{B}=-(bk+d+\sqrt{-4ack^2-4aek-4af+b^2k^2+2bdk+d^2})/2a\\x_\text{C}=-(d+eh-\sqrt{-4af-4bfh-4cfh^2+d^2+2deh+e^2h^2})/2(a+bh+ch^2)\\x_\text{D}=-(d+eh+\sqrt{-4af-4bfh-4cfh^2+d^2+2deh+e^2h^2})/2(a+bh+ch^2)\\x_\text{E}=-(bk+d-\sqrt{-4ack^2-4aek-4af+b^2k^2+2bdk+d^2})/2a\\x_\text{F}=-(d+eg+\sqrt{-4af-4bfg-4cfg^2+d^2+2deg+e^2g^2})/2(a+2bg+2cg^2)\end{cases}">

#### Step 2

Without further simplification, SymPy can hardly solve the intersections G and H. (This may be due to too many calculations during cancellation of <img src="https://latex.codecogs.com/gif.latex?\sqrt{x}^2"> and *x*.<sup>[2]</sup> I don't know if Mathematica or other alternatives can do this.) So we need to replace all square roots with:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}P=\sqrt{-4af-4bfg-4cfg^2+d^2+2deg+e^2g^2}\\Q=\sqrt{-4af-4bfh-4cfh^2+d^2+2deh+e^2h^2}\\R=\sqrt{-4ack^2-4aek-4af+b^2k^2+2bdk+d^2}\end{cases}">

Then the 6 points are simplified as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}x_\text{A}=-(d+eg-P)/2(a+bg+cg^2)\\x_\text{B}=-(bk+d+R)/2a\\x_\text{C}=-(d+eh-Q)/2(a+bh+ch^2)\\x_\text{D}=-(d+eh+Q)/2(a+bh+ch^2)\\x_\text{E}=-(bk+d-R)/2a\\x_\text{F}=-(d+eg+P)/2(a+2bg+2cg^2)\end{cases}">

[Here](projective/pascal2.py) we solve the G and H and get the expression <img src="https://latex.codecogs.com/gif.latex?x_\text{G}y_\text{H}-x_\text{H}y_\text{G}"> to check if G, H and I are collinear.

The numerator of this expression can be denoted as *S*×*T*−*U*×*V*, with both *S* and *U* containing 69 terms, and both *T* and *V* containing 125 terms. We just need to prove the numerator equal to 0.

#### Step 3

[Here](projective/pascal3.py) we expand the numerator *S*×*T*−*U*×*V* to 432 terms (cancelled from 69×125×2 terms).

#### Step 4

There are many *P*<sup>2</sup>, *Q*<sup>2</sup> and *R*<sup>3</sup> in the above expanded numerator. So we can replace them with:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}P^2=-4af-4bfg-4cfg^2+d^2+2deg+e^2g^2\\Q^2=-4af-4bfh-4cfh^2+d^2+2deh+e^2h^2\\R^2=-4ack^2-4aek-4af+b^2k^2+2bdk+d^2\end{cases}">

This can be done by replacing `P**2`, `Q**2` and `R**3` with `P2`, `Q2` and `R2*R` in text editor.

[Here](projective/pascal4.py) shows the final result equal to 0, which means G, H and I are collinear.

### Notes

1. Here we use the diagram from [Cut the Knot](https://www.cut-the-knot.org/Generalization/OverlookedPascal.shtml).
2. More explanations can be found [here](https://docs.sympy.org/latest/tutorial/simplification.html).