from sage.all import *

# ISBN 9787030207210, p169, §7.3.2, problem 7

def cyc4(f, vars):
    a, b, c, d = vars
    t = var('t')
    return f.subs({d: t}).subs({c: d}).subs({b: c}).subs({a: b}).subs({t: a})

def cyc3(f, vars):
    a, b, c, d = vars
    t = var('t')
    return f.subs({d: t}).subs({c: d}).subs({b: c}).subs({t: b})

def sum_comb4(f, vars):
    f1 = cyc4(f, vars)
    f2 = cyc4(f1, vars)
    f3 = cyc3(f2, vars)
    return f + f1 + f2 + cyc4(f2, vars) + f3 + cyc4(f3, vars)

def main():
    x1, x2, x3, x4 = var('x1, x2, x3, x4')
    n = 200
    f = sum_comb4((-x3**2 - 2*x4*x1 + 6*x1**2 + 6*x2**2 + 4*x2*x1 - x4**2 - 2*x2*x3 - 2*x3*x1 - 2*x4*x2)*(x1 - x2)**n, (x1, x2, x3, x4))
    a, u, v, w = var('a, u, v, w')
    print('f =', expand(f.subs({x1: a}).subs({x2: a + u}).subs({x3: a + u + v}).subs({x4: a + u + v + w})))
    # same speed, same result
    # print('f =', expand(f.subs({x4: x3 + w}).subs({x3: x2 + v}).subs({x2: x1 + u}).subs({x1: a})))
