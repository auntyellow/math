from sympy import *

# ISBN 9787542848482, p68, §2.4, ex8
# sum_cyc(sqrt(x**2 + y*z)) <= 3*(x + y + z)/2

def main():
    x, y, z = symbols('x, y, z', positive = True)
    # use conclusion from radical3.py
    A, B, C, D = x**2 + y*z, y**2 + z*x, z**2 + x*y, (3*(x + y + z)/2)**2
    f1 = D - A - B - C
    print('f1 =', factor(f1))
    f2 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    print('f2 =', factor(f2))
    f3 = (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D
    u, v = symbols('u, v', positive = True)
    print('f3 =', factor(f3.subs(y, x + u).subs(z, x + u + v)))
    # holds when x = 0 and v = 0 (y = z)

if __name__ == '__main__':
    main()