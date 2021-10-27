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

def reflect(L1, L2):
    ## TODO
    return None

def main():
    # https://blancosilva.github.io/post/2013/07/15/some-results-related-to-the-feuerbach-point.html (Theorem 2)
    # The Feuerbach point of a triangle is the anti-Steiner point of the Euler line of the intouch triangle with respect to the same intouch triangle.
    a, b, r = symbols('a, b, r', positive = True)
    A, B, C, I = (-a, 0), (b, 0), ((a - b)*r**2/(a*b - r**2), 2*a*b*r/(a*b - r**2)), (0, r)
    A1, B1, C1 = (2*b*r**2/(b**2 + r**2), 2*b**2*r/(b**2 + r**2)), (-2*a*r**2/(a**2 + r**2), 2*a**2*r/(a**2 + r**2)), (0, 0)
    nine_point = circle(((A[0] + C[0])/2, (A[1] + C[1])/2), ((B[0] + C[0])/2, (B[1] + C[1])/2), ((b - a)/2, 0))
    print('Nine-Point Circle:', nine_point, '= 0')
    print('Intouch\'s Circumcircle:', circle(A1, B1, C1), '= 0')
    x, y, z = symbols('x, y, z')
    incircle = x**2 + y**2 - 2*y*r
    G = ((A1[0] + B1[0] + C1[0])/3, (A1[1] + B1[1] + C1[1])/3)
    print('Intouch\'s Centroid:', G)
    euler = line(I, G)
    print('Intouch\'s Euler-Line:', euler)

if __name__ == '__main__':
    main()