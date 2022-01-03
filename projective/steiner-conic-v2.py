from sympy import factor, poly, symbols
from homogeneous import *

def main():
    a, b, t, x, y, z = symbols('a, b, t, x, y, z')
    A, B, C, D = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)
    AC, AD, BC, BD = cross(A, C), cross(A, D), cross(B, C), cross(B, D)
    # (AC,AD;AE,AF)=(BC,BD;BE,BF)
    AE, BE, AF, BF = span(a, AC, 1, AD), span(b, BC, 1, BD), span(a, AC, t, AD), span(b, BC, t, BD)
    F0 = cross(AF, BF)
    print('Parametric Equation:', F0)
    F = (x, y, z)
    AF, BF = cross(A, F), cross(B, F)
    crA = fraction(cross_ratio(AC, AD, AE, AF))
    crB = fraction(cross_ratio(BC, BD, BE, BF))
    p = expand(crA[0]*crB[1] - crA[1]*crB[0])
    print('Quadric Equation:', p, '= 0')
    print('Are they equivalent?', expand(p.subs(x, F0[0]).subs(y, F0[1]).subs(z, F0[2])) == 0);

if __name__ == '__main__':
    main()