from sympy import Eq, poly, solve, symbols
from homogeneous import *

def subs_all(P, subs):
    return reduced(P[0].subs(subs), P[1].subs(subs), P[2].subs(subs))

def lies_on(P, L):
    return expand(P[0]*L[0] + P[1]*L[1] + P[2]*L[2]) == 0

def on_conic(P):
    a, b, c, d, e, f = symbols('a, b, c, d, e, f')
    x, y, z = P
    return a*x**2 + 2*b*x*y + c*y**2 + 2*d*x*z + 2*e*y*z + f*z**2

def main():
    t, u0, v0, w0, x, y, z, x0, y0, z0, x1, y1, z1 = symbols('t, u0, v0, w0, x, y, z, x0, y0, z0, x1, y1, z1')
    P, Q = (x0, y0, z0), (x, y, z)
    M = span(1, P, t, Q)
    t = solve(Eq(on_conic(M), 0), t)
    M, N = span(1, P, t[0], Q), span(1, P, t[1], Q)
    print('M:', M)
    print('N:', N)
    cr = fraction(cross_ratio(P, Q, M, N))
    p_poly = poly(cr[0] + cr[1], (x, y, z))
    p = reduced(p_poly.nth(1, 0, 0), p_poly.nth(0, 1, 0), p_poly.nth(0, 0, 1))
    print('P\'s Polar:', p)
    R = cross(p, (u0, v0, w0))
    print('Arbitrary point R on P\'s Polar:', R)
    r = subs_all(p, [(x0, x1), (y0, y1), (z0, z1), (x1, R[0]), (y1, R[1]), (z1, R[2])])
    print('R\'s Polar:', r)
    print('Is P on R\'s Polar?', lies_on(P, r))

if __name__ == '__main__':
    main()