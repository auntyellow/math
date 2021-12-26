from sympy import poly, symbols
from homogeneous import *

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, x, y, z = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, x, y, z')
    # `A, B = (a, 0, c), (d, 0, f)` is much faster than `A, B = (a, b, c), (d, e, f)`
    # The dual theorem is also proved when lines AB are parallel.
    # To prove the common case that AB are not parallel, WLOG, AB meet at origin, we can use `A, B = (a, b, 0), (c, d, 0)`
    A, B, C, D, E, F = (a, 0, c), (d, 0, f), (g, h, j), (k, m, n), (p, q, r), (x, y, z)
    AC, AD, AE, AF = cross(A, C), cross(A, D), cross(A, E), cross(A, F)
    BC, BD, BE, BF = cross(B, C), cross(B, D), cross(B, E), cross(B, F)
    L, L1, M, M1, N, N1 = cross(BC, AD), cross(AC, BD), cross(BC, AE), cross(AC, BE), cross(BC, AF), cross(AC, BF)
    print('L:', L)
    print('L1:', L1)
    print('M:', M)
    print('M1:', M1)
    print('N:', N)
    print('N1:', N1)
    P = cross(cross(L, L1), cross(M, M1))
    print('P:', P)
    print('Locus of F:', poly(incidence(N, N1, P), F).expr, '= 0')

if __name__ == '__main__':
    main()