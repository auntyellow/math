from sympy import symbols
from homogeneous import *

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s')
    A, C, B, D = (a, b, c), (d, e, f), (g, h, j), (k, m, n)
    E, F = span(p, A, q, C), span(r, B, s, D)
    print(incidence(A, C, E))
    print(incidence(B, D, F))
    AB, BC, CD, DE, EF, FA = cross(A, B), cross(B, C), cross(C, D), cross(D, E), cross(E, F), cross(F, A)
    G, H, J = cross(AB, DE), cross(BC, EF), cross(CD, FA) 
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print(incidence(G, H, J))

if __name__ == '__main__':
    main()