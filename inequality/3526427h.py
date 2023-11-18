from sympy import *

# https://math.stackexchange.com/q/3526427

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', positive = True)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    x, y, z = symbols('x, y, z', positive = True)
    f = sum_cyc((x + y)**2*x**2/(x**2 + y**2)**2, (x, y, z)) - 3
    print('f(xyz) =', factor(f.subs(y, x + y).subs(z, x + y + z)))
    print('f(xzy) =', factor(f.subs(z, x + z).subs(y, x + y + z)))
    # result in f(xzy)
    g = 32*x**10*y**2 + 32*x**10*y*z + 32*x**10*z**2 + 96*x**9*y**3 + 192*x**9*y**2*z + 224*x**9*y*z**2 + 224*x**9*z**3 + 144*x**8*y**4 + 384*x**8*y**3*z + 432*x**8*y**2*z**2 + 768*x**8*y*z**3 + 720*x**8*z**4 + 128*x**7*y**5 + 448*x**7*y**4*z + 384*x**7*y**3*z**2 + 512*x**7*y**2*z**3 + 1728*x**7*y*z**4 + 1408*x**7*z**5 + 72*x**6*y**6 + 328*x**6*y**5*z + 252*x**6*y**4*z**2 - 416*x**6*y**3*z**3 + 588*x**6*y**2*z**4 + 2792*x**6*y*z**5 + 1864*x**6*z**6 + 24*x**5*y**7 + 152*x**5*y**6*z + 160*x**5*y**5*z**2 - 640*x**5*y**4*z**3 - 1152*x**5*y**3*z**4 + 1088*x**5*y**2*z**5 + 3296*x**5*y*z**6 + 1752*x**5*z**7 + 4*x**4*y**8 + 40*x**4*y**7*z + 84*x**4*y**6*z**2 - 248*x**4*y**5*z**3 - 1080*x**4*y**4*z**4 - 728*x**4*y**3*z**5 + 1688*x**4*y**2*z**6 + 2816*x**4*y*z**7 + 1188*x**4*z**8 + 4*x**3*y**8*z + 24*x**3*y**7*z**2 - 4*x**3*y**6*z**3 - 276*x**3*y**5*z**4 - 524*x**3*y**4*z**5 + 228*x**3*y**3*z**6 + 1624*x**3*y**2*z**7 + 1700*x**3*y*z**8 + 576*x**3*z**9 + 3*x**2*y**8*z**2 + 16*x**2*y**7*z**3 + 20*x**2*y**6*z**4 - 10*x**2*y**5*z**5 + 96*x**2*y**4*z**6 + 548*x**2*y**3*z**7 + 935*x**2*y**2*z**8 + 692*x**2*y*z**9 + 192*x**2*z**10 + 2*x*y**8*z**3 + 14*x*y**7*z**4 + 42*x*y**6*z**5 + 88*x*y**5*z**6 + 174*x*y**4*z**7 + 286*x*y**3*z**8 + 302*x*y**2*z**9 + 172*x*y*z**10 + 40*x*z**11 + y**8*z**4 + 6*y**7*z**5 + 17*y**6*z**6 + 32*y**5*z**7 + 47*y**4*z**8 + 54*y**3*z**9 + 43*y**2*z**10 + 20*y*z**11 + 4*z**12
    print('g(xyz) =', expand(g.subs(y, x + y).subs(z, x + y + z)))
    print('g(xzy) =', expand(g.subs(z, x + z).subs(y, x + y + z)))
    print('g(yxz) =', expand(g.subs(x, x + y).subs(z, x + y + z)))
    print('g(yzx) =', expand(g.subs(z, y + z).subs(x, x + y + z)))
    print('g(zxy) =', expand(g.subs(x, x + z).subs(y, x + y + z)))
    print('g(zyx) =', expand(g.subs(y, y + z).subs(x, x + y + z)))

if __name__ == '__main__':
    main()