from sympy import *

# ISBN 9787542848482, p36, §2.1, ex3
# x**2 + y**2 + z**2 + x*y*z = 4 -> 0 <= x*y + y*z + z*x - x*y*z <= 2

def main():
    x, y, z = symbols('x, y, z', positive = True)
    z = solve(Eq(x**2 + y**2 + z**2 + x*y*z, 4), z)[1]
    print('z =', z)
    sxy = x**2*y**2 - 4*x**2 - 4*y**2 + 16
    print('  = sqrt({})/2 - x*y/2'.format(factor(sxy)))
    ym = solve(Eq(sxy, (x*y)**2), y)[0]
    print('y <=', ym)

    f = x*y + y*z + z*x - x*y*z
    print('f = x*y + y*z + z*x - x*y*z =', factor(f))
    u, v = symbols('u, v', positive = True)
    print('  =', factor(f.subs(y, ym/(1 + v)).subs(x, 2/(1 + u))))
    u4v2_2u = u**4*v**2 + 2*u**4*v + 4*u**3*v**2 + 8*u**3*v + 5*u**2*v**2 + 10*u**2*v + u**2 + 2*u*v**2 + 4*u*v + 2*u
    print('u**4*v**2 + ... + 2*u =', factor(u4v2_2u))
    u2v2_1 = u**2*v**2 + 2*u**2*v + 2*u*v**2 + 4*u*v + v**2 + 2*v + 1
    U = symbols('U', positive = True)
    print('f =', factor(f.subs(y, ym/(1 + v)).subs(x, 2/(1 + u))). \
        subs(sqrt(u4v2_2u), U*sqrt(u2v2_1)).subs(sqrt(u**2 + 2*u), U).subs(U, sqrt(u**2 + 2*u)).factor())

    d = x + y - x*y
    print(d, '=', factor(d.subs(y, ym/(1 + v)).subs(x, 2/(1 + u))))
    # to prove: d >= 0
    # x->0: -x**2/2/a**3 + x/2/a + a <= sqrt(a**2 + x) <= x/2/a + a
    f = x**2*y**2 - x**2*y - x*y**2 + 2*x*y + (x + y - x*y)*sqrt(x**2*y**2 - 4*x**2 - 4*y**2 + 16)
    x2y2 = x**2*y**2 - 4*x**2 - 4*y**2
    f1 = x**2*y**2 - x**2*y - x*y**2 + 2*x*y + (x + y - x*y)*(-x2y2**2/128 + x2y2/8 + 4)
    print('f - f1 =', factor((f - f1).subs(y, ym/(1 + v)).subs(x, 2/(1 + u))))
    print('f1 =', factor(f1.subs(y, ym/(1 + v)).subs(x, 2/(1 + u))))
    # U = sqrt(u**2 + 2*u)
    g = 2*u**8*v**5 + 2*u**8*v**4*U + 10*u**8*v**4 + 8*u**8*v**3*U + 17*u**8*v**3 + 11*u**8*v**2*U + 11*u**8*v**2 + 6*u**8*v*U - 2*u**8 + 18*u**7*v**5 + 16*u**7*v**4*U + 90*u**7*v**4 + 64*u**7*v**3*U + 157*u**7*v**3 + 89*u**7*v**2*U + 111*u**7*v**2 + 50*u**7*v*U + 12*u**7*v + 2*u**7*U - 14*u**7 + 71*u**6*v**5 + 53*u**6*v**4*U + 355*u**6*v**4 + 212*u**6*v**3*U + 636*u**6*v**3 + 298*u**6*v**2*U + 488*u**6*v**2 + 172*u**6*v*U + 101*u**6*v + 17*u**6*U - 35*u**6 + 161*u**5*v**5 + 93*u**5*v**4*U + 805*u**5*v**4 + 372*u**5*v**3*U + 1480*u**5*v**3 + 530*u**5*v**2*U + 1220*u**5*v**2 + 316*u**5*v*U + 359*u**5*v + 57*u**5*U - 25*u**5 + 230*u**4*v**5 + 88*u**4*v**4*U + 1150*u**4*v**4 + 352*u**4*v**3*U + 2167*u**4*v**3 + 517*u**4*v**2*U + 1901*u**4*v**2 + 330*u**4*v*U + 703*u**4*v + 93*u**4*U + 49*u**4 + 212*u**3*v**5 + 34*u**3*v**4*U + 1060*u**3*v**4 + 136*u**3*v**3*U + 2047*u**3*v**3 + 227*u**3*v**2*U + 1901*u**3*v**2 + 182*u**3*v*U + 825*u**3*v + 73*u**3*U + 123*u**3 + 123*u**2*v**5 - 11*u**2*v**4*U + 615*u**2*v**4 - 44*u**2*v**3*U + 1220*u**2*v**3 - 34*u**2*v**2*U + 1200*u**2*v**2 + 20*u**2*v*U + 585*u**2*v + 21*u**2*U + 113*u**2 + 41*u*v**5 - 15*u*v**4*U + 205*u*v**4 - 60*u*v**3*U + 420*u*v**3 - 78*u*v**2*U + 440*u*v**2 - 36*u*v*U + 235*u*v - 3*u*U + 51*u + 6*v**5 - 4*v**4*U + 30*v**4 - 16*v**3*U + 64*v**3 - 24*v**2*U + 72*v**2 - 16*v*U + 42*v - 4*U + 10
    p = Poly(g, U)
    a, b = p.nth(1), p.nth(0)
    print('g = ({})*U + {}'.format(a, b))
    # doesn't work because a*U - b is undetermined

    # a**2 - b**2 <= 0 && a + b <= 0 -> a - b >= 0
    g = (x**2*y**2 - x**2*y - x*y**2 + 2*x*y)**2 - ((x*y - x - y)*sqrt(x**2*y**2 - 4*x**2 - 4*y**2 + 16))**2
    h = (x**2*y**2 - x**2*y - x*y**2 + 2*x*y) + ((x*y - x - y)*sqrt(x**2*y**2 - 4*x**2 - 4*y**2 + 16))
    u, v = symbols('u, v', positive = True)
    # g <= 0 doesn't hold
    print('g =', factor(g.subs(y, ym/(1 + v)).subs(x, 2/(1 + u))))
    # h <= 0 doesn't hold
    print('h =', factor(h.subs(y, ym/(1 + v)).subs(x, 2/(1 + u))))

    f = 2 - (x*y + y*z + z*x - x*y*z)
    print('f =', factor(f))
    print('  =', factor(f.subs(y, ym/(1 + v)).subs(x, 2/(1 + u))))
    # a**2 - b**2 >= 0 && a + b <= 0 -> a - b <= 0
    g = (x**2*y**2 - x**2*y - x*y**2 + 2*x*y - 4)**2 - ((x*y - x - y)*sqrt(x**2*y**2 - 4*x**2 - 4*y**2 + 16))**2
    h = (x**2*y**2 - x**2*y - x*y**2 + 2*x*y - 4) + ((x*y - x - y)*sqrt(x**2*y**2 - 4*x**2 - 4*y**2 + 16))
    # to prove: g <= 0 (a**2 - b**2 >= 0)
    print('g =', factor(g.subs(y, ym/(1 + v)).subs(x, 2/(1 + u))))
    # to prove: h <= 0 (a + b <= 0)
    print('h =', factor(h.subs(y, ym/(1 + v)).subs(x, 2/(1 + u))))
    # -sqrt(u**2 + 2*u) > -(u + 1)
    j = u**4*v**2 + 2*u**4*v + u**4 + 4*u**3*v**2 + 8*u**3*v + 6*u**3 + 6*u**2*v**2 - 2*u**2*v*sqrt(u**2 + 2*u) + 12*u**2*v - 2*u**2*(u + 1) + 8*u**2 + 4*u*v**2 - 2*u*v*(u + 1) + 2*u*v*sqrt(u**4*v**2 + 2*u**4*v + 4*u**3*v**2 + 8*u**3*v + 5*u**2*v**2 + 10*u**2*v + u**2 + 2*u*v**2 + 4*u*v + 2*u) + 8*u*v + 2*u*sqrt(u**2 + 2*u)*sqrt(u**4*v**2 + 2*u**4*v + 4*u**3*v**2 + 8*u**3*v + 5*u**2*v**2 + 10*u**2*v + u**2 + 2*u*v**2 + 4*u*v + 2*u) - 2*u*(u + 1) + 2*u*sqrt(u**4*v**2 + 2*u**4*v + 4*u**3*v**2 + 8*u**3*v + 5*u**2*v**2 + 10*u**2*v + u**2 + 2*u*v**2 + 4*u*v + 2*u) + v**2 + 2*v*sqrt(u**4*v**2 + 2*u**4*v + 4*u**3*v**2 + 8*u**3*v + 5*u**2*v**2 + 10*u**2*v + u**2 + 2*u*v**2 + 4*u*v + 2*u) + 2*v - 2*(u + 1)*sqrt(u**4*v**2 + 2*u**4*v + 4*u**3*v**2 + 8*u**3*v + 5*u**2*v**2 + 10*u**2*v + u**2 + 2*u*v**2 + 4*u*v + 2*u) + 2*sqrt(u**4*v**2 + 2*u**4*v + 4*u**3*v**2 + 8*u**3*v + 5*u**2*v**2 + 10*u**2*v + u**2 + 2*u*v**2 + 4*u*v + 2*u) + 1
    print('j =', factor(j))
    # -2*u**(5/2)*v*sqrt(u + 2) > -2*u**2*v*(u + 1)
    j1 = -2*u**2*v*(u + 1) + 2*u**(S(3)/2)*v*sqrt(u**3*v**2 + 2*u**3*v + 4*u**2*v**2 + 8*u**2*v + 5*u*v**2 + 10*u*v + u + 2*v**2 + 4*v + 2) + 2*sqrt(u)*v*sqrt(u**3*v**2 + 2*u**3*v + 4*u**2*v**2 + 8*u**2*v + 5*u*v**2 + 10*u*v + u + 2*v**2 + 4*v + 2) + u**4*v**2 + 2*u**4*v + u**4 + 4*u**3*v**2 + 8*u**3*v + 4*u**3 + 6*u**2*v**2 + 10*u**2*v + 2*u**2*sqrt(u + 2)*sqrt(u**3*v**2 + 2*u**3*v + 4*u**2*v**2 + 8*u**2*v + 5*u*v**2 + 10*u*v + u + 2*v**2 + 4*v + 2) + 4*u**2 + 4*u*v**2 + 6*u*v - 2*u + v**2 + 2*v + 1
    print('j\' =', factor(j1))
    # 4*u**2 - 2*u + 1 >= 3*u**2 + (u - 1)**2

if __name__ == '__main__':
    main()