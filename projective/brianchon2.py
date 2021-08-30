from sympy import *

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

a, b, c, d, e, f, g, h, j, k, x, y = symbols('a, b, c, d, e, f, g, h, j, k, x, y')
#P = sqrt(c*h**2 + e*h + f)
#Q = sqrt(c*j**2 + e*j + f)
#R = sqrt(a*g**2 + d*g + f)
#S = sqrt(-4*a*c*f + a*e**2 + b**2*f - b*d*e + c*d**2)
P, Q, R, S = symbols('P, Q, R, S')
AF = Eq(y, (2*a*e*g - b*d*g - 2*b*f + d*e + 2*R*S)*(x - g)/(4*a*c*g**2 - b**2*g**2 - 2*b*e*g + 4*c*d*g + 4*c*f - e**2))
AB = Eq(y, (2*a*e*g - b*d*g - 2*b*f + d*e - 2*R*S)*(x - g)/(4*a*c*g**2 - b**2*g**2 - 2*b*e*g + 4*c*d*g + 4*c*f - e**2))
BC = Eq(y, x*(-b*e*h - 2*b*f + 2*c*d*h + d*e + 2*P*S)/(4*c*f - e**2) + h)
CD = Eq(y, x*(-b*e*h - 2*b*f + 2*c*d*h + d*e - 2*P*S)/(4*c*f - e**2) + h)
DE = Eq(y, x*(-b*e*j - 2*b*f + 2*c*d*j + d*e + 2*Q*S)/(4*c*f - e**2) + j)
EF = Eq(y, x*(-b*e*j - 2*b*f + 2*c*d*j + d*e - 2*Q*S)/(4*c*f - e**2) + j)

A, C, E = (g, 0), (0, h), (0, j)
B, D, F = intersect(AB, BC), intersect(CD, DE), intersect(EF, AF)
print('B:', B)
print('D:', D)
print('F:', F)

PP = 8*P*S*a*c*g**2 - 2*P*S*b**2*g**2 - 4*P*S*b*e*g + 8*P*S*c*d*g + 8*P*S*c*f - 2*P*S*e**2 + 8*R*S*c*f - 2*R*S*e**2 - 4*a*b*c*e*g**2*h - 8*a*b*c*f*g**2 + 8*a*c**2*d*g**2*h + 4*a*c*d*e*g**2 - 8*a*c*e*f*g + 2*a*e**3*g + b**3*e*g**2*h + 2*b**3*f*g**2 - 2*b**2*c*d*g**2*h - b**2*d*e*g**2 + 2*b**2*e**2*g*h + 4*b**2*e*f*g - 8*b*c*d*e*g*h - 4*b*c*d*f*g - 4*b*c*e*f*h - 3*b*d*e**2*g + b*e**3*h + 8*c**2*d**2*g*h + 8*c**2*d*f*h + 4*c*d**2*e*g - 2*c*d*e**2*h
QQ = -8*Q*S*a*c*g**2 + 2*Q*S*b**2*g**2 + 4*Q*S*b*e*g - 8*Q*S*c*d*g - 8*Q*S*c*f + 2*Q*S*e**2 - 8*R*S*c*f + 2*R*S*e**2 - 4*a*b*c*e*g**2*j - 8*a*b*c*f*g**2 + 8*a*c**2*d*g**2*j + 4*a*c*d*e*g**2 - 8*a*c*e*f*g + 2*a*e**3*g + b**3*e*g**2*j + 2*b**3*f*g**2 - 2*b**2*c*d*g**2*j - b**2*d*e*g**2 + 2*b**2*e**2*g*j + 4*b**2*e*f*g - 8*b*c*d*e*g*j - 4*b*c*d*f*g - 4*b*c*e*f*j - 3*b*d*e**2*g + b*e**3*j + 8*c**2*d**2*g*j + 8*c**2*d*f*j + 4*c*d**2*e*g - 2*c*d*e**2*j
RR = 2*P*S + 2*Q*S + b*e*h - b*e*j - 2*c*d*h + 2*c*d*j
PQR = PP * QQ * RR
pp = []
for p in [A, B, C, D, E, F]:
    pp.append((expand(p[0] * PQR), expand(p[1] * PQR)))
A, B, C, D, E, F = pp[0], pp[1], pp[2], pp[3], pp[4], pp[5]
print('A =', A[0], ',', A[1])
print('B =', B[0], ',', B[1])
print('C =', C[0], ',', C[1])
print('D =', D[0], ',', D[1])
print('E =', E[0], ',', E[1])
print('F =', F[0], ',', F[1])