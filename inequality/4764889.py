from sympy import *

# https://math.stackexchange.com/q/4764889

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', positive = True)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c = symbols('a, b, c', positive = True)
    x1 = sqrt(a/(a + b + c))
    y1 = sqrt(b/(a + b + c))
    z1 = sqrt(c/(a + b + c))
    print('x*x + y*y + z*z =', factor(x1*x1 + y1*y1 + z1*z1))

    x, y, z = symbols('x, y, z', positive = True)
    # left ineq: 1 <= f
    f = sum_cyc(x/(1 + x*y), (x, y, z)).subs(x, x1).subs(y, y1).subs(z, z1)
    print('f =', factor(f))
    A, B, C = symbols('A, B, C', positive = True)
    f1 = fraction(factor(f.subs(sqrt(a), A).subs(sqrt(b), B).subs(sqrt(c), C)))
    print('g =', factor(f1[0]**2 - f1[1]**2))

    # right ineq: f <= 3*sqrt(3)/2
    f = sum_cyc(x/(1 - x*y), (x, y, z)).subs(x, x1).subs(y, y1).subs(z, z1)
    print('f =', factor(f))
    f1 = fraction(factor(f.subs(sqrt(a), A).subs(sqrt(b), B).subs(sqrt(c), C)))
    g = f1[0]**2*4 - f1[1]**2*27
    u, v = symbols('u, v', positive = True)
    print('g =', factor(g.subs(B, A*(1 + u)).subs(C, A*(1 + u + v))))

if __name__ == '__main__':
    main()