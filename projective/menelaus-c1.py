from sympy import Eq, cancel, symbols
from cartesian import *

def pair(p1, p2, p3):
    return p1[0] - p2[0], p2[0] - p3[0]

def main():
    # https://en.wikipedia.org/wiki/Menelaus%27s_theorem
    # DEF are collinear => (AF/FB)*(BD/DC)*(CE/EA)=-1
    # Put AB onto x-axis and C onto y-axis
    a, b, c, g, h, x, y = symbols('a, b, c, g, h, x, y')
    A, B, C = (a, 0), (b, 0), (0, c)
    DEF = Eq(y, g*x + h)
    D, E, F = intersect(DEF, line(B, C)), intersect(DEF, line(A, C)), intersect(DEF, line(A, B))
    (AF, FB), (BD, DC), (CE, EA) = pair(A, F, B), pair(B, D, C), pair(C, E, A)
    print(cancel(AF*BD*CE + FB*DC*EA))

if __name__ == '__main__':
    main()