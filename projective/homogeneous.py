from sympy import Matrix, factor, gcd

def reduce(x, y, z):
    x1, y1, z1 = factor(x), factor(y), factor(z)
    divisor = gcd(x1, y1, z1)
    return x1 / divisor, y1 / divisor, z1 / divisor

def span(m, P1, n, P2):
    return reduce(m*P1[0] + n*P2[0], m*P1[1] + n*P2[1], m*P1[2] + n*P2[2])

def cross(P1, P2):
    a, b, c, d, e, f = P1[0], P1[1], P1[2], P2[0], P2[1], P2[2]
    # | a b c |
    # | d e f |
    # | x y z |
    return reduce(b*f - c*e, c*d - a*f, a*e - b*d)

def incidence(P1, P2, P3):
    return Matrix([[P1[0], P1[1], P1[2]], [P2[0], P2[1], P2[2]], [P3[0], P3[1], P3[2]]]).det()