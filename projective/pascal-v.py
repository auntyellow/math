from sympy import symbols
from homogeneous import *

def main():
    p, q, r, s, t = symbols('p, q, r, s, t')
    A, B, C, D, E = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, p, q), (1, r, s)
    AB, AC, AD, AE = cross(A, B), cross(A, C), cross(A, D), cross(A, E)
    BC, BD, BE = cross(B, C), cross(B, D), cross(B, E)
    AF = span(1, AB, t, AC)
    L, L1, M, M1, N = cross(BC, AD), cross(AC, BD), cross(BC, AE), cross(AC, BE), cross(BC, AF)
    print('L:', L)
    print('L1:', L1)
    print('M:', M)
    print('M1:', M1)
    print('N:', N)
    P = cross(cross(L, L1), cross(M, M1))
    print('P:', P)
    N1 = cross(AC, cross(N, P))
    print('N1:', N1)
    F = cross(AF, cross(B, N1))
    print('F:', F)
    CD, DE, EF = cross(C, D), cross(D, E), cross(E, F)
    G, H, J = cross(AB, DE), cross(BC, EF), cross(CD, AF)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear/concurrent?', incidence(G, H, J) == 0)

if __name__ == '__main__':
    main()