from sympy import *

# ISBN 9787542848482, p36, §2.1, ex3
# x**2 + y**2 + z**2 + x*y*z = 4 -> 0 <= x*y + y*z + z*x - x*y*z <= 2

def main():
    x, y, z = symbols('x, y, z')
    l = symbols('l')
    g = x**2 + y**2 + z**2 + x*y*z - 4
    f = x*y + y*z + z*x - x*y*z
    L = f + l*g
    Lx, Ly, Lz = diff(L, x), diff(L, y), diff(L, z)
    print('L_x =', Lx)
    print('L_y =', Ly)
    print('L_z =', Lz)
    # Unable to solve by SymPy
    # s = solve([Eq(Lx, 0), Eq(Ly, 0), Eq(Lz, 0), Eq(g, 0)], (x, y, z, l))

    l0 = solve(Eq(Lx, 0), l)
    print('l =', l0)
    l0 = l0[0]
    x0 = solve(Eq(Ly.subs(l, l0), 0), x)
    print('x =', x0)
    # skip x = y
    x0 = x0[1]
    y0 = solve(Eq(Lz.subs(l, l0), 0).subs(x, x0), y)
    print('y =', y0)
    # skip y = z
    y0 = y0[1]
    z0 = solve(Eq(g.subs(x, x0).subs(y, y0), 0), z)
    print('z =', z0)
    # only root "1/4 + sqrt(17)/4" makes y and x non-negative
    z0 = z0[3]
    y0 = y0.subs(z, z0)
    print('y =', y0)
    x0 = x0.subs(y, y0).subs(z, z0)
    print('x =', x0)
    f0 = f.subs(x, x0).subs(y, y0).subs(z, z0)
    print('f_m =', N(f0))
    print()

    # now try x = y
    x0 = y
    y0 = solve(Eq(Lz.subs(l, l0), 0).subs(x, x0), y)
    print('y =', y0)
    # skip y = z
    y0 = y0[2]
    z0 = solve(Eq(g.subs(x, x0).subs(y, y0), 0), z)
    print('z =', z0)
    z0 = z0[1]
    # only root "7/8 - sqrt(17)/8" makes y and x non-negative
    y0 = y0.subs(z, z0)
    print('y =', y0)
    x0 = x0.subs(y, y0).subs(z, z0)
    print('x =', x0)
    f0 = f.subs(x, x0).subs(y, y0).subs(z, z0)
    print('f_m =', N(f0))
    print()

    # now try x = y = z
    x0 = z
    y0 = z
    z0 = solve(Eq(g.subs(x, x0).subs(y, y0), 0), z)
    print('z =', z0)
    z0 = z0[1]
    # only root "1" makes y and x non-negative
    y0 = y0.subs(z, z0)
    print('y =', y0)
    x0 = x0.subs(y, y0).subs(z, z0)
    print('x =', x0)
    f0 = f.subs(x, x0).subs(y, y0).subs(z, z0)
    print('f_m =', f0)

if __name__ == '__main__':
    main()