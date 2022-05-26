from sympy import symbols
from homogeneous import *

def polar(P):
    x, y, z = P
    a, b = symbols('a, b')
    # result from pole-polar-v.py
    return a*y - b*y + b*z, a*x - a*z - b*x, -a*y + b*x

def main():
    A, B, C, D = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)
    AA, BB, CC, DD = polar(A), polar(B), polar(C), polar(D)
    print('A\'s Tangent:', AA)
    print('B\'s Tangent:', BB)
    print('C\'s Tangent:', CC)
    print('D\'s Tangent:', DD)

    E, F, G, H = cross(AA, BB), cross(BB, CC), cross(CC, DD), cross(DD, AA)
    AC, BD, EG, FH = cross(A, C), cross(B, D), cross(E, G), cross(F, H)
    print('AC:', AC)
    print('BD:', BD)
    print('EG:', EG)
    print('FH:', FH)
    print('Are AC, BD, EG and FH concurrent/collinear?', incidence(AC, BD, EG) == 0 and incidence(AC, BD, FH) == 0)
    print('(AC,BD;EG,FH) =', cross_ratio(AC, BD, EG, FH))

    AB, BC, CD, DA = cross(A, B), cross(B, C), cross(C, D), cross(D, A)
    J, K, L, M = cross(AA, CC), cross(BB, DD), cross(AB, CD), cross(DA, BC)
    print('J:', J)
    print('K:', K)
    print('L:', L)
    print('M:', M)
    print('Are JKLM collinear/concurrent?', incidence(J, L, M) == 0 and incidence(K, L, M) == 0)
    print('(J,K;L,M) =', cross_ratio(J, K, L, M))

if __name__ == '__main__':
    main()