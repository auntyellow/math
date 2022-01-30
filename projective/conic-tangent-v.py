from sympy import Matrix, factor, poly, symbols

def line(P1, P2):
    a, b, c, d, e, f = P1[0], P1[1], P1[2], P2[0], P2[1], P2[2]
    # | a b c |
    # | d e f |
    # | x y z |
    x, y, z = symbols('x, y, z')
    return (b*f - c*e)*x + (c*d - a*f)*y + (a*e - b*d)*z

def tangent(P):
    x0, y0, z0 = P[0], P[1], P[2]
    a, b, x, y, z = symbols('a, b, x, y, z')
    # result from pole-polar-v.py
    return (a*y0 - b*y0 + b*z0)*x + (a*x0 - a*z0 - b*x0)*y + (-a*y0 + b*x0)*z

def coeffs(expr):
    p = poly(expr, symbols('x, y, z'))
    return factor([p.nth(2, 0, 0)*2, p.nth(1, 1, 0), p.nth(0, 2, 0)*2, p.nth(1, 0, 1), p.nth(0, 1, 1), p.nth(0, 0, 2)*2])

def main():
    # This program shows why a conic can be represented as αβ=γ²,
    # where α=0 and β=0 are two tangent lines and γ=0 is the secant line passing through the two tangent points
    # see ISBN 9787542850393 §3.2
    a, b, x, y, z = symbols('a, b, x, y, z')
    A, B = (1, 0, 0), (0, 1, 0)
    # result from steiner-conic-v.py
    C0 = coeffs(a*x*y - a*y*z - b*x*y + b*x*z)
    C1 = coeffs(line(A, B)**2)
    C2 = coeffs(tangent(A)*tangent(B))
    print('αβ - γ²:', C0)
    print('αβ:', C1)
    print('γ²:', C2)
    mat = Matrix([C0, C1, C2])
    print('Rank(', mat, ') =', mat.rank())

if __name__ == '__main__':
    main()