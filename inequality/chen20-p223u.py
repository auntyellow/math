from sympy import *

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2 + (P1[2] - P2[2])**2

def main():
    # ISBN 9787030655189, p223, ex 8.5.2
    # 1 = c <= a <= b
    p, q = symbols('p, q', negative = False)
    A, B, C = (1/(1 + p), 1/(1 + p), 0), (1/(1 + p + q), 0, 1/(1 + p + q)), (0, 1, 1)
    AB2, AC2, BC2 = dist2(A, B), dist2(A, C), dist2(B, C)
    print('BC^2 - AB^2 =', factor(BC2 - AB2)) # BC >= AB
    print('AC^2 - AB^2 =', factor(AC2 - AB2)) # AC >= AB
    print('AC^2 - BC^2 =', factor(AC2 - BC2)) # may be positive or negative
    print('p >= 1 \/ (p < 1 /\ q >= 1/p - p) ==> AC <= BC')
    a2, b2 = BC2/AB2, AC2/AB2
    print('a^2 =', factor(a2))
    print('b^2 =', factor(b2))
    print('p < 1 /\ q <= 1/p - p ==> AC >= BC')
    a2, b2 = AC2/AB2, BC2/AB2
    print('a^2 =', factor(a2))
    print('b^2 =', factor(b2))

if __name__ == '__main__':
    main()