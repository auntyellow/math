from sympy import *

# https://math.stackexchange.com/q/2016364

def main():
    a, b, c, d = symbols('a, b, c, d', negative = False)
    f = a**4 + b**4 + c**4 + d**4 + a**2*b**2 + b**2*c**2 + c**2*d**2 + d**2*a**2 + 8*(1 - a)*(1 - b)*(1 - c)*(1 - d) - 1
    S2 = S(1)/2
    print('f(----) =', factor(f.subs(a, S2/(1 + a)).subs(b, S2/(1 + b)).subs(c, S2/(1 + c)).subs(d, S2/(1 + d))))
    print('f(---+) =', factor(f.subs(a, S2/(1 + a)).subs(b, S2/(1 + b)).subs(c, S2/(1 + c)).subs(d, S2 + S2/(1 + d))))
    print('f(--++) =', factor(f.subs(a, S2/(1 + a)).subs(b, S2/(1 + b)).subs(c, S2 + S2/(1 + c)).subs(d, S2 + S2/(1 + d))))
    print('f(-+++) =', factor(f.subs(a, S2/(1 + a)).subs(b, S2 + S2/(1 + b)).subs(c, S2 + S2/(1 + c)).subs(d, S2 + S2/(1 + d))))
    print('f(++++) =', factor(f.subs(a, S2 + S2/(1 + a)).subs(b, S2 + S2/(1 + b)).subs(c, S2 + S2/(1 + c)).subs(d, S2 + S2/(1 + d))))
    print('f(-+-+) =', factor(f.subs(a, S2/(1 + a)).subs(b, S2 + S2/(1 + b)).subs(c, S2/(1 + c)).subs(d, S2 + S2/(1 + d))))

if __name__ == '__main__':
    main()
