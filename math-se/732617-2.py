from sympy import *

def main():
    t, x, y, z = symbols('t, x, y, z')
    # https://math.stackexchange.com/a/4397060
    plane = Eq(4*x + 3*z + 29, 0)
    t = solve(plane.subs(x, -1 + 4*t).subs(y, 3).subs(z, 3*t), t)[0]
    print('t =', t)
    T = (-1 + 4*t, 3, 3*t)
    print('Tangent Point: ', T)
    C = (-1, 3, 0)
    print('Distance to Center: ', sqrt((C[0] - T[0])**2 + (C[1] - T[1])**2 + (C[2] - T[2])**2))

if __name__ == '__main__':
    main()