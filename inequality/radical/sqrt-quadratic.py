from sympy import *

def main():
    # find best k such that sqrt(x) >= k*x**2 + (1 - k)*x when 0 <= x <= 1
    k, u, x = symbols('k, u, x')
    s = k*x**2 + (1 - k)*x
    print('x - s**2 =', factor((x - s**2).subs(x, 1/(1 + u))))
    p = Poly(-k**2*u + 2*k*u + 2*k + u**2 + 2*u + 1, u)
    print('    non_negative_coeffs = [')
    for coeff in p.coeffs():
        print('        ' + str(coeff) + ',')
    print('    ]')
    s = s.subs(k, -S(1)/2)
    print('s(0) =', factor(s.subs(x, 0)))
    print('s(1) =', factor(s.subs(x, 1)))
    print('s(x) =', s)
    print('x - s**2 =', factor((x - s**2).subs(x, 1/(1 + u))))

if __name__ == '__main__':
    main()