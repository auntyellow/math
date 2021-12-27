from sympy import cancel, expand, poly, symbols
from homogeneous import *

def intersect(x, z):
    a, b, d, e, f = symbols('a, b, d, e, f')
    return (z*(e*x - b*z), a*z**2 - d*x*z + f*x**2, x*(b*z - e*x))

def cross_ratio(a, b, c, d):
    return cancel((a - c)*(b - d)/(a - d)/(b - c))

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, u, v, w = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, u, v, w')
    L = intersect(g, h)
    print('Line L:', L)
    print('Is line L tangent to conic?', expand((a*u**2 + b*u*v + d*u*w + e*v*w + f*w**2).subs(u, L[0]).subs(v, L[1]).subs(w, L[2])) == 0)
    B, C, D, E, F = intersect(1, 0), intersect(g, h), intersect(j, k), intersect(m, n), intersect(p, q)
    print('(AC,AD;AE,AF) =', cross_ratio(g/h, j/k, m/n, p/q))
    BC, BD, BE, BF = cross(B, C), cross(B, D), cross(B, E), cross(B, F)
    print('Point BC:', BC)
    print('Point BD:', BD)
    print('Point BE:', BE)
    print('Point BF:', BF)
    print('(BC,BD;BE,BF) =', cross_ratio(BC[0]/BC[2], BD[0]/BD[2], BE[0]/BE[2], BF[0]/BF[2]))

if __name__ == '__main__':
    main()