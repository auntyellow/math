from sympy import *

# ISBN 9787030207210, p169, §7.3.2, problem 7

def sym(f, gens, vars):
    x1, x2, x3, x4, a, b, c, d, u, v, w = gens
    y1, y2, y3, y4 = vars
    g = f.subs({x1: y1}).subs({x2: y2}).subs({x3: y3}).subs({x4: y4})
    return poly(g.subs({d: c + w}).subs({c: b + v}).subs({b: a + u}), gens)

def pow(f, gens, n):
    x1, x2, x3, x4, a, b, c, d, u, v, w = gens
    return poly(f.subs({d: c + w}).subs({c: b + v}).subs({b: a + u}), gens)**n

def main():
    gens = symbols('x1, x2, x3, x4, a, b, c, d, u, v, w')
    x1, x2, x3, x4, a, b, c, d, u, v, w = gens
    sub_poly = Poly(-x3**2 - 2*x4*x1 + 6*x1**2 + 6*x2**2 + 4*x2*x1 - x4**2 - 2*x2*x3 - 2*x3*x1 - 2*x4*x2, gens)
    n = 1000
    f = pow(a - b, gens, n)*sym(sub_poly, gens, (a, b, c, d))
    f += pow(a - c, gens, n)*sym(sub_poly, gens, (a, c, b, d))
    f += pow(a - d, gens, n)*sym(sub_poly, gens, (a, d, b, c))
    f += pow(b - c, gens, n)*sym(sub_poly, gens, (b, c, a, d))
    f += pow(b - d, gens, n)*sym(sub_poly, gens, (b, d, a, c))
    f += pow(c - d, gens, n)*sym(sub_poly, gens, (c, d, a, b))
    print('f =', f.expr)

if __name__ == '__main__':
    main()