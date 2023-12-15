from sympy import *

# http://xbna.pku.edu.cn/CN/Y2013/V49/I4/545 , ex 4.4

def main():
    a, b, c, u, v = symbols('a, b, c, u, v', negative = False)
    f = (a**2 + b**2 + c**2)**2 - 3*(a**3*b + b**3*c + c**3*a)
    print('f(abc) =', factor(f.subs(c, a*(1 + u + v)).subs(b, a*(1 + u))))
    print('f(acb) =', factor(f.subs(b, a*(1 + u + v)).subs(c, a*(1 + u))))
    # f(acb)
    g = u**4 - u**3*v + u**3 - u**2*v**2 - 3*u**2*v + u**2 + u*v**3 - 2*u*v**2 + u*v + v**4 + v**3 + v**2
    # proved by polynomial-prover
    print('g(uv) =', factor(g.subs(v, u*(1 + v))))
    # unable to find rational zeros
    print('g(vu) =', factor(g.subs(u, v*(1 + u))))
    # equality occurs when a = sin(pi/7)**2, b = sin(4*pi/7)**2 and c = sin(2*pi/7)**2
    # see https://math.stackexchange.com/q/2587996/

if __name__ == '__main__':
    main()