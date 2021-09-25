from sympy import expand, Matrix

def span(P1, P2, k):
    return P1[0] + P2[0]*k, P1[1] + P2[1]*k, P1[2] + P2[2]*k

def cross(P1, P2):
    a, b, c, d, e, f = P1[0], P1[1], P1[2], P2[0], P2[1], P2[2]
    # | a b c |
    # | d e f |
    # | x y z |
    return expand(b*f - c*e), expand(c*d - a*f), expand(a*e - b*d)

def incidence(P1, P2, P3):
    return expand(Matrix([[P1[0], P1[1], P1[2]], [P2[0], P2[1], P2[2]], [P3[0], P3[1], P3[2]]]).det())