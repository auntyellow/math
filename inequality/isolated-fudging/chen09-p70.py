from sympy import *

# ISBN 9787542848482, p68, §2.4, ex9
# sum_cyc(sqrt(1 + 48*x/(y + z))) >= 15

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    x, y, z = symbols('x, y, z', negative = False)
    f0 = sqrt(1 + 48*x/(y + z))
    m, n, p, q, r, s, t = symbols('m, n, p, q, r, s, t')
    n = 1
    g = 15*(n*x**2 + m*(y**2 + z**2) + p*(x*y + x*z) + q*y*z)
    h = (n + 2*m)*(x**2 + y**2 + z**2) + (2*p + q)*(x*y + x*z + y*z)
    print('sum_cyc(g/h) =', cancel(sum_cyc(g/h, (x, y, z))))
    f = f0**2 - (g/h)**2
    # f >= 0 if sum_cyc(f0) >= 15
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(x, 1).subs(y, 1).subs(z, 1), 0)
    s32 = S(3)/2
    # f(3/2,3/2,0) = 0
    eq2 = Eq(f.subs(x, s32).subs(y, s32).subs(z, 0), 0)
    # f(3/2,0,3/2) = 0
    eq3 = Eq(f.subs(x, s32).subs(y, 0).subs(z, s32), 0)
    # f(0,3/2,3/2) = 0
    eq4 = Eq(f.subs(x, 0).subs(y, s32).subs(z, s32), 0)
    # f_a,b(1,1,1) = 0
    eq5 = Eq(diff(f.subs(z, 3 - x - y), x).subs(x, 1).subs(y, 1), 0)
    eq6 = Eq(diff(f.subs(z, 3 - x - y), y).subs(x, 1).subs(y, 1), 0)
    # f_a(3/2,3/2,0) = 0
    eq7 = Eq(diff(f.subs(z, 0).subs(y, 3 - x), x).subs(x, s32), 0)
    # f_a(3/2,0,3/2) = 0
    eq8 = Eq(diff(f.subs(y, 0).subs(z, 3 - x), x).subs(x, s32), 0)
    # f_b(0,3/2,3/2) = 0
    eq9 = Eq(diff(f.subs(x, 0).subs(z, 3 - y), y).subs(y, s32), 0)
    print('eq1:', factor(eq1)) # True
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3)) # = eq2
    print('eq4:', factor(eq4))
    print('eq5:', factor(eq5))
    print('eq6:', factor(eq6)) # True
    print('eq7:', factor(eq7))
    print('eq8:', factor(eq8)) # = eq7
    print('eq9:', factor(eq9)) # True
    mpq = solve([eq2, eq4, eq5, eq7], (m, p, q))
    print('mpq =', mpq)
    mpq = mpq[0]
    f = f.subs(m, mpq[0]).subs(p, mpq[1]).subs(q, mpq[2])
    u, v = symbols('u, v', negative = False)
    # doesn't hold
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    print('f(1,1,100) =', f.subs(x, 1).subs(y, 1).subs(z, 100))
    print()

    # try cubic homogeneous polynomial
    g = 15*(n*x**3 + p*(x**2*y + x**2*z) + q*(x*y**2 + x*z**2) + r*(y**2*z + y*z**2) + s*(y**3 + z**3) + t*x*y*z)
    h = (n + 2*s)*(x**3 + y**3 + z**3) + (p + q + r)*(x**2*y + x**2*z + x*y**2 + x*z**2 + y**2*z + y*z**2) + 3*t*x*y*z
    # factor(sum_cyc(...)) is too slow
    print('sum_cyc(g/h) =', cancel(sum_cyc(g/h, (x, y, z))))
    f = f0**2 - (g/h)**2
    # f(1,1,1) = 0
    eq1 = Eq(f.subs(x, 1).subs(y, 1).subs(z, 1), 0)
    # f(3/2,3/2,0) = 0
    eq2 = Eq(f.subs(x, s32).subs(y, s32).subs(z, 0), 0)
    # f(3/2,0,3/2) = 0
    eq3 = Eq(f.subs(x, s32).subs(y, 0).subs(z, s32), 0)
    # f(0,3/2,3/2) = 0
    eq4 = Eq(f.subs(x, 0).subs(y, s32).subs(z, s32), 0)
    # f_a,b(1,1,1) = 0
    eq5 = Eq(diff(f.subs(z, 3 - x - y), x).subs(x, 1).subs(y, 1), 0)
    eq6 = Eq(diff(f.subs(z, 3 - x - y), y).subs(x, 1).subs(y, 1), 0)
    # f_a(3/2,3/2,0) = 0
    eq7 = Eq(diff(f.subs(z, 0).subs(y, 3 - x), x).subs(x, s32), 0)
    # f_a(3/2,0,3/2) = 0
    eq8 = Eq(diff(f.subs(y, 0).subs(z, 3 - x), x).subs(x, s32), 0)
    # f_b(0,3/2,3/2) = 0
    eq9 = Eq(diff(f.subs(x, 0).subs(z, 3 - y), y).subs(y, s32), 0)
    print('eq1:', factor(eq1)) # True
    print('eq2:', factor(eq2))
    print('eq3:', factor(eq3)) # = eq2
    print('eq4:', factor(eq4))
    print('eq5:', factor(eq5))
    print('eq6:', factor(eq6)) # True
    print('eq7:', factor(eq7))
    print('eq8:', factor(eq8)) # = eq7
    print('eq9:', factor(eq9)) # True
    pqr = solve([eq2, eq4, eq5, eq7], (p, q, r))
    print('pqr =', pqr)
    pqr = pqr[0]

if __name__ == '__main__':
    main()