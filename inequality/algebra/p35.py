from sympy import *

# ISBN 9787542848482, p35, §2.1, ex2
# x + y + z = x*y*z => 1/sqrt(1 + x**2) + 1/sqrt(1 + y**2) + 1/sqrt(1 + z**2) <= Integer(3)/2

def main():
    x, y = symbols('x, y', positive = True)
    # x + y + z = x*y*z, x*y > 1
    z = (x + y)/(x*y - 1)
    print('x + y + z - x*y*z =', factor(x + y + z - x*y*z))
    # f >= 0
    f = 3*sqrt(x**2 + 1)*sqrt(y**2 + 1) - 2*(x*y - 1) - 2*sqrt(x**2 + 1) - 2*sqrt(y**2 + 1)
    # a**2 - b**2 >= 0 && a + b >= 0 => a - b >= 0
    g = (3*sqrt(x**2 + 1)*sqrt(y**2 + 1) - 2*(x*y - 1))**2 - (2*sqrt(x**2 + 1) + 2*sqrt(y**2 + 1))**2
    # to prove: (3*sqrt(x**2 + 1)*sqrt(y**2 + 1) - 2*(x*y - 1)) + (2*sqrt(x**2 + 1) + 2*sqrt(y**2 + 1)) >= 0
    # 3*sqrt(x**2 + 1)*sqrt(y**2 + 1) > 3*x*y > 2*(x*y - 1)
    print('g =', factor(g))
    h = (13*x**2*y**2 + 5*x**2 - 8*x*y + 5*y**2 + 5)**2 - ((12*x*y - 4)*sqrt(x**2 + 1)*sqrt(y**2 + 1))**2
    # to prove: (13*x**2*y**2 + 5*x**2 - 8*x*y + 5*y**2 + 5) + ((12*x*y - 4)*sqrt(x**2 + 1)*sqrt(y**2 + 1)) >= 0
    # sqrt(x**2 + 1) > x, sqrt(y**2 + 1) > y, 12*x*y - 4 > 8, (13*x**2*y**2 + 5*x**2 - 8*x*y + 5*y**2 + 5) + 8*x*y > 0
    u, v, w = symbols('u, v, w', positive = True)
    # y = (1 + u)/x, h = 0 at x = sqrt(3) and u = 2
    h = h.subs(y, (1 + u)/x)
    print('h =', factor(h))
    s3 = sqrt(3)
    print('h(<s3,<2) =', factor(h.subs(x, sqrt(3)/(1 + v)).subs(u, 2/(1 + w)))) # to prove
    print('h(>s3,<2) =', factor(h.subs(x, sqrt(3) + v).subs(u, 2/(1 + w)))) # obvious
    print('h(<s3,>2) =', factor(h.subs(x, sqrt(3)/(1 + v)).subs(u, 2 + w))) # obvious
    print('h(>s3,>2) =', factor(h.subs(x, sqrt(3) + v).subs(u, 2 + w))) # to prove
    # x <= u <= s3, to prove
    print('h(xu3) =', factor(h.subs(x, sqrt(3)/(1 + v + w)).subs(u, sqrt(3)/(1 + v))))
    # u <= x <= s3, to prove
    print('h(xu3) =', factor(h.subs(x, sqrt(3)/(1 + v)).subs(u, sqrt(3)/(1 + v + w))))
    # x <= s3 <= u <= 2, to prove
    print('h(x3u2) =', factor(h.subs(x, sqrt(3)/(1 + v)).subs(u, 2 - (2 - sqrt(3))/(1 + w))))
    # s3 <= x <= 2 <= u, unable to prove
    print('h(3x2u) =', factor(h.subs(x, 2 - (2 - sqrt(3))/(1 + v)).subs(u, 2 + w)))
    # 2 <= x <= u, to prove
    print('h(2xu) =', factor(h.subs(x, 2 + v).subs(u, 2 + v + w)))
    # 2 <= x <= u, obvious
    print('h(2ux) =', factor(h.subs(x, 2 + v + w).subs(u, 2 + v)))
    # s3 <= x <= 2 <= u
    j = 369*v**8*w**4 + 2700*v**8*w**3 + 4958*v**8*w**2 - 2020*v**8*w + 1049*v**8 + 744*sqrt(3)*v**7*w**4 + 1464*v**7*w**4 + 5408*sqrt(3)*v**7*w**3 + 10784*v**7*w**3 + 8632*sqrt(3)*v**7*w**2 + 22400*v**7*w**2 - 10288*sqrt(3)*v**7*w + 4416*v**7*w - 10840*v**7 + 9616*sqrt(3)*v**7 + 4018*v**6*w**4 + 2864*sqrt(3)*v**6*w**4 + 30408*v**6*w**3 + 20416*sqrt(3)*v**6*w**3 + 35280*sqrt(3)*v**6*w**2 + 61978*v**6*w**2 - 22048*sqrt(3)*v**6*w + 28*v**6*w - 50208*sqrt(3)*v**6 + 100408*v**6 + 4560*sqrt(3)*v**5*w**4 + 8828*v**5*w**4 + 31488*sqrt(3)*v**5*w**3 + 68080*v**5*w**3 + 47928*sqrt(3)*v**5*w**2 + 148748*v**5*w**2 - 55920*sqrt(3)*v**5*w + 36424*v**5*w - 54240*v**5 + 40896*sqrt(3)*v**5 + 4480*sqrt(3)*v**4*w**4 + 11705*v**4*w**4 + 29952*sqrt(3)*v**4*w**3 + 90956*v**4*w**3 + 35744*sqrt(3)*v**4*w**2 + 210852*v**4*w**2 - 91456*sqrt(3)*v**4*w + 100912*v**4*w - 115584*sqrt(3)*v**4 + 211728*v**4 + 3560*sqrt(3)*v**3*w**4 + 8324*v**3*w**4 + 23968*sqrt(3)*v**3*w**3 + 64944*v**3*w**3 + 32064*sqrt(3)*v**3*w**2 + 149952*v**3*w**2 - 58048*sqrt(3)*v**3*w + 67680*v**3*w - 27648*v**3 + 18432*sqrt(3)*v**3 + 3164*v**2*w**4 + 2064*sqrt(3)*v**2*w**4 + 24640*v**2*w**3 + 14400*sqrt(3)*v**2*w**3 + 24000*sqrt(3)*v**2*w**2 + 55216*v**2*w**2 - 16896*sqrt(3)*v**2*w + 18816*v**2*w - 36864*sqrt(3)*v**2 + 64512*v**2 + 848*v*w**4 + 544*sqrt(3)*v*w**4 + 6432*v*w**3 + 3904*sqrt(3)*v*w**3 + 6400*sqrt(3)*v*w**2 + 14976*v*w**2 - 6144*sqrt(3)*v*w + 9216*v*w + 208*w**4 + 1536*w**3 + 3072*w**2
    s = symbols('s', positive = True)
    # v <= w
    print('j(vw) =', factor(j.subs(w, v*(1 + s))))
    # w <= v
    print('j(wv) =', factor(j.subs(v, w*(1 + s))))

if __name__ == '__main__':
    main()