from sympy import *

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

def collinear(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

def line(p1, p2):
    return collinear((x, y), p1, p2)

a, b, c, d, e, f, g, h, x, y = symbols('a, b, c, d, e, f, g, h, x, y')
AC, DF, AF, CD = Eq(y, a * x + c), Eq(y, d * x + f), Eq(y, g * x), Eq(y, h * x)
A, C, D, F = intersect(AC, AF), intersect(AC, CD), intersect(DF, CD), intersect(DF, AF)
B = b, d * b + f
E = e, a * e + c
AB, BC, DE, EF = line(A, B), line(B, C), line(D, E), line(E, F)
G, K = intersect(AB, DE), intersect(BC, EF)
print(collinear((0, 0), G, K))