from sympy import cos, sin
from cartesian_s import *

def line_t(t1, t2):
    return line((cos(t1), sin(t1)), (cos(t2), sin(t2)))

def perpendicular(P1, P2, P3):
    return simplify((P1[0] - P2[0])*P3[0] + (P1[1] - P2[1])*P3[1])

def main():
    # https://www.imomath.com/index.php?options=334 (Theorem 9)
    t1, t2, t3, t4 = symbols('t1, t2, t3, t4')
    # t1 = 0 can be faster
    AB, AC, AD = line_t(t1, t2), line_t(t1, t3), line_t(t1, t4)
    BC, BD, CD = line_t(t2, t3), line_t(t2, t4), line_t(t3, t4)
    E, F, G = intersect(AB, CD), intersect(AD, BC), intersect(AC, BD)
    print('E:', E)
    print('F:', F)
    print('G:', G)
    print('Is EF perpendicular to OG?', perpendicular(E, F, G) == 0)
    print('Is FG perpendicular to OE?', perpendicular(F, G, E) == 0)
    print('Is GE perpendicular to OF?', perpendicular(G, E, F) == 0)

if __name__ == '__main__':
    main()