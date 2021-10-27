from random import randint
from sympy import expand, sqrt
from cartesian import *

def tangent(x0, y0):
    x, y = symbols('x, y')
    return Eq(x0*x + y0*y, 1)

def sub_y(x, y):
    return y, (1 - randint(0, 1)*2)*sqrt(1 - x**2)

def concurrent(P1, P2, P3, P4, P5, P6, subs):
    return expand(fraction(cancel(concurrency(P1, P2, P3, P4, P5, P6)))[0].subs(subs)) == 0

def main():
    # A quadrilateral ABCD circumscribed about a unit circle with tangent points EFGH
    # Prove 2 diagonals and 2 lines connecting to opposite tangent points (AC, BD, EG, FH) are concurrent
    a, b, c, d, e, f, g, h = symbols('a, b, c, d, e, f, g, h')
    E, F, G, H = (a, b), (c, d), (e, f), (g, h)
    DA, AB, BC, CD = tangent(a, b), tangent(c, d), tangent(e, f), tangent(g, h)
    A, B, C, D = intersect(DA, AB), intersect(AB, BC), intersect(BC, CD), intersect(CD, DA)
    subs = [sub_y(a, b), sub_y(c, d), sub_y(e, f), sub_y(g, h)]
    print('Are AC, EG and FH concurrent?', concurrent(A, C, E, G, F, H, subs))
    # AC, BE and DF are also concurrent
    print('Are AC, BE and DF concurrent?', concurrent(A, C, B, E, D, F, subs))

if __name__ == '__main__':
    main()