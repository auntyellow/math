from sympy import *

def line(t01, t02):
    x1, y1, x2, y2, x3, y3 = x, y, cos(t01), sin(t01), cos(t02), sin(t02)
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

def perpendicular(P1, P2, P3):
    return simplify((P1[0] - P2[0]) * P3[0] + (P1[1] - P2[1]) * P3[1])

# https://www.imomath.com/index.php?options=334 (Theorem 9)
t1, t2, t3, t4, x, y = symbols('t1, t2, t3, t4, x, y')
# t1 = 0 can be faster
AB, AC, AD, BC, BD, CD = line(t1, t2), line(t1, t3), line(t1, t4), line(t2, t3), line(t2, t4), line(t3, t4)
E, F, G = intersect(AB, CD), intersect(AD, BC), intersect(AC, BD)

print('E:', E)
print('F:', F)
print('G:', G)
print(perpendicular(E, F, G))
print(perpendicular(F, G, E))
print(perpendicular(G, E, F))