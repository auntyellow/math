from sympy import *

def center(P1, P2, P3):
    # return x, y
    xx = [P1[0], P2[0], P3[0]]
    yy = [P1[1], P2[1], P3[1]]
    mat, vec = [], []
    for i in range(3):
        mat.append([2 * xx[i], 2 * yy[i], -1])
        vec.append([simplify(xx[i] * xx[i] + yy[i] * yy[i])])
    coef = Matrix(mat).inv() * Matrix(vec)
    return simplify(coef[0]), simplify(coef[1])

def collinear(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

# Circumcenter, Centroid, and Nine-Point Center are collinear
# Put AB onto x-axis and C onto y-axis
a, b, c = symbols('a, b, c', positive = True)
# a, b, c = 1, 1, sqrt(3)
x, y = symbols('x, y')
orthocenter = (0, a * b / c)
centroid = ((b - a) / 3, c / 3)
circumcenter = center((-a, 0), (b, 0), (0, c))
nine_point = center((b / 2, c / 2), (-a / 2, c / 2), ((b - a) / 2, 0))
print('circumcenter:', circumcenter)
print('nine_point_center:', nine_point)
print(collinear(orthocenter, centroid, circumcenter))
print(collinear(orthocenter, centroid, nine_point))