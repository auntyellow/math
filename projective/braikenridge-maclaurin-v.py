from sympy import symbols
from homogeneous import *

def main():
    p, q, r, s, t = symbols('p, q, r, s, t')
    A, B, C, D, E = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, p, q), (1, r, s)
    AB, AC, BC, CD, DE = cross(A, B), cross(A, C), cross(B, C), cross(C, D), cross(D, E)
    AF = span(1, AB, t, AC)
    G, J = cross(AB, DE), cross(CD, AF)
    print('G:', G)
    print('J:', J)
    H = cross(BC, cross(G, J))
    print('H:', H)
    F = cross(AF, cross(E, H))
    AD, AE, BD, BE, BF = cross(A, D), cross(A, E), cross(B, D), cross(B, E), cross(B, F)
    L, L1, M, M1, N, N1 = cross(BC, AD), cross(AC, BD), cross(BC, AE), cross(AC, BE), cross(BC, AF), cross(AC, BF)
    print('L:', L)
    print('L1:', L1)
    print('M:', M)
    print('M1:', M1)
    print('N:', N)
    print('N1:', N1)
    LL1, MM1, NN1 = cross(L, L1), cross(M, M1), cross(N, N1)
    print('Are LL1, MM1 and NN1 concurrent/collinear?', incidence(LL1, MM1, NN1) == 0)

if __name__ == '__main__':
    main()