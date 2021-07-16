### Chemical Equilibrium Equations

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{N}^\text{T}\mathbf{X}+\mathbf{C}=\mathbf{Y}\\\mathbf{N}\ln\mathbf{Y}=\ln\mathbf{K}\end{cases}">

Here <img src="https://latex.codecogs.com/gif.latex?\mathbf{C}=\begin{pmatrix}c_1\\c_2\\\vdots\\c_n\end{pmatrix}"> are initial concentrations (mol/L) of *n* types of substances;

<img src="https://latex.codecogs.com/gif.latex?\mathbf{N}=\begin{pmatrix}\nu_{11}&\nu_{12}&\cdots&\nu_{1n}\\\nu_{21}&\nu_{22}&\cdots&\nu_{2n}\\\vdots&\vdots&\ddots&\vdots\\\nu_{m1}&\nu_{m2}&\cdots&\nu_{mn}\\\end{pmatrix}"> are coefficients of *m* chemical reactions (negative for reagents, positive for products, and zero if the substance is not related to the reaction);

<img src="https://latex.codecogs.com/gif.latex?\mathbf{X}=\begin{pmatrix}x_1\\x_2\\\vdots\\x_m\end{pmatrix}"> are amounts of reactions (concentration changes for each reaction);

<img src="https://latex.codecogs.com/gif.latex?\mathbf{Y}=\begin{pmatrix}y_1\\y_2\\\vdots\\y_n\end{pmatrix}"> are final (equilibrium state) concentrations;

<img src="https://latex.codecogs.com/gif.latex?\mathbf{K}=\begin{pmatrix}k_1\\k_2\\\vdots\\k_m\end{pmatrix}"> are equilibrium constants for each reaction.

I need to solve **X** (*m* variables) and **Y** (*n* variables) by given **C**, **N** and **K**, either analytic or numeric solutions.

### Example

0.1 mol/L ammonia solution, we have 2 equilibria:

*(A)* H<sub>2</sub>O ↽⇀ H<sup>+</sup> + OH<sup>-</sup> (concentration of H<sub>2</sub>O is not considered)

*(B)* NH<sub>3</sub> + H<sub>2</sub>O ↽⇀ NH<sub>4</sub><sup>+</sup> + OH<sup>-</sup> (concentration of H<sub>2</sub>O is not considered)

Equilibrium constants:

 - k<sub>A</sub> = \[H<sup>+</sup>][OH<sup>−</sup>] = 10<sup>-14</sup>
 - k<sub>B</sub> = \[NH<sub>4</sub><sup>+</sup>][OH<sup>−</sup>]/[NH<sub>3</sub>] = 1.77x10<sup>−5</sup>

 So we have 2 reactions (*A* and *B*) and 4 substances (H<sup>+</sup>, OH<sup>−</sup>, NH<sub>3</sub> and NH<sub>4</sub><sup>+</sup>), and known values are:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{C}=\begin{pmatrix}c_\text{H+}\\c_\text{OH-}\\c_\text{NH3}\\c_\text{NH4+}\end{pmatrix}=\begin{pmatrix}0\\0\\0.1\\0\end{pmatrix}">

<img src="https://latex.codecogs.com/gif.latex?\mathbf{N}=\begin{pmatrix}\nu_{\text{A},\text{H+}}&\nu_{\text{A},\text{OH-}}&0&0\\0&\nu_{\text{B},\text{OH-}}&\nu_{\text{B},\text{NH3}}&\nu_{\text{B},\text{NH4}}\end{pmatrix}=\begin{pmatrix}1&1&0&0\\0&1&-1&1\end{pmatrix}">

<img src="https://latex.codecogs.com/gif.latex?\mathbf{K}=\begin{pmatrix}k_A\\k_B\end{pmatrix}=\begin{pmatrix}10^{-14}\\1.77\times10^{-5}\end{pmatrix}">

The solutions are:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{X}=\begin{pmatrix}x_A\\x_B\end{pmatrix}=\begin{pmatrix}7.57\times10^{-12}\\1.32\times10^{-3}\end{pmatrix}">

<img src="https://latex.codecogs.com/gif.latex?\mathbf{Y}=\begin{pmatrix}y_\text{H+}\\y_\text{OH-}\\y_\text{NH3}\\y_\text{NH4+}\end{pmatrix}=\begin{pmatrix}7.57\times10^{-12}\\1.32\times10^{-3}\\0.0987\\1.32\times10^{-3}\end{pmatrix}">

Here I used the approximation of <img src="https://latex.codecogs.com/gif.latex?y_\text{OH-}=y_\text{NH4+}">, so just solved a quadratic equation.

But how can I solve a more complicated system like:

- H<sub>2</sub>O = H<sup>+</sup> + OH<sup>-</sup>
- NH<sub>3</sub> + H<sub>2</sub>O = NH<sub>4</sub><sup>+</sup> + OH<sup>-</sup>
- CO<sub>2</sub> + H<sub>2</sub>O = H<sup>+</sup> + HCO<sub>3</sub><sup>-</sup>
- HCO<sub>3</sub><sup>-</sup> = H<sup>+</sup> + CO<sub>3</sub><sup>2-</sup>

which includes 4 reactions and 7 substances?
