from sympy import *

def tangent(P):
    m = P[1] - k * P[0]
    k1, k2 = solve(Eq((b * m + 2 * c * k * m + d + e * k) ** 2, 4 * (a + b * k + c * k ** 2) * (c * m ** 2 + e * m + f)), k)
    return Eq(y, k1 * x + P[1] - k1 * P[0]), Eq(y, k2 * x + P[1] - k2 * P[0])

a, b, c, d, e, f, g, h, j, k, x, y = symbols('a, b, c, d, e, f, g, h, j, k, x, y')
A, C, E = (g, 0), (0, h), (0, j)
(AB, AF), (CD, BC), (EF, DE) = tangent(A), tangent(C), tangent(E)

print('AF:', AF)
print('AB:', AB)
print('BC:', BC)
print('CD:', CD)
print('DE:', DE)
print('EF:', EF)

subs = {a: 1, b: 0, c: 1, d: 0, e: 0, f: -1, g: 1.25, h: 1.25, j: -1.25}

print('AF:', N(AF, subs = subs))
print('AB:', N(AB, subs = subs))
print('BC:', N(BC, subs = subs))
print('CD:', N(CD, subs = subs))
print('DE:', N(DE, subs = subs))
print('EF:', N(EF, subs = subs))