from sympy import Eq, symbols
from cartesian import *

def main():
    # AEC and DBF are collinear respectively, and G=AB∩DE, H=BC∩EF, J=AF∩CD. Prove GHJ are collinear.
    # Put J onto the origin, and make BFD parallel to x-axis
    a, b, c, e, f, g, h, x, y = symbols('a, b, c, e, f, g, h, x, y')
    AC, DF, AF, CD = Eq(y, a*x + c), Eq(y, f), Eq(y, g*x), Eq(y, h*x)
    B, E = (b, f), (e, a*e + c)
    A, C, D, F = intersect(AC, AF), intersect(AC, CD), intersect(DF, CD), intersect(DF, AF)
    AB, BC, DE, EF = line(A, B), line(B, C), line(D, E), line(E, F)
    G, H, J = intersect(AB, DE), intersect(BC, EF), (0, 0)
    print(collinear(G, H, J))

if __name__ == '__main__':
    main()