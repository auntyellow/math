from sage.all import *

# https://math.stackexchange.com/q/4261358

def main():
    R = PolynomialRing(QQ, 'l, x, y, z', order = 'lex')
    l, x, y, z = R.gens()
    g = x**3 + y**3 + z**3 - 3
    f = x + y + z - x**3*y**3 - x**3*z**3 - y**3*z**3
    L = f + l*g
    Lx, Ly, Lz = diff(L, x), diff(L, y), diff(L, z)
    print('L_x =', Lx)
    print('L_y =', Ly)
    print('L_z =', Lz)
    print()

    B = R.ideal(Lx, Ly, Lz, g).groebner_basis()
    for f in B:
        print(factor(f), '= 0')
    print(len(B), 'equations')

    t = QQ['t'].gen()
    zn = B[len(B) - 1].subs({z: t}).roots(RealField(1000), multiplicities = False)
    print('z =', zn)
    print(len(zn), 'roots')

    # TODO isolate real roots, see
    # https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/real_roots.html

if __name__ == '__main__':
    main()