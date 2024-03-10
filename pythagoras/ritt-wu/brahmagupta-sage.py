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

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2

def main():
    # https://ask.sagemath.org/question/33051#post-id-33060
    A = QQ['a, b, c, d']
    a, b, c, d = A.gens()
    R = PolynomialRing(A.fraction_field(), 'x1, x2, x3, x4', order = 'lex')
    x1, x2, x3, x4 = R.gens()
    A, B, C, D = (0, 0), (a, 0), (x1, x2), (x3, x4)
    BC = dist2(B, C) - b**2
    CD = dist2(C, D) - c**2
    DA = dist2(D, A) - d**2
    concyc = det(concyclic, A, B, C, D)
    S0 = (det(collinear, A, B, C) + det(collinear, A, C, D))/2
    B = R.ideal(BC, CD, DA, concyc).groebner_basis()
    x1_, x2_, x3_, x4_ = var('x1_, x2_, x3_, x4_')
    for s in solve(B[3].subs({x4: x4_}), x4_):
        x40 = s.right()
        x10 = solve(B[0].subs({x1: x1_, x4: x40}), x1_)[0].right()
        x20 = solve(B[1].subs({x2: x2_, x4: x40}), x2_)[0].right()
        x30 = solve(B[2].subs({x3: x3_, x4: x40}), x3_)[0].right()
        print('S^2 =', factor(S0.subs({x1: x10, x2: x20, x3: x30, x4: x40})**2))

if __name__ == '__main__':
    main()