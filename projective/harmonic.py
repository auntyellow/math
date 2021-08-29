from sympy import *

def line(p1, p2):
    x1, y1, x2, y2, x3, y3 = x, y, p1[0], p1[1], p2[0], p2[1]
    return Eq(simplify(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3), 0)

def intersect(L1, L2):
    p = solve([L1, L2], (x, y))
    return simplify(p[x]), simplify(p[y])

def cross_ratio(a, b, c, d):
    return simplify((a - c) * (b - d) / (a - d) / (b - c))

def R(A, B, C, D, i):
    return cross_ratio(A[i], B[i], C[i], D[i])

# Given diagram from https://en.wikipedia.org/wiki/Projective_harmonic_conjugate, prove (A,B;C,D)=-1
# Put MN∩KL onto origin and rotate MN onto x-axis
h, k, l, m, n, x, y = symbols('h, k, l, m, n, x, y')
K, L, M, N = (k, h * k), (l, h * l), (0, m), (0, n)
LMA, LNB, NKA, MKB, LKD, MNC = line(L, M), line(L, N), line(N, K), line(M, K), line(L, K), line(M, N)
A, B = intersect(LMA, NKA), intersect(LNB, MKB)
ADBC = line(A, B)
D, C = intersect(ADBC, LKD), intersect(ADBC, MNC)
print(R(A, B, C, D, 0))
print(R(A, B, C, D, 1))