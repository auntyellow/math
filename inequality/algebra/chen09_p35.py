from sympy import *

# ISBN 9787542848482, p35, §2.1, ex2
# x + y + z = x*y*z -> 1/sqrt(1 + x**2) + 1/sqrt(1 + y**2) + 1/sqrt(1 + z**2) <= 3/2

def main():
    x, y = symbols('x, y', positive = True)
    # x + y + z = x*y*z, x*y > 1
    z = (x + y)/(x*y - 1)
    print('x + y + z - x*y*z =', factor(x + y + z - x*y*z))
    # use conclusion from radical3.py
    A, B, C, D = 1/(1 + x**2), 1/(1 + y**2), 1/(1 + z**2), S(9)/4

    f1 = D - A - B - C
    u, v = symbols('u, v', positive = True)
    print('f1 =', factor(f1.subs(y, (1 + u)/x)))

    f2 = A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D)
    print('f2 =', factor(f2.subs(y, (1 + u)/x)))
    # f2's numerator
    g = 25*u**4*x**4 - 14*u**4*x**2 + 25*u**4 + 180*u**3*x**4 + 152*u**3*x**2 + 100*u**3 - 14*u**2*x**6 + 282*u**2*x**4 + 382*u**2*x**2 + 150*u**2 + 180*u*x**6 + 332*u*x**4 + 252*u*x**2 + 100*u + 25*x**8 + 36*x**6 + 22*x**4 + 36*x**2 + 25
    print('g(xu) =', factor(g.subs(u, x*(1 + u)))) # proved by polynomial-prover
    print('g(ux) =', factor(g.subs(x, u*(1 + x))))

    f3 = (A**2 + B**2 + C**2 + D**2 - 2*(A*B + A*C + A*D + B*C + B*D + C*D))**2 - 64*A*B*C*D
    print('f3 =', factor(f3.subs(y, (1 + u)/x)))

    # f3's one numerator
    g2 = 25*u**4*x**4 - 14*u**4*x**2 + 25*u**4 + 372*u**3*x**4 + 344*u**3*x**2 + 100*u**3 - 14*u**2*x**6 + 666*u**2*x**4 + 766*u**2*x**2 + 150*u**2 + 372*u*x**6 + 716*u*x**4 + 444*u*x**2 + 100*u + 25*x**8 + 36*x**6 + 22*x**4 + 36*x**2 + 25
    print('g2(xu) =', factor(g2.subs(u, x*(1 + u)))) # proved by polynomial-prover
    print('g2(ux) =', factor(g2.subs(x, u*(1 + x))))

    # f3's another numerator
    g1 = 25*u**4*x**4 - 14*u**4*x**2 + 25*u**4 - 12*u**3*x**4 - 40*u**3*x**2 + 100*u**3 - 14*u**2*x**6 - 102*u**2*x**4 - 2*u**2*x**2 + 150*u**2 - 12*u*x**6 - 52*u*x**4 + 60*u*x**2 + 100*u + 25*x**8 + 36*x**6 + 22*x**4 + 36*x**2 + 25
    s3 = sqrt(3)
    # g1 = 0 at x = sqrt(3) and u = 2
    print('g1 =', g1.subs(x, s3).subs(u, 2))
    print('g1(<s3,<2) =', factor(g1.subs(x, s3/(1 + x)).subs(u, 2/(1 + u)))) # to prove
    print('g1(>s3,<2) =', factor(g1.subs(x, s3 + x).subs(u, 2/(1 + u))))
    print('g1(<s3,>2) =', factor(g1.subs(x, s3/(1 + x)).subs(u, 2 + u)))
    print('g1(>s3,>2) =', factor(g1.subs(x, s3 + x).subs(u, 2 + u))) # to prove

    # g1(<s3,<2)'s numerator
    h1 = 25*u**4*x**8 + 200*u**4*x**7 + 808*u**4*x**6 + 2048*u**4*x**5 + 3568*u**4*x**4 + 4352*u**4*x**3 + 4480*u**4*x**2 + 3584*u**4*x + 3328*u**4 + 300*u**3*x**8 + 2400*u**3*x**7 + 9192*u**3*x**6 + 21552*u**3*x**5 + 32736*u**3*x**4 + 32064*u**3*x**3 + 22656*u**3*x**2 + 13056*u**3*x + 12288*u**3 + 1350*u**2*x**8 + 10800*u**2*x**7 + 39504*u**2*x**6 + 85824*u**2*x**5 + 114768*u**2*x**4 + 88512*u**2*x**3 + 33984*u**2*x**2 + 4608*u**2*x + 12288*u**2 + 2700*u*x**8 + 21600*u*x**7 + 76104*u*x**6 + 154224*u*x**5 + 186336*u*x**4 + 120384*u*x**3 + 20736*u*x**2 - 18432*u*x + 2025*x**8 + 16200*x**7 + 55512*x**6 + 106272*x**5 + 122256*x**4 + 82944*x**3 + 27648*x**2
    print('h1(ux) =', factor(h1.subs(x, u*(1 + x))))
    print('h1(xu) =', factor(h1.subs(u, x*(1 + u))))
    # g1(>s3,>2)'s numerator
    h2 = 25*u**4*x**4 + 100*sqrt(3)*u**4*x**3 + 436*u**4*x**2 + 272*sqrt(3)*u**4*x + 208*u**4 + 188*u**3*x**4 + 752*sqrt(3)*u**3*x**3 + 3232*u**3*x**2 + 1952*sqrt(3)*u**3*x + 1536*u**3 - 14*u**2*x**6 - 84*sqrt(3)*u**2*x**5 - 204*u**2*x**4 + 864*sqrt(3)*u**2*x**3 + 5200*u**2*x**2 + 3200*sqrt(3)*u**2*x + 3072*u**2 - 68*u*x**6 - 408*sqrt(3)*u*x**5 - 2864*u*x**4 - 3296*sqrt(3)*u*x**3 - 6528*u*x**2 - 3072*sqrt(3)*u*x + 25*x**8 + 200*sqrt(3)*x**7 + 2056*x**6 + 3936*sqrt(3)*x**5 + 13584*x**4 + 9216*sqrt(3)*x**3 + 9216*x**2
    print('h2(ux) =', factor(h2.subs(x, u*(1 + x)))) # proved by polynomial-prover
    print('h2(xu) =', factor(h2.subs(u, x*(1 + u)))) # proved by polynomial-prover

if __name__ == '__main__':
    main()