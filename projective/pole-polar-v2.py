from sympy import Eq, solve, symbols
from homogeneous import *

def point_subs(P, t, u):
    return P[0].subs(t, u), P[1].subs(t, u), P[2].subs(t, u)

def main():
    a, b, c, d, e, r, s, t, u, v = symbols('a, b, c, d, e, r, s, t, u, v')
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
    print('Are Qs collinear/concurrent?', incidence(Q, point_subs(Q, t, s), point_subs(Q, t, r)) == 0)
    subs = {c: Q[0], d: Q[1], e: Q[2]}
    Q = reduced(Q[0].subs(subs), Q[1].subs(subs), Q[2].subs(subs))
    print('Point on Q\'s polar:', Q)
    print('Is P on Q\'s polar?', incidence(P, Q, point_subs(Q, t, s)) == 0) 

if __name__ == '__main__':
    main()