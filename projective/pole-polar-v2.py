from sympy import Eq, Matrix, factor, poly, solve, symbols
from homogeneous import *

def subs_all(P, t, u):
    return P[0].subs(t, u), P[1].subs(t, u), P[2].subs(t, u)

def lies_on(P, L):
    return expand(P[0]*L[0] + P[1]*L[1] + P[2]*L[2]) == 0

def coeff_matrix(p):
    a, b, c, d, e, f = p.nth(2, 0, 0), p.nth(1, 1, 0), p.nth(0, 2, 0), p.nth(1, 0, 1), p.nth(0, 1, 1), p.nth(0, 0, 2)
    return Matrix([[a, b/2, d/2], [b/2, c, e/2], [d/2, e/2, f]])

def main():
    a, b, t, u, v, w, x, y, z = symbols('a, b, t, u, v, w, x, y, z')
    # results from steiner-conic-v.py
    P, M = (x, y, z), (t*(a + t), t*(b + t), (a + t)*(b + t))
    N = subs_all(M, t, u)
    u = solve(Eq(incidence(P, M, N), 0), u)
    u = u[1] if u[0] == t else u[0]
    N = multiplied(u*(a + u), u*(b + u), (a + u)*(b + u))
    print('N:', N)
    Q = span(1, M, v, P)
    v = fraction(cancel(solve(Eq(cross_ratio(P, Q, M, N), -1), v)[0]))
    Q = span(v[1], M, v[0], P)
    print('Q:', Q)
    polarP = cross(Q, subs_all(Q, t, w))
    print('P\'s Polar:', polarP)
    xx, yy, zz = symbols('xx, yy, zz')
    subs = [(x, xx), (y, yy), (z, zz), (xx, Q[0]), (yy, Q[1]), (zz, Q[2])]
    polarQ = reduced(polarP[0].subs(subs), polarP[1].subs(subs), polarP[2].subs(subs))
    print('Q\'s Polar:', polarQ)
    print('Is P on Q\'s Polar?', lies_on(P, polarQ))

    subs = [(x, M[0]), (y, M[1]), (z, M[2])]
    m = reduced(polarP[0].subs(subs), polarP[1].subs(subs), polarP[2].subs(subs))
    print('M\'s Tangent Line m:', factor(m))
    print('Is M on m?', lies_on(M, m))
    t0, t1, t2, t3, t4 = symbols('t0, t1, t2, t3, t4')
    m0, m1, m2, m3, m4 = subs_all(m, t, t0), subs_all(m, t, t1), subs_all(m, t, t2), subs_all(m, t, t3), subs_all(m, t, t4)
    m_m1, m_m2, m_m3, m_m4 = cross(m, m1), cross(m, m2), cross(m, m3), cross(m, m4)
    print('(m m1,m m2;m m3,m m4) =', cross_ratio(m_m1, m_m2, m_m3, m_m4))
    m0m1, m0m2, m0m3, m0m4 = cross(m0, m1), cross(m0, m2), cross(m0, m3), cross(m0, m4)
    print('(m0m1,m0m2;m0m3,m0m4) =', cross_ratio(m0m1, m0m2, m0m3, m0m4))

    u, v, w = symbols('u, v, w')
    m4 = (u, v, w)
    m_m4, m0m4 = cross(m, m4), cross(m0, m4)
    cr = fraction(cross_ratio(m_m1, m_m2, m_m3, m_m4))
    cr0 = fraction(cross_ratio(m0m1, m0m2, m0m3, m0m4))
    p = expand(cr[0]*cr0[1] - cr[1]*cr0[0])
    print('Quadric Equation:', factor(p), '= 0')
    print('Are they equivalent?', expand(p.subs(u, m[0]).subs(v, m[1]).subs(w, m[2])) == 0);

    point_coeffs = coeff_matrix(poly(a*x*y - a*y*z - b*x*y + b*x*z, (x, y, z)))
    line_coeffs = coeff_matrix(poly(a**2*u**2 + 2*a**2*u*w + a**2*w**2 + 2*a*b*u*v - 2*a*b*u*w - 2*a*b*v*w - 2*a*b*w**2 + b**2*v**2 + 2*b**2*v*w + b**2*w**2, (u, v, w)))
    print('Coefficients of Point Conic:', point_coeffs)
    print('Coefficients of Line Conic:', line_coeffs)
    print('Their Product:', expand(point_coeffs*line_coeffs))

if __name__ == '__main__':
    main()