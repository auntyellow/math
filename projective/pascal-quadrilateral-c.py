from random import randint
from sympy import expand, sqrt
from cartesian import *

def tangent(x0, y0):
    x, y = symbols('x, y')
    return Eq(x0*x + y0*y, 1)

def sub_y(x, y):
    return y, (1 - randint(0, 1)*2)*sqrt(1 - x**2)

def collinear_subs(P1, P2, P3, subs):
    return expand(collinear(P1, P2, P3).lhs.subs(subs)) == 0

def main():
    # A quadrilateral ABCD inscribed in a unit circle with tangent lines aa, bb, cc and dd
    # Prove intersections of 2 opposite tangent lines (aa∩cc and bb∩dd, denoted as E and F), and
    # intersections of 2 opposite edges (AB∩CD and BC∩DA, denoted as G and H), are collinear
    a, b, c, d, e, f, g, h = symbols('a, b, c, d, e, f, g, h')
    A, B, C, D = (a, b), (c, d), (e, f), (g, h)
    AB, BC, CD, DA = line(A, B), line(B, C), line(C, D), line(D, A)
    aa, bb, cc, dd = tangent(a, b), tangent(c, d), tangent(e, f), tangent(g, h)
    E, F, G, H = intersect(aa, cc), intersect(bb, dd), intersect(AB, CD), intersect(DA, BC)
    subs = [sub_y(a, b), sub_y(c, d), sub_y(e, f), sub_y(g, h)]
    print('Are EFG collinear?', collinear_subs(E, F, G, subs))
    print('Are EFH collinear?', collinear_subs(E, F, H, subs))
    # AB∩CD (G), aa∩BC (P) and bb∩DA (Q) are also collinear
    P, Q = intersect(aa, BC), intersect(bb, DA)
    print('Are GPQ collinear?', collinear_subs(G, P, Q, subs))

    # More interesting results:
    # BC∩DA (H), AC∩BD (J), aa∩bb (K) and cc∩dd (L) are also collinear
    AC, BD = line(A, C), line(B, D)
    J, K, L = intersect(AC, BD), intersect(aa, bb), intersect(cc, dd)
    print('Are HKL collinear?', collinear_subs(H, K, L, subs))
    print('Are JKL collinear?', collinear_subs(J, K, L, subs))
    # AB∩CD (G), AC∩BD (J), bb∩cc (M) and dd∩aa (N) are also collinear
    M, N = intersect(bb, cc), intersect(dd, aa)
    print('Are GMN collinear?', collinear_subs(G, M, N, subs))
    print('Are JMN collinear?', collinear_subs(J, M, N, subs))
    # Because E = aa∩cc = KN∩LM and F = bb∩dd = KM∩LN, we have (E, F; G, H) = -1
    # See https://en.wikipedia.org/wiki/Projective_harmonic_conjugate

if __name__ == '__main__':
    main()