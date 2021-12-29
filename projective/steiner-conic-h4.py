from sympy import cancel, expand, poly, symbols
from homogeneous import *

def intersect(u, v):
    a, b, c, d, e = symbols('a, b, c, d, e')
    return (v*(e*u - d*v), u*(d*v - e*u), a*v**2 - b*u*v + c*u**2)

def cross_ratio_lines(a, b, c, d):
    return cross_ratio(a[1]/a[0], b[1]/b[0], c[1]/c[0], d[1]/d[0])

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
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, x, y, z = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, x, y, z')
    P = intersect(g, h)
    print('P:', P)
    print('Is P on conic?', expand((a*x**2 + b*x*y + c*y**2 + d*x*z + e*y*z).subs(x, P[0]).subs(y, P[1]).subs(z, P[2])) == 0)
    A, B, C, D, E, F = (0, 0, 1), intersect(0, 1), intersect(g, h), intersect(j, k), intersect(m, n), intersect(p, q)
    AC, AD, AE, AF = cross(A, C), cross(A, D), cross(A, E), cross(A, F)
    print('AB:', cross(A, B))
    print('AC:', AC)
    print('AD:', AD)
    print('AE:', AE)
    print('AF:', AF)
    print('(AC,AD;AE,AF) =', cross_ratio_lines(AC, AD, AE, AF))
    BC, BD, BE, BF = cross(B, C), cross(B, D), cross(B, E), cross(B, F)
    print('BC:', BC)
    print('BD:', BD)
    print('BE:', BE)
    print('BF:', BF)
    print('(BC,BD;BE,BF) =', cross_ratio_lines(BC, BD, BE, BF))
    print('(AC,AD;AE,AF) = (BC,BD;BE,BF)?', projective_mapping(AC, AD, AE, AF, BC, BD, BE, BF))

if __name__ == '__main__':
    main()