from sympy import *

# https://math.stackexchange.com/q/4741634

def main():
    '''
    x, y, z = symbols('x, y, z', positive = True)
    z = solve(Eq(x*x + y*y + z*z + x*y*z, 4), z)[1]
    print('z =', z)
    '''
    a, b, c = symbols('a, b, c', positive = True)
    x = 2*a/sqrt((a + b)*(a + c))
    y = 2*b/sqrt((b + c)*(b + a))
    z = 2*c/sqrt((c + a)*(c + b))
    print('x*x + y*y + z*z + x*y*z =', factor(x*x + y*y + z*z + x*y*z))

    f = 4*(x*y + y*z + z*x - x*y*z) - (x*x*y + z)*(y*y*z + x)*(z*z*x + y)
    t, u, v = symbols('t, u, v', positive = True)
    '''
    f1 = f.subs(a, t).subs(b, a).subs(t, b)
    print('Is f symmetric?', f1 == f)
    f1 = f.subs(a, t).subs(b, a).subs(c, b).subs(t, c)
    print('Is f cyclic?', f1 == f)
    print('f =', factor(f.subs(a, c*(1 + u)).subs(b, c*(1 + v))))
    g = -4*u**6*v**4*sqrt(v + 2) + 2*u**6*v**4*sqrt(u + v + 2) + 2*u**6*v**3*sqrt(u + 2) - 22*u**6*v**3*sqrt(v + 2) + 14*u**6*v**3*sqrt(u + v + 2) + 12*u**6*v**2*sqrt(u + 2) - 42*u**6*v**2*sqrt(v + 2) + 36*u**6*v**2*sqrt(u + v + 2) + 24*u**6*v*sqrt(u + 2) - 32*u**6*v*sqrt(v + 2) + 40*u**6*v*sqrt(u + v + 2) + 16*u**6*sqrt(u + 2) - 8*u**6*sqrt(v + 2) + 16*u**6*sqrt(u + v + 2) - 4*u**5*v**5*sqrt(v + 2) + 4*u**5*v**5*sqrt(u + v + 2) + 6*u**5*v**4*sqrt(u + 2) - 54*u**5*v**4*sqrt(v + 2) + 50*u**5*v**4*sqrt(u + v + 2) - 5*u**5*v**3*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 42*u**5*v**3*sqrt(u + 2) - 214*u**5*v**3*sqrt(v + 2) + 226*u**5*v**3*sqrt(u + v + 2) - 25*u**5*v**2*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 124*u**5*v**2*sqrt(u + 2) - 348*u**5*v**2*sqrt(v + 2) + 472*u**5*v**2*sqrt(u + v + 2) - 40*u**5*v*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 184*u**5*v*sqrt(u + 2) - 232*u**5*v*sqrt(v + 2) + 456*u**5*v*sqrt(u + v + 2) - 20*u**5*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 112*u**5*sqrt(u + 2) - 48*u**5*sqrt(v + 2) + 160*u**5*sqrt(u + v + 2) + 2*u**4*v**6*sqrt(u + v + 2) + 6*u**4*v**5*sqrt(u + 2) - 22*u**4*v**5*sqrt(v + 2) + 34*u**4*v**5*sqrt(u + v + 2) - 10*u**4*v**4*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 70*u**4*v**4*sqrt(u + 2) - 210*u**4*v**4*sqrt(v + 2) + 292*u**4*v**4*sqrt(u + v + 2) - 95*u**4*v**3*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 300*u**4*v**3*sqrt(u + 2) - 688*u**4*v**3*sqrt(v + 2) + 1156*u**4*v**3*sqrt(u + v + 2) - 305*u**4*v**2*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 652*u**4*v**2*sqrt(u + 2) - 964*u**4*v**2*sqrt(v + 2) + 2216*u**4*v**2*sqrt(u + v + 2) - 400*u**4*v*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 772*u**4*v*sqrt(u + 2) - 528*u**4*v*sqrt(v + 2) + 1984*u**4*v*sqrt(u + v + 2) - 180*u**4*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 408*u**4*sqrt(u + 2) - 64*u**4*sqrt(v + 2) + 640*u**4*sqrt(u + v + 2) + 2*u**3*v**6*sqrt(u + 2) + 2*u**3*v**6*sqrt(v + 2) + 14*u**3*v**6*sqrt(u + v + 2) - 5*u**3*v**5*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 46*u**3*v**5*sqrt(u + 2) - 18*u**3*v**5*sqrt(v + 2) + 130*u**3*v**5*sqrt(u + v + 2) - 95*u**3*v**4*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 332*u**3*v**4*sqrt(u + 2) - 212*u**3*v**4*sqrt(v + 2) + 808*u**3*v**4*sqrt(u + v + 2) - 614*u**3*v**3*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 1136*u**3*v**3*sqrt(u + 2) - 620*u**3*v**3*sqrt(v + 2) + 2856*u**3*v**3*sqrt(u + v + 2) - 1572*u**3*v**2*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 2104*u**3*v**2*sqrt(u + 2) - 652*u**3*v**2*sqrt(v + 2) + 5148*u**3*v**2*sqrt(u + v + 2) - 1752*u**3*v*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 2128*u**3*v*sqrt(u + 2) - 64*u**3*v*sqrt(v + 2) + 4368*u**3*v*sqrt(u + v + 2) - 704*u**3*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 960*u**3*sqrt(u + 2) + 160*u**3*sqrt(v + 2) + 1328*u**3*sqrt(u + v + 2) + 6*u**2*v**6*sqrt(u + 2) + 12*u**2*v**6*sqrt(v + 2) + 36*u**2*v**6*sqrt(u + v + 2) - 25*u**2*v**5*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 100*u**2*v**5*sqrt(u + 2) + 104*u**2*v**5*sqrt(v + 2) + 268*u**2*v**5*sqrt(u + v + 2) - 305*u**2*v**4*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 636*u**2*v**4*sqrt(u + 2) + 416*u**2*v**4*sqrt(v + 2) + 1272*u**2*v**4*sqrt(u + v + 2) - 1572*u**2*v**3*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 2036*u**2*v**3*sqrt(u + 2) + 1004*u**2*v**3*sqrt(v + 2) + 3912*u**2*v**3*sqrt(u + v + 2) - 3516*u**2*v**2*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 3560*u**2*v**2*sqrt(u + 2) + 1560*u**2*v**2*sqrt(v + 2) + 6568*u**2*v**2*sqrt(u + v + 2) - 3536*u**2*v*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 3328*u**2*v*sqrt(u + 2) + 1456*u**2*v*sqrt(v + 2) + 5296*u**2*v*sqrt(u + v + 2) - 1312*u**2*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 1344*u**2*sqrt(u + 2) + 576*u**2*sqrt(v + 2) + 1536*u**2*sqrt(u + v + 2) + 24*u*v**6*sqrt(v + 2) + 40*u*v**6*sqrt(u + v + 2) - 40*u*v**5*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 40*u*v**5*sqrt(u + 2) + 248*u*v**5*sqrt(v + 2) + 280*u*v**5*sqrt(u + v + 2) - 400*u*v**4*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 384*u*v**4*sqrt(u + 2) + 1056*u*v**4*sqrt(v + 2) + 1116*u*v**4*sqrt(u + v + 2) - 1752*u*v**3*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 1440*u*v**3*sqrt(u + 2) + 2368*u*v**3*sqrt(v + 2) + 2960*u*v**3*sqrt(u + v + 2) - 3536*u*v**2*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 2672*u*v**2*sqrt(u + 2) + 3008*u*v**2*sqrt(v + 2) + 4544*u*v**2*sqrt(u + v + 2) - 3296*u*v*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 2496*u*v*sqrt(u + 2) + 2112*u*v*sqrt(v + 2) + 3456*u*v*sqrt(u + v + 2) - 1152*u*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 960*u*sqrt(u + 2) + 640*u*sqrt(v + 2) + 960*u*sqrt(u + v + 2) - 8*v**6*sqrt(u + 2) + 16*v**6*sqrt(v + 2) + 16*v**6*sqrt(u + v + 2) - 20*v**5*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) - 48*v**5*sqrt(u + 2) + 160*v**5*sqrt(v + 2) + 112*v**5*sqrt(u + v + 2) - 180*v**4*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) - 64*v**4*sqrt(u + 2) + 640*v**4*sqrt(v + 2) + 408*v**4*sqrt(u + v + 2) - 704*v**3*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 160*v**3*sqrt(u + 2) + 1328*v**3*sqrt(v + 2) + 960*v**3*sqrt(u + v + 2) - 1312*v**2*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 576*v**2*sqrt(u + 2) + 1536*v**2*sqrt(v + 2) + 1344*v**2*sqrt(u + v + 2) - 1152*v*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 640*v*sqrt(u + 2) + 960*v*sqrt(v + 2) + 960*v*sqrt(u + v + 2) - 384*sqrt(u + 2)*sqrt(v + 2)*sqrt(u + v + 2) + 256*sqrt(u + 2) + 256*sqrt(v + 2) + 256*sqrt(u + v + 2)
    g1 = g.subs(u, t).subs(v, u).subs(t, v)
    print('Is g symmetric?', g1 == g)
    '''

    A, B, C = symbols('A, B, C', positive = True)
    print('f =', factor(f).subs(sqrt(a + b), C).subs(sqrt(b + c), A).subs(sqrt(c + a), B))
    g = -5*A*B*C*a**5*b**3*c - 10*A*B*C*a**5*b**2*c**2 - 5*A*B*C*a**5*b*c**3 - 10*A*B*C*a**4*b**4*c - 30*A*B*C*a**4*b**3*c**2 - 30*A*B*C*a**4*b**2*c**3 - 10*A*B*C*a**4*b*c**4 - 5*A*B*C*a**3*b**5*c - 30*A*B*C*a**3*b**4*c**2 - 114*A*B*C*a**3*b**3*c**3 - 30*A*B*C*a**3*b**2*c**4 - 5*A*B*C*a**3*b*c**5 - 10*A*B*C*a**2*b**5*c**2 - 30*A*B*C*a**2*b**4*c**3 - 30*A*B*C*a**2*b**3*c**4 - 10*A*B*C*a**2*b**2*c**5 - 5*A*B*C*a*b**5*c**3 - 10*A*B*C*a*b**4*c**4 - 5*A*B*C*a*b**3*c**5 - 4*A*a**6*b**4 - 6*A*a**6*b**3*c + 2*A*a**6*b*c**3 - 4*A*a**5*b**5 - 10*A*a**5*b**4*c - 2*A*a**5*b**3*c**2 + 10*A*a**5*b**2*c**3 + 6*A*a**5*b*c**4 - 2*A*a**4*b**5*c + 10*A*a**4*b**4*c**2 + 32*A*a**4*b**3*c**3 + 10*A*a**4*b**2*c**4 + 6*A*a**4*b*c**5 + 2*A*a**3*b**6*c + 18*A*a**3*b**5*c**2 + 48*A*a**3*b**4*c**3 + 20*A*a**3*b**3*c**4 + 6*A*a**3*b**2*c**5 + 2*A*a**3*b*c**6 + 6*A*a**2*b**6*c**2 + 30*A*a**2*b**5*c**3 + 32*A*a**2*b**4*c**4 - 2*A*a**2*b**3*c**5 + 6*A*a**2*b**2*c**6 + 6*A*a*b**6*c**3 + 18*A*a*b**5*c**4 + 2*A*a*b**4*c**5 + 6*A*a*b**3*c**6 + 2*A*b**6*c**4 + 4*A*b**5*c**5 + 2*A*b**4*c**6 + 2*B*a**6*b**3*c + 6*B*a**6*b**2*c**2 + 6*B*a**6*b*c**3 + 2*B*a**6*c**4 + 6*B*a**5*b**4*c + 6*B*a**5*b**3*c**2 - 2*B*a**5*b**2*c**3 + 2*B*a**5*b*c**4 + 4*B*a**5*c**5 + 6*B*a**4*b**5*c + 10*B*a**4*b**4*c**2 + 20*B*a**4*b**3*c**3 + 32*B*a**4*b**2*c**4 + 18*B*a**4*b*c**5 + 2*B*a**4*c**6 + 2*B*a**3*b**6*c + 10*B*a**3*b**5*c**2 + 32*B*a**3*b**4*c**3 + 48*B*a**3*b**3*c**4 + 30*B*a**3*b**2*c**5 + 6*B*a**3*b*c**6 - 2*B*a**2*b**5*c**3 + 10*B*a**2*b**4*c**4 + 18*B*a**2*b**3*c**5 + 6*B*a**2*b**2*c**6 - 6*B*a*b**6*c**3 - 10*B*a*b**5*c**4 - 2*B*a*b**4*c**5 + 2*B*a*b**3*c**6 - 4*B*b**6*c**4 - 4*B*b**5*c**5 + 2*C*a**6*b**4 + 6*C*a**6*b**3*c + 6*C*a**6*b**2*c**2 + 2*C*a**6*b*c**3 + 4*C*a**5*b**5 + 18*C*a**5*b**4*c + 30*C*a**5*b**3*c**2 + 18*C*a**5*b**2*c**3 - 2*C*a**5*b*c**4 - 4*C*a**5*c**5 + 2*C*a**4*b**6 + 2*C*a**4*b**5*c + 32*C*a**4*b**4*c**2 + 48*C*a**4*b**3*c**3 + 10*C*a**4*b**2*c**4 - 10*C*a**4*b*c**5 - 4*C*a**4*c**6 + 6*C*a**3*b**6*c - 2*C*a**3*b**5*c**2 + 20*C*a**3*b**4*c**3 + 32*C*a**3*b**3*c**4 - 2*C*a**3*b**2*c**5 - 6*C*a**3*b*c**6 + 6*C*a**2*b**6*c**2 + 6*C*a**2*b**5*c**3 + 10*C*a**2*b**4*c**4 + 10*C*a**2*b**3*c**5 + 2*C*a*b**6*c**3 + 6*C*a*b**5*c**4 + 6*C*a*b**4*c**5 + 2*C*a*b**3*c**6
    p = poly(g, (A, B, C))
    print('Is g = ...A + ...B + ...C + ...ABC?', expand(p.nth(1, 0, 0)*A + p.nth(0, 1, 0)*B + p.nth(0, 0, 1)*C + p.nth(1, 1, 1)*A*B*C) == g)
    print(f'g = A({p.nth(1, 0, 0)})')
    print(f'  + B({p.nth(0, 1, 0)})')
    print(f'  + C({p.nth(0, 0, 1)})')
    print(f'+ ABC({p.nth(1, 1, 1)})')
    print('...A + ...B + ...C =', factor((p.nth(1, 0, 0)*A + p.nth(0, 1, 0)*B + p.nth(0, 0, 1)*C).subs(A, sqrt(b + c)).subs(B, sqrt(c + a)).subs(C, sqrt(a + b)).subs(a, c*(1 + u)).subs(b, c*(1 + v))))
    # should prove ...A + ...B + ...C >= 0
    print('...(ABC) =', factor(p.nth(1, 1, 1).subs(a, c*(1 + u)).subs(b, c*(1 + v))))
    # should prove ...ABC <= 0

    h = (p.nth(1, 0, 0)*A + p.nth(0, 1, 0)*B + p.nth(0, 0, 1)*C)**2 - (p.nth(1, 1, 1)*A*B*C)**2
    h = expand(h.subs(A**2, b + c).subs(B**2, c + a).subs(C**2, a + b)).subs(sqrt(a + b), C).subs(sqrt(b + c), A).subs(sqrt(c + a), B)
    # numeric validation
    # print('h =', factor(h.subs(A, sqrt(b + c)).subs(B, sqrt(c + a)).subs(C, sqrt(a + b)).subs(a, c*(1 + u)).subs(b, c*(1 + v))))
    p = poly(h, (A, B, C))
    print('Is h = ... + ...AB + ...BC + ...CA?', expand(p.nth(0, 0, 0) + p.nth(1, 1, 0)*A*B + p.nth(0, 1, 1)*B*C + p.nth(1, 0, 1)*C*A) == h)
    print(f'h = ({p.nth(0, 0, 0)})')
    print(f'+ AB({p.nth(1, 1, 0)})')
    print(f'+ BC({p.nth(0, 1, 1)})')
    print(f'+ CA({p.nth(1, 0, 1)})')
    # too complicated to prove ...

if __name__ == '__main__':
    main()