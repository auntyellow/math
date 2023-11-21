from sympy import *

def main():
    # prove sqrt(A) + sqrt(B) + sqrt(C) <= sqrt(D)
    # inequality holds only if A + B + C <= D (I)

    # Step 1: remove 2 radicals
    # (sqrt(A) + sqrt(B)) + (sqrt(D) - sqrt(C)) >= 0 is obvious (because of I)
    # (sqrt(A) + sqrt(B)) - (sqrt(D) - sqrt(C)) <= 0 if (and only if?):
    # (sqrt(A) + sqrt(B))**2 - (sqrt(D) - sqrt(C))**2 = 2*(sqrt(A*B) + sqrt(C*D)) - (D + C - A - B) <= 0

    # Step 2: remove 1 radical
    # 2*(sqrt(A*B) + sqrt(C*D)) + (D + C - A - B) >= 0 is obvious (because of I)
    # 2*(sqrt(A*B) + sqrt(C*D)) - (D + C - A - B) <= 0 if (and only if?):
    # 4*(sqrt(A*B) + sqrt(C*D))**2 - (D + C - A - B)**2 =

    A, B, C, D = symbols('A, B, C, D', negative = False)
    f20 = 4*(sqrt(A*B) + sqrt(C*D))**2 - (D + C - A - B)**2
    print('f2_0 =', expand(f20))
    # 8*sqrt(A*B*C*D) - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)) <= 0

    # Step 3: remove 1 radical
    # 8*sqrt(A*B*C*D) + (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)) >= 0 (Step 4)
    # 8*sqrt(A*B*C*D) - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)) <= 0 if (and only if?):
    # 64*A*B*C*D - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 <= 0 (III)

    # Step 4: prove that inequality holds only if
    # A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D) >= 0 (II)
    f2 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    E = symbols('E', negative = False)
    print('f2 =', expand(f2.subs(D, (sqrt(A) + sqrt(B) + sqrt(C) + E)**2)))

    # Step 5: prove that inequality holds only if
    # (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D >= 0 (III)
    f3 = (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D
    print('f3 =', factor(f3.subs(D, (sqrt(A) + sqrt(B) + sqrt(C) + E)**2)))

    # Conclusion: sqrt(A) + sqrt(B) + sqrt(C) <= sqrt(D) if and only if:
    # (I) D - A - B - C >= 0, and
    # (II) A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D) >= 0, and
    # (III) (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D >= 0
    # equality occurs if and only if (III)'s equality occurs
    # see ISBN 9787560349800, p321
 
if __name__ == '__main__':
    main()