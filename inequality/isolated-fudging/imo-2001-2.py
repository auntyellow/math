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
    x, y, z = symbols('x, y, z', negative = False)
    f0 = a/sqrt(a**2 + 8*b*c)
    # graph of f0(b=c)
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
    # graph of g/3h(b=c)
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
    # graph of g/3h(b=c)
    print('y =', factor((g/h/3).subs(m, mpq0[0]).subs(p, mpq0[1]).subs(q, mpq0[2]).subs(a, x).subs(b, (3 - x)/2).subs(c, (3 - x)/2)))
    f = f.subs(m, mpq0[0]).subs(p, mpq0[1]).subs(q, mpq0[2])
    u, v = symbols('u, v', negative = False)
    print('f(abc) =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    print('f(cba) =', factor(f.subs(b, c*(1 + u)).subs(a, c*(1 + u + v))))
    print()

    # search possible p and q without assuming f(1,1,0) = f(0,0,1) = 0
    m0 = solve(eq2, m)
    print('m =', m0)
    f = f.subs(m, m0[0])
    # a <= b <= c
    print('f(abc) =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    # c <= b <= a
    print('f(cba) =', factor(f.subs(b, c*(1 + u)).subs(a, c*(1 + u + v))))
    # k1 <= 0
    k1 = 800*p**2*u**6 + 2400*p**2*u**5*v + 320*p**2*u**5 + 3200*p**2*u**4*v**2 + 800*p**2*u**4*v - 4092*p**2*u**4 + 2400*p**2*u**3*v**3 + 1600*p**2*u**3*v**2 - 8184*p**2*u**3*v - 5024*p**2*u**3 + 1000*p**2*u**2*v**4 + 1600*p**2*u**2*v**3 - 6264*p**2*u**2*v**2 - 7536*p**2*u**2*v - 1512*p**2*u**2 + 200*p**2*u*v**5 + 880*p**2*u*v**4 - 2172*p**2*u*v**3 - 4416*p**2*u*v**2 - 1512*p**2*u*v + 200*p**2*v**5 - 195*p**2*v**4 - 952*p**2*v**3 - 540*p**2*v**2 + 1120*p*q*u**4*v**2 + 224*p*q*u**4 + 2240*p*q*u**3*v**3 + 1344*p*q*u**3*v**2 + 448*p*q*u**3*v + 2016*p*q*u**3 + 1680*p*q*u**2*v**4 + 2016*p*q*u**2*v**3 - 2380*p*q*u**2*v**2 + 3024*p*q*u**2*v + 1512*p*q*u**2 + 560*p*q*u*v**5 + 1792*p*q*u*v**4 - 2604*p*q*u*v**3 - 2016*p*q*u*v**2 + 1512*p*q*u*v + 560*p*q*v**5 - 98*p*q*v**4 - 1512*p*q*v**3 - 756*p*q*v**2 - 640*p*u**6 - 1920*p*u**5*v - 2048*p*u**5 - 2560*p*u**4*v**2 - 5120*p*u**4*v - 3536*p*u**4 - 1920*p*u**3*v**3 - 5760*p*u**3*v**2 - 7072*p*u**3*v - 4000*p*u**3 - 800*p*u**2*v**4 - 3520*p*u**2*v**3 - 5584*p*u**2*v**2 - 6000*p*u**2*v - 1512*p*u**2 - 160*p*u*v**5 - 1152*p*u*v**4 - 2048*p*u*v**3 - 4800*p*u*v**2 - 1512*p*u*v - 160*p*v**5 - 12*p*v**4 - 1400*p*v**3 - 1836*p*v**2 - 196*q**2*u**4 - 392*q**2*u**3*v + 392*q**2*u**2*v**4 - 588*q**2*u**2*v**2 + 392*q**2*u*v**5 + 784*q**2*u*v**4 - 392*q**2*u*v**3 + 392*q**2*v**5 + 245*q**2*v**4 - 448*q*u**4*v**2 + 1008*q*u**4 - 896*q*u**3*v**3 - 1792*q*u**3*v**2 + 2016*q*u**3*v + 2016*q*u**3 - 672*q*u**2*v**4 - 2688*q*u**2*v**3 - 1792*q*u**2*v**2 + 3024*q*u**2*v + 1512*q*u**2 - 224*q*u*v**5 - 1344*q*u*v**4 - 2800*q*u*v**3 - 2016*q*u*v**2 + 1512*q*u*v - 224*q*v**5 - 196*q*v**4 - 1512*q*v**3 - 756*q*v**2 + 128*u**6 + 384*u**5*v + 768*u**5 + 512*u**4*v**2 + 1920*u**4*v + 1536*u**4 + 384*u**3*v**3 + 2048*u**3*v**2 + 3072*u**3*v + 1024*u**3 + 160*u**2*v**4 + 1152*u**2*v**3 + 1856*u**2*v**2 + 1536*u**2*v + 32*u*v**5 + 320*u*v**4 + 320*u*v**3 - 384*u*v**2 + 32*v**5 - 160*v**4 - 448*v**3 - 1296*v**2
    # k2 <= 0
    k2 = 17*p**2*u**6 + 158*p**2*u**5*v + 106*p**2*u**5 + 557*p**2*u**4*v**2 + 818*p**2*u**4*v - 579*p**2*u**4 + 868*p**2*u**3*v**3 + 2816*p**2*u**3*v**2 - 1620*p**2*u**3*v - 1208*p**2*u**3 + 512*p**2*u**2*v**4 + 4592*p**2*u**2*v**3 - 864*p**2*u**2*v**2 - 3792*p**2*u**2*v - 540*p**2*u**2 - 40*p**2*u*v**5 + 3208*p**2*u*v**4 + 2280*p**2*u*v**3 - 4560*p**2*u*v**2 - 1512*p**2*u*v - 100*p**2*v**6 + 520*p**2*v**5 + 1908*p**2*v**4 - 1024*p**2*v**3 - 1512*p**2*v**2 + 98*p*q*u**6 + 448*p*q*u**5*v + 756*p*q*u**5 + 770*p*q*u**4*v**2 + 4900*p*q*u**4*v - 98*p*q*u**4 + 532*p*q*u**3*v**3 + 10696*p*q*u**3*v**2 + 7980*p*q*u**3*v - 1512*p*q*u**3 - 224*p*q*u**2*v**4 + 9912*p*q*u**2*v**3 + 17276*p*q*u**2*v**2 + 5040*p*q*u**2*v - 756*p*q*u**2 - 616*p*q*u*v**5 + 4368*p*q*u*v**4 + 12544*p*q*u*v**3 + 9072*p*q*u*v**2 + 1512*p*q*u*v - 280*p*q*v**6 + 448*p*q*v**5 + 3248*p*q*v**4 + 4032*p*q*v**3 + 1512*p*q*v**2 - 288*p*u**6 - 776*p*u**5*v - 3008*p*u**5 + 204*p*u**4*v**2 - 8248*p*u**4*v - 6828*p*u**4 + 2408*p*u**3*v**3 - 6968*p*u**3*v**2 - 14552*p*u**3*v - 5944*p*u**3 + 2900*p*u**2*v**4 - 784*p*u**2*v**3 - 11416*p*u**2*v**2 - 8592*p*u**2*v - 1836*p*u**2 + 1544*p*u*v**5 + 1712*p*u*v**4 - 4288*p*u*v**3 - 6096*p*u*v**2 - 1512*p*u*v + 360*p*v**6 + 928*p*v**5 - 608*p*v**4 - 2048*p*v**3 - 1512*p*v**2 - 147*q**2*u**6 - 686*q**2*u**5*v + 98*q**2*u**5 - 1519*q**2*u**4*v**2 - 1078*q**2*u**4*v + 245*q**2*u**4 - 1960*q**2*u**3*v**3 - 1960*q**2*u**3*v**2 - 392*q**2*u**3*v - 1568*q**2*u**2*v**4 - 1960*q**2*u**2*v**3 - 588*q**2*u**2*v**2 - 784*q**2*u*v**5 - 1176*q**2*u*v**4 - 392*q**2*u*v**3 - 196*q**2*v**6 - 392*q**2*v**5 - 196*q**2*v**4 + 784*q*u**6 + 3192*q*u**5*v + 1344*q*u**5 + 6356*q*u**4*v**2 + 7448*q*u**4*v - 196*q*u**4 + 7784*q*u**3*v**3 + 16184*q*u**3*v**2 + 7784*q*u**3*v - 1512*q*u**3 + 5852*q*u**2*v**4 + 17360*q*u**2*v**3 + 17864*q*u**2*v**2 + 5040*q*u**2*v - 756*q*u**2 + 2520*q*u*v**5 + 9072*q*u*v**4 + 14112*q*u*v**3 + 9072*q*u*v**2 + 1512*q*u*v + 504*q*v**6 + 2016*q*v**5 + 4032*q*v**4 + 4032*q*v**3 + 1512*q*v**2 - 1040*u**6 - 3776*u**5*v - 4192*u**5 - 5792*u**4*v**2 - 11712*u**4*v - 6592*u**4 - 4928*u**3*v**3 - 13312*u**3*v**2 - 12736*u**3*v - 4736*u**3 - 2512*u**2*v**4 - 8512*u**2*v**3 - 9376*u**2*v**2 - 4800*u**2*v - 1296*u**2 - 768*u*v**5 - 3456*u*v**4 - 4608*u*v**3 - 1536*u*v**2 - 128*v**6 - 768*v**5 - 1536*v**4 - 1024*v**3
    p1 = Poly(k1, (u, v))
    p2 = Poly(k2, (u, v))
    print('p1(u,v) =', p1)
    print('p2(u,v) =', p2)
    print()
    print('```python')
    print('    non_positive_coeffs = [')
    for coeff in p1.coeffs():
        print('        ' + str(coeff) + ',')
    for coeff in p2.coeffs():
        print('        ' + str(coeff) + ',')
    print('    ]')
    print('```')
    print()
    # result from imo-2001-2a.py
    p0, q0 = S(2)/5, 0
    print('g =', factor(g.subs(m, m0[0]).subs(p, p0).subs(q, q0)))
    print('h =', factor(h.subs(m, m0[0]).subs(p, p0).subs(q, q0)))
    f = f.subs(p, p0).subs(q, q0)
    print('f(abc) =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    print('f(cba) =', factor(f.subs(b, c*(1 + u)).subs(a, c*(1 + u + v))))

if __name__ == '__main__':
    main()