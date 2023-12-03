from sympy import *

# http://xbna.pku.edu.cn/CN/Y2013/V49/I4/545 , ex 4.5

def main():
    a, b, c, d = symbols('a, b, c, d', negative = False)
    p, q, r, s = symbols('p, q, r, s', negative = False)
    f = (a**2 + 3)*(b**2 + 3)*(c**2 + 3)*(d**2 + 3) - 16*(a + b + c + d)**2
    print('f(abcd1) =', factor(f.subs(d, 1/(1 + p)).subs(c, 1/(1 + p + q)).subs(b, 1/(1 + p + q + r)).subs(a, 1/(1 + p + q + r + s))))
    print('f(abc1d) =', factor(f.subs(d, 1 + p).subs(c, 1/(1 + q)).subs(b, 1/(1 + q + r)).subs(a, 1/(1 + q + r + s))))
    print('f(ab1cd) =', factor(f.subs(d, 1 + p + q).subs(c, 1 + p).subs(b, 1/(1 + r)).subs(a, 1/(1 + r + s))))
    print('f(a1bcd) =', factor(f.subs(d, 1 + p + q + r).subs(c, 1 + p + q).subs(b, 1 + p).subs(a, 1/(1 + s))))
    print('f(1abcd) =', factor(f.subs(d, 1 + p + q + r + s).subs(c, 1 + p + q + r).subs(b, 1 + p + q).subs(a, 1 + p)))

if __name__ == '__main__':
    main()