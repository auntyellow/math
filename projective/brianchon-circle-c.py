from random import randint
from sympy import expand, sqrt
from cartesian import *

def tangent(x0, y0):
    x, y = symbols('x, y')
    return Eq(x0*x + y0*y, 1)

def sub_y(x, y):
    return y, (1 - randint(0, 1)*2)*sqrt(1 - x**2)

def main():
    # A hexagon ABCDEF circumscribed about a unit circle with tangent points (a, b), ..., (m, n)
    # Prove 3 principal diagonals (AD, BE, CF) are concurrent
    a, b, c, d, e, f, g, h, j, k, m, n = symbols('a, b, c, d, e, f, g, h, j, k, m, n')
    AB, BC, CD = tangent(a, b), tangent(c, d), tangent(e, f)
    # AB = tangent(1, 0) can be faster
    DE, EF, FA = tangent(g, h), tangent(j, k), tangent(m, n)
    A, B, C = intersect(FA, AB), intersect(AB, BC), intersect(BC, CD)
    D, E, F = intersect(CD, DE), intersect(DE, EF), intersect(EF, FA)
    print('A:', A)
    print('B:', B)
    print('C:', C)
    print('D:', D)
    print('E:', E)
    print('F:', F)
    print('Are AD, BE and CF concurrent?', expand(fraction(cancel(concurrency(line(A, D), line(B, E), line(C, F))))[0]. \
        subs([sub_y(a, b), sub_y(c, d), sub_y(e, f), sub_y(g, h), sub_y(j, k), sub_y(m, n)])) == 0)

if __name__ == '__main__':
    main()