from sympy import *

# https://en.wikipedia.org/wiki/Lagrange_point

def main():
    G, GM, M, R, r, u, v = symbols('G, GM, M, R, r, u, v', positive = True)
    x, y = symbols('x, y')
    m = M*r/R
    omega2 = G*M/R/(R + r)**2
    # potential of large body
    V_M = -G*M/sqrt((x + r)**2 + y**2)
    # potential of small body
    V_m = -G*m/sqrt((x - R)**2 + y**2)
    # potential of centrifugal force
    V_c = -omega2*(x**2 + y**2)/2
    V = V_M + V_m + V_c
    print('V =', V)
    print('V_x =', diff(V, x))
    print('V_y =', diff(V, y))
    print()

    V_x = -G*M*(-r - x)/u**3 - G*M*r*(R - x)/(R*v**3) - G*M*x/(R*(R + r)**2)
    V_y = G*M*y/u**3 + G*M*r*y/(R*v**3) - G*M*y/(R*(R + r)**2)
    for f in [factor(V_x), factor(V_y), factor((x + r)**2 + y**2 - u**2), factor((x - R)**2 + y**2 - v**2)]:
        print(f, '= 0')
    print()

    f1 = -R**3*r*u**3 + R**3*r*v**3 + R**3*v**3*x - 2*R**2*r**2*u**3 + 2*R**2*r**2*v**3 + R**2*r*u**3*x + 2*R**2*r*v**3*x - R*r**3*u**3 + R*r**3*v**3 + 2*R*r**2*u**3*x + R*r**2*v**3*x + r**3*u**3*x - u**3*v**3*x
    # y = 0 is also a solution
    f2 = R**3*v**3 + R**2*r*u**3 + 2*R**2*r*v**3 + 2*R*r**2*u**3 + R*r**2*v**3 + r**3*u**3 - u**3*v**3
    f3 = r**2 + 2*r*x - u**2 + x**2 + y**2
    f4 = R**2 - 2*R*x - v**2 + x**2 + y**2
    # too slow
    B = groebner([f1, f3.subs(y, 0), f4.subs(y, 0)], u, v, x)
    print(B, len(B))

if __name__ == '__main__':
    main()