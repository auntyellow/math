from sympy import *

def circle(x0, y0, r):
    return Eq((x - x0)**2 + (y - y0)**2, r**2)

def radical(Ma, Mb):
    p = solve([Ma, Mb], (x, y))
    x1, y1, x2, y2 = simplify(p[0][0]), simplify(p[0][1]), simplify(p[1][0]), simplify(p[1][1])
    return [simplify(y1 - y2), simplify(x2 - x1), simplify(x1 * y2 - x2 * y1)]

# https://en.wikipedia.org/wiki/Radical_axis#Radical_center_of_three_circles,_construction_of_the_radical_axis
# https://en.wikipedia.org/wiki/Power_center_(geometry)
# Circles M1 M2 M3 intersect at P1 Q1 P2 Q2 P3 Q3. Prove P1Q1 P2Q2 P3Q3 meet at the same point.
# Put M1 M2 onto x-axis and M3 onto y-axis
a, b, c, d, e, f, x, y = symbols('a, b, c, d, e, f, x, y')
M1, M2, M3 = circle(a, 0, b), circle(c, 0, d), circle(0, e, f)
print(Matrix([radical(M1, M2), radical(M1, M3), radical(M2, M3)]).det())