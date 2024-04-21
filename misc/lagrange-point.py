from sympy import *

# https://en.wikipedia.org/wiki/Lagrange_point

def main():
    G, M, R, r = symbols('G, M, R, r', positive = True)
    x, y = symbols('x, y')
    m = M*r/R
    omega2 = G*M/R/(R + r)**2
    # potential of large body
    V_M = G*M/sqrt((x + r)**2 + y**2)
    # potential of small body
    V_m = G*m/sqrt((x - R)**2 + y**2)
    # potential of centrifugal force
    V_c = omega2*(x**2 + y**2)/2
    V = V_M + V_m + V_c
    print('V =', V)
    # TODO: solve V_x = 0 and V_y = 0

if __name__ == '__main__':
    main()