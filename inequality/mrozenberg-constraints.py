from sympy import *

# https://www.cut-the-knot.org/m/Algebra/MRozenbergInequalityWithConstraints.shtml

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', positive = True)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c = symbols('a, b, c', positive = True)
    f = sum_cyc(4*a*b*(a**2 + b**2) - a**4 - 5*a**2*b**2 - 2*a**2*b*c)

if __name__ == '__main__':
    main()