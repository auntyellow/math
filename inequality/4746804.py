from sympy import *

# https://math.stackexchange.com/q/4746804

def main():
    a, b = symbols('a, b', positive = True)
    c = (1 - a*b)/(a + b)
    f = 1 + 36*(a*b*c)**2 - 21*a*b*c/(a + b + c)
    u, v = symbols('u, v', positive = True)
    # a <= 1, b >= 1/a (so a*b <= 1)
    print('f =', factor(f.subs(b, 1/(a + u))))

    g = a**10 + 6*a**9*u + 15*a**8*u**2 + 4*a**8 + 20*a**7*u**3 + 15*a**6*u**4 - 3*a**6*u**2 + 6*a**6 + 6*a**5*u**5 - 4*a**5*u**3 - 16*a**5*u + a**4*u**6 - 18*a**4*u**4 - 10*a**4*u**2 + 4*a**4 - 12*a**3*u**5 + 18*a**3*u**3 - 8*a**3*u + a**2*u**6 + 8*a**2*u**4 + 9*a**2*u**2 + a**2 + 2*a*u**5 - 14*a*u**3 + 2*a*u + u**4 + u**2
    # u <= a can be proved by polynomial-prover with u = [0, oo], v = [0, oo]
    print('g(ua) =', factor(g.subs(a, u*(1 + v))))
    # a <= u doesn't work, even if we know minimum at a = 1/sqrt(3) and v = 1
    print('g(au) =', factor(g.subs(u, a*(1 + v))))

if __name__ == '__main__':
    main()