from sympy import *

def main():
    t, u, v, w, x, y, z = symbols('t, u, v, w, x, y, z', negative = False)
    # SDSTest.java, testTransform
    # example 2
    f = (3*x - y)**2 + (x - z)**2
    print('f(131) =', f.subs({x: 1, y: 3, z: 1}))
    # zero at (1, 3, 1) -> (1, 1, 1)
    f = f.subs(y, 3*y)
    print('f(y->3y) =', factor(f))
    print('f(111) =', f.subs({x: 1, y: 1, z: 1}))
    print('f =', factor(f.subs(z, x*(1 + u)).subs(y, x*(1 + v))))
    # example 3
    f = (2*w - x)**2 + (w - y)**2 + (w - z)**2
    print('f(1211) =', f.subs({w: 1, x: 2, y: 1, z: 1}))
    # zero at (1, 2, 1, 1) -> (1, 1, 1, 1)
    f = f.subs(x, 2*x)
    print('f(y->2y) =', factor(f))
    print('f(1111) =', f.subs({w: 1, x: 1, y: 1, z: 1}))
    print('f =', factor(f.subs(x, w*(1 + t)).subs(y, w*(1 + u)).subs(z, w*(1 + v))))
    print()

    # non-homogeneous
    f = (4*x - 3*y)**2 + 1
    print('f =', Poly(f).homogenize(z).expr)
    f = (5*x - 4*y)**2 + x
    print('f =', Poly(f).homogenize(z).expr)

if __name__ == '__main__':
    main()