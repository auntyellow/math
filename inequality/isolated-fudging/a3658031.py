from sympy import *

# https://math.stackexchange.com/a/3658031
# sum_cyc(1/(2 + a**2 + b**2)) <= 3/4

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
    f0 = 1/(2 + a**2 + b**2)
    # graph of f0(a=b)
    print('y =', factor(f0.subs(c, x).subs(a, (3 - x)/2).subs(b, (3 - x)/2)))
    print()

    # prove directly by buffalo-way
    xyz = (x + y + z)/3
    a0, b0, c0 = x/xyz, y/xyz, z/xyz
    print('a + b + c =', factor(a0 + b0 + c0))
    f = sum_cyc(f0, (a, b, c)).subs(a, a0).subs(b, b0).subs(c, c0) - S(3)/4
    u, v = symbols('u, v', positive = True)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print()

    # isolated fudging by undetermined coefficients
    m, n = symbols('m, n')
    n = 1
    g = n*c + m*(a + b)
    h = (n + 2*m)*(a + b + c)/3
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    f = f0 - g/h/4
    print('f =', f)
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(a, 1).subs(b, 1).subs(c, 1), 0)
    # f_a,b(1,1) = 0
    eq2 = Eq(diff(f.subs(c, 3 - a - b), a).subs(a, 1).subs(b, 1), 0)
    eq3 = Eq(diff(f.subs(c, 3 - a - b), b).subs(a, 1).subs(b, 1), 0)
    print('eq1:', factor(eq1)) # True
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3)) # = eq2
    m0 = solve(eq2, m)
    print('m =', m0)
    m0 = m0[0]
    # graph of g/4h(a=b)
    print('y =', factor((g/h/4).subs(m, m0).subs(c, x).subs(a, (3 - x)/2).subs(b, (3 - x)/2)))
    f = f.subs(m, m0)
    print('f(1,1,2) =', f.subs(a, .8).subs(b, .8).subs(c, 1.4))
    # doesn't work
    print('f(1,2,2) =', f.subs(a, .6).subs(b, 1.2).subs(c, 1.2))
    print()

    # try quadratic homogeneous polynomial
    p, q = symbols('p, q')
    n = 1
    g = n*c**2 + m*(a**2 + b**2) + p*(a*c + b*c) + q*a*b
    h = (n + 2*m)*(a**2 + b**2 + c**2)/3 + (2*p + q)*(a*b + a*c + b*c)/3
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    f = f0 - g/h/4
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(a, 1).subs(b, 1).subs(c, 1), 0)
    # f_a,b(1,1) = 0
    eq2 = Eq(diff(f.subs(c, 3 - a - b), a).subs(a, 1).subs(b, 1), 0)
    eq3 = Eq(diff(f.subs(c, 3 - a - b), b).subs(a, 1).subs(b, 1), 0)
    # assume f(0,0,3) = f(3/2,3/2,0) = 0 ??
    s32 = S(3)/2
    eq4 = Eq(f.subs(a, 0).subs(b, 0).subs(c, 3), 0)
    eq5 = Eq(f.subs(a, s32).subs(b, s32).subs(c, 0), 0)
    print('eq1:', factor(eq1)) # True
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3)) # = eq2
    print('eq4:', factor(eq4))
    print('eq5:', factor(eq5))
    mpq = solve([eq2, eq4, eq5], (m, p, q))
    print('mpq =', mpq)
    # graph of g/4h(a=b), doesn't work because it is below f0(a=b), i.e. f0 - g/h/4 > 0
    print('y =', factor((g/h/4).subs(m, mpq[m]).subs(p, mpq[p]).subs(q, mpq[q]).subs(c, x).subs(a, (3 - x)/2).subs(b, (3 - x)/2)))
    print()

    m0 = solve(eq2, m)
    print('m =', m0)
    m0 = m0[0]
    f = f.subs(m, m0)
    f = f.subs(a, a0).subs(b, b0).subs(c, c0)
    # x <= y <= z
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    # z <= y <= x
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    # k1 <= 0, numerator in f(xyz)
    k1 = 64*p*u**4 + 128*p*u**3*v + 136*p*u**3 + 80*p*u**2*v**2 + 204*p*u**2*v + 72*p*u**2 + 16*p*u*v**3 + 72*p*u*v - 34*p*v**3 - 72*p*v**2 - 32*q*u**4 - 64*q*u**3*v - 96*q*u**3 + 6*q*u**2*v**2 - 144*q*u**2*v - 72*q*u**2 + 38*q*u*v**3 + 36*q*u*v**2 - 72*q*u*v + 25*q*v**4 + 42*q*v**3 + 36*q*v**2 - 28*u**4 - 56*u**3*v - 32*u**3 - 76*u**2*v**2 - 48*u**2*v - 48*u*v**3 - 72*u*v**2 - 17*v**4 - 28*v**3 - 36*v**2
    # k2 >= 0, numerator in f(zyx)
    k2 = 38*p*u**4 + 22*p*u**3*v + 110*p*u**3 - 20*p*u**2*v**2 + 72*p*u**2 - 4*p*u*v**3 - 84*p*u*v**2 - 72*p*u*v - 8*p*v**3 - 72*p*v**2 - 19*q*u**4 + 40*q*u**3*v - 30*q*u**3 + 66*q*u**2*v**2 + 108*q*u**2*v - 36*q*u**2 + 40*q*u*v**3 + 144*q*u*v**2 + 72*q*u*v + 8*q*v**4 + 48*q*v**3 + 72*q*v**2 + 25*u**4 + 20*u**3*v + 44*u**3 - 8*u**2*v**2 + 36*u**2 - 24*u*v**3 - 48*u*v**2 - 4*v**4 - 32*v**3
    # k3 >= 0, denominator in f(xyz) and (zyx)
    k3 = 2*p*u**2 + 2*p*u*v + 8*p*u + 4*p*v + 6*p - q*u**2 - q*u*v - q*v**2 + 4*u**2 + 4*u*v + 8*u + 2*v**2 + 4*v + 6
    p1 = Poly(k1, (u, v))
    p2 = Poly(k2, (u, v))
    p3 = Poly(k3, (u, v))
    print('p1(u,v) =', p1)
    print('p2(u,v) =', p2)
    print('p3(u,v) =', p3)
    # search possible p and q
    fraction_range = [0]
    ratio = S(16)/15
    for i in range(-50, 51):
        k = 0
        for j in continued_fraction_convergents(continued_fraction(ratio**i)):
            k = j
            if j.q >= 100:
                break
        fraction_range.append(k)
        fraction_range.insert(0, -k)
    '''
    for i in fraction_range:
        found = False
        for j in fraction_range:
            hold = True
            for coef in p1.coeffs():
                if coef.subs(p, i).subs(q, j) > 0:
                    hold = False
                    break
            if not hold:
                continue
            for coef in p2.coeffs():
                if coef.subs(p, i).subs(q, j) < 0:
                    hold = False
                    break
            if not hold:
                continue
            for coef in p3.coeffs():
                if coef.subs(p, i).subs(q, j) < 0:
                    hold = False
                    break
            if not hold:
                continue
            p0, q0 = i, j
            print('p =', p0, ', q =', q0)
            found = True
            break
        if found:
            break
    '''
    p0, q0 = S(4)/101, S(74)/109
    # more simple: p0, q0 = 0, S(2)/3
    # can hardly find: p0, q0 = S(1)/3, S(2)/3
    print('g =', factor(g.subs(m, m0).subs(p, p0).subs(q, q0)))
    print('h =', factor(h.subs(m, m0).subs(p, p0).subs(q, q0)))
    # graph of g/4h(a=b)
    print('y =', factor((g/h/4).subs(m, m0).subs(p, p0).subs(q, q0).subs(c, x).subs(a, (3 - x)/2).subs(b, (3 - x)/2)))
    f = f.subs(p, p0).subs(q, q0)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    print()

    # p0, q0 = S(1)/3, S(2)/3
    g = 3*(6*c**2 + a**2 + b**2 + 2*a*c + 2*b*c + 4*a*b)
    h = 32*(a**2 + b**2 + c**2 + a*b + a*c + b*c)
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    # graph of g/h(a=b)
    print('y =', factor((g/h).subs(c, x).subs(a, (3 - x)/2).subs(b, (3 - x)/2)))
    f = f0 - g/h
    f = f.subs(a, a0).subs(b, b0).subs(c, c0)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v)))) # doesn't work
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    j = 75*u**4 + 162*u**3*v + 182*u**3 + 88*u**2*v**2 + 216*u**2*v + 108*u**2 + 4*u*v**3 + 60*u*v**2 + 72*u*v + 4*v**4 - 8*v**3 + 72*v**2
    print('j(uv) =', factor(j.subs(v, u*(1 + v)))) # doesn't work
    print('j(vu) =', factor(j.subs(u, v*(1 + u))))
    k = 4*u**2*v**4 + 20*u**2*v**3 + 124*u**2*v**2 + 366*u**2*v + 333*u**2 - 8*u*v**3 + 36*u*v**2 + 312*u*v + 450*u + 72*v**2 + 216*v + 252
    print('k =', factor(k.subs(u, 1/u)))
    k1 = 72*u**2*v**2 + 216*u**2*v + 252*u**2 - 8*u*v**3 + 36*u*v**2 + 312*u*v + 450*u + 4*v**4 + 20*v**3 + 124*v**2 + 366*v + 333
    print('k1(uv) =', factor(k1.subs(v, u*(1 + v))))
    print('k1(vu) =', factor(k1.subs(u, v*(1 + u))))
    print()

    # p0, q0 = 0, S(2)/3
    g = 3*(6*c**2 + a**2 + b**2 + 4*a*b)
    h = 16*(2*a**2 + 2*b**2 + 2*c**2 + a*b + a*c + b*c)
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    # graph of g/h(a=b)
    print('y =', factor((g/h).subs(c, x).subs(a, (3 - x)/2).subs(b, (3 - x)/2)))
    f = f0 - g/h
    f = f.subs(a, a0).subs(b, b0).subs(c, c0)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))

if __name__ == '__main__':
    main()