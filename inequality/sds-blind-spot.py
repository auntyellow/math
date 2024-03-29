from sympy import *

def main():
    t, u, v, w, x, y, z = symbols('t, u, v, w, x, y, z', negative = False)
    # homogeneous, SDSTest.java, testTransform
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

    # non-homogeneous, SDSTest.java, testBasic
    f = (4*x - 3*y)**2 + 1
    f = Poly(f).homogenize(z).expr
    print('f =', f)
    # works when zero found at (3, 4, 0), see sds-blind-spot-a.py
    print('f(4x<=3y) =', expand(f.subs(x, 3*x/7).subs(y, y + 4*x/7)))
    print('f(3y<=4x) =', expand(f.subs(y, 4*y/7).subs(x, x + 3*y/7)))
    f = (5*x - 4*y)**2 + x
    f = Poly(f).homogenize(z).expr
    print('f =', f)
    # works when zero found at (4, 5, 0)
    print('f(5x<=4y) =', expand(f.subs(x, 4*x/9).subs(y, y + 5*x/9)))
    print('f(4y<=5x) =', expand(f.subs(y, 5*y/9).subs(x, x + 4*y/9)))
    f = (x**2 - y)**2 + 1
    print('f =', expand(f))
    f = Poly(f).homogenize(z).expr
    print('f =', f)
    # zero found at (0, 1, 0), but unable to divide simplex

if __name__ == '__main__':
    main()