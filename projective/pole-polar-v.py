from sympy import Eq, solve, symbols
from homogeneous import *

def main():
    a, b, c, x = symbols('a, b, c, x')
    # results from conic-involution-v2.py
    P, A1, A2, A3, B1, B2, B3 = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (a, 1, 0), (b, 0, 1), (a + b - 1, 1, 1)
    A1B2, A1B3, A2B1, A3B1 = cross(A1, B2), cross(A1, B3), cross(A2, B1), cross(A3, B1)
    C12, C13 = cross(A1B2, A2B1), cross(A1B3, A3B1)
    p = cross(C12, C13)
    A1B1, A2B2 = PA1, PA2 = cross(P, A1), cross(P, A2)
    PQ = span(c, PA1, 1, PA2)
    Q = cross(p, PQ)
    print('Q:', Q)
    M = span(x, P, 1, Q)
    A1M, A2B3, A2M = cross(A1, M), cross(A2, B3), cross(A2, M)
    # M is on the conic so (A1B1,A1B2;A1B3,A1M) = (A2B1,A2B2;A2B3,A2M)
    x = solve(Eq(cross_ratio(A1B1, A1B2, A1B3, A1M), cross_ratio(A2B1, A2B2, A2B3, A2M)), x)
    print('x1 =', x[0])
    print('x2 =', x[1])
    M = span(x[0], P, 1, Q)
    N = span(x[1], P, 1, Q)
    print('M:', M)
    print('N:', N)
    print('(P,Q;M,N) =', cross_ratio(P, Q, M, N))

if __name__ == '__main__':
    main()