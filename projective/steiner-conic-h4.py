from sympy import cancel, expand, poly, symbols
from homogeneous import *

def intersect(u, v):
    a, b, c, d, e = symbols('a, b, c, d, e')
    return (v*(e*u - d*v), u*(d*v - e*u), a*v**2 - b*u*v + c*u**2)

def cross_ratio(a, b, c, d):
    return cancel((a - c)*(b - d)/(a - d)/(b - c))

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, x, y, z = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, x, y, z')
    P = intersect(g, h)
    print('P:', P)
    print('Is P on conic?', expand((a*x**2 + b*x*y + c*y**2 + d*x*z + e*y*z).subs(x, P[0]).subs(y, P[1]).subs(z, P[2])) == 0)
    B, C, D, E, F = intersect(0, 1), intersect(g, h), intersect(j, k), intersect(m, n), intersect(p, q)
    print('(AC,AD;AE,AF) =', cross_ratio(h/g, k/j, n/m, q/p))
    BC, BD, BE, BF = cross(B, C), cross(B, D), cross(B, E), cross(B, F)
    print('BC:', BC)
    print('BD:', BD)
    print('BE:', BE)
    print('BF:', BF)
    print('(BC,BD;BE,BF) =', cross_ratio(BC[1]/BC[0], BD[1]/BD[0], BE[1]/BE[0], BF[1]/BF[0]))

if __name__ == '__main__':
    main()