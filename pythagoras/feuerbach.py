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
    a, b, c, AC, BC = symbols('a, b, c, AC, BC', positive = True)
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
    discriminant = expand(discriminant.subs(AC, sqrt(a**2 + c**2)).subs(BC, sqrt(b**2 + c**2)))
    # print('Discriminant: ', discriminant)
    return discriminant == 0

def main():
    # https://en.wikipedia.org/wiki/Nine-point_circle
    # https://en.wikipedia.org/wiki/Feuerbach_point
    # Nine-point circle is internally tangent to incircle and externally tangent to 3 excircles
    # Put AB onto x-axis and C onto y-axis
    a, b, c, AC, BC = symbols('a, b, c, AC, BC', positive = True)
    # a, b, c, AC, BC = 1, 1, sqrt(3), 2, 2
    A, B, C = (-a, 0), (b, 0), (0, c)
    nine_point = circle((b/2, c/2), (-a/2, c/2), ((b - a)/2, 0))
    print('Nine-Point Circle Equation:', nine_point, '= 0')
    print('Is altitude foot on Nine-Point Circle?', on_circle(nine_point, (0, 0)))
    print('Is midpoint of of vertex and orthocenter on Nine-Point Circle?', on_circle(nine_point, (0, (c + a*b/c)/2)))

    # AB, AC, BC = a + b, sqrt(a**2 + c**2), sqrt(b**2 + c**2)
    AB = a + b
    # AD, BE, CF are internal bisectors  
    AF = (AB + AC - BC)/2
    BF = AB - AF
    F = (AF - a, 0)
    E = (a*AF/AC - a, c*AF/AC)
    D = (b - b*BF/BC, c*BF/BC)
    incircle = circle(D, E, F)
    print()
    print('Incircle Equation:', incircle, '= 0')
    print('Does Nine-Point Circle kiss Incircle?', kiss(nine_point, incircle))
    # G, H, K are tangent points of BC, AC and AB with AB side excircle 
    AK = (AB + BC - AC)/2
    BK = AB - AK
    K = (AK - a, 0)
    H = (-a*AK/AC - a, -c*AK/AC)
    G = (b + b*BK/BC, -c*BK/BC)
    excircle = circle(G, H, K)
    print()
    print('Excircle Equation:', excircle, '= 0')
    print('Does Nine-Point Circle kiss Excircle?', kiss(nine_point, excircle))

if __name__ == '__main__':
    main()