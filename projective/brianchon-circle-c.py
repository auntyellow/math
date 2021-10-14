from sympy import cos, sin
from cartesian_s import *

def tangent(t):
    x, y = symbols('x, y')
    return Eq(x*cos(t) + y*sin(t), 1)

def main():
    # A hexagon ABCDEF circumscribed about a unit circle with tangent points' polar angles t1..t6
    # Prove 3 principal diagonals (AD, BE, CF) are concurrent
    t1, t2, t3, t4, t5, t6 = symbols('t1, t2, t3, t4, t5, t6')
    AB, BC, CD, DE, EF, FA = tangent(t1), tangent(t2), tangent(t3), tangent(t4), tangent(t5), tangent(t6)
    A, B, C = intersect(FA, AB), intersect(AB, BC), intersect(BC, CD)
    D, E, F = intersect(CD, DE), intersect(DE, EF), intersect(EF, FA)
    print('A:', A)
    print('B:', B)
    print('C:', C)
    print('D:', D)
    print('E:', E)
    print('F:', F)
    print('Are AD, BE and CF concurrent?', concurrency(A, D, B, E, C, F) == 0)

if __name__ == '__main__':
    main()