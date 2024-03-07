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
    subs1 = {x: z/(1 + u), y: z/(1 + v)}
    A0, B0, C0, D0 = factor(A0.subs(subs1)), factor(B0.subs(subs1)), factor(C0.subs(subs1)), S(45)/4
    print('f(z=max) =', sqrt(A0) + sqrt(B0) + sqrt(C0) - sqrt(D0))

    # f = 0 iff u = v = 0, so try 0 <= u, v <= U and make U as large as possible
    # 6 doesn't work
    U = 5
    subs1 = {u: U/(1 + u), v: U/(1 + v)}
    # u1, v1 = U, U
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
    # proved by SDS
    print()

    # B > D when x, y << z, so try u, v >= V and make V as small as possible
    # 12 doesn't work
    V = 13
    subs1 = {u: V + u, v: V + v}
    A, B, C, D = A0.subs(subs1), B0.subs(subs1), C0.subs(subs1), D0
    # try to use conclusion from radical3b.py
    print('B - D =', factor(B - D))
    print()

    # prove when (u >= U /\ 0 <= v <= V) \/ (v >= U /\ 0 <= u <= V)
    # u and v are not symmetric, so prove before \/, then prove after \/
    # prove when 0 <= 1/u <= 1/U /\ 0 <= v <= V by radical-prover
    # factor to avoid division by zero
    A, B, C, D = factor(A0.subs(u, 1/u)), factor(B0.subs(u, 1/u)), factor(C0.subs(u, 1/u)), D0
    print('f(1/u,v) =', sqrt(A) + sqrt(B) + sqrt(C) - sqrt(D))
    # prove when 0 <= 1/v >= 1/U /\ 0 <= u <= V by radical-prover
    A, B, C, D = factor(A0.subs(v, 1/v)), factor(B0.subs(v, 1/v)), factor(C0.subs(v, 1/v)), D0
    print('f(u,1/v) =', sqrt(A) + sqrt(B) + sqrt(C) - sqrt(D))

if __name__ == '__main__':
    main()