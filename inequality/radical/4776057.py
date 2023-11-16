from sympy import *

# https://math.stackexchange.com/q/4776057

def main():
    x, y, z = symbols('x, y, z', positive = True)
    xyz = (x + y + z)/sqrt(5)
    a, b, c = x/xyz, y/xyz, z/xyz
    # prove sum_cyc(a/sqrt(5 - 4*b*c)) <= 3/sqrt(5)
    # use conclusion from radical3.py
    A, B, C, D = a**2/(5 - 4*b*c), b**2/(5 - 4*c*a), c**2/(5 - 4*a*b), S(9)/5
    f1 = D - A - B - C
    u, v = symbols('u, v', positive = True)
    print('f1 =', factor(f1.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    f2 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    print('f2 =', factor(f2.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    f3 = (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D
    print('f3 =', factor(f3.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))

if __name__ == '__main__':
    main()