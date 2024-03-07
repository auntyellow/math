from sympy import *

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c, u, v = symbols('a, b, c, u, v', negative = False)
    A0 = a**2/(a**2 + 8*b*c)
    B0 = cyc(A0, (a, b, c))
    C0 = cyc(B0, (a, b, c))
    subs1 = {b: a*(1 + u), c: a*(1 + v)}
    A0, B0, C0, D0 = factor(A0.subs(subs1)), factor(B0.subs(subs1)), factor(C0.subs(subs1)), 1
    print('f(a=min) =', sqrt(A0) + sqrt(B0) + sqrt(C0) - sqrt(D0))

    # f = 0 iif u = v = 0, so try 0 <= u, v <= U and make U as large as possible
    U = S(11)/6
    subs1 = {u: U/(1 + u), v: U/(1 + v)}
    A, B, C, D = A0.subs(subs1), B0.subs(subs1), C0.subs(subs1), D0
    # try to use conclusion from radical3b.py
    f1 = D - C
    print('f1 =', factor(f1))
    f2 = D + C - A - B
    print('f2 =', factor(f2))
    f3 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D) + 32*A*B*C*D/(A + B)/(C + D)
    # too slow
    # print('f3 =', factor(f3))
    f4 = 64*A*B*C*D - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2
    # too slow
    # print('f4 =', factor(f4))
    # only one negative term so can prove positive easily:
    # k*u**14*v**12 + ... - k*u**13*v**13 + ... + k*u**12*v**14 + ...
    # U = 4/3: k = 50031545098999707
    # U = 11/6: k = 209847509734914867068928
    print()

    # f is ambiguous when u -> +oo. luckily we can try u >= U and make U as small as possible
    # result from sqrt-quadratic.py
    x = symbols('x', negative = False)
    # u >= 11 or smaller doesn't work, should use sqrt(x) >= cubic(x)
    s = -x**2/2 + 3*x/2
    f = s.subs(x, A0) + s.subs(x, B0) + s.subs(x, C0) - D0
    print('f =', factor(f.subs(u, u + 12)))
    # then prove when S(11)/6 <= u <= 12 /\ 0 <= v <= 12 by radical-prover

if __name__ == '__main__':
    main()