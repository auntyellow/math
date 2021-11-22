from random import randint
from sympy import sqrt, expand
from cartesian import *

def perpendicular(P1, P2, P3, subs):
    return expand(fraction(cancel((P1[0] - P2[0])*P3[0] + (P1[1] - P2[1])*P3[1]))[0].subs(subs)) == 0

def sub_y(x, y):
    return y, (1 - randint(0, 1)*2)*sqrt(1 - x**2)

def main():
    # https://imomath.com/index.cgi?page=polePolarBrianchonBrokard (Theorem 9)
    a, b, c, d, e, f, g, h = symbols('a, b, c, d, e, f, g, h')
    A, B, C, D = (a, b), (c, d), (e, f), (g, h)
    AB, AC, AD, BC, BD, CD = line(A, B), line(A, C), line(A, D), line(B, C), line(B, D), line(C, D)
    E, F, G = intersect(AB, CD), intersect(AD, BC), intersect(AC, BD)
    print('E:', E)
    print('F:', F)
    print('G:', G)
    subs = [sub_y(a, b), sub_y(c, d), sub_y(e, f), sub_y(g, h)]
    print('Is EF perpendicular to OG?', perpendicular(E, F, G, subs))
    print('Is FG perpendicular to OE?', perpendicular(F, G, E, subs))
    print('Is GE perpendicular to OF?', perpendicular(G, E, F, subs))

if __name__ == '__main__':
    main()