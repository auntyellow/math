from sympy import *

a, b, c, AC, BC = symbols('a, b, c, AC, BC', positive = True)
# a, b, c, AC, BC = 1, 1, sqrt(3), 2, 2
x9 = -AC*BC*a*c + AC*BC*b*c
y9 = AC*BC*a*b + AC*BC*c**2
r92 = a**4*b**4 + 2*a**4*b**2*c**2 + a**4*c**4 + 2*a**2*b**4*c**2 + 4*a**2*b**2*c**4 + 2*a**2*c**6 + b**4*c**4 + 2*b**2*c**6 + c**8
xi = -2*AC*BC*a*c + 2*AC*BC*b*c - 2*AC*b**2*c - 2*AC*c**3 + 2*BC*a**2*c + 2*BC*c**3
yi = -2*AC*BC*a*b + 2*AC*BC*c**2 + 2*AC*a*b**2 + 2*AC*a*c**2 + 2*BC*a**2*b + 2*BC*b*c**2 - 2*a**2*b**2 - 2*a**2*c**2 - 2*b**2*c**2 - 2*c**4
ri2 = 16*AC*BC*a**3*b**3 + 16*AC*BC*a**3*b*c**2 - 8*AC*BC*a**2*b**2*c**2 - 8*AC*BC*a**2*c**4 + 16*AC*BC*a*b**3*c**2 + 16*AC*BC*a*b*c**4 - 8*AC*BC*b**2*c**4 - 8*AC*BC*c**6 - 16*AC*a**3*b**4 - 24*AC*a**3*b**2*c**2 - 8*AC*a**3*c**4 + 8*AC*a**2*b**3*c**2 + 8*AC*a**2*b*c**4 - 16*AC*a*b**4*c**2 - 24*AC*a*b**2*c**4 - 8*AC*a*c**6 + 8*AC*b**3*c**4 + 8*AC*b*c**6 - 16*BC*a**4*b**3 - 16*BC*a**4*b*c**2 + 8*BC*a**3*b**2*c**2 + 8*BC*a**3*c**4 - 24*BC*a**2*b**3*c**2 - 24*BC*a**2*b*c**4 + 8*BC*a*b**2*c**4 + 8*BC*a*c**6 - 8*BC*b**3*c**4 - 8*BC*b*c**6 + 16*a**4*b**4 + 24*a**4*b**2*c**2 + 8*a**4*c**4 - 8*a**3*b**3*c**2 - 8*a**3*b*c**4 + 24*a**2*b**4*c**2 + 40*a**2*b**2*c**4 + 16*a**2*c**6 - 8*a*b**3*c**4 - 8*a*b*c**6 + 8*b**4*c**4 + 16*b**2*c**6 + 8*c**8
xe = -2*AC*BC*a*c + 2*AC*BC*b*c + 2*AC*b**2*c + 2*AC*c**3 - 2*BC*a**2*c - 2*BC*c**3
ye = -2*AC*BC*a*b + 2*AC*BC*c**2 - 2*AC*a*b**2 - 2*AC*a*c**2 - 2*BC*a**2*b - 2*BC*b*c**2 - 2*a**2*b**2 - 2*a**2*c**2 - 2*b**2*c**2 - 2*c**4
re2 = 16*AC*BC*a**3*b**3 + 16*AC*BC*a**3*b*c**2 - 8*AC*BC*a**2*b**2*c**2 - 8*AC*BC*a**2*c**4 + 16*AC*BC*a*b**3*c**2 + 16*AC*BC*a*b*c**4 - 8*AC*BC*b**2*c**4 - 8*AC*BC*c**6 + 16*AC*a**3*b**4 + 24*AC*a**3*b**2*c**2 + 8*AC*a**3*c**4 - 8*AC*a**2*b**3*c**2 - 8*AC*a**2*b*c**4 + 16*AC*a*b**4*c**2 + 24*AC*a*b**2*c**4 + 8*AC*a*c**6 - 8*AC*b**3*c**4 - 8*AC*b*c**6 + 16*BC*a**4*b**3 + 16*BC*a**4*b*c**2 - 8*BC*a**3*b**2*c**2 - 8*BC*a**3*c**4 + 24*BC*a**2*b**3*c**2 + 24*BC*a**2*b*c**4 - 8*BC*a*b**2*c**4 - 8*BC*a*c**6 + 8*BC*b**3*c**4 + 8*BC*b*c**6 + 16*a**4*b**4 + 24*a**4*b**2*c**2 + 8*a**4*c**4 - 8*a**3*b**3*c**2 - 8*a**3*b*c**4 + 24*a**2*b**4*c**2 + 40*a**2*b**2*c**4 + 16*a**2*c**6 - 8*a*b**3*c**4 - 8*a*b*c**6 + 8*b**4*c**4 + 16*b**2*c**6 + 8*c**8

# (r9 - ri)^2 = (x9 - xi)^2 + (y9 - yi)^2 => [r9^2 + ri^2 - (x9 - xi)^2 - (y9 - yi)^2]^2 = 4*r9^2*ri^2
print('Detect if Nine-Point Circle tangents Incircle:')
print(expand((r92 + ri2 - (x9 - xi)**2 - (y9 - yi)**2)**2 - 4 * r92 * ri2))
# (r9 + re)^2 = (x9 - xi)^2 + (y9 - yi)^2 => [r9^2 + re^2 - (x9 - xe)^2 - (y9 - ye)^2]^2 = 4*r9^2*re^2
print('Detect if Nine-Point Circle tangents Excircle:')
print(expand((r92 + re2 - (x9 - xe)**2 - (y9 - ye)**2)**2 - 4 * r92 * re2))