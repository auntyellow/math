from sympy import cancel, expand, poly, symbols
from homogeneous import *

def tangent(x, z):
    a, b, d, e, f = symbols('a, b, d, e, f')
    return (z*(e*x - b*z), a*z**2 - d*x*z + f*x**2, x*(b*z - e*x))

def cross_ratio_points(a, b, c, d):
    return cross_ratio(a[0]/a[2], b[0]/b[2], c[0]/c[2], d[0]/d[2])

def cross_ratio(a, b, c, d):
    return cancel((a - c)*(b - d)/(a - d)/(b - c))

def projective_mapping(a0, a1, a2, a3, b0, b1, b2, b3):
    #                  b0                  a0
    # (a0, a1, a2, a3) == (c0, c1, c2, c3) == (b0, b1, b2, b3)
    #                  /\                  /\  
    c1 = cross(cross(a0, b1), cross(b0, a1))
    c2 = cross(cross(a0, b2), cross(b0, a2))
    c3 = cross(cross(a0, b3), cross(b0, a3))
    return incidence(c1, c2, c3) == 0

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, u, v, w = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, u, v, w')
    L = tangent(g, h)
    print('Line L:', L)
    print('Is line L tangent to conic?', expand((a*u**2 + b*u*v + d*u*w + e*v*w + f*w**2).subs(u, L[0]).subs(v, L[1]).subs(w, L[2])) == 0)
    A, B, C, D, E, F = (0, 1, 0), tangent(0, 1), tangent(g, h), tangent(j, k), tangent(m, n), tangent(p, q)
    AC, AD, AE, AF = cross(A, C), cross(A, D), cross(A, E), cross(A, F)
    print('AC:', AC)
    print('AD:', AD)
    print('AE:', AE)
    print('AF:', AF)
    print('(AC,AD;AE,AF) =', cross_ratio_points(AC, AD, AE, AF))
    BC, BD, BE, BF = cross(B, C), cross(B, D), cross(B, E), cross(B, F)
    print('Point BC:', BC)
    print('Point BD:', BD)
    print('Point BE:', BE)
    print('Point BF:', BF)
    print('(BC,BD;BE,BF) =', cross_ratio_points(BC, BD, BE, BF))
    print('(AC,AD;AE,AF) = (BC,BD;BE,BF)?', projective_mapping(AC, AD, AE, AF, BC, BD, BE, BF))

if __name__ == '__main__':
    main()