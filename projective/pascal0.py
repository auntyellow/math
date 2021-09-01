from sympy import *

def collinear(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

def line(t01, t02):
    return collinear((x, y), (cos(t01), sin(t01)), (cos(t02), sin(t02)))

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

# A hexagon ABCDEF inscribed in a unit circle with polar angles t1..t6
# Prove 3 intersections of opposite edges (AB∩DE, BC∩EF, CD∩FA) are collinear
t1, t2, t3, t4, t5, t6, x, y = symbols('t1, t2, t3, t4, t5, t6, x, y')
AB, BC, CD = line(t1, t2), line(t2, t3), line(t3, t4)
DE, EF, FA = line(t4, t5), line(t5, t6), line(t6, t1)
G, H, K = intersect(AB, DE), intersect(BC, EF), intersect(CD, FA)

print('G:', G)
print('H:', H)
print('K:', K)
print(collinear(G, H, K))