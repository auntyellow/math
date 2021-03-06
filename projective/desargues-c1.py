from cartesian import *

def L(a, b):
    x, y = symbols('x, y')
    return Eq(y, a*x + b)

def main():
    e, f, g, h, j, k, m, n = symbols('e, f, g, h, j, k, m, n')
    A1B1, A2B2, A1C1, A2C2, B1C1, B2C2 = L(g, 0), L(h, 0), L(j, e), L(k, e), L(m, f), L(n, f)
    A1, A2 = intersect(A1B1, A1C1), intersect(A2B2, A2C2)
    B1, B2 = intersect(A1B1, B1C1), intersect(A2B2, B2C2)
    C1, C2 = intersect(A1C1, B1C1), intersect(A2C2, B2C2)
    A1A2, B1B2, C1C2 = line(A1, A2), line(B1, B2), line(C1, C2)
    print('A1A2:', A1A2.lhs, '= 0')
    print('B1B2:', B1B2.lhs, '= 0')
    print('C1C2:', C1C2.lhs, '= 0')
    print('Are A1A2, B1B2 and C1C2 concurrent?', concurrency(A1A2, B1B2, C1C2) == 0)

if __name__ == '__main__':
    main()