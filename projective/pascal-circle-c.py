from random import randint
from sympy import expand, sqrt
from cartesian import *

def sub_y(x, y):
    return y, (1 - randint(0, 1)*2)*sqrt(1 - x**2)

def main():
    # A hexagon ABCDEF inscribed in a unit circle
    # Prove 3 intersections of opposite edges (AB∩DE, BC∩EF, CD∩FA) are collinear
    a, b, c, d, e, f, g, h, j, k, m, n = symbols('a, b, c, d, e, f, g, h, j, k, m, n')
    A, B, C, D, E, F = (a, b), (c, d), (e, f), (g, h), (j, k), (m, n)
    # A = (1, 0) can be faster
    AB, BC, CD, DE, EF, FA = line(A, B), line(B, C), line(C, D), line(D, E), line(E, F), line(F, A)
    G, H, J = intersect(AB, DE), intersect(BC, EF), intersect(CD, FA)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear?', expand(collinear(G, H, J).lhs. \
        subs([sub_y(a, b), sub_y(c, d), sub_y(e, f), sub_y(g, h), sub_y(j, k), sub_y(m, n)])) == 0)

if __name__ == '__main__':
    main()