from sage.all import *

# ISBN 9787030207210, p169, §7.3.2, problem 7

def sym(f, vars1, vars2):
    x1, x2, x3, x4, a, b, c, d = vars1
    g = f.subs({x1: a}).subs({x2: b}).subs({x3: c}).subs({x4: d})
    a, b, c, d, u, v, w = vars2
    return g.subs({d: c + w}).subs({c: b + v}).subs({b: a + u})

def pow_n(f, vars, n):
    a, b, c, d, u, v, w = vars
    return (f.subs({d: c + w}).subs({c: b + v}).subs({b: a + u}))**n

def main():
    R = PolynomialRing(ZZ, 'x1, x2, x3, x4, a, b, c, d, u, v, w', order = 'lex')
    x1, x2, x3, x4, a, b, c, d, u, v, w = R.gens()
    sub_poly = -x3**2 - 2*x4*x1 + 6*x1**2 + 6*x2**2 + 4*x2*x1 - x4**2 - 2*x2*x3 - 2*x3*x1 - 2*x4*x2
    n = 1000
    f = pow_n(a - b, (a, b, c, d, u, v, w), n)*sym(sub_poly, (x1, x2, x3, x4, a, b, c, d), (a, b, c, d, u, v, w))
    f += pow_n(a - c, (a, b, c, d, u, v, w), n)*sym(sub_poly, (x1, x2, x3, x4, a, c, b, d), (a, b, c, d, u, v, w))
    f += pow_n(a - d, (a, b, c, d, u, v, w), n)*sym(sub_poly, (x1, x2, x3, x4, a, d, b, c), (a, b, c, d, u, v, w))
    f += pow_n(b - c, (a, b, c, d, u, v, w), n)*sym(sub_poly, (x1, x2, x3, x4, b, c, a, d), (a, b, c, d, u, v, w))
    f += pow_n(b - d, (a, b, c, d, u, v, w), n)*sym(sub_poly, (x1, x2, x3, x4, b, d, a, c), (a, b, c, d, u, v, w))
    f += pow_n(c - d, (a, b, c, d, u, v, w), n)*sym(sub_poly, (x1, x2, x3, x4, c, d, a, b), (a, b, c, d, u, v, w))
    print('f =', f)

if __name__ == '__main__':
    main()