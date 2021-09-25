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
    X1, X2, X3 = cross(A1B1, A1C1), cross(A2B2, A2C2), cross(A3B3, A3C3)
    print('X1:', X1)
    print('X2:', X2)
    print('X3:', X3)
    print(incidence(X1, X2, X3))

if __name__ == "__main__":
    main()