from sympy import *

# ISBN 9787542848482, p36, §2.1, ex3
# x**2 + y**2 + z**2 + x*y*z = 4 -> 0 <= x*y + y*z + z*x - x*y*z <= 2

def dump(s, f):
    x0, y0, z0, l0 = s
    if x0 < 0 or y0 < 0 or z0 < 0:
        return
    x0, y0, z0 = simplify(x0), simplify(y0), simplify(z0)
    print('x =', x0)
    print('y =', y0)
    print('z =', z0)
    x, y, z = symbols('x, y, z')
    print('f_m =', N(f.subs(x, x0).subs(y, y0).subs(z, z0)))
    print()

def main():
    x, y, z, l = symbols('x, y, z, l')
    g = x**2 + y**2 + z**2 + x*y*z - 4
    f = x*y + y*z + z*x - x*y*z
    L = f + l*g
    Lx, Ly, Lz = diff(L, x), diff(L, y), diff(L, z)
    print('L_x =', Lx)
    print('L_y =', Ly)
    print('L_z =', Lz)
    print()
    ss = solve([Eq(Lx, 0), Eq(Ly, 0), Eq(Lz, 0), Eq(g, 0)], (x, y, z, l))
    for s in ss:
        dump(s, f)

    ss = solve([Eq(x, 0), Eq(Ly, 0), Eq(Lz, 0), Eq(g, 0)], (x, y, z, l))
    for s in ss:
        dump(s, f)

    ss = solve([Eq(x, 0), Eq(y, 0), Eq(Lz, 0), Eq(g, 0)], (x, y, z, l))
    for s in ss:
        dump(s, f)

if __name__ == '__main__':
    main()