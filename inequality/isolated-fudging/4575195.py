from sympy import *

# https://math.stackexchange.com/q/4575195

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', positive = True)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    x, y, z = symbols('x, y, z', positive = True)
    f0 = sqrt((4*x**2 + y**2)/(3*x**2 + y*z))
    # graph of f0(y=z)
    print('y =', factor(f0.subs(y, (3 - x)/2).subs(z, (3 - x)/2)))
    print()

    m, n, p, q, r, s, t = symbols('m, n, p, q, r, s, t')
    n = 1
    g = n*x + p*y + q*z
    h = (n + p + q)*(x + y + z)/3
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (x, y, z))))
    s5 = sqrt(5)
    f = f0**2 - (s5*g/h/2)**2
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(x, 1).subs(y, 1).subs(z, 1), 0)
    # homogeneous, hence assume x + y + z = 3
    # f_x,y(1,1) = 0
    eq2 = Eq(diff(f.subs(z, 3 - x - y), x).subs(x, 1).subs(y, 1), 0)
    eq3 = Eq(diff(f.subs(z, 3 - x - y), y).subs(x, 1).subs(y, 1), 0)
    print('eq1:', factor(eq1)) # True
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3))
    pq = solve([eq2, eq3], (p, q))
    print('pq =', pq)
    p0, q0 = pq[p], pq[q]
    print('g =', factor(g.subs(p, p0).subs(q, q0)))
    print('h =', factor(h.subs(p, p0).subs(q, q0)))
    # graph of s5g/2h(y=z)
    print('y =', factor((s5*g/h/2).subs(p, p0).subs(q, q0).subs(y, (3 - x)/2).subs(z, (3 - x)/2)))
    f = f.subs(p, p0).subs(q, q0)
    # doesn't work
    print('f(1,2,3) =', f.subs(x, 1).subs(y, 2).subs(z, 3))
    print()

    # try quadratic homogeneous polynomial
    g = n*x**2 + p*y**2 + q*z**2 + r*x*y + s*x*z + t*y*z
    h = (n + p + q)*(x**2 + y**2 + z**2)/3 + (r + s + t)*(x*y + x*z + y*z)/3
    print('sum_cyc(g/h) =', cancel(sum_cyc(g/h, (x, y, z))))
    f = f0**2 - (s5*g/h/2)**2
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(x, 1).subs(y, 1).subs(z, 1), 0)
    # homogeneous, hence assume x + y + z = 3
    # f_x,y(1,1) = 0
    eq2 = Eq(diff(f.subs(z, 3 - x - y), x).subs(x, 1).subs(y, 1), 0)
    eq3 = Eq(diff(f.subs(z, 3 - x - y), y).subs(x, 1).subs(y, 1), 0)
    print('eq1:', factor(eq1)) # True
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3))
    pq = solve([eq2, eq3], (p, q))
    print('pq =', pq)
    p0, q0 = pq[p], pq[q]
    print('g =', factor(g.subs(p, p0).subs(q, q0)))
    print('h =', factor(h.subs(p, p0).subs(q, q0)))
    # graph of s5g/2h(y=z)
    print('y =', factor((s5*g/h/2).subs(p, p0).subs(q, q0).subs(y, (3 - x)/2).subs(z, (3 - x)/2)))
    f = f.subs(p, p0).subs(q, q0)
    u, v = symbols('u, v', positive = True)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    # k1 >= 0
    k1 = 171376*r**2*u**6 - 244768*r**2*u**5*v + 823232*r**2*u**5 - 1406892*r**2*u**4*v**2 - 3017456*r**2*u**4*v + 1748720*r**2*u**4 - 1751248*r**2*u**3*v**3 - 8035224*r**2*u**3*v**2 - 9663680*r**2*u**3*v + 2609760*r**2*u**3 - 932129*r**2*u**2*v**4 - 6166376*r**2*u**2*v**3 - 16795860*r**2*u**2*v**2 - 14191920*r**2*u**2*v + 1586880*r**2*u**2 - 190125*r**2*u*v**5 - 1864258*r**2*u*v**4 - 8690300*r**2*u*v**3 - 15688440*r**2*u*v**2 - 7675200*r**2*u*v - 190125*r**2*v**5 - 1428520*r**2*v**4 - 3900900*r**2*v**3 - 4899600*r**2*v**2 - 423808*r*t*u**6 - 847616*r*t*u**5*v - 2168576*r*t*u**5 - 414864*r*t*u**4*v**2 - 3676672*r*t*u**4*v - 5751680*r*t*u**4 + 1015144*r*t*u**3*v**3 - 427248*r*t*u**3*v**2 - 9191680*r*t*u**3*v - 8586240*r*t*u**3 + 1415732*r*t*u**2*v**4 + 4233608*r*t*u**2*v**3 - 928800*r*t*u**2*v**2 - 11888640*r*t*u**2*v - 4953600*r*t*u**2 + 503100*r*t*u*v**5 + 2831464*r*t*u*v**4 + 6370880*r*t*u*v**3 + 1362240*r*t*u*v**2 - 4953600*r*t*u*v + 503100*r*t*v**5 + 2550760*r*t*v**4 + 2580000*r*t*v**3 + 2476800*r*t*v**2 + 480480*r*u**6 - 2348880*r*u**5*v + 756960*r*u**5 - 6763800*r*u**4*v**2 - 16574160*r*u**4*v + 1036800*r*u**4 - 6976440*r*u**3*v**3 - 30450480*r*u**3*v**2 - 40828800*r*u**3*v + 1109760*r*u**3 - 3541380*r*u**2*v**4 - 22281240*r*u**2*v**3 - 53901600*r*u**2*v**2 - 44755200*r*u**2*v + 1393920*r*u**2 - 760500*r*u*v**5 - 7082760*r*u*v**4 - 26945520*r*u*v**3 - 38976480*r*u*v**2 - 20793600*r*u*v - 760500*r*v**5 - 4778400*r*v**4 - 8998800*r*v**3 - 9691200*r*v**2 + 118336*t**2*u**6 + 236672*t**2*u**5*v + 236672*t**2*u**5 + 355008*t**2*u**4*v**2 + 473344*t**2*u**4*v + 591680*t**2*u**4 + 236672*t**2*u**3*v**3 + 710016*t**2*u**3*v**2 + 1183360*t**2*u**3*v - 214484*t**2*u**2*v**4 + 473344*t**2*u**2*v**3 + 1775040*t**2*u**2*v**2 - 332820*t**2*u*v**5 - 428968*t**2*u*v**4 + 1183360*t**2*u*v**3 - 332820*t**2*v**5 - 739600*t**2*v**4 - 1320960*t*u**6 - 2641920*t*u**5*v - 5283840*t*u**5 - 918480*t*u**4*v**2 - 9246720*t*u**4*v - 13870080*t*u**4 + 2414880*t*u**3*v**3 - 1032000*t*u**3*v**2 - 23116800*t*u**3*v - 17172480*t*u**3 + 2358120*t*u**2*v**4 + 7905120*t*u**2*v**3 - 3632640*t*u**2*v**2 - 23777280*t*u**2*v - 9907200*t*u**2 + 1006200*t*u*v**5 + 4716240*t*u*v**4 + 8008320*t*u*v**3 + 2724480*t*u*v**2 - 9907200*t*u*v + 1006200*t*v**5 + 2734800*t*v**4 + 5160000*t*v**3 + 4953600*t*v**2 - 582480*u**6 - 4103280*u**5*v - 3494880*u**5 - 6480000*u**4*v**2 - 20516400*u**4*v - 7879680*u**4 - 6001200*u**3*v**3 - 25920000*u**3*v**2 - 38269440*u**3*v - 8219520*u**3 - 2880900*u**2*v**4 - 18003600*u**2*v**3 - 33519600*u**2*v**2 - 32742720*u**2*v - 3559680*u**2 - 760500*u*v**5 - 5761800*u*v**4 - 14396400*u*v**3 - 15199200*u*v**2 - 10886400*u*v - 760500*v**5 - 1476000*v**4 - 2394000*v**3 + 216000*v**2
    # k2 <= 0
    k2 = 2237095*r**2*u**6 + 9565542*r**2*u**5*v + 10562615*r**2*u**5 + 14058055*r**2*u**4*v**2 + 37398662*r**2*u**4*v + 19123420*r**2*u**4 + 7865208*r**2*u**3*v**3 + 40946924*r**2*u**3*v**2 + 54768680*r**2*u**3*v + 15697500*r**2*u**3 + 372912*r**2*u**2*v**4 + 13154536*r**2*u**2*v**3 + 39133500*r**2*u**2*v**2 + 34610760*r**2*u**2*v + 4899600*r**2*u**2 - 818176*r**2*u*v**5 - 2446496*r**2*u*v**4 + 1925840*r**2*u*v**3 + 10161360*r**2*u*v**2 + 7675200*r**2*u*v - 73984*r**2*v**6 - 1192448*r**2*v**5 - 3440720*r**2*v**4 - 3737760*r**2*v**3 - 1586880*r**2*v**2 - 1944460*r*t*u**6 - 4492296*r*t*u**5*v - 6765620*r*t*u**5 + 1130900*r*t*u**4*v**2 - 5352296*r*t*u**4*v - 9671560*r*t*u**4 + 9512976*r*t*u**3*v**3 + 23132968*r*t*u**3*v**2 + 5455840*r*t*u**3*v - 7327200*r*t*u**3 + 8371584*r*t*u**2*v**4 + 35789072*r*t*u**2*v**3 + 43653600*r*t*u**2*v**2 + 11269440*r*t*u**2*v - 2476800*r*t*u**2 + 2818048*r*t*u*v**5 + 18284288*r*t*u*v**4 + 36931840*r*t*u*v**3 + 27740160*r*t*u*v**2 + 4953600*r*t*u*v + 374272*r*t*v**6 + 3390464*r*t*v**5 + 9714560*r*t*v**4 + 11228160*r*t*v**3 + 4953600*r*t*v**2 + 4710300*r*u**6 + 23005080*r*u**5*v + 20564700*r*u**5 + 37995060*r*u**4*v**2 + 84911640*r*u**4*v + 35929200*r*u**4 + 28688880*r*u**3*v**3 + 104534040*r*u**3*v**2 + 124075680*r*u**3*v + 29766000*r*u**3 + 8850840*r*u**2*v**4 + 48439920*r*u**2*v**3 + 102013440*r*u**2*v**2 + 82962720*r*u**2*v + 9691200*r*u**2 - 921120*r*u*v**5 + 1850160*r*u*v**4 + 17927040*r*u*v**3 + 32843520*r*u*v**2 + 20793600*r*u*v - 1044480*r*v**6 - 3563040*r*v**5 - 6071040*r*v**4 - 4465920*r*v**3 - 1393920*r*v**2 + 406780*t**2*u**6 - 133128*t**2*u**5*v + 1146380*t**2*u**5 - 3143300*t**2*u**4*v**2 - 1316488*t**2*u**4*v + 739600*t**2*u**4 - 4970112*t**2*u**3*v**3 - 5443456*t**2*u**3*v**2 - 1183360*t**2*u**3*v - 3905088*t**2*u**2*v**4 - 5206784*t**2*u**2*v**3 - 1775040*t**2*u**2*v**2 - 1893376*t**2*u*v**5 - 3076736*t**2*u*v**4 - 1183360*t**2*u*v**3 - 473344*t**2*v**6 - 946688*t**2*v**5 - 591680*t**2*v**4 - 1522200*t*u**6 - 464400*t*u**5*v - 8797800*t*u**5 + 14835000*t*u**4*v**2 + 2549040*t*u**4*v - 16976400*t*u**4 + 30918720*t*u**3*v**3 + 58720800*t*u**3*v**2 + 15645120*t*u**3*v - 14654400*t*u**3 + 28369680*t*u**2*v**4 + 84417600*t*u**2*v**3 + 89082240*t*u**2*v**2 + 22538880*t*u**2*v - 4953600*t*u**2 + 13209600*t*u*v**5 + 48875520*t*u*v**4 + 78597120*t*u*v**3 + 55480320*t*u*v**2 + 9907200*t*u*v + 2641920*t*v**6 + 10567680*t*v**5 + 21795840*t*v**4 + 22456320*t*v**3 + 9907200*t*v**2 - 1894500*u**6 - 772200*u**5*v - 5854500*u**5 + 3190860*u**4*v**2 + 6975000*u**4*v - 7002000*u**4 + 6036480*u**3*v**3 + 23506560*u**3*v**2 + 24343200*u**3*v - 3258000*u**3 + 4583520*u**2*v**4 + 23434560*u**2*v**3 + 40392720*u**2*v**2 + 27482400*u**2*v - 216000*u**2 + 1844640*u*v**5 + 10498320*u*v**4 + 23417280*u*v**3 + 25041600*u*v**2 + 10886400*u*v + 307440*v**6 + 1844640*v**5 + 4579200*v**4 + 6019200*v**3 + 3559680*v**2
    p1 = Poly(k1, (u, v))
    p2 = Poly(k2, (u, v))
    print('p1(u,v) =', p1)
    print('p2(u,v) =', p2)
    # search possible s and t
    print()
    print('```python')
    print('    non_negative_coeffs = [ \\')
    for coeff in p1.coeffs():
        print('        ' + str(coeff) + ', \\')
    print('    ]')
    print('    non_positive_coeffs = [ \\')
    for coeff in p2.coeffs():
        print('        ' + str(coeff) + ', \\')
    print('    ]')
    print('```')
    print()
    r0, s0, t0 = 0, 0, 0
    # graph of s5g/2h(x=y)
    print('y =', factor((s5*g/h/2).subs(p, p0).subs(q, q0).subs(r, r0).subs(s, s0).subs(t, t0).subs(y, (3 - x)/2).subs(z, (3 - x)/2)))
    g = g.subs(p, p0).subs(q, q0).subs(r, r0).subs(s, s0).subs(t, t0)
    h = h.subs(p, p0).subs(q, q0).subs(r, r0).subs(s, s0).subs(t, t0)
    print('g =', factor(g))
    print('h =', factor(h))
    f = f.subs(r, r0).subs(s, s0).subs(t, t0)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))

if __name__ == '__main__':
    main()