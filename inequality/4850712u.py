from sympy import *

# https://math.stackexchange.com/q/4850712

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    k, m, n, u, v, x, y, z = symbols('k, m, n, u, v, x, y, z', negative = False)
    # m, n = 5, 13    # non-negative, https://math.stackexchange.com/q/1777075
    # m, n = 63, 164  # non-negative
    # m, n = 121, 315 # negative
    f = sum_cyc(x**3/(n*x**2 + m*y**2) - x/(n + m), (x, y, z))
    print('f =', f)
    fn, fd = fraction(cancel(f))
    # proved or found counterexample by SDS
    print('fn =', fn)
    print('fd =', fd)
    # try to prove or find counterexample by polynomial-prover or SDS
    print('fn(xyz) =', factor(fn.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('fn(xzy) =', factor(fn.subs(z, x*(1 + u)).subs(y, x*(1 + u + v))))

    # https://math.stackexchange.com/q/4850712#comment10335938_4850712
    f = sum_cyc(x**3 + k*x*y**2 - (k + 1)*x**2*y, (x, y, z))
    # negative at z = 0
    f = f.subs(z, 0)
    print('f =', f)
    print('f(xy) =', factor(f.subs(y, x*(1 + u))))
    print('f(yx) =', factor(f.subs(x, y*(1 + u))))
    # f(yx)
    g = -k*u**2 - k*u + u**3 + 2*u**2 + u + 1
    disc = discriminant(g, u)
    print(disc, '= 0')
    k = solve(disc, k)[2]
    print('k =', k, '=', N(k))

if __name__ == '__main__':
    main()