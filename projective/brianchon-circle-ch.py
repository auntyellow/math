from sympy import poly
from cartesian import *
from homogeneous import *

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

def tangent(circle_eq, P):
    x, y = symbols('x, y')
    circle_poly = poly(circle_eq, (x, y))
    d, e, f = circle_poly.nth(1, 0)/2, circle_poly.nth(0, 1)/2, circle_poly.nth(0, 0)
    x0, y0 = P[0], P[1]
    return Eq((x0 + d)*x + (y0 + e)*y + (d*x0 + e*y0 + f), 0)

def main():
    # A hexagon ABCDEF circumscribed about a unit circle with tangent points (a, b), ..., (m, n)
    # Prove 3 principal diagonals (AD, BE, CF) are concurrent
    a, b, c, d, e, f = symbols('a, b, c, d, e, f')
    ab, bc, cd = (0, 0), (0, a), (b, c)
    circle_eq = circle(ab, bc, cd)
    de, ef, fa = point_on_circle(circle_eq, d), point_on_circle(circle_eq, e), point_on_circle(circle_eq, f)
    AB, BC, CD = tangent(circle_eq, ab), tangent(circle_eq, bc), tangent(circle_eq, cd)
    DE, EF, FA = tangent(circle_eq, de), tangent(circle_eq, ef), tangent(circle_eq, fa)
    A, B, C = intersect(FA, AB), intersect(AB, BC), intersect(BC, CD)
    D, E, F = intersect(CD, DE), intersect(DE, EF), intersect(EF, FA)
    A = to_homogeneous(A)
    B = to_homogeneous(B)
    C = to_homogeneous(C)
    D = to_homogeneous(D)
    E = to_homogeneous(E)
    F = to_homogeneous(F)
    print('A:', A)
    print('B:', B)
    print('C:', C)
    print('D:', D)
    print('E:', E)
    print('F:', F)
    # Cartesian is too slow
    # print('Are AD, BE and CF concurrent?', concurrency(A, D, B, E, C, F) == 0)
    print('Are AD, BE and CF concurrent?', incidence(cross(A, D), cross(B, E), cross(C, F)) == 0)

if __name__ == '__main__':
    main()