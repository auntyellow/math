from sympy import *

def collinear(P):
    return [P[0], P[1], 1]

def det(row_def, *points):
    mat = []
    for point in points:
        mat.append(row_def(point))
    return Matrix(mat).det()

def perpendicular(P1, P2, P3, P4):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = P1, P2, P3, P4
    return (x1 - x2)*(x3 - x4) + (y1 - y2)*(y3 - y4)

def vars(expr):
    return sorted(expr.free_symbols, key = lambda s: s.name)

def main():
    var('x1:8')
    A, B, C, F, E, D, H = (0, 0), (1, 0), (x1, x2), (x1, 0), (x3, x4), (x5, x6), (x1, x7)
    # collinearities of ACE and BCD are not necessary
    # h0 = det(collinear, C, A, E)
    # h0 = det(collinear, B, C, D)
    h1 = perpendicular(C, A, E, B)
    h2 = perpendicular(B, C, D, A)
    h3 = det(collinear, A, D, H)
    g = det(collinear, B, E, H)

    print('h3 =', h3, vars(h3))
    # h3a = prem(h4, h3, x6) # eliminate x6, resultant(h4, h3, x6) also works
    # print('h3a =', h3a, vars(h3a))
    print('h2 =', h2, vars(h2))
    print('h1 =', h1, vars(h1))
    # h1a = prem(h2, h1, x4) # eliminate x4, resultant(h2, h1, x4) also works
    # print('h1a =', h1a, vars(h1a))
    print('g =', g, vars(g))
    print()

    R = prem(g, h3, x7)
    print('R(x7) =', R, vars(R))
    R = prem(R, h2, x6)
    print('R(x6) =', factor(R), vars(R))
    # prem about x5 doesn't prove
    R = prem(R, h1, x4)
    print('R(x4) =', R)
    print()

    # ISBN 9787040316988, p297, theorem 6.1.4, x1, x2, x3 and x5 are free variables
    G = groebner([h1, h2, h3], x4, x6, x7)
    print(G, len(G))
    print(G.reduce(g))
    print()

    # theorem 6.1.5
    z = symbols('z')
    G = groebner([h1, h2, h3, 1 - z*g], x4, x6, x7, z)
    print(G)

if __name__ == '__main__':
    main()