from sympy import factor, poly, solve
from cartesian import *

def dist2(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def main():
    a, b, r = symbols('a, b, r', positive = True)
    #b = a
    A, B = (-a, 0), (b, 0)
    k, x, y = symbols('k, x, y')
    incircle = x**2 + y**2 - 2*r*y
    incircle_coeffs = poly(incircle.subs(y, k*(x + a)), x).all_coeffs()
    k = solve(Eq((incircle_coeffs[1]**2 - 4*incircle_coeffs[0]*incircle_coeffs[2])/k, 0), k)[0]
    AC = Eq(y, k*(x + a))
    BC = Eq(y, k.subs(a, -b)*(x - b))
    C = intersect(AC, BC)
    print('C:', C)
    G = ((A[0] + B[0] + C[0])/3, (A[1] + B[1] + C[1])/3)
    print('Centroid:', G)
    H = (C[0], (A[0] - C[0])*(C[0] - B[0])/C[1])
    print('Othocenter:', H)
    I = (0, r)
    print('Incenter:', I)
    print('They are collinear if and only if', factor(collinear(G, H, I).lhs), '= 0')
    print('AC**2 - AB**2 =', cancel(dist2(A, C) - (a + b)**2))
    print('BC**2 - AB**2 =', cancel(dist2(B, C) - (a + b)**2))

if __name__ == '__main__':
    main()