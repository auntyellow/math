from sympy import Eq, solve, symbols
from homogeneous import *

def main():
    a, b, x = symbols('a, b, x')
    # A1B1, A2B2 and A3B3 are concurrent =>
    # (A1,A2;A3,B1)=(B1,B2;B3,A1), i.e. (A1,A2,A3)->(B1,B2,B3) is an involution
    A1, A2, A3, B1, B2 = (1, 0, 0), (0, 1, 0), (a, b, 1), (1, 1, 1), (0, 0, 1)
    A1A2, A1B2, A2B1, A2B2, A3B2, B1B2 = cross(A1, A2), cross(A1, B2), cross(A2, B1), cross(A2, B2), cross(A3, B2), cross(B1, B2)
    A2B3 = span(x, A1A2, 1, A2B2)
    C12, C23 = cross(A1B2, A2B1), cross(A2B3, A3B2)
    print('C12:', C12)
    print('C23:', C23)
    # construct B3 by projective axis C
    C13 = cross(cross(A3, B1), cross(C12, C23))
    B3 = cross(A2B3, cross(A1, C13))
    print('B3:', B3)
    A1B1, A3B3 = cross(A1, B1), cross(A3, B3)
    x = solve(Eq(incidence(A1B1, A2B2, A3B3), 0), x)[0]
    print('x =', x)
    x = fraction(x)
    A2B3 = span(x[0], A1A2, x[1], A2B2)
    print('(A1,A2;A3,B1) =', cross_ratio(A1B2, A2B2, A3B2, B1B2))
    print('(B1,B2;B3,A1) =', cross_ratio(A2B1, A2B2, A2B3, A1A2))

if __name__ == '__main__':
    main()