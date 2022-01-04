from sympy import Eq, solve, symbols
from homogeneous import *

def main():
    a, b, c, x = symbols('a, b, c, x')
    A, B, C, D, E = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (a + 1, b + 1, (a + 1)*(b + 1))
    # results from conic-involution-v2.py
    F = (a**2*b + a**2 - a*b**2 - 2*a*b + b**2, a**2*b**2 + 2*a**2*b + a**2 - a*b**3 - 3*a*b**2 - 2*a*b + b**3 + b**2, a**2*b + a**2 - 2*a*b**2 - 2*a*b + b**3 + b**2)
    AE, AF, BD, CD = cross(A, E), cross(A, F), cross(B, D), cross(C, D)
    G, H = cross(AE, BD), cross(AF, CD)
    p = cross(G, H)
    AD, BE = PA, PB = cross(A, D), cross(B, E)
    P = cross(AD, BE)
    PQ = span(c, PA, 1, PB)
    Q = cross(p, PQ)
    print('Q:', Q)
    M = span(x, P, 1, Q)
    AM, BF, BM = cross(A, M), cross(B, F), cross(B, M)
    # M is on the conic so (AD,AE;AF,AM) = (BD,BE;BF,BM)
    x = solve(Eq(cross_ratio(AD, AE, AF, AM), cross_ratio(BD, BE, BF, BM)), x)
    print('x1 =', x[0])
    print('x2 =', x[1])
    M = span(x[0], P, 1, Q)
    N = span(x[1], P, 1, Q)
    print('M:', M)
    print('N:', N)
    print('(P,Q;M,N) =', cross_ratio(P, Q, M, N))

if __name__ == '__main__':
    main()