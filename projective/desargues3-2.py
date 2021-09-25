from sympy import Eq, symbols
from cartesian import *

def main():
    e, f, g, h, j, k, m, n, p, q, r = symbols('e, f, g, h, j, k, m, n, p, q, r')
    A1, A2, A3, B1, B2, B3, C1, C2, C3 = (g, 0), (h, 0), (j, 0), (k, e*k), (m, e*m), (n, e*n), (p, f*p), (q, f*q), (r, f*r)
    A1B1, A2B2, A3B3 = line(A1, B1), line(A2, B2), line(A3, B3)
    A1C1, A2C2, A3C3 = line(A1, C1), line(A2, C2), line(A3, C3)
    X1, X2, X3 = intersect(A2B2, A3B3), intersect(A1B1, A3B3), intersect(A1B1, A2B2)
    print('X1:', X1)
    print('X2:', X2)
    print('X3:', X3)
    Y1, Y2, Y3 = intersect(A2C2, A3C3), intersect(A1C1, A3C3), intersect(A1C1, A2C2)
    print('Y1:', Y1)
    print('Y2:', Y2)
    print('Y3:', Y3)
    print(concurrency(X1, Y1, X2, Y2, X3, Y3))

if __name__ == '__main__':
    main()