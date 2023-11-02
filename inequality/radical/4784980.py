from sympy import *

# https://math.stackexchange.com/q/4784980

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', positive = True)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c = symbols('a, b, c', positive = True)
    # prove a stronger form sqrt(A) + sqrt(B) + sqrt(C) <= 2
    A, B, C = a**2/(a**2 + 5*b*c/4), a**2/(b**2 + 5*c*a/4), c**2/(c**2 + 5*a*b/4)
    # A, B, C <= 1 is obvious

    # Step 1: remove 1 radical
    # (sqrt(A) + sqrt(B)) + (2 - sqrt(C)) >= 0 is obvious
    # (sqrt(A) + sqrt(B)) - (2 - sqrt(C)) <= 0 if (and only if?):
    # (sqrt(A) + sqrt(B))**2 - (2 - sqrt(C))**2 = (2*sqrt(A*B) + 4*sqrt(C)) - (4 + C - A - B) <= 0

    # Step 2: remove 1 radical
    # (2*sqrt(A*B) + 4*sqrt(C)) + (4 + C - A - B) >= 0 is obvious
    # (2*sqrt(A*B) + 4*sqrt(C)) - (4 + C - A - B) <= 0 if and only if (and only if?):
    # (2*sqrt(A*B) + 4*sqrt(C))**2 - (4 + C - A - B)**2 =
    '''
    A, B, C = symbols('A, B, C', positive = True)
    f0 = (2*sqrt(A*B) + 4*sqrt(C))**2 - (4 + C - A - B)**2
    print('f0 =', expand(f0))
    '''
    # 16*sqrt(A*B*C) - (16 + A**2 + B**2 + C**2 - 8*(A + B + C) - 2*(A*B + A*C + B*C)) <= 0

    # Step 3: remove 1 radical
    # 16*sqrt(A*B*C) + (16 + A**2 + B**2 + C**2 - 8*(A + B + C) - 2*(A*B + A*C + B*C)) is obvious?
    f0 = 16 + A**2 + B**2 + C**2 - 8*(A + B + C) - 2*(A*B + A*C + B*C)
    u, v = symbols('u, v', positive = True)
    print('f0 =', factor(f0.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    # 16*sqrt(A*B*C) - (16 + A**2 + B**2 + C**2 - 8*(A + B + C) - 2*(A*B + A*C + B*C)) <= 0 if (and only if?):
    # 256*A*B*C - (16 + A**2 + B**2 + C**2 - 8*(A + B + C) - 2*(A*B + A*C + B*C))**2 <= 0

    # Final Step
    f = 256*A*B*C - (16 + A**2 + B**2 + C**2 - 8*(A + B + C) - 2*(A*B + A*C + B*C))**2
    print('f =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    # equality occurs when u = v = 0, i.e. a = b = c

    # Generally: sqrt(A) + sqrt(B) <= sqrt(C) if:
    # A + B <= C and 2*(A + B)*C <= C**2 + (A - B)**2
    # sqrt(A) + sqrt(B) + sqrt(C) <= sqrt(D) if:
    # ... see ISBN 9787560349800, p319, theorem 13.8
 
if __name__ == '__main__':
    main()