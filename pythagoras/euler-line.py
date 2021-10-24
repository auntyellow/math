from sympy import factor, poly, solve, sqrt
from cartesian import *

def collinear_eq(P1, P2, P3):
    x1, y1, x2, y2, x3, y3 = P1[0], P1[1], P2[0], P2[1], P3[0], P3[1]
    return factor(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)

def dist2(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def main():
    a, b, r = symbols('a, b, r', positive = True)
    A, B = (0, a), (0, -b)
    k, x, y = symbols('k, x, y')
    incircle = x**2 + y**2 - 2*r*x
    incircle_poly = poly(incircle.subs(y, k*x + a), x)
    print('Equation of Incircle and AC:', incircle_poly.expr, '= 0')
    incircle_coeffs = incircle_poly.all_coeffs()
    discriminant = incircle_coeffs[1]**2 - 4*incircle_coeffs[0]*incircle_coeffs[2]
    print('Discriminant of Incircle and AC:', discriminant)
    k = solve(Eq(discriminant, 0), k)[0]
    print('k =', k)
    AC = Eq(y, k*x + a)
    BC = Eq(y, k.subs(a, -b)*x - b)
    # Test case: A is a right angle and AB = AC
    # a0 = r
    # b0 = (sqrt(2)+1)*r
    # A, B = (0, a0), (0, -b0)
    # AC = AC.subs(a, a0).subs(b, b0)
    # BC = BC.subs(a, a0).subs(b, b0)
    print('AC:', AC)
    print('BC:', BC)
    C = intersect(AC, BC)
    print('C:', C)
    print()
    G = ((A[0] + B[0] + C[0])/3, (A[1] + B[1] + C[1])/3)
    print('Centroid:', G)
    H = (factor((A[1] - C[1])*(C[1] - B[1])/C[0]), factor(C[1]))
    print('Othocenter:', H)
    I = (r, 0)
    print('Incenter:', I)
    # print('Are they collinear?', collinear(G, H, I))
    print('They are collinear if and only if', collinear_eq(G, H, I), '= 0')
    AB2 = cancel(dist2(A, B))
    AC2 = cancel(dist2(A, C))
    BC2 = cancel(dist2(B, C))
    print('AB**2 - AC**2 =', factor(AB2 - AC2))
    print('AB**2 - BC**2 =', factor(AB2 - BC2))
    print('AC**2 - BC**2 =', factor(AC2 - BC2))

if __name__ == '__main__':
    main()