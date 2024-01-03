from sympy import *

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

# ISBN 9787312056185, p352, ex 11.19

def main():
    a, b, c, d, u, v, w = symbols('a, b, c, d, u, v, w', negative = False)
    f = sum_cyc((1 - a)**2 - c**2*(1 - a**2)*(1 - b**2)/(a*b + c)**2, (a, b, c))
    fn, fd = fraction(cancel(f.subs(a, a/d).subs(b, b/d).subs(c, c/d)))
    print('fn =', fn) # proved by SDS
    print('fd =', fd)
    print('f(0, 1/2, 1/2) =', f.subs(a, 0).subs(b, .5).subs(c, .5))
    print('f(u, u, u) =', cancel(f.subs(a, u).subs(b, u).subs(c, u)))
    '''
    # can be proved by 3-var polynomial-prover? too slow
    print('f(abc1) =', factor(f.subs(a, 1/(1 + u + v + w)).subs(b, 1/(1 + u + v)).subs(c, 1/(1 + u))))
    print('f(ab1c) =', factor(f.subs(a, 1/(1 + u + v)).subs(b, 1/(1 + u)).subs(c, 1 + w)))
    print('f(a1bc) =', factor(f.subs(a, 1/(1 + u)).subs(b, 1 + v).subs(c, 1 + v + w)))
    print('f(1abc) =', factor(f.subs(a, 1 + u).subs(b, 1 + u + v).subs(c, 1 + u + v + w)))
    '''

if __name__ == '__main__':
    main()