from sympy import *

# ISBN 9787542848482, p34, §2.1, ex1

def main():
    a, b, c = symbols('a, b, c', positive = True)
    f = (a**2 + 2)*(b**2 + 2)*(c**2 + 2) - 9*(a*b + a*c + b*c)
    u, v, w = symbols('u, v, w', positive = True)
    # a <= b <= c <= 1
    print('f(abc1) =', factor(f.subs(a, 1/(1 + u + v + w)).subs(b, 1/(1 + u + v)).subs(c, 1/(1 + u))))
    # a <= b <= 1 <= c
    print('f(ab1c) =', factor(f.subs(a, 1/(1 + u + v)).subs(b, 1/(1 + u)).subs(c, 1 + w)))
    g = 4*u**4*w**2 + 8*u**4*w + 12*u**4 + 8*u**3*v*w**2 + 16*u**3*v*w + 24*u**3*v + 16*u**3*w**2 + 14*u**3*w + 30*u**3 + 4*u**2*v**2*w**2 + 8*u**2*v**2*w + 12*u**2*v**2 + 24*u**2*v*w**2 + 21*u**2*v*w + 45*u**2*v + 28*u**2*w**2 + 2*u**2*w + 21*u**2 + 8*u*v**2*w**2 + 7*u*v**2*w + 15*u*v**2 + 28*u*v*w**2 + 2*u*v*w + 21*u*v + 24*u*w**2 - 6*u*w + 6*v**2*w**2 + 3*v**2*w + 9*v**2 + 12*v*w**2 - 3*v*w + 9*w**2
    s, t = symbols('s, t', positive = True)
    # u, v <= w
    print('g(uvw) =', factor(g.subs(u, w/(1 + s)).subs(v, w/(1 + t))))
    # w <= u, v
    print('g(wuv) =', factor(g.subs(u, w*(1 + s)).subs(v, w*(1 + t))))
    # a <= 1 <= b <= c
    print('f(a1bc) =', factor(f.subs(a, 1/(1 + u)).subs(b, 1 + v).subs(c, 1 + v + w)))
    g = 2*u**2*v**4 + 4*u**2*v**3*w + 8*u**2*v**3 + 2*u**2*v**2*w**2 + 12*u**2*v**2*w + 11*u**2*v**2 + 4*u**2*v*w**2 + 11*u**2*v*w + 6*u**2*v + 6*u**2*w**2 + 3*u**2*w + 9*u**2 + 4*u*v**4 + 8*u*v**3*w + 16*u*v**3 + 4*u*v**2*w**2 + 24*u*v**2*w + 22*u*v**2 + 8*u*v*w**2 + 22*u*v*w - 6*u*v + 12*u*w**2 - 3*u*w + 3*v**4 + 6*v**3*w + 12*v**3 + 3*v**2*w**2 + 18*v**2*w + 21*v**2 + 6*v*w**2 + 21*v*w + 9*w**2
    # u <= v, w
    print('g(uvw) =', factor(g.subs(v, u*(1 + s)).subs(w, u*(1 + t))))
    # v, w <= u
    print('g(vwu) =', factor(g.subs(v, u/(1 + s)).subs(w, u/(1 + t))))
    # 1 <= a <= b <= c
    print('f(1abc) =', factor(f.subs(a, 1 + u).subs(b, 1 + u + v).subs(c, 1 + u + v + w)))

if __name__ == '__main__':
    main()