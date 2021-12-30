from sympy import poly
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
    return cancel(-poly(c, x).nth(1)/2), cancel(-poly(c, y).nth(1)/2)

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

def cross_ratio(a, b, c, d):
    return cancel((a - c)*(b - d)/(a - d)/(b - c))

def main():
    # https://www.cut-the-knot.org/Curriculum/Geometry/FeuerbachIncidence.shtml
    # Let Fa, Fb, Fc be the touch points of the nine-point circle with the A-, B-, C- excircles, respectively.
    # The lines AFa, BFb, CFc meet at X(12), the harmonic conjugate of the Feuerbach point Fi with
    # respect to the incenter I and the nine-point center N
    a, b, r = symbols('a, b, r', positive = True)
    A, B, C, I = (-a, 0), (b, 0), ((a - b)*r**2/(a*b - r**2), 2*a*b*r/(a*b - r**2)), (0, r)
    nine_point = circle(((A[0] + C[0])/2, (A[1] + C[1])/2), ((B[0] + C[0])/2, (B[1] + C[1])/2), ((b - a)/2, 0))
    print('Nine-Point Circle Equation:', nine_point, '= 0')
    N = center(nine_point)
    print('Nine-Point Center N:', N)
    x, y = symbols('x, y')
    incircle = x**2 + y**2 - 2*y*r
    Fi = kiss(incircle, nine_point)
    print('Feuerbach Point Fi:', Fi)
    AB = a + b
    AC = b*(a**2 + r**2)/(a*b - r**2)
    BC = a*(b**2 + r**2)/(a*b - r**2)
    # G, H, K are tangent points of BC, AC and AB with AB side excircle 
    AK = (AB + BC - AC)/2
    BK = AB - AK
    K = (AK - a, 0)
    H = ((A[0] - C[0])*AK/AC + A[0], (A[1] - C[1])*AK/AC + A[1])
    G = ((B[0] - C[0])*BK/BC + B[0], (B[1] - C[1])*BK/BC + B[1])
    excircle = circle(G, H, K)
    print('Excircle Equation:', excircle, '= 0')
    Fc = kiss(nine_point, excircle)
    print('Feuerbach Point Fc:', Fc)
    IN, CFc = line(I, N), line(C, Fc)
    X12 = intersect(IN, CFc)
    print('X12:', X12)
    print('(I,N;Fi,X12) =', cross_ratio(I[0], N[0], Fi[0], X12[0]))

if __name__ == '__main__':
    main()