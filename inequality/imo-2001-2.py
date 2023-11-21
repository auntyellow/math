from sympy import *

# https://web.evanchen.cc/handouts/Ineq/en.pdf , ex 2.9
# 1 <= sum_cyc(a/sqrt(a**2 + 8*b*c)) < 2

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c = symbols('a, b, c', negative = False)
    # sum_cyc(a/sqrt(a**2 + 8*b*c)) < 2
    # https://math.stackexchange.com/a/4785071
    # Cauchy-Schwarz:
    # This doesn't work:
    # sum_cyc(a/sqrt(a**2 + 8*b*c)) = sum_cyc(sqrt(a)*sqrt(a/(a**2 + 8*b*c)))
    # This works:
    # sum_cyc(a/sqrt(a**2 + 8*b*c)) = sum_cyc(sqrt(a*(b + c))*sqrt(a/(b + c)/(a**2 + 8*b*c)))
    # <= sqrt(sum_cyc(a*(b + c))*sum_cyc(a/(b + c)/(a**2 + 8*b*c)))
    f = 4 - sum_cyc(a*(b + c), (a, b, c))*sum_cyc(a/(b + c)/(a**2 + 8*b*c), (a, b, c))
    f = factor(f)
    print('f =', f)
    u, v = symbols('u, v', negative = False)
    print('  =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    print()

    # https://web.evanchen.cc/handouts/Ineq/en.pdf , ex 3.4
    # sum_cyc(a/sqrt(a**2 + 8*b*c)) >= 1
    # Holder: m + n = 1: (A1 + A2 + A3)**m*(B1 + B2 + B3)**n >= A1**m*B1**n + A2**m*B2**n + A3**m*B3**n
    # sum_cyc(a/sqrt(a**2 + 8*b*c))**(2/3)*sum_cyc(a*(a**2 + 8*b*c))**(1/3) >=
    # sum_cyc((a/sqrt(a**2 + 8*b*c))**(2/3)*(a*(a**2 + 8*b*c))**(1/3)) = sum_cyc(a)
    # to prove: sum_cyc(a)**3 >= sum_cyc(a*(a**2 + 8*b*c))
    f = sum_cyc(a, (a, b, c))**3 - sum_cyc(a*(a**2 + 8*b*c), (a, b, c))
    f = factor(f)
    print('f =', f)
    u, v = symbols('u, v', negative = False)
    print('  =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))

if __name__ == '__main__':
    main()