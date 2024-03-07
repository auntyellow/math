from sympy import *

# https://math.stackexchange.com/q/4261358

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    x, y, z = symbols('x, y, z', negative = False)
    xyz = (x + y + z)/3
    a, b, c = x/xyz, y/xyz, z/xyz
    print('a + b + c =', factor(a + b + c))
    f3 = a/(a*b + b*c + c*a)**3

    m, n, p, q = symbols('m, n, p, q')
    n = 1
    g = n*x + m*(y + z)
    h = (n + 2*m)*(x + y + z)
    print('sum_cyc(g/h) =', factor(sum_cyc(g/h, (x, y, z))))
    f = f3 - (g/h)**3
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(x, 1).subs(y, 1).subs(z, 1), 0)
    # homogeneous, hence assume x + y + z = 3
    # f_x,y(1,1) = 0
    eq2 = Eq(diff(f.subs(z, 3 - x - y), x).subs(x, 1).subs(y, 1), 0)
    eq3 = Eq(diff(f.subs(z, 3 - x - y), y).subs(x, 1).subs(y, 1), 0)
    print('eq1:', factor(eq1)) # True
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3)) # True
    m0 = solve(eq2, m)
    print('m =', m0)
    m0 = m0[0]
    f = f.subs(m, m0)
    u, v = symbols('u, v', negative = False)
    # U = 5 doesn't work
    U = 4
    # x <= y <= z <= U*a
    # too slow
    print('f(xyzU) =', factor(f.subs({z: x*(U + u)/(1 + u), y: x*(U + u + v)/(1 + u + v)})))
    print('f(zyxU) =', factor(f.subs({x: z*(U + u)/(1 + u), y: z*(U + u + v)/(1 + u + v)})))
    print('f(yxzU) =', factor(f.subs({z: y*(U + u)/(1 + u), x: y*(U + u + v)/(1 + u + v)})))

if __name__ == '__main__':
    main()