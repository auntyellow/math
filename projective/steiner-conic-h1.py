from sympy import poly, symbols
from homogeneous import *

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, x, y, z = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, x, y, z')
    AC, AD, BC, BD = (a, b, c), (d, e, f), (g, h, j), (k, m, n)
    AE, BE = span(p, AC, q, AD), span(r, BC, s, BD)
    F = (x, y, z)
    AF, BF = cross(cross(AC, AD), F), cross(cross(BC, BD), F)
    L, L1, M, M1 = cross(BC, AD), cross(AC, BD), cross(BC, AE), cross(AC, BE)
    P = cross(cross(L, L1), cross(M, M1))
    print('P:', P)
    N, N1 = cross(AF, BC), cross(BF, AC)
    print('N:', N)
    print('N1:', N1)
    print('Locus of F:', poly(incidence(P, N, N1), F).expr, '= 0')

if __name__ == '__main__':
    main()