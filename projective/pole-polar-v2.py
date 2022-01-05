from sympy import Eq, solve, symbols
from homogeneous import *

def point_subs(P, t, u):
    return P[0].subs(t, u), P[1].subs(t, u), P[2].subs(t, u)

def lies_on(P, L):
    return expand(P[0]*L[0] + P[1]*L[1] + P[2]*L[2]) == 0

def main():
    a, b, t, u, v, w, x, y, z = symbols('a, b, c, d, e, t, x, y, z')
    # results from steiner-conic-v.py
    P, M, N = (x, y, z), (t*(a + t), t*(b + t), (a + t)*(b + t)), (u*(a + u), u*(b + u), (a + u)*(b + u))
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
    xx, yy, zz = symbols('xx, yy, zz')
    subs = [(x, xx), (y, yy), (z, zz), (xx, Q[0]), (yy, Q[1]), (zz, Q[2])]
    polarQ = reduced(polarP[0].subs(subs), polarP[1].subs(subs), polarP[2].subs(subs))
    print('Q\'s Polar:', polarQ)
    print('Is P on Q\'s Polar?', lies_on(P, polarQ))

if __name__ == '__main__':
    main()