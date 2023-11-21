from sympy import *

# https://math.stackexchange.com/q/915719

def main():
    x, y, z = symbols('x, y, z', negative = False)
    xyz = (x + y + z)/2
    a, b, c = x/xyz, y/xyz, z/xyz
    A, B, C, D = (a*b)**2/(2*c + a + b), (b*c)**2/(2*a + b + c), (c*a)**2/(2*b + c + a), S(2)/3
    # use conclusion from radical3.py
    f1 = D - A - B - C
    u, v = symbols('u, v', negative = False)
    print('f1 =', factor(f1.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    f2 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    print('f2 =', factor(f2.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    f3 = (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D
    print('f3 =', factor(f3.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))

if __name__ == '__main__':
    main()