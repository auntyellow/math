from sage.all import *

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

def dist(P1, P2, d2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2 - d2

def main():
    # https://imomath.com/index.cgi?page=inversion (Problem 1)
    A = QQ['a, c, d, e, f']
    a, c, d, e, f = A.gens()
    R = PolynomialRing(A.fraction_field(), 'xd, yd, xg, yg, xh, yh', order = 'lex')
    xd, yd, xg, yg, xh, yh = R.gens()
    A, B, C, E, F = (-(a + 1)*e, (a + 1)*f), (0, 0), ((c + 1)*e, (c + 1)*f), (-e, f), (e, f)
    D, G, H = (xd, yd), (xg, yg), (xh, yh)
    print('BE = BF?', dist(B, E, dist(B, F, 0)) == 0)
    print('Is AEB collinear?', det(collinear, A, E, B) == 0)
    print('Is BFC collinear?', det(collinear, B, F, C) == 0)
    f1 = det(collinear, C, G, D)   # G, D
    # CG = CF
    f2 = dist(C, G, dist(C, F, 0)) # G
    f3 = dist(G, D, d**2)          # G, D
    f4 = det(collinear, A, H, D)   # H, D
    # AE = AH
    f5 = dist(A, H, dist(A, E, 0)) # H
    f6 = dist(H, D, d**2)          # H, D
    g = det(concyclic, E, F, G, H) # G, H
    B = R.ideal(f1, f2, f3, f4, f5, f6).groebner_basis()
    for p in B:
        print(factor(p), '= 0')
    print(len(B), 'equations')


if __name__ == '__main__':
    main()