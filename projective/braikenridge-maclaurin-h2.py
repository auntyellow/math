from sympy import poly, symbols
from homogeneous import *

def point_on_conic(conic_z_roots, x0, y0, root = 0):
    f, x, y = symbols('f, x, y')
    return multiplied(x0, y0, conic_z_roots[root].subs(x, x0).subs(y, y0))

def main():
    a0, a1, a2, b0, b1, b2, c0, c1, c2, d0, d1, d2, e0, e1, e2, x, y, z = \
        symbols('a0, a1, a2, b0, b1, b2, c0, c1, c2, d0, d1, d2, e0, e1, e2, x, y, z')
    # `A, B = (a0, 0, a2), (b0, 0, b2)` is much faster than `A, B = (a0, a1, a2), (b0, b1, b2)`
    # The dual theorem is also proved when lines AB are parallel.
    # To prove the common case that AB are not parallel, WLOG, AB meet at origin, we can use `(a0, a1, 0), (b0, b1, 0)`
    A, B, C, D, E, F = (a0, a1, a2), (b0, b1, b2), (c0, c1, c2), (d0, d1, d2), (e0, e1, e2), (x, y, z)
    AB, BC, CD, DE, EF, FA = cross(A, B), cross(B, C), cross(C, D), cross(D, E), cross(E, F), cross(F, A)
    G, H, J = cross(AB, DE), cross(BC, EF), cross(CD, FA)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    # compare with steiner-conic-h1.py
    p = poly(-incidence(G, H, J), F)
    a, b, c, d, e, f = p.nth(2, 0, 0), p.nth(1, 1, 0), p.nth(0, 2, 0), p.nth(1, 0, 1), p.nth(0, 1, 1), p.nth(0, 0, 2)
    # Should reduce if `a1, b1 = 0, 0`
    # gcd = gcd_list([a, b, c, d, e, f])
    # print('GCD:', gcd)
    # a, b, c, d, e, f = cancel(a/gcd), cancel(b/gcd), cancel(c/gcd), cancel(d/gcd), cancel(e/gcd), cancel(f/gcd) 
    print('Locus of F:')
    print(p.expr, '= 0')
    print('x**2*(', a, ') +')
    print('x*y*(', b, ') +')
    print('y**2*(', c, ') +')
    print('x*z*(', d, ') +')
    print('y*z*(', e, ') +')
    print('z**2*(', f, ') = 0')

if __name__ == '__main__':
    main()