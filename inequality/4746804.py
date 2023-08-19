from sympy import *

# https://math.stackexchange.com/q/4746804

def main():
    a, b = symbols('a, b', positive = True)
    # a*b <= 1
    c = (1 - a*b)/(a + b)
    f = 1 + 36*(a*b*c)**2 - 21*a*b*c/(a + b + c)
    u, v = symbols('u, v', positive = True)
    s3 = 1/sqrt(3)
    # a <= b <= s3
    print('f(ab3) =', factor(f.subs(b, s3/(1 + u)).subs(a, s3/(1 + u + v))))
    # a <= s3 <= b <= 1/a, b <= 1 || 1 <= b ??
    print('f(a3b1) =', factor(f.subs(b, s3 + (1/a - s3)/(1 + v)).subs(a, s3/(1 + u))))
    # s3 <= a <= b <= 1
    print('f(3ab1) =', factor(f.subs(b, s3 + (1 - s3)/(1 + u)).subs(a, s3 + (1 - s3)/(1 + u + v))))
    # s3 <= a <= 1 <= b <= 1/a
    print('f(3a1b) =', factor(f.subs(b, 1 + (1/a - 1)/(1 + v)).subs(a, s3 + (1 - s3)/(1 + u))))

if __name__ == '__main__':
    main()