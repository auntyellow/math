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
    return a[0]*cancel(lcd/a[1]), b[0]*cancel(lcd/b[1]), c[0]*cancel(lcd/c[1]), d[0]*cancel(lcd/d[1]), e[0]*cancel(lcd/e[1]), f[0]*cancel(lcd/f[1])

def collinear(Q0, Q1, Q2, i, j, k):
    return Matrix([[Q0[i], Q0[j], Q0[k]], [Q1[i], Q1[j], Q1[k]], [Q2[i], Q2[j], Q2[k]]]).det() == 0

def main():
    # This program shows why a conic can be represented as αβ=γ²,
    # where α=0 and β=0 are two tangent lines and γ=0 is the secant line passing through the two tangent points
    # see ISBN 9787542850393 §3.2
    a, b, c, d, e, f, g, h, j, x, y = symbols('a, b, c, d, e, f, g, h, j, x, y')
    Q0 = (a, b, c, d, e, f)
    conic = a*x**2 + 2*b*x*y + c*y**2 + 2*d*x + 2*e*y + f
    secant = g*x + h*y + j
    Q1 = coeffs(secant**2)
    y0 = solve(Eq(secant, 0), y)[0]
    x0 = solve(Eq(conic.subs(y, y0), 0), x)
    x1, x2 = x0[0], x0[1]
    P1, P2 = (x1, y0.subs(x, x1)), (x2, y0.subs(x, x2))
    print('Is P1 on conic?', on_conic(P1))
    print('Is P2 on conic?', on_conic(P2))
    Q2 = coeffs(tangent(P1)*tangent(P2))
    print("αβ - γ² =", Q0)
    print("γ² =", Q1)
    print("αβ =", Q2)
    print("Are abc collinear?", collinear(Q0, Q1, Q2, 0, 1, 2))
    print("Are abd collinear?", collinear(Q0, Q1, Q2, 0, 1, 3))
    print("Are acf collinear?", collinear(Q0, Q1, Q2, 0, 2, 5))
    print("Are adf collinear?", collinear(Q0, Q1, Q2, 0, 3, 5))
    print("Are bce collinear?", collinear(Q0, Q1, Q2, 1, 2, 4))
    print("Are bde collinear?", collinear(Q0, Q1, Q2, 1, 3, 4))
    print("Are cef collinear?", collinear(Q0, Q1, Q2, 2, 4, 5))
    print("Are def collinear?", collinear(Q0, Q1, Q2, 3, 4, 5))

if __name__ == '__main__':
    main()