from sympy import *

# ISBN 9787542848482, p35, §2.1, ex2
# x+y+z=xyz -> 1/sqrt(1+x^2)+1/sqrt(1+y^2)+1/sqrt(1+z^2)<=3/2

def main():
    x, y = symbols('x, y', positive = True)
    # x + y + z = x*y*z, x*y > 1
    z = (x + y)/(x*y - 1)
    print('x + y + z - x*y*z =', factor(x + y + z - x*y*z))
    # f >= 0
    f = 3*sqrt(x**2 + 1)*sqrt(y**2 + 1) - 2*(x*y - 1) - 2*sqrt(x**2 + 1) - 2*sqrt(y**2 + 1)
    # a**2 - b**2 >= 0 && a + b >= 0 -> a - b >= 0
    g = (3*sqrt(x**2 + 1)*sqrt(y**2 + 1) - 2*(x*y - 1))**2 - (2*sqrt(x**2 + 1) + 2*sqrt(y**2 + 1))**2
    # to prove: (3*sqrt(x**2 + 1)*sqrt(y**2 + 1) - 2*(x*y - 1)) + (2*sqrt(x**2 + 1) + 2*sqrt(y**2 + 1)) >= 0
    # 3*sqrt(x**2 + 1)*sqrt(y**2 + 1) > 3*x*y > 2*(x*y - 1)
    print('g =', factor(g))
    h = (13*x**2*y**2 + 5*x**2 - 8*x*y + 5*y**2 + 5)**2 - ((12*x*y - 4)*sqrt(x**2 + 1)*sqrt(y**2 + 1))**2
    # to prove: (13*x**2*y**2 + 5*x**2 - 8*x*y + 5*y**2 + 5) + ((12*x*y - 4)*sqrt(x**2 + 1)*sqrt(y**2 + 1)) >= 0
    # sqrt(x**2 + 1) > x, sqrt(y**2 + 1) > y, 12*x*y - 4 > 8, (13*x**2*y**2 + 5*x**2 - 8*x*y + 5*y**2 + 5) + 8*x*y > 0
    print('h =', factor(h))

    u, v, w = symbols('u, v, w', positive = True)
    # y = (1 + u)/x, h = 0 at x = sqrt(3) and u = 2
    h = h.subs(y, (1 + u)/x)
    print('h =', factor(h))
    s3 = sqrt(3)
    print('h(<s3,<2) =', factor(h.subs(x, s3/(1 + v)).subs(u, 2/(1 + w)))) # to prove
    print('h(>s3,<2) =', factor(h.subs(x, s3 + v).subs(u, 2/(1 + w)))) # obvious
    print('h(<s3,>2) =', factor(h.subs(x, s3/(1 + v)).subs(u, 2 + w))) # obvious
    print('h(>s3,>2) =', factor(h.subs(x, s3 + v).subs(u, 2 + w))) # to prove

    # h(<s3,<2)
    t = symbols('t', positive = True)
    # v <= w
    print('h(<s3,<2,vw) =', factor(h.subs(x, s3/(1 + v)).subs(u, 2/(1 + w)).subs(w, v*(1 + t))))
    # w <= v
    print('h(<s3,<2,wv) =', factor(h.subs(x, s3/(1 + v)).subs(u, 2/(1 + w)).subs(v, w*(1 + t))))
    # h(>s3,>2)
    # v <= w
    print('h(>s3,>2,vw) =', factor(h.subs(x, s3 + v).subs(u, 2 + w).subs(w, v*(1 + t))))
    # w <= v
    print('h(>s3,>2,wv) =', factor(h.subs(x, s3 + v).subs(u, 2 + w).subs(v, w*(1 + t))))

if __name__ == '__main__':
    main()