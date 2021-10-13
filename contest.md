Many contest geometry problems can be solved in analytic ways. Here are some examples.

### A circle divided into 8 regions

Let *K* be the point *K* in the interior of the unit circle. The circle is divided into 8 regions using four lines passing through *K* such that each two adjacent lines form an angle of 45°, as shown in the picture. Four of these regions are colored such that no two colored regions share more than one point. Prove that the area of the colored regions is exactly half the area of the circle. <sup>[1]</sup>

<img src="diagrams/duke-putman-2012-6-8.gif">

Areas can be calculated by integration. Cartesian coordinates may work but we need to divide this figures into too many pieces and calculate them one by one. Here we'd like to use polar coordinates.

Put *K* onto origin and rotate the diameter through *K* onto polar axis (x-axis), then the circle denoted in Cartesian coordinates:

<img src="https://latex.codecogs.com/gif.latex?(x-a)^2+y^2=r^2">

can be written in polar coordinates (just replace with <img src="https://latex.codecogs.com/gif.latex?x=\rho%20\cos\theta"> and <img src="https://latex.codecogs.com/gif.latex?y=\rho%20\sin\theta">):

<img src="https://latex.codecogs.com/gif.latex?\rho(\theta)=a\cos%20\theta\pm\sqrt{r^2-a^2\sin^2\theta}">

Either positive or negative root is okay.

The area of each part is:

<img src="https://latex.codecogs.com/gif.latex?A_i=\frac{1}{2}\int_{\theta_0+\frac{i}4\pi}^{\theta_0+\frac{i+1}4\pi}\rho(\theta)^2d\theta">

The result doesn't look analytic. Fortunately, the diagonal two parts can be calculated together because:

<img src="https://latex.codecogs.com/gif.latex?{A_i+A_{i+4}=\frac{1}{2}\left[\int_{\theta_0+\frac{i}4\pi}^{\theta_0+\frac{i+1}4\pi}\rho(\theta)^2d\theta+\int_{\theta_0+\frac{i+4}4\pi}^{\theta_0+\frac{i+5}4\pi}\rho(\theta)^2d\theta\right]=\frac{1}{2}\int_{\theta_0+\frac{i}4\pi}^{\theta_0+\frac{i+1}4\pi}\left[\rho(\theta)^2+\rho(\theta+\pi)^2\right]d\theta=\int_{\theta_0+\frac{i}4\pi}^{\theta_0+\frac{i+1}4\pi}\left[r^2+a^2(\cos^2\theta-sin^2\theta)\right]d\theta}">

After some calculations, we have:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}A_0+A_4=\frac{\pi%20r^2}4+\frac{1}{\sqrt{2}}a^2\cos(2\theta_0+\frac{\pi}4)\\A_1+A_5=\frac{\pi%20r^2}4-\frac{1}{\sqrt{2}}a^2\sin(2\theta_0+\frac{\pi}4)\\A_2+A_6=\frac{\pi%20r^2}4-\frac{1}{\sqrt{2}}a^2\cos(2\theta_0+\frac{\pi}4)\\A_3+A_7=\frac{\pi%20r^2}4+\frac{1}{\sqrt{2}}a^2\sin(2\theta_0+\frac{\pi}4)\end{cases}">

Finally, we get:

<img src="https://latex.codecogs.com/gif.latex?(A_0+A_4)+(A_2+A_6)=(A_1+A_5)+(A_3+A_7)=\frac{\pi%20r^2}2"> □

### Note

1. [Duke 2012 Putnam preparation, Homework 6: Geometry](https://imomath.com/index.php?options=586), Problem 8