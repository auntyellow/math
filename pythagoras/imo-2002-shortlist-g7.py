from sympy import Eq, expand, poly, solve, sqrt, symbols
from cartesian import *
from homogeneous import *

def circle(P1, P2, P3):
    # return F(x, y) such that F(x, y) = 0 is the circle's equation
    d, e, f, x, y = symbols('d, e, f, x, y')
    circle_eq = Eq(x**2 + y**2 + d*x + e*y + f, 0)
    circle_eqs = []
    circle_eqs.append(circle_eq.subs(x, P1[0]).subs(y, P1[1]))
    circle_eqs.append(circle_eq.subs(x, P2[0]).subs(y, P2[1]))
    circle_eqs.append(circle_eq.subs(x, P3[0]).subs(y, P3[1]))
    s = solve(circle_eqs, (d, e, f))
    return x**2 + y**2 + s[d]*x + s[e]*y + s[f]

def center(c):
    x, y = symbols('x, y')
    return cancel(-poly(c, x).nth(1)/2), cancel(-poly(c, y).nth(1)/2)

def main():
    # https://imomath.com/index.php?options=323 (Problem 14)
    a, b, c, AB, AC = symbols('a, b, c, AB, AC', positive = True)
    A, B, C, M = (0, a), (-b, 0), (c, 0), (0, a/2)
    #AB, AC = sqrt(a**2 + b**2), sqrt(a**2 + c**2)

    # Step 1: Solve K and incircle
    BC = b + c
    BK = (AB + BC - AC)/2
    K = (BK - b, 0)
    CK = BC - BK
    K_B = (c - c*CK/AC, a*CK/AC)
    K_C = (b*BK/AB - b, a*BK/AB)
    incircle = circle(K, K_B, K_C)
    I = center(incircle)
    print('I =', I)

    # Step 2: Solve N
    KM = line(K, M)
    x, y = symbols('x, y')
    y_KM = solve(KM, y)[0]
    incircle_poly = poly(incircle.subs(y, y_KM), x)
    incircle_coeffs = incircle_poly.all_coeffs()
    # Vieta's Formula: x_N + x_K = -b/a
    x_N = -incircle_coeffs[1]/incircle_coeffs[0] - K[0]
    N = (cancel(x_N), cancel(y_KM.subs(x, x_N)))
    print('N =', N)

    # Step 3: Solve BCN and center S
    x_N, y_N = symbols('x_N, y_N')
    S = center(circle((x_N, y_N), B, C))
    S = (cancel(S[0].subs(x_N, N[0]).subs(y_N, N[1])), cancel(S[1].subs(x_N, N[0]).subs(y_N, N[1])))
    print('S =', S)

    # Step 4: Prove INS collinear
    collinear = incidence(to_homogeneous(I), to_homogeneous(N), to_homogeneous(S))
    print(expand(collinear.subs(AB, sqrt(a**2 + b**2)).subs(AC, sqrt(a**2 + c**2))))

if __name__ == '__main__':
    main()