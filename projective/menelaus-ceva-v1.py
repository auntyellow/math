from sympy import Eq, solve, symbols
from homogeneous import *

def main():
    a, b, c = symbols('a, b, c')
    # desargues.md, trick 2c
    A, B, C, D0, E0 = (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, 1), (1, 0, 1)
    F0 = cross(cross(A, B), cross(D0, E0))
    print('F0:', F0)
    D, E, F = (0, b, 1), (1, 0, c), (a, 1, 0)
    a = solve(Eq(incidence(D, E, F), 0), a)[0]
    F = multiplied(a, 1, 0)
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