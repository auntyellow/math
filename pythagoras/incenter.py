from sympy import sqrt, symbols, expand
from homogeneous import *

def simp_sqrt(expr):
    zA, zB, zC = symbols('zA, zB, zC')
    if expr == zA**2*zB**2:
        return zA*zB
        # return -zA*zB # if zA < 0 xor zB < 0
    if expr == zA**2*zC**2:
        return zA*zC
        # return -zA*zC # if zA < 0 xor zC < 0
    if expr == zB**2*zC**2:
        return zB*zC
        # return -zA*zC # if zB < 0 xor zC < 0
    return sqrt(expr)

def dist(P1, P2):
    f = fraction(cancel((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2))
    return sqrt(f[0])/simp_sqrt(f[1])

def bisector(A, B, C):
    xA, yA, zA, xB, yB, zB, xC, yC, zC = A[0], A[1], A[2], B[0], B[1], B[2], C[0], C[1], C[2]
    r, s, u, v = yA*zB - yB*zA, xB*zA - xA*zB, yB*zC - yC*zB, xC*zB - xB*zC
    m, n, q = r*v + s*u, s*v - r*u, sqrt(r**2 + s**2)*sqrt(u**2 + v**2)
    return reduced(yB*zB*(n + q) + xB*zB*m, xB*zB*(n - q) - yB*zB*m, (yB**2 - xB**2)*m - 2*xB*yB*n)

def equals(P1, P2):
    a, b, c, d, e, f = P1[0], P1[1], P1[2], P2[0], P2[1], P2[2]
    # | a b c |
    # | d e f |
    # | x y z |
    return expand(b*f - c*e) == 0 and expand(c*d - a*f) == 0 and expand(a*e - b*d) == 0

def main():
    # This program shows why it is difficult to represent incenter and angle bisector by homogeneous coordinates
    # https://en.wikipedia.org/wiki/Incenter#Cartesian_coordinates
    r, s, u, v, xA, yA, zA, xB, yB, zB, xC, yC, zC = symbols('r, s, u, v, xA, yA, zA, xB, yB, zB, xC, yC, zC')
    # (xA, yA, zA), (xB, yB, zB), (xC, yC, zC) = (sqrt(3), 0, 1), (0, 1, 1), (0, 0, 1)
    A, B, C = (xA/zA, yA/zA), (xB/zB, yB/zB), (xC/zC, yC/zC)
    a, b, c = dist(B, C), dist(C, A), dist(A, B)
    I = to_homogeneous(((a*xA/zA + b*xB/zB + c*xC/zC)/(a + b + c), (a*yA/zA + b*yB/zB + c*yC/zC)/(a + b + c)))
    print('I:', I)
    A, B, C = to_homogeneous(A), to_homogeneous(B), to_homogeneous(C)
    BI = cross(B, I)
    print('BI:', BI)

    # (xA, yA, zA), (xB, yB, zB), (xC, yC, zC) = (sqrt(3), 0, 1), (0, 1, 1), (0, 0, 1)
    A, B, C = (xA, yA, zA), (xB, yB, zB), (xC, yC, zC)
    ABC = bisector(A, B, C)
    print('Bisector of angle ABC:', ABC)
    print('Is it identical to BI?', equals(ABC, BI))
    BCA = bisector(B, C, A)
    print('Bisector of angle BCA:', BCA)
    CAB = bisector(C, A, B)
    print('Bisector of angle CAB:', CAB)
    print('Are they concurrent?', incidence(ABC, BCA, CAB) == 0)

if __name__ == '__main__':
    main()