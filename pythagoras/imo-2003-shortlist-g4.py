from sympy import *

def circle(G):
    return Eq(simplify((x - G[0])**2 + (y - G[1])**2 - G[0]**2 - G[1]**2), 0)

def intersect(Ga, Gb):
    return solve([Ga, Gb], (x, y))[1]

def segment(P1, P2):
    return simplify((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)

# https://www.imomath.com/index.php?options=323 (Example 1)
a, b, c, d, k, x, y = symbols('a, b, c, d, k, x, y')
G1, G2, G3, G4 = circle((a, 0)), circle((b, k*b)), circle((c, 0)), circle((d, k*d))
A, B, C, D, P = intersect(G1, G2), intersect(G2, G3), intersect(G3, G4), intersect(G4, G1), (0, 0)
print(simplify(segment(A, B)*segment(B, C)*segment(P, D)**2 - segment(C, D)*segment(D, A)*segment(P, B)**2))