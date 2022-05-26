from sympy import Matrix, cancel, fraction, expand, gcd_list, lcm_list

def reduced(x, y, z):
    gcd = gcd_list([x, y, z])
    return cancel(x/gcd), cancel(y/gcd), cancel(z/gcd)

def span(m, P1, n, P2):
    return reduced(m*P1[0] + n*P2[0], m*P1[1] + n*P2[1], m*P1[2] + n*P2[2])

def cross(P1, P2):
    (a, b, c), (d, e, f) = P1, P2
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

def dep_coeff_index(A, B, C, i, j):
    return expand(B[i]*C[j] - B[j]*C[i]), expand(A[j]*C[i] - A[i]*C[j])

def dep_coeff(A, B, C):
    # return (m, n) such that kC=mA+nB
    m, n = dep_coeff_index(A, B, C, 0, 1)
    if m != 0 and n != 0:
        return m, n
    m, n = dep_coeff_index(A, B, C, 1, 2)
    if m != 0 and n != 0:
        return m, n
    m, n = dep_coeff_index(A, B, C, 2, 0)
    if m != 0 and n != 0:
        return m, n
    return None

def cross_ratio(A, B, C, D):
    # C=pA+qB, D=rA+sB, (A,B;C,D)=qr/ps
    p, q = dep_coeff(A, B, C)
    r, s = dep_coeff(A, B, D)
    return cancel(q*r/p/s)