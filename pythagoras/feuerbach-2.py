from sympy import *

a, b, c, AC, BC = symbols('a, b, c, AC, BC', positive = True)
# a, b, c, AC, BC = 1, 1, sqrt(3), 2, 2
AC2 = a * a + c * c
BC2 = b * b + c * c
# All multiply "4*AC*BC*c", r^2s multiply "16*AC2*BC2*c"
x9 = (b - a)*AC*BC*c
y9 = (a*b + c**2)*AC*BC
r92 = (a**2*b**2 + a**2*c**2 + b**2*c**2 + c**4)*AC2*BC2
xi = (AC2*BC - AC*BC2 - 2*AC*BC*a + 2*AC*BC*b - AC*b**2 - AC*c**2 + BC*a**2 + BC*c**2)*c
yi = AC2*BC*b - AC2*b**2 - AC2*c**2 + AC*BC2*a - 2*AC*BC*a*b + 2*AC*BC*c**2 + AC*a*b**2 + AC*a*c**2 - BC2*a**2 - BC2*c**2 + BC*a**2*b + BC*b*c**2
ri2 = AC2**2*BC2*b**2 + AC2**2*BC2*c**2 - 2*AC2**2*BC*b**3 - 2*AC2**2*BC*b*c**2 + AC2**2*b**4 + 2*AC2**2*b**2*c**2 + AC2**2*c**4 + 2*AC2*AC*BC2*BC*a*b - 2*AC2*AC*BC2*BC*c**2 - 6*AC2*AC*BC2*a*b**2 - 2*AC2*AC*BC2*a*c**2 + 4*AC2*AC*BC2*b*c**2 + 6*AC2*AC*BC*a*b**3 + 6*AC2*AC*BC*a*b*c**2 - 2*AC2*AC*BC*b**2*c**2 - 2*AC2*AC*BC*c**4 - 2*AC2*AC*a*b**4 - 4*AC2*AC*a*b**2*c**2 - 2*AC2*AC*a*c**4 + AC2*BC2**2*a**2 + AC2*BC2**2*c**2 - 6*AC2*BC2*BC*a**2*b + 4*AC2*BC2*BC*a*c**2 - 2*AC2*BC2*BC*b*c**2 + 10*AC2*BC2*a**2*b**2 + 2*AC2*BC2*a**2*c**2 - 8*AC2*BC2*a*b*c**2 + 2*AC2*BC2*b**2*c**2 + 2*AC2*BC2*c**4 - 6*AC2*BC*a**2*b**3 - 6*AC2*BC*a**2*b*c**2 + 4*AC2*BC*a*b**2*c**2 + 4*AC2*BC*a*c**4 - 2*AC2*BC*b**3*c**2 - 2*AC2*BC*b*c**4 + AC2*a**2*b**4 + 2*AC2*a**2*b**2*c**2 + AC2*a**2*c**4 + AC2*b**4*c**2 + 2*AC2*b**2*c**4 + AC2*c**6 - 2*AC*BC2**2*a**3 - 2*AC*BC2**2*a*c**2 + 6*AC*BC2*BC*a**3*b - 2*AC*BC2*BC*a**2*c**2 + 6*AC*BC2*BC*a*b*c**2 - 2*AC*BC2*BC*c**4 - 6*AC*BC2*a**3*b**2 - 2*AC*BC2*a**3*c**2 + 4*AC*BC2*a**2*b*c**2 - 6*AC*BC2*a*b**2*c**2 - 2*AC*BC2*a*c**4 + 4*AC*BC2*b*c**4 + 2*AC*BC*a**3*b**3 + 2*AC*BC*a**3*b*c**2 - 2*AC*BC*a**2*b**2*c**2 - 2*AC*BC*a**2*c**4 + 2*AC*BC*a*b**3*c**2 + 2*AC*BC*a*b*c**4 - 2*AC*BC*b**2*c**4 - 2*AC*BC*c**6 + BC2**2*a**4 + 2*BC2**2*a**2*c**2 + BC2**2*c**4 - 2*BC2*BC*a**4*b - 4*BC2*BC*a**2*b*c**2 - 2*BC2*BC*b*c**4 + BC2*a**4*b**2 + BC2*a**4*c**2 + 2*BC2*a**2*b**2*c**2 + 2*BC2*a**2*c**4 + BC2*b**2*c**4 + BC2*c**6
xe = (-AC2*BC + AC*BC2 - 2*AC*BC*a + 2*AC*BC*b + AC*b**2 + AC*c**2 - BC*a**2 - BC*c**2)*c
ye = -AC2*BC*b - AC2*b**2 - AC2*c**2 - AC*BC2*a - 2*AC*BC*a*b + 2*AC*BC*c**2 - AC*a*b**2 - AC*a*c**2 - BC2*a**2 - BC2*c**2 - BC*a**2*b - BC*b*c**2
re2 = AC2**2*BC2*b**2 + AC2**2*BC2*c**2 + 2*AC2**2*BC*b**3 + 2*AC2**2*BC*b*c**2 + AC2**2*b**4 + 2*AC2**2*b**2*c**2 + AC2**2*c**4 + 2*AC2*AC*BC2*BC*a*b - 2*AC2*AC*BC2*BC*c**2 + 6*AC2*AC*BC2*a*b**2 + 2*AC2*AC*BC2*a*c**2 - 4*AC2*AC*BC2*b*c**2 + 6*AC2*AC*BC*a*b**3 + 6*AC2*AC*BC*a*b*c**2 - 2*AC2*AC*BC*b**2*c**2 - 2*AC2*AC*BC*c**4 + 2*AC2*AC*a*b**4 + 4*AC2*AC*a*b**2*c**2 + 2*AC2*AC*a*c**4 + AC2*BC2**2*a**2 + AC2*BC2**2*c**2 + 6*AC2*BC2*BC*a**2*b - 4*AC2*BC2*BC*a*c**2 + 2*AC2*BC2*BC*b*c**2 + 10*AC2*BC2*a**2*b**2 + 2*AC2*BC2*a**2*c**2 - 8*AC2*BC2*a*b*c**2 + 2*AC2*BC2*b**2*c**2 + 2*AC2*BC2*c**4 + 6*AC2*BC*a**2*b**3 + 6*AC2*BC*a**2*b*c**2 - 4*AC2*BC*a*b**2*c**2 - 4*AC2*BC*a*c**4 + 2*AC2*BC*b**3*c**2 + 2*AC2*BC*b*c**4 + AC2*a**2*b**4 + 2*AC2*a**2*b**2*c**2 + AC2*a**2*c**4 + AC2*b**4*c**2 + 2*AC2*b**2*c**4 + AC2*c**6 + 2*AC*BC2**2*a**3 + 2*AC*BC2**2*a*c**2 + 6*AC*BC2*BC*a**3*b - 2*AC*BC2*BC*a**2*c**2 + 6*AC*BC2*BC*a*b*c**2 - 2*AC*BC2*BC*c**4 + 6*AC*BC2*a**3*b**2 + 2*AC*BC2*a**3*c**2 - 4*AC*BC2*a**2*b*c**2 + 6*AC*BC2*a*b**2*c**2 + 2*AC*BC2*a*c**4 - 4*AC*BC2*b*c**4 + 2*AC*BC*a**3*b**3 + 2*AC*BC*a**3*b*c**2 - 2*AC*BC*a**2*b**2*c**2 - 2*AC*BC*a**2*c**4 + 2*AC*BC*a*b**3*c**2 + 2*AC*BC*a*b*c**4 - 2*AC*BC*b**2*c**4 - 2*AC*BC*c**6 + BC2**2*a**4 + 2*BC2**2*a**2*c**2 + BC2**2*c**4 + 2*BC2*BC*a**4*b + 4*BC2*BC*a**2*b*c**2 + 2*BC2*BC*b*c**4 + BC2*a**4*b**2 + BC2*a**4*c**2 + 2*BC2*a**2*b**2*c**2 + 2*BC2*a**2*c**4 + BC2*b**2*c**4 + BC2*c**6
print('x9 =', expand(x9))
print('y9 =', expand(y9))
print('r92 =', expand(r92))
print('xi =', expand(xi))
print('yi =', expand(yi))
print('ri2 =', expand(ri2))
print('xe =', expand(xe))
print('ye =', expand(ye))
print('re2 =', expand(re2))