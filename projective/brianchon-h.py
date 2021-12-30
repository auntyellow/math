from sympy import Eq, solve, symbols
from homogeneous import *

def pair(conic, line):
    x, y = symbols('x, y')
    p = solve([conic, Eq(y, line)], (x, y))
    return (cancel(p[0][0]), cancel(p[0][1])), (cancel(p[1][0]), cancel(p[1][1]))

def tangent_line(P):
    a, b, c, d, e, f = symbols('a, b, c, d, e, f')
    return expand(a*P[0] + b*P[1] + d*P[2]), expand(b*P[0] + c*P[1] + e*P[2]), expand(d*P[0] + e*P[1] + f*P[2])

def main():
    a, b, c, d, e, f, g, h, k, x, y = symbols('a, b, c, d, e, f, g, h, k, x, y')
    conic = Eq(a*x**2 + 2*b*x*y + c*y**2 + 2*d*x + 2*e*y + f, 0)
    (F, A), (D, C), (B, E) = pair(conic, g*x), pair(conic, h*x), pair(conic, k)
    print('x_A =', A[0])
    print('x_B =', B[0])
    print('x_C =', C[0])
    print('x_D =', D[0])
    print('x_E =', E[0])
    print('x_F =', F[0])
    A, B, C = to_homogeneous(A), to_homogeneous(B), to_homogeneous(C)
    D, E, F = to_homogeneous(D), to_homogeneous(E), to_homogeneous(F)
    print('A:', A)
    print('B:', B)
    print('C:', C)
    print('D:', D)
    print('E:', E)
    print('F:', F)
    aa, bb, cc = tangent_line(A), tangent_line(B), tangent_line(C)
    dd, ee, ff = tangent_line(D), tangent_line(E), tangent_line(F)
    print('aa:', aa)
    print('bb:', bb)
    print('cc:', cc)
    print('dd:', dd)
    print('ee:', ee)
    print('ff:', ff)
    ad, db, bf, fc, ce, ea = cross(aa, dd), cross(dd, bb), cross(bb, ff), cross(ff, cc), cross(cc, ee), cross(ee, aa)
    print('ad:', ad)
    print('db:', db)
    print('bf:', bf)
    print('fc:', fc)
    print('ce:', ce)
    print('ea:', ea)
    gg, hh, jj = cross(ad, fc), cross(db, ce), cross(bf, ea)
    print('gg:', gg)
    print('hh:', hh)
    print('jj:', jj)
    print('Are gg, hh and jj concurrent?', incidence(gg, hh, jj) == 0)

if __name__ == '__main__':
    main()