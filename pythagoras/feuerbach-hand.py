from sympy import expand, poly, sqrt
from cartesian import *

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

def on_circle(circle_eq, P):
    x, y = symbols('x, y')
    return cancel(circle_eq.subs(x, P[0]).subs(y, P[1])) == 0

def kiss(c1_eq, c2_eq):
    x, y = symbols('x, y')
    radical = fraction(cancel(c1_eq - c2_eq))[0]
    # print('Radical:', radical)
    radical_y = solve(Eq(radical, 0), y)[0]
    # print('y =', radical_y)
    c1_radical = fraction(cancel(c1_eq.subs(y, radical_y)))[0]
    # print('C1-Radical: ', c1_radical)
    c1_coeffs = poly(c1_radical, x).all_coeffs()
    discriminant = fraction(cancel(c1_coeffs[1]**2 - 4*c1_coeffs[0]*c1_coeffs[2]))[0]
    # print('Discriminant: ', discriminant)
    return discriminant == 0

def main():
    a, b, r = symbols('a, b, r', positive = True)
    A, B, C = (-a, 0), (b, 0), ((a - b)*r**2/(a*b - r**2), 2*a*b*r/(a*b - r**2))
    nine_point = circle(((A[0] + C[0])/2, (A[1] + C[1])/2), ((B[0] + C[0])/2, (B[1] + C[1])/2), ((b - a)/2, 0))
    print('Nine-Point Circle Equation:', nine_point, '= 0')
    print('Is altitude foot on Nine-Point Circle?', on_circle(nine_point, (C[0], 0)))
    print('Is midpoint of vertex and orthocenter on Nine-Point Circle?', \
        on_circle(nine_point, (C[0], (C[1] + (A[0] - C[0])*(C[0] - B[0])/C[1])/2)))
    x, y = symbols('x, y')
    incircle = x**2 + y**2 - 2*y*r
    print('Incircle/Excircle Equation:', incircle, '= 0')
    print('Does Nine-Point Circle kiss Incircle/Excircle?', kiss(nine_point, incircle))

if __name__ == '__main__':
    main()