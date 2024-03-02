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
    h = (n + 2*m)*(a + b + c)
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    f = f0**2 - (g/h)**2
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
    # graph of g/h(b=c)
    print('y =', factor((g/h).subs(m, m0).subs(a, x).subs(b, (3 - x)/2).subs(c, (3 - x)/2)))
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
    f = f0**2 - (g/h)**2
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
    f = f0**2 - (g/h)**2
    U, V = 100, S(100)/99
    # a <= b <= V*a, c <= b/U
    print('f(cUabV) =', factor(f.subs(c, b/(U + u)).subs(b, a*(V + v)/(1 + v))))
    # c <= b <= V*c, a <= b/U
    print('f(aUcbV) =', factor(f.subs(a, b/(U + u)).subs(b, c*(V + v)/(1 + v))))
    # b <= a <= V*b, c <= a/U
    print('f(cUbaV) =', factor(f.subs(c, a/(U + u)).subs(a, b*(V + v)/(1 + v))))
    k1 = 1440894015*m**2*u**3*v**4 + 5777160246*m**2*u**3*v**3 + 8686146051*m**2*u**3*v**2 + 5804387424*m**2*u**3*v + 1454507604*m**2*u**3 + 432844562106*m**2*u**2*v**4 + 1735441860636*m**2*u**2*v**3 + 2609266618530*m**2*u**2*v**2 + 1743585900408*m**2*u**2*v + 436916580400*m**2*u**2 + 43340843196387*m**2*u*v**4 + 173768513370606*m**2*u*v**3 + 261261279783603*m**2*u*v**2 + 174580391601000*m**2*u*v + 43746781990000*m**2*u + 1446531945101892*m**2*v**4 + 5799589871743800*m**2*v**3 + 8719603139580300*m**2*v**2 + 5826564412020000*m**2*v + 1460019199000000*m**2 + 1344834414*m*u**3*v**4 + 5392921842*m*u**3*v**3 + 8109798246*m*u**3*v**2 + 5420168622*m*u**3*v + 1358457804*m*u**3 + 403258204998*m*u**2*v**4 + 1617082848018*m*u**2*v**3 + 2431710683226*m*u**2*v**2 + 1625205640806*m*u**2*v + 407319600600*m*u**2 + 40305455864388*m*u*v**4 + 161624264670792*m*u*v**3 + 243041156106804*m*u*v**2 + 162431341340400*m*u*v + 40708994040000*m*u + 1342797950458800*m*v**4 + 5384519828899200*m*v**3 + 8096807024420400*m*v**2 + 5411246347980000*m*v + 1356161202000000*m + 288178803*u**3*v**4 + 1156596408*u**3*v**3 + 1740726207*u**3*v**2 + 1164378402*u**3*v + 292069800*u**3 + 86069402496*u**2*v**4 + 345432265794*u**2*v**3 + 519883263900*u**2*v**2 + 347747340402*u**2*v + 87226939800*u**2 + 8568612468801*u*v**4 + 34388947097802*u*v**3 + 51755448759201*u*v**2 + 34618506100200*u*v + 8683391970000*u + 284346024920100*v**4 + 1141168459840200*v**3 + 1717438443920100*v**2 + 1148755608000000*v + 288139599000000
    k2 = -(31049568*m**2*u**4*v**3 + 93462336*m**2*u**4*v**2 + 93776760*m**2*u**4*v + 31363992*m**2*u**4 + 12419827200*m**2*u**3*v**3 + 37384934400*m**2*u**3*v**2 + 37510704000*m**2*u**3*v + 12545596800*m**2*u**3 + 1862962436412*m**2*u**2*v**3 + 5607704994012*m**2*u**2*v**2 + 5626570197303*m**2*u**2*v + 1881827639700*m**2*u**2 + 124195927757616*m**2*u*v**3 + 373842263836008*m**2*u*v**2 + 375099912099000*m**2*u*v + 125453576020000*m**2*u + 3104838807760404*m**2*v**3 + 9345877231719600*m**2*v**2 + 9377317224990000*m**2*v + 3136278801000000*m**2 + 31049568*m*u**3*v**3 + 93619152*m*u**3*v**2 + 94091184*m*u**3*v + 31521600*m*u**3 + 9299345616*m*u**2*v**3 + 28038857616*m*u**2*v**2 + 28180151604*m*u**2*v + 9440639600*m*u**2 + 928370439612*m*u*v**3 + 2799161738406*m*u*v**2 + 2813259279600*m*u*v + 942467980000*m*u + 30893151920004*m*v**3 + 93146737919400*m*v**2 + 93615584040000*m*v + 31361998000000*m + 3881196*u**2*v**3 + 11721996*u**2*v**2 + 11800701*u**2*v + 3959900*u**2 + 772358004*u*v**3 + 2332657602*u*v**2 + 2348299800*u*v + 788000000*u + 38423840400*v**3 + 116045800200*v**2 + 116822970000*v + 39201000000)
    k3 = 14554485*m**2*u**3*v**3 + 43967286*m**2*u**3*v**2 + 44273097*m**2*u**3*v + 14860300*m**2*u**3 + 4372167294*m**2*u**2*v**3 + 13208004018*m**2*u**2*v**2 + 13300103124*m**2*u**2*v + 4464267608*m**2*u**2 + 437786294913*m**2*u*v**3 + 1322544313332*m**2*u*v**2 + 1331789736816*m**2*u*v + 447031840000*m**2*u + 14611433788908*m**2*v**3 + 44141653709208*m**2*v**2 + 44451015840000*m**2*v + 14920800000000*m**2 + 13584186*m*u**3*v**3 + 41026986*m*u**3*v**2 + 41303196*m*u**3*v + 13860400*m*u**3 + 4073315202*m*u**2*v**3 + 12302450424*m*u**2*v**2 + 12385492416*m*u**2*v + 4156358400*m*u**2 + 407125816812*m*u*v**3 + 1229645378016*m*u*v**2 + 1237967280000*m*u*v + 415447840000*m*u + 13563615661200*m*v**3 + 40967019561600*m*v**2 + 41244999840000*m*v + 13841600000000*m + 2910897*u**3*v**3 + 8781696*u**3*v**2 + 8830899*u**3*v + 2960100*u**3 + 869387904*u**2*v**3 + 2622806406*u**2*v**2 + 2637508500*u**2*v + 884090000*u**2 + 86551641099*u*v**3 + 261113341500*u*v**2 + 262577700000*u*v + 88016000000*u + 2872182069900*v**3 + 8664966090000*v**2 + 8713584000000*v + 2920800000000
    # search possible m
    print()
    print('```python')
    print('    coeffs = [')
    for coeff in Poly(k1, u, v).coeffs() + Poly(k2, u, v).coeffs() + Poly(k3, u, v).coeffs():
        print('        ' + str(coeff) + ',')
    print('    ]')
    print('```')
    # unable to cover area near (0, 1, 1)
    print()

    # try quadratic homogeneous polynomial
    p, q = symbols('p, q')
    n = 1
    g = n*a**2 + m*(b**2 + c**2) + p*(a*b + a*c) + q*b*c
    h = (n + 2*m)*(a**2 + b**2 + c**2) + (2*p + q)*(a*b + a*c + b*c)
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    f = f0**2 - (g/h)**2
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
    p1 = Poly(k1, (u, v))
    print('p1(u,v) =', p1)
    for coeff in p1.coeffs():
        print('   ', coeff, '>= 0')
    p2 = Poly(k2, (u, v))
    print('p2(u,v) =', p2)
    for coeff in p2.coeffs():
        print('   ', coeff, '>= 0')
    p3 = Poly(k3, (u, v))
    print('p3(u,v) =', p3)
    for coeff in p3.coeffs():
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