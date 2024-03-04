from sympy import *

# IMO 2001 problem 2
# sum_cyc(a/sqrt(a**2 + 8*b*c)) >= 1

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c = symbols('a, b, c', negative = False)
    f2 = a**2/(a**2 + 8*b*c)

    m, n = symbols('m, n')
    n = 1
    g = n*a + m*(b + c)
    h = (n + 2*m)*(a + b + c)
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    f = f2 - (g/h)**2
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
    f = f.subs(m, m0)
    print('f(1,1,1) =', f.subs(a, 1).subs(b, 1).subs(c, 1))
    print('f(1,8,9) =', f.subs(a, 1).subs(b, 8).subs(c, 9))
    # doesn't work
    print('f(1,8,10) =', f.subs(a, 1).subs(b, 8).subs(c, 10))
    print()

    # try piecewise
    u, v = symbols('u, v', negative = False)
    # U = S(11)/2 can guarantee g = a - (b + c)/11 >= 0
    U = S(11)/2
    # a <= b <= c <= U*a
    print('f(abcU) =', factor(f.subs(c, a*(U + u)/(1 + u)).subs(b, a*(U + u + v)/(1 + u + v))))
    print('g(abcU) =', factor(g.subs(c, a*(U + u)/(1 + u)).subs(b, a*(U + u + v)/(1 + u + v)).subs(m, m0)))
    # c <= b <= a <= U*c
    print('f(cbaU) =', factor(f.subs(a, c*(U + u)/(1 + u)).subs(b, c*(U + u + v)/(1 + u + v))))
    print('g(cbaU) =', factor(g.subs(a, c*(U + u)/(1 + u)).subs(b, c*(U + u + v)/(1 + u + v)).subs(m, m0)))
    # b <= a <= c <= U*b
    print('f(bacU) =', factor(f.subs(c, b*(U + u)/(1 + u)).subs(a, b*(U + u + v)/(1 + u + v))))
    print('g(bacU) =', factor(g.subs(c, b*(U + u)/(1 + u)).subs(a, b*(U + u + v)/(1 + u + v)).subs(m, m0)))
    print()
    # f(1,0,0) = 0
    f = f2 - (g/h)**2
    eq4 = Eq(f.subs(a, 1).subs(b, 0).subs(c, 0), 0)
    print('eq4:', factor(eq4))
    m0 = solve(eq4, m)
    print('m =', m0)
    m0 = m0[1]
    f = f.subs(m, m0)
    # V = 5 doesn't work
    V = 6
    # a <= b <= c/V
    print('f(abVc) =', factor(f.subs(b, c/V/(1 + u)).subs(a, c/V/(1 + u + v))))
    # c <= b <= a/V
    print('f(cbVa) =', factor(f.subs(b, a/V/(1 + u)).subs(c, a/V/(1 + u + v))))
    # b <= a <= c/V
    print('f(baVc) =', factor(f.subs(a, c/V/(1 + u)).subs(b, c/V/(1 + u + v))))
    print()
    # remaining areas
    f = f2 - (g/h)**2
    U, V = 100, S(100)/99
    # a <= b <= V*a, c <= b/U, non-negative
    print('f(cUabV) =', factor(f.subs(c, b/(U + u)).subs(b, a*(V + v)/(1 + v))))
    # c <= b <= V*c, a <= b/U, negative, unable to cover area near (0, 1, 1)
    print('f(aUcbV) =', factor(f.subs(a, b/(U + u)).subs(b, c*(V + v)/(1 + v))))
    # b <= a <= V*b, c <= a/U, non-negative
    print('f(cUbaV) =', factor(f.subs(c, a/(U + u)).subs(a, b*(V + v)/(1 + v))))
    print()

    # try quadratic homogeneous polynomial
    p, q = symbols('p, q')
    n = 1
    g = n*a**2 + m*(b**2 + c**2) + p*(a*b + a*c) + q*b*c
    h = (n + 2*m)*(a**2 + b**2 + c**2) + (2*p + q)*(a*b + a*c + b*c)
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    f = f2 - (g/h)**2
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(a, 1).subs(b, 1).subs(c, 1), 0)
    # f_a,b(1,1) = 0
    eq2 = Eq(diff(f.subs(c, 3 - a - b), a).subs(a, 1).subs(b, 1), 0)
    eq3 = Eq(diff(f.subs(c, 3 - a - b), b).subs(a, 1).subs(b, 1), 0)
    # f(1,1,0) = 0
    eq4 = Eq(f.subs(a, 1).subs(b, 0).subs(c, 0), 0)
    print('eq1:', factor(eq1)) # True
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3)) # True
    print('eq4:', factor(eq4))
    mp = solve([eq2, eq4], (m, p))
    print('mp =', mp)
    m0, p0 = mp[1]
    print('m =', m0)
    print('p =', p0)
    f = f.subs(m, m0).subs(p, p0)
    # a <= b <= c
    print('f(abc) =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    # c <= b <= a
    print('f(cba) =', factor(f.subs(b, c*(1 + u)).subs(a, c*(1 + u + v))))
    # b <= a <= c
    print('f(bac) =', factor(f.subs(a, b*(1 + u)).subs(c, b*(1 + u + v))))
    k1 = -(200*q**2*u**6 + 600*q**2*u**5*v + 80*q**2*u**5 + 600*q**2*u**4*v**2 + 200*q**2*u**4*v - 1088*q**2*u**4 + 200*q**2*u**3*v**3 + 160*q**2*u**3*v**2 - 2176*q**2*u**3*v - 1616*q**2*u**3 + 40*q**2*u**2*v**3 - 1216*q**2*u**2*v**2 - 2424*q**2*u**2*v - 648*q**2*u**2 - 128*q**2*u*v**3 - 744*q**2*u*v**2 - 648*q**2*u*v + 32*q**2*v**3 + 320*q*u**5 + 800*q*u**4*v + 1356*q*u**4 + 640*q*u**3*v**2 + 2712*q*u**3*v + 1792*q*u**3 + 160*q*u**2*v**3 + 1542*q*u**2*v**2 + 2688*q*u**2*v + 756*q*u**2 + 186*q*u*v**3 + 1128*q*u*v**2 + 756*q*u*v + 116*q*v**3 + 270*q*v**2 - 68*u**4 - 136*u**3*v - 176*u**3 - 176*u**2*v**2 - 264*u**2*v - 108*u**2 - 108*u*v**3 - 384*u*v**2 - 108*u*v - 25*v**4 - 148*v**3 - 270*v**2)
    k2 = 32*q**2*u**6 + 128*q**2*u**5*v + 96*q**2*u**5 + 192*q**2*u**4*v**2 + 808*q**2*u**4*v + 96*q**2*u**4 + 128*q**2*u**3*v**3 + 1456*q**2*u**3*v**2 + 1880*q**2*u**3*v + 32*q**2*u**3 + 32*q**2*u**2*v**4 + 872*q**2*u**2*v**3 + 3376*q**2*u**2*v**2 + 1848*q**2*u**2*v + 128*q**2*u*v**4 + 1720*q**2*u*v**3 + 2760*q**2*u*v**2 + 648*q**2*u*v + 128*q**2*v**4 + 976*q**2*v**3 + 648*q**2*v**2 - 154*q*u**6 - 546*q*u**5*v - 732*q*u**5 - 734*q*u**4*v**2 - 2556*q*u**4*v - 1272*q*u**4 - 466*q*u**3*v**3 - 3452*q*u**3*v**2 - 4230*q*u**3*v - 964*q*u**3 - 144*q*u**2*v**4 - 2204*q*u**2*v**3 - 5322*q*u**2*v**2 - 2976*q*u**2*v - 270*q*u**2 - 20*q*u*v**5 - 616*q*u*v**4 - 2880*q*u*v**3 - 3360*q*u*v**2 - 756*q*u*v - 40*q*v**5 - 516*q*v**4 - 1232*q*v**3 - 756*q*v**2 + 147*u**6 + 518*u**5*v + 686*u**5 + 717*u**4*v**2 + 1898*u**4*v + 1201*u**4 + 488*u**3*v**3 + 1996*u**3*v**2 + 2400*u**3*v + 932*u**3 + 162*u**2*v**4 + 1032*u**2*v**3 + 1796*u**2*v**2 + 1128*u**2*v + 270*u**2 + 20*u*v**5 + 288*u*v**4 + 760*u*v**3 + 600*u*v**2 + 108*u*v + 40*v**5 + 188*v**4 + 256*v**3 + 108*v**2
    k3 = 32*q**2*u**6 + 64*q**2*u**5*v + 96*q**2*u**5 + 32*q**2*u**4*v**2 - 328*q**2*u**4*v + 96*q**2*u**4 - 816*q**2*u**3*v**2 - 1496*q**2*u**3*v + 32*q**2*u**3 - 392*q**2*u**2*v**3 - 1688*q**2*u**2*v**2 - 1752*q**2*u**2*v - 224*q**2*u*v**3 - 840*q**2*u*v**2 - 648*q**2*u*v - 32*q**2*v**3 - 154*q*u**6 - 378*q*u**5*v - 732*q*u**5 - 314*q*u**4*v**2 - 1104*q*u**4*v - 1272*q*u**4 - 90*q*u**3*v**3 - 548*q*u**3*v**2 - 858*q*u**3*v - 964*q*u**3 - 136*q*u**2*v**3 - 264*q*u**2*v**2 + 84*q*u**2*v - 270*q*u**2 - 162*q*u*v**3 - 300*q*u*v**2 + 216*q*u*v - 116*q*v**3 - 270*q*v**2 + 147*u**6 + 364*u**5*v + 686*u**5 + 332*u**4*v**2 + 1532*u**4*v + 1201*u**4 + 140*u**3*v**3 + 1264*u**3*v**2 + 2404*u**3*v + 932*u**3 + 25*u**2*v**4 + 428*u**2*v**3 + 1802*u**2*v**2 + 1668*u**2*v + 270*u**2 + 50*u*v**4 + 436*u*v**3 + 1140*u*v**2 + 432*u*v + 25*v**4 + 148*v**3 + 270*v**2
    for coeff in Poly(k1, (u, v)).coeffs() + Poly(k2, (u, v)).coeffs() + Poly(k3, (u, v)).coeffs():
        print('   ', coeff, '>= 0')
    # every coeff should be non-negative, so q = 0
    q0 = 0
    print('q =', q0)
    p0 = p0.subs(q, q0)
    print('p =', p0)
    print()
    print('g =', factor(g.subs(m, m0).subs(p, p0).subs(q, q0)))
    print('h =', factor(h.subs(m, m0).subs(p, p0).subs(q, q0)))
    f = f.subs(q, q0)
    print('f(abc) =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    print('f(cba) =', factor(f.subs(b, c*(1 + u)).subs(a, c*(1 + u + v))))
    print('f(bac) =', factor(f.subs(a, b*(1 + u)).subs(c, b*(1 + u + v))))

if __name__ == '__main__':
    main()