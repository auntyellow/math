from sympy import sqrt, symbols
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

def main():
    # This program shows why it is difficult to represent incenter and angle bisector by homogeneous coordinates
    # https://en.wikipedia.org/wiki/Incenter#Cartesian_coordinates
    xA, yA, zA, xB, yB, zB, xC, yC, zC = symbols('xA, yA, zA, xB, yB, zB, xC, yC, zC')
    A, B, C = (xA/zA, yA/zA), (xB/zB, yB/zB), (xC/zC, yC/zC)
    a, b, c = dist(B, C), dist(C, A), dist(A, B)
    I = to_homogeneous(((a*xA/zA + b*xB/zB + c*xC/zC)/(a + b + c), (a*yA/zA + b*yB/zB + c*yC/zC)/(a + b + c)))
    print('I =', I)

if __name__ == '__main__':
    main()