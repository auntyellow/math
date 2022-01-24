from sympy import Eq, solve, symbols
from homogeneous import *

def subs_all(P, subs):
    return reduced(P[0].subs(subs), P[1].subs(subs), P[2].subs(subs))

def lies_on(P, L):
    return expand(P[0]*L[0] + P[1]*L[1] + P[2]*L[2]) == 0

def on_conic(P):
    a, b, c, d, e, f = symbols('a, b, c, d, e, f')
    x, y, z = P[0], P[1], P[2]
    return a*x**2 + 2*b*x*y + c*y**2 + 2*d*x*z + 2*e*y*z + f*z**2

def main():
    s, t, x0, y0, z0, x1, y1, z1, x2, y2, z2 = symbols('s, t, x0, y0, z0, x1, y1, z1, x2, y2, z2')
    P, P1 = (x0, y0, z0), (x1, y1, z1)
    M = span(1, P, s, P1)
    s = solve(Eq(on_conic(M), 0), s)
    M, N = span(1, P, s[0], P1), span(1, P, s[1], P1)
    print('M:', M)
    print('N:', N)
    Q = span(1, P, t, P1)
    t = fraction(cancel(solve(Eq(cross_ratio(P, Q, M, N), -1), t)[0]))
    Q = span(t[1], P, t[0], P1)
    print('Q:', Q)
    p = cross(Q, subs_all(Q, [(x1, x2), (y1, y2), (z1, z2)]))
    print('P\'s Polar:', p)
    q = subs_all(p, [(x0, x2), (y0, y2), (z0, z2), (x2, Q[0]), (y2, Q[1]), (z2, Q[2])])
    print('Q\'s Polar:', q)
    print('Is P on Q\'s Polar?', lies_on(P, q))

if __name__ == '__main__':
    main()