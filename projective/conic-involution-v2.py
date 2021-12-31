from sympy import Eq, solve, symbols
from homogeneous import *

def main():
    a, b, x = symbols('a, b, x')
    # AD, BE and CF are concurrent => (A,B;C,D)=(D,E;F,A), i.e. (A,B,C)->(D,E,F) is an involution
    A, B, C, D, E = (1, 0, 0), (0, 1, 0), (a, b, 1), (1, 1, 1), (0, 0, 1)
    AB, AD, AE, BD, BE, CE, DE = cross(A, B), cross(A, D), cross(A, E), cross(B, D), cross(B, E), cross(C, E), cross(D, E)
    BF = span(x, AB, 1, BE)
    G, H, J = cross(BD, CE), cross(AE, BF), cross(AD, BE)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    # solve x by Pascal's theorem
    x = solve(Eq(incidence(G, H, J), 0), x)[0]
    print('x =', x)
    x = fraction(x)
    BF = span(x[0], AB, x[1], BE)
    print('(A,B;C,D) =', cross_ratio(AE, BE, CE, DE))
    print('(D,E;F,A) =', cross_ratio(BD, BE, BF, AB))

if __name__ == '__main__':
    main()