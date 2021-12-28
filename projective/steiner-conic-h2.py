from sympy import expand, poly, symbols
from homogeneous import *

def cross_ratio_lines(a, b, c, d):
    # To prove the dual theorem, use a[0]/a[2], ...
    return cross_ratio_frac(a[1]/a[0], b[1]/b[0], c[1]/c[0], d[1]/d[0])

def cross_ratio_frac(a, b, c, d):
    return fraction(cancel((a - c)*(b - d)/(a - d)/(b - c)))

def main():
    a0, a1, a2, b0, b1, b2, c0, c1, c2, d0, d1, d2, e0, e1, e2, x, y, z = \
        symbols('a0, a1, a2, b0, b1, b2, c0, c1, c2, d0, d1, d2, e0, e1, e2, x, y, z')
    # `A, B = (a0, 0, a2), (b0, 0, b2)` is much faster than `A, B = (a0, a1, a2), (b0, b1, b2)`
    # The dual theorem is also proved when lines AB are parallel.
    # To prove the common case that AB are not parallel, WLOG, AB meet at origin, we can use `A, B = (a, b, 0), (c, d, 0)`
    A, B, C, D, E, F = (a0, a1, a2), (b0, b1, b2), (c0, c1, c2), (d0, d1, d2), (e0, e1, e2), (x, y, z)
    AC, AD, AE, AF = cross(A, C), cross(A, D), cross(A, E), cross(A, F)
    BC, BD, BE, BF = cross(B, C), cross(B, D), cross(B, E), cross(B, F)
    crA = cross_ratio_lines(AC, AD, AE, AF)
    crB = cross_ratio_lines(BC, BD, BE, BF)
    p = poly(expand(crA[0]*crB[1] - crA[1]*crB[0]), F)
    a, b, c, d, e, f = p.nth(2, 0, 0), p.nth(1, 1, 0), p.nth(0, 2, 0), p.nth(1, 0, 1), p.nth(0, 1, 1), p.nth(0, 0, 2)
    # Should reduce if `a1, b1 = 0, 0`
    # gcd = gcd_list([a, b, c, d, e, f])
    # print('GCD:', gcd)
    # a, b, c, d, e, f = cancel(a/gcd), cancel(b/gcd), cancel(c/gcd), cancel(d/gcd), cancel(e/gcd), cancel(f/gcd) 
    print('Locus of F:')
    print('x**2*(', a, ') +')
    print('x*y*(', b, ') +')
    print('y**2*(', c, ') +')
    print('x*z*(', d, ') +')
    print('y*z*(', e, ') +')
    print('z**2*(', f, ') = 0')

if __name__ == '__main__':
    main()