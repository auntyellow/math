from sympy import *

# ISBN 9787542848482, p36, §2.1, ex3
# x**2 + y**2 + z**2 + x*y*z = 4 => 0 <= x*y + y*z + z*x - x*y*z <= 2

def main():
    x, y, z = symbols('x, y, z', positive = True)
    z = solve(Eq(x*x + y*y + z*z + x*y*z, 4), z)[1]
    print('z =', z)
    sxy = x**2*y**2 - 4*x**2 - 4*y**2 + 16
    print('  = sqrt({})/2 - x*y/2'.format(factor(sxy)))
    ym = solve(Eq(sxy, (x*y)**2), y)[0]
    print('y <=', ym)

    f = x*y + y*z + z*x - x*y*z
    print('f =', factor(f))
    # a**2 - b**2 <= 0 && a + b <= 0 => a - b >= 0
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
    # a**2 - b**2 >= 0 && a + b <= 0 => a - b <= 0
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
    j1 = -2*u**2*v*(u + 1) + 2*u**(Integer(3)/2)*v*sqrt(u**3*v**2 + 2*u**3*v + 4*u**2*v**2 + 8*u**2*v + 5*u*v**2 + 10*u*v + u + 2*v**2 + 4*v + 2) + 2*sqrt(u)*v*sqrt(u**3*v**2 + 2*u**3*v + 4*u**2*v**2 + 8*u**2*v + 5*u*v**2 + 10*u*v + u + 2*v**2 + 4*v + 2) + u**4*v**2 + 2*u**4*v + u**4 + 4*u**3*v**2 + 8*u**3*v + 4*u**3 + 6*u**2*v**2 + 10*u**2*v + 2*u**2*sqrt(u + 2)*sqrt(u**3*v**2 + 2*u**3*v + 4*u**2*v**2 + 8*u**2*v + 5*u*v**2 + 10*u*v + u + 2*v**2 + 4*v + 2) + 4*u**2 + 4*u*v**2 + 6*u*v - 2*u + v**2 + 2*v + 1
    print('j\' =', factor(j1))
    # 4*u**2 - 2*u + 1 >= 3*u**2 + (u - 1)**2

if __name__ == '__main__':
    main()