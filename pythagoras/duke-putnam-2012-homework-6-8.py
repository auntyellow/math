from sympy import pi, cos, sin, integrate, simplify, symbols

def main():
    # https://imomath.com/index.cgi?page=psPutnamPreparationGeometry (Problem 8)
    a, r = symbols('a, r', positive = True)
    theta, t = symbols('theta, t')
    rho2 = a**2*(cos(theta)**2 - sin(theta)**2) + r**2
    A04 = simplify(integrate(rho2, (theta, t, t + pi/4)))
    A15 = simplify(integrate(rho2, (theta, t + pi/4, t + pi/2)))
    A26 = simplify(integrate(rho2, (theta, t + pi/2, t + 3*pi/4)))
    A37 = simplify(integrate(rho2, (theta, t + 3*pi/4, t + pi)))
    print('A04 =', A04)
    print('A15 =', A15)
    print('A26 =', A26)
    print('A37 =', A37)
    print('A04 + A26 =', A04 + A26)
    print('A15 + A37 =', A15 + A37)

if __name__ == '__main__':
    main()