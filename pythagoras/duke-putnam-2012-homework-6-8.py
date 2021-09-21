from sympy import *

# https://www.imomath.com/index.php?options=586 (Problem 8)
a, r = symbols('a, r', positive = True)
theta, t = symbols('theta, t')
rho2 = a**2*(cos(theta)**2 - sin(theta)**2) + r**2
S1 = integrate(rho2, (theta, t, t + pi / 4))
S2 = integrate(rho2, (theta, t + pi / 4, t + pi / 2))
S3 = integrate(rho2, (theta, t + pi / 2, t + 3 * pi / 4))
S4 = integrate(rho2, (theta, t + 3 * pi / 4, t + pi))
print(simplify(S1 + S3))
print(simplify(S2 + S4))