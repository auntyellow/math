from sympy import Eq, solve, symbols
from homogeneous import *

def point_subs(P, t, u):
    return P[0].subs(t, u), P[1].subs(t, u), P[2].subs(t, u)

def lies_on(P, L):
    return expand(P[0]*L[0] + P[1]*L[1] + P[2]*L[2]) == 0

def main():
    a, b, c, d, e, s, t, u, v, w = symbols('a, b, c, d, e, s, t, u, v, w')
    # results from steiner-conic-v.py
    P, M, N = (c, d, e), (t*(a + t), t*(b + t), (a + t)*(b + t)), (u*(a + u), u*(b + u), (a + u)*(b + u))
    u = solve(Eq(incidence(P, M, N), 0), u)
    u = u[1] if u[0] == t else u[0]
    N = multiplied(u*(a + u), u*(b + u), (a + u)*(b + u))
    print('N:', N)
    Q = span(1, M, v, P)
    v = fraction(cancel(solve(Eq(cross_ratio(P, Q, M, N), -1), v)[0]))
    Q = span(v[1], M, v[0], P)
    print('Q:', Q)
    polarP = cross(Q, point_subs(Q, t, w))
    print('P\'s Polar:', polarP)
    R = span(s, point_subs(Q, t, 0), 1, point_subs(Q, t, 1))
    print('R on P\'s Polar:', R)
    print('Is R on P\'s Polar?', lies_on(R, polarP))
    cc, dd, ee = symbols('cc, dd, ee')
    subs = [(c, cc), (d, dd), (e, ee), (cc, R[0]), (dd, R[1]), (ee, R[2])]
    polarR = reduced(polarP[0].subs(subs), polarP[1].subs(subs), polarP[2].subs(subs))
    print('R\'s Polar:', polarR)
    print('Is P on R\'s Polar?', lies_on(P, polarR))

if __name__ == '__main__':
    main()