from sympy import Eq, solve, symbols
from homogeneous import *

def mapping(B0, A0, A1, A2, r):
    # return A on a conic such that (A0,A1;A2,A)=r
    a, b, t = symbols('a, b, t')
    A = t*(a + t), t*(b + t), (a + t)*(b + t)
    t = solve(Eq(cross_ratio(cross(B0, A0), cross(B0, A1), cross(B0, A2), cross(B0, A)), r), t)[0]
    return multiplied(t*(a + t), t*(b + t), (a + t)*(b + t))

def main():
    a, b, c, ri, rj, rk, rl = symbols('a, b, c, ri, rj, rk, rl')
    # results from steiner-conic-v.py
    A0, B0, A1, B1, A2, B2 = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (a + 1, b + 1, (a + 1)*(b + 1)), (c*(a + c), c*(b + c), (a + c)*(b + c))
    Ai, Aj, Bi, Bj = mapping(B0, A0, A1, A2, ri), mapping(B0, A0, A1, A2, rj), mapping(A0, B0, B1, B2, ri), mapping(A0, B0, B1, B2, rj)
    print('Ai:', Ai)
    print('Aj:', Aj)
    print('Bi:', Bi)
    print('Bj:', Bj)
    C = cross(cross(Ai, Bj), cross(Bi, Aj))
    print('AiBj∩BiAj:', C)
    print('Projective Axis:', cross(C, (C[0].subs(ri, rj).subs(rk, rl), C[1].subs(ri, rj).subs(rk, rl), C[2].subs(ri, rj).subs(rk, rl))))

if __name__ == '__main__':
    main()