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

# ISBN 9787040316988, p297, ex 6.1.6

def main():
    u1, u2, u3, y1, y2, y3, y4, y5, y6 = symbols('u1, u2, u3, y1, y2, y3, y4, y5, y6')
    # hypotheses in book
    h1 = expand(u3*y2**2 - (u3**2 + u2**2 - u1**2)*y2 + u3*(y1**2 - u1**2))
    h2 = (u2 + u1)*(y3 - y1) + u3*(y4 - y2)
    h3 = (u2 + u1)*y4 - u3*(y3 + u1)
    h4 = (u2 - u1)*(y5 - y1) - u3*(y6 - y2)
    h5 = (u2 - u1)*y6 - u3*(y5 - u1)
    g = (y3 - y1)*y6 - y4*(y5 - y1)
    print('h1 =', expand(h1))
    print('h2 =', expand(h2))
    print('h3 =', expand(h3))
    print('h4 =', expand(h4))
    print('h5 =', expand(h5))
    print('g =', expand(g))
    print()
    # hypotheses derived
    A, B, C, P, D, E, F = (u1, 0), (-u1, 0), (u2, u3), (y1, y2), (y1, 0), (y3, y4), (y5, y6)
    h1 = det(concyclic, A, B, C, P)
    print('h1 =', factor(h1))
    h2 = perpendicular(B, C, E, P)
    print('h2 =', factor(h2))
    h3 = det(collinear, B, C, E)
    print('h3 =', factor(h3))
    h4 = perpendicular(C, A, F, P)
    print('h4 =', factor(h4))
    h5 = det(collinear, C, A, F)
    print('h5 =', factor(h5))
    g = det(collinear, D, E, F)
    print('g =', factor(g))
    print()

    # much simpler than u1..u3, y1..y6
    G = groebner([h1, h2, h3, h4, h5], y6, y5, y4, y3, y2, y1, u3, u2, u1)
    print(G, len(G))
    # TODO why != 0?
    print(G.reduce(g))

if __name__ == '__main__':
    main()