from sympy import Eq, solve, symbols
from homogeneous import *

def main():
    a, b, x = symbols('a, b, x')
    # (A,B,C)->(D,E,F) is an involution, i.e. (A,B;C,D)=(D,E;F,A) => AD, BE and CF are concurrent
    A, B, C, D, E = (1, 0, 0), (0, 1, 0), (a, b, 1), (1, 1, 1), (0, 0, 1)
    AB, AD, AE, BD, BE, CE, DE = cross(A, B), cross(A, D), cross(A, E), cross(B, D), cross(B, E), cross(C, E), cross(D, E)
    BF = span(x, AB, 1, BE)
    crE = fraction(cross_ratio(AE, BE, CE, DE))
    crB = fraction(cross_ratio(BD, BE, BF, AB))
    x = solve(Eq(crE[0]*crB[1], crE[1]*crB[0]), x)[0]
    print('x =', x)
    x = fraction(x)
    BF = span(x[0], AB, x[1], BE)
    G, H = cross(BD, CE), cross(AE, BF)
    print('G:', G)
    print('H:', H)
    GH = cross(G, H)
    # solve F by Pascal's theorem
    # J = cross(AD, cross(G, H))
    # F = cross(BF, cross(C, J)) 
    # Are AD, BE and CF concurrent?
    # Replace CF with GH, so F is not necessary
    print('Are AD, BE and GH concurrent?', incidence(AD, BE, GH) == 0)

if __name__ == '__main__':
    main()