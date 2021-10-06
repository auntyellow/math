from sympy import Eq, symbols
from cartesian import *

def L(a, b):
    x, y = symbols('x, y')
    return Eq(y, a*x + b)

def main():
    e, f, g, h, j, k, m, n = symbols('e, f, g, h, j, k, m, n')
    A1B1, A2B2, A1C1, A2C2, B1C1, B2C2 = L(g, 0), L(h, 0), L(j, e), L(k, e), L(m, f), L(n, f)
    A1, A2 = intersect(A1B1, A1C1), intersect(A2B2, A2C2)
    B1, B2 = intersect(A1B1, B1C1), intersect(A2B2, B2C2)
    C1, C2 = intersect(A1C1, B1C1), intersect(A2C2, B2C2)
    print('A1:', A1)
    print('A2:', A2)
    print('B1:', B1)
    print('B2:', B2)
    print('C1:', C1)
    print('C2:', C2)
    print(concurrency(A1, A2, B1, B2, C1, C2))

if __name__ == '__main__':
    main()