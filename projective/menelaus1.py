from sympy import *

def line(p1, p2):
    x1, y1, x2, y2, x3, y3 = x, y, p1[0], p1[1], p2[0], p2[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

def X(p1, p2, p3):
    return p1[0] - p2[0], p2[0] - p3[0]

# https://en.wikipedia.org/wiki/Menelaus%27s_theorem
# DEF are collinear => (AF/FB)*(BD/DC)*(CE/EA)=-1
# Put AB onto x-axis and C onto y-axis
a, b, c, g, h, x, y = symbols('a, b, c, g, h, x, y')
A, B, C = (a, 0), (b, 0), (0, c)
DEF = Eq(y, g * x + h)
D, E, F = intersect(DEF, line(B, C)), intersect(DEF, line(A, C)), intersect(DEF, line(A, B))
(AF, FB), (BD, DC), (CE, EA) = X(A, F, B), X(B, D, C), X(C, E, A)
print(simplify(AF * BD * CE + FB * DC * EA))