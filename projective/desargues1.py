from sympy import *

def L(a, b):
    return Eq(y, a * x + b)

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return p[x], p[y]

def line_coef(P1, P2):
    x1, y1, x2, y2 = P1[0], P1[1], P2[0], P2[1]
    return [simplify(y1 - y2), simplify(x2 - x1), simplify(x1 * y2 - x2 * y1)]

e, f, g, h, j, k, m, n, x, y = symbols('e, f, g, h, j, k, m, n, x, y')
A1B1, A2B2, A1C1, A2C2, B1C1, B2C2 = L(g, 0), L(h, 0), L(j, e), L(k, e), L(m, f), L(n, f)
A1, A2 = intersect(A1B1, A1C1), intersect(A2B2, A2C2)
B1, B2 = intersect(A1B1, B1C1), intersect(A2B2, B2C2)
C1, C2 = intersect(A1C1, B1C1), intersect(A2C2, B2C2)
print("A1:", A1)
print("A2:", A2)
print("B1:", B1)
print("B2:", B2)
print("C1:", C1)
print("C2:", C2)
print(Matrix([line_coef(A1, A2), line_coef(B1, B2), line_coef(C1, C2)]).det())