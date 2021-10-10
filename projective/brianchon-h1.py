from sympy import expand, symbols
from homogeneous import *

def tangent_line(P):
    a, b, c, d, e, f = symbols('a, b, c, d, e, f')
    return (a*P[0] + b*P[1] + d*P[2], b*P[0] + c*P[1] + e*P[2], d*P[0] + e*P[1] + f*P[2])

def main():
    a, b, c, d, e, f, g, h, k, x, y = symbols('a, b, c, d, e, f, g, h, k, x, y')
    #P = sqrt(-a*f - 2*b*f*g - c*f*g**2 + d**2 + 2*d*e*g + e**2*g**2)
    #Q = sqrt(-a*f - 2*b*f*h - c*f*h**2 + d**2 + 2*d*e*h + e**2*h**2)
    #R = sqrt(-a*c*k**2 - 2*a*e*k - a*f + b**2*k**2 + 2*b*d*k + d**2)
    P, Q, R = symbols('P, Q, R')
    x_A = -(d + e*g - P)/(a + 2*b*g + c*g**2)
    x_B = -(b*k + d + R)/a
    x_C = -(d + e*h - Q)/(a + 2*b*h + c*h**2)
    x_D = -(d + e*h + Q)/(a + 2*b*h + c*h**2)
    x_E = -(b*k + d - R)/a
    x_F = -(d + e*g + P)/(a + 2*b*g + c*g**2)

    A, B, C, D, E, F = (x_A, g*x_A), (x_B, k), (x_C, h*x_C), (x_D, h*x_D), (x_E, k), (x_F, g*x_F)
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
    ad, db, bf, fc, ce, ea = cross(aa, dd, False), cross(dd, bb, False), cross(bb, ff, False), cross(ff, cc, False), cross(cc, ee, False), cross(ee, aa, False)
    print('ad:', ad)
    print('db:', db)
    print('bf:', bf)
    print('fc:', fc)
    print('ce:', ce)
    print('ea:', ea)
    G, H, J = cross(ad, fc, False), cross(db, ce, False), cross(bf, ea, False)
    G = expand(G[0]), expand(G[1]), expand(G[2])
    H = expand(H[0]), expand(H[1]), expand(H[2])
    J = expand(J[0]), expand(J[1]), expand(J[2])
    print('G:', G)
    print('H:', H)
    print('J:', J)
    # print(incidence(G, H, J))

if __name__ == '__main__':
    main()