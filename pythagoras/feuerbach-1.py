from sympy import expand, poly
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

def on_circle(circle_eq, P):
    x, y, z = symbols('x, y, z')
    return expand(circle_eq.subs(x, P[0]).subs(y, P[1]).subs(z, P[2])) == 0

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
    if discriminant != 0:
        return None
    x0 = -c1_coeffs[1]/2/c1_coeffs[0]
    return x0, radical_y.subs(x, x0)

def main():
    # https://blancosilva.github.io/post/2013/07/15/some-results-related-to-the-feuerbach-point.html (Theorem 1)
    # The circle through the feet of the internal bisectors of a triangle passes through the Feuerbach point.
    a, b, r = symbols('a, b, r', positive = True)
    A, B, C, I = (-a, 0), (b, 0), ((a - b)*r**2/(a*b - r**2), 2*a*b*r/(a*b - r**2)), (0, r)
    nine_point = circle(((A[0] + C[0])/2, (A[1] + C[1])/2), ((B[0] + C[0])/2, (B[1] + C[1])/2), ((b - a)/2, 0))
    print('Nine-Point Circle Equation:', nine_point, '= 0')
    x, y, z = symbols('x, y, z')
    incircle = x**2 + y**2 - 2*y*r
    print('Incircle/Excircle Equation:', incircle, '= 0')
    F = kiss(nine_point, incircle)
    print('F:', F)
    BC, AC, AB, AI, BI, CI = line(B, C), line(A, C), line(A, B), line(A, I), line(B, I), line(C, I)
    A1, B1, C1 = intersect(BC, AI), intersect(AC, BI), intersect(AB, CI)
    print('A1', A1)
    print('B1', B1)
    print('C1', C1)
    bisector_feet = circle(A1, B1, C1)
    print('Bisector-Feet Circle Equation:', bisector_feet, '= 0')
    bisector_feet = poly(fraction(cancel(bisector_feet))[0], (x, y)).homogenize(z).expr
    F = to_homogeneous(F)
    print('F in Homogeneous:', F)
    print('Bisector-Feet Circle Equation in Homogeneous:', bisector_feet, '= 0')
    print('Is Feuerbach point on Bisector-Feet Circle?', on_circle(bisector_feet, F))

if __name__ == '__main__':
    main()