from sympy import symbols
from homogeneous import *

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, r = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, r')
    O = (a, b, c)
    A1, B1, C1 = (d, e, f), (g, h, j), (k, m, n)
    A2, B2, C2 = span(O, A1, p), span(O, B1, q), span(O, C1, r)
    print(incidence(O, A1, A2))
    print(incidence(O, B1, B2))
    print(incidence(O, C1, C2))
    print(incidence(cross(A1, A2), cross(B1, B2), cross(C1, C2)))
    A1B1, A1C1, B1C1 = cross(A1, B1), cross(A1, C1), cross(B1, C1)
    A2B2, A2C2, B2C2 = cross(A2, B2), cross(A2, C2), cross(B2, C2)
    X1, X2, X3 = cross(A1B1, A2B2), cross(A1C1, A2C2), cross(B1C1, B2C2) 
    print('X1:', X1)
    print('X2:', X2)
    print('X3:', X3)
    print(incidence(X1, X2, X3))

if __name__ == '__main__':
    main()