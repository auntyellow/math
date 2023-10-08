from sympy import *

# https://math.stackexchange.com/q/3657950
# sum_cyc(a/(b + c)) >= 3/2

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', positive = True)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c = symbols('a, b, c', positive = True)
    x = symbols('x', positive = True)
    f0 = a/(b + c)
    # graph of f0(b=c)
    print('y =', factor(f0.subs(a, x).subs(b, (3 - x)/2).subs(c, (3 - x)/2)))
    m, n = symbols('m, n')
    n = 1
    g = n*a + m*(b + c)
    h = (n + 2*m)*(a + b + c)/3
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    f = a/(b + c) - g/h/2
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(a, 1).subs(b, 1).subs(c, 1), 0)
    # homogeneous, hence assume a + b + c = 3
    # f_a,b(1,1) = 0
    eq2 = Eq(diff(f.subs(c, 3 - a - b), a).subs(a, 1).subs(b, 1), 0)
    eq3 = Eq(diff(f.subs(c, 3 - a - b), b).subs(a, 1).subs(b, 1), 0)
    print('eq1:', factor(eq1)) # True
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3)) # True
    m0 = solve(eq2, m)
    print('m =', m0)
    m0 = m0[0]
    print('g =', factor(g.subs(m, m0)))
    print('h =', factor(h.subs(m, m0)))
    # graph of g/2h(b=c)
    print('y =', factor((g/h/2).subs(m, m0).subs(a, x).subs(b, (3 - x)/2).subs(c, (3 - x)/2)))
    f = f.subs(m, m0)
    u, v = symbols('u, v', positive = True)
    # a <= b <= c
    print('f(abc) =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    # c <= b <= a
    print('f(cba) =', factor(f.subs(b, c*(1 + u)).subs(a, c*(1 + u + v))))

if __name__ == '__main__':
    main()