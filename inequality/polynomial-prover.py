import logging
from sympy import *

def sign(f):
    # return 0 if sign is not determined
    u, v = symbols('u, v', positive = True)
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
# 2. critical point on x = y (example? why?)

def negative(f, x0 = 0, x1 = oo, y0 = 0, y1 = oo):
    x, y = symbols('x, y', positive = True)

    # try to find counterexample
    f0 = f.subs(x, x0).subs(y, y0)
    if f0 < 0:
        return 'f({},{})={}'.format(x0, y0, f0)

    # try to prove by buffalo way
    dx, dy = x1 - x0, y1 - y0
    u, v = symbols('u, v', positive = True)
    f1 = f.subs(x, x0 + (u if dx == oo else dx/(1 + u))). \
        subs(y, y0 + (v if dy == oo else dy/(1 + v)))
    f1 = factor(f1)
    s = sign(f1)
    if s > 0:
        logging.info('non_negative: [{},{},{},{}], f={}'.format(x0, x1, y0, y1, f0))
        return ''
    elif s < 0:
        return 'f={}<0'.format(f1)
        
    logging.info('try_dividing: [{},{},{},{}], f={}'.format(x0, x1, y0, y1, f0))

    # divide
    xm = (1 if x0 == 0 else x0*2) if x1 == oo else x0 + dx/Integer(2)
    ym = (1 if y0 == 0 else y0*2) if y1 == oo else y0 + dy/Integer(2)
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
    x, y = symbols('x, y', positive = True)
    # https://math.stackexchange.com/q/3831395
    f = x**5 - x**3/2 - x + Integer(4)/5
    # https://math.stackexchange.com/q/83670
    f = x**8 - x**7 + 2*x**6 - 2*x**5 + 3*x**4 - 3*x**3 + 4*x**2 - 4*x + Integer(5)/2
    u, v = symbols('u, v', positive = True)
    # https://math.stackexchange.com/q/1775572
    f = 65*u**10 + 215*u**9*v + 546*u**9 + 285*u**8*v**2 + 1503*u**8*v + 1989*u**8 + 275*u**7*v**3 + 1488*u**7*v**2 + 4284*u**7*v + 4095*u**7 + 315*u**6*v**4 + 1061*u**6*v**3 + 2436*u**6*v**2 + 6093*u**6*v + 5226*u**6 + 285*u**5*v**5 + 1290*u**5*v**4 + 591*u**5*v**3 - 441*u**5*v**2 + 4029*u**5*v + 4329*u**5 + 135*u**4*v**6 + 1185*u**4*v**5 + 1725*u**4*v**4 - 3020*u**4*v**3 - 5898*u**4*v**2 + 570*u**4*v + 2392*u**4 + 25*u**3*v**7 + 500*u**3*v**6 + 1890*u**3*v**5 + 779*u**3*v**4 - 5556*u**3*v**3 - 6582*u**3*v**2 - 326*u**3*v + 858*u**3 + 75*u**2*v**7 + 690*u**2*v**6 + 1866*u**2*v**5 + 762*u**2*v**4 - 2778*u**2*v**3 - 2400*u**2*v**2 + 192*u**2*v + 156*u**2 + 75*u*v**7 + 636*u*v**6 + 1617*u*v**5 + 1527*u*v**4 + 318*u*v**3 + 114*u*v**2 + 156*u*v + 65*v**7 + 351*v**6 + 741*v**5 + 754*v**4 + 390*v**3 + 156*v**2
    # https://math.stackexchange.com/q/1777075
    f = 90*u**7 + 190*u**6*v + 396*u**6 + 120*u**5*v**2 + 542*u**5*v + 630*u**5 + 55*u**4*v**3 + 41*u**4*v**2 + 164*u**4*v + 504*u**4 + 60*u**3*v**4 - 40*u**3*v**3 - 824*u**3*v**2 - 416*u**3*v + 252*u**3 + 25*u**2*v**5 + 115*u**2*v**4 - 332*u**2*v**3 - 984*u**2*v**2 - 156*u**2*v + 72*u**2 + 50*u*v**5 + 206*u*v**4 - 64*u*v**3 - 192*u*v**2 + 72*u*v + 90*v**5 + 216*v**4 + 108*v**3 + 72*v**2
    # intermediate step for sum_cyc(x**3/(8*x**2 + 3*y**2)) - (x + y + z)/11
    # f = 33*u**7 + 69*u**6*v + 143*u**6 + 42*u**5*v**2 + 190*u**5*v + 220*u**5 + 18*u**4*v**3 + 2*u**4*v**2 + 30*u**4*v + 165*u**4 + 21*u**3*v**4 - 24*u**3*v**3 - 336*u**3*v**2 - 194*u**3*v + 77*u**3 + 9*u**2*v**5 + 39*u**2*v**4 - 141*u**2*v**3 - 401*u**2*v**2 - 81*u**2*v + 22*u**2 + 18*u*v**5 + 71*u*v**4 - 42*u*v**3 - 92*u*v**2 + 22*u*v + 33*v**5 + 77*v**4 + 33*v**3 + 22*v**2
    f = f.subs(u, x).subs(v, y)
    print('[' + negative(f) + ']')

if __name__ == '__main__':
    main()