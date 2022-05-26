from sympy import sqrt, symbols
from homogeneous import *

def sin1(t):
    return t/sqrt(1 + t**2)

def cos1(t):
    return 1/sqrt(1 + t**2)

def sin2(a, b):
    tanA, tanB = a[1]/a[0], b[1]/b[0]
    return cancel(sin1(tanB)*cos1(tanA) - cos1(tanB)*sin1(tanA))

def ratio(a, b, c):
    assert incidence(a, b, c) == 0
    return cancel(sin2(b, a)/sin2(c, b))

def main():
    a, b, c, d, e, f, g, h, j, m, n, p, q, r, s = symbols('a, b, c, d, e, f, g, h, j, m, n, p, q, r, s')
    aa, bb, cc = (a, b, c), (d, e, f), (g, h, j)
    dd, ee, ff = span(m, bb, n, cc), span(p, cc, q, aa), span(r, aa, s, bb)
    print('bd/dc * ce/ea * af/fb =', cancel(ratio(bb, dd, cc)*ratio(cc, ee, aa)*ratio(aa, ff, bb)))

if __name__ == '__main__':
    main()