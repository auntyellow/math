from sympy import *

# ISBN 9787560349800, p303, ex 12.12 (p339, ex 14.35)

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    a, b, c = symbols('a, b, c', negative = False)
    f = sum_cyc((3*a**4 + a**2*b**2)/(a**3 + b**3), (a, b, c)) - 2*(a + b + c)
    u, v = symbols('u, v', negative = False)
    print('f(abc) =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v)))) # g
    print('f(bca) =', factor(f.subs(c, a*(1 + u)).subs(b, a*(1 + u + v))))
    # f(abc)'s numerator
    g = 2*u**10 + 7*u**9*v + 16*u**9 + 10*u**8*v**2 + 45*u**8*v + 58*u**8 + 10*u**7*v**3 + 44*u**7*v**2 + 124*u**7*v + 126*u**7 + 11*u**6*v**4 + 28*u**6*v**3 + 57*u**6*v**2 + 189*u**6*v + 180*u**6 + 10*u**5*v**5 + 36*u**5*v**4 - 11*u**5*v**3 - 29*u**5*v**2 + 171*u**5*v + 174*u**5 + 5*u**4*v**6 + 38*u**4*v**5 + 35*u**4*v**4 - 125*u**4*v**3 - 148*u**4*v**2 + 102*u**4*v + 112*u**4 + u**3*v**7 + 18*u**3*v**6 + 59*u**3*v**5 + 9*u**3*v**4 - 161*u**3*v**3 - 128*u**3*v**2 + 56*u**3*v + 44*u**3 + 3*u**2*v**7 + 25*u**2*v**6 + 59*u**2*v**5 + 27*u**2*v**4 - 42*u**2*v**3 - 14*u**2*v**2 + 30*u**2*v + 8*u**2 + 3*u*v**7 + 21*u*v**6 + 49*u*v**5 + 58*u*v**4 + 42*u*v**3 + 26*u*v**2 + 8*u*v + 2*v**7 + 10*v**6 + 22*v**5 + 28*v**4 + 20*v**3 + 8*v**2
    print('g(uv) =', factor(g.subs(v, u*(1 + v)))) # h
    print('g(vu) =', factor(g.subs(u, v*(1 + u))))
    # g(uv) = u**2*h
    h = u**8*v**7 + 12*u**8*v**6 + 61*u**8*v**5 + 171*u**8*v**4 + 289*u**8*v**3 + 302*u**8*v**2 + 188*u**8*v + 56*u**8 + 3*u**7*v**7 + 39*u**7*v**6 + 209*u**7*v**5 + 601*u**7*v**4 + 1017*u**7*v**3 + 1057*u**7*v**2 + 680*u**7*v + 228*u**7 + 3*u**6*v**7 + 46*u**6*v**6 + 272*u**6*v**5 + 810*u**6*v**4 + 1324*u**6*v**3 + 1262*u**6*v**2 + 811*u**6*v + 350*u**6 + 2*u**5*v**7 + 35*u**5*v**6 + 227*u**5*v**5 + 689*u**5*v**4 + 991*u**5*v**3 + 597*u**5*v**2 + 227*u**5*v + 252*u**5 + 10*u**4*v**6 + 109*u**4*v**5 + 422*u**4*v**4 + 637*u**4*v**3 + 171*u**4*v**2 - 195*u**4*v + 128*u**4 + 22*u**3*v**5 + 168*u**3*v**4 + 410*u**3*v**3 + 314*u**3*v**2 + 62*u**3*v + 186*u**3 + 28*u**2*v**4 + 154*u**2*v**3 + 280*u**2*v**2 + 266*u**2*v + 224*u**2 + 20*u*v**3 + 86*u*v**2 + 142*u*v + 120*u + 8*v**2 + 24*v + 24
    print('h(v>=1) =', factor(h.subs(v, 1 + v)))
    print('h(v<=1) =', factor(h.subs(v, 1/(1 + v))))

if __name__ == '__main__':
    main()