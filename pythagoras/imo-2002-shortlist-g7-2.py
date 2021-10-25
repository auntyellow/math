from sympy import factor
from cartesian import *

def main():
    # https://imomath.com/index.php?options=323 (Problem 14)
    b, c, r = symbols('b, c, r', positive = True)
    B, C, I = (-b, 0), (c, 0), (0, r)
    print('I:', I)
    d, e, f, x, y = symbols('d, e, f, x, y')
    incircle = x**2 + y**2 - 2*y*r
    y_KM = b*c*x/(b - c)/r
    x_N = solve(incircle.subs(y, y_KM)/x, x)[0]
    N = (factor(x_N), factor(y_KM.subs(x, x_N)))
    print('N:', N)
    circle_eq = Eq(x**2 + y**2 + d*x + e*y + f, 0)
    circle_eqs = []
    circle_eqs.append(circle_eq.subs(x, N[0]).subs(y, N[1]))
    circle_eqs.append(circle_eq.subs(x, B[0]).subs(y, B[1]))
    circle_eqs.append(circle_eq.subs(x, C[0]).subs(y, C[1]))
    S = solve(circle_eqs, (d, e, f))
    S = factor(-S[d]/2), factor(-S[e]/2)
    print('S:', S)
    print('Are INS collinear?', collinear(I, N, S))

if __name__ == '__main__':
    main()