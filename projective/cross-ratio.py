from sympy import cancel, expand, symbols

def span(m, P1, n, P2):
    return m*P1[0] + n*P2[0], m*P1[1] + n*P2[1], m*P1[2] + n*P2[2]

def cross_ratio(A, B, C, D):
    a, b, c, d = A[0]/A[2], B[0]/B[2], C[0]/C[2], D[0]/D[2]
    return cancel((a - c)*(b - d)/(a - d)/(b - c))

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

def cross_ratio_2(A, B, C, D):
    # C=pA+qB, D=rA+sB, (A,B;C,D)=qr/ps
    p, q = dep_coeff(A, B, C)
    r, s = dep_coeff(A, B, D)
    return cancel(q*r/p/s)

def main():
    a, b, c, d, e, f, g, h, j, k, m, n = symbols('a, b, c, d, e, f, g, h, j, k, m, n')
    A, B = (a, 0, b), (c, 0, d)
    C, D = span(1, A, m, B), span(1, A, n, B)
    print('C=A+mB, D=A+nB:')
    print('(A,B;C,D) =', cross_ratio(A, B, C, D))
    print('(A,B;C,D) =', cross_ratio_2(A, B, C, D))
    C, D, E, F = span(e, A, f, B), span(g, A, h, B), span(j, A, k, B), span(m, A, n, B)
    print('C=eA+fB, D=gA+hB, E=jA+kB, F=mA+nB:')
    print('(C,D;E,F) =', cross_ratio(C, D, E, F))
    print('(C,D;E,F) =', cross_ratio_2(C, D, E, F))

if __name__ == '__main__':
    main()