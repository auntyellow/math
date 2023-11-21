from sympy import *

# https://www.cut-the-knot.org/m/Algebra/MRozenbergInequalityWithConstraints.shtml

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c = symbols('a, b, c', negative = False)
    f = sum_cyc(4*a*b*(a**2 + b**2) - a**4 - 5*a**2*b**2 - 2*a**2*b*c, (a, b, c))
    print('f =', factor(f))
    # see ggb, sufficient to prove:
    # 1. a, b <= 1 <= c <= 2 (red) and
    # 2. a <= 1 <= b, c <= 2 (organge)
    x, y, z = symbols('x, y, z', negative = False)
    xyz = x + y + z
    a0, b0, c0 = 1 - x/xyz, 1 - y/xyz, 2 - z/xyz
    print('a + b + c =', factor(a0 + b0 + c0))
    f1 = f.subs(a, a0).subs(b, b0).subs(c, c0)
    print('f1 =', factor(f1))
    a0, b0, c0 = x/xyz, 1 + y/xyz, 1 + z/xyz
    print('a + b + c =', factor(a0 + b0 + c0))
    f2 = f.subs(a, a0).subs(b, b0).subs(c, c0)
    print('f2 =', factor(f2))
    # 3. a, b <= 1, 2 <= c: doesn't hold
    a0, b0, c0 = x/xyz, y/xyz, 2 + z/xyz
    print('a + b + c =', factor(a0 + b0 + c0))
    f3 = f.subs(a, a0).subs(b, b0).subs(c, c0)
    print('f3 =', factor(f3))
    print('f(1/3,1/3,7/3) =', f.subs(a, S(1)/3).subs(b, S(1)/3).subs(c, S(7)/3))

if __name__ == '__main__':
    main()