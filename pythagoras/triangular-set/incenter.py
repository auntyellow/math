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

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2

def bisect(P, A, B, C):
    xpb, ypb, xpc, ypc = symbols('xpb, ypb, xpc, ypc')
    Pb, Pc = (xpb, ypb), (xpc, ypc)
    s = solve([det(collinear, A, B, Pb), perpendicular(P, Pb, A, B)], xpb, ypb)
    Pb = (s[xpb], s[ypb])
    s = solve([det(collinear, A, C, Pc), perpendicular(P, Pc, A, C)], xpc, ypc)
    Pc = (s[xpc], s[ypc])
    return dist2(P, Pb) - dist2(P, Pc)

def vars(expr):
    return sorted(expr.free_symbols, key = lambda s: s.name)

def main():
    var('x1:11')
    A, B, C, D, E, F, G = (0, 0), (1, 0), (x1, x2), (x3, x4), (x5, x6), (x7, x8), (x9, x10)
    h1 = bisect(D, A, B, C)
    h2 = bisect(E, B, C, A)
    h3 = bisect(F, C, A, B)
    h4 = det(collinear, A, D, G)
    h5 = det(collinear, B, E, G)
    g = det(collinear, C, F, G)
    print('h1 =', factor(h1))
    h1 = 2*x1*x3*x4 - x2*x3**2 + x2*x4**2
    print('h1 =', h1)
    x40 = solve(h1, x4)
    print('x4 =', x40)
    h11, h12 = factor(x40[0] - x4), factor(x40[1] - x4)
    print('h1 =', h11*h12, '=', factor(expand(h11*h12)))
    # hardly work due to difficult to decide whether h11 or h12 should be used
    print()

    A, B, G, C = (0, 0), (1, 0), (x1, x2), (x3, x4)
    h1 = bisect(G, A, B, C)
    h2 = bisect(G, B, A, C)
    g = bisect(G, C, A, B)
    print('h1 =', factor(h1))
    print('h2 =', factor(h2))
    print('h3 =', factor(g))
    h1 = x1**2*x4 - 2*x1*x2*x3 - x2**2*x4
    h2 = x1**2*x4 - 2*x1*x2*x3 + 2*x1*x2 - 2*x1*x4 - x2**2*x4 + 2*x2*x3 - 2*x2 + x4
    g = 2*x1**2*x3*x4 - x1**2*x4 - 2*x1*x2*x3**2 + 2*x1*x2*x3 + 2*x1*x2*x4**2 - 2*x1*x3**2*x4 - 2*x1*x4**3 - 2*x2**2*x3*x4 + x2**2*x4 + 2*x2*x3**3 - 2*x2*x3**2 + 2*x2*x3*x4**2 - 2*x2*x4**2 + x3**2*x4 + x4**3
    print('h1 =', h1, vars(h1))
    print('h2 =', h2, vars(h2))
    print('g =', g)
    print()

    # method 1: solve x3 and x4 directly
    s = solve([h1, h2], x3, x4)
    print('x3, x4 =', s)
    print('g =', cancel(g.subs(s)))
    print()

    # method 2: triangular set
    h1a = prem(h2, h1, x4) # eliminate x4, resultant(h2, h1, x4) also works
    print('h1a =', h1a, vars(h1a))
    R = prem(g, h2, x4)
    print('R(x4) =', R, vars(R))
    R = prem(R, h1a, x3)
    print('R(x3) =', R)
    print()

    # method 3: ISBN 9787040316988, p297, theorem 6.1.4, x1 and x2 are free variables
    G = groebner([h1, h2], x3, x4)
    print(G, len(G))
    print(G.reduce(g))
    print()

    # method 4: theorem 6.1.5
    z = symbols('z')
    G = groebner([h1, h2, 1 - z*g], x3, x4, z)
    print(G)

if __name__ == '__main__':
    main()