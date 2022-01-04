from sympy import symbols
from homogeneous import *

def main():
    a, b, c = symbols('a, b, c')
    A, B, C, D, E = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (a, 1, b)
    AC, AD, AE, BC, BD, BE = cross(A, C), cross(A, D), cross(A, E), cross(B, C), cross(B, D), cross(B, E)
    CF = span(1, AC, c, BC)
    G, H = cross(AC, BD), cross(BE, CF)
    print('G:', G)
    print('H:', H)
    J = cross(AE, cross(G, H))
    print('J:', J)
    F = cross(CF, cross(D, J))
    print('F:', F)
    AF, BF = cross(A, F), cross(B, F)
    print('(AC,AD;AE,AF) =', cross_ratio(AC, AD, AE, AF))
    print('(BC,BD;BE,BF) =', cross_ratio(BC, BD, BE, BF))

if __name__ == '__main__':
    main()