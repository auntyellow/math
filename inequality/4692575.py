from sympy import *

def main():
    # https://math.stackexchange.com/q/4692575
    a, b, c = symbols('a, b, c', positive = True)
    f = 1/a + 1/b + 1/c + 6/(a + b + c) - 5
    u, v = symbols('u, v', positive = True)
    # a <= 1 <= b, c
    print('f(a1bc) =', factor(f.subs(a, 1/b/c).subs(b, 1 + u).subs(c, 1 + v)))
    # a, b <= 1 <= c
    print('f(ab1c) =', factor(f.subs(c, 1/a/b).subs(a, 1/(1 + u)).subs(b, 1/(1 + v))))
    print()

    # https://math.stackexchange.com/q/4765317
    f = 1/a + 1/b + 1/c - 6/(a + b + c) - 1
    w = symbols('w', positive = True)
    # a <= 1 <= b, c
    print('f(a1bc) =', factor(f.subs(a, 1/(b*c + w)).subs(b, 1 + u).subs(c, 1 + v)))
    # a, b <= 1 <= c <= 1/ab
    print('f(ab1c) =', factor(f.subs(c, 1 + (1/a/b - 1)/(1 + w)).subs(a, 1/(1 + u)).subs(b, 1/(1 + v))))
    # a, b, c <= 1
    print('f(abc1) =', factor(f.subs(a, 1/(1 + u + v + w)).subs(b, 1/(1 + u + v)).subs(c, 1/(1 + u))))

if __name__ == '__main__':
    main()