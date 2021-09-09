from sympy import *

def X(p1, p2, p3):
    return p1[0] - p2[0], p2[0] - p3[0]

def line_coef(p1, p2):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    return [simplify(y1 - y2), simplify(x2 - x1), simplify(x1 * y2 - x2 * y1)]

# https://en.wikipedia.org/wiki/Ceva%27s_theorem
# (AF/FB)*(BD/DC)*(CE/EA)=1 => AD, BE, CF are concurrent
# Put AB onto x-axis and C onto y-axis
a, b, c, d, e, f, x, y = symbols('a, b, c, d, e, f, x, y')
A, B, C, D, E, F = (a, 0), (b, 0), (0, c), (d, (1 - d / b) * c), (e, (1 - e / a) * c), (f, 0)
(AF, FB), (BD, DC), (CE, EA) = X(A, F, B), X(B, D, C), X(C, E, A)
F = (solve(Eq(simplify(AF * BD * CE - FB * DC * EA), 0), f)[0], 0)
print(Matrix([line_coef(A, D), line_coef(B, E), line_coef(C, F)]).det())