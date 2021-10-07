from sympy import Eq, solve, symbols
from cartesian import *

def main():
    # https://imomath.com/index.php?options=334 (Theorem 7)
    # A and B are conjugated => (A,B;C,D)=-1
    a, b, x, y = symbols('a, b, x, y')
    A, B = (0, 1/a), (b, a)
    AB = line(A, B)
    circle = Eq(x**2 + y**2, 1)
    roots = solve([AB, circle], (x, y))
    C, D = roots[0], roots[1]
    print(cross_ratio(A[0], B[0], C[0], D[0]))

if __name__ == '__main__':
    main()