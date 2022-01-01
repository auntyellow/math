from sympy import Eq, solve, symbols
from homogeneous import *

def main():
    a, b, x, y = symbols('a, b, x, y')
    # (A1,A2,A3)->(B1,B2,B3) is an involution, i.e. (A1,A2;A3,B1)=(B1,B2;B3,A1)
    # => A1B1, A2B2 and A3B3 are concurrent
    A1, A2, A3, B1, B2 = (1, 0, 0), (0, 1, 0), (a, b, 1), (1, 1, 1), (0, 0, 1)
    A1A2, A1B1, A1B2, A2A3 = cross(A1, A2), cross(A1, B1), cross(A1, B2), cross(A2, A3)
    A2B1, A2B2, A3B2, B1B2 = cross(A2, B1), cross(A2, B2), cross(A3, B2), cross(B1, B2)
    A2B3, B2B3 = span(x, A1A2, 1, A2B2), span(y, A1B2, 1, A2B2)
    x = solve(Eq(cross_ratio(A1B2, A2B2, A3B2, B1B2), cross_ratio(A2B1, A2B2, A2B3, A1A2)), x)[0]
    x = fraction(x)
    print('x =', x)
    A2B3 = span(x[0], A1A2, x[1], A2B2)
    # Steiner conic: (A1B2,A3B2;B1B2,B2B3)=(A1A2,A2A3;A2B1,A2B3)
    y = solve(Eq(cross_ratio(A1B2, A3B2, B1B2, B2B3), cross_ratio(A1A2, A2A3, A2B1, A2B3)), y)[0]
    y = fraction(y)
    print('y =', y)
    B2B3 = span(y[0], A1B2, y[1], A2B2)
    B3 = cross(A2B3, B2B3)
    print('B3:', B3)
    A3B3 = cross(A3, B3)
    print('Are A1B1, A2B2 and A3B3 concurrent?', incidence(A1B1, A2B2, A3B3) == 0)

if __name__ == '__main__':
    main()