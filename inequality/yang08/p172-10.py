from sympy import *

# ISBN 9787030207210, p172, §7.3.3, ex 10

def main():
    a, b, c = symbols('a, b, c', negative = False)
    f = a*(a + b)**5 + b*(c + b)**5 + c*(a + c)**5
    u, v = symbols('u, v', negative = False)
    print('f(++-,abc) =', factor(f.subs(c, -c).subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    print('f(++-,acb) =', factor(f.subs(c, -c).subs(c, a*(1 + u)).subs(b, a*(1 + u + v))))
    print('f(++-,bac) =', factor(f.subs(c, -c).subs(a, b*(1 + u)).subs(c, b*(1 + u + v))))
    print('f(++-,bca) =', factor(f.subs(c, -c).subs(c, b*(1 + u)).subs(a, b*(1 + u + v))))
    print('f(++-,cab) =', factor(f.subs(c, -c).subs(a, c*(1 + u)).subs(b, c*(1 + u + v))))
    print('f(++-,cba) =', factor(f.subs(c, -c).subs(b, c*(1 + u)).subs(a, c*(1 + u + v))))
    # f(++-,bac)
    g1 = u**6 + 10*u**5 - 5*u**4*v + 50*u**4 - 10*u**3*v**2 + 120*u**3 - 10*u**2*v**3 + 160*u**2 + u*v**5 - 5*u*v**4 + 112*u + v**6 + 32
    print('g1(uv) =', factor(g1.subs(v, u*(1 + v))))
    print('g1(vu) =', factor(g1.subs(u, v*(1 + u)))) # *
    # g1(uv)
    h1 = u**6*v**6 + 7*u**6*v**5 + 20*u**6*v**4 + 30*u**6*v**3 + 25*u**6*v**2 + 11*u**6*v + 3*u**6 - 5*u**5*v**4 - 30*u**5*v**3 - 70*u**5*v**2 - 75*u**5*v - 20*u**5 + 50*u**4 + 120*u**3 + 160*u**2 + 112*u + 32
    print('h1(uv) =', factor(h1.subs(u, 1/u).subs(v, u*(1 + v)))) # *
    print('h1(vu) =', factor(h1.subs(u, 1/u).subs(u, v*(1 + u))))
    # h1(vu)
    j1 = 32*u**6*v**6 + 192*u**5*v**6 + 112*u**5*v**5 + 480*u**4*v**6 + 560*u**4*v**5 + 160*u**4*v**4 + 640*u**3*v**6 + 1120*u**3*v**5 + 640*u**3*v**4 + 120*u**3*v**3 + 480*u**2*v**6 + 1120*u**2*v**5 + 960*u**2*v**4 + 360*u**2*v**3 + 50*u**2*v**2 + 192*u*v**6 + 555*u*v**5 + 610*u*v**4 + 290*u*v**3 + 25*u*v**2 - 20*u*v + 33*v**6 + 114*v**5 + 150*v**4 + 80*v**3 - 9*v + 3
    print('j1(uv) =', factor(j1.subs(u, 1/u).subs(v, u*(1 + v))))
    print('j1(vu) =', factor(j1.subs(u, 1/u).subs(u, v*(1 + u)))) # *
    print()

    print('f(+--,abc) =', factor(f.subs(b, -b).subs(c, -c).subs(b, a*(1 + u)).subs(c, a*(1 + u + v))))
    print('f(+--,acb) =', factor(f.subs(b, -b).subs(c, -c).subs(c, a*(1 + u)).subs(b, a*(1 + u + v))))
    print('f(+--,bac) =', factor(f.subs(b, -b).subs(c, -c).subs(a, b*(1 + u)).subs(c, b*(1 + u + v))))
    print('f(+--,bca) =', factor(f.subs(b, -b).subs(c, -c).subs(c, b*(1 + u)).subs(a, b*(1 + u + v))))
    print('f(+--,cab) =', factor(f.subs(b, -b).subs(c, -c).subs(a, c*(1 + u)).subs(b, c*(1 + u + v))))
    print('f(+--,cba) =', factor(f.subs(b, -b).subs(c, -c).subs(b, c*(1 + u)).subs(a, c*(1 + u + v))))
    # f(+--,cba)
    g2 = u**6 + 10*u**5 - 5*u**4*v + 50*u**4 - 10*u**3*v**2 + 120*u**3 - 10*u**2*v**3 + 160*u**2 + u*v**5 - 5*u*v**4 + 112*u + v**6 + 32
    print('g2(uv) =', factor(g2.subs(v, u*(1 + v))))
    print('g2(vu) =', factor(g2.subs(u, v*(1 + u)))) # *
    h2 = u**6*v**6 + 7*u**6*v**5 + 20*u**6*v**4 + 30*u**6*v**3 + 25*u**6*v**2 + 11*u**6*v + 3*u**6 - 5*u**5*v**4 - 30*u**5*v**3 - 70*u**5*v**2 - 75*u**5*v - 20*u**5 + 50*u**4 + 120*u**3 + 160*u**2 + 112*u + 32
    print('h2(uv) =', factor(h2.subs(u, 1/u).subs(v, u*(1 + v)))) # *
    print('h2(vu) =', factor(h2.subs(u, 1/u).subs(u, v*(1 + u))))
    # h2(vu)
    j2 = 32*u**6*v**6 + 192*u**5*v**6 + 112*u**5*v**5 + 480*u**4*v**6 + 560*u**4*v**5 + 160*u**4*v**4 + 640*u**3*v**6 + 1120*u**3*v**5 + 640*u**3*v**4 + 120*u**3*v**3 + 480*u**2*v**6 + 1120*u**2*v**5 + 960*u**2*v**4 + 360*u**2*v**3 + 50*u**2*v**2 + 192*u*v**6 + 555*u*v**5 + 610*u*v**4 + 290*u*v**3 + 25*u*v**2 - 20*u*v + 33*v**6 + 114*v**5 + 150*v**4 + 80*v**3 - 9*v + 3
    print('j2(uv) =', factor(j2.subs(u, 1/u).subs(v, u*(1 + v))))
    print('j2(vu) =', factor(j2.subs(u, 1/u).subs(u, v*(1 + u)))) # *
    # * proved by polynomial-prover

if __name__ == '__main__':
    main()