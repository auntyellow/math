from sympy import *

def main():
    # verify radical3 by ISBN 9787560349800, p321
    # sqrt(A) + sqrt(B) + sqrt(C) <= sqrt(D) holds if and only if:
    A, B, C, D = symbols('A, B, C, D', positive = True)
    t, s1, s2, s3 = D, A + B + C, A*B + A*C + B*C, A*B*C
    c0 = t**4 - 4*s1*t**3 + 2*(3*s1**2 - 4*s2)*t**2 - 4*(s1**3 - 4*s1*s2 + 16*s3)*t + (s1**2 - 4*s2)**2
    print('c0 =', expand(c0))
    # see radical3.py
    f3 = (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D
    print('Is c0 >= 0 equivalent to (III)?', expand(c0 - f3) == 0)

    c1 = t**3 - 3*s1*t**2 + (3*s1**2 - 4*s2)*t - (s1**3 - 4*s1*s2 + 16*s3)
    print('c1 =', expand(c1))
    # see radical3.py
    f2 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    print('f2 =', expand(f2))
    print('c1 - f2*(D - A - B - C) =', expand(c1 - f2*(D - A - B - C)))
    # hence c1 implies f2
    E = symbols('E', positive = True)
    print('c1 =', expand(c1.subs(D, (sqrt(A) + sqrt(B) + sqrt(C) + E)**2)))

    c2 = 3*t**2 - 6*s1*t + (3*s1**2 - 4*s2)
    print('c2 =', expand(c2))    
    print('c2 - f2*3 =', expand(c2 - f2*3))
    # hence f2 implies c2, c1 imples c2 (c2 is redundant)

if __name__ == '__main__':
    main()