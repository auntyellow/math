from sympy import *

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

def line(p1, p2):
    x1, y1, x2, y2, x3, y3 = x, y, p1[0], p1[1], p2[0], p2[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

# https://www.imomath.com/index.php?options=586 (Problem 7)
a, b, r, AC = symbols('a, b, r, AC', positive = True)
c, x, y = symbols('c, x, y')
A, B, C, O = (-a, 0), (0, 0), (b, c), (0, r)
P = (a * (a + b) / AC - a, a * c / AC)
r = solve(Eq((P[0] - O[0])**2 + (P[1] - O[1])**2, r**2), r)[0]
print('r =', r)

# AC^2=(a+b)^2+c^2
r = a*((a + b)**2 + c**2 - 2*AC*a - 2*AC*b + a**2 + 2*a*b + b**2 + c**2)/(2*AC*c)
BC, BP = line(B, C), line(B, P)
OH = Eq(y, r - b * x / c)
T = intersect(BP, OH)
print('T:', T)
M = intersect(BC, line(A, T))
print('M:', M)
print(simplify(B[0] + C[0] - 2 * M[0]))
# b*(AC**2 - a**2 - 2*a*b - b**2 - c**2)/(AC**2 - 2*AC*a - 2*AC*b + a**2 + 2*a*b + b**2 + c**2)
print(simplify(B[1] + C[1] - 2 * M[1]))
# c*(AC**2 - a**2 - 2*a*b - b**2 - c**2)/(AC**2 - 2*AC*a - 2*AC*b + a**2 + 2*a*b + b**2 + c**2)

# AC**2 - a**2 - 2*a*b - b**2 - c**2 = (a + b)**2 + c**2 - a**2 - 2*a*b - b**2 = 0