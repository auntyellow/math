from sympy import Eq, cancel, expand, solve, sqrt, symbols
from cartesian import *

def pair(conic, line):
    x, y = symbols('x, y')
    p = solve([conic, Eq(y, line)], (x, y))
    return (cancel(p[0][0]), cancel(p[0][1])), (cancel(p[1][0]), cancel(p[1][1]))

def main():
    a, b, c, d, e, f, g, h, k, x, y, P, Q, R = symbols('a, b, c, d, e, f, g, h, k, x, y, P, Q, R')
    conic = Eq(a*x**2 + 2*b*x*y + c*y**2 + 2*d*x + 2*e*y + f, 0)
    (F, A), (D, C), (B, E) = pair(conic, g*x), pair(conic, h*x), pair(conic, k)
    print('x_A =', A[0])
    print('x_B =', B[0])
    print('x_C =', C[0])
    print('x_D =', D[0])
    print('x_E =', E[0])
    print('x_F =', F[0])

    subs = {a: 1, b: 0, c: 1, d: 0, e: 0, f: -1, g: 1, h: -1, k: 0}
    print('x_A =', A[0].evalf(subs = subs))
    print('x_B =', B[0].evalf(subs = subs))
    print('x_C =', C[0].evalf(subs = subs))
    print('x_D =', D[0].evalf(subs = subs))
    print('x_E =', E[0].evalf(subs = subs))
    print('x_F =', F[0].evalf(subs = subs))

    P0 = sqrt(-a*f - 2*b*f*g - c*f*g**2 + d**2 + 2*d*e*g + e**2*g**2)
    Q0 = sqrt(-a*f - 2*b*f*h - c*f*h**2 + d**2 + 2*d*e*h + e**2*h**2)
    R0 = sqrt(-a*c*k**2 - 2*a*e*k - a*f + b**2*k**2 + 2*b*d*k + d**2)
    A = A[0].subs(P0, P), A[1].subs(P0, P)
    B = B[0].subs(R0, R), B[1].subs(R0, R)
    C = C[0].subs(Q0, Q), C[1].subs(Q0, Q)
    D = D[0].subs(Q0, Q), D[1].subs(Q0, Q)
    E = E[0].subs(R0, R), E[1].subs(R0, R)
    F = F[0].subs(P0, P), F[1].subs(P0, P)
    print('A:', A)
    print('B:', B)
    print('C:', C)
    print('D:', D)
    print('E:', E)
    print('F:', F)
    AB, DE, BC, EF = line(A, B), line(D, E), line(B, C), line(E, F)
    G, H = intersect(AB, DE), intersect(BC, EF)
    print('G:', G)
    print('H:', H)
    determinant = fraction(cancel(G[0]*H[1] - G[1]*H[0]))[0]
    print('G, H and J are collinear if and only if', determinant, '= 0')
    print('Are G, H and J collinear?', expand(determinant.subs(P, P0).subs(Q, Q0).subs(R, R0)) == 0)

if __name__ == '__main__':
    main()