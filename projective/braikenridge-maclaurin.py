from sympy import *

def L(a, b):
    return Eq(y, a * x + b)

def intersect(L1, L2):
    P = solve([L1, L2], (x, y))
    return simplify(P[x]), simplify(P[y])

'''
Braikenridge-Maclaurin theorem is the converse to Pascal's theorem.
Diagram: https://www.cut-the-knot.org/Generalization/OverlookedPascal.shtml
Put I onto origin and GH onto y-axis, and denote 6 lines as:
  AB: y=jx+g, DE: y=kx+g
  BC: y=mx+h, EF: y=nx+h
  AF: y=px,   CD: y=qx
Prove: ABCDEF lie on a conic.
'''

g, h, j, k, m, n, p, q, x, y = symbols('g, h, j, k, m, n, p, q, x, y')
AB, DE, BC, EF, AF, CD = L(j, g), L(k, g), L(m, h), L(n, h), L(p, 0), L(q, 0)
A, E, C = intersect(AB, AF), intersect(DE, EF), intersect(BC, CD)
D, B, F = intersect(CD, DE), intersect(AB, BC), intersect(AF, EF)
print('A:', A)
print('B:', B)
print('C:', C)
print('D:', D)
print('E:', E)
print('F:', F)

'''
Assume the conic doesn't go through origin I, so these points match the conic:
ax^2+bxy+cy^2+dx+ey+1=0
According to:
https://en.wikipedia.org/wiki/Five_points_determine_a_conic#Construction
The proof can be:

mat = []
for P in [A, B, C, D, E, F]:
    x, y = P[0], P[1]
    mat.append([x * x, x * y, y * y, x, y, 1])
print('M =', Matrix(mat))
# print('det M =', Matrix(mat).det())

However, the last line (remarked) is so slow that we had to use 2 tricks:
1. expand determinant early to avoid simplification, then do substitution, see:
   https://stackoverflow.com/a/37056325/4260959
2. multiply each row by LCD to avoid fraction calculation, see:
   https://math.stackexchange.com/a/4236022/919440
'''

points = [A, B, C, D, E, F]
denominators = [j - p, j - m, q - m, q - k, k - n, p - n]
coefficients = [x * x, x * y, y * y, x, y, 1]
subs = {}
mat = []
for s in range(6):
    row = []
    denominator = denominators[s] ** 2
    subs_xy = {}
    subs_xy[x] = points[s][0]
    subs_xy[y] = points[s][1]
    for t in range(6):
        rst = symbols('r' + str(s) + str(t))
        subs[rst] = expand(simplify(N(coefficients[t] * denominator, subs = subs_xy)))
        row.append(rst)
    mat.append(row)
print('M =', N(Matrix(mat), subs = subs))
print('det M =', expand(N(Matrix(mat).det(), subs = subs)))