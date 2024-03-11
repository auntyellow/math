from sympy import *

def main():
    # https://imomath.com/index.cgi?page=inversion (Problem 11)
    # projectively transform the hexahedron into a cube, then the sphere becomes a quadric surface
    a, b, c, d, e, f, g, h, j, k, x, y, z = symbols('a, b, c, d, e, f, g, h, j, k, x, y, z')
    surface = (Matrix([[x, y, z, 1]])*Matrix([[a, b, c, d], [b, e, f, g], [c, f, h, j], [d, g, j, k]])*Matrix([[x], [y], [z], [1]]))[0, 0]
    print('surface:', Poly(surface, x, y, z), '= 0')
    eq1 = surface.subs({x: 0, y: 0, z: 0})
    eq2 = surface.subs({x: 1, y: 0, z: 0})
    eq3 = surface.subs({x: 0, y: 1, z: 0})
    eq4 = surface.subs({x: 0, y: 0, z: 1})
    eq5 = surface.subs({x: 1, y: 1, z: 0})
    eq6 = surface.subs({x: 1, y: 0, z: 1})
    eq7 = surface.subs({x: 0, y: 1, z: 1})
    s = solve([eq1, eq2, eq3, eq4, eq5, eq6, eq7], a, b, c, d, e, f, g, h, j, k)
    print(s)
    print('Is (1, 1, 1) on the surface?', surface.subs(s).subs({x: 1, y: 1, z: 1}) == 0)
    print('Is (-1, -1, -1) on the surface?', surface.subs(s).subs({x: -1, y: -1, z: -1}) == 0)

if __name__ == '__main__':
    main()