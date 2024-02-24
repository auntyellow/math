from sympy import *

# https://math.stackexchange.com/q/4741634

def main():
    l, x, y, z = symbols('l, x, y, z', negative = False)
    g = x**2 + y**2 + z**2 + x*y*z - 4
    f = 4*(x*y + y*z + z*x - x*y*z) - (x*x*y + z)*(y*y*z + x)*(z*z*x + y)
    L = f + l*g
    Lx, Ly, Lz = diff(L, x), diff(L, y), diff(L, z)
    # too slow
    # B = groebner([Lx, Ly, Lz, g], l, x, y, z)

if __name__ == '__main__':
    main()