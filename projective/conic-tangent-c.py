from sympy import Matrix, Eq, cancel, factor, poly, solve, symbols

def on_conic(P):
    a, b, c, d, e, f = symbols('a, b, c, d, e, f')
    x, y = P[0], P[1]
    return cancel(a*x**2 + 2*b*x*y + c*y**2 + 2*d*x + 2*e*y + f) == 0

def tangent(P):
    x0, y0 = P[0], P[1]
    a, b, c, d, e, f, x, y = symbols('a, b, c, d, e, f, x, y')
    return (a*x0 + b*y0 + d)*x + (b*x0 + c*y0 + e)*y + (d*x0 + e*y0 + f)

def coeff_matrix(expr):
    p = poly(expr, symbols('x, y'))
    a, b, c, d, e, f = p.nth(2, 0), p.nth(1, 1), p.nth(0, 2), p.nth(1, 0), p.nth(0, 1), p.nth(0, 0)
    return Matrix([[a, b/2, d/2], [b/2, c, e/2], [d/2, e/2, f]])

def main():
    # This program shows why a conic can be represented as αβ=γ²,
    # where α=0 and β=0 are two tangent lines and γ=0 is the secant line passing through the two tangent points
    # see ISBN 9787542850393 §3.2
    a, b, c, d, e, f, g, h, j, x, y = symbols('a, b, c, d, e, f, g, h, j, x, y')
    conic = a*x**2 + 2*b*x*y + c*y**2 + 2*d*x + 2*e*y + f
    secant = g*x + h*y + j
    m1 = coeff_matrix(secant*secant)
    y0 = solve(Eq(secant, 0), y)[0]
    x0 = solve(Eq(conic.subs(y, y0), 0), x)
    x1, x2 = x0[0], x0[1]
    P1, P2 = (x1, y0.subs(x, x1)), (x2, y0.subs(x, x2))
    print('Is P1 on conic?', on_conic(P1))
    print('Is P2 on conic?', on_conic(P2))
    m2 = coeff_matrix(tangent(P1)*tangent(P2))
    print(m1)
    print(m2)
    print('a =', factor(m2[0, 0]))
    print('b =', factor(m2[0, 1]))
    print('c =', factor(m2[1, 1]))
    print('d =', factor(m2[0, 2]))
    print('e =', factor(m2[1, 2]))
    print('f =', factor(m2[2, 2]))

if __name__ == '__main__':
    main()