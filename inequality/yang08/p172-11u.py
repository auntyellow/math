from sympy import *

# ISBN 9787030207210, p172, §7.3.3, ex 11

def main():
    x, y, z = symbols('x, y, z', negative = False)
    f = 2572755344*x**4 - 20000000*x**3*y - 6426888360*x**3*z + 30000000*x**2*y**2 \
        + 5315682897*x**2*z**2 - 20000000*x*y**3 - 1621722090*x*z**3 + 170172209*y**4 \
        - 1301377672*y**3*z + 3553788598*y**2*z**2 - 3864133016*y*z**3 \
        + 1611722090*z**4
    u, v = symbols('u, v')
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(xzy) =', factor(f.subs(z, x*(1 + u)).subs(y, x*(1 + u + v))))
    print('f(yxz) =', factor(f.subs(x, y*(1 + u)).subs(z, y*(1 + u + v))))
    print('f(yzx) =', factor(f.subs(z, y*(1 + u)).subs(x, y*(1 + u + v))))
    print('f(zxy) =', factor(f.subs(x, z*(1 + u)).subs(y, z*(1 + u + v))))
    print('f(zyx) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    # f(xyz)
    g1 = 170172209*u**4 + 660688836*u**3*v - 961033254*u**3 + 1631722090*u**2*v**2 - 2883099762*u**2*v + 1441549881*u**2 + 2582755344*u*v**3 - 1601722090*u*v**2 + 2883099762*u*v + 1611722090*v**4 + 961033254*v**3 + 2082238717*v**2
    print('g1(uv) =', factor(g1.subs(v, u*(1 + v))))
    print('g1(vu) =', factor(g1.subs(u, v*(1 + u))))
    # f(xzy)
    g2 = 170172209*u**4 + 20000000*u**3*v - 961033254*u**3 + 670688836*u**2*v**2 + 1441549881*u**2 - 620688836*u*v**3 + 1281377672*u*v**2 + 170172209*v**4 - 640688836*v**3 + 640688836*v**2
    print('g2(uv) =', factor(g2.subs(v, u*(1 + v))))
    print('g2(vu) =', factor(g2.subs(u, v*(1 + u))))
    # f(zxy)
    g3 = 2732927553*u**4 + 660688836*u**3*v + 3203444180*u**3 + 991033254*u**2*v**2 - 1922066508*u**2*v + 2082238717*u**2 + 660688836*u*v**3 - 1922066508*u*v**2 + 1281377672*u*v + 170172209*v**4 - 640688836*v**3 + 640688836*v**2
    print('g3(uv) =', factor(g3.subs(v, u*(1 + v))))
    print('g3(vu) =', factor(g3.subs(u, v*(1 + u))))

if __name__ == '__main__':
    main()