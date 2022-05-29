from sympy import Eq, solve, symbols
from homogeneous import *

def lies_on(P, L):
    return expand(P[0]*L[0] + P[1]*L[1] + P[2]*L[2]) == 0

def main():
    t, x0, y0, z0, x, y, z = symbols('t, x0, y0, z0, x, y, z')
    A, B, C, P = (1, 0, 0), (0, 1, 0), (0, 0, 1), (x0, y0, z0)
    AB, BC, CA = cross(A, B), cross(B, C), cross(C, A)
    D, E, F = cross(BC, cross(A, P)), cross(CA, cross(B, P)), cross(AB, cross(C, P))
    D1, E1, F1 = cross(BC, cross(E, F)), cross(CA, cross(F, D)), cross(AB, cross(D, E))
    print('(A,B;F,F\') =', cross_ratio(A, B, F, F1))
    print('(B,C;D,D\') =', cross_ratio(B, C, D, D1))
    print('(C,A;E,E\') =', cross_ratio(C, A, E, E1))
    print('Are D\'E\'F\' Collinear?', incidence(D1, E1, F1) == 0);
    p = cross(D1, E1)
    print('P\'s Polar:', p)
    Q = span(1, D1, t, E1)
    print('Q on P\'s Polar:', Q)
    print('Is Q on P\'s Polar?', lies_on(Q, p))
    subs = [(x0, Q[0]), (y0, Q[1]), (z0, Q[2])]
    q = reduced(p[0].subs(subs), p[1].subs(subs), p[2].subs(subs))
    print('Q\'s Polar:', q)
    print('Is P on Q\'s Polar?', lies_on(P, q))
    txz = fraction(cancel(solve(Eq(x/z, q[0]/q[2]), t)[0]))
    tyz = fraction(cancel(solve(Eq(y/z, q[1]/q[2]), t)[0]))
    q = expand(txz[0]*tyz[1] - txz[1]*tyz[0])
    print('Envelope of Q\'s Polar:', q, '= 0')

if __name__ == '__main__':
    main()