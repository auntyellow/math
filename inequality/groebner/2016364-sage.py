from sage.all import *

# https://math.stackexchange.com/q/2016364

def main():
    R = PolynomialRing(QQ, 'a, b, c, d', order = 'lex')
    a, b, c, d = R.gens()
    f = a**4 + b**4 + c**4 + d**4 + a**2*b**2 + b**2*c**2 + c**2*d**2 + d**2*a**2 + 8*(1 - a)*(1 - b)*(1 - c)*(1 - d) - 1
    f_a, f_b, f_c, f_d = diff(f, a), diff(f, b), diff(f, c), diff(f, d)
    B = R.ideal(f_a, f_b, f_c, f_d).groebner_basis()
    for f in B:
        print(factor(f), '= 0')
    print(len(B), 'equations')
    print()

    d = 0
    f = a**4 + b**4 + c**4 + d**4 + a**2*b**2 + b**2*c**2 + c**2*d**2 + d**2*a**2 + 8*(1 - a)*(1 - b)*(1 - c)*(1 - d) - 1
    f_a, f_b, f_c = diff(f, a), diff(f, b), diff(f, c)
    B = R.ideal(f_a, f_b, f_c).groebner_basis()
    for f in B:
        print(factor(f), '= 0')
    print(len(B), 'equations')
    print()

    d = 1
    f = a**4 + b**4 + c**4 + d**4 + a**2*b**2 + b**2*c**2 + c**2*d**2 + d**2*a**2 + 8*(1 - a)*(1 - b)*(1 - c)*(1 - d) - 1
    f_a, f_b, f_c = diff(f, a), diff(f, b), diff(f, c)
    B = R.ideal(f_a, f_b, f_c).groebner_basis()
    for f in B:
        print(factor(f), '= 0')
    print(len(B), 'equations')

if __name__ == '__main__':
    main()
