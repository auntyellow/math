from sympy import symbols
from homogeneous import *

def ratio(A, B, C):
    assert incidence(A, B, C) == 0
    return cancel((A[0]/A[2] - B[0]/B[2])/(B[0]/B[2] - C[0]/C[2]))

def main():
    a, b, c, d, e, f, g, h, j, m, n, p, q, r, s = symbols('a, b, c, d, e, f, g, h, j, m, n, p, q, r, s')
    A, B, C = (a, b, c), (d, e, f), (g, h, j)
    D, E, F = span(m, B, n, C), span(p, C, q, A), span(r, A, s, B)
    print('BD/DC * CE/EA * AF/FB =', cancel(ratio(B, D, C)*ratio(C, E, A)*ratio(A, F, B)))

if __name__ == '__main__':
    main()