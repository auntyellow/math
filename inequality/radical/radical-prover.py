import logging
from sympy import *

def sign(f):
    # return 0 if sign is not determined
    u, v, w = symbols('u, v, w', negative = False)
    if f.func == Pow:
        return sign(f.args[0])**f.args[1]
    if f.func == Mul:
        s = 1
        for p in f.args:
            s0 = sign(p)
            if s0 == 0:
                return 0
            s *= s0
        return s
    p = Poly(f, u, v, w)
    pos = false
    neg = false
    for coef in p.coeffs():
        if coef > 0:
            if neg:
                return 0
            pos = true
        elif coef < 0:
            if pos:
                return 0
            neg = true
    return 1 if pos else (-1 if neg else 0)

def subs2(f, x0, y0):
    x, y = symbols('x, y', negative = False)
    f0 = f.subs(x, x0).subs(y, y0)
    # ambiguous: y*(x + 1)**2/(9*x**2*y + 8*x**2 + 2*x*y + y)
    if f.subs(y, y0).subs(x, x0) == f0:
        return f0
    if x0 == y0:
        return factor(f.subs(y, x)).subs(x, x0)
    raise Exception('{} is ambiguous at ({}, {})'.format(f, x0, y0))

def negative(f, x0, x1, y0, y1):
    x, y = symbols('x, y', negative = False)

    # try to find counterexample
    f0 = f.subs(x, x0).subs(y, y0)
    if f0 < 0:
        return 'f({},{})={}'.format(x0, y0, f0)

    if f.func != Add:
        raise Exception('{} has no radicals'.format(f))
    # replace power with linear
    f1 = 0
    for p in f.args:
        if p.func != Pow or p.args[1] >= 1:
            f1 += p
            continue
        exp = p.args[1]
        t = p.args[0]
        # find a linear function s = m*t + n <= t**exp
        t0, t1 = t.subs(x, x0), t.subs(x, x1)
        t00, t01, t10, t11 = subs2(t, x0, y0), subs2(t, x0, y1), subs2(t, x1, y0), subs2(t, x1, y1)
        s00, s01, s10, s11 = t00**exp, t01**exp, t10**exp, t11**exp
        pairs = [(t00, s00), (t01, s01), (t10, s10), (t11, s11)]
        pairs.sort(key = lambda pair : pair[1])
        t0, s0 = pairs[0]
        t1, s1 = pairs[3]
        # | t0 s0 1 |
        # | t1 s1 1 | = t0*s1 - s0*t1 + t1*s - s1*t + s0*t - t0*s = 0
        # | t  s  1 |
        f1 += (t0*s1 - s0*t1 - s1*t + s0*t)/(t0 - t1)

    # try to prove by buffalo way
    dx, dy = x1 - x0, y1 - y0
    u, v = symbols('u, v', negative = False)
    f1 = f1.subs(x, x0 + dx/(1 + u)).subs(y, y0 + dy/(1 + v))
    f1 = factor(f1)
    s = sign(f1)
    if s > 0:
        logging.info('non_negative: [{},{},{},{}], f={}'.format(x0, x1, y0, y1, f0))
        return ''
    elif s < 0:
        return 'f={}<0'.format(f1)

    logging.info('try_dividing: [{},{},{},{}], f={}'.format(x0, x1, y0, y1, f0))

    # divide
    xm = x0 + dx/S(2)
    ym = y0 + dy/S(2)
    n = negative(f, xm, x1, ym, y1)
    if n != '':
        return n
    n = negative(f, x0, xm, ym, y1)
    if n != '':
        return n
    n = negative(f, xm, x1, y0, ym)
    if n != '':
        return n
    return negative(f, x0, xm, y0, ym)

def main():
    logging.basicConfig(level = 'INFO')
    x, y = symbols('x, y', negative = False)
    u, v = x, y
    # imo-2001-2
    # f(1/u,v)
    f = sqrt(u/(8*u*v + 9*u + 8*v + 8)) + sqrt((u + 1)**2/(8*u**2*v + 9*u**2 + 2*u + 1)) + sqrt(u*(v + 1)**2/(u*v**2 + 2*u*v + 9*u + 8)) - 1
    print('[' + negative(f, 0, 6/S(11), 0, S(11)/6) + ']')
    # f(u,1/v)
    f = sqrt(v/(8*u*v + 8*u + 9*v + 8)) + sqrt((v + 1)**2/(8*u*v**2 + 9*v**2 + 2*v + 1)) + sqrt(v*(u + 1)**2/(u**2*v + 2*u*v + 9*v + 8)) - 1
    print('[' + negative(f, 0, S(11)/6, 0, 6/S(11)) + ']')
    # f(1/u,1/v)
    f = sqrt(u*v/(9*u*v + 8*u + 8*v + 8)) + sqrt(u*(v + 1)**2/(9*u*v**2 + 2*u*v + u + 8*v**2)) + sqrt(v*(u + 1)**2/(9*u**2*v + 8*u**2 + 2*u*v + v)) - 1
    print('[' + negative(f, 0, 6/S(11), 0, 6/S(11)) + ']')

if __name__ == '__main__':
    main()