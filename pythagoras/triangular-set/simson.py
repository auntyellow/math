from sympy import *

def collinear(P):
    return [P[0], P[1], 1]

def concyclic(P):
    x, y = P
    return [x**2 + y**2, x, y, 1]

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
    # https://en.wikipedia.org/wiki/Simson_line
    u1, u2, u3, x1, x2, x3, x4, x5 = symbols('u1, u2, u3, x1, x2, x3, x4, x5')
    A, B, C, P, F, E, D = (0, 0), (1, 0), (u1, u2), (u3, x1), (u3, 0), (x2, x3), (x4, x5)
    h1 = det(concyclic, A, B, C, P)
    h2 = det(collinear, C, A, E)
    h3 = perpendicular(C, A, E, P)
    h4 = det(collinear, B, C, D)
    h5 = perpendicular(B, C, D, P)
    g = det(collinear, D, E, F)

    print('h5 =', h5, vars(h5))
    print('h4 =', h4, vars(h4))
    h4a = prem(h5, h4, x5) # eliminate x5, resultant(h5, h4, x5) also works
    print('h4a =', h4a, vars(h4a))
    print('h3 =', h3, vars(h3))
    print('h2 =', h2, vars(h2))
    h2a = prem(h3, h2, x3) # eliminate x3, resultant(h3, h2, x3) also works
    print('h2a =', h2a, vars(h2a))
    print('h1 =', h1, vars(h1))
    print('g =', g, vars(g))
    print()

    R = prem(g, h5, x5)
    print('R(x5) =', R, vars(R))
    R = prem(R, h4a, x4)
    print('R(x4) =', R, vars(R))
    R = prem(R, h3, x3)
    print('R(x3) =', R, vars(R))
    R = prem(R, h2a, x2)
    print('R(x2) =', R, vars(R))
    R = prem(R, h1, x1)
    print('R(x1) =', R)
    print()

    # ISBN 9787040316988, p297, theorem 6.1.4
    G = groebner([h1, h2, h3, h4, h5], x1, x2, x3, x4, x5)
    print(G, len(G))
    print(G.reduce(g))
    print()

    # theorem 6.1.5
    z = symbols('z')
    G = groebner([h1, h2, h3, h4, h5, 1 - z*g], x1, x2, x3, x4, x5, z)
    print(G)

if __name__ == '__main__':
    main()