from sympy import Eq, solve, symbols
from homogeneous import *

def mapping(B0, A0, A1, A2, r):
    # return Ai on a conic such that (A0,A1;A2,Ai)=r
    # results from steiner-conic-v.py
    a, b, t = symbols('a, b, t')
    Ai = (t*(a + t), t*(b + t), (a + t)*(b + t))
    t0 = solve(Eq(cross_ratio(cross(B0, A0), cross(B0, A1), cross(B0, A2), cross(B0, Ai)), r), t)[0]
    return multiplied(Ai[0].subs(t, t0), Ai[1].subs(t, t0), Ai[2].subs(t, t0))

def point_subs(P, r, s, t, u):
    return P[0].subs(r, t).subs(s, u), P[1].subs(r, t).subs(s, u), P[2].subs(r, t).subs(s, u)

def main():
    a, b, c, ri, rj, rk, rl, rm, rn = symbols('a, b, c, ri, rj, rk, rl, rm, rn')
    # results from steiner-conic-v.py
    A0, B0, A1, B1, A2, B2 = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (a + 1, b + 1, (a + 1)*(b + 1)), (c*(a + c), c*(b + c), (a + c)*(b + c))
    Ai, Aj, Bi, Bj = mapping(B0, A0, A1, A2, ri), mapping(B0, A0, A1, A2, rj), mapping(A0, B0, B1, B2, ri), mapping(A0, B0, B1, B2, rj)
    print('Ai:', Ai)
    print('Aj:', Aj)
    print('Bi:', Bi)
    print('Bj:', Bj)
    C = cross(cross(Ai, Bj), cross(Bi, Aj))
    print('AiBj∩BiAj:', C)
    print('Are they collinear/concurrent?', incidence(C, point_subs(C, ri, rj, rk, rl), point_subs(C, ri, rj, rm, rn)) == 0)

if __name__ == '__main__':
    main()