from sympy import expand, poly, symbols
from homogeneous import *

def main():
    a0, a1, a2, b0, b1, b2, c0, c1, c2, d0, d1, d2, e0, e1, e2 = symbols('a0, a1, a2, b0, b1, b2, c0, c1, c2, d0, d1, d2, e0, e1, e2')
    # `(a0, 0, a2), (b0, 0, b2)` is much faster than `(a0, a1, a2), (b0, b1, b2)`.
    # The dual theorem is also proved when lines A and B are parallel to y-axis.
    # To prove the common case that AB are not parallel, WLOG, AB meet at origin, we can use `(a0, a1, 0), (b0, b1, 0)`.

    # This is much faster than 6x6 matrix:
    # mat = [[a0**2, b0**2, c0**2, d0**2, e0**2, x**2], ...]
    # conic_poly = poly(Matrix(mat).det(), (x, y, z))
    # a = conic_poly.coeff_monomial(x**2)
    # ...
    # SymPy's det() may be very slow. More efficient ways in this case could be:
    # 1. use adjugate() or Laplace expansion to reduce to 4x4 matrix
    # 2. https://stackoverflow.com/a/37056325/4260959
    r1 = [a0**2, b0**2, c0**2, d0**2, e0**2]
    r2 = [a0*a1, b0*b1, c0*c1, d0*d1, e0*e1]
    r3 = [a1**2, b1**2, c1**2, d1**2, e1**2]
    r4 = [a0*a2, b0*b2, c0*c2, d0*d2, e0*e2]
    r5 = [a1*a2, b1*b2, c1*c2, d1*d2, e1*e2]
    r6 = [a2**2, b2**2, c2**2, d2**2, e2**2]
    a, b = Matrix([r2, r3, r4, r5, r6]).det(), -Matrix([r1, r3, r4, r5, r6]).det()
    c, d = Matrix([r1, r2, r4, r5, r6]).det(), -Matrix([r1, r2, r3, r5, r6]).det()
    e, f = Matrix([r1, r2, r3, r4, r6]).det(), -Matrix([r1, r2, r3, r4, r5]).det()
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