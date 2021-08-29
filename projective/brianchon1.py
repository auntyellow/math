from sympy import *

def line(p1, p2):
    x1, y1, x2, y2, x3, y3 = x, y, p1[0], p1[1], p2[0], p2[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

# In diagram from https://en.wikipedia.org/wiki/Brianchon%27s_theorem, replace P1P2P3P4P5P6 with ABCDEF
# Put A onto origin and rotate AE onto y-axis
a, b, c, d, e, f, g, h, k = symbols('a, b, c, d, e, f, g, h, k')
# Conic: ax^2+bxy+cy^2+dx+ey+1=0
A, C, E = (0, 0), (g, h), (0, f)
# AB,AF:y=k12x; BC,CD:y=m12x+h-m12g; DE,EF:y=n12x+f
(k1, k2) = solve(Eq((d + e * k) ** 2, 4 * (a + b * k + c * k * k)), k)
print(k1, k2)