from sympy import *

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c = symbols('a, b, c', negative = False)
    # use conclusion from radical3.py
    # ISBN 9787560349800, p301, ex 12.9 (p147, ex 6.44; p335, ex 14.29)
    A, B, C, D = a**2/(a + b), b**2/(b + c), c**2/(c + a), S(25)*(a + b + c)/16
    f1 = D - A - B - C
    print('f1 =', factor(f1))
    f2 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    print('f2 =', factor(f2))
    f3 = (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D
    print('f3 =', factor(f3))
    # zero at (3, 1, 0) found by SDS
    print()
    u, v, w = symbols('u, v, w', negative = False)
    a, b, c = u + v, v + w, u + w
    # p302
    A, B, C, D = a**2/(a + b), b**2/(b + c), c**2/(c + a), (3*a + 3*b + 3*c)/2
    f1 = D - A - B - C
    print('f1 =', factor(f1))
    f2 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    print('f2 =', factor(f2))
    f3 = (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D
    print('f3 =', factor(f3))
    # zero at (1, 1, 1) found by SDS

if __name__ == '__main__':
    main()