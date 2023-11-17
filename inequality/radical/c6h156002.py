from sympy import *

def main():
    a, b, c = symbols('a, b, c', positive = True)
    abc = a + b + c
    x, y, z = a/abc, b/abc, c/abc
    # https://artofproblemsolving.com/community/c6h156002
    A, B, C, D = 1 - 2*x*y, 1 - 2*x*z, 1 - 2*y*z, 7
    # try to use conclusion from radical3b.py
    f1 = D - C
    print('f1 =', factor(f1))
    f2 = D + C - A - B
    u, v = symbols('u, v', positive = True)
    print('f2 =', factor(f2.subs(b, a + u).subs(c, a + u + v)))
    f3 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    print('f3 =', factor(f3.subs(b, a + u).subs(c, a + u + v)))
    f4 = 64*A*B*C*D - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2
    print('f4 =', factor(f4.subs(b, a + u).subs(c, a + u + v)))
    # equality occurs when u = v = 0, i.e. a = b = c, i.e. x = y = z = 1/3
    # ignore constraints A >= 0, B >= 0 and C >= 0
    print()

    # https://artofproblemsolving.com/community/c6h156002p876416
    A, B, C, D = 9 - 32*x*y, 9 - 32*x*z, 9 - 32*y*z, 49
    f1 = D - C
    print('f1 =', factor(f1))
    f2 = D + C - A - B
    u, v = symbols('u, v', positive = True)
    print('f2 =', factor(f2.subs(b, a + u).subs(c, a + u + v)))
    # isn't always non-negative when ignore constraints A >= 0, B >= 0 and C >= 0
    f3 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    print('f3 =', factor(f3.subs(b, a + u).subs(c, a + u + v)))
    f4 = 64*A*B*C*D - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2
    print('f4 =', factor(f4.subs(b, a + u).subs(c, a + u + v)))
    # equality occurs when a = v = 0, i.e. a = 0 and b = c, i.e. x = 0 and y = z = 1/2

    # use f3's strong form:
    # f3' = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D) + 8*sqrt(A*B*C*D)
    # try to prove 8*sqrt(A*B*C*D) >= 500, i.e. 64*A*B*C*D >= 250000
    # why 500? f3 = 8*(... - 61*v**4)/(... + v)**4 = 8*61 = 488 < 500 when v = +oo
    g3 = 64*A*B*C*D - 250000
    print('g3 =', factor(g3.subs(b, a + u).subs(c, a + u + v)))
    f31 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D) + 500
    print('f3\' =', factor(f31.subs(b, a + u).subs(c, a + u + v)))

if __name__ == '__main__':
    main()