from sympy import Eq, cancel, expand, lcm_list, symbols
from cartesian import *

def L(a, b):
    x, y = symbols('x, y')
    return Eq(y, a*x + b)

def main():
    g, h, j, k, m, n, p, q, x, y = symbols('g, h, j, k, m, n, p, q, x, y')
    AB, DE, BC, EF, AF, CD = L(j, g), L(k, g), L(m, h), L(n, h), L(p, 0), L(q, 0)
    A, E, C = intersect(AB, AF), intersect(DE, EF), intersect(BC, CD)
    D, B, F = intersect(CD, DE), intersect(AB, BC), intersect(AF, EF)
    print('A:', A)
    print('B:', B)
    print('C:', C)
    print('D:', D)
    print('E:', E)
    print('F:', F)

    points = [A, B, C, D, E, F]
    coefficients = [x*x, x*y, y*y, x, y]
    subs = {}
    mat = []
    for s in range(6):
        numerators, denominators, row = [], [], []
        for t in range(5):
            frac = fraction(cancel(coefficients[t].subs(x, points[s][0]).subs(y, points[s][1])))
            numerators.append(frac[0])
            denominators.append(frac[1])
        numerators.append(1)
        denominators.append(1)
        lcd = lcm_list(denominators)
        for t in range(6):
            rst = symbols('r' + str(s) + str(t))
            row.append(rst)
            subs[rst] = numerators[t]*cancel(lcd/denominators[t])
        mat.append(row)
    print('M =', Matrix(mat).evalf(subs = subs))
    print('det M =', expand(Matrix(mat).det().evalf(subs = subs)))

if __name__ == '__main__':
    main()