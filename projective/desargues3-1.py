from sympy import Eq, symbols
from cartesian import *

def L(a, b):
    x, y = symbols('x, y')
    return Eq(y, a*x + b)

def main():
    e, f, g, h, j, k, m, n, p, q, r = symbols('e, f, g, h, j, k, m, n, p, q, r')
    A1B1, A2B2, A3B3, A1C1, A2C2, A3C3, B1C1, B2C2, B3C3 = L(g, 0), L(h, 0), L(j, 0), L(k, e), L(m, e), L(n, e), L(p, f), L(q, f), L(r, f)
    A1, A2, A3 = intersect(A1B1, A1C1), intersect(A2B2, A2C2), intersect(A3B3, A3C3)
    B1, B2, B3 = intersect(A1B1, B1C1), intersect(A2B2, B2C2), intersect(A3B3, B3C3)
    A1A2, A1A3, A2A3 = line(A1, A2), line(A1, A3), line(A2, A3)
    B1B2, B1B3, B2B3 = line(B1, B2), line(B1, B3), line(B2, B3)
    X1, X2, X3 = intersect(A2A3, B2B3), intersect(A1A3, B1B3), intersect(A1A2, B1B2)
    print('X1:', X1)
    print('X2:', X2)
    print('X3:', X3)
    print(collinear(X1, X2, X3))

if __name__ == '__main__':
    main()