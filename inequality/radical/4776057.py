from sympy import *

# https://math.stackexchange.com/q/4776057

def main():
    u, v = symbols('u, v', positive = True)
    A, B, C = 1, 1 + u, 1 + u + v
    ABC = (A + B + C)/sqrt(5)
    a0, b0, c0 = A/ABC, B/ABC, C/ABC
    print('a + b + c =', factor(a0 + b0 + c0))
    a, b, c = symbols('a, b, c', positive = True)
    f = a/sqrt(5 - 4*b*c) + b/sqrt(5 - 4*c*a) + c/sqrt(5 - 4*a*b) - 1
    # f = ... - 3/sqrt(5) <= 0 ?
    print('f =', factor(f.subs(a, a0).subs(b, b0).subs(c, c0)))

    # A**2 - B**2 >= 0 && A + B >= 0 -> A - B >= 0
    g = (a/sqrt(5 - 4*b*c) + b/sqrt(5 - 4*c*a))**2 - (1 - c/sqrt(5 - 4*a*b))**2
    # to prove: g2 = (a/sqrt(5 - 4*b*c) + b/sqrt(5 - 4*c*a)) + (1 - c/sqrt(5 - 4*a*b)) >= 0
    g1 = 1 - c**2/(5 - 4*a*b)
    print('g1 =', factor(g1.subs(a, a0).subs(b, b0).subs(c, c0)))
    # g1 >= 0 -> 1 - c/sqrt(5 - 4*a*b) >= 0 -> g2 >= 0
    print('g =', expand(g))
    h = (a**2/(-4*b*c + 5) + b**2/(-4*a*c + 5) - c**2/(-4*a*b + 5) - 1)**2 - (2*a*b/(sqrt(-4*a*c + 5)*sqrt(-4*b*c + 5)) + 2*c/sqrt(-4*a*b + 5))**2
    # A**2 - B**2 <= 0 && A - B <= 0 -> A + B >= 0
    print('h =', factor(h.subs(a, a0).subs(b, b0).subs(c, c0)))
    # to prove: (a**2/(-4*b*c + 5) + b**2/(-4*a*c + 5) - c**2/(-4*a*b + 5) - 1) - (2*a*b/(sqrt(-4*a*c + 5)*sqrt(-4*b*c + 5)) + 2*c/sqrt(-4*a*b + 5)) <= 0
    # not obvious ...

if __name__ == '__main__':
    main()