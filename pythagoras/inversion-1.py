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
    xa, ya, xc, yc, xd, yd = symbols('xa, ya, xc, yc, xd, yd')
    A, B, C, D, E, F = (-(a + 1)*e, (a + 1)*f), (0, 0), ((c + 1)*e, (c + 1)*f), (xd, yd), (-e, f), (e, f)
    print('BE = BF?', dist2(B, E, dist2(B, F, 0)) == 0)
    print('Is AEB collinear?', det(collinear, A, E, B) == 0)
    print('Is BFC collinear?', det(collinear, B, F, C) == 0)
    # R = sqrt(e**2 + f**2)
    # S = sqrt(S2)
    R, S = symbols('R, S', positive = True)
    S2 = -(-R**2*a**2 + 2*R**2*a*c - R**2*c**2 + a**2*e**2 + a**2*f**2 + 2*a*c*e**2 - 2*a*c*f**2 + 4*a*e**2 + c**2*e**2 + c**2*f**2 + 4*c*e**2 + 4*e**2)*(-R**2*a**2 - 2*R**2*a*c - R**2*c**2 - 4*R*a*d - 4*R*c*d + a**2*e**2 + a**2*f**2 + 2*a*c*e**2 - 2*a*c*f**2 + 4*a*e**2 + c**2*e**2 + c**2*f**2 + 4*c*e**2 - 4*d**2 + 4*e**2)
    print('S^2 =', expand(S2))
    AE, CF = a*R, c*R
    # DG = DH = d
    AD, CD = AE + d, CF + d
    # choose one of two points
    # D1 = solve([dist2(A, D, AD**2), dist2(C, D, CD**2)], xd, yd)[1]
    # print('D =', D1)
    denominator = 2*a**2*e**2 + 2*a**2*f**2 + 4*a*c*e**2 - 4*a*c*f**2 + 8*a*e**2 + 2*c**2*e**2 + 2*c**2*f**2 + 8*c*e**2 + 8*e**2
    D1 = (R**2*a**3*e + R**2*a**2*c*e + 2*R**2*a**2*e - R**2*a*c**2*e - R**2*c**3*e - 2*R**2*c**2*e + 2*R*a**2*d*e + 4*R*a*d*e - 2*R*c**2*d*e - 4*R*c*d*e + S*a*f - S*c*f - a**3*e**3 - a**3*e*f**2 - a**2*c*e**3 + 3*a**2*c*e*f**2 - 4*a**2*e**3 + a*c**2*e**3 - 3*a*c**2*e*f**2 - 4*a*e**3 + c**3*e**3 + c**3*e*f**2 + 4*c**2*e**3 + 4*c*e**3, -R**2*a**3*f + R**2*a**2*c*f + R**2*a*c**2*f - R**2*c**3*f - 2*R*a**2*d*f + 4*R*a*c*d*f - 2*R*c**2*d*f + S*a*e + S*c*e + 2*S*e + a**3*e**2*f + a**3*f**3 + 3*a**2*c*e**2*f - a**2*c*f**3 + 6*a**2*e**2*f + 2*a**2*f**3 + 3*a*c**2*e**2*f - a*c**2*f**3 + 12*a*c*e**2*f - 4*a*c*f**3 + 12*a*e**2*f + c**3*e**2*f + c**3*f**3 + 6*c**2*e**2*f + 2*c**2*f**3 + 12*c*e**2*f + 8*e**2*f)
    print('D =', D1)
    E = (expand(E[0]*denominator*AD*CD), expand(E[1]*denominator*AD*CD))
    F = (expand(F[0]*denominator*AD*CD), expand(F[1]*denominator*AD*CD))
    G = (expand(C[0]*denominator*AD*CD + (D1[0] - C[0]*denominator)*CF*AD), expand(C[1]*denominator*AD*CD + (D1[1] - C[1]*denominator)*CF*AD))
    H = (expand(A[0]*denominator*AD*CD + (D1[0] - A[0]*denominator)*AE*CD), expand(A[1]*denominator*AD*CD + (D1[1] - A[1]*denominator)*AE*CD))
    print('x_E =', E[0])
    print('y_E =', E[1])
    print('x_F =', F[0])
    print('y_F =', F[1])
    print('x_G =', G[0])
    print('y_G =', G[1])
    print('x_H =', H[0])
    print('y_H =', H[1])
    # calculated in Inversion1.java
    # g = det(concyclic, E, F, G, H)
    # print('Are E, F, G and H concyclic?', expand(g) == 0)

if __name__ == '__main__':
    main()