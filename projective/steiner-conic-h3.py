from sympy import expand, poly, symbols
from homogeneous import *

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, x, y, z = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, x, y, z')
    # `A, B = (a, 0, c), (d, 0, f)` is much faster than `A, B = (a, b, c), (d, e, f)`
    # The dual theorem is also proved when lines AB are parallel.
    # To prove the common case that AB are not parallel, WLOG, AB meet at origin, we can use `A, B = (a, b, 0), (c, d, 0)`
    points = [(x, y, z), (a, 0, c), (d, 0, f), (g, h, j), (k, m, n), (p, q, r)]
    coefficients = [x**2, x*y, y**2, x*z, y*z, z**2]
    subs, mat = [], []
    for s in range(6):
        row = []
        for t in range(6):
            rst = symbols('r' + str(s) + str(t))
            subs.append((rst, coefficients[t].subs(x, points[s][0]).subs(y, points[s][1]).subs(z, points[s][2])))
            row.append(rst)
        mat.append(row)
    print('M =', Matrix(mat).subs(subs))
    p = poly(expand(Matrix(mat).det().subs(subs)), (x, y, z))
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