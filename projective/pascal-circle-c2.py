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

def on_circle(circle_eq, P):
    x, y = symbols('x, y')
    return cancel(circle_eq.subs(x, P[0]).subs(y, P[1])) == 0

def main():
    # A hexagon ABCDEF inscribed in a unit circle
    # Prove 3 intersections of opposite edges (AB∩DE, BC∩EF, CD∩FA) are collinear
    a, b, c, d, e, f = symbols('a, b, c, d, e, f')
    A, B, C = (0, 0), (a, 0), (b, c)
    circle_eq = circle(A, B, C)
    print('Circle Equation:', circle_eq, '= 0')
    D, E, F = point_on_circle(circle_eq, d), point_on_circle(circle_eq, e), point_on_circle(circle_eq, f)
    print('D:', D)
    print('E:', E)
    print('F:', F)
    print('Is D on Circle?', on_circle(circle_eq, D))
    print('Is E on Circle?', on_circle(circle_eq, E))
    print('Is F on Circle?', on_circle(circle_eq, F))
    AB, BC, CD, DE, EF, FA = line(A, B), line(B, C), line(C, D), line(D, E), line(E, F), line(F, A)
    G, H, J = intersect(AB, DE), intersect(BC, EF), intersect(CD, FA)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear?', collinear(G, H, J))

if __name__ == '__main__':
    main()