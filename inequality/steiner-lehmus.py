from sympy import factor
from cartesian import *

def main():
    # https://en.wikipedia.org/wiki/Steiner%E2%80%93Lehmus_theorem
    a, b, r = symbols('a, b, r', positive = True)
    A, B, C, I = (-a, 0), (b, 0), ((a - b)*r**2/(a*b - r**2), 2*a*b*r/(a*b - r**2)), (0, r)
    AC, BC, AD, BE = line(A, C), line(B, C), line(A, I), line(B, I)
    D, E = intersect(AD, BC), intersect(BE, AC)
    print('D:', D)
    print('E:', E)
    print('AD**2 - BE**2 =', factor(dist2(A, D) - dist2(B, E)))
    # should prove this factor is always negative:
    p = -a**4*b**2 - 4*a**3*b**3 - a**2*b**4 + 5*a**2*b**2*r**2 - 4*a*b*r**4 + r**6

if __name__ == '__main__':
    main()