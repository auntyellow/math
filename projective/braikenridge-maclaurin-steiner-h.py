from sympy import symbols
from homogeneous import *

def cross_ratio_lines(a, b, c, d):
    # To prove the dual theorem, use a[0]/a[2], ...
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
    A, C, E, G, H, J = (a, b, c), (d, e, f), (g, 0, h), (0, j, k), (0, m, n), (0, p, q)
    # The dual theorem is also proved when lines GHJ are parallel.
    # To prove the common case that GHJ are concurrent, we should use:
    # A, C, E, G, H, J = (a, b, c), (d, e, f), (g, 0, h), (j, k, 0), (m, n, 0), (p, q, 0)
    AB, BC, CD, DE, EF, AF = cross(A, G), cross(H, C), cross(C, J), cross(G, E), cross(E, H), cross(J, A)
    B, D, F = cross(AB, BC), cross(CD, DE), cross(EF, AF)
    print('B:', B)
    print('D:', D)
    print('F:', F)
    # This is too slow. Try another projective mapping.
    # AC, AD, AE, BD, BE, BF = cross(A, C), cross(A, D), cross(A, E), cross(B, D), cross(B, E), cross(B, F)
    # print('(AC,AD;AE,AF) =', cross_ratio_lines(AC, AD, AE, AF))
    # print('(BC,BD;BE,BF) =', cross_ratio_lines(BC, BD, BE, BF))
    # print('(AC,AD;AE,AF) = (BC,BD;BE,BF)?', projective_mapping(AC, AD, AE, AF, BC, BD, BE, BF))
    AD, AE, CE, CF = cross(A, D), cross(A, E), cross(C, E), cross(C, F)
    print('(AB,AD;AE,AF) =', cross_ratio_lines(AB, AD, AE, AF))
    print('(BC,CD;CE,CF) =', cross_ratio_lines(BC, CD, CE, CF))
    print('(AB,AD;AE,AF) = (BC,CD;CE,CF)?', projective_mapping(AB, AD, AE, AF, BC, CD, CE, CF))

if __name__ == '__main__':
    main()