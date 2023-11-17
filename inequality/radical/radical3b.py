from sympy import *

def main():
    # prove sqrt(A) + sqrt(B) + sqrt(C) >= sqrt(D)

    # Step 1: remove 1 radical
    # (sqrt(A) + sqrt(B)) + (sqrt(D) - sqrt(C)) >= 0, should prove (I) D - C >= 0
    # (sqrt(A) + sqrt(B)) - (sqrt(D) - sqrt(C)) >= 0 if:
    # (sqrt(A) + sqrt(B))**2 - (sqrt(D) - sqrt(C))**2 = 2*(sqrt(A*B) + sqrt(C*D)) - (D + C - A - B) >= 0

    # Step 2: remove 1 radical
    # 2*(sqrt(A*B) + sqrt(C*D)) + (D + C - A - B) >= 0, should prove (II) D + C - A - B >= 0
    # 2*(sqrt(A*B) + sqrt(C*D)) - (D + C - A - B) >= 0 if:
    # 4*(sqrt(A*B) + sqrt(C*D))**2 - (D + C - A - B)**2 =

    A, B, C, D = symbols('A, B, C, D', positive = True)
    f1 = 4*(sqrt(A*B) + sqrt(C*D))**2 - (D + C - A - B)**2
    print('f1 =', expand(f1))
    # 8*sqrt(A*B*C*D) - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)) >= 0

    # Step 3: remove 1 radical
    # 8*sqrt(A*B*C*D) + (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)) >= 0,
    # should prove (III) A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D) >= 0
    # 8*sqrt(A*B*C*D) - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)) >= 0 if:
    # 64*A*B*C*D - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 >= 0 (IV)

    # Conclusion: sqrt(A) + sqrt(B) + sqrt(C) >= sqrt(D) if (but not only if):
    # (I) D - C >= 0, and
    # (II) D + C - A - B [+ 2*(sqrt(A*B) + sqrt(C*D))] >= 0, and
    # (III) A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D) [+ 8*sqrt(A*B*C*D)] >= 0, and
    # (IV) 64*A*B*C*D - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 >= 0
    # when (I), (II) and (III) holds, equality occurs if and only if (IV)'s equality occurs
 
if __name__ == '__main__':
    main()