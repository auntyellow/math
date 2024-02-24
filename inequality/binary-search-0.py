from sympy import *

def main():
    x, y = symbols('x, y', negative = False)
    # try to prove positive when x_i >= 0

    f = (5*x - 3*y)**2
    print('f =', expand(f))
    print('f(yx) =', cancel(f.subs(y, x*y)/x**2))
    print('f(xy) =', cancel(f.subs(x, x*y)/y**2))
    print()

    f = (5*x - 3*y)**2 + 1
    f = f.subs({x: 1/x, y: 1/y})*x**2*y**2
    print('f =', expand(f))
    print('f(yx) =', cancel(f.subs(y, x*y)/x**2))
    print('f(xy) =', cancel(f.subs(x, x*y)/y**2))
    print()

    f = (3*x**2 - 5*y)**2
    print('f =', expand(f))
    print('f(yx) =', cancel(f.subs(y, x*y)/x**2))
    print('f(xy) =', cancel(f.subs(x, x*y)/y**2))
    g = 9*x**2 - 30*x*y + 25*y**2
    print('g(yx) =', cancel(g.subs(y, x*y)/x**2))
    print('g(xy) =', cancel(g.subs(x, x*y)/y**2))
    print()

    f = (3*x**2 - 5*y)**2 + 1
    print('f =', expand(f))
    f = f.subs({x: 1/x, y: 1/y})*x**4*y**2
    print('f =', expand(f))
    print('f(yx) =', cancel(f.subs(y, x*y)/x**2))
    print('f(xy) =', cancel(f.subs(x, x*y)/y**2))
    g = x**4*y**2 + 25*x**2 - 30*x*y + 9*y**2
    print('g(yx) =', cancel(g.subs(y, x*y)/x**2))
    print('g(xy) =', cancel(g.subs(x, x*y)/y**2))
    print()

    u, v = symbols('u, v', negative = False)
    # result from p172-11u.py
    f = 2572755344*u**4 - 6426888360*u**3*v - 3844133016*u**3 + 5315682897*u**2*v**2 + 8649299286*u**2*v + 1441549881*u**2 - 1621722090*u*v**3 - 5766199524*u*v**2 - 2883099762*u*v + 1611722090*v**4 - 961033254*v**3 + 2082238717*v**2
    print('f(vu) =', cancel(f.subs(v, v*u)/u**2))
    print('f(uv) =', cancel(f.subs(u, v*u)/v**2))

if __name__ == '__main__':
    main()