from sympy import *

# https://math.stackexchange.com/q/4575195

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    x, y, z, u, v = symbols('x, y, z, u, v', negative = False)
    A0 = (4*x**2 + y**2)/(3*x**2 + y*z)
    B0 = cyc(A0, (x, y, z))
    C0 = cyc(B0, (x, y, z))
    D0 = S(45)/4
    y1, z1 = x*(1 + u), x*(1 + v)
    A0, B0, C0 = factor(A0.subs(y, y1).subs(z, z1)), factor(B0.subs(y, y1).subs(z, z1)), factor(C0.subs(y, y1).subs(z, z1))
    f = sqrt(A0) + sqrt(B0) + sqrt(C0) - sqrt(D0)
    # f = 0 iff u = v = 0, see figure in 4575195a.py
    print('f =', f)
    # try 0 <= u, v <= U and make U as large as possible
    U = 5
    u1, v1 = U/(1 + u), U/(1 + v)
    # u1, v1 = U, U
    A, B, C, D = A0.subs(u, u1).subs(v, v1), B0.subs(u, u1).subs(v, v1), C0.subs(u, u1).subs(v, v1), D0

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
    # proved by SDS

    # prove when u > U V v > U (u and v are not symmetric, so prove when u > U, then prove when v > U) by radical-prover
    # prove when 0 <= 1/u <= 1/U (u >= U) and 0 <= v <= U
    # factor to avoid division by zero
    A, B, C, D = factor(A0.subs(u, 1/u)), factor(B0.subs(u, 1/u)), factor(C0.subs(u, 1/u)), D0
    print('f(1/u,v) =', sqrt(A) + sqrt(B) + sqrt(C) - sqrt(D0))
    # prove when 0 <= u <= U and 0 <= 1/v <= 1/U (v >= U) (not necessary due to symmetric)
    A, B, C = factor(A0.subs(v, 1/v)), factor(B0.subs(v, 1/v)), factor(C0.subs(v, 1/v))
    print('f(u,1/v) =', sqrt(A) + sqrt(B) + sqrt(C) - sqrt(D0))
    # prove when 0 <= 1/u <= 1/U (u >= U) and 0 <= 1/v <= 1/U (v >= U)
    A, B, C = factor(A0.subs(u, 1/u).subs(v, 1/v)), factor(B0.subs(u, 1/u).subs(v, 1/v)), factor(C0.subs(u, 1/u).subs(v, 1/v))
    print('f(1/u,1/v) =', sqrt(A) + sqrt(B) + sqrt(C) - sqrt(D0))

if __name__ == '__main__':
    main()