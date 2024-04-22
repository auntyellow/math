from sage.all import *

# https://en.wikipedia.org/wiki/Lagrange_point

def main():
    A = QQ['R, r']
    R, r = A.gens()
    PR = PolynomialRing(A.fraction_field(), 'u, v, x', order = 'lex')
    u, v, x = PR.gens()
    f1 = -R**3*r*u**3 + R**3*r*v**3 + R**3*v**3*x - 2*R**2*r**2*u**3 + 2*R**2*r**2*v**3 + R**2*r*u**3*x + 2*R**2*r*v**3*x - R*r**3*u**3 + R*r**3*v**3 + 2*R*r**2*u**3*x + R*r**2*v**3*x + r**3*u**3*x - u**3*v**3*x
    f3 = r**2 + 2*r*x - u**2 + x**2
    f4 = R**2 - 2*R*x - v**2 + x**2
    '''
    B = PR.ideal(f1, f3, f4).groebner_basis()
    with proof.WithProof('polynomial', False):
        for f in B:
            print(factor(f), '= 0')
    print(len(B), 'equations')
    # B[4]:
    # -x + R and x + r are singularities
    # x**2 + (-R + r)*x + R**2 + R*r + r**2 has no real solution
    print()
    '''
    R, r = 1 - 3e-6, 3e-6
    x = QQ['x'].gen()
    # doesn't seem like Lagrange points
    L_ = -x**3 + (R - r)*x**2 + (R**2 + 3*R*r + r**2)*x - R**3 - R**2*r + R*r**2 + r**3
    print('L? =', L_.roots(RR, multiplicities = False))
    L2 = -x**5 + (2*R - 2*r)*x**4 + (-R**2 + 4*R*r - r**2)*x**3 + (R**3 + R**2*r + 5*R*r**2 + r**3)*x**2 + (-2*R**4 - 4*R**3*r - R**2*r**2 + 4*R*r**3 + 2*r**4)*x + R**5 + 2*R**4*r + R**3*r**2 + R**2*r**3 + 2*R*r**4 + r**5
    print('L2 =', L2.roots(RR, multiplicities = False))
    L1 = x**5 + (-2*R + 2*r)*x**4 + (R**2 - 4*R*r + r**2)*x**3 + (-R**3 + R**2*r - R*r**2 + r**3)*x**2 + (2*R**4 + 4*R**3*r + 5*R**2*r**2 + 4*R*r**3 + 2*r**4)*x - R**5 - 2*R**4*r - R**3*r**2 + R**2*r**3 + 2*R*r**4 + r**5
    print('L1 =', L1.roots(RR, multiplicities = False))
    L3 = x**5 + (-2*R + 2*r)*x**4 + (R**2 - 4*R*r + r**2)*x**3 + (R**3 + 5*R**2*r + R*r**2 + r**3)*x**2 + (-2*R**4 - 4*R**3*r + R**2*r**2 + 4*R*r**3 + 2*r**4)*x + R**5 + 2*R**4*r + R**3*r**2 + R**2*r**3 + 2*R*r**4 + r**5
    print('L3 =', L3.roots(RR, multiplicities = False))

if __name__ == '__main__':
    main()