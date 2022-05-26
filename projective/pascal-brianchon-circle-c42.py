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

def point_on_circle(circle_eq, slope):
    x, y = symbols('x, y')
    x0 = solve(Eq(circle_eq.subs(y, slope*x)/x, 0), x)[0]
    return x0, slope*x0

def on_circle(circle_eq, P):
    x, y = symbols('x, y')
    return cancel(circle_eq.subs(x, P[0]).subs(y, P[1])) == 0

def tangent(circle_eq, P):
    x, y = symbols('x, y')
    circle_poly = poly(circle_eq, (x, y))
    d, e, f = circle_poly.nth(1, 0)/2, circle_poly.nth(0, 1)/2, circle_poly.nth(0, 0)
    x0, y0 = P
    return Eq((x0 + d)*x + (y0 + e)*y + (d*x0 + e*y0 + f), 0)

def slope(L):
    p = poly(L.lhs, symbols('x, y'))
    return p.nth(0, 1)/p.nth(1, 0)

def cross_ratio(a, b, c, d):
    return cancel(((a - c)*(b - d)/(a - d)/(b - c)))

def main():
    # A quadrilateral EFGH circumscribed about a unit circle with tangent points ABCD
    a, b, c, d = symbols('a, b, c, d')
    A, B, C = (0, 0), (a, 0), (b, c)
    circle_eq = circle(A, B, C)
    print('Circle Equation:', circle_eq, '= 0')
    D = point_on_circle(circle_eq, d)
    print('D:', D)
    print('Is D on Circle?', on_circle(circle_eq, D))
    AA, BB, CC, DD = tangent(circle_eq, A), tangent(circle_eq, B), tangent(circle_eq, C), tangent(circle_eq, D)
    print('A\'s Tangent:', AA.lhs, '= 0')
    print('B\'s Tangent:', BB.lhs, '= 0')
    print('C\'s Tangent:', CC.lhs, '= 0')
    print('D\'s Tangent:', DD.lhs, '= 0')

    # Prove 2 diagonals and 2 lines connecting to opposite tangent points (AC, BD, EG, FH) are concurrent
    E, F, G, H = intersect(AA, BB), intersect(BB, CC), intersect(CC, DD), intersect(DD, AA)
    AC, BD, EG, FH = line(A, C), line(B, D), line(E, G), line(F, H)
    print('AC:', AC.lhs, '= 0')
    print('BD:', BD.lhs, '= 0')
    print('EG:', EG.lhs, '= 0')
    print('FH:', FH.lhs, '= 0')
    print('Are AC, BD, EG and FH concurrent?', concurrency(AC, BD, EG) == 0 and concurrency(AC, BD, FH) == 0)
    print('(AC,BD;EG,FH) =', cross_ratio(slope(AC), slope(BD), slope(EG), slope(FH)))

    # Prove intersections of 2 opposite tangent lines (aa∩cc and bb∩dd, denoted as J and K), and
    # intersections of 2 opposite edges (AB∩CD and BC∩DA, denoted as L and M), are collinear
    AB, BC, CD, DA = line(A, B), line(B, C), line(C, D), line(D, A)
    J, K, L, M = intersect(AA, CC), intersect(BB, DD), intersect(AB, CD), intersect(DA, BC)
    print('J:', J)
    print('K:', K)
    print('L:', L)
    print('M:', M)
    print('Are JKLM collinear?', collinear(J, K, L) and collinear(J, K, M))
    print('(J,K;L,M) =', cross_ratio(J[0], K[0], L[0], M[0]))

if __name__ == '__main__':
    main()