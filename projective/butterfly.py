from sympy import *

def pair(func):
    p = solve([conic, Eq(y, func)], (x, y))
    return (simplify(p[0][0]), simplify(p[0][1])), (simplify(p[1][0]), simplify(p[1][1]))

def line(p1, p2):
    x1, y1, x2, y2, x3, y3 = x, y, p1[0], p1[1], p2[0], p2[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

a, b, c, d, e, f, q, r, x, y = symbols('a, b, c, d, e, f, q, r, x, y')
conic = Eq(a * x * x + b * x * y + c * y * y + d * x + e * y + f, 0)
A, B = pair(0)
P, Q = pair(q * x)
R, S = pair(r * x)
AB = Eq(y, 0)
PS, QR = line(P, S), line(Q, R)
C, D = intersect(AB, PS), intersect(AB, QR)
print(simplify(1 / A[0] + 1 / B[0]))
print(simplify(1 / C[0] + 1 / D[0]))