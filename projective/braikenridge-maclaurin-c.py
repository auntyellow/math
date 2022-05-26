from cartesian import *

def L(a, b):
    x, y = symbols('x, y')
    return Eq(y, a*x + b)

def main():
    g, h, j, k, m, n, p, q = symbols('g, h, j, k, m, n, p, q')
    AB, DE, BC, EF, AF, CD = L(j, g), L(k, g), L(m, h), L(n, h), L(p, 0), L(q, 0)
    A, E, C = intersect(AB, AF), intersect(DE, EF), intersect(BC, CD)
    D, B, F = intersect(CD, DE), intersect(AB, BC), intersect(AF, EF)
    print('A:', A)
    print('B:', B)
    print('C:', C)
    print('D:', D)
    print('E:', E)
    print('F:', F)

    mat = []
    for P in [A, B, C, D, E, F]:
        x, y = P
        mat.append([x*x, x*y, y*y, x, y, 1])
    print('M =', Matrix(mat))
    print('det M =', Matrix(mat).det(method='domain-ge'))

if __name__ == '__main__':
    main()