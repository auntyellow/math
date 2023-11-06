from sympy import *

# ISBN 9787542848482, p36, §2.1, ex3
# x**2 + y**2 + z**2 + x*y*z = 4 -> 0 <= x*y + y*z + z*x - x*y*z <= 2

def main():
    a, b, c = symbols('a, b, c', positive = True)
    x, y, z = 2 - 4*b*c/(b + a)/(c + a), 2 - 4*c*a/(c + b)/(a + b), 2 - 4*a*b/(a + c)/(b + c)
    print('x**2 + y**2 + z**2 + x*y*z =', factor(x**2 + y**2 + z**2 + x*y*z))
    f = x*y + y*z + z*x - x*y*z
    u, v = symbols('u, v', positive = True)
    print('f =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    g = x*y + y*z + z*x - x*y*z - 2
    print('g =', factor(g.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))

    # not negative because x may be negative
    print('x =', factor(x.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    print('y =', factor(y.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    print('z =', factor(z.subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    # should restrict that x >= 0, i.e. u*(u + v) <= 2, or u <= sqrt(2) && v <= 2/u - u
    s2 = sqrt(2)
    # g's numerator, h <= 0
    h = 4*u**6 + 12*u**5*v + 8*u**5 + 13*u**4*v**2 + 20*u**4*v - 4*u**4 + 6*u**3*v**3 + 8*u**3*v**2 - 8*u**3*v - 16*u**3 + u**2*v**4 - 8*u**2*v**3 - 36*u**2*v**2 - 24*u**2*v - 8*u**2 - 4*u*v**4 - 32*u*v**3 - 40*u*v**2 - 8*u*v - 4*v**4 - 16*v**3 - 8*v**2
    s, t = symbols('s, t', positive = True)
    print('h =', factor(h.subs(v, (2/u - u)/(1 + t)).subs(u, s2/(1 + s))))

if __name__ == '__main__':
    main()