from sympy import Eq, solve, symbols
from cartesian import *

def pair(p1, p2, p3):
    return p1[0] - p2[0], p2[0] - p3[0]

def main():
    # https://en.wikipedia.org/wiki/Menelaus%27s_theorem
    # (AF/FB)*(BD/DC)*(CE/EA)=-1 => DEF are collinear
    # Put AB onto x-axis and C onto y-axis
    a, b, c, d, e, f, x, y = symbols('a, b, c, d, e, f, x, y')
    A, B, C, D, E, F = (a, 0), (b, 0), (0, c), (d, (1 - d / b) * c), (e, (1 - e / a) * c), (f, 0)
    (AF, FB), (BD, DC), (CE, EA) = pair(A, F, B), pair(B, D, C), pair(C, E, A)
    F = (solve(Eq(AF * BD * CE + FB * DC * EA, 0), f)[0], 0)
    print(collinear(D, E, F))

if __name__ == '__main__':
    main()