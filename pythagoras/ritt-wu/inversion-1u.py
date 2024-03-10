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

def dist2(P1, P2, d2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2 - d2

def main():
    # https://imomath.com/index.cgi?page=inversion (Problem 1)
    a, c, d, e, f = symbols('a, c, d, e, f', positive = True)
    xd, yd, xg, yg, xh, yh = symbols('xd, yd, xg, yg, xh, yh')
    # xd, yd, xg, yg, xh, yh are undetermined
    A, B, C, E, F = (-(a + 1)*e, (a + 1)*f), (0, 0), ((c + 1)*e, (c + 1)*f), (-e, f), (e, f)
    D, G, H = (xd, yd), (xg, yg), (xh, yh)
    print('BE = BF?', dist2(B, E, dist2(B, F, 0)) == 0)
    print('Is AEB collinear?', det(collinear, A, E, B) == 0)
    print('Is BFC collinear?', det(collinear, B, F, C) == 0)
    h1 = det(collinear, C, G, D)     # G, D
    h2 = dist2(C, G, dist2(C, F, 0)) # G, CG = CF
    h3 = dist2(G, D, d**2)           # G, D
    h4 = det(collinear, A, H, D)     # H, D
    h5 = dist2(A, H, dist2(A, E, 0)) # H, AE = AH
    h6 = dist2(H, D, d**2)           # H, D
    g = det(concyclic, E, F, G, H)   # G, H
    B1 = groebner([h1, h2, h3], xg, yg, xd, yd)
    h7 = B1[len(B1) - 1]
    print('h7 =', h7)
    B2 = groebner([h4, h5, h6], xh, yh, xd, yd)
    h8 = B2[len(B2) - 1]
    print('h8 =', h8)
    # too slow
    # '''
    B = groebner([h7, h8], xd, yd)
    print(B, len(B))
    # '''

if __name__ == '__main__':
    main()