from sympy import Eq, Matrix, cancel, fraction, lcm_list, poly, solve, symbols

def on_conic(P):
    a, b, c, d, e, f = symbols('a, b, c, d, e, f')
    x, y = P[0], P[1]
    return cancel(a*x**2 + 2*b*x*y + c*y**2 + 2*d*x + 2*e*y + f) == 0

def tangent(P):
    x0, y0 = P[0], P[1]
    a, b, c, d, e, f, x, y = symbols('a, b, c, d, e, f, x, y')
    return (a*x0 + b*y0 + d)*x + (b*x0 + c*y0 + e)*y + (d*x0 + e*y0 + f)

def coeffs(expr):
    p = poly(expr, symbols('x, y'))
    a, c, f = fraction(cancel(p.nth(2, 0))), fraction(cancel(p.nth(0, 2))), fraction(cancel(p.nth(0, 0)))
    b, d, e = fraction(cancel(p.nth(1, 1)/2)), fraction(cancel(p.nth(1, 0)/2)), fraction(cancel(p.nth(0, 1)/2))
    lcd = lcm_list([a[1], b[1], c[1], d[1], e[1], f[1]])
    return [a[0]*cancel(lcd/a[1]), b[0]*cancel(lcd/b[1]), c[0]*cancel(lcd/c[1]), d[0]*cancel(lcd/d[1]), e[0]*cancel(lcd/e[1]), f[0]*cancel(lcd/f[1])]

def main():
    # This program shows why a conic can be represented as αβ=γ²,
    # where α=0 and β=0 are two tangent lines and γ=0 is the secant line passing through the two tangent points
    # see ISBN 9787542850393 §3.2
    a, b, c, d, e, f, g, h, j, x, y = symbols('a, b, c, d, e, f, g, h, j, x, y')
    conic = a*x**2 + 2*b*x*y + c*y**2 + 2*d*x + 2*e*y + f
    secant = g*x + h*y + j
    y0 = solve(Eq(secant, 0), y)[0]
    x0 = solve(Eq(conic.subs(y, y0), 0), x)
    x1, x2 = x0[0], x0[1]
    P1, P2 = (x1, y0.subs(x, x1)), (x2, y0.subs(x, x2))
    print('Is P1 on conic?', on_conic(P1))
    print('Is P2 on conic?', on_conic(P2))
    C1 = coeffs(secant**2)
    C2 = coeffs(tangent(P1)*tangent(P2))
    print('γ²:', C1)
    print('αβ:', C2)
    mat = Matrix([[a, b, c, d, e, f], C1, C2])
    print('Rank(', mat, ') =', mat.rank())

if __name__ == '__main__':
    main()