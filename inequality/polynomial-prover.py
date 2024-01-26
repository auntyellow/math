import logging
from sympy import *

def sign(f):
    # return 0 if sign is not determined
    u, v = symbols('u, v', negative = False)
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
    p = Poly(f, u, v)
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

# May not work if:
# 1. zero on x or y != m/2^n, e.g. (x-1/3)^2+y^2
# 2. critical point near x = y or x = 1/y (why?)
#    example: g in 4746804.py, so try x <= y and y <= x (why usually work?)

# return None if f >= 0, or the counterexample (x0, y0, f0)
# param f: 2-var function about x and y
def negative(f, x0, x1, y0, y1):
    x, y = symbols('x, y', negative = False)

    # try to find counterexample
    f0 = f.subs(x, x0).subs(y, y0)
    if f0 < 0:
        return x0, y0, f0

    # try to prove by buffalo way
    dx, dy = x1 - x0, y1 - y0
    u, v = symbols('u, v', negative = False)
    f1 = f.subs(x, x0 + dx/(1 + u)).subs(y, y0 + dy/(1 + v))
    f1 = factor(f1)
    s = sign(f1)
    if s > 0:
        logging.info('non_negative: [{},{},{},{}], f={}'.format(x0, x1, y0, y1, f0))
        return None
    elif s < 0:
        logging.warn('should be negative: f={}<0'.format(f1))

    logging.info('try_dividing: [{},{},{},{}], f={}'.format(x0, x1, y0, y1, f0))

    # divide
    if dx < dy:
        ym = y0 + dy/S(2)
        n = negative(f, x0, x1, ym, y1)
        if n != None:
            return n
        return negative(f, x0, x1, y0, ym)
    xm = x0 + dx/S(2)
    n = negative(f, xm, x1, y0, y1)
    if n != None:
        return n
    return negative(f, x0, xm, y0, y1)

def inverse(f, *vars):
    f1 = f
    logging.info('before inverse: {}'.format(f1))
    for var in vars:
        f1 = factor(f1.subs(var, 1/var))*var**Poly(f1, var).degree()
        logging.info('after inverse about {}: {}'.format(var, f1))
    return f1

# return '' if f >= 0, or the counterexample
# param f: 2-var function about x and y
def negative_oo(f):
    x, y = symbols('x, y', negative = False)
    n = negative(f, 0, 1, 0, 1)
    if n != None:
        x0, y0, f0 = n
        return 'f({},{})={}'.format(x0, y0, f0)
    n = negative(inverse(f, x), 0, 1, 0, 1)
    if n != None:
        x0, y0, f0 = n
        return 'f({},{})={}'.format(1/x0, y0, f0)
    n = negative(inverse(f, y), 0, 1, 0, 1)
    if n != None:
        x0, y0, f0 = n
        return 'f({},{})={}'.format(y0, 1/y0, f0)
    n = negative(inverse(f, x, y), 0, 1, 0, 1)
    if n != None:
        x0, y0, f0 = n
        return 'f({},{})={}'.format(1/x0, 1/y0, f0)
    return ''

