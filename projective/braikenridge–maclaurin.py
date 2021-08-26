from sympy import *

def L(a, b):
    return Eq(y, a * x + b)

def intersect(L1, L2):
    P = solve([L1, L2], (x, y))
    return simplify(P[x]), simplify(P[y])

g, h, j, k, m, n, p, q, x, y = symbols('g, h, j, k, m, n, p, q, x, y')
AB, DE, BC, EF, AF, CD = L(j, g), L(k, g), L(m, h), L(n, h), L(p, 0), L(q, 0)
A, E, C = intersect(AB, AF), intersect(DE, EF), intersect(BC, CD)
D, B, F = intersect(CD, DE), intersect(AB, BC), intersect(AF, EF)

mat = []
for P in [A, B, C, D, E, F]:
    x, y = P[0], P[1]
    mat.append([x * x, x * y, y * y, x, y, 1])
print(Matrix(mat).det())