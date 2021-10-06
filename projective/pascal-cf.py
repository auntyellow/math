from sympy import Eq, simplify, solve, symbols
from cartesian import *
from homogeneous import *

def pair(conic, line):
    x, y = symbols('x, y')
    p = solve([conic, Eq(y, line)], (x, y))
    return (simplify(p[0][0]), simplify(p[0][1])), (simplify(p[1][0]), simplify(p[1][1]))

def to_homogeneous(P, denominator):
    return simplify(P[0]*denominator), simplify(P[1]*denominator), simplify(denominator)

def main():
    a, b, c, d, e, f, g, h, k, x, y = symbols('a, b, c, d, e, f, g, h, k, x, y')
    conic = Eq(a*x**2 + b*x*y + c*y**2 + d*x + e*y + f, 0)
    (F, A), (D, C), (B, E) = pair(conic, g*x), pair(conic, h*x), pair(conic, k)
    print('x_A =', A[0])
    print('x_B =', B[0])
    print('x_C =', C[0])
    print('x_D =', D[0])
    print('x_E =', E[0])
    print('x_F =', F[0])
    F, A = to_homogeneous(F, 2*(a + b*g + c*g**2)), to_homogeneous(A, 2*(a + b*g + c*g**2))
    D, C = to_homogeneous(D, 2*(a + b*h + c*h**2)), to_homogeneous(C, 2*(a + b*h + c*h**2))
    B, E = to_homogeneous(B, 2*a), to_homogeneous(E, 2*a)
    print('A:', A)
    print('B:', B)
    print('C:', C)
    print('D:', D)
    print('E:', E)
    print('F:', F)
    AB, BC, CD, DE, EF, FA = cross(A, B), cross(B, C), cross(C, D), cross(D, E), cross(E, F), cross(F, A)
    print('AB:', AB)
    print('BC:', BC)
    print('CD:', CD)
    print('DE:', DE)
    print('EF:', EF)
    print('FA:', FA)
    G, H, J = cross(AB, DE), cross(BC, EF), cross(CD, FA) 
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print(incidence(G, H, J))

if __name__ == '__main__':
    main()