from sympy import Eq, solve, symbols
from homogeneous import *

def point_on_conic(conic_z_roots, x0, y0, root = 0):
    f, x, y = symbols('f, x, y')
    return multiplied(x0, y0, conic_z_roots[root].subs(x, x0).subs(y, y0))

def main():
    a, b, c, d, e, f, x, y, z = symbols('a, b, c, d, e, f, x, y, z')
    roots = solve(Eq(a*x**2 + 2*b*x*y + c*y**2 + 2*d*x*z + 2*e*y*z + f*z**2, 0), z)
    print('z =', roots)
    g, h, j, k, m, n, p, q, r, s, t, u = symbols('g, h, j, k, m, n, p, q, r, s, t, u')
    A, B, C = point_on_conic(roots, g, h), point_on_conic(roots, j, k), point_on_conic(roots, m, n)
    D, E, F = point_on_conic(roots, p, q), point_on_conic(roots, r, s), point_on_conic(roots, t, u)
    print('A:', A)
    print('B:', B)
    print('C:', C)
    print('D:', D)
    print('E:', E)
    print('F:', F)
    AB, BC, CD, DE, EF, FA = cross(A, B), cross(B, C), cross(C, D), cross(D, E), cross(E, F), cross(F, A)
    G, H, J = cross(AB, DE), cross(BC, EF), cross(CD, FA) 
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print(incidence(G, H, J))

if __name__ == '__main__':
    main()