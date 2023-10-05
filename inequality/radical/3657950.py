from sympy import *

# https://math.stackexchange.com/q/3657950

def cyc(f):
    a, b, c, t = symbols('a, b, c, t', positive = True)
    return f.subs(c, t).subs(b, c).subs(a, b).subs(t, a)

def sum_cyc(f):
    f1 = cyc(f)
    return f + f1 + cyc(f1)

def main():
    a, b, c = symbols('a, b, c', positive = True)
    # sum_cyc(a/(b + c)) >= 3/2
    m, n = symbols('m, n')
    n = 1
    g = n*a + m*(b + c)
    h = (n + 2*m)*(a + b + c)/3
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h)))
    f = a/(b + c) - g/h/2
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(a, 1).subs(b, 1).subs(c, 1), 0)
    # f_a,b,c(1,1,1) = 0
    eq2 = Eq(diff(f, a).subs(a, 1).subs(b, 1).subs(c, 1), 0)
    eq2_ = Eq(diff(f, a).subs(a, 2).subs(b, 2).subs(c, 2), 0)
    eq3 = Eq(diff(f, b).subs(a, 1).subs(b, 1).subs(c, 1), 0)
    eq4 = Eq(diff(f, c).subs(a, 1).subs(b, 1).subs(c, 1), 0)
    print('eq1:', eq1)
    print('eq2:', factor(eq2))
    print('eq2\':', factor(eq2_)) # = eq2
    print('eq3:', factor(eq3)) # = eq2
    print('eq4:', factor(eq4)) # = eq2
    m0 = solve(eq2, m)
    print('m =', m0)
    u, v = symbols('u, v', positive = True)
    f = f.subs(m, m0[0])
    print('f =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    print()

    # IMO 2001 Problem 2
    # https://yufeizhao.com/olympiad/wc08/ineq.pdf
    f = a**2/(a**2 + 8*b*c) - (g/h/3)**2
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(a, 1).subs(b, 1).subs(c, 1), 0)
    # f_a,b,c(1,1,1) = 0
    eq2 = Eq(diff(f, a).subs(a, 1).subs(b, 1).subs(c, 1), 0)
    eq2_ = Eq(diff(f, a).subs(a, 2).subs(b, 2).subs(c, 2), 0)
    eq3 = Eq(diff(f, b).subs(a, 1).subs(b, 1).subs(c, 1), 0)
    eq4 = Eq(diff(f, c).subs(a, 1).subs(b, 1).subs(c, 1), 0)
    print('eq1:', eq1)
    print('eq2:', factor(eq2))
    print('eq2\':', factor(eq2_)) # = eq2
    print('eq3:', factor(eq3)) # = eq2
    print('eq4:', factor(eq4)) # = eq2
    m0 = solve(eq2, m)
    print('m =', m0)
    f = f.subs(m, m0[0])
    print('f(1,8,9) =', f.subs(a, 1).subs(b, 8).subs(c, 9))
    # doesn't work
    print('f(1,8,10) =', f.subs(a, 1).subs(b, 8).subs(c, 10))
    print()

    # sum_cyc(sqrt(a/(b + c))) >= 2
    f = a/(b + c) - (2*g/h/3)**2
    # f(1,1,0) = 0
    eq1 = Eq(f.subs(a, 1).subs(b, 1).subs(c, 0), 0)
    eq2 = Eq(f.subs(a, 1).subs(b, 0).subs(c, 1), 0)
    eq3 = Eq(f.subs(a, 0).subs(b, 1).subs(c, 1), 0)
    # f_b,c(a=0,1,1) = 0
    eq4 = Eq(diff(f, b).subs(a, 0).subs(b, 1).subs(c, 1), 0)
    eq4_ = Eq(diff(f, b).subs(a, 0).subs(b, 2).subs(c, 2), 0)
    eq5 = Eq(diff(f, c).subs(a, 0).subs(b, 1).subs(c, 1), 0)
    # f_a,c(1,b=0,1) = 0
    eq6 = Eq(diff(f, a).subs(a, 1).subs(b, 0).subs(c, 1), 0)
    eq6_ = Eq(diff(f, a).subs(a, 2).subs(b, 0).subs(c, 2), 0)
    eq7 = Eq(diff(f, c).subs(a, 1).subs(b, 0).subs(c, 1), 0)
    print('eq1:', factor(eq1))
    print('eq2:', factor(eq2)) # = eq1
    print('eq3:', factor(eq3))
    print('eq4:', factor(eq4)) # True
    print('eq4\':', factor(eq4_)) # True
    print('eq5:', factor(eq5)) # True
    print('eq6:', factor(eq6))
    print('eq6\':', factor(eq6_)) # = eq6
    print('eq7:', factor(eq7)) # = eq6
    m0 = solve([eq1, eq3, eq6], m)
    print('m =', m0)
    f = f.subs(m, m0[0][0])
    print('f =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    print()

if __name__ == '__main__':
    main()