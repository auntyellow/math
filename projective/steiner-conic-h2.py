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
    p = poly(incidence(N, N1, P), F);
    cxx, cxy, cxz, cyy, cyz, czz = p.nth(2, 0, 0), p.nth(1, 1, 0), p.nth(1, 0, 1), p.nth(0, 2, 0), p.nth(0, 1, 1), p.nth(0, 0, 2)
    gcd = gcd_list([cxx, cxy, cxz, cyy, cyz, czz])
    cxx, cxy, cxz, cyy, cyz, czz = cancel(cxx/gcd), cancel(cxy/gcd), cancel(cxz/gcd), cancel(cyy/gcd), cancel(cyz/gcd), cancel(czz/gcd) 
    print('Locus of F:')
    print('x**2*(', cxx, ') +')
    print('x*y*(', cxy, ') +')
    print('x*z*(', cxz, ') +')
    print('y**2*(', cyy, ') +')
    print('y*z*(', cyz, ') +')
    print('z**2*(', czz, ') = 0')

if __name__ == '__main__':
    main()