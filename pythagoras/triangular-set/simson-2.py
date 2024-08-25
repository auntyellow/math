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
    # https://en.wikipedia.org/wiki/Simson_line converse
    u1, u2, u3, x1, x2, x3, x4, x5 = symbols('u1, u2, u3, x1, x2, x3, x4, x5')
    A, B, C, P, F, E, D = (0, 0), (1, 0), (u1, u2), (u3, x1), (u3, 0), (x2, x3), (x4, x5)
    h1 = det(collinear, C, A, E)
    h2 = perpendicular(C, A, E, P)
    h3 = det(collinear, B, C, D)
    h4 = perpendicular(B, C, D, P)
    h5 = det(collinear, D, E, F)
    g = det(concyclic, A, B, C, P)

    x_i = [x1, x2, x3, x4, x5]
    print('h5 =', poly(h5, x_i).expr, vars(h5))
    print('h4 =', poly(h4, x_i).expr, vars(h4))
    h4a = prem(h5, h4, x5) # eliminate x5
    print('h4a =', poly(h4a, x_i).expr, vars(h4a))
    print('h3 =', poly(h3, x_i).expr, vars(h3))
    h3b = prem(h4, h3, x5) # eliminate x5
    print('h3b =', poly(h3b, x_i).expr, vars(h3b))
    h3a = prem(h4a, h3b, x4) # eliminate x4
    print('h3a =', poly(h3a, x_i).expr, vars(h3a))
    print('h2 =', poly(h2, x_i).expr, vars(h2))
    h2a = prem(h3a, h2, x3) # eliminate x3
    print('h2a =', poly(h2a, x_i).expr, vars(h2a))
    print('h1 =', poly(h1, x_i).expr, vars(h1))
    h1b = prem(h3a, h1, x3) # eliminate x3
    print('h1b =', poly(h1b, x_i).expr, vars(h1b))
    h1a = prem(h2a, h1b, x2) # eliminate x2
    print('h1a =', poly(h1a, x_i).expr, vars(h1a))
    print('g =', poly(g, x_i).expr, vars(g))
    # Wu's method
    # prem(g, h1a, x1) doesn't work; resultant(h1a, g, x1) works
    R = prem(h1a, g, x1)
    # there are degenerated conditions that g != 0
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