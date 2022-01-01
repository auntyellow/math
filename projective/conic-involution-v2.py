from sympy import Eq, solve, symbols
from homogeneous import *

def main():
    a, b, x = symbols('a, b, x')
    # A1B1, A2B2 and A3B3 are concurrent =>
    # (A1,A2;A3,B1)=(B1,B2;B3,A1), i.e. (A1,A2,A3)->(B1,B2,B3) is an involution
    P, A1, A2, A3 = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)
    B1, B2, B3 = span(a, P, 1, A1), span(b, P, 1, A2), span(x, P, 1, A3)
    A1A2, A1B1, A1B2, A2A3, A2B1 = cross(A1, A2), cross(A1, B1), cross(A1, B2), cross(A2, A3), cross(A2, B1)
    A2B2, A2B3, A3B2, B1B2, B2B3 = cross(A2, B2), cross(A2, B3), cross(A3, B2), cross(B1, B2), cross(B2, B3)
    # Steiner conic: (A1B2,A3B2;B1B2,B2B3)=(A1A2,A2A3;A2B1,A2B3)
    x = solve(Eq(cross_ratio(A1B2, A3B2, B1B2, B2B3), cross_ratio(A1A2, A2A3, A2B1, A2B3)), x)
    # two solutions, omit x = 0
    if len(x) == 2 and x[0] == 0:
        x = x[1]
    else:
        x = x[0]
    print('x =', x)
    x = fraction(x)
    B3 = span(x[0], P, x[1], A3)
    print('B3:', B3)
    A2B3 = cross(A2, B3)
    print('(A1,A2;A3,B1) =', cross_ratio(A1B2, A2B2, A3B2, B1B2))
    print('(B1,B2;B3,A1) =', cross_ratio(A2B1, A2B2, A2B3, A1A2))

if __name__ == '__main__':
    main()