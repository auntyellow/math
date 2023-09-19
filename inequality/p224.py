from sympy import *

def dist2(A, B):
    return (A[0] - B[0])**2 + (A[1] - B[1])**2 + (A[2] - B[2])**2

def main():
    # ISBN 9787030655189, p224, ex 8.5.2
    # 1 = c <= a <= b
    p, q = symbols('p, q', positive = True)
    A, B, C = (1/(1 + p), 1/(1 + p), 0), (1/(1 + p + q), 0, 1/(1 + p + q)), (0, 1, 1)
    a2, b2, c2 = dist2(B, C), dist2(C, A), dist2(A, B)
    print('a^2 - c^2 =', factor(a2 - c2))
    print('b^2 - a^2 =', factor(b2 - a2)) # not positive?

if __name__ == '__main__':
    main()