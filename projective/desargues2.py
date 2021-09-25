from sympy import Eq, symbols
from cartesian import *

def main():
    e, f, g, h, j, k, m, n = symbols('e, f, g, h, j, k, m, n')
    A1, A2, B1, B2, C1, C2 = (g, 0), (h, 0), (j, e * j), (k, e * k), (m, f * m), (n, f * n)
    A1B1, A1C1, B1C1, A2B2, A2C2, B2C2 = line(A1, B1), line(A1, C1), line(B1, C1), line(A2, B2), line(A2, C2), line(B2, C2)
    ab, ac, bc = intersect(A1B1, A2B2), intersect(A1C1, A2C2), intersect(B1C1, B2C2)
    print('ab:', ab)
    print('ac:', ac)
    print('bc:', bc)
    print(collinear(ab, ac, bc))

if __name__ == '__main__':
    main()