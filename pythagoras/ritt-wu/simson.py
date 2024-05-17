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
    var('x1:9')
    A, B, C, P, F, E, D = (0, 0), (1, 0), (x1, x2), (x3, x4), (x3, 0), (x5, x6), (x7, x8)
    h1 = det(concyclic, A, B, C, P)
    h2 = det(collinear, C, A, E)
    h3 = perpendicular(C, A, E, P)
    h4 = det(collinear, B, C, D)
    h5 = perpendicular(B, C, D, P)
    g = det(collinear, D, E, F)

    print('h5 =', h5, vars(h5))
    print('h4 =', h4, vars(h4))
    h4a = prem(h5, h4, x8) # eliminate x8, resultant(h5, h4, x8) also works
    print('h4a =', h4a, vars(h4a))
    print('h3 =', h3, vars(h3))
    print('h2 =', h2, vars(h2))
    h2a = prem(h3, h2, x6) # eliminate x6, resultant(h3, h2, x6) also works
    print('h2a =', h2a, vars(h2a))
    print('h1 =', h1, vars(h1))
    print('g =', g, vars(g))
    print()

    R = prem(g, h5, x8)
    print('R(x8) =', R, vars(R))
    R = prem(R, h4a, x7)
    print('R(x7) =', R, vars(R))
    R = prem(R, h3, x6)
    print('R(x6) =', R, vars(R))
    R = prem(R, h2a, x5)
    print('R(x5) =', factor(R), vars(R))
    R = prem(R, h1, x4)
    print('R(x4) =', R)
    print()

    # much simpler than x1..x8
    G = groebner([h1, h2, h3, h4, h5], x8, x7, x6, x5, x4, x3, x2, x1)
    print(G, len(G))
    # TODO why != 0?
    print(G.reduce(g))

if __name__ == '__main__':
    main()