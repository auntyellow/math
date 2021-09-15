from sympy import *

def circle(P1, P2, P3):
    # return x, y, r^2
    xx = [P1[0], P2[0], P3[0]]
    yy = [P1[1], P2[1], P3[1]]
    mat, vec = [], []
    for i in range(3):
        mat.append([2 * xx[i], 2 * yy[i], -1])
        vec.append([simplify(xx[i] * xx[i] + yy[i] * yy[i])])
    coef = Matrix(mat).inv() * Matrix(vec)
    x0 = cancel(coef[0])
    y0 = cancel(coef[1])
    return x0, y0, cancel(x0 * x0 + y0 * y0 - coef[2])

# https://en.wikipedia.org/wiki/Nine-point_circle
# https://en.wikipedia.org/wiki/Feuerbach_point
# Nine-point circle is internally tangent to incircle and externally tangent to 3 excircles
# Put AB onto x-axis and C onto y-axis
a, b, c, AC, BC = symbols('a, b, c, AC, BC', positive = True)
# a, b, c, AC, BC = 1, 1, sqrt(3), 2, 2
x, y = symbols('x, y')
A, B, C = (-a, 0), (b, 0), (0, c)
nine_point = circle((b / 2, c / 2), (-a / 2, c / 2), ((b - a) / 2, 0))
print('Nine-Point Circle')
print('x9 =', nine_point[0])
print('y9 =', nine_point[1])
print('r92 =', nine_point[2])

# AB, AC, BC = a + b, sqrt(a * a + c * c), sqrt(b * b + c * c)
AB = a + b
# AD, BE, CF are internal bisectors  
AF = (AB + AC - BC) / 2
BF = AB - AF
F = (AF - a, 0)
E = (a * AF / AC - a, c * AF / AC)
D = (b - b * BF / BC, c * BF / BC)
incircle = circle(D, E, F)
print('Incircle')
print('xi =', incircle[0])
print('yi =', incircle[1])
print('ri2 =', incircle[2])
# G, H, K are tangent points of BC, AC and AB with AB side excircle 
AK = (AB + BC - AC) / 2
BK = AB - AK
K = (AK - a, 0)
H = (-a * AK / AC - a, -c * AK / AC)
G = (b + b * BK / BC, -c * BK / BC)
excircle = circle(G, H, K)
print('Excircle')
print('xe =', excircle[0])
print('ye =', excircle[1])
print('re2 =', excircle[2])