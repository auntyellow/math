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
    u1, u2, u3, u4, x1, x2, x3 = symbols('u1, u2, u3, u4, x1, x2, x3')
    A, B, C, F, E, D, H = (0, 0), (1, 0), (u1, u2), (u1, 0), (u3, x1), (u4, x2), (u1, x3)
    # collinearities of ACE and BCD are not necessary
    # h0 = det(collinear, C, A, E)
    # h0 = det(collinear, B, C, D)
    h1 = perpendicular(C, A, E, B)
    h2 = perpendicular(B, C, D, A)
    h3 = det(collinear, A, D, H)
    g = det(collinear, B, E, H)

    print('h3 =', h3, vars(h3))
    print('h2 =', h2, vars(h2))
    print('h1 =', h1, vars(h1))
    print('g =', g, vars(g))
    print()

    R = prem(g, h3, x3)
    print('R(x3) =', R, vars(R))
    R = prem(R, h2, x2)
    print('R(x2) =', R, vars(R))
    R = prem(R, h1, x1)
    print('R(x1) =', R)
    print()

    # ISBN 9787040316988, p297, theorem 6.1.4
    G = groebner([h1, h2, h3], x1, x2, x3)
    print(G, len(G))
    print(G.reduce(g))
    print()

    # theorem 6.1.5
    z = symbols('z')
    G = groebner([h1, h2, h3, 1 - z*g], x1, x2, x3, z)
    print(G)

if __name__ == '__main__':
    main()