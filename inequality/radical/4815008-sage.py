from sage.all import *

def main():
    u, v = var('u, v')
    a = 4/(1 + u)
    b = (4 - a)/(1 + v)
    c = (4 - a - b)/(1 + a*b)
    A0 = 1/(a**2 + 4*b*c)
    B0 = 1/(b**2 + 4*a*c)
    C0 = 1/(c**2 + 4*a*b)
    D = Integer(25)/16
    subs = {u: Integer(1)/2 + 1/(1 + u)}
    A, B, C = A0.subs(subs), B0.subs(subs), C0.subs(subs)
    # try to use conclusion from radical3b.py
    f1 = D - C
    print('f1 =', factor(f1))
    f2 = D + C - A - B
    print('f2 =', factor(f2))
    f3 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D) + 32*A*B*C*D/(A + B)/(C + D)
    print('f3 =', factor(f3))
    f4 = 64*A*B*C*D - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2
    print('f4 =', factor(f4))

if __name__ == '__main__':
    main()