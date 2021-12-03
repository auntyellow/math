from sympy import factor, poly, sqrt
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

def center(c):
    x, y = symbols('x, y')
    return factor(-poly(c, x).nth(1)/2), factor(-poly(c, y).nth(1)/2)

def radius2(c):
    p = poly(c, symbols('x, y'))
    return factor(p.nth(1, 0)**2/4 + p.nth(0,1)**2/4 - p.nth(0, 0))

def main():
    # https://en.wikipedia.org/wiki/Nine-point_circle
    # https://en.wikipedia.org/wiki/Feuerbach_point
    # Nine-point circle is internally tangent to incircle and externally tangent to 3 excircles
    a, b, c, r = symbols('a, b, c, r', positive = True)
    a, b, r = symbols('a, b, r', positive = True)
    A, B, C, I = (-a, 0), (b, 0), ((a - b)*r**2/(a*b - r**2), 2*a*b*r/(a*b - r**2)), (0, r)
    nine_point = circle(((A[0] + C[0])/2, (A[1] + C[1])/2), ((B[0] + C[0])/2, (B[1] + C[1])/2), ((b - a)/2, 0))
    print('Nine-Point Circle Equation:', nine_point, '= 0')
    N = center(nine_point)
    print('N:', N)
    x, y, z = symbols('x, y, z')
    incircle = x**2 + y**2 - 2*y*r
    print('Incircle/Excircle Equation:', incircle, '= 0')
    IN2 = factor(dist2(I, N))
    print('IN**2 =', IN2)
    rN2 = radius2(nine_point)
    print('r(N)**2 =', rN2)

if __name__ == '__main__':
    main()