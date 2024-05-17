from sympy import Matrix, Poly
from cartesian import *

# ISBN 9787040316988, p300, ex 6.1.10

def line_coef(L):
    p = Poly(L.lhs - L.rhs, symbols('x, y'))
    return [p.nth(1, 0), p.nth(0, 1), p.nth(0, 0)]

def concurrency(L1, L2, L3):
    return Matrix([line_coef(L1), line_coef(L2), line_coef(L3)]).det()

def main():
    a, b, c, k = symbols('a, b, c, k', positive = True)
    A, B, C = (-a, 0), (b, 0), (0, c)
    D, E, F = (b/2, c/2), (-a/2, c/2), ((b - a)/2, 0)
    A1, B1, C1 = (b/2 + k*c, c/2 + k*b), (-a/2 - k*c, c/2 + k*a), ((b - a)/2, -k*(a + b))
    AA1, BB1, CC1 = line(A, A1), line(B, B1), line(C, C1)
    print('Are AA\', BB\' and CC\' concurrent?', concurrency(AA1, BB1, CC1) == 0)

if __name__ == '__main__':
    main()