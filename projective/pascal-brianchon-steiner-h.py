from sympy import symbols
from homogeneous import *

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, t = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, t')
    AC, AD, BC, BD = (a, b, c), (d, e, f), (g, h, j), (k, m, n)
    AE, AF, BE, BF = span(1, AC, r, AD), span(1, AC, s, AD), span(1, BC, t, BD), span(r, BC, s*t, BD)
    A, B, C, D, E, F = cross(AC, AD), cross(BC, BD), cross(AC, BC), cross(AD, BD), cross(AE, BE), cross(AF, BF)
    print('A:', A)
    print('B:', B)
    print('C:', C)
    print('D:', D)
    print('E:', E)
    print('F:', F)
    # This is too slow. Try another Pascal line.
    # AB, CD, DE, EF = cross(A, B), cross(C, D), cross(D, E), cross(E, F)
    # G, H, J = cross(AB, DE), cross(BC, EF), cross(CD, AF)
    CF, DF = cross(C, F), cross(D, F)
    G, H, J = cross(AC, BD), cross(AE, DF), cross(BE, CF)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear/concurrent?', incidence(G, H, J) == 0)    

if __name__ == '__main__':
    main()