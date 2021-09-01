from sympy import *

def L(p, q):
    return Eq(y, p * x + q)

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

def line_coef(P1, P2):
    x1, y1, x2, y2 = P1[0], P1[1], P2[0], P2[1]
    return [simplify(y1 - y2), simplify(x2 - x1), simplify(x1 * y2 - x2 * y1)]

# Lines abc and def are concurrent respectively, and G=a∩d, H=c∩f, J=a∩e, K=b∩f, M=b∩d, N=c∩e.
# Prove GH, JK and MN are collinear.
# Put concurrent point of abc onto origin, and concurrent point of def onto y-axis
a, b, c, d, e, f, g, x, y = symbols('a, b, c, d, e, f, g, x, y')
AA, BB, CC, DD, EE, FF = L(a, 0), L(b, 0), L(c, 0), L(d, g), L(e, g), L(f, g)
G, H = intersect(AA, DD), intersect(CC, FF)
J, K = intersect(AA, EE), intersect(BB, FF)
M, N = intersect(BB, DD), intersect(CC, EE)
print(Matrix([line_coef(G, H), line_coef(J, K), line_coef(M, N)]).det())