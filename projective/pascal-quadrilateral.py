from sympy import *

def tangent(t0):
    return Eq(x * cos(t0) + y * sin(t0), 1)

def collinear(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

def line(t01, t02):
    return collinear((x, y), (cos(t01), sin(t01)), (cos(t02), sin(t02)))

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

# A quadrilateral ABCD inscribed in a unit circle with tangent lines abcd
# Prove intersections of 2 opposite edges and 2 opposite tangent lines (AB∩CD, AD∩BC, a∩c, b∩d) are collinear
t1, t2, t3, t4, x, y = symbols('t1, t2, t3, t4, x, y')
a, b, c, d = tangent(t1), tangent(t2), tangent(t3), tangent(t4)
AB, BC, CD, DA = line(t1, t2), line(t2, t3), line(t3, t4), line(t4, t1)
E, F, G, H = intersect(a, c), intersect(b, d), intersect(AB, CD), intersect(DA, BC)
print(collinear(E, F, G))
print(collinear(E, F, H))
# AC∩BD, AD∩BC and a∩b are also collinear
AC, BD = line(t1, t3), line(t2, t4)
J, K = intersect(AC, BD), intersect(a, b)
print(collinear(H, J, K))