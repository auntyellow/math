from math import inf
from sympy import *

# ISBN 9787542878021, p122, §8, ex8
# 5*(a*b*c + b*c*d + c*d*a + d*a*b) - v*a*b*c*d <= 12

def main():
    w, x, y, z, v, p, q, r = symbols('w, x, y, z, v, p, q, r', negative = False)
    wxyz = (w + x + y + z)/4
    a, b, c, d = w/wxyz, x/wxyz, y/wxyz, z/wxyz
    print('a + b + c + d =', factor(a + b + c + d))
    f = 5*(a*b*c + b*c*d + c*d*a + d*a*b) - v*a*b*c*d - 12
    f = f.subs(x, w*(1 + p)).subs(y, w*(1 + p + q)).subs(z, w*(1 + p + q + r))
    print('f =', factor(f))
    # g >= 0
    g = 3*p**4 + 8*p**3*q + 4*p**3*r + 64*p**3*v - 464*p**3 + 88*p**2*q**2 + 88*p**2*q*r + 128*p**2*q*v - 928*p**2*q + 82*p**2*r**2 + 64*p**2*r*v - 464*p**2*r + 192*p**2*v - 1488*p**2 + 128*p*q**3 + 192*p*q**2*r + 64*p*q**2*v - 352*p*q**2 + 136*p*q*r**2 + 64*p*q*r*v - 352*p*q*r + 256*p*q*v - 1984*p*q + 36*p*r**3 + 112*p*r**2 + 128*p*r*v - 992*p*r + 192*p*v - 1536*p + 48*q**4 + 96*q**3*r + 64*q**3 + 72*q**2*r**2 + 96*q**2*r + 64*q**2*v - 448*q**2 + 24*q*r**3 + 128*q*r**2 + 64*q*r*v - 448*q*r + 128*q*v - 1024*q + 3*r**4 + 48*r**3 + 48*r**2 + 64*r*v - 512*r + 64*v - 512
    p0 = Poly(g, (p, q, r))
    max = -inf
    for coeff in p0.coeffs():
        # print(coeff)
        m = solve(Eq(coeff, 0), v)
        if len(m) == 0:
            continue
        m = m[0]
        if m > max:
            max = m
    print('v >=', max)
    print('f =', factor(f.subs(v, max)))

if __name__ == '__main__':
    main()