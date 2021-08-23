from sympy import *

def pair(func):
    p = solve([conic, Eq(y, func)], (x, y))
    return (simplify(p[0][0]), simplify(p[0][1])), (simplify(p[1][0]), simplify(p[1][1]))

def line(p1, p2):
    x1, y1, x2, y2, x3, y3 = x, y, p1[0], p1[1], p2[0], p2[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

a, b, c, d, e, f, g, h, k, x, y = symbols('a, b, c, d, e, f, g, h, k, x, y')
conic = Eq(a * x * x + b * x * y + c * y * y + d * x + e * y + f, 0)
F, A = pair(g * x)
D, C = pair(h * x)
B, E = pair(k)

print('x_A =', A[0])
print('x_B =', B[0])
print('x_C =', C[0])
print('x_D =', D[0])
print('x_E =', E[0])
print('x_F =', F[0])

subs = {a: 1, b: 0, c: 1, d: 0, e: 0, f: -1, g: 1, h: -1, k: 0}

print('x_A =', N(A[0], subs = subs))
print('x_B =', N(B[0], subs = subs))
print('x_C =', N(C[0], subs = subs))
print('x_D =', N(D[0], subs = subs))
print('x_E =', N(E[0], subs = subs))
print('x_F =', N(F[0], subs = subs))