from sympy import *

def line(t0):
    return Eq(x * cos(t0) + y * sin(t0), 1)

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

def line_coef(P1, P2):
    x1, y1, x2, y2 = P1[0], P1[1], P2[0], P2[1]
    return [simplify(y1 - y2), simplify(x2 - x1), simplify(x1 * y2 - x2 * y1)]

t1, t2, t3, t4, t5, t6, x, y = symbols('t1, t2, t3, t4, t5, t6, x, y')
AB, BC, CD, DE, EF, FA = line(t1), line(t2), line(t3), line(t4), line(t5), line(t6)
A, B, C = intersect(FA, AB), intersect(AB, BC), intersect(BC, CD)
D, E, F = intersect(CD, DE), intersect(DE, EF), intersect(EF, FA)

print('A:', A)
print('B:', B)
print('C:', C)
print('D:', D)
print('E:', E)
print('F:', F)
print(simplify(Matrix([line_coef(A, D), line_coef(B, E), line_coef(C, F)]).det()))