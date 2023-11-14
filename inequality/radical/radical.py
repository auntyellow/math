from sympy import *

def main():
    # prove sqrt(A) + sqrt(B) + sqrt(C) <= D
    # inequality holds only if A + B + C <= D**2 (I)

    # Step 1: remove 1 radical
    # (sqrt(A) + sqrt(B)) + (D - sqrt(C)) >= 0 is obvious (because of I)
    # (sqrt(A) + sqrt(B)) - (D - sqrt(C)) <= 0 if (and only if?):
    # (sqrt(A) + sqrt(B))**2 - (D - sqrt(C))**2 = (2*sqrt(A*B) + 4*sqrt(C)) - (D**2 + C - A - B) <= 0

    # Step 2: remove 1 radical
    # 2*(sqrt(A*B) + D*sqrt(C)) + (D**2 + C - A - B) >= 0 is obvious (because of I)
    # 2*(sqrt(A*B) + D*sqrt(C)) - (D**2 + C - A - B) <= 0 if (and only if?):
    # 4*(sqrt(A*B) + D*sqrt(C))**2 - (D**2 + C - A - B)**2 =

    A, B, C, D = symbols('A, B, C, D', positive = True)
    f1 = 4*(sqrt(A*B) + D*sqrt(C))**2 - (D**2 + C - A - B)**2
    print('f1 =', expand(f1))
    # 8*sqrt(A*B*C)*D - (D**4 + A**2 + B**2 + C**2 - 2*(A + B + C)*D**2 - 2*(A*B + A*C + B*C)) <= 0

    # Step 3: remove 1 radical
    # 8*sqrt(A*B*C)*D + (D**4 + A**2 + B**2 + C**2 - 2*(A + B + C)*D**2 - 2*(A*B + A*C + B*C)) >= 0 (Step 4)
    # 8*sqrt(A*B*C)*D - (D**4 + A**2 + B**2 + C**2 - 2*(A + B + C)*D**2 - 2*(A*B + A*C + B*C)) <= 0 if (and only if?):
    # 64*A*B*C*D**2 - (D**4 + A**2 + B**2 + C**2 - 2*(A + B + C)*D**2 - 2*(A*B + A*C + B*C))**2 <= 0 (III)

    # Step 4: prove that inequality holds only if
    # D**4 + A**2 + B**2 + C**2 - 2*(A + B + C)*D**2 - 2*(A*B + A*C + B*C) >= 0 (II)
    f2 = D**4 + A**2 + B**2 + C**2 - 2*(A + B + C)*D**2 - 2*(A*B + A*C + B*C)
    E = symbols('E', positive = True)
    print('f2 =', expand(f2.subs(D, sqrt(A) + sqrt(B) + sqrt(C) + E)))

    # Step 5: prove that inequality holds only if
    # 64*A*B*C*D**2 - (D**4 + A**2 + B**2 + C**2 - 2*(A + B + C)*D**2 - 2*(A*B + A*C + B*C))**2 <= 0 (III)
    f3 = 64*A*B*C*D**2 - (D**4 + A**2 + B**2 + C**2 - 2*(A + B + C)*D**2 - 2*(A*B + A*C + B*C))**2
    print('f3 =', expand(f3.subs(D, sqrt(A) + sqrt(B) + sqrt(C) + E)))

    # Conclusion: sqrt(A) + sqrt(B) + sqrt(C) <= D if and only if:
    # (I) A + B + C <= D**2, and
    # (II) D**4 + A**2 + B**2 + C**2 - 2*(A + B + C)*D**2 - 2*(A*B + A*C + B*C) >= 0, and
    # (III) 64*A*B*C*D**2 - (D**4 + A**2 + B**2 + C**2 - 2*(A + B + C)*D**2 - 2*(A*B + A*C + B*C))**2 <= 0

    # sqrt(A) + sqrt(B) <= sqrt(C) if and only if:
    # (I) A + B <= C, and
    # (II) 2*(A + B)*C <= C**2 + (A - B)**2
    # sqrt(A) + sqrt(B) + sqrt(C) <= sqrt(D) if and only if:
    # (I) A + B + C <= D, and
    # (II) sqrt(A*B) + sqrt(A*C) + sqrt(B*C) <= (D - A - B - C)/2
    # see ISBN 9787560349800, p319, theorem 13.8
 
if __name__ == '__main__':
    main()