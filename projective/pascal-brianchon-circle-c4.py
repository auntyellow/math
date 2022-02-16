from random import randint
from sympy import expand, sqrt
from cartesian import *

def tangent(x0, y0):
    x, y = symbols('x, y')
    return Eq(x0*x + y0*y - 1, 0)

def sub_y(x, y):
    return y, (1 - randint(0, 1)*2)*sqrt(1 - x**2)

def concurrent_subs(L1, L2, L3, subs):
    return expand(fraction(cancel(concurrency(L1, L2, L3)))[0].subs(subs)) == 0

def collinear_subs(P1, P2, P3, subs):
    return expand(collinear(P1, P2, P3).lhs.subs(subs)) == 0

def slope(L):
    p = poly(L.lhs, symbols('x, y'))
    return p.nth(0, 1)/p.nth(1, 0)

def cross_ratio_subs(a, b, c, d, subs):
    return cancel(((a - c)*(b - d)/(a - d)/(b - c)).subs(subs))

def main():
    # A quadrilateral EFGH circumscribed about a unit circle with tangent points ABCD
    a, b, c, d, e, f, g, h = symbols('a, b, c, d, e, f, g, h')
    A, B, C, D = (a, b), (c, d), (e, f), (g, h)
    AA, BB, CC, DD = tangent(a, b), tangent(c, d), tangent(e, f), tangent(g, h)
    print('A\'s Tangent:', AA.lhs, '= 0')
    print('B\'s Tangent:', BB.lhs, '= 0')
    print('C\'s Tangent:', CC.lhs, '= 0')
    print('D\'s Tangent:', DD.lhs, '= 0')
    subs = [sub_y(a, b), sub_y(c, d), sub_y(e, f), sub_y(g, h)]

    # Prove 2 diagonals and 2 lines connecting to opposite tangent points (AC, BD, EG, FH) are concurrent
    E, F, G, H = intersect(AA, BB), intersect(BB, CC), intersect(CC, DD), intersect(DD, AA)
    AC, BD, EG, FH = line(A, C), line(B, D), line(E, G), line(F, H)
    print('AC:', AC.lhs, '= 0')
    print('BD:', BD.lhs, '= 0')
    print('EG:', EG.lhs, '= 0')
    print('FH:', FH.lhs, '= 0')
    print('Are AC, BD, EG and FH concurrent?', concurrent_subs(AC, BD, EG, subs) and concurrent_subs(AC, BD, FH, subs))
    print('(AC,BD;EG,FH) =', cross_ratio_subs(slope(AC), slope(BD), slope(EG), slope(FH), subs))

    # Prove intersections of 2 opposite tangent lines (aa∩cc and bb∩dd, denoted as J and K), and
    # intersections of 2 opposite edges (AB∩CD and BC∩DA, denoted as L and M), are collinear
    AB, BC, CD, DA = line(A, B), line(B, C), line(C, D), line(D, A)
    J, K, L, M = intersect(AA, CC), intersect(BB, DD), intersect(AB, CD), intersect(DA, BC)
    print('J:', J)
    print('K:', K)
    print('L:', L)
    print('M:', M)
    print('Are JKLM collinear?', collinear_subs(J, K, L, subs) and collinear_subs(J, K, M, subs))
    print('(J,K;L,M) =', cross_ratio_subs(J[0], K[0], L[0], M[0], subs))

if __name__ == '__main__':
    main()