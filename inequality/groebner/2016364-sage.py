from sage.all import *

# https://math.stackexchange.com/q/2016364

def main():
    R = PolynomialRing(QQ, 'a, b, c, d', order = 'lex')
    a, b, c, d = R.gens()
    f = a**4 + b**4 + c**4 + d**4 + a**2*b**2 + b**2*c**2 + c**2*d**2 + d**2*a**2 + 8*(1 - a)*(1 - b)*(1 - c)*(1 - d) - 1
    # f_a, f_b, f_c, f_d = diff(f, a), diff(f, b), diff(f, c), diff(f, d)
    f_a = 4*a**3 + 2*a*b**2 + 2*a*d**2 - 8*(1 - b)*(1 - c)*(1 - d)
    f_b = 2*a**2*b + 4*b**3 + 2*b*c**2 - (1 - c)*(1 - d)*(8 - 8*a)
    f_c = 2*b**2*c + 4*c**3 + 2*c*d**2 - (1 - b)*(1 - d)*(8 - 8*a)
    f_d = 2*a**2*d + 2*c**2*d + 4*d**3 - (1 - b)*(1 - c)*(8 - 8*a)
    B = R.ideal(f_a, f_b, f_c, f_d).groebner_basis()
    for f in B:
        print(factor(f), '= 0')
    print(len(B), 'equations')
    x = QQ['x'].gen()
    # RR may get wrong values, perhaps due to precision loss
    dn = B[len(B) - 1].subs({d: x}).roots(AA, multiplicities = False)
    print('d =', dn)
    # dn[0] and dn[4] can't solve c, dn[3] can't solve b, dn[1] is saddle point
    d0 = dn[2]
    cn = B[len(B) - 2].subs({c: x, d: d0}).roots(AA, multiplicities = False)
    print('c =', cn)
    c0 = cn[len(cn) - 1]
    bn = B[len(B) - 4].subs({b: x, c: c0, d: d0}).roots(AA, multiplicities = False)
    print('b =', bn)
    b0 = bn[len(bn) - 1]
    an = B[len(B) - 7].subs({a: x, b: b0, c: c0, d: d0}).roots(AA, multiplicities = False)
    print('a =', an)
    a0 = an[len(an) - 1]
    print('f =', f.subs({a: a0, b: b0, c: c0, d: d0}))

if __name__ == '__main__':
    main()
