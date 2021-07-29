Here is an elementary derivation (without calculus) of [Euler's formula](https://en.wikipedia.org/wiki/Euler's_formula) <img src="https://latex.codecogs.com/gif.latex?e^{ix}=\cos%20x+i\sin%20x">.

### Step 1

For any positive real number *y* ≠ 1 (e.g. *y* = 10), we have <img src="https://latex.codecogs.com/gif.latex?y^i=a+bi">, and we also have <img src="https://latex.codecogs.com/gif.latex?y^{-i}=a-bi">. <sup>[1]</sup>

Because <img src="https://latex.codecogs.com/gif.latex?1=y^i%20y^{-i}=(a+bi)(a-bi)=a^2+b^2">, there should be a real number *x* matching <img src="https://latex.codecogs.com/gif.latex?a=\cos%20x"> and <img src="https://latex.codecogs.com/gif.latex?b=\sin%20x">. Then we get <img src="https://latex.codecogs.com/gif.latex?y^i=\cos%20x+i\sin%20x">.

This also means, for any real number *x* ≠ 0, there should be a real number *y* matching <img src="https://latex.codecogs.com/gif.latex?y^i=\cos%20x+i\sin%20x">.

So we can get the real number <img src="https://latex.codecogs.com/gif.latex?e=y^{1/x}"> matching <img src="https://latex.codecogs.com/gif.latex?e^{i%20x}=y^i=\cos%20x+i\sin%20x">. (Although we don't know the exact value of *e* here, and *e* may be dependent on *x*.)

### Step 2

Make *x* = 1, we get <img src="https://latex.codecogs.com/gif.latex?e^i=\cos%201+i\sin%201">.

Then we generalize [de Moivre's formula](https://en.wikipedia.org/wiki/De_Moivre%27s_formula) <img src="https://latex.codecogs.com/gif.latex?(\cos\theta+i\sin\theta)^n=\cos%20n\theta+i\sin%20n\theta"> to non-integer powers <img src="https://latex.codecogs.com/gif.latex?(\cos\theta+i\sin\theta)^x=\cos%20x\theta+i\sin%20x\theta">. <sup>[2]</sup>

Make *θ* = 1, we get <img src="https://latex.codecogs.com/gif.latex?(\cos%201+i\sin%201)^x=\cos%20x+i\sin%20x">, and finally we get <img src="https://latex.codecogs.com/gif.latex?e^{ix}=\cos%20x+i\sin%20x">.

This means, the unique real number *e* (although we still don't know the exact value here) matches *x* = 1 and all other values.

### Notes

[1] Here we use a rule of [complex conjugate](https://en.wikipedia.org/wiki/Complex_conjugate):

> In general, if <img src="https://latex.codecogs.com/gif.latex?\varphi"> is a holomorphic function whose restriction to the real numbers is real-valued, and <img src="https://latex.codecogs.com/gif.latex?\varphi%20(z)"> and <img src="https://latex.codecogs.com/gif.latex?\varphi%20(\overline{z})"> are defined, then
>
> <img src="https://latex.codecogs.com/gif.latex?\varphi({\overline%20z})=\overline{\varphi(z)}">

This rule doesn't look elementary. However, we can accept it intuitively. According to the definition of imaginary number *i*<sup>2</sup> = −1, *i* can be replaced with -*i* in any equation, and vice versa.

[2] The generalization doesn't look elementary (may use some complex analysis) and may fail in some cases. See [here](https://en.wikipedia.org/wiki/De_Moivre%27s_formula#Failure_for_non-integer_powers,_and_generalization).