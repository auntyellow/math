from sympy import Eq, Matrix, cancel, fraction, poly, solve, symbols

def collinear(P1, P2, P3):
    (x1, y1), (x2, y2), (x3, y3) = P1, P2, P3
    return Eq(fraction(cancel(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3))[0], 0)

def line(P1, P2):
    return collinear(symbols('x, y'), P1, P2)

def intersect(L1, L2):
    x, y = symbols('x, y')
    p = solve([L1, L2], (x, y))
    return p[x], p[y]

def line_coef(L):
    p = poly(L.lhs - L.rhs, symbols('x, y'))
    return [p.nth(1, 0), p.nth(0, 1), p.nth(0, 0)]

def concurrency(L1, L2, L3):
    return Matrix([line_coef(L1), line_coef(L2), line_coef(L3)]).det()