from sympy import symbols
from homogeneous import *

def main():
    a, b, c = symbols('a, b, c')
    A, C, E, G, H, J = (0, 0, 1), (1, 1, 1), (1, b, c), (1, 0, 0), (0, 1, 0), (a, 1, 0)
    AB, BC, CD, DE, EF, AF = cross(A, G), cross(H, C), cross(C, J), cross(G, E), cross(E, H), cross(J, A)
    B, D, F = cross(AB, BC), cross(CD, DE), cross(EF, AF)
    print('B:', B)
    print('D:', D)
    print('F:', F)
    # This is too slow. Try another projective mapping.
    # AC, AD, AE, BD, BE, BF = cross(A, C), cross(A, D), cross(A, E), cross(B, D), cross(B, E), cross(B, F)
    # print('(AC,AD;AE,AF) =', cross_ratio(AC, AD, AE, AF))
    # print('(BC,BD;BE,BF) =', cross_ratio(BC, BD, BE, BF))
    AD, AE, CE, CF = cross(A, D), cross(A, E), cross(C, E), cross(C, F)
    print('(AB,AD;AE,AF) =', cross_ratio(AB, AD, AE, AF))
    print('(BC,CD;CE,CF) =', cross_ratio(BC, CD, CE, CF))

if __name__ == '__main__':
    main()