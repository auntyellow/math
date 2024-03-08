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
    n, p, q, r, s, t = symbols('n, p, q, r, s, t')
    '''
    n = 1
    g = 3*sqrt(5)*(n*x + p*y + q*z)
    h = 2*(n + p + q)*(x + y + z)
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
    pq = solve([eq2, eq3], p, q)
    print('pq =', pq)
    pq = pq[0]
    f = f.subs(p, pq[0]).subs(q, pq[1])
    U = S(100)/99
    # x <= y <= z <= U*x
    print('f(xyzU) =', factor(f.subs(z, x*(U + u)/(1 + u)).subs(y, x*(U + u + v)/(1 + u + v))))
    print('f(xzyU) =', factor(f.subs(y, x*(U + u)/(1 + u)).subs(z, x*(U + u + v)/(1 + u + v))))
    print('f(yxzU) =', factor(f.subs(z, y*(U + u)/(1 + u)).subs(x, y*(U + u + v)/(1 + u + v))))
    print('f(xyzU) =', factor(f.subs(x, y*(U + u)/(1 + u)).subs(z, y*(U + u + v)/(1 + u + v))))
    print('f(zxyU) =', factor(f.subs(y, z*(U + u)/(1 + u)).subs(x, z*(U + u + v)/(1 + u + v))))
    print('f(zyxU) =', factor(f.subs(x, z*(U + u)/(1 + u)).subs(y, z*(U + u + v)/(1 + u + v))))
    # unable to cover area near (1, 1, 1)
    print()

    # try quadratic homogeneous polynomial
    n = 1
    g = 3*sqrt(5)*(n*x**2 + p*y**2 + q*z**2 + r*x*y + s*x*z + t*y*z)
    h = 2*((n + p + q)*(x**2 + y**2 + z**2) + (r + s + t)*(x*y + x*z + y*z))
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
    st = solve([eq2, eq3], s, t)
    print('st =', st)
    st = st[0]
    f = f.subs(s, st[0]).subs(t, st[1])
    # U = 2 doesn't seem to work
    U = S(3)/2
    # x <= y <= z <= U*x
    fxyz = factor(f.subs(z, x*(U + u)/(1 + u)).subs(y, x*(U + u + v)/(1 + u + v)))
    fxzy = factor(f.subs(y, x*(U + u)/(1 + u)).subs(z, x*(U + u + v)/(1 + u + v)))
    fyxz = factor(f.subs(z, y*(U + u)/(1 + u)).subs(x, y*(U + u + v)/(1 + u + v)))
    fyzx = factor(f.subs(x, y*(U + u)/(1 + u)).subs(z, y*(U + u + v)/(1 + u + v)))
    fzxy = factor(f.subs(y, z*(U + u)/(1 + u)).subs(x, z*(U + u + v)/(1 + u + v)))
    fzyx = factor(f.subs(x, z*(U + u)/(1 + u)).subs(y, z*(U + u + v)/(1 + u + v)))
    # search possible p, q and r
    print()
    print('```python')
    print('    coeffs = [')
    for fi in [fxyz, fxzy, fyxz, fyzx, fzxy, fzyx]:
        assert fi.func == Mul
        negative = False
        expr = None
        for p in fi.args:
            if p.is_constant():
                if p < 0:
                    negative = True
                continue
            if p.func == Pow:
                if p.args[1] % 2 != 0 and '-' in str(p.args[0]):
                    raise Exception(fi, 'contains minus:', p.args[0])
                continue
            if expr != None:
                raise Exception(fi, 'contains multiple factors:', expr, p)
            expr = p
        for coeff in Poly(-expr if negative else expr, u, v).coeffs():
            print('        ' + str(coeff) + ',')
    print('    ]')
    print('```')
    print()
    # result from 4575195a.py
    p0, q0, r0 = S(1529)/840, S(179)/237, S(104)/207
    f = f.subs(p, p0).subs(q, q0).subs(r, r0)
    print('f(xyzU) =', factor(f.subs(z, x*(U + u)/(1 + u)).subs(y, x*(U + u + v)/(1 + u + v))))
    print('f(xzyU) =', factor(f.subs(y, x*(U + u)/(1 + u)).subs(z, x*(U + u + v)/(1 + u + v))))
    print('f(yxzU) =', factor(f.subs(z, y*(U + u)/(1 + u)).subs(x, y*(U + u + v)/(1 + u + v))))
    print('f(xyzU) =', factor(f.subs(x, y*(U + u)/(1 + u)).subs(z, y*(U + u + v)/(1 + u + v))))
    print('f(zxyU) =', factor(f.subs(y, z*(U + u)/(1 + u)).subs(x, z*(U + u + v)/(1 + u + v))))
    print('f(zyxU) =', factor(f.subs(x, z*(U + u)/(1 + u)).subs(y, z*(U + u + v)/(1 + u + v))))
    # we proved x <= y <= z <= 3*x/2, much weaker than radical/4575195.py (x <= y <= z <= 6*x)

if __name__ == '__main__':
    main()