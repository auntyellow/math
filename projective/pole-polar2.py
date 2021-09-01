from sympy import *

def line(p1, p2):
    x1, y1, x2, y2, x3, y3 = x, y, p1[0], p1[1], p2[0], p2[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

def R(aa, bb, cc, dd):
    return simplify((aa - cc) * (bb - dd) / (aa - dd) / (bb - cc))

# https://imomath.com/index.php?options=334 (Theorem 7)
# (A,B;C,D)=-1 => A(0,a1) and B(b,a) are conjugated, i.e. a1=1/a
a, b, a1, x, y = symbols('a, a1, h, x, y')
A, B = (0, a1), (b, a)
AB = line(A, B)
circle = Eq(x * x + y * y, 1)
roots = solve([AB, circle], (x, y))
C, D = roots[0], roots[1]
print(solve(Eq(R(A[0], B[0], C[0], D[0]), -1), a1))