from sympy import *

# https://math.stackexchange.com/a/3658031

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', positive = True)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    x, y, z = symbols('x, y, z', positive = True)
    xyz = (x + y + z)/3
    a, b, c = x/xyz, y/xyz, z/xyz
    print('a + b + c =', factor(a + b + c))
    print()

    g = 3*(6*c**2 + a**2 + b**2 + 2*a*c + 2*b*c + 4*a*b)
    h = 32*(a**2 + b**2 + c**2 + a*b + a*c + b*c)
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    f = 1/(2 + a**2 + b**2) - g/h
    u, v = symbols('u, v', positive = True)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v)))) # doesn't work
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    j = 75*u**4 + 162*u**3*v + 182*u**3 + 88*u**2*v**2 + 216*u**2*v + 108*u**2 + 4*u*v**3 + 60*u*v**2 + 72*u*v + 4*v**4 - 8*v**3 + 72*v**2
    print('j(uv) =', factor(j.subs(v, u*(1 + v)))) # doesn't work
    print('j(vu) =', factor(j.subs(u, v*(1 + u))))
    k = 4*u**2*v**4 + 20*u**2*v**3 + 124*u**2*v**2 + 366*u**2*v + 333*u**2 - 8*u*v**3 + 36*u*v**2 + 312*u*v + 450*u + 72*v**2 + 216*v + 252
    print('k =', factor(k.subs(u, 1/u)))
    k1 = 72*u**2*v**2 + 216*u**2*v + 252*u**2 - 8*u*v**3 + 36*u*v**2 + 312*u*v + 450*u + 4*v**4 + 20*v**3 + 124*v**2 + 366*v + 333
    print('k\'(uv) =', factor(k1.subs(v, u*(1 + v))))
    print('k\'(vu) =', factor(k1.subs(u, v*(1 + u))))
    print()

    g = 3*(6*c**2 + a**2 + b**2 + 4*a*b)
    h = 16*(2*a**2 + 2*b**2 + 2*c**2 + a*b + a*c + b*c)
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (a, b, c))))
    f = 1/(2 + a**2 + b**2) - g/h
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    print()

    # prove directly by buffalo-way
    f = sum_cyc(1/(2 + a**2 + b**2), (a, b, c)) - S(3)/4
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))

if __name__ == '__main__':
    main()