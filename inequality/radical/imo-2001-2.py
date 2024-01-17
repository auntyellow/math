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
    A = a**2/(a**2 + 8*b*c)
    B = cyc(A, (a, b, c))
    C = cyc(B, (a, b, c))
    b1, c1 = a*(1 + u), a*(1 + v)
    A, B, C = factor(A.subs(b, b1).subs(c, c1)), factor(B.subs(b, b1).subs(c, c1)), factor(C.subs(b, b1).subs(c, c1))
    f = sqrt(A) + sqrt(B) + sqrt(C) - 1
    # f = 0 iff u = v = 0, see figure in imo-2001-2a.py
    print('f =', f)
    # try 0 <= u <= u1 and 0 <= v <= v1, and make u1 and v1 as large as possible
    u1, v1 = S(4)/3/(1 + u), S(4)/3/(1 + v)
    # u1, v1 = S(4)/3, S(4)/3
    A, B, C, D = A.subs(u, u1).subs(v, v1), B.subs(u, u1).subs(v, v1), C.subs(u, u1).subs(v, v1), 1

    # try to use conclusion from radical3b.py
    f1 = D - C
    print('f1 =', factor(f1))
    f2 = D + C - A - B
    print('f2 =', factor(f2))
    f3 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    print('f3 =', factor(f3))
    f4 = 64*A*B*C*D - (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2
    print('f4 =', factor(f4))

    # TODO prove inequality when u > 4/3 or v > 4/3

if __name__ == '__main__':
    main()