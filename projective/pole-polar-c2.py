from sympy import Eq, solve, symbols
from cartesian import *

def main():
    # https://imomath.com/index.php?options=334 (Theorem 7)
    # (A,B;C,D)=-1 => A(0,a1) and B(b,a) are conjugated, i.e. a1=1/a
    a, b, a1, x, y = symbols('a, b, a1, x, y')
    A, B = (0, a1), (b, a)
    AB = line(A, B)
    circle = Eq(x**2 + y**2, 1)
    roots = solve([AB, circle], (x, y))
    C, D = roots[0], roots[1]
    print(solve(Eq(R(A[0], B[0], C[0], D[0]), -1), a1))

if __name__ == '__main__':
    main()