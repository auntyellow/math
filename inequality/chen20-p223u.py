from sympy import *

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2

def main():
    # ISBN 9787030655189, p223, ex 8.5.2
    # 1 = c <= a <= b
    p, q = symbols('p, q', negative = False)
    A, B, C = (1/(1 + p), 1/(1 + p), 0), (1/(1 + p + q), 0, 1/(1 + p + q)), (0, 1, 1)
    a2, b2, c2 = dist2(B, C), dist2(C, A), dist2(A, B)
    print('a^2 - c^2 =', factor(a2 - c2))
    print('b^2 - a^2 =', factor(b2 - a2)) # not positive?

if __name__ == '__main__':
    main()