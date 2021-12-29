from sympy import symbols
from homogeneous import *

def projective_mapping(a0, a1, a2, a3, b0, b1, b2, b3):
    # (a0, a1, a2, a3) =^b0^= (c0, c1, c2, c3) =^a0^= (b0, b1, b2, b3)
    c1 = cross(cross(a0, b1), cross(b0, a1))
    c2 = cross(cross(a0, b2), cross(b0, a2))
    c3 = cross(cross(a0, b3), cross(b0, a3))
    return incidence(c1, c2, c3) == 0

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
    # print('(AC,AD;AE,AF) = (BC,BD;BE,BF)?', projective_mapping(AC, AD, AE, AF, BC, BD, BE, BF))
    AD, AE, CE, CF = cross(A, D), cross(A, E), cross(C, E), cross(C, F)
    print('(AB,AD;AE,AF) = (BC,CD;CE,CF)?', projective_mapping(AB, AD, AE, AF, BC, CD, CE, CF))

if __name__ == '__main__':
    main()