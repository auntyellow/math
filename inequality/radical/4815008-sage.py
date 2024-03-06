from sage.all import *

def main():
    u, v = var('u, v')
    a0 = 4/(1 + u)
    b0 = (4 - a0)/(1 + v)
    c0 = (4 - a0 - b0)/(1 + a0*b0)
    subs = {u: Integer(1)/2 + 1/(1 + u), v: Integer(1)/2/(1 + v)}
    a, b, c = a0.subs(subs), b0.subs(subs), c0.subs(subs)
    A, B, C, D = 1/(a**2 + 4*b*c), 1/(b**2 + 4*a*c), 1/(c**2 + 4*a*b), Integer(25)/16
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