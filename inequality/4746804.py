from sympy import *

# https://math.stackexchange.com/q/4746804

def main():
    a, b = symbols('a, b', negative = False)
    # a*b <= 1
    c = (1 - a*b)/(a + b)
    f = 1 + 36*(a*b*c)**2 - 21*a*b*c/(a + b + c)
    u, v = symbols('u, v', negative = False)
    s3 = 1/sqrt(3)
    # a <= b <= s3
    print('f(ab3) =', factor(f.subs(b, s3/(1 + u)).subs(a, s3/(1 + u + v))))
    # a <= s3 <= b <= 1/a
    print('f(a3b) =', factor(f.subs(b, 1/a - (1/a - s3)/(1 + v)).subs(a, s3/(1 + u))))
    # critical point at (u, v) = (0, 0), so try u <= v and v <= u
    g = 243*u**10*v**6 + 486*u**10*v**5 + 243*u**10*v**4 + 2430*u**9*v**6 + 5184*u**9*v**5 + 3078*u**9*v**4 + 324*u**9*v**3 + 11259*u**8*v**6 + 24138*u**8*v**5 + 17658*u**8*v**4 + 2106*u**8*v**3 + 243*u**8*v**2 + 31752*u**7*v**6 + 65664*u**7*v**5 + 58050*u**7*v**4 + 7326*u**7*v**3 + 774*u**7*v**2 + 90*u**7*v + 60264*u**6*v**6 + 116748*u**6*v**5 + 120159*u**6*v**4 + 18270*u**6*v**3 + 507*u**6*v**2 + 240*u**6*v + 12*u**6 + 80352*u**5*v**6 + 143028*u**5*v**5 + 163620*u**5*v**4 + 32670*u**5*v**3 - 360*u**5*v**2 + 126*u**5*v + 36*u**5 + 76176*u**4*v**6 + 123624*u**4*v**5 + 148656*u**4*v**4 + 39000*u**4*v**3 + 228*u**4*v**2 - 144*u**4*v + 60*u**4 + 50688*u**3*v**6 + 75600*u**3*v**5 + 89328*u**3*v**4 + 29232*u**3*v**3 + 1440*u**3*v**2 - 192*u**3*v + 48*u**3 + 22656*u**2*v**6 + 31968*u**2*v**5 + 34464*u**2*v**4 + 12960*u**2*v**3 + 1200*u**2*v**2 - 96*u**2*v + 16*u**2 + 6144*u*v**6 + 8640*u*v**5 + 8064*u*v**4 + 3168*u*v**3 + 384*u*v**2 - 32*u*v + 768*v**6 + 1152*v**5 + 960*v**4 + 384*v**3 + 64*v**2
    w = symbols('w', negative = False)
    print('g(uv) =', factor(g.subs(v, u*(1 + w))))
    print('g(vw) =', factor(g.subs(u, v*(1 + w))))
    # s3 <= a <= b <= 1
    print('f(3ab1) =', factor(f.subs(b, s3 + (1 - s3)/(1 + u)).subs(a, s3 + (1 - s3)/(1 + u + v))))
    # s3 <= a <= 1 <= b <= 1/a
    print('f(3a1b) =', factor(f.subs(b, 1 + (1/a - 1)/(1 + v)).subs(a, s3 + (1 - s3)/(1 + u))))

if __name__ == '__main__':
    main()