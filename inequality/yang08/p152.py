from sympy import *

# ISBN 9787030207210, p152, §7

def main():
    x, y, z = symbols('x, y, z', negative = False)
    f0 = x**6 + y**6 + 2*x**5*y + 5*y**4*x**2 + 4*x*y**5
    print('f =', f0)
    # x >= 0 and y >= 0: obvious positive
    u, v = symbols('u, v', negative = False)
    # x >= 0 and y <= 0:
    f = f0.subs(y, -y)
    print('f =', f)
    print('f(xy) =', factor(f.subs(y, x*(1 + u))))
    print('f(yx) =', factor(f.subs(x, y*(1 + u))))
    # x <= 0 and y >= 0: identical to x >= 0 and y <= 0
    f = f0.subs(x, -x)
    print('f =', f)
    # x <= 0 and y <= 0: identical to x >= 0 and y >= 0
    f = f0.subs(x, -x).subs(y, -y)
    print('f =', f)
    print()

    # p153, §7.1
    f = z**3 + x**2*y + y**2*x - 3*x*y*z
    print('f =', f)
    # x and y are symmetric
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(yzx) =', factor(f.subs(z, y*(1 + u)).subs(x, y*(1 + u + v)))) # g    
    print('f(zxy) =', factor(f.subs(x, z*(1 + u)).subs(y, z*(1 + u + v))))
    g = u**3 + u**2 - u*v + v**2
    print('g(uv) =', factor(g.subs(v, u*(1 + v))))
    print('g(vu) =', factor(g.subs(u, v*(1 + u))))
    print()

    f = x**3 + y**3 + z**3 - (x**2*y + x**2*z + y**2*x + y**2*z + z**2*x + z**2*y) + 3*x*y*z
    print('f =', f)
    # x, y and z are symmetric
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print()

    # p156
    f = 10195920*z**8 + 2109632*z**7 - 5387520*z**6 + 1361336*z**5 + 61445*z**4 - 52468*z**3 + 6350*z**2 - 300*z + 5
    print('y =', f.subs(z, x))
    # proved by polynomial-prover

if __name__ == '__main__':
    main()