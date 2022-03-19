from sympy import *

def reduced(x, y, z, w):
    gcd = gcd_list([x, y, z, w])
    if gcd == 0:
        return 0, 0, 0, 1
    return cancel(x/gcd), cancel(y/gcd), cancel(z/gcd), cancel(w/gcd)

def cross(P1, P2, P3):
    x10, x11, x12, x13 = P1[0], P1[1], P1[2], P1[3]
    x20, x21, x22, x23 = P2[0], P2[1], P2[2], P2[3]
    x30, x31, x32, x33 = P3[0], P3[1], P3[2], P3[3]
    # generated by cross-3d.py
    x = -x11*x22*x33 + x11*x23*x32 + x12*x21*x33 - x12*x23*x31 - x13*x21*x32 + x13*x22*x31
    y = x10*x22*x33 - x10*x23*x32 - x12*x20*x33 + x12*x23*x30 + x13*x20*x32 - x13*x22*x30
    z = -x10*x21*x33 + x10*x23*x31 + x11*x20*x33 - x11*x23*x30 - x13*x20*x31 + x13*x21*x30
    w = x10*x21*x32 - x10*x22*x31 - x11*x20*x32 + x11*x22*x30 + x12*x20*x31 - x12*x21*x30
    return reduced(x, y, z, w)

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q')
    A, B = Matrix([[a + p*e, b + p*f, c + p*g, d + p*h]]), Matrix([[a + q*e, b + q*f, c + q*g, d + q*h]])
    Lx = A.transpose()*B - B.transpose()*A
    L = [Lx[0, 1], Lx[0, 2], Lx[0, 3], Lx[1, 2], Lx[1, 3], Lx[2, 3]]
    print('L =', L)
    gcd = gcd_list(L)
    print('GCD:', gcd)
    for i in range(6):
        L[i] = cancel(L[i]/gcd)
    print('L =', L)
    A, B, C = (a, b, c, d), (e, f, g, h), (j, k, m, n)
    E = cross(A, B, C)
    print('E:', E)

if __name__ == '__main__':
    main()