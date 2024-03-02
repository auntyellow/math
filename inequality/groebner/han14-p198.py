from sympy import *

# ISBN 9787560349800, p198, ex 7.30

def main():
    a, b, c, d = symbols('a, b, c, d', negative = False)
    f = (a + b + c + d)**6 - 1728*(a - b)*(a - c)*(a - d)*(b - c)*(b - d)*(c - d)
    # assume a >= b >= c >= d

    # 1. d > 0
    u, v, w = symbols('u, v, w', negative = False)
    print('f =', factor(f.subs(a, d*(1 + u + v + w)).subs(b, d*(1 + u + v)).subs(c, d*(1 + u))))
    g = 729*u**6 + 2916*u**5*v + 1458*u**5*w + 5832*u**5 + 4860*u**4*v**2 + 4860*u**4*v*w + 19440*u**4*v + 1215*u**4*w**2 + 9720*u**4*w + 19440*u**4 + 4320*u**3*v**3 + 4752*u**3*v**2*w + 25920*u**3*v**2 + 1512*u**3*v*w**2 + 25920*u**3*v*w + 51840*u**3*v + 540*u**3*w**3 + 6480*u**3*w**2 + 25920*u**3*w + 34560*u**3 + 2160*u**2*v**4 + 864*u**2*v**3*w + 17280*u**2*v**3 - 1944*u**2*v**2*w**2 + 25920*u**2*v**2*w + 51840*u**2*v**2 - 648*u**2*v*w**3 + 12960*u**2*v*w**2 + 51840*u**2*v*w + 69120*u**2*v + 135*u**2*w**4 + 2160*u**2*w**3 + 12960*u**2*w**2 + 34560*u**2*w + 34560*u**2 + 576*u*v**5 - 288*u*v**4*w + 5760*u*v**4 - 2016*u*v**3*w**2 + 11520*u*v**3*w + 23040*u*v**3 - 1008*u*v**2*w**3 + 8640*u*v**2*w**2 + 34560*u*v**2*w + 46080*u*v**2 + 180*u*v*w**4 + 2880*u*v*w**3 + 17280*u*v*w**2 + 46080*u*v*w + 46080*u*v + 18*u*w**5 + 360*u*w**4 + 2880*u*w**3 + 11520*u*w**2 + 23040*u*w + 18432*u + 64*v**6 + 192*v**5*w + 768*v**5 + 240*v**4*w**2 + 1920*v**4*w + 3840*v**4 + 160*v**3*w**3 + 1920*v**3*w**2 + 7680*v**3*w + 10240*v**3 + 60*v**2*w**4 + 960*v**2*w**3 + 5760*v**2*w**2 + 15360*v**2*w + 15360*v**2 + 12*v*w**5 + 240*v*w**4 + 1920*v*w**3 + 7680*v*w**2 + 15360*v*w + 12288*v + w**6 + 24*w**5 + 240*w**4 + 1280*w**3 + 3840*w**2 + 6144*w + 4096
    assert g.func == Add
    g1, g2 = 0, 0
    for term in g.args:
        if Poly(term, (u, v, w)).total_degree() == 6:
            g1 += term
        else:
            g2 += term
    print('g1 =', g1)
    print('g2 =', g2) # g2 > 0
    g1 = 729*u**6 + 2916*u**5*v + 1458*u**5*w + 4860*u**4*v**2 + 4860*u**4*v*w + 1215*u**4*w**2 + 4320*u**3*v**3 + 4752*u**3*v**2*w + 1512*u**3*v*w**2 + 540*u**3*w**3 + 2160*u**2*v**4 + 864*u**2*v**3*w - 1944*u**2*v**2*w**2 - 648*u**2*v*w**3 + 135*u**2*w**4 + 576*u*v**5 - 288*u*v**4*w - 2016*u*v**3*w**2 - 1008*u*v**2*w**3 + 180*u*v*w**4 + 18*u*w**5 + 64*v**6 + 192*v**5*w + 240*v**4*w**2 + 160*v**3*w**3 + 60*v**2*w**4 + 12*v*w**5 + w**6
    s, t = symbols('s, t', negative = False)
    # g1 = 0 when s = 1.53208413 and t = 2.22668231, i.e. v = 2.53208413 and w = 4.75876644, unable to convert to exact number
    print('g1(uvw) =', factor(g1.subs(v, u*(1 + s)).subs(w, u*(1 + s + t))))
    # proved by polynomial-prover
    print('g1(uwv) =', factor(g1.subs(w, u*(1 + s)).subs(v, u*(1 + s + t))))
    # proved by polynomial-prover
    print('g1(vuw) =', factor(g1.subs(u, v*(1 + s)).subs(w, v*(1 + s + t))))
    # positive
    print('g1(vwu) =', factor(g1.subs(w, v*(1 + s)).subs(u, v*(1 + s + t))))
    # positive
    print('g1(wuv) =', factor(g1.subs(u, w*(1 + s)).subs(v, w*(1 + s + t))))
    # positive
    print('g1(wvu) =', factor(g1.subs(v, w*(1 + s)).subs(u, w*(1 + s + t))))

    # 2. d = 0
    # f = 0 when u = 2.53209057 and v = 4.7587785, unable to convert to exact number
    print('f(d=0) =', factor(f.subs(d, 0).subs(a, c*(1 + u + v)).subs(b, c*(1 + u))))
    # equivalent to g1(uvw)
    h = 64*u**6 + 192*u**5*v + 576*u**5 + 240*u**4*v**2 - 288*u**4*v + 2160*u**4 + 160*u**3*v**3 - 2016*u**3*v**2 + 864*u**3*v + 4320*u**3 + 60*u**2*v**4 - 1008*u**2*v**3 - 1944*u**2*v**2 + 4752*u**2*v + 4860*u**2 + 12*u*v**5 + 180*u*v**4 - 648*u*v**3 + 1512*u*v**2 + 4860*u*v + 2916*u + v**6 + 18*v**5 + 135*v**4 + 540*v**3 + 1215*v**2 + 1458*v + 729
    print('h =', h)
    # (a + b + c)**6 >= 1728*(a - b)*(a - c)*(b - c)*a*b*c
    # equality occurs when a = 2 + 2*cos(pi/9), b = 2 - 2*cos(4*pi/9) and c = 2 - 2*cos(2*pi/9)
    # see https://math.stackexchange.com/a/3353472
    h_u, h_v = diff(h, u), diff(h, v)
    print('h_u =', h_u)
    print('h_v =', h_v)
    B = groebner([h_u, h_v], u, v)
    print(B)
    print(factor(B[1]), '= 0')
    v01 = nsolve(B[1], (15, 100), solver='bisect', verify=False)
    v02 = nsolve(B[1], (4, 15), solver='bisect', verify=False)
    v03 = nsolve(B[1], (2, 4), solver='bisect', verify=False)
    v04 = nsolve(B[1], (1, 2), solver='bisect', verify=False)
    v05 = nsolve(B[1], (.2, 1), solver='bisect', verify=False)
    v06 = nsolve(B[1], (0, .2), solver='bisect', verify=False)
    v0n = [v01, v02, v03, v04, v05, v06]
    print('v =', v0n)
    for v0 in v0n:
        p = Poly(B[0].subs(v, v0), u)
        print(p.expr, '= 0')
        u0 = -N(p.nth(0)/p.nth(1))
        if u0 >= 0:
            print('u0 =', u0)
            print('v0 =', v0)
            # v01 and v03 are saddle points; v02 is minimum (largest root of v**3 - 3*v**2 - 9*v + 3 = 0)
            print('h0 =', N(h.subs(u, u0).subs(v, v0)))
    print()

    # prove h(v0, u0) = 0:
    h1 = v**3 - 3*v**2 - 9*v + 3
    print('h1 =', h1)
    h2 = rem(B[0], h1, v)
    print('h2 =', h2)
    R = rem(h, h2, u)
    print('R =', R)
    R = rem(R, h1)
    print('R =', R)
    print()

    # another way to prove g1(v0, u0) = 0:
    res = resultant(h, h1, v)
    print('res =', factor(res), '= 0')
    # disc = 0 means h(u0) = h_u(u0) = 0
    print('disc =', discriminant(res))

if __name__ == '__main__':
    main()