from sympy import *

# When can we say that a≥b≥c without loss of generality?
# https://math.stackexchange.com/q/4774244

def is_cyclic(f, vars):
    x, y, z = vars
    t = symbols('t', positive = True)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x) == f

def is_symmetric(f, vars):
    x, y, z = vars
    t = symbols('t', positive = True)
    return is_cyclic(f, vars) and f.subs(y, t).subs(x, y).subs(t, x) == f

def main():
    a, b, c = symbols('a, b, c', positive = True)
    f = a/(b + c) + b/(c + a) + c/(a + b) - S(3)/2
    print('Is f cyclic?', is_cyclic(f, (a, b, c)))
    print('Is f symmetric?', is_symmetric(f, (a, b, c)))
    u, v = symbols('u, v', positive = True)
    print('f(a≥b≥c) =', factor(f.subs(b, c*(1 + u)).subs(a, c*(1 + u + v))))
    print()

    f = a/b + b/c + c/a - 3
    print('Is f cyclic?', is_cyclic(f, (a, b, c)))
    print('Is f symmetric?', is_symmetric(f, (a, b, c)))
    print('f(a≥b≥c) =', factor(f.subs(b, c*(1 + u)).subs(a, c*(1 + u + v))))
    print('f(b≥a≥c) =', factor(f.subs(a, c*(1 + u)).subs(b, c*(1 + u + v))))
    print()

    f = a**3/(3*a**2 + b**2) + b**3/(3*b**2 + c**2) + c**3/(3*c**2 + a**2) - (a + b + c)/4
    print('Is f cyclic?', is_cyclic(f, (a, b, c)))
    print('Is f symmetric?', is_symmetric(f, (a, b, c)))
    print('f(a≥b≥c) =', factor(f.subs(b, c*(1 + u)).subs(a, c*(1 + u + v))))
    print('f(b≥a≥c) =', factor(f.subs(a, c*(1 + u)).subs(b, c*(1 + u + v))))
    print('f(3,4,1) =', f.subs(a, 3).subs(b, 4).subs(c, 1))
    print('f(2,3,1) =', f.subs(a, 2).subs(b, 3).subs(c, 1))

if __name__ == '__main__':
    main()