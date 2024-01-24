from sympy import *

# https://math.stackexchange.com/q/1777075

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    m, n, u, v, x, y, z = symbols('m, n, u, v, x, y, z', negative = False)
    # m, n = 5, 13    # non-negative, original question
    # m, n = 63, 164  # non-negative
    # m, n = 121, 315 # negative
    f = sum_cyc(x**3/(n*x**2 + m*y**2) - x/(n + m), (x, y, z))
    print('f =', f)
    fn, fd = fraction(cancel(f))
    # proved or found counterexample by SDS
    print('fn =', fn)
    print('fd =', fd)
    # proved or found counterexample by polynomial-prover
    print('fn(xyz) =', factor(fn.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('fn(xzy) =', factor(fn.subs(z, x*(1 + u)).subs(y, x*(1 + u + v))))

if __name__ == '__main__':
    main()