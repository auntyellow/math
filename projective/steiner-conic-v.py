from sympy import factor, poly, symbols
from homogeneous import *

def factor_all(P):
    return factor(P[0]), factor(P[1]), factor(P[2])

def main():
    a, b, t, x, y, z = symbols('a, b, t, x, y, z')
    A, B, C, D = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)
    AC, AD, BC, BD = cross(A, C), cross(A, D), cross(B, C), cross(B, D)
    # (AC,AD;AE,AF)=(BC,BD;BE,BF)
    AE, BE = span(a, AC, 1, AD), span(b, BC, 1, BD)
    print('E:', factor_all(cross(AE, BE)))
    F = (x, y, z)
    AF, BF = cross(A, F), cross(B, F)
    crA = fraction(cross_ratio(AC, AD, AE, AF))
    crB = fraction(cross_ratio(BC, BD, BE, BF))
    p = expand(crA[0]*crB[1] - crA[1]*crB[0])
    print('Quadric Equation:', p, '= 0')
    AF, BF = span(a, AC, t, AD), span(b, BC, t, BD)
    F = cross(AF, BF)
    print('Parametric Equation:', factor(F))
    print('Are they equivalent?', expand(p.subs(x, F[0]).subs(y, F[1]).subs(z, F[2])) == 0);
    print('Steiner Construction:')
    L, L1, M, M1 = cross(BC, AD), cross(AC, BD), cross(BC, AE), cross(AC, BE)
    print('L:', L)
    print('L\':', L1)
    print('M:', M)
    print('M\':', M1)
    P = cross(cross(L, L1), cross(M, M1))
    print('P:', P)
    B = cross(BC, BD)
    AF = span(a, AC, t, AD)
    print('AF:', AF)
    N = cross(BC, AF)
    print('N:', N)
    N1 = cross(AC, cross(N, P))
    print('N\':', N1)
    F = cross(AF, cross(B, N1))
    print('Parametric Equation:', factor_all(F))

if __name__ == '__main__':
    main()