from sympy import simplify
from cartesian import *

def main():
    # https://imomath.com/index.cgi?page=psPutnamPreparationGeometry (Problem 6)
    a, c, f = symbols('a, c, f', positive = True)
    # a, c, f = 1, 1, 3/4
    x, y = symbols('x, y')
    A, B, C, D, F = (0, a), (0, 0), (c, 0), (c, a), (f, a*f/c)
    BD, AE = Eq(y, a*x/c), Eq(y, a - c*x/a)
    AF, CF = line(A, F), line(C, F)
    BG = Eq(y, f*x/a/(1 - f/c))
    E, G = intersect(BD, AE), intersect(BG, CF)
    print('E:', E)
    print('G:', G)
    GH = Eq(y - G[1], c*(G[0] - x)/a)
    H = (solve(GH, x)[0].subs(y, 0), 0)
    print('H:', H)
    BE2, BG2, EG2, BH2, EH2 = dist2(B, E), dist2(B, G), dist2(E, G), dist2(B, H), dist2(E, H)
    cos2BGE = (BG2 + EG2 - BE2)**2/4/BG2/EG2
    cos2BHE = (BH2 + EH2 - BE2)**2/4/BH2/EH2
    print('cos²∠BGE - cos²∠BHE =', simplify(cos2BGE - cos2BHE))

if __name__ == '__main__':
    main()