from sympy import *

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

a, b, c, d, e, f, g, h, j, k, x, y = symbols('a, b, c, d, e, f, g, h, j, k, x, y')
#P = sqrt((c*h**2 + e*h + f)*(-4*a*c*f + a*e**2 + b**2*f - b*d*e + c*d**2))
#Q = sqrt((c*j**2 + e*j + f)*(-4*a*c*f + a*e**2 + b**2*f - b*d*e + c*d**2))
#R = sqrt((a*g**2 + d*g + f)*(-4*a*c*f + a*e**2 + b**2*f - b*d*e + c*d**2))
P, Q, R = symbols('P, Q, R')
AF = Eq(y, (2*a*e*g - b*d*g - 2*b*f + d*e + 2*R)*(x - g)/(4*a*c*g**2 - b**2*g**2 - 2*b*e*g + 4*c*d*g + 4*c*f - e**2))
AB = Eq(y, (2*a*e*g - b*d*g - 2*b*f + d*e - 2*R)*(x - g)/(4*a*c*g**2 - b**2*g**2 - 2*b*e*g + 4*c*d*g + 4*c*f - e**2))
BC = Eq(y, x*(-b*e*h - 2*b*f + 2*c*d*h + d*e + 2*P)/(4*c*f - e**2) + h)
CD = Eq(y, x*(-b*e*h - 2*b*f + 2*c*d*h + d*e - 2*P)/(4*c*f - e**2) + h)
DE = Eq(y, x*(-b*e*j - 2*b*f + 2*c*d*j + d*e + 2*Q)/(4*c*f - e**2) + j)
EF = Eq(y, x*(-b*e*j - 2*b*f + 2*c*d*j + d*e - 2*Q)/(4*c*f - e**2) + j)

A, C, E = (g, 0), (0, h), (0, j)
B, D, F = intersect(AB, BC), intersect(CD, DE), intersect(EF, AF)
print('B:', B)
print('D:', D)
print('F:', F)