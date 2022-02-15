from sympy import symbols
from homogeneous import *

def polar(P):
    x, y, z = P[0], P[1], P[2]
    a, b = symbols('a, b')
    # result from pole-polar-v.py
    return a*y - b*y + b*z, a*x - a*z - b*x, -a*y + b*x

def main():
    A, B, C, D = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)
    aa, bb, cc, dd = polar(A), polar(B), polar(C), polar(D)
    print('A\'s Tangent:', aa)
    print('B\'s Tangent:', bb)
    print('C\'s Tangent:', cc)
    print('D\'s Tangent:', dd)

    E, F, G, H = cross(aa, bb), cross(bb, cc), cross(cc, dd), cross(dd, aa)
    AC, BD, EG, FH = cross(A, C), cross(B, D), cross(E, G), cross(F, H)
    print('AC:', AC)
    print('BD:', BD)
    print('EG:', EG)
    print('FH:', FH)
    print('Are AC, BD, EG and FH concurrent/collinear?', incidence(AC, BD, EG) == 0 and incidence(AC, BD, FH) == 0)
    print('(AC,BD;EG,FH) =', cross_ratio(AC, BD, EG, FH))

    AB, BC, CD, DA = cross(A, B), cross(B, C), cross(C, D), cross(D, A)
    J, K, L, M = cross(aa, cc), cross(bb, dd), cross(AB, CD), cross(DA, BC)
    print('J:', J)
    print('K:', K)
    print('L:', L)
    print('M:', M)
    print('Are JKLM collinear/concurrent?', incidence(J, L, M) == 0 and incidence(K, L, M) == 0)
    print('(J,K;L,M) =', cross_ratio(J, K, L, M))

if __name__ == '__main__':
    main()