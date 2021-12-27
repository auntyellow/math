from sympy import symbols
from homogeneous import *

def main():
    p, q, r, s = symbols('p, q, r, s')
    A, B, C, D, E, F = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, p, q), (1, 0, r), (1, p + s, q)
    print('Are ACE collinear/concurrent?', incidence(A, C, E) == 0)
    print('Are BDF collinear/concurrent?', incidence(B, D, F) == 0)
    AB, BC, CD, DE, EF, FA = cross(A, B), cross(B, C), cross(C, D), cross(D, E), cross(E, F), cross(F, A)
    G, H, J = cross(AB, DE), cross(BC, EF), cross(CD, FA)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear/concurrent?', incidence(G, H, J) == 0)

if __name__ == '__main__':
    main()