from sympy import *

# https://math.stackexchange.com/q/4261358

def main():
    l, x, y, z = symbols('l, x, y, z', negative = False)
    g = x**3 + y**3 + z**3 - 3
    f = x + y + z - x**3*y**3 - x**3*z**3 - y**3*z**3
    L = f + l*g
    Lx, Ly, Lz = diff(L, x), diff(L, y), diff(L, z)
    # too slow
    B = groebner([Lx, Ly, Lz, g], l, x, y, z)

if __name__ == '__main__':
    main()