def main():
    logging.basicConfig(level = 'INFO')
    x, y = symbols('x, y', negative = False)
    # https://math.stackexchange.com/q/3831395
    f = x**5 - x**3/2 - x + S(4)/5
    # https://math.stackexchange.com/q/83670
    f = x**8 - x**7 + 2*x**6 - 2*x**5 + 3*x**4 - 3*x**3 + 4*x**2 - 4*x + S(5)/2
    # https://math.stackexchange.com/q/4765187
    f = (1 + x)**7 - 7**(S(7)/3)*x**4
    # ISBN 9787030207210, p156, §7.1
    z = x
    f = 10195920*z**8 + 2109632*z**7 - 5387520*z**6 + 1361336*z**5 + 61445*z**4 - 52468*z**3 + 6350*z**2 - 300*z + 5
    u, v = x, y
    # https://math.stackexchange.com/q/1775572
    f = 65*u**10 + 215*u**9*v + 546*u**9 + 285*u**8*v**2 + 1503*u**8*v + 1989*u**8 + 275*u**7*v**3 + 1488*u**7*v**2 + 4284*u**7*v + 4095*u**7 + 315*u**6*v**4 + 1061*u**6*v**3 + 2436*u**6*v**2 + 6093*u**6*v + 5226*u**6 + 285*u**5*v**5 + 1290*u**5*v**4 + 591*u**5*v**3 - 441*u**5*v**2 + 4029*u**5*v + 4329*u**5 + 135*u**4*v**6 + 1185*u**4*v**5 + 1725*u**4*v**4 - 3020*u**4*v**3 - 5898*u**4*v**2 + 570*u**4*v + 2392*u**4 + 25*u**3*v**7 + 500*u**3*v**6 + 1890*u**3*v**5 + 779*u**3*v**4 - 5556*u**3*v**3 - 6582*u**3*v**2 - 326*u**3*v + 858*u**3 + 75*u**2*v**7 + 690*u**2*v**6 + 1866*u**2*v**5 + 762*u**2*v**4 - 2778*u**2*v**3 - 2400*u**2*v**2 + 192*u**2*v + 156*u**2 + 75*u*v**7 + 636*u*v**6 + 1617*u*v**5 + 1527*u*v**4 + 318*u*v**3 + 114*u*v**2 + 156*u*v + 65*v**7 + 351*v**6 + 741*v**5 + 754*v**4 + 390*v**3 + 156*v**2
    # https://math.stackexchange.com/q/4850712
    # from 4850712u.py
    # m, n = 5, 13, non-negative, https://math.stackexchange.com/q/1777075
    f = 90*u**7 + 190*u**6*v + 396*u**6 + 120*u**5*v**2 + 542*u**5*v + 630*u**5 + 55*u**4*v**3 + 41*u**4*v**2 + 164*u**4*v + 504*u**4 + 60*u**3*v**4 - 40*u**3*v**3 - 824*u**3*v**2 - 416*u**3*v + 252*u**3 + 25*u**2*v**5 + 115*u**2*v**4 - 332*u**2*v**3 - 984*u**2*v**2 - 156*u**2*v + 72*u**2 + 50*u*v**5 + 206*u*v**4 - 64*u*v**3 - 192*u*v**2 + 72*u*v + 90*v**5 + 216*v**4 + 108*v**3 + 72*v**2
    # m, n = 63, 164, non-negative
    f = 14301*u**7 + 30177*u**6*v + 62879*u**6 + 19026*u**5*v**2 + 85942*u**5*v + 99880*u**5 + 8694*u**4*v**3 + 6242*u**4*v**2 + 25434*u**4*v + 79677*u**4 + 9513*u**3*v**4 - 6552*u**3*v**3 - 131640*u**3*v**2 - 66962*u**3*v + 39725*u**3 + 3969*u**2*v**5 + 18207*u**2*v**4 - 53157*u**2*v**3 - 157193*u**2*v**2 - 25281*u**2*v + 11350*u**2 + 7938*u*v**5 + 32639*u*v**4 - 10554*u*v**3 - 30956*u*v**2 + 11350*u*v + 14301*v**5 + 34277*v**4 + 17025*v**3 + 11350*v**2
    # m, n = 121, 315, negative
    # f = 52756*u**7 + 111320*u**6*v + 231952*u**6 + 70180*u**5*v**2 + 317010*u**5*v + 368420*u**5 + 32065*u**4*v**3 + 22985*u**4*v**2 + 93730*u**4*v + 293864*u**4 + 35090*u**3*v**4 - 24200*u**3*v**3 - 485724*u**3*v**2 - 247152*u**3*v + 146496*u**3 + 14641*u**2*v**5 + 67155*u**2*v**4 - 196156*u**2*v**3 - 580008*u**2*v**2 - 93336*u**2*v + 41856*u**2 + 29282*u*v**5 + 120390*u*v**4 - 38992*u*v**3 - 114264*u*v**2 + 41856*u*v + 52756*v**5 + 126440*v**4 + 62784*v**3 + 41856*v**2
    print('[' + negative_oo(f) + ']')

if __name__ == '__main__':
    main()