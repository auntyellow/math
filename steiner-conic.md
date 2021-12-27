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

### Steiner conic and Quatric curve

#### Steiner conic → Quatric curve

The Steiner conic follows the quatric curve equation <img src="https://latex.codecogs.com/gif.latex?Ax^2+Bxy+Cy^2+Dxz+Eyz+F=0">. Let's denote lines *cdec'd'e'* in homogeneous coordinate:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{c}=[a,b,c]\\\mathbf{d}=[d,e,f]\\\mathbf{e}=p\mathbf{c}+q\mathbf{d}\\\mathbf{c'}=[g,h,j]\\\mathbf{d'}=[k,m,n]\\\mathbf{e'}=r\mathbf{c'}+s\mathbf{d'}\end{cases}">

Point <img src="https://latex.codecogs.com/gif.latex?F(x,y,z)"> follows <img src="https://latex.codecogs.com/gif.latex?N=BC{\cap}AF">, <img src="https://latex.codecogs.com/gif.latex?N'=AC{\cap}BF">, and *NN'P* are collinear, and *N* and *N'* can be calculated by step 1 and 2 in the above the construction. So we can get the equation eventually:

<img src="https://latex.codecogs.com/gif.latex?\begin{array}{l}(akps-dgqr)x^2+(amps+bkps-dhqr-egqr)xy+(bmps-ehqr)y^2+\\(anps+ckps-djqr-fgqr)xz+(bnps+cmps-ejqr-fhqr)yz+(cnps-fjqr)z^2=0\end{array}">

#### Quatric curve → Steiner conic

### Pascal's theorem