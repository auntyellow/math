from sympy import *

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    u, v, a, b, c, d, k = symbols('u, v, a, b, c, d, k', negative = False)
    # https://artofproblemsolving.com/community/c6h185286p1023057
    f = sum_cyc(3/(a + 2*b) - 2/(a + b), (a, b, c))
    print('f(abc) =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    print('f(acb) =', factor(f.subs(c, a*(1 + u)).subs(b, a*(1 + u + v)))) # trivially non-negative
    g = 6*u**5 + 5*u**4*v + 24*u**4 - 8*u**3*v**2 + 16*u**3*v + 30*u**3 - 9*u**2*v**3 - 18*u**2*v**2 + 21*u**2*v + 12*u**2 - 2*u*v**4 - 10*u*v**3 + 3*u*v**2 + 12*u*v + 6*v**3 + 12*v**2
    # find u + v = d tangent to g = 0
    disc = discriminant(g.subs(v, d - u), u)
    print(factor(disc), '= 0')
    # d (in the post) = sqrt(1 + u + v)
    d0 = nsolve(cancel(disc/d**2), (0, 10), solver='bisect', verify=False)
    print('u + v =', d0)
    a0 = sqrt(1 + d0)
    print('a0 =', a0)
    gd = g.subs(v, d - u)
    gd1 = diff(gd, u)
    # groebner(..., u, d) can get d0
    B = groebner([gd, gd1], d, u)
    print(B)
    print(factor(B[1]), '= 0')
    u0 = nsolve(cancel(B[1]/u**2), (0, d0), solver='bisect', verify=False)
    # c (in the post) = (1 + u)/sqrt(1 + u + v) 
    print('u0 =', u0)
    print('c0 =', (1 + u0)/a0)

    # https://artofproblemsolving.com/community/c6h185286p1023084
    f = sum_cyc((1 + k)/(a + k*b) - 2/(a + b), (a, b, c))
    print('f(abc) =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    print('f(acb) =', factor(f.subs(c, a*(1 + u)).subs(b, a*(1 + u + v))))
    # assume k > 1 (k = 1 is trivial)
    # f(abc)
    g1 = 2*k**2*u**5 + 5*k**2*u**4*v + 8*k**2*u**4 + 4*k**2*u**3*v**2 + 16*k**2*u**3*v + 10*k**2*u**3 + k**2*u**2*v**3 + 10*k**2*u**2*v**2 + 15*k**2*u**2*v + 4*k**2*u**2 + 2*k**2*u*v**3 + 9*k**2*u*v**2 + 4*k**2*u*v + 2*k**2*v**3 + 4*k**2*v**2 - 5*k*u**4*v - 10*k*u**3*v**2 - 16*k*u**3*v - 6*k*u**2*v**3 - 24*k*u**2*v**2 - 12*k*u**2*v - k*u*v**4 - 8*k*u*v**3 - 12*k*u*v**2 - 2*u**5 - 5*u**4*v - 8*u**4 - 4*u**3*v**2 - 16*u**3*v - 10*u**3 - u**2*v**3 - 10*u**2*v**2 - 15*u**2*v - 4*u**2 - 2*u*v**3 - 9*u*v**2 - 4*u*v - 2*v**3 - 4*v**2
    # f(acb)
    g2 = 2*k**2*u**5 + 5*k**2*u**4*v + 8*k**2*u**4 + 4*k**2*u**3*v**2 + 16*k**2*u**3*v + 10*k**2*u**3 + k**2*u**2*v**3 + 10*k**2*u**2*v**2 + 15*k**2*u**2*v + 4*k**2*u**2 + 2*k**2*u*v**3 + 9*k**2*u*v**2 + 4*k**2*u*v + 2*k**2*v**3 + 4*k**2*v**2 + 5*k*u**4*v + 10*k*u**3*v**2 + 16*k*u**3*v + 6*k*u**2*v**3 + 24*k*u**2*v**2 + 12*k*u**2*v + k*u*v**4 + 8*k*u*v**3 + 12*k*u*v**2 - 2*u**5 - 5*u**4*v - 8*u**4 - 4*u**3*v**2 - 16*u**3*v - 10*u**3 - u**2*v**3 - 10*u**2*v**2 - 15*u**2*v - 4*u**2 - 2*u*v**3 - 9*u*v**2 - 4*u*v - 2*v**3 - 4*v**2
    # g1 is stronger than g2
    print('g2 - g1 =', g2 - g1)
    # find u + v = 1 (c <= 2*a, i.e. 1/sqrt(2) <= a, b, c <= sqrt(2)) tangent to g1 = 0
    disc = discriminant(g1.subs(v, 1 - u), u)
    print(factor(disc), '= 0')
    k0 = nsolve(disc, (1, 10), solver='bisect', verify=False)
    print('k0 =', k0)
    # assume 0 < k < 1, g2 is stronger than g1
    disc = discriminant(g2.subs(v, 1 - u), u)
    print(factor(disc), '= 0')
    k0 = nsolve(disc, (0, 1), solver='bisect', verify=False)
    print('k0 =', k0)
    gk = g1.subs(v, 1 - u)
    gk1 = diff(gk, u)
    # groebner(..., u, k) can get k0
    B = groebner([gk, gk1], k, u)
    print(B)
    print(factor(B[1]), '= 0')
    u0 = nsolve(B[1], (0, 1), solver='bisect', verify=False)
    # c (in the post) = (1 + u)/sqrt(1 + u + v) 
    print('u0 =', u0)
    print('c0 =', N((1 + u0)/sqrt(2)))
    gk = g2.subs(v, 1 - u)
    gk1 = diff(gk, u)
    # groebner(..., u, k) can get k0
    B = groebner([gk, gk1], k, u)
    print(B)
    print(factor(B[1]), '= 0') # same as [gk, gk1] from g1

if __name__ == '__main__':
    main()