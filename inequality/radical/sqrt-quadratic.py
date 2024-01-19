from sympy import *

def main():
    # find best a and b such that sqrt(x) >= a*x**2 + b*x when 0 <= x <= c
    a, b, c, x = symbols('a, b, c, x')
    s = a*x**2 + b*x
    eq1 = Eq(sqrt(c), s.subs(x, c))
    eq2 = Eq(diff(sqrt(x)).subs(x, c), diff(s, x).subs(x, c))
    result = solve([eq1, eq2], a, b)
    print('sqrt(x) <= s(x) =', s.subs(a, result[a]).subs(b, result[b]))

if __name__ == '__main__':
    main()