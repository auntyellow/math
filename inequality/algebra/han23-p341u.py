from sympy import *

# ISBN 9787312056185, p341, ex 11.7

def main():
    a, b, c, u, v, w = symbols('a, b, c, u, v, w', negative = False)
    f = 1/(a + u*b)/(a + v*b) + 1/(b + u*c)/(b + v*c) + 1/(c + u*a)/(c + v*a) - 9/(1 + u)/(1 + v)/(a*b + b*c + c*a)
    fn = Poly(fraction(cancel(f))[0]).homogenize(w).expr
    print('fn =', fn)

if __name__ == '__main__':
    main()