from sympy import expand, poly, symbols
from homogeneous import *

def cross_ratio_lines(a, b, c, d):
    # To prove the dual theorem, use a[0]/a[2], ...
    return cross_ratio_frac(a[1]/a[0], b[1]/b[0], c[1]/c[0], d[1]/d[0])

def cross_ratio_frac(a, b, c, d):
    return fraction(cancel((a - c)*(b - d)/(a - d)/(b - c)))

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, t, u, x, y, z = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, t, u, x, y, z')
    AC, AD, BC, BD = (a, b, c), (d, e, f), (g, h, j), (k, m, n)
    AE, BE = span(p, AC, q, AD), span(r, BC, s, BD)
    F = (x, y, z)
    AF, BF = cross(cross(AC, AD), F), cross(cross(BC, BD), F)
    crA = cross_ratio_lines(AC, AD, AE, AF)
    crB = cross_ratio_lines(BC, BD, BE, BF)
    p = poly(expand(crA[0]*crB[1] - crA[1]*crB[0]), F)
    cxx, cxy, cxz, cyy, cyz, czz = p.nth(2, 0, 0), p.nth(1, 1, 0), p.nth(1, 0, 1), p.nth(0, 2, 0), p.nth(0, 1, 1), p.nth(0, 0, 2)
    gcd = gcd_list([cxx, cxy, cxz, cyy, cyz, czz])
    cxx, cxy, cxz, cyy, cyz, czz = cancel(cxx/gcd), cancel(cxy/gcd), cancel(cxz/gcd), cancel(cyy/gcd), cancel(cyz/gcd), cancel(czz/gcd)
    p = poly(cxx*x**2 + cxy*x*y + cxz*x*z + cyy*y**2 + cyz*y*z + czz*z**2, F).expr;
    print('Locus of F:', p, '= 0')
    print('Verify if F is on the locus ...')
    L, L1, M, M1 = cross(BC, AD), cross(AC, BD), cross(BC, AE), cross(AC, BE)
    print('L:', L)
    print('L\':', L1)
    print('M:', M)
    print('M\':', M1)
    P = cross(cross(L, L1), cross(M, M1))
    print('P:', P)
    B = cross(BC, BD)
    AF = span(t, AC, u, AD)
    print('AF:', AF)
    N = cross(BC, AF)
    print('N:', N)
    N1 = cross(AC, cross(N, P))
    print('N\':', N1)
    F = cross(AF, cross(B, N1))
    print('F:', F)
    print('Is F on the locus?', expand(p.subs(x, F[0]).subs(y, F[1]).subs(z, F[2])) == 0)

if __name__ == '__main__':
    main()