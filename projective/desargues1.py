from sympy import *

def L(a, b):
    return Eq(y, a * x + b)

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return p[x], p[y]

def collinear(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

def line(p1, p2):
    return collinear((x, y), p1, p2)

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
A1A2, B1B2, C1C2 = line(A1, A2), line(B1, B2), line(C1, C2)
O1, O2, O3 = intersect(A1A2, B1B2), intersect(A1A2, C1C2), intersect(B1B2, C1C2)
print(O1)
print(O2)
print(O3)
print(collinear(O1, O2, O3))