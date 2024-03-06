from sympy import *

# https://math.stackexchange.com/q/4815008

def main():
    # a*b + a*c + b*c = 3:
    # https://math.stackexchange.com/q/2133854
    # a*b + a*c + b*c + a*b*c = 4:
    # https://math.stackexchange.com/q/3273670
    # a + b + c + a*b*c = 4:
    # https://math.stackexchange.com/q/3663772
    # https://math.stackexchange.com/q/4725605
    # https://math.stackexchange.com/q/4735498
    # https://math.stackexchange.com/q/4815008

    # f = 1/sqrt(a**2 + 4*b*c) + 1/sqrt(b**2 + 4*a*c) + 1/sqrt(c**2 + 4*a*b) - 5/4
    # critical points:
    # f(1, 0) = 0, i.e. a = b = c = 1
    # f(oo, oo) = f(oo, 0) = f(0, ?) = oo, i.e. a*b + b*c + a*c = 0, i.e. a = 4 or b = 4 or c = 4

    u, v = symbols('u, v', negative = False)
    a0 = 4/(1 + u)
    b0 = (4 - a0)/(1 + v)
    c0 = (4 - a0 - b0)/(1 + a0*b0)
    D = S(25)/16
    '''
    subs = {u: S(1)/2 + 1/(1 + u), v: S(1)/2/(1 + v)}
    a, b, c = a0.subs(subs), b0.subs(subs), c0.subs(subs)
    A, B, C = 1/(a**2 + 4*b*c), 1/(b**2 + 4*a*c), 1/(c**2 + 4*a*b)
    # try to use conclusion from radical3b.py
    f1 = D - C
    print('f1 =', factor(f1))
    f2 = D + C - A - B
    print('f2 =', factor(f2))
    f3 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D) + 32*A*B*C*D/(A + B)/(C + D)
    # too slow, calculated in 4815008-sage.py
    print('f3 =', factor(f3))
    f4 = 64*A*B*C*D - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2
    # too slow, calculated in 4815008-sage.py
    print('f4 =', factor(f4))
    '''

    # prove 1/sqrt(b**2 + 4*a*c) >= 5/4 when u <= 1/100
    # 1/50 doesn't work
    subs = {u: S(1)/100/(1 + u)}
    a, b, c = a0.subs(subs), b0.subs(subs), c0.subs(subs)
    f = 1/(b**2 + 4*a*c) - D
    print('f(u<=1/100) =', factor(f))
    print()

    # prove 1/sqrt(a**2 + 4*b*c) >= 5/4 or 1/sqrt(b**2 + 4*a*c) >= 5/4 when u >= 100 and v >= 100
    # 50 doesn't work
    subs = {u: u + 100, v: v + 100}
    a, b, c = a0.subs(subs), b0.subs(subs), c0.subs(subs)
    f = 1/(a**2 + 4*b*c) - D
    g = 1/(b**2 + 4*a*c) - D
    print('f(u,v>=100) =', factor(f))
    print('g(u,v>=100) =', factor(g))
    print()

    # prove 1/sqrt(a**2 + 4*b*c) >= 5/4 or 1/sqrt(c**2 + 4*a*b) >= 5/4 when u >= 100 and v <= 1/100
    # 50 doesn't work
    subs = {u: u + 100, v: S(1)/100/(1 + v)}
    a, b, c = a0.subs(subs), b0.subs(subs), c0.subs(subs)
    f = 1/(a**2 + 4*b*c) - D
    g = 1/(c**2 + 4*a*b) - D
    print('f(u>=100,v<=1/100) =', factor(f))
    print('g(u>=100,v<=1/100) =', factor(g))
    print()

    # 1/100 <= u <= 1/2 and v <= 1/100
    # 3/2 <= u <= 100 and v <= 1/100
    # u >= 1/100 and 1/100 <= v <= 100
    # 1/100 <= u <= 100 and v >= 100

if __name__ == '__main__':
    main()