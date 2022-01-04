from sympy import symbols
from homogeneous import *

def main():
    a, b, t = symbols('a, b, t')
    # results from steiner-conic-v.py
    A, B, C, D, E, F = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (a + 1, b + 1, (a + 1)*(b + 1)), (t*(a + t), t*(b + t), (a + t)*(b + t))
    AB, BC, CD, DE, EF, FA = cross(A, B), cross(B, C), cross(C, D), cross(D, E), cross(E, F), cross(F, A)
    G, H, J = cross(AB, DE), cross(BC, EF), cross(CD, FA)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear/concurrent?', incidence(G, H, J) == 0)

if __name__ == '__main__':
    main()