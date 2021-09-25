from sympy import symbols
from homogeneous import *

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, t, u = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, t, u')
    O = (a, b, c)
    A1, B1, C1 = (d, e, f), (g, h, j), (k, m, n)
    A2, B2, C2 = span(O, A1, p), span(O, B1, q), span(O, C1, r)
    A3, B3, C3 = span(O, A1, s), span(O, B1, t), span(O, C1, u)
    print(incidence(O, A2, A3))
    print(incidence(O, B2, B3))
    print(incidence(O, C2, C3))
    print(incidence(cross(A2, A3), cross(B2, B3), cross(C2, C3)))
    A1B1, A2B2, A3B3 = cross(A1, B1), cross(A2, B2), cross(A3, B3)
    A1C1, A2C2, A3C3 = cross(A1, C1), cross(A2, C2), cross(A3, C3)
    X1, X2, X3 = cross(A2B2, A3B3), cross(A1B1, A3B3), cross(A1B1, A2B2)
    print('X1:', X1)
    print('X2:', X2)
    print('X3:', X3)
    Y1, Y2, Y3 = cross(A2C2, A3C3), cross(A1C1, A3C3), cross(A1C1, A2C2)
    print('Y1:', Y1)
    print('Y2:', Y2)
    print('Y3:', Y3)
    # This is not necessary because X1, Y1 and Z1 are incident according to Desargues's theorem
    # Z1, Z2, Z3 = cross(B2C2, B3C3), cross(B1C1, B3C3), cross(B1C1, B2C2)
    X1Y1, X2Y2, X3Y3 = cross(X1, Y1), cross(X2, Y2), cross(X3, Y3)
    print('X1Y1:', X1Y1)
    print('X2Y2:', X2Y2)
    print('X3Y3:', X3Y3)
    print(incidence(X1Y1, X2Y2, X3Y3))

if __name__ == '__main__':
    main()