from sympy import *

# ISBN 9787030207210, p171, §7.3.3, ex 8

def main():
    x, y, z = symbols('x, y, z', positive = True)
    f = x**4*y**2 - 2*x**4*y*z + x**4*z**2 + 3*x**3*y**2*z - 2*x**3*y*z**2 - 2*x**2*y**4 - 2*x**2*y**3*z + x**2*y**2*z**2 + 2*x*y**4*z + y**6
    u, v = symbols('u, v', positive = True)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(xzy) =', factor(f.subs(z, x*(1 + u)).subs(y, x*(1 + u + v))))
    print('f(yxz) =', factor(f.subs(x, y*(1 + u)).subs(z, y*(1 + u + v)))) # *
    # equality occurs when u = v = 1/2
    print('f(yzx) =', factor(f.subs(z, y*(1 + u)).subs(x, y*(1 + u + v))))
    print('f(zxy) =', factor(f.subs(x, z*(1 + u)).subs(y, z*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v)))) # *

    # f(yzx)
    g = u**6 + 4*u**5*v + 2*u**5 + 6*u**4*v**2 + 6*u**4*v + 4*u**3*v**3 + 6*u**3*v**2 - u**3*v - 2*u**3 + u**2*v**4 + 2*u**2*v**3 - 2*u**2*v**2 - 3*u**2*v - u**2 - u*v**3 - u*v + v**3 - v + 1
    s2 = S(1)/2
    print('g(1/2,1/2) =', factor(g.subs(u, s2).subs(v, s2)))
    s, t = symbols('s, t', positive = True)
    print('g(uv2) =', factor(g.subs(u, s2/(1 + s + t)).subs(v, s2/(1 + s))))
    print('g(vu2) =', factor(g.subs(v, s2/(1 + s + t)).subs(u, s2/(1 + s))))
    print('g(u2v) =', factor(g.subs(u, s2/(1 + s)).subs(v, s2*(1 + t))))
    print('g(v2u) =', factor(g.subs(v, s2/(1 + s)).subs(u, s2*(1 + t))))
    print('g(2uv) =', factor(g.subs(u, s2*(1 + s)).subs(v, s2*(1 + s + t))))
    print('g(2vu) =', factor(g.subs(v, s2*(1 + s)).subs(u, s2*(1 + s + t))))
    # g(u2v)
    h1 = 8*s**6*t**3 + 24*s**6*t**2 - 8*s**6*t + 40*s**6 + 44*s**5*t**3 + 132*s**5*t**2 - 76*s**5*t + 220*s**5 + s**4*t**4 + 108*s**4*t**3 + 310*s**4*t**2 - 284*s**4*t + 457*s**4 + 4*s**3*t**4 + 156*s**3*t**3 + 424*s**3*t**2 - 504*s**3*t + 424*s**3 + 6*s**2*t**4 + 140*s**2*t**3 + 378*s**2*t**2 - 424*s**2*t + 148*s**2 + 4*s*t**4 + 72*s*t**3 + 208*s*t**2 - 136*s*t + t**4 + 16*t**3 + 52*t**2
    # g(v2u)
    h2 = s**4*t**6 + 10*s**4*t**5 + 35*s**4*t**4 + 44*s**4*t**3 - 9*s**4*t**2 - 54*s**4*t + 37*s**4 + 4*s**3*t**6 + 44*s**3*t**5 + 172*s**3*t**4 + 260*s**3*t**3 + 40*s**3*t**2 - 224*s**3*t + 88*s**3 + 6*s**2*t**6 + 72*s**2*t**5 + 312*s**2*t**4 + 552*s**2*t**3 + 238*s**2*t**2 - 304*s**2*t + 52*s**2 + 4*s*t**6 + 52*s*t**5 + 248*s*t**4 + 504*s*t**3 + 336*s*t**2 - 136*s*t + t**6 + 14*t**5 + 73*t**4 + 168*t**3 + 148*t**2
    print('h1(st) =', factor(h1.subs(t, s*(1 + t)))) # *
    print('h1(ts) =', factor(h1.subs(s, t*(1 + s)))) # *
    print('h2(st) =', factor(h2.subs(t, s*(1 + t))))
    print('h2(ts) =', factor(h2.subs(s, t*(1 + s)))) # *
    # * proved by polynomial-prover

if __name__ == '__main__':
    main()