from sympy import *

def line(p1, p2):
    x1, y1, x2, y2, x3, y3 = x, y, p1[0], p1[1], p2[0], p2[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

def R(aa, bb, cc, dd, i):
    a, b, c, d = aa[i], bb[i], cc[i], dd[i]
    return simplify((a - c) * (b - d) / (a - d) / (b - c))

# https://imomath.com/index.php?options=334 (Theorem 7)
a, b, r, x, y = symbols('a, b, r, x, y')
A, B = (0, r / a), (b, r * a)
AB = line(A, B)
circle = Eq(x * x + y * y, r * r)
roots = solve([AB, circle], (x, y))
C, D = (roots[0][0], roots[0][1]), (roots[1][0], roots[1][1])
print(R(A, B, C, D, 0))
print(R(A, B, C, D, 1))