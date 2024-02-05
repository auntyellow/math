from sympy import *

# ISBN 9787542848482, p53, §2.3, ex4
# x + y + z = 1
# sum_cyc(x*y/sqrt(x*y + y*z)) <= sqrt(2)/2
# sum_cyc(x*y/sqrt(x*y + y*z)) <= 3*sqrt(3)/sqrt((x + y)*(y + z)*(z + x))/4

def main():
    a, b, c, u, v = symbols('a, b, c, u, v', negative = False)
    abc = a + b + c
    x, y, z = a/abc, b/abc, c/abc
    A, B, C, D = (x*y)**2/(x*y + y*z), (y*z)**2/(y*z + z*x), (z*x)**2/(z*x + x*y), S(27)*(x + y)*(y + z)*(z + x)/16 # S(1)/2
    # use conclusion from radical3.py
    f1 = D - A - B - C
    print('f1 =', factor(f1))
    f2 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    u, v = symbols('u, v', negative = False)
    # print('f2 =', factor(f2)) # for D = S(1)/2
    print('f2 =', factor(f2.subs(b, a*(1 + u)).subs(c, a*(1 + v))))
    f3 = (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D
    print('f3 =', factor(f3.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))

if __name__ == '__main__':
    main()