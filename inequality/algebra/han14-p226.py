from sympy import *

# ISBN 9787560349800, p226, ex 9.5

def main():
    a, b, c, u, v, w = symbols('a, b, c, u, v, w', negative = False)
    f = a/(b + c + 1) + b/(c + a + 1) + c/(a + b + 1) + (1 - a)*(1 - b)*(1 - c) - 1
    print('f =', factor(f.subs(a, 1/(1 + u)).subs(b, 1/(1 + u + v)).subs(c, 1/(1 + u + v + w))))
    print()

    f += S(1)/8
    s2 = S(1)/2
    print('f(.5,.5,.5) =', f.subs({a: s2, b: s2, c: s2}))
    print('f =', factor(f))
    # abc are symmetric, so need to prove: ---, --+, -++ and --- (-: <= .5; +: >= .5)
    print('f(---) =', factor(f.subs(a, (1 - a)/2).subs(b, (1 - b)/2).subs(c, (1 - c)/2)))
    print('f(--+) =', factor(f.subs(a, (1 - a)/2).subs(b, (1 - b)/2).subs(c, (1 + c)/2)))
    print('f(-++) =', factor(f.subs(a, (1 - a)/2).subs(b, (1 + b)/2).subs(c, (1 + c)/2)))
    print('f(+++) =', factor(f.subs(a, (1 + a)/2).subs(b, (1 + b)/2).subs(c, (1 + c)/2)))

if __name__ == '__main__':
    main()