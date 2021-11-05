from sympy import symbols
from homogeneous import *

def main():
    a, b, c, d, e, f, g, h, k, m, n, p, q = symbols('a, b, c, d, e, f, g, h, k, m, n, p, q')
    A, C, E, B, D = (a, 0, b), (c, 0, d), (e, 0, f), (0, g, h), (k, m, n)
    # The dual theorem is also proved when lines ACE are parallel.
    # To prove the common case that ACE are concurrent, we should use:
    # A, C, E, B, D = (a, b, 0), (c, d, 0), (e, f, 0), (0, g, h), (k, m, n)
    F = span(p, B, q, D)
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