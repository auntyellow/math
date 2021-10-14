from sympy import expand, poly, simplify
from cartesian import *

def foot(P1, P2, P3):
    x, y = symbols('x, y')
    P1P2 = line(P1, P2)
    P3H = Eq((P1[0] - P2[0])*(x - P3[0]) + (P1[1] - P2[1])*(y - P3[1]), 0)
    return intersect(P1P2, P3H)

def circle(P1, P2, P3):
    # return F(x, y) such that F(x, y) = 0 is the circle's equation
    D, E, F, x, y = symbols('D, E, F, x, y')
    circle_eq = Eq(x**2 + y**2 + D*x + E*y + F, 0)
    circle_eqs = []
    circle_eqs.append(circle_eq.subs(x, P1[0]).subs(y, P1[1]))
    circle_eqs.append(circle_eq.subs(x, P2[0]).subs(y, P2[1]))
    circle_eqs.append(circle_eq.subs(x, P3[0]).subs(y, P3[1]))
    s = solve(circle_eqs, (D, E, F))
    return x**2 + y**2 + s[D]*x + s[E]*y + s[F]

def center(c):
    x, y = symbols('x, y')
    return cancel(-poly(c, x).nth(1)/2), cancel(-poly(c, y).nth(1)/2)

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2

def cos2eq(a2, b2, c2, d2, e2, f2):
    left_num = fraction(cancel(a2 + b2 - c2))
    left_den1 = fraction(cancel(a2))
    left_den2 = fraction(cancel(b2))
    right_num = fraction(cancel(d2 + e2 - f2))
    right_den1 = fraction(cancel(d2))
    right_den2 = fraction(cancel(e2))
    left = left_num[0]**2*left_den1[1]*left_den2[1]*right_num[1]**2*right_den1[0]*right_den2[0]
    right = right_num[0]**2*right_den1[1]*right_den2[1]*left_num[1]**2*left_den1[0]*left_den2[0]
    return expand(left - right) == 0

def main():
    a, b, c, d, e, x, y = symbols('a, b, c, d, e, x, y')
    A, B, C, P = (0, a), (b, 0), (c, 0), (d, e)
    D, E, F = foot(B, C, P), foot(C, A, P), foot(A, B, P)
    print('D:', D)
    print('E:', E)
    print('F:', F)
    pedal_circle = circle(D, E, F)
    print('Pedal Circle:', pedal_circle, '= 0')
    M = center(pedal_circle)
    print('M:', M)
    Q = (2*M[0] - P[0], 2*M[1] - P[1])
    print('Q:', Q)
    G, H, J = foot(B, C, Q), foot(C, A, Q), foot(A, B, Q)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Is G on Pedal Circle?', simplify(pedal_circle.subs(x, G[0]).subs(y, G[1])) == 0)
    print('Is H on Pedal Circle?', simplify(pedal_circle.subs(x, H[0]).subs(y, H[1])) == 0)
    print('Is J on Pedal Circle?', simplify(pedal_circle.subs(x, J[0]).subs(y, J[1])) == 0)
    AB2, AC2, BC2 = dist2(A, B), dist2(A, C), dist2(B, C)
    PA2, PB2, PC2 = dist2(P, A), dist2(P, B), dist2(P, C)
    QA2, QB2, QC2 = dist2(Q, A), dist2(Q, B), dist2(Q, C)
    print('cos²∠PAB = cos²∠QAC?', cos2eq(PA2, AB2, PB2, QA2, AC2, QC2))
    print('cos²∠PAC = cos²∠QAB?', cos2eq(PA2, AC2, PC2, QA2, AB2, QB2))
    print('cos²∠PBA = cos²∠QBC?', cos2eq(PB2, AB2, PA2, QB2, BC2, QC2))
    print('cos²∠PBC = cos²∠QBA?', cos2eq(PB2, BC2, PC2, QB2, AB2, QA2))
    print('cos²∠PCA = cos²∠QCB?', cos2eq(PC2, AC2, PA2, QC2, BC2, QB2))
    print('cos²∠PCB = cos²∠QCA?', cos2eq(PC2, BC2, PB2, QC2, AC2, QA2))

if __name__ == '__main__':
    main()