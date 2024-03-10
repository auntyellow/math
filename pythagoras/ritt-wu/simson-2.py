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
    xc, yc, xd, yd, xe, ye, xf, yf, xp, yp = symbols('xc, yc, xd, yd, xe, ye, xf, yf, xp, yp')
    A, B, C, P, F, E, D = (0, 0), (0, 1), (xc, yc), (xp, yp), (xf, yf), (xe, ye), (xd, yd)
    h1 = det(collinear, A, B, F)
    h2 = perpendicular(A, B, F, P)
    h3 = det(collinear, C, A, E)
    h4 = perpendicular(C, A, E, P)
    h5 = det(collinear, B, C, D)
    h6 = perpendicular(B, C, D, P)
    h7 = det(collinear, D, E, F)
    g = det(concyclic, A, B, C, P)
    # eliminate xf, yf, xe, ye, xd, yd
    # get xc(yp), yc(yp), xp(yp) 
    G = groebner([h1, h2, h3, h4, h5, h6, h7], xd, yd, xe ,ye, xf, yf, xp)
    print(G, len(G))
    h8 = G[len(G) - 1]
    print('g =', Poly(g, xp))
    print('h8 =', Poly(h8, xp))
    R = prem(g, h8, xp)
    print('R(xp) =', R)
    print('Is g == h8?', expand(g) == expand(h8))

if __name__ == '__main__':
    main()