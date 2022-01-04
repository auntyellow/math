from sympy import Eq, solve, symbols
from homogeneous import *

def main():
    a, b, t = symbols('a, b, t')
    # AD, BE and CF are concurrent => (A,B;C,D)=(D,E;F,A), i.e. (A,B,C)->(D,E,F) is an involution
    # results from steiner-conic-v.py
    A, B, C, D, E, F = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (a + 1, b + 1, (a + 1)*(b + 1)), (t*(a + t), t*(b + t), (a + t)*(b + t))
    AB, AD, AE, BD, BE, CE, CF, DE = cross(A, B), cross(A, D), cross(A, E), cross(B, D), cross(B, E), cross(C, E), cross(C, F), cross(D, E)
    t0 = solve(Eq(incidence(AD, BE, CF), 0), t)[0]
    print('t =', t0)
    F = multiplied(F[0].subs(t, t0), F[1].subs(t, t0), F[2].subs(t, t0))
    print('F:', F)
    BF = cross(B, F)
    print('(A,B;C,D) =', cross_ratio(AE, BE, CE, DE))
    print('(D,E;F,A) =', cross_ratio(BD, BE, BF, AB))

if __name__ == '__main__':
    main()