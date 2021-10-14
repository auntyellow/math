from sympy import cos, sin
from cartesian_s import *

def line_t(t1, t2):
    return line((cos(t1), sin(t1)), (cos(t2), sin(t2)))

def main():
    # A hexagon ABCDEF inscribed in a unit circle with polar angles t1..t6
    # Prove 3 intersections of opposite edges (AB∩DE, BC∩EF, CD∩FA) are collinear
    t1, t2, t3, t4, t5, t6 = symbols('t1, t2, t3, t4, t5, t6')
    AB, BC, CD = line_t(t1, t2), line_t(t2, t3), line_t(t3, t4)
    DE, EF, FA = line_t(t4, t5), line_t(t5, t6), line_t(t6, t1)
    G, H, K = intersect(AB, DE), intersect(BC, EF), intersect(CD, FA)
    print('G:', G)
    print('H:', H)
    print('K:', K)
    print('Are GHK collinear?', collinear(G, H, K))

if __name__ == '__main__':
    main()