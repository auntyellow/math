from sympy import *

# https://math.stackexchange.com/q/4776057

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c = symbols('a, b, c', negative = False)
    f0 = a/sqrt(5 - 4*b*c)
    s5 = sqrt(5)
    m, n, p, q = symbols('m, n, p, q')
    n = 1
    g = n*a + m*(b + c)
    h = (n + 2*m)*(a + b + c)
    print('sum_cyc(g/h) =', cancel(sum_cyc(g/h, (a, b, c))))
    f = f0**2 - (g/h)**2
    # prove: sum_cyc(f0) >= 1
    # f(s5,0,0) = f(0,s5,0) = f(0,0,s5) = 0
    eq1 = Eq(f.subs(a, s5).subs(b, 0).subs(c, 0), 0)
    eq2 = Eq(f.subs(a, 0).subs(b, s5).subs(c, 0), 0)
    eq3 = Eq(f.subs(a, 0).subs(b, 0).subs(c, s5), 0)
    print('eq1:', factor(eq1))
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3)) # = eq2
    m0 = solve([eq1, eq2], m)
    print('m =', m0)
    m0 = m0[0][0]
    print('g =', factor(g.subs(m, m0)))
    print('h =', factor(h.subs(m, m0)))
    f = f.subs(m, m0)
    x, y, z = symbols('x, y, z', negative = False)
    xyz = (x + y + z)/s5
    a0, b0, c0 = x/xyz, y/xyz, z/xyz
    print('a + b + c =', factor(a0 + b0 + c0))
    f = f.subs(a, a0).subs(b, b0).subs(c, c0)
    u, v = symbols('u, v', negative = False)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    print('f(yxz) =', factor(f.subs(x, y*(1 + u)).subs(z, y*(1 + u + v))))

if __name__ == '__main__':
    main()