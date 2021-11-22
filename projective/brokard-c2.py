from sympy import poly
from cartesian import *

def circle(P1, P2, P3):
    # return F(x, y) such that F(x, y) = 0 is the circle's equation
    d, e, f, x, y = symbols('d, e, f, x, y')
    circle_eq = Eq(x**2 + y**2 + d*x + e*y + f, 0)
    circle_eqs = []
    circle_eqs.append(circle_eq.subs(x, P1[0]).subs(y, P1[1]))
    circle_eqs.append(circle_eq.subs(x, P2[0]).subs(y, P2[1]))
    circle_eqs.append(circle_eq.subs(x, P3[0]).subs(y, P3[1]))
    s = solve(circle_eqs, (d, e, f))
    return x**2 + y**2 + s[d]*x + s[e]*y + s[f]

def point_on_circle(circle_eq, slope):
    x, y = symbols('x, y')
    x0 = solve(Eq(circle_eq.subs(y, slope*x)/x, 0), x)[0]
    return x0, slope*x0

def center(circle_eq):
    x, y = symbols('x, y')
    return cancel(-poly(circle_eq, x).nth(1)/2), cancel(-poly(circle_eq, y).nth(1)/2)

def perpendicular(P1, P2, P3, P4):
    x1, y1, x2, y2, x3, y3, x4, y4 = P1[0], P1[1], P2[0], P2[1], P3[0], P3[1], P4[0], P4[1]
    return cancel((x1 - x2)*(x3 - x4) + (y1 - y2)*(y3 - y4)) == 0

def main():
    # https://imomath.com/index.cgi?page=polePolarBrianchonBrokard (Theorem 9)
    a, b, c, d, e, f, g, h = symbols('a, b, c, d, e, f, g, h')
    A, B, C = (0, 0), (a, 0), (b, c)
    circle_eq = circle(A, B, C)
    D = point_on_circle(circle_eq, d)
    O = center(circle_eq)
    print('O:', O)
    AB, AC, AD, BC, BD, CD = line(A, B), line(A, C), line(A, D), line(B, C), line(B, D), line(C, D)
    E, F, G = intersect(AB, CD), intersect(AD, BC), intersect(AC, BD)
    print('E:', E)
    print('F:', F)
    print('G:', G)
    print('Is EF perpendicular to OG?', perpendicular(E, F, G, O))
    print('Is FG perpendicular to OE?', perpendicular(F, G, E, O))
    print('Is GE perpendicular to OF?', perpendicular(G, E, F, O))

if __name__ == '__main__':
    main()