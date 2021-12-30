from sympy import Matrix, cancel, fraction, gcd_list, lcm_list

def reduced(x, y, z):
    gcd = gcd_list([x, y, z])
    return cancel(x/gcd), cancel(y/gcd), cancel(z/gcd)

def cross(P1, P2):
    a, b, c, d, e, f = P1[0], P1[1], P1[2], P2[0], P2[1], P2[2]
    # | a b c |
    # | d e f |
    # | x y z |
    return reduced(b*f - c*e, c*d - a*f, a*e - b*d)

def incidence(P1, P2, P3):
    return Matrix([[P1[0], P1[1], P1[2]], [P2[0], P2[1], P2[2]], [P3[0], P3[1], P3[2]]]).det()

def multiplied(x, y, z):
    x1, y1, z1 = fraction(cancel(x)), fraction(cancel(y)), fraction(cancel(z))
    lcd = lcm_list([x1[1], y1[1], z1[1]])
    return x1[0]*cancel(lcd/x1[1]), y1[0]*cancel(lcd/y1[1]), z1[0]*cancel(lcd/z1[1])

def to_homogeneous(P):
    return multiplied(P[0], P[1], 1)