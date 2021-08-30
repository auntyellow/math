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
print('A:', A)
print('B:', B)
print('C:', C)
print('D:', D)
print('E:', E)
print('F:', F)

points = [A, B, C, D, E, F]
denominators = [j - p, j - m, q - m, q - k, k - n, p - n]
coefficients = [x * x, x * y, y * y, x, y, 1]
subs = {}
mat = []
for s in range(6):
    row = []
    denominator = denominators[s] ** 2
    subs_xy = {}
    subs_xy[x] = points[s][0]
    subs_xy[y] = points[s][1]
    for t in range(6):
        rst = symbols('r' + str(s) + str(t))
        subs[rst] = expand(simplify(N(coefficients[t] * denominator, subs = subs_xy)))
        row.append(rst)
    mat.append(row)
print('M =', N(Matrix(mat), subs = subs))
print('det M =', expand(N(Matrix(mat).det(), subs = subs)))