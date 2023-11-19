from sympy import *

# ISBN 9787030207210, p172, §7.3.3, ex 11

def main():
    x, y, z = symbols('x, y, z', positive = True)
    f = 2572755344*x**4 - 20000000*x**3*y - 6426888360*x**3*z + 30000000*x**2*y**2 \
        + 5315682897*x**2*z**2 - 20000000*x*y**3 - 1621722090*x*z**3 + 170172209*y**4 \
        - 1301377672*y**3*z + 3553788598*y**2*z**2 - 3864133016*y*z**3 \
        + 1611722090*z**4
    u, v = symbols('u, v')
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v)))) # *
    print('f(xzy) =', factor(f.subs(z, x*(1 + u)).subs(y, x*(1 + u + v))))
    print('f(yxz) =', factor(f.subs(x, y*(1 + u)).subs(z, y*(1 + u + v))))
    print('f(yzx) =', factor(f.subs(z, y*(1 + u)).subs(x, y*(1 + u + v))))
    print('f(zxy) =', factor(f.subs(x, z*(1 + u)).subs(y, z*(1 + u + v)))) # *
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    # f(xzy)
    g = 170172209*u**4 + 20000000*u**3*v - 961033254*u**3 + 670688836*u**2*v**2 + 1441549881*u**2 - 620688836*u*v**3 + 1281377672*u*v**2 + 170172209*v**4 - 640688836*v**3 + 640688836*v**2
    print('g(uv) =', factor(g.subs(v, u*(1 + v))))
    print('g(vu) =', factor(g.subs(u, v*(1 + u))))
    # g(uv), critical point near (0, +oo) and (0, 0) ...
    h1 = 170172209*u**2*v**4 + 60000000*u**2*v**3 - 170344418*u**2*v**2 + 180000000*u**2*v + 410344418*u**2 - 640688836*u*v**3 - 640688836*u*v**2 + 640688836*u*v - 320344418*u + 640688836*v**2 + 1281377672*v + 2082238717
    # g(vu), critical point near (+oo, 0) and (0, 0) ...
    h2 = 170172209*u**4*v**2 + 700688836*u**3*v**2 - 961033254*u**3*v + 1751722090*u**2*v**2 - 2883099762*u**2*v + 1441549881*u**2 + 1461377672*u*v**2 - 1601722090*u*v + 2883099762*u + 410344418*v**2 - 320344418*v + 2082238717

if __name__ == '__main__':
    main()