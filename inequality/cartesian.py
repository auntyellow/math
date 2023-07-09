from sympy import Eq, Matrix, cancel, fraction, solve, symbols

def collinear(P1, P2, P3):
    (x1, y1), (x2, y2), (x3, y3) = P1, P2, P3
    return Eq(fraction(cancel(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3))[0], 0)

def line(P1, P2):
    return collinear(symbols('x, y'), P1, P2)

def intersect(L1, L2):
    x, y = symbols('x, y')
    p = solve([L1, L2], (x, y))
    return p[x], p[y]

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2