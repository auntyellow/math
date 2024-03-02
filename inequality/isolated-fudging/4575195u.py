from sympy import *

# https://math.stackexchange.com/q/4575195

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    x, y, z, u, v = symbols('x, y, z, u, v', negative = False)
    f2 = (4*x**2 + y**2)/(3*x**2 + y*z)
    p, q, r = symbols('p, q, r')
    p = 1
    g = 3*sqrt(5)*(p*x + q*y + r*z)
    h = 2*(p + q + r)*(x + y + z)
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (x, y, z))))
    f = f2 - (g/h)**2
    # f(1,1,1) = 0
    eq1 = f.subs(x, 1).subs(y, 1).subs(z, 1)
    # homogeneous, hence assume x + y + z = 3
    # f_x,y(1,1) = 0
    eq2 = diff(f.subs(z, 3 - x - y), x).subs(x, 1).subs(y, 1)
    eq3 = diff(f.subs(z, 3 - x - y), y).subs(x, 1).subs(y, 1)
    print('eq1:', factor(eq1), '= 0') # True
    print('eq2:', factor(eq2), '= 0')
    print('eq3:', factor(eq3), '= 0')
    qr = solve([eq2, eq3], q, r)
    print('qr =', qr)
    qr = qr[0]
    f = f.subs(q, qr[0]).subs(r, qr[1])
    U = S(100)/99
    # x <= y <= z <= U*x
    print('f(xyzU) =', factor(f.subs(z, x*(U + u)/(1 + u)).subs(y, x*(U + u + v)/(1 + u + v))))
    print('f(xzyU) =', factor(f.subs(y, x*(U + u)/(1 + u)).subs(z, x*(U + u + v)/(1 + u + v))))
    print('f(yxzU) =', factor(f.subs(z, y*(U + u)/(1 + u)).subs(x, y*(U + u + v)/(1 + u + v))))
    print('f(xyzU) =', factor(f.subs(x, y*(U + u)/(1 + u)).subs(z, y*(U + u + v)/(1 + u + v))))
    print('f(zxyU) =', factor(f.subs(y, z*(U + u)/(1 + u)).subs(x, z*(U + u + v)/(1 + u + v))))
    print('f(zyxU) =', factor(f.subs(z, z*(U + u)/(1 + u)).subs(y, z*(U + u + v)/(1 + u + v))))
    # unable to cover area near (1, 1, 1)

if __name__ == '__main__':
    main()