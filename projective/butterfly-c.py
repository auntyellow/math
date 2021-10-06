from sympy import Eq, simplify, solve, symbols
from cartesian import *

def pair(conic, line):
    x, y = symbols('x, y')
    p = solve([conic, Eq(y, line)], (x, y))
    return (simplify(p[0][0]), simplify(p[0][1])), (simplify(p[1][0]), simplify(p[1][1]))

def main():
    a, b, c, d, e, f, q, r, x, y = symbols('a, b, c, d, e, f, q, r, x, y')
    conic = Eq(a*x**2 + b*x*y + c*y**2 + d*x + e*y + f, 0)
    A, B = pair(conic, 0)
    P, Q = pair(conic, q*x)
    R, S = pair(conic, r*x)
    AB = Eq(y, 0)
    PS, QR = line(P, S), line(Q, R)
    C, D = intersect(AB, PS), intersect(AB, QR)
    print(simplify(1 / A[0] + 1 / B[0]))
    print(simplify(1 / C[0] + 1 / D[0]))

if __name__ == '__main__':
    main()