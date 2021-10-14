from sympy import cos, sin
from cartesian_s import *

def line_t(t1, t2):
    return line((cos(t1), sin(t1)), (cos(t2), sin(t2)))

def tangent(t):
    x, y = symbols('x, y')
    return Eq(x*cos(t) + y*sin(t), 1)

def main():
    # A quadrilateral ABCD inscribed in a unit circle with tangent lines abcd
    # Prove intersections of 2 opposite tangent lines (a∩c and b∩d, denoted as E and F), and
    # intersections of 2 opposite edges (AB∩CD and BC∩DA, denoted as G and H), are collinear
    t1, t2, t3, t4 = symbols('t1, t2, t3, t4')
    AB, BC, CD, DA = line_t(t1, t2), line_t(t2, t3), line_t(t3, t4), line_t(t4, t1)
    a, b, c, d = tangent(t1), tangent(t2), tangent(t3), tangent(t4)
    E, F, G, H = intersect(a, c), intersect(b, d), intersect(AB, CD), intersect(DA, BC)
    print('Are EFG collinear?', collinear(E, F, G))
    print('Are EFH collinear?', collinear(E, F, H))
    # AB∩CD (G), a∩BC (P) and b∩DA (Q) are also collinear
    P, Q = intersect(a, BC), intersect(b, DA)
    print('Are GPQ collinear?', collinear(G, P, Q))

    # More interesting results:
    # BC∩DA (H), AC∩BD (J), a∩b (K) and c∩d (L) are also collinear
    AC, BD = line_t(t1, t3), line_t(t2, t4)
    J, K, L = intersect(AC, BD), intersect(a, b), intersect(c, d)
    print('Are HKL collinear?', collinear(H, K, L))
    print('Are JKL collinear?', collinear(J, K, L))
    # AB∩CD (G), AC∩BD (J), b∩c (M) and d∩a (N) are also collinear
    M, N = intersect(b, c), intersect(d, a)
    print('Are GMN collinear?', collinear(G, M, N))
    print('Are JMN collinear?', collinear(J, M, N))
    # Because E = a∩c = KN∩LM and F = b∩d = KM∩LN, we have (E, F; G, H) = -1
    # See https://en.wikipedia.org/wiki/Projective_harmonic_conjugate

if __name__ == '__main__':
    main()