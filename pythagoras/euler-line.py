from sympy import factor, sqrt
from cartesian import *

def main():
    a, b, r = symbols('a, b, r', positive = True)
    # Test case: A is a right angle and AB = AC
    # a = r
    # b = (sqrt(2) + 1)*r
    A, B = (-a, 0), (b, 0)
    x, y = symbols('x, y')
    incircle = x**2 + y**2 - 2*r*y
    y0 = solve(incircle.subs(x, -r*y/a)/y, y)[0]
    AC = line(A, (-r*y0/a, y0))
    y0 = solve(incircle.subs(x, r*y/b)/y, y)[0]
    BC = line(B, (r*y0/b, y0))
    print('AC:', AC.lhs, '= 0')
    print('BC:', BC.lhs, '= 0')
    C = intersect(AC, BC)
    print('C:', C)
    print()
    G = ((A[0] + B[0] + C[0])/3, (A[1] + B[1] + C[1])/3)
    print('Centroid:', G)
    H = (factor(C[0]), factor((A[0] - C[0])*(C[0] - B[0])/C[1]))
    print('Orthocenter:', H)
    I = (0, r)
    print('Incenter:', I)
    (x1, y1), (x2, y2), (x3, y3) = G, H, I
    print('They are collinear if and only if', factor(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3), '= 0')
    AB2 = cancel(dist2(A, B))
    AC2 = cancel(dist2(A, C))
    BC2 = cancel(dist2(B, C))
    print('AB**2 - AC**2 =', factor(AB2 - AC2))
    print('AB**2 - BC**2 =', factor(AB2 - BC2))
    print('AC**2 - BC**2 =', factor(AC2 - BC2))

if __name__ == '__main__':
    main()