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

warning_set = set()
warning_set2 = set()

def warn(f, f0, x0, y0):
    tuple = (f, f0, x0, y0)
    if not tuple in warning_set:
        warning_set.add(tuple)
        logging.warning('{} = {} at ({}, {})'.format(f, f0, x0, y0))

def subs2(f, x0, y0):
    x, y = symbols('x, y', negative = False)
    f0, f1 = f.subs(x, x0).subs(y, y0), f.subs(y, y0).subs(x, x0)
    # TODO what to return if nan or oo?
    if f0 == nan or abs(f0) == oo:
        warn(f, f0, x0, y0)
        f0 = 0
    if f1 == nan or abs(f1) == oo:
        warn(f, f1, x0, y0)
        f1 = 0
    if f0 != f1:
        tuple = (f, f0, f1, x0, y0)
        if not tuple in warning_set2:
            warning_set2.add(tuple)
            logging.warning('{} = {} or {} at ({}, {})'.format(f, f0, f1, x0, y0))
    return min(f0, f1)

# return '' if sum(sqrt(A_n)) - D >= 0, or the counterexample
# param A_n: 2-var functions about x and y
# param D: a positive constant
def negative(A_n, D, x0, x1, y0, y1):
    x, y = symbols('x, y', negative = False)

    # try to find counterexample
    f0 = -D
    for A_i in A_n:
        f0 += subs2(sqrt(A_i), x0, y0)
    if f0 < 0:
        return 'f({},{})={}'.format(x0, y0, N(f0))

    sum_min = 0
    min_n = []
    for A_i in A_n:
        a00, a01, a10, a11 = subs2(A_i, x0, y0), subs2(A_i, x0, y1), subs2(A_i, x1, y0), subs2(A_i, x1, y1)
        min_i = min(sqrt(a00), sqrt(a01), sqrt(a10), sqrt(a11))
        sum_min += min_i
        min_n.append(min_i)
    # divide if sum_min - D < 0
    f0 = sum_min - D
    dx, dy = x1 - x0, y1 - y0
    if f0 < 0:
        logging.info('sum_min < D: [{},{},{},{}], f={}'.format(x0, x1, y0, y1, N(f0)))
    else:
        u, v = symbols('u, v', negative = False)
        non_negative = True
        for i in range(len(A_n)):
            # sqrt(A_i) >= D*m_i/sum_min (for all i) => sum(sqrt(A_i)) >= D
            f = A_n[i] - (min_n[i]*D/sum_min)**2
            f = factor(f.subs(x, x0 + dx/(1 + u)).subs(y, y0 + dy/(1 + v)))
            if sign(f) <= 0:
                logging.info('unable to prove sqrt({}) >= {}: [{},{},{},{}]'.format(A_n[i], min_n[i]*D/sum_min, x0, x1, y0, y1))
                non_negative = False
                break
        if non_negative:
            logging.info('non_negative: [{},{},{},{}], f={}'.format(x0, x1, y0, y1, N(f0)))
            return ''
    
    # divide
    xm = x0 + dx/S(2)
    ym = y0 + dy/S(2)
    n = negative(A_n, D, xm, x1, ym, y1)
    if n != '':
        return n
    n = negative(A_n, D, x0, xm, ym, y1)
    if n != '':
        return n
    n = negative(A_n, D, xm, x1, y0, ym)
    if n != '':
        return n
    return negative(A_n, D, x0, xm, y0, ym)

def main():
    logging.basicConfig(level = 'INFO')
    x, y = symbols('x, y', negative = False)
    '''
    u, v = x, y
    # imo-2001-2, slow
    A_n = [(u + 1)**2/(u**2 + 2*u + 8*v + 9), (v + 1)**2/(8*u + v**2 + 2*v + 9), 1/(8*u*v + 8*u + 8*v + 9)]
    # sqrt(A) + sqrt(B) + sqrt(C) >= 11/10 works; 10/9 doesn't work
    print('[' + negative(A_n, 1, S(11)/6, 12, 0, 12) + ']')
    # result from 4575195.py, slow++
    # f(1/u,v)
    A_n = [(u + 1)*(v**2 + 2*v + 5)/(u*v**2 + 2*u*v + 4*u + 3), (4*u**2*v**2 + 8*u**2*v + 5*u**2 + 2*u + 1)/((v + 1)*(3*u**2*v + 4*u**2 + 2*u + 1)), (v + 1)*(5*u**2 + 8*u + 4)/((u + 1)*(3*u*v + 4*u + 3*v + 3))]
    print('[' + negative(A_n, 3*sqrt(5)/2, 0, S(1)/5, 0, 23) + ']')
    # f(u,1/v)
    A_n = [(u + 1)*(5*v**2 + 2*v + 1)/(3*u*v**2 + 4*v**2 + 2*v + 1), (u**2*v**2 + 2*u*v**2 + 5*v**2 + 8*v + 4)/((v + 1)*(u**2*v + 2*u*v + 4*v + 3)), (v + 1)*(4*u**2 + 8*u + 5)/((u + 1)*(3*u*v + 3*u + 4*v + 3))]
    print('[' + negative(A_n, 3*sqrt(5)/2, 0, 23, 0, S(1)/5) + ']')
    '''
    # find negative at (1, 1)
    print('[' + negative([(x - 1)**2 + (y - 1)**2], sqrt(2), 0, 2, 0, 2) + ']')
    # prove non-negative
    print('[' + negative([(x - 1)**2 + (y - 1)**2 + 1], 1, 0, 2, 0, 2) + ']')
    # unable to prove because zero point (1, 1) is not on the lattice
    # print('[' + negative([(x - 1)**2 + (y - 1)**2 + 1], 1, 0, 3, 0, 3) + ']')

if __name__ == '__main__':
    main()