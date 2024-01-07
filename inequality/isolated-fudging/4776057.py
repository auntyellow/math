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
    x, y, z = symbols('x, y, z', negative = False)
    f0 = a/sqrt(5 - 4*b*c)
    s5 = sqrt(5)
    # graph of f0(b=c)
    print('y =', factor(f0.subs(a, x).subs(b, (s5 - x)/2).subs(c, (s5 - x)/2)))
    print()

    m, n, p, q = symbols('m, n, p, q')
    n = 1
    g = n*a + m*(b + c)
    h = (n + 2*m)*(a + b + c)/3
    print('sum_cyc(g/h) =', cancel(sum_cyc(g/h, (a, b, c))))
    f = f0**2 - (g/h/3)**2
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
    # graph of g/3h(b=c)
    print('y =', factor((g/h/3).subs(m, m0).subs(a, x).subs(b, (s5 - x)/2).subs(c, (s5 - x)/2)))
    f = f.subs(m, m0)
    x, y, z = symbols('x, y, z', negative = False)
    xyz = (x + y + z)/s5
    a0, b0, c0 = x/xyz, y/xyz, z/xyz
    print('a + b + c =', factor(a0 + b0 + c0))
    f = f.subs(a, a0).subs(b, b0).subs(c, c0)
    u, v = symbols('u, v', negative = False)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    print()

    # prove: sum_cyc(f0) <= 3/s5
    f = f0**2 - (g/h/s5)**2
    # f(s5/3,s5/3,s5/3) = 0
    eq1 = Eq(f.subs(a, s5/3).subs(b, s5/3).subs(c, s5/3), 0)
    # f_a,b(s5/3,s5/3,s5/3) = 0
    eq2 = Eq(diff(f.subs(c, s5 - a - b), a).subs(a, s5/3).subs(b, s5/3), 0)
    eq3 = Eq(diff(f.subs(c, s5 - a - b), b).subs(a, s5/3).subs(b, s5/3), 0)
    print('eq1:', factor(eq1)) # True
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3)) # True
    m0 = solve(eq2, m)
    print('m =', m0)
    m0 = m0[0]
    print('g =', factor(g.subs(m, m0)))
    print('h =', factor(h.subs(m, m0)))
    # graph of g/s5h(b=c)
    print('y =', factor((g/h/s5).subs(m, m0).subs(a, x).subs(b, (s5 - x)/2).subs(c, (s5 - x)/2)))
    f = f.subs(m, m0)
    f = f.subs(a, a0).subs(b, b0).subs(c, c0)
    u, v = symbols('u, v', negative = False)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    # doesn't hold
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    print('f(20,1,1) =', N(f.subs(x, 20).subs(y, 1).subs(z, 1)))
    print()

    # try quadratic homogeneous polynomial
    g = n*a**2 + m*(b**2 + c**2) + p*(a*b + a*c) + q*b*c
    h = (n + 2*m)*(a**2 + b**2 + c**2)/3 + (2*p + q)*(a*b + a*c + b*c)/3
    print('sum_cyc(g/h) =', cancel(sum_cyc(g/h, (a, b, c))))
    f = f0**2 - (g/h/s5)**2
    # f(s5/3,s5/3,s5/3) = 0
    eq1 = Eq(f.subs(a, s5/3).subs(b, s5/3).subs(c, s5/3), 0)
    # f_a,b(s5/3,s5/3,s5/3) = 0
    eq2 = Eq(diff(f.subs(c, s5 - a - b), a).subs(a, s5/3).subs(b, s5/3), 0)
    eq3 = Eq(diff(f.subs(c, s5 - a - b), b).subs(a, s5/3).subs(b, s5/3), 0)
    # assume f(s5,0,0) = 0 ?
    eq4 = Eq(f.subs(a, s5).subs(b, 0).subs(c, 0), 0)
    print('eq1:', factor(eq1)) # True
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3)) # True
    print('eq4:', factor(eq4))
    m0 = solve(eq2, m)
    print('m =', m0)
    m0 = m0[0]
    f = f.subs(m, m0)
    f = f.subs(a, a0).subs(b, b0).subs(c, c0)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    # k1 >= 0, numerator in f(xyz)
    k1 = 144*p**2*u**5 + 36*p**2*u**4*v**2 + 360*p**2*u**4*v - 7772*p**2*u**4 + 72*p**2*u**3*v**3 - 576*p**2*u**3*v**2 - 15544*p**2*u**3*v - 14736*p**2*u**3 + 72*p**2*u**2*v**4 - 1224*p**2*u**2*v**3 - 4080*p**2*u**2*v**2 - 22104*p**2*u**2*v - 6840*p**2*u**2 + 36*p**2*u*v**5 - 900*p**2*u*v**4 + 3692*p**2*u*v**3 + 12528*p**2*u*v**2 - 6840*p**2*u*v + 9*p**2*v**6 - 234*p**2*v**5 + 745*p**2*v**4 + 9948*p**2*v**3 + 13140*p**2*v**2 + 4480*p*q*u**4 + 1152*p*q*u**3*v**2 + 8960*p*q*u**3*v + 19200*p*q*u**3 + 288*p*q*u**2*v**4 + 1728*p*q*u**2*v**3 - 6048*p*q*u**2*v**2 + 28800*p*q*u**2*v + 14400*p*q*u**2 + 288*p*q*u*v**5 - 2880*p*q*u*v**4 - 10528*p*q*u*v**3 - 8640*p*q*u*v**2 + 14400*p*q*u*v + 144*p*q*v**6 - 1728*p*q*v**5 - 7952*p*q*v**4 - 9120*p*q*v**3 - 7200*p*q*v**2 - 2016*p*u**5 - 504*p*u**4*v**2 - 5040*p*u**4*v + 4872*p*u**4 - 1008*p*u**3*v**3 + 9744*p*u**3*v + 7008*p*u**3 - 1008*p*u**2*v**4 + 5040*p*u**2*v**3 + 33888*p*u**2*v**2 + 10512*p*u**2*v + 720*p*u**2 - 504*p*u*v**5 + 4536*p*u*v**4 + 29016*p*u*v**3 + 42336*p*u*v**2 + 720*p*u*v - 126*p*v**6 + 1260*p*v**5 + 9762*p*v**4 + 19416*p*v**3 + 19080*p*v**2 - 1280*q**2*u**4 - 2560*q**2*u**3*v - 3840*q**2*u**2*v**2 + 2304*q**2*u*v**4 - 2560*q**2*u*v**3 + 576*q**2*v**6 + 1152*q**2*v**5 + 1600*q**2*v**4 + 9600*q*u**4 - 8064*q*u**3*v**2 + 19200*q*u**3*v + 19200*q*u**3 - 2016*q*u**2*v**4 - 12096*q*u**2*v**3 - 2208*q*u**2*v**2 + 28800*q*u**2*v + 14400*q*u**2 - 2016*q*u*v**5 - 12096*q*u*v**4 - 11808*q*u*v**3 - 8640*q*u*v**2 + 14400*q*u*v - 1008*q*v**6 - 4032*q*v**5 - 8592*q*v**4 - 9120*q*v**3 - 7200*q*v**2 + 7056*u**5 + 1764*u**4*v**2 + 17640*u**4*v + 19044*u**4 + 3528*u**3*v**3 + 28224*u**3*v**2 + 38088*u**3*v + 21744*u**3 + 3528*u**2*v**4 + 24696*u**2*v**3 + 45648*u**2*v**2 + 32616*u**2*v + 7560*u**2 + 1764*u*v**5 + 12348*u*v**4 + 26604*u*v**3 + 29808*u*v**2 + 7560*u*v + 441*v**6 + 2646*v**5 + 6777*v**4 + 9468*v**3 + 5940*v**2
    # k2 >= 0, numerator in f(zyx)
    k2 = 4180*p**2*u**6 + 9700*p**2*u**5*v + 24440*p**2*u**5 + 5561*p**2*u**4*v**2 + 42822*p**2*u**4*v + 49741*p**2*u**4 - 464*p**2*u**3*v**3 + 9988*p**2*u**3*v**2 + 52904*p**2*u**3*v + 42612*p**2*u**3 + 44*p**2*u**2*v**4 - 11024*p**2*u**2*v**3 - 19632*p**2*u**2*v**2 + 12672*p**2*u**2*v + 13140*p**2*u**2 + 520*p**2*u*v**5 - 1704*p**2*u*v**4 - 28144*p**2*u*v**3 - 32616*p**2*u*v**2 - 6840*p**2*u*v - 20*p**2*v**6 + 1160*p**2*v**5 - 4604*p**2*v**4 - 12624*p**2*v**3 - 6840*p**2*v**2 - 4160*p*q*u**6 + 64*p*q*u**5*v - 15616*p*q*u**5 + 19664*p*q*u**4*v**2 + 17760*p*q*u**4*v - 23792*p*q*u**4 + 28096*p*q*u**3*v**3 + 101920*p*q*u**3*v**2 + 42752*p*q*u**3*v - 19680*p*q*u**3 + 16640*p*q*u**2*v**4 + 116992*p*q*u**2*v**3 + 149472*p*q*u**2*v**2 + 37440*p*q*u**2*v - 7200*p*q*u**2 + 3520*p*q*u*v**5 + 55680*p*q*u*v**4 + 124160*p*q*u*v**3 + 86400*p*q*u*v**2 + 14400*p*q*u*v - 320*p*q*v**6 + 8960*p*q*v**5 + 33280*p*q*v**4 + 38400*p*q*v**3 + 14400*p*q*v**2 + 8040*p*u**6 + 18696*p*u**5*v + 36336*p*u**5 + 13410*p*u**4*v**2 + 61356*p*u**4*v + 65994*p*u**4 - 960*p*u**3*v**3 + 17448*p*u**3*v**2 + 77040*p*u**3*v + 56904*p*u**3 - 5832*p*u**2*v**4 - 30240*p*u**2*v**3 + 2784*p*u**2*v**2 + 36864*p*u**2*v + 19080*p*u**2 - 1392*p*u*v**5 - 27792*p*u*v**4 - 29856*p*u*v**3 - 4752*p*u*v**2 + 720*p*u*v + 600*p*v**6 - 6384*p*v**5 - 11832*p*v**4 - 4128*p*v**3 + 720*p*v**2 + 1024*q**2*u**6 - 2816*q**2*u**5*v + 2048*q**2*u**5 - 9664*q**2*u**4*v**2 - 4224*q**2*u**4*v + 1600*q**2*u**4 - 12800*q**2*u**3*v**3 - 12800*q**2*u**3*v**2 - 2560*q**2*u**3*v - 10240*q**2*u**2*v**4 - 12800*q**2*u**2*v**3 - 3840*q**2*u**2*v**2 - 5120*q**2*u*v**5 - 7680*q**2*u*v**4 - 2560*q**2*u*v**3 - 1280*q**2*v**6 - 2560*q**2*v**5 - 1280*q**2*v**4 - 3648*q*u**6 + 6720*q*u**5*v - 14592*q*u**5 + 41040*q*u**4*v**2 + 23136*q*u**4*v - 24432*q*u**4 + 67776*q*u**3*v**3 + 120864*q*u**3*v**2 + 41472*q*u**3*v - 19680*q*u**3 + 55296*q*u**2*v**4 + 154368*q*u**2*v**3 + 153312*q*u**2*v**2 + 37440*q*u**2*v - 7200*q*u**2 + 24000*q*u*v**5 + 86400*q*u*v**4 + 134400*q*u*v**3 + 86400*q*u*v**2 + 14400*q*u*v + 4800*q*v**6 + 19200*q*v**5 + 38400*q*v**4 + 38400*q*v**3 + 14400*q*v**2 + 1044*u**6 + 36*u**5*v + 6264*u**5 - 4887*u**4*v**2 + 9702*u**4*v + 14013*u**4 - 12528*u**3*v**3 + 6948*u**3*v**2 + 25416*u**3*v + 14292*u**3 - 14580*u**2*v**4 - 5904*u**2*v**3 + 30096*u**2*v**2 + 24192*u**2*v + 5940*u**2 - 8568*u*v**5 - 10728*u*v**4 + 11088*u*v**3 + 27864*u*v**2 + 7560*u*v - 2196*v**6 - 3960*v**5 - 828*v**4 + 8496*v**3 + 7560*v**2
    p1 = Poly(k1, (u, v))
    p2 = Poly(k2, (u, v))
    print('p1(u,v) =', p1)
    print('p2(u,v) =', p2)
    # search possible p and q
    print()
    print('```python')
    print('    non_negative_coeffs = [')
    for coeff in p1.coeffs():
        print('        ' + str(coeff) + ',')
    for coeff in p2.coeffs():
        print('        ' + str(coeff) + ',')
    print('    ]')
    print('```')
    print()
    # result from a3658031a.py
    p0, q0 = S(121)/941, S(201)/388
    print('g =', factor(g.subs(m, m0).subs(p, p0).subs(q, q0)))
    print('h =', factor(h.subs(m, m0).subs(p, p0).subs(q, q0)))
    # graph of g/s5h(b=c)
    print('y =', factor((g/h/s5).subs(m, m0).subs(p, p0).subs(q, q0).subs(a, x).subs(b, (s5 - x)/2).subs(c, (s5 - x)/2)))
    f = f.subs(p, p0).subs(q, q0)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))

if __name__ == '__main__':
    main()