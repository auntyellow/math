from sympy import Eq, solve, symbols
from homogeneous import *

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, t, u, v, x, y = \
        symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, t, u, v, x, y')
    A, B, C = (a, b, c), (d, e, f), (g, h, j)
    D0, E0, F0 = span(k, B, m, C), span(n, C, p, A), span(q, A, x, B)
    x = solve(Eq(incidence(D0, E0, F0), 0), x)[0]
    F0 = span(q, A, x, B)
    F0 = multiplied(F0[0], F0[1], F0[2])
    print('F0:', F0)
    D, E, F = span(r, B, s, C), span(t, C, u, A), span(v, A, y, B)
    y = solve(Eq(incidence(D, E, F), 0), y)[0]
    F = span(v, A, y, B)
    F = multiplied(F[0], F[1], F[2])
    print('F:', F)
    print('Are B, C, D0 and D collinear/concurrent?', incidence(B, C, D0) == 0 and incidence(B, C, D) == 0)
    print('Are C, A, E0 and E collinear/concurrent?', incidence(C, A, E0) == 0 and incidence(C, A, E) == 0)
    print('Are A, B, F0 and F collinear/concurrent?', incidence(A, B, F0) == 0 and incidence(A, B, F) == 0)
    print('Are D0, E0 and F0 collinear/concurrent?', incidence(D0, E0, F0) == 0)
    print('Are D, E and F collinear/concurrent?', incidence(D, E, F) == 0)
    BCDD0, CAEE0, ABFF0 = cross_ratio(B, C, D, D0), cross_ratio(C, A, E, E0), cross_ratio(A, B, F, F0)
    print('(B,C;D,D0) =', BCDD0)
    print('(C,A;E,E0) =', CAEE0)
    print('(A,B;F,F0) =', ABFF0)
    print('(B,C;D,D0)(C,A;E,E0)(A,B;F,F0) =', cancel(BCDD0*CAEE0*ABFF0))

if __name__ == '__main__':
    main()