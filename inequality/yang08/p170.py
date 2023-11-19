from sympy import *

# ISBN 9787030207210, p170, §7.3.3

def main():
    a1, a2, a3, a4 = symbols('a1, a2, a3, a4', positive = True)
    f = a1/(a2 + a3) + a2/(a3 + a4) + a3/(a4 + a1) + a4/(a1 + a2) - 2
    u, v, w = symbols('u, v, w', positive = True)
    print('f(1234) =', factor(f.subs(a2, a1*(1 + u)).subs(a3, a1*(1 + u + v)).subs(a4, a1*(1 + u + v + w))))
    print('f(1243) =', factor(f.subs(a2, a1*(1 + u)).subs(a4, a1*(1 + u + v)).subs(a3, a1*(1 + u + v + w))))
    print('f(1324) =', factor(f.subs(a3, a1*(1 + u)).subs(a2, a1*(1 + u + v)).subs(a4, a1*(1 + u + v + w))))
    print('f(1342) =', factor(f.subs(a3, a1*(1 + u)).subs(a4, a1*(1 + u + v)).subs(a2, a1*(1 + u + v + w))))
    print('f(1423) =', factor(f.subs(a4, a1*(1 + u)).subs(a2, a1*(1 + u + v)).subs(a3, a1*(1 + u + v + w))))
    print('f(1432) =', factor(f.subs(a4, a1*(1 + u)).subs(a3, a1*(1 + u + v)).subs(a2, a1*(1 + u + v + w))))
    # f(1342)'s numerator
    g = 2*u**4 + 3*u**3*v + u**3*w + 6*u**3 + u**2*v**2 - u**2*v*w + 4*u**2*v + 2*u**2*w**2 + u**2*w + 4*u**2 - u*v**2*w + 2*u*v*w**2 - 2*u*v*w + u*w**3 + 5*u*w**2 + v**2*w**2 + v*w**3 + 4*v*w**2 + 2*w**3 + 4*w**2
    s, t = symbols('s, t', positive = True)
    print('g(uvw) =', factor(g.subs(v, u*(1 + s)).subs(w, u*(1 + s + t))))
    print('g(uwv) =', factor(g.subs(w, u*(1 + s)).subs(v, u*(1 + s + t))))
    print('g(vuw) =', factor(g.subs(u, v*(1 + s)).subs(w, v*(1 + s + t))))
    print('g(vwu) =', factor(g.subs(w, v*(1 + s)).subs(u, v*(1 + s + t))))
    print('g(wuv) =', factor(g.subs(u, w*(1 + s)).subs(v, w*(1 + s + t))))
    print('g(wvu) =', factor(g.subs(v, w*(1 + s)).subs(u, w*(1 + s + t))))

if __name__ == '__main__':
    main()