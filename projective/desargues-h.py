from sympy import symbols
from homogeneous import *

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, t, u = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, t, u')
    O = (a, b, c)
    A1, B1, C1 = (d, e, f), (g, h, j), (k, m, n)
    A2, B2, C2 = span(p, O, q, A1), span(r, O, s, B1), span(t, O, u, C1)
    print('Are O, A1 and A2 collinear/concurrent?', incidence(O, A1, A2) == 0)
    print('Are O, B1 and B2 collinear/concurrent?', incidence(O, B1, B2) == 0)
    print('Are O, C1 and C2 collinear/concurrent?', incidence(O, C1, C2) == 0)
    print('Are A1A2, B1B2 and C1C2 concurrent/collinear?', incidence(cross(A1, A2), cross(B1, B2), cross(C1, C2)) == 0)
    A1B1, A1C1, B1C1 = cross(A1, B1), cross(A1, C1), cross(B1, C1)
    A2B2, A2C2, B2C2 = cross(A2, B2), cross(A2, C2), cross(B2, C2)
    G, H, J = cross(A1B1, A2B2), cross(A1C1, A2C2), cross(B1C1, B2C2)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear/concurrent?', incidence(G, H, J) == 0)

if __name__ == '__main__':
    main()