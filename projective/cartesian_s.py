from sympy import Eq, Matrix, simplify, solve, symbols

def collinear(P1, P2, P3):
    x1, y1, x2, y2, x3, y3 = P1[0], P1[1], P2[0], P2[1], P3[0], P3[1]
    return Eq(simplify(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3), 0)

def line(P1, P2):
    x, y = symbols('x, y')
    return collinear((x, y), P1, P2)

def intersect(L1, L2):
    x, y = symbols('x, y')
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

def line_coef(P1, P2):
    x1, y1, x2, y2 = P1[0], P1[1], P2[0], P2[1]
    return [simplify(y1 - y2), simplify(x2 - x1), simplify(x1*y2 - x2*y1)]

def concurrency(P1, P2, P3, P4, P5, P6):
    return simplify(Matrix([line_coef(P1, P2), line_coef(P3, P4), line_coef(P5, P6)]).det())

def cross_ratio(a, b, c, d):
    return simplify((a - c)*(b - d)/(a - d)/(b - c))