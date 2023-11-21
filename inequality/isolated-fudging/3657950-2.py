from sympy import *

# https://math.stackexchange.com/q/3657950
# sum_cyc(sqrt(a/(b + c))) >= 2

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c = symbols('a, b, c', negative = False)
    x = symbols('x', negative = False)
    f0 = sqrt(a/(b + c))
    # graph of f0(b=c)
    print('y =', factor(f0.subs(a, x).subs(b, (3 - x)/2).subs(c, (3 - x)/2)))
    m, n = symbols('m, n')
    n = 1
    g = n*a + m*(b + c)
    h = (n + 2*m)*(a + b + c)/3
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    f = f0**2 - (2*g/h/3)**2
    # f(1,1,0) = f(1,0,1) = f(0,1,1) = 0
    eq1 = Eq(f.subs(a, 1).subs(b, 1).subs(c, 0), 0)
    eq2 = Eq(f.subs(a, 1).subs(b, 0).subs(c, 1), 0)
    eq3 = Eq(f.subs(a, 0).subs(b, 1).subs(c, 1), 0)
    # homogeneous, hence assume a + b = 2
    # f_a(1,1,0) = 0
    eq4 = Eq(diff(f.subs(c, 0).subs(b, 2 - a), a).subs(a, 1), 0)
    # f_a(1,0,1) = 0
    eq5 = Eq(diff(f.subs(b, 0).subs(c, 2 - a), a).subs(a, 1), 0)
    # f_b(0,1,1) = 0
    eq6 = Eq(diff(f.subs(a, 0).subs(c, 2 - b), b).subs(b, 1), 0)
    print('eq1:', factor(eq1))
    print('eq2:', factor(eq2)) # = eq1
    print('eq3:', factor(eq3))
    print('eq4:', factor(eq4))
    print('eq5:', factor(eq5)) # = eq4
    print('eq6:', factor(eq6)) # True
    m0 = solve([eq1, eq3, eq4], m)
    print('m =', m0)
    m0 = m0[0][0]
    print('g =', factor(g.subs(m, m0)))
    print('h =', factor(h.subs(m, m0)))
    # graph of 2g/3h(b=c)
    print('y =', factor((2*g/h/3).subs(m, m0).subs(a, x).subs(b, (3 - x)/2).subs(c, (3 - x)/2)))
    f = f.subs(m, m0)
    u, v = symbols('u, v', negative = False)
    # a <= b <= c
    print('f(abc) =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    # c <= b <= a
    print('f(cba) =', factor(f.subs(b, c*(1 + u)).subs(a, c*(1 + u + v))))

if __name__ == '__main__':
    main()