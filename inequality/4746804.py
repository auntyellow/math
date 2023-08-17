from sympy import *

# https://math.stackexchange.com/q/4746804

def main():
    a, b = symbols('a, b', positive = True)
    c = (1 - a*b)/(a + b)
    f = 1 + 36*(a*b*c)**2 - 21*a*b*c/(a + b + c)
    u, v, w = symbols('u, v, w', positive = True)
    print('f =', factor(f.subs(a, u).subs(b, 1/(u + v))))

    g = u**10 + 6*u**9*v + 15*u**8*v**2 + 4*u**8 + 20*u**7*v**3 + 15*u**6*v**4 - 3*u**6*v**2 + 6*u**6 + 6*u**5*v**5 - 4*u**5*v**3 - 16*u**5*v + u**4*v**6 - 18*u**4*v**4 - 10*u**4*v**2 + 4*u**4 - 12*u**3*v**5 + 18*u**3*v**3 - 8*u**3*v + u**2*v**6 + 8*u**2*v**4 + 9*u**2*v**2 + u**2 + 2*u*v**5 - 14*u*v**3 + 2*u*v + v**4 + v**2
    print('g(uv) =', factor(g.subs(v, u*(1 + w))))

if __name__ == '__main__':
    main()