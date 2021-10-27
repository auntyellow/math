from sympy import expand, poly, simplify
from cartesian import *

def circle(P1, P2, P3):
    # return F(x, y) such that F(x, y) = 0 is the circle's equation
    D, E, F, x, y = symbols('D, E, F, x, y')
    circle_eq = Eq(x**2 + y**2 + D*x + E*y + F, 0)
    circle_eqs = []
    circle_eqs.append(circle_eq.subs(x, P1[0]).subs(y, P1[1]))
    circle_eqs.append(circle_eq.subs(x, P2[0]).subs(y, P2[1]))
    circle_eqs.append(circle_eq.subs(x, P3[0]).subs(y, P3[1]))
    s = solve(circle_eqs, (D, E, F))
    return x**2 + y**2 + s[D]*x + s[E]*y + s[F]

def on_circle(circle_eq, P):
    x, y = symbols('x, y')
    return cancel(circle_eq.subs(x, P[0]).subs(y, P[1])) == 0

def foot(P1, P2, P3):
    x, y = symbols('x, y')
    P1P2 = line(P1, P2)
    P3H = Eq((P1[0] - P2[0])*(x - P3[0]) + (P1[1] - P2[1])*(y - P3[1]), 0)
    return intersect(P1P2, P3H)

def main():
    # https://en.wikipedia.org/wiki/Simson_line
    a, b, c, d, x, y = symbols('a, b, c, d, x, y')
    A, B, C = (0, 0), (a, 0), (b, c)
    AB, AC, BC = line(A, B), line(A, C), line(B, C)
    circle_eq = circle(A, B, C)
    x0 = solve(circle_eq.subs(y, d*x)/x, x)[0]
    P = (x0, d*x0)
    print('P:', P)
    print('Are ABCP concyclic?', on_circle(circle_eq, P))
    D, E, F = foot(B, C, P), foot(C, A, P), foot(A, B, P)
    print('D:', D)
    print('E:', E)
    print('F:', F)
    print('Are DEF collinear?', collinear(D, E, F))

if __name__ == '__main__':
    main()