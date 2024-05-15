from sage.all import *

# https://math.stackexchange.com/q/1767225

def main():
    A = QQ['a, b, c, d, e, f, g, h, j, k, m, n']
    a, b, c, d, e, f, g, h, j, k, m, n = A.gens()
    R = PolynomialRing(A.fraction_field(), 'y, x', order = 'lex')
    y, x = R.gens()
    F1 = a*x**2 + b*x*y + c*y**2 + d*x + e*y + f
    F2 = g*x**2 + h*x*y + j*y**2 + k*x + m*y + n
    B = R.ideal(F1, F2).groebner_basis()
    print(B[1], '= 0')

if __name__ == '__main__':
    main()
