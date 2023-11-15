from sympy import *

def main():
    # prove sqrt(A) + sqrt(B) <= sqrt(C)
    # inequality holds only if A + B <= C (I)

    # Step 1: remove 2 radicals
    # (sqrt(A) + sqrt(B)) + sqrt(C) >= 0 is obvious
    # (sqrt(A) + sqrt(B)) - sqrt(C) <= 0 if (and only if?):
    # (sqrt(A) + sqrt(B))**2 - C = 2*sqrt(A*B) - (C - A - B) <= 0

    # Step 2: remove 1 radical
    # 2*sqrt(A*B) + (C - A - B) >= 0 is obvious (because of I)
    # 2*sqrt(A*B) - (C - A - B) <= 0 if (and only if?):
    # 4*A*B - (C - A - B)**2 = 2*(A*B + A*C + B*C) - A**2 - B**2 - C**2 <= 0 (II)

    # Step 3: prove that inequality holds only if
    # 2*(A*B + A*C + B*C) - A**2 - B**2 - C**2 <= 0 (II)
    A, B, C, D = symbols('A, B, C, D', positive = True)
    f2 = 2*(A*B + A*C + B*C) - A**2 - B**2 - C**2
    print('f2 =', factor(f2.subs(C, (sqrt(A) + sqrt(B) + D)**2)))

    # Conclusion: sqrt(A) + sqrt(B) <= sqrt(C) if and only if:
    # (I) A + B <= C, and
    # (II) 2*(A*B + A*C + B*C) - A**2 - B**2 - C**2 <= 0
    # equality occurs if and only if (II)'s equality occurs
    # see ISBN 9787560349800, p322
 
if __name__ == '__main__':
    main()