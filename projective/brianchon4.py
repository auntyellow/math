from sympy import *

def point(t0):
    return cos(t0), sin(t0)

def line(t0):
    return Eq(x * cos(t0) + y * sin(t0), 1)

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

def line_coef(P1, P2):
    x1, y1, x2, y2 = P1[0], P1[1], P2[0], P2[1]
    return [simplify(y1 - y2), simplify(x2 - x1), simplify(x1 * y2 - x2 * y1)]

# A quadrilateral ABCD circumscribed about a unit circle with tangent points EFGH
# Prove 2 diagonals and 2 lines connecting to opposite tangent points (AC, BD, EG, FH) are concurrent
t1, t2, t3, t4, x, y = symbols('t1, t2, t3, t4, x, y')
E, F, G, H = point(t1), point(t2), point(t3), point(t4)
DA, AB, BC, CD = line(t1), line(t2), line(t3), line(t4)
A, B, C, D = intersect(DA, AB), intersect(AB, BC), intersect(BC, CD), intersect(CD, DA)
print(simplify(Matrix([line_coef(A, C), line_coef(E, G), line_coef(F, H)]).det()))
# AC, BE and DF are also concurrent
print(simplify(Matrix([line_coef(A, C), line_coef(B, E), line_coef(D, F)]).det()))