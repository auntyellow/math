from sympy import *

# https://math.stackexchange.com/q/4746266

def main():
    a, b, c = symbols('a, b, c', negative = False)
    x, y, z = 2*a/(b + c), 2*b/(a + c), 2*c/(a + b)
    print('x*y + x*z + y*z + x*y*z =', factor(x*y + x*z + y*z + x*y*z))
    # use conclusion from radical3.py
    A, B, C, D = 1/(x + 1), 1/(y + 1), 1/(z + 1), S(7)/3 + 4/sqrt(3)
    f1 = D - A - B - C
    u, v = symbols('u, v', negative = False)
    print('f1 =', factor(f1.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    f2 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    print('f2 =', factor(f2.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    f3 = (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D
    print('f3 =', factor(f3.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))

if __name__ == '__main__':
    main()