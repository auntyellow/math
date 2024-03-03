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
    subs1 = {x: z/(1 + u), y: z/(1 + v)}
    A1, B1, C1, D1 = factor(A0.subs(subs1)), factor(B0.subs(subs1)), factor(C0.subs(subs1)), D0
    # f = 0 iff u = v = 0, see figure in 4575195a.py
    print('f(z=max) =', sqrt(A1) + sqrt(B1) + sqrt(C1) - sqrt(D1))
    # try 0 <= u, v <= U and make U as large as possible
    # 6 doesn't work
    U = 5
    subs1 = {u: U/(1 + u), v: U/(1 + v)}
    # u1, v1 = U, U
    A, B, C, D = A1.subs(subs1), B1.subs(subs1), C1.subs(subs1), D1

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

    # prove when u > U \/ v > U (u and v are not symmetric, so prove when u > U, then prove when v > U)
    # prove when 0 <= 1/u <= 1/U (u >= U) /\ 0 <= v <= 23 by radical-prover
    # factor to avoid division by zero
    A, B, C, D = factor(A1.subs(u, 1/u)), factor(B1.subs(u, 1/u)), factor(C1.subs(u, 1/u)), D1
    print('f(1/u,v) =', sqrt(A) + sqrt(B) + sqrt(C) - sqrt(D))
    # prove when 0 <= u <= 23 /\ 0 <= 1/v <= 1/U (v >= U) by radical-prover
    A, B, C, D = factor(A1.subs(v, 1/v)), factor(B1.subs(v, 1/v)), factor(C1.subs(v, 1/v)), D1
    print('f(u,1/v) =', sqrt(A) + sqrt(B) + sqrt(C) - sqrt(D))
    # hard to prove when u -> oo and v -> oo due to A -> oo and ambiguous B
    '''
    subs1 = {u: 1/u, v:1/v}
    A, B, C, D = factor(A1.subs(subs1)), factor(B1.subs(subs1)), factor(C1.subs(subs1)), D1
    print('f(1/u,1/v) =', sqrt(A) + sqrt(B) + sqrt(C) - sqrt(D))
    '''
    print()

    # prove when x, y << z, plotted in 4575195c.py, which covers u >= 23 and v >= 23
    # z >= m*x, z >= m*y, m >= 2*V - 2, see affine.py
    # 12 doesn't work
    V = 13
    subs1 = {x: x/V, y: y/V}
    subs2 = {z: z + (V - 1)*x/V + (V - 1)*y/V}
    A = A0.subs(subs1).subs(subs2)
    B = B0.subs(subs1).subs(subs2)
    C = C0.subs(subs1).subs(subs2)
    print('f(x,y<<z) =', sqrt(A) + sqrt(B) + sqrt(C) - sqrt(D))
    f = B - D
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + v))))
    print('f(yzx) =', factor(f.subs(z, y*(1 + u)).subs(x, y*(1 + v))))
    print('f(zxy) =', factor(f.subs(x, z*(1 + u)).subs(y, z*(1 + v))))

if __name__ == '__main__':
    main()