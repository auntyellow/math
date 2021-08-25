from sympy import *

def collinear(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

def line(p1, p2):
    return collinear((x, y), p1, p2)

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return p[x], p[y]

e, f, g, h, j, k, m, n, x, y = symbols('e, f, g, h, j, k, m, n, x, y')
A1, A2, B1, B2, C1, C2 = (g, 0), (h, 0), (j, e * j), (k, e * k), (m, f * m), (n, f * n)
A1B1, A1C1, B1C1, A2B2, A2C2, B2C2 = line(A1, B1), line(A1, C1), line(B1, C1), line(A2, B2), line(A2, C2), line(B2, C2)
ab, ac, bc = intersect(A1B1, A2B2), intersect(A1C1, A2C2), intersect(B1C1, B2C2)
print("ab:", ab)
print("ac:", ac)
print("bc:", bc)
print(collinear(ab, ac, bc))