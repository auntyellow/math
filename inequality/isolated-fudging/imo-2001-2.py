from sympy import *

# https://yufeizhao.com/olympiad/wc08/ineq.pdf
# sum_cyc(a/sqrt(a**2 + 8*b*c)) >= 1

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', positive = True)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c = symbols('a, b, c', positive = True)
    x, y, z = symbols('x, y, z', positive = True)
    f0 = a/sqrt(a**2 + 8*b*c)
    # graph of f0(a=b)
    print('y =', factor(f0.subs(a, x).subs(b, (3 - x)/2).subs(c, (3 - x)/2)))
    print()

    m, n = symbols('m, n')
    n = 1
    g = n*a + m*(b + c)
    h = (n + 2*m)*(a + b + c)/3
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    f = f0**2 - (g/h/3)**2
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
    # graph of g/3h(a=b)
    print('y =', factor((g/3/h).subs(m, m0).subs(a, x).subs(b, (3 - x)/2).subs(c, (3 - x)/2)))
    f = f.subs(m, m0)
    print('f(1,1,1) =', f.subs(a, 1).subs(b, 1).subs(c, 1))
    print('f(1,8,9) =', f.subs(a, 1).subs(b, 8).subs(c, 9))
    # doesn't work
    print('f(1,8,10) =', f.subs(a, 1).subs(b, 8).subs(c, 10))
    print()

    # try quadratic homogeneous polynomial
    p, q = symbols('p, q')
    n = 1
    g = n*a**2 + m*(b**2 + c**2) + p*(a*b + a*c) + q*b*c
    h = (n + 2*m)*(a**2 + b**2 + c**2)/3 + (2*p + q)*(a*b + a*c + b*c)/3
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    f = f0**2 - (g/h/3)**2
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(a, 1).subs(b, 1).subs(c, 1), 0)
    # f_a,b(1,1) = 0
    eq2 = Eq(diff(f.subs(c, 3 - a - b), a).subs(a, 1).subs(b, 1), 0)
    eq3 = Eq(diff(f.subs(c, 3 - a - b), b).subs(a, 1).subs(b, 1), 0)
    # assume f(1,1,0) = f(0,0,1) = 0 ?
    # f0(1,1,0) = 0
    eq4 = Eq(f.subs(a, 1).subs(b, 0).subs(c, 0), 0)
    # f0(0,0,1) = 1, so should verify if g/3h(0,0,1) is positive
    eq5 = Eq(f.subs(a, 0).subs(b, 1).subs(c, 1), 0)
    print('eq1:', factor(eq1)) # True
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3)) # True
    print('eq4:', factor(eq4))
    print('eq5:', factor(eq5))
    mpq = solve([eq2, eq4, eq5], (m, p, q))
    print('mpq =', mpq)
    for mpq0 in mpq:
        print('mpq =', mpq0)
        print('g/3h(0,0,1) =', (g/h/3).subs(m, mpq0[0]).subs(p, mpq0[1]).subs(q, mpq0[2]).subs(a, 1).subs(b, 0).subs(c, 0))
    mpq0 = mpq[1]
    g = g.subs(m, mpq0[0]).subs(p, mpq0[1]).subs(q, mpq0[2])
    h = h.subs(m, mpq0[0]).subs(p, mpq0[1]).subs(q, mpq0[2])
    print('g =', factor(g))
    print('h =', factor(h))
    # graph of g/3h(a=b)
    print('y =', factor((g/h/3).subs(m, mpq0[0]).subs(p, mpq0[1]).subs(q, mpq0[2]).subs(a, x).subs(b, (3 - x)/2).subs(c, (3 - x)/2)))
    f = f.subs(m, mpq0[0]).subs(p, mpq0[1]).subs(q, mpq0[2])
    xyz = (x + y + z)/3
    a0, b0, c0 = x/xyz, y/xyz, z/xyz
    print('a + b + c =', factor(a0 + b0 + c0))
    f = f.subs(a, a0).subs(b, b0).subs(c, c0)
    u, v = symbols('u, v', positive = True)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))

if __name__ == '__main__':
    main()