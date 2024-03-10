from sage.all import *

# https://math.stackexchange.com/q/4850712

def main():
    R = PolynomialRing(QQ, 'k, u, v', order = 'lex')
    k, u, v = R.gens()
    g = -k**2*u**4*v**2 - 2*k**2*u**4*v - k**2*u**4 - 3*k**2*u**3*v**2 - 6*k**2*u**3*v - 3*k**2*u**3 + k**2*u**2*v**3 + k**2*u**2*v**2 - 2*k**2*u**2*v - 2*k**2*u**2 - k**2*u*v**4 - 2*k**2*u*v**3 + k**2*u*v**2 + 2*k**2*u*v - k**2*v**4 - 3*k**2*v**3 - 2*k**2*v**2 + k*u**5*v**2 + 2*k*u**5*v + k*u**5 + k*u**4*v**3 + 8*k*u**4*v**2 + 12*k*u**4*v + 4*k*u**4 - k*u**3*v**4 + 16*k*u**3*v**2 + 24*k*u**3*v + 6*k*u**3 - 4*k*u**2*v**4 - 10*k*u**2*v**3 + 4*k*u**2*v**2 + 16*k*u**2*v + 4*k*u**2 - 5*k*u*v**4 - 16*k*u*v**3 - 14*k*u*v**2 - 4*k*u*v + k*v**5 + 4*k*v**4 + 6*k*v**3 + 4*k*v**2 + u**5 + 5*u**4 - u**3*v**2 - 2*u**3*v + 9*u**3 + u**2*v**5 + 5*u**2*v**4 + 9*u**2*v**3 + 3*u**2*v**2 - 6*u**2*v + 6*u**2 + 2*u*v**5 + 10*u*v**4 + 18*u*v**3 + 9*u*v**2 - 6*u*v + v**5 + 5*v**4 + 9*v**3 + 6*v**2
    g_u = -4*k**2*u**3*v**2 - 8*k**2*u**3*v - 4*k**2*u**3 - 9*k**2*u**2*v**2 - 18*k**2*u**2*v - 9*k**2*u**2 + 2*k**2*u*v**3 + 2*k**2*u*v**2 - 4*k**2*u*v - 4*k**2*u - k**2*v**4 - 2*k**2*v**3 + k**2*v**2 + 2*k**2*v + 5*k*u**4*v**2 + 10*k*u**4*v + 5*k*u**4 + 4*k*u**3*v**3 + 32*k*u**3*v**2 + 48*k*u**3*v + 16*k*u**3 - 3*k*u**2*v**4 + 48*k*u**2*v**2 + 72*k*u**2*v + 18*k*u**2 - 8*k*u*v**4 - 20*k*u*v**3 + 8*k*u*v**2 + 32*k*u*v + 8*k*u - 5*k*v**4 - 16*k*v**3 - 14*k*v**2 - 4*k*v + 5*u**4 + 20*u**3 - 3*u**2*v**2 - 6*u**2*v + 27*u**2 + 2*u*v**5 + 10*u*v**4 + 18*u*v**3 + 6*u*v**2 - 12*u*v + 12*u + 2*v**5 + 10*v**4 + 18*v**3 + 9*v**2 - 6*v
    g_v = -2*k**2*u**4*v - 2*k**2*u**4 - 6*k**2*u**3*v - 6*k**2*u**3 + 3*k**2*u**2*v**2 + 2*k**2*u**2*v - 2*k**2*u**2 - 4*k**2*u*v**3 - 6*k**2*u*v**2 + 2*k**2*u*v + 2*k**2*u - 4*k**2*v**3 - 9*k**2*v**2 - 4*k**2*v + 2*k*u**5*v + 2*k*u**5 + 3*k*u**4*v**2 + 16*k*u**4*v + 12*k*u**4 - 4*k*u**3*v**3 + 32*k*u**3*v + 24*k*u**3 - 16*k*u**2*v**3 - 30*k*u**2*v**2 + 8*k*u**2*v + 16*k*u**2 - 20*k*u*v**3 - 48*k*u*v**2 - 28*k*u*v - 4*k*u + 5*k*v**4 + 16*k*v**3 + 18*k*v**2 + 8*k*v - 2*u**3*v - 2*u**3 + 5*u**2*v**4 + 20*u**2*v**3 + 27*u**2*v**2 + 6*u**2*v - 6*u**2 + 10*u*v**4 + 40*u*v**3 + 54*u*v**2 + 18*u*v - 6*u + 5*v**4 + 20*v**3 + 27*v**2 + 12*v
    B = R.ideal(g, g_u, g_v).groebner_basis()
    for f in B:
        print(factor(f), '= 0')
    print(len(B), 'equations')
    x = QQ['x'].gen()
    # AA got 1.384744217412241? and RR got 1.38474421741224
    # however, RR got a wrong u0, perhaps due to precision loss
    vn = B[len(B) - 1].subs({v: x}).roots(AA, multiplicities = False)
    print('v =', vn)
    v0 = vn[len(vn) - 1]
    un = B[len(B) - 2].subs({u: x, v: v0}).roots(RR, multiplicities = False)
    print('u =', un)
    u0 = un[len(un) - 1]
    kn = g.subs({k: x, u: u0, v: v0}).roots(RR, multiplicities = False)
    print('k =', kn)

if __name__ == '__main__':
    main()