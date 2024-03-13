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
    # S = sqrt(...)
    # e2_f2 = sqrt(e**2 + f**2)
    AD2, CD2, S, e2_f2 = symbols('AD2, CD2, S, e2_f2', positive = True)
    AE, CF = a*e2_f2, c*e2_f2
    # DG = DH = d
    AD, CD = AE + d, CF + d
    '''
    # choose one of two points
    D1 = solve([dist2((xa, ya), D, AD2), dist2((xc, yc), D, CD2)], xd, yd)[1]
    print('D =', D1)
    subs1 = {xa: A[0], ya: A[1], xc: C[0], yc: C[1], AD2: AD**2, CD2: CD**2}
    D1 = (D1[0].subs(subs1), D1[1].subs(subs1))
    print('D =', D1)
    '''
    denominator = 2*(a**2*e**2 + a**2*f**2 + 2*a*c*e**2 - 2*a*c*f**2 + 4*a*e**2 + c**2*e**2 + c**2*f**2 + 4*c*e**2 + 4*e**2)
    D = (-(a - c)*(S*f + a**2*e**3 - a**2*e*e2_f2**2 + a**2*e*f**2 + 2*a*c*e**3 - 2*a*c*e*e2_f2**2 - 2*a*c*e*f**2 - 2*a*d*e*e2_f2 + 4*a*e**3 - 2*a*e*e2_f2**2 + c**2*e**3 - c**2*e*e2_f2**2 + c**2*e*f**2 - 2*c*d*e*e2_f2 + 4*c*e**3 - 2*c*e*e2_f2**2 - 4*d*e*e2_f2 + 4*e**3), -S*a*e - S*c*e - 2*S*e + a**3*e**2*f - a**3*e2_f2**2*f + a**3*f**3 + 3*a**2*c*e**2*f + a**2*c*e2_f2**2*f - a**2*c*f**3 - 2*a**2*d*e2_f2*f + 6*a**2*e**2*f + 2*a**2*f**3 + 3*a*c**2*e**2*f + a*c**2*e2_f2**2*f - a*c**2*f**3 + 4*a*c*d*e2_f2*f + 12*a*c*e**2*f - 4*a*c*f**3 + 12*a*e**2*f + c**3*e**2*f - c**3*e2_f2**2*f + c**3*f**3 - 2*c**2*d*e2_f2*f + 6*c**2*e**2*f + 2*c**2*f**3 + 12*c*e**2*f + 8*e**2*f)
    print('D =', D)
    E = (E[0]*denominator*AD*CD, E[1]*denominator*AD*CD)
    F = (F[0]*denominator*AD*CD, F[1]*denominator*AD*CD)
    G = (C[0]*denominator*AD*CD + (D[0] - C[0]*denominator)*CF*AD, C[1]*denominator*AD*CD + (D[1] - C[1]*denominator)*CF*AD)
    H = (A[0]*denominator*AD*CD + (D[0] - A[0]*denominator)*AE*CD, A[1]*denominator*AD*CD + (D[1] - A[1]*denominator)*AE*CD)
    print('E =', E)
    print('F =', F)
    print('G =', G)
    print('H =', H)
    # S = sqrt(-e**4*(-a - 1)**4 + 4*e**4*(-a - 1)**3*(c + 1) - 6*e**4*(-a - 1)**2*(c + 1)**2 + 4*e**4*(-a - 1)*(c + 1)**3 - e**4*(c + 1)**4 - 2*e**2*f**2*(-a - 1)**2*(a + 1)**2 + 4*e**2*f**2*(-a - 1)**2*(a + 1)*(c + 1) - 2*e**2*f**2*(-a - 1)**2*(c + 1)**2 + 4*e**2*f**2*(-a - 1)*(a + 1)**2*(c + 1) - 8*e**2*f**2*(-a - 1)*(a + 1)*(c + 1)**2 + 4*e**2*f**2*(-a - 1)*(c + 1)**3 - 2*e**2*f**2*(a + 1)**2*(c + 1)**2 + 4*e**2*f**2*(a + 1)*(c + 1)**3 - 2*e**2*f**2*(c + 1)**4 + 2*e**2*(-a - 1)**2*(a*e2_f2 + d)**2 + 2*e**2*(-a - 1)**2*(c*e2_f2 + d)**2 - 4*e**2*(-a - 1)*(c + 1)*(a*e2_f2 + d)**2 - 4*e**2*(-a - 1)*(c + 1)*(c*e2_f2 + d)**2 + 2*e**2*(c + 1)**2*(a*e2_f2 + d)**2 + 2*e**2*(c + 1)**2*(c*e2_f2 + d)**2 - f**4*(a + 1)**4 + 4*f**4*(a + 1)**3*(c + 1) - 6*f**4*(a + 1)**2*(c + 1)**2 + 4*f**4*(a + 1)*(c + 1)**3 - f**4*(c + 1)**4 + 2*f**2*(a + 1)**2*(a*e2_f2 + d)**2 + 2*f**2*(a + 1)**2*(c*e2_f2 + d)**2 - 4*f**2*(a + 1)*(c + 1)*(a*e2_f2 + d)**2 - 4*f**2*(a + 1)*(c + 1)*(c*e2_f2 + d)**2 + 2*f**2*(c + 1)**2*(a*e2_f2 + d)**2 + 2*f**2*(c + 1)**2*(c*e2_f2 + d)**2 - (a*e2_f2 + d)**4 + 2*(a*e2_f2 + d)**2*(c*e2_f2 + d)**2 - (c*e2_f2 + d)**4)
    # should use a powerful tool to calculate det
    # g = det(concyclic, E, F, G, H)
    # print('g =', g)

if __name__ == '__main__':
    main()