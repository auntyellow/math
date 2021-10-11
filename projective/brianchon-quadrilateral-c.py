from sympy import cos, sin, symbols
from cartesian_s import *

def tangent(t):
    x, y = symbols('x, y')
    return Eq(x*cos(t) + y*sin(t), 1)

def point(t):
    return cos(t), sin(t)

def main():
    # A quadrilateral ABCD circumscribed about a unit circle with tangent points EFGH
    # Prove 2 diagonals and 2 lines connecting to opposite tangent points (AC, BD, EG, FH) are concurrent
    t1, t2, t3, t4 = symbols('t1, t2, t3, t4')
    DA, AB, BC, CD = tangent(t1), tangent(t2), tangent(t3), tangent(t4)
    A, B, C, D = intersect(DA, AB), intersect(AB, BC), intersect(BC, CD), intersect(CD, DA)
    E, F, G, H = point(t1), point(t2), point(t3), point(t4)
    print(concurrency(A, C, E, G, F, H))
    # AC, BE and DF are also concurrent
    print(concurrency(A, C, B, E, D, F))

if __name__ == '__main__':
    main()