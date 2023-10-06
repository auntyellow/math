from sympy import *

# Isolated Fudging

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', positive = True)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    # https://math.stackexchange.com/q/3657950
    # sum_cyc(a/(b + c)) >= 3/2
    a, b, c = symbols('a, b, c', positive = True)
    m, n = symbols('m, n')
    n = 1
    g = n*a + m*(b + c)
    h = (n + 2*m)*(a + b + c)/3
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
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

    # https://math.stackexchange.com/a/3658031
    # sum_cyc(1/(2 + a**2 + b**2)) <= 3/4
    x, y, z = symbols('x, y, z', positive = True)
    xyz = (x + y + z)/3
    a, b, c = x/xyz, y/xyz, z/xyz
    print('a + b + c =', factor(a + b + c))
    g = n*x + m*(y + z)
    h = (n + 2*m)*(x + y + z)/3
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (x, y, z))))
    f = 1/(2 + b**2 + c**2) - g/h/4
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(x, 1).subs(y, 1).subs(z, 1), 0)
    # f_x,y,z(1,1,1) = 0
    eq2 = Eq(diff(f, x).subs(x, 1).subs(y, 1).subs(z, 1), 0)
    eq2_ = Eq(diff(f, x).subs(x, 2).subs(y, 2).subs(z, 2), 0)
    eq3 = Eq(diff(f, y).subs(x, 1).subs(y, 1).subs(z, 1), 0)
    eq4 = Eq(diff(f, z).subs(x, 1).subs(y, 1).subs(z, 1), 0)
    print('eq1:', eq1)
    print('eq2:', factor(eq2))
    print('eq2\':', factor(eq2_)) # = eq2
    print('eq3:', factor(eq3)) # = eq2
    print('eq4:', factor(eq4)) # = eq2
    m0 = solve(eq2, m)
    print('m =', m0)
    f = f.subs(m, m0[0])
    print('f(1,1,2) =', f.subs(x, 1).subs(y, 1).subs(z, 2))
    # doesn't work
    print('f(1,2,2) =', f.subs(x, 1).subs(y, 2).subs(z, 2))
    # try quadratic homogeneous polynomial
    p, q = symbols('p, q')
    # m, n, p, q = 1, 6, 2, 4
    g = n*x**2 + m*(y**2 + z**2) + p*(x*y + x*z) + q*y*z
    h = (n + 2*m)*(x**2 + y**2 + z**2)/3 + (2*p + q)*(x*y + x*z + y*z)/3
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (x, y, z))))
    f = 1/(2 + b**2 + c**2) - g/h/4
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(x, 1).subs(y, 1).subs(z, 1), 0)
    # f_x,y,z(1,1,1) = 0
    eq2 = Eq(diff(f, x).subs(x, 1).subs(y, 1).subs(z, 1), 0)
    eq2_ = Eq(diff(f, x).subs(x, 2).subs(y, 2).subs(z, 2), 0)
    eq3 = Eq(diff(f, y).subs(x, 1).subs(y, 1).subs(z, 1), 0)
    eq4 = Eq(diff(f, z).subs(x, 1).subs(y, 1).subs(z, 1), 0)
    print('eq1:', eq1)
    print('eq2:', factor(eq2))
    print('eq2\':', factor(eq2_)) # = eq2
    print('eq3:', factor(eq3)) # = eq2
    print('eq4:', factor(eq4)) # = eq2
    m0 = solve(eq2, m)
    print('m =', m0)
    f = f.subs(m, m0[0])
    print('f =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    j = 64*p*u**4 + 128*p*u**3*v + 136*p*u**3 + 80*p*u**2*v**2 + 204*p*u**2*v + 72*p*u**2 + 16*p*u*v**3 + 72*p*u*v - 34*p*v**3 - 72*p*v**2 - 32*q*u**4 - 64*q*u**3*v - 96*q*u**3 + 6*q*u**2*v**2 - 144*q*u**2*v - 72*q*u**2 + 38*q*u*v**3 + 36*q*u*v**2 - 72*q*u*v + 25*q*v**4 + 42*q*v**3 + 36*q*v**2 - 28*u**4 - 56*u**3*v - 32*u**3 - 76*u**2*v**2 - 48*u**2*v - 48*u*v**3 - 72*u*v**2 - 17*v**4 - 28*v**3 - 36*v**2
    k = 2*p*u**2 + 2*p*u*v + 8*p*u + 4*p*v + 6*p - q*u**2 - q*u*v - q*v**2 + 4*u**2 + 4*u*v + 8*u + 2*v**2 + 4*v + 6
    pj = Poly(j, (u, v))
    pk = Poly(k, (u, v))
    print('p_j(u,v) =', pj)
    print('p_k(u,v) =', pk)
    for coef in pj.coeffs():
        print(coef, '<= 0')
    for coef in pk.coeffs():
        print(coef, '>= 0')
    return

    # https://math.stackexchange.com/q/3657950
    # sum_cyc(sqrt(a/(b + c))) >= 2
    a, b, c = symbols('a, b, c', positive = True)
    g = n*a + m*(b + c)
    h = (n + 2*m)*(a + b + c)/3
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

    # https://yufeizhao.com/olympiad/wc08/ineq.pdf
    # IMO 2001 Problem 2
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

if __name__ == '__main__':
    main()