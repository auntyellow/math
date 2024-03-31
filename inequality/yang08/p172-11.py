from sympy import *

# ISBN 9787030207210, p172, §7.3.3, ex 11

def main():
    x, y, z = symbols('x, y, z', negative = False)
    f = 2572755344*x**4 - 20000000*x**3*y - 6426888360*x**3*z + 30000000*x**2*y**2 \
        + 5315682897*x**2*z**2 - 20000000*x*y**3 - 1621722090*x*z**3 + 170172209*y**4 \
        - 1301377672*y**3*z + 3553788598*y**2*z**2 - 3864133016*y*z**3 \
        + 1611722090*z**4
    u, v = symbols('u, v', negative = False) # 0 <= u, v <= 1
    # proved by Bisection
    print('f(x=max(xyz)) =', factor(f.subs(y, x*(1 - u)).subs(z, x*(1 - v))))
    print('f(y=max(xyz)) =', factor(f.subs(x, y*(1 - u)).subs(z, y*(1 - v))))
    print('f(z=max(xyz)) =', factor(f.subs(x, z*(1 - u)).subs(y, z*(1 - v))))

if __name__ == '__main__':
    main()