from sage.all import *

def main():
    # sum_cyc(sqrt(a/(b + c))) >= 2
    R = PolynomialRing(QQ, 'l1, l2, l3, l4, A, B, C, a, b, c', order = 'lex')
    l1, l2, l3, l4, A, B, C, a, b, c = R.gens()
    g1 = A**2*(b + c) - a
    g2 = B**2*(a + c) - b
    g3 = C**2*(a + b) - c
    g4 = a + b + c - 1
    f = A + B + C - 3
    L = f + l1*g1 + l2*g2 + l3*g3 + l4*g4
    B = R.ideal(g1, g2, g3, g4, diff(L, a), diff(L, b), diff(L, c), diff(L, A), diff(L, B), diff(L, C)).groebner_basis()
    for f in B:
        print(factor(f), '= 0')
    print(len(B), 'equations')
    # c = 0 degenerates to sqrt-1.py

if __name__ == '__main__':
    main()