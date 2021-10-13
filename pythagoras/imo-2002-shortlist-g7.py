from sympy import Eq, Poly, solve, sqrt, symbols
from cartesian import *

def circle_eq(P):
    x, y = P[0], P[1]
    return Eq(x**2 + y**2 + d*x + e*y + f, 0)

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

def main():
    # https://imomath.com/index.php?options=323 (Problem 14)
    a, b, c = symbols('a, b, c', positive = True)
    A, B, C, M = (0, a), (-b, 0), (c, 0), (0, a/2)
    #AB, AC = sqrt(a**2 + b**2), sqrt(a**2 + c**2)

    # Step 1: Calculate K and Incircle
    AB, AC = symbols('AB, AC')
    BC = b + c
    BK = (AB + BC - AC)/2
    CK = (AB + AC - BC)/2
    K = (BK - b, 0)
    print('K:', K)
    K_B = (c - c*CK/AC, a*CK/AC)
    K_C = (b*BK/AB - b, a*BK/AB)
    incircle = circle(K, K_B, K_C)

    # Step 2: Solve N
    KM = line(K, M)
    print('KM:', KM)
    x, y = symbols('x, y')
    y_KM = solve(KM, y)[0]
    print('y_KM =', y_KM)
    incircle_poly = Poly(incircle.subs(y, y_KM), x)
    incircle_coeffs = incircle_poly.all_coeffs()
    x_N = -incircle_coeffs[1]/incircle_coeffs[0] - K[0]
    N = (x_N, y_KM.subs(x, x_N))
    print('N:', N)

if __name__ == '__main__':
    main()