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
    k, u, v, x, y, z = symbols('k, u, v, x, y, z', negative = False)
    # https://math.stackexchange.com/q/1775572
    # m, n = 5, 8
    # f = sum_cyc(x**4/(n*x**3 + m*y**3) - x/(n + m), (x, y, z))
    # m, n = 5, 13    # non-negative, https://math.stackexchange.com/q/1777075
    # m, n = 63, 164  # non-negative
    # m, n = 121, 315 # negative
    m, n = 1, k
    f = sum_cyc(x**3/(n*x**2 + m*y**2) - x/(n + m), (x, y, z))
    print('f =', f)
    fn, fd = fraction(cancel(f))
    # proved or found counterexample by SDS
    print('fn =', fn)
    print('fd =', fd)
    # try to prove or find counterexample by polynomial-prover or SDS
    print('fn(xyz) =', factor(fn.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('fn(xzy) =', factor(fn.subs(z, x*(1 + u)).subs(y, x*(1 + u + v))))
    # x = min(x, y, z)
    print('fn =', factor(fn.subs(y, x*(1 + u)).subs(z, x*(1 + v))))
    g = -k**2*u**4*v**2 - 2*k**2*u**4*v - k**2*u**4 - 3*k**2*u**3*v**2 - 6*k**2*u**3*v - 3*k**2*u**3 + k**2*u**2*v**3 + k**2*u**2*v**2 - 2*k**2*u**2*v - 2*k**2*u**2 - k**2*u*v**4 - 2*k**2*u*v**3 + k**2*u*v**2 + 2*k**2*u*v - k**2*v**4 - 3*k**2*v**3 - 2*k**2*v**2 + k*u**5*v**2 + 2*k*u**5*v + k*u**5 + k*u**4*v**3 + 8*k*u**4*v**2 + 12*k*u**4*v + 4*k*u**4 - k*u**3*v**4 + 16*k*u**3*v**2 + 24*k*u**3*v + 6*k*u**3 - 4*k*u**2*v**4 - 10*k*u**2*v**3 + 4*k*u**2*v**2 + 16*k*u**2*v + 4*k*u**2 - 5*k*u*v**4 - 16*k*u*v**3 - 14*k*u*v**2 - 4*k*u*v + k*v**5 + 4*k*v**4 + 6*k*v**3 + 4*k*v**2 + u**5 + 5*u**4 - u**3*v**2 - 2*u**3*v + 9*u**3 + u**2*v**5 + 5*u**2*v**4 + 9*u**2*v**3 + 3*u**2*v**2 - 6*u**2*v + 6*u**2 + 2*u*v**5 + 10*u*v**4 + 18*u*v**3 + 9*u*v**2 - 6*u*v + v**5 + 5*v**4 + 9*v**3 + 6*v**2
    # try to find critical point
    g_u, g_v = diff(g, u), diff(g, v)
    print('g_u =', g_u)
    print('g_v =', g_v)
    # too slow
    # print(groebner([g, g_u, g_v], k, u, v))
    # solve v, u and k in 4850712-sage.py
    print()

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