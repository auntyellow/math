The **[Steiner Conic](https://en.wikipedia.org/wiki/Steiner_conic)** is an alternative definition of a conic: Given two pencils *P*(*A*), *P*(*B*) of lines at two points *A*, *B* (all lines containing *A* and *B* resp.) and a projective but not perspective mapping *π* of *P*(*A*) onto *P*(*B*), then the intersection points of corresponding lines form a non-degenerate projective conic section.

<img src="diagrams/steiner-conic.png">

In the above figure,

<img src="https://latex.codecogs.com/gif.latex?(c,d,e,f)\frac{c'}{\overline\wedge}(c'',d'',e'',f'')\frac{c}{\overline\wedge}(c',d',e',f')">

Therefore, by given lines *cdec'd'e'* or points *ABCDE*, and by given an arbitrary line *f* passing through *A*, we can construct line *f'* or point *F* by these steps:

1. <img src="https://latex.codecogs.com/gif.latex?{L=BC{\cap}AD,L'=AC{\cap}BD,M=BC{\cap}AE,M'=AC{\cap}BE,N=f{\cap}BC}">
2. <img src="https://latex.codecogs.com/gif.latex?P=LL'{\cap}MM'">
3. <img src="https://latex.codecogs.com/gif.latex?N'=AC{\cap}NP">
4. <img src="https://latex.codecogs.com/gif.latex?F=f{\cap}BN'">

This is the construction of Steiner *point* conic. Analogously, we can construct the Steiner *line* conic according to the principle of duality.

### Steiner conic → Quadric curve

The Steiner conic follows the quadric curve equation <img src="https://latex.codecogs.com/gif.latex?Ax^2+Bxy+Cy^2+Dxz+Eyz+Fz^2=0">. Let's denote lines *cdec'd'e'* in homogeneous coordinate:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{c}=[a,b,c]\\\mathbf{d}=[d,e,f]\\\mathbf{e}=p\mathbf{c}+q\mathbf{d}\\\mathbf{c'}=[g,h,j]\\\mathbf{d'}=[k,m,n]\\\mathbf{e'}=r\mathbf{c'}+s\mathbf{d'}\end{cases}">

Point <img src="https://latex.codecogs.com/gif.latex?F(x,y,z)"> follows <img src="https://latex.codecogs.com/gif.latex?N=BC{\cap}AF">, <img src="https://latex.codecogs.com/gif.latex?N'=AC{\cap}BF">, and *NN'P* are collinear, and *N* and *N'* can be calculated by step 1 and 2 in the above the construction. So we can get the equation eventually:

<img src="https://latex.codecogs.com/gif.latex?\begin{array}{l}(akps-dgqr)x^2+(amps+bkps-dhqr-egqr)xy+(bmps-ehqr)y^2+\\(anps+ckps-djqr-fgqr)xz+(bnps+cmps-ejqr-fhqr)yz+(cnps-fjqr)z^2=0\end{array}">

[Here](projective/steiner-conic-h1.py) is the calculation process.

According to the duality, this process also shows that the Steiner *line* conic follows the quadric curve (the envelope of a set of straight lines) equation.

### Five points determine a conic

[Here](projective/steiner-conic-h2.py) we calculate lines *cdec'd'e'* by given points *ABCDE*, and get the similar result, although the time is longer and the equation is more complicated.

[Here](projective/steiner-conic-h3.py) we get the same result by a rule that [five points determine a conic](https://en.wikipedia.org/wiki/Five_points_determine_a_conic):

<img src="https://latex.codecogs.com/gif.latex?\det\left[\begin{matrix}x^2&xy&y^2&xz&yz&z^2\\x_\text{A}^2&x_\text{A}y_\text{A}&y_\text{A}^2&x_\text{A}z_\text{A}&y_\text{A}z_\text{A}&z_\text{A}^2\\x_\text{B}^2&x_\text{B}y_\text{B}&y_\text{B}^2&x_\text{B}z_\text{B}&y_\text{B}z_\text{B}&z_\text{B}^2\\x_\text{C}^2&x_\text{C}y_\text{C}&y_\text{C}^2&x_\text{C}z_\text{C}&y_\text{C}z_\text{C}&z_\text{C}^2\\x_\text{D}^2&x_\text{D}y_\text{D}&y_\text{D}^2&x_\text{D}z_\text{D}&y_\text{D}z_\text{D}&z_\text{D}^2\\x_\text{E}^2&x_\text{E}y_\text{E}&y_\text{E}^2&x_\text{E}z_\text{E}&y_\text{E}z_\text{E}&z_\text{E}^2\end{matrix}\right]=0"> 

According to the duality, these two processes also shows that five straight lines determine a line conic.

### Quadric curve → Steiner conic

Conversely, any quadric curve is a Steiner conic. We only need to prove that for any 6 points *ABCDEF* on a quadric curve, <img src="https://latex.codecogs.com/gif.latex?(AC,AD;AE,AF)=(BC,BD;BE,BF)">.

WLOG, we can put *A* onto origin and *AB* onto y-axis, and denote the quadric curve as <img src="https://latex.codecogs.com/gif.latex?ax^2+bxy+cy^2+dxz+eyz=0">. For any line <img src="https://latex.codecogs.com/gif.latex?ux+vy=0"> passing through *A*, we can get the other intersection of the line and the quadric curve <img src="https://latex.codecogs.com/gif.latex?P(v(eu-dv),u(dv-eu),av^2-buv+cu^2)">.

[Here](projective/steiner-conic-h4.py) is the proof process.

To prove the dual fact, we can put line *A* onto x-axis and point *AB* onto origin, and denote the quadric curve (the envelope of a set of straight lines) as <img src="https://latex.codecogs.com/gif.latex?au^2+buv+duw+evw+fw^2=0">. For any point (*x*,0,*z*) (*z*=0 means the point at infinity) lying on *A*, we can get the other tangent line <img src="https://latex.codecogs.com/gif.latex?L[v(eu-dv),u(dv-eu),av^2-buv+cu^2]">.

[Here](projective/steiner-conic-h5.py) is the proof process.

### Pascal's theorem

The proof of Pascal's theorem on a Steiner conic is much simpler than on a quadric curve, because only incidence relations of points and straight lines should be considered, just like Desargues's theorem and Pappus's theorem.

[Here](projective/pascal-v.py) is a vector proof.

According to the duality, this process also proves Brianchon's theorem.

### Braikenridge-Maclaurin theorem

[Here](projective/braikenridge-maclaurin-v.py) is a vector proof.