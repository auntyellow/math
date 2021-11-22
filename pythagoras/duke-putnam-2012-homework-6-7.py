from sympy import simplify, sqrt
from cartesian import *

def main():
    # https://imomath.com/index.cgi?page=psPutnamPreparationGeometry (Problem 7)
    a, b, r, AC = symbols('a, b, r, AC', positive = True)
    c, x, y = symbols('c, x, y')
    A, B, C, O = (-a, 0), (0, 0), (b, c), (0, r)
    AC0 = sqrt((a + b)**2 + c**2)
    P = (a*(a + b)/AC - a, a*c/AC)
    r = solve(Eq((P[0] - O[0])**2 + (P[1] - O[1])**2, r**2), r)[0]
    print('r =', r)
    BC, BP = line(B, C), line(B, P)
    OH = Eq(y, r - b*x/c)
    T = intersect(BP, OH)
    print('T:', T)
    M = intersect(BC, line(A, T))
    print('M:', M)
    print('M = (B + C)/2 in x?', simplify(simplify(B[0] + C[0] - 2*M[0]).subs(AC, AC0)) == 0)
    print('M = (B + C)/2 in y?', simplify(simplify(B[1] + C[1] - 2*M[1]).subs(AC, AC0)) == 0)

if __name__ == '__main__':
    main()