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
    u1, u2, u3, u4, u5, x1, x2, x3, x4, x5 = symbols('u1, u2, u3, u4, u5, x1, x2, x3, x4, x5')
    A, B, C, D, E, F, G = (0, 0), (1, 0), (u1, u2), (u3, x1), (u4, x2), (u5, x3), (x4, x5)
    h1 = bisect(D, A, B, C)
    h2 = bisect(E, B, C, A)
    h3 = bisect(F, C, A, B)
    h4 = det(collinear, A, D, G)
    h5 = det(collinear, B, E, G)
    g = det(collinear, C, F, G)
    print('h1 =', factor(h1))
    # h1 = 2*u1*u3*x1 - u2*u3**2 + u2*x1**2
    print('h1 =', h1)
    x10 = solve(h1, x1)
    print('x1 =', x10)
    h11, h12 = factor(x10[0] - x1), factor(x10[1] - x1)
    print('h1 =', h11*h12, '=', factor(expand(h11*h12)))
    # hardly work due to difficult to decide whether h11 or h12 should be used
    print()

    A, B, G, C = (0, 0), (1, 0), (u1, u2), (x1, x2)
    h1 = bisect(G, A, B, C)
    h2 = bisect(G, B, A, C)
    g = bisect(G, C, A, B)
    print('h1 =', factor(h1))
    print('h2 =', factor(h2))
    print('g =', factor(g))
    h1 = -u1**2*x2 + 2*u1*u2*x1 + u2**2*x2
    h2 = -u1**2*x2 + 2*u1*u2*x1 - 2*u1*u2 + 2*u1*x2 + u2**2*x2 - 2*u2*x1 + 2*u2 - x2
    g = 2*u1**2*x1*x2 - u1**2*x2 - 2*u1*u2*x1**2 + 2*u1*u2*x1 + 2*u1*u2*x2**2 - 2*u1*x1**2*x2 - 2*u1*x2**3 - 2*u2**2*x1*x2 + u2**2*x2 + 2*u2*x1**3 - 2*u2*x1**2 + 2*u2*x1*x2**2 - 2*u2*x2**2 + x1**2*x2 + x2**3
    print('h1 =', h1, vars(h1))
    print('h2 =', h2, vars(h2))
    print('g =', g)
    print()

    # method 1: solve x1 and x2 directly
    s = solve([h1, h2], x1, x2)
    print('x1, x2 =', s)
    print('g =', cancel(g.subs(s)))
    print()

    # method 2: Wu's method
    h1a = prem(h2, h1, x2) # eliminate x2, resultant(h2, h1, x2) also works
    print('h1a =', h1a, vars(h1a))
    R = prem(g, h2, x2)
    print('R(x2) =', R, vars(R))
    R = prem(R, h1a, x1)
    print('R(x1) =', R)
    print()

    # method 3: ISBN 9787040316988, p297, theorem 6.1.4
    G = groebner([h1, h2], x1, x2)
    print(G, len(G))
    print(G.reduce(g))
    print()

    # method 4: theorem 6.1.5
    z = symbols('z')
    G = groebner([h1, h2, 1 - z*g], x1, x2, z)
    print(G)

if __name__ == '__main__':
    main()