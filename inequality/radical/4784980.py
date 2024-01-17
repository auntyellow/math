from sympy import *

# https://math.stackexchange.com/q/4784980

def main():
    a, b, c = symbols('a, b, c', negative = False)
    A, B, C, D = a**2/(4*a**2 + 5*b*c), a**2/(4*b**2 + 5*c*a), c**2/(4*c**2 + 5*a*b), 1
    # prove a stronger form sqrt(A) + sqrt(B) + sqrt(C) <= 1
    # use conclusion from radical3.py
    f1 = D - A - B - C
    u, v = symbols('u, v', negative = False)
    print('f1 =', factor(f1.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    f2 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    print('f2 =', factor(f2.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    f3 = (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D
    print('f3 =', factor(f3.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))

if __name__ == '__main__':
    main()