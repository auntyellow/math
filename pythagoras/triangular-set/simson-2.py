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

def main():
    # https://en.wikipedia.org/wiki/Simson_line converse
    u1, u2, u3, x1, x2, x3, x4, x5 = symbols('u1, u2, u3, x1, x2, x3, x4, x5')
    A, B, C, P, F, E, D = (0, 0), (1, 0), (u1, u2), (u3, x1), (u3, 0), (x2, x3), (x4, x5)
    h1 = det(collinear, C, A, E)
    h2 = perpendicular(C, A, E, P)
    h3 = det(collinear, B, C, D)
    h4 = perpendicular(B, C, D, P)
    h5 = det(collinear, D, E, F)
    g = det(concyclic, A, B, C, P)

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