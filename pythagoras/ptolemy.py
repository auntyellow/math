from sympy import *

def collinear(P):
    return [P[0], P[1], 1]

def concyclic(P):
    x, y = P
    return [x**2 + y**2, x, y, 1]

def det(row_def, *points):
    mat = []
    for point in points:
        mat.append(row_def(point))
    return Matrix(mat).det()

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2

def main():
    # https://en.wikipedia.org/wiki/Ptolemy%27s_theorem
    b, e, f = symbols('b, e, f', positive = True)
    d, x, y = symbols('d, x, y')
    A, B, C, D, E = (0, 0), (b, 0), (x, y), (d, e), (d + f, e)
    # ABCD are concyclic
    circle = det(concyclic, A, B, C, D)
    p = Poly(circle.subs(y, e*x/(d + f)), x)
    # A and C lie on AE, x_A (= 0) and x_C are two roots of p, so use vieta's formula
    C = (-factor(p.nth(1)/p.nth(2)), -factor(e*p.nth(1)/p.nth(2)/(d + f)))
    print('C =', C)
    print('Is C on circle?', cancel(circle.subs({x: C[0], y: C[1]})) == 0)
    denominator = (d + f)**2 + e**2
    B, C, D = (b*denominator, 0), (factor(C[0]*denominator), factor(C[1]*denominator)), (d*denominator, e*denominator)
    print('C =', C)
    print('Are ABCD concyclic?', det(concyclic, A, B, C, D) == 0)
    AB2, CD2, BC2, AD2, AC2, BD2 = dist2(A, B), dist2(C, D), dist2(B, C), dist2(A, D), dist2(A, C), dist2(B, D)
    # AC2*BD2 - AB2*CD2 - AD2*BC2 >= 0 when C on arc BD
    # BC2*AD2 - AB2*CD2 - AC2*BD2 >= 0 when C on arc DA
    # AB2*CD2 - AC2*BD2 - AD2*BC2 >= 0 when C on arc AB
    # let's prove the case C on arc BD
    g = factor(AC2*BD2 - AB2*CD2 - BC2*AD2)
    print('g =', g, '>= 0')
    # too slow
    # h = expand(4*AB2*CD2*BC2*AD2 - g**2)
    # print('h =', h)
    print()

    # https://en.wikipedia.org/wiki/Ptolemy%27s_inequality
    u, v = symbols('u, v', positive = True)
    # wlog, assume A outside circle
    A = (-u*e**2, 0)
    AB2, CD2, BC2, AD2, AC2, BD2 = dist2(A, B), dist2(C, D), dist2(B, C), dist2(A, D), dist2(A, C), dist2(B, D)
    # to prove sqrt(AB2*CD2) + sqrt(BC2*AD2) >= sqrt(AC2*BD2) <==>
    # (sqrt(AB2*CD2) + sqrt(BC2*AD2))**2 = AB2*CD2 + BC2*AD2 + 2*sqrt(AB2*CD2*BC2*AD2) >= AC2*BD2 <==>
    # 2*sqrt(AB2*CD2*BC2*AD2) >= AC2*BD2 - AB2*CD2 + BC2*AD2 = g
    # g <= 0 means Ptolemy's inequality holds
    # g >= 0 should prove h = 4*AB2*CD2*BC2*AD2 - g**2 >= 0
    g = factor(AC2*BD2 - AB2*CD2 - BC2*AD2)
    print('g =', g)
    # g = 2*f*g1*g2*g3*g4, g1 >= 0, g2 >= 0, g3 >= 0 when u + b >= 0
    g4 = d**4 + 2*d**3*f + 2*d**2*e**2 + d**2*f**2 + 2*d*e**2*f + d*e**2*u + e**4 + e**2*f**2
    # g4 >= 0 when d >= 0
    # too slow
    # h = expand(4*AB2*CD2*BC2*AD2 - g**2)
    # proved by SDS
    # print('h =', h)

    # when d <= 0:
    print('g4 =', g4)
    u = factor(solve(g4, u)[0])
    print('g4 >= 0 iff u <=', u)
    u = (d**2 + e**2)*(d**2 + 2*d*f + e**2 + f**2)/((v - d)*e**2)
    print('i.e. u =', u)
    # d <= 0 in A, B, C, D
    A = (-u*e**2, 0)
    AB2, CD2, BC2, AD2, AC2, BD2 = dist2(A, B), dist2(C, D), dist2(B, C), dist2(A, D), dist2(A, C), dist2(B, D)
    g = factor(AC2*BD2 - AB2*CD2 - BC2*AD2)
    print('g =', g, '>= 0')
    # too slow
    # h = cancel(4*AB2*CD2*BC2*AD2 - g**2)
    # proved by SDS
    # print('h =', h)

if __name__ == '__main__':
    main()