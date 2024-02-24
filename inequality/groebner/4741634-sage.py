from sage.all import *

# https://math.stackexchange.com/q/4741634

def main():
    R = PolynomialRing(QQ, 'l, x, y, z', order = 'lex')
    l, x, y, z = R.gens()
    g = x**2 + y**2 + z**2 + x*y*z - 4
    f = 4*(x*y + y*z + z*x - x*y*z) - (x*x*y + z)*(y*y*z + x)*(z*z*x + y)
    L = f + l*g
    Lx, Ly, Lz = diff(L, x), diff(L, y), diff(L, z)
    print('L_x =', Lx);
    print('L_y =', Ly);
    print('L_z =', Lz);

    B = R.ideal(Lx, Ly, Lz, g).groebner_basis()
    for f in B:
        print(factor(f), '= 0')
    print(len(B), 'equations')

if __name__ == '__main__':
    main()