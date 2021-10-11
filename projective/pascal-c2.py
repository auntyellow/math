from sympy import cancel, symbols
from cartesian import *

def main():
    a, b, c, d, e, f, g, h, k = symbols('a, b, c, d, e, f, g, h, k')
    #P = sqrt(-a*f - 2*b*f*g - c*f*g**2 + d**2 + 2*d*e*g + e**2*g**2)
    #Q = sqrt(-a*f - 2*b*f*h - c*f*h**2 + d**2 + 2*d*e*h + e**2*h**2)
    #R = sqrt(-a*c*k**2 - 2*a*e*k - a*f + b**2*k**2 + 2*b*d*k + d**2)
    P, Q, R = symbols('P, Q, R')
    x_A = -(d + e*g - P)/(a + 2*b*g + c*g**2)
    x_B = -(b*k + d + R)/a
    x_C = -(d + e*h - Q)/(a + 2*b*h + c*h**2)
    x_D = -(d + e*h + Q)/(a + 2*b*h + c*h**2)
    x_E = -(b*k + d - R)/a
    x_F = -(d + e*g + P)/(a + 2*b*g + c*g**2)

    A, B, C, D, E, F = (x_A, g*x_A), (x_B, k), (x_C, h*x_C), (x_D, h*x_D), (x_E, k), (x_F, g*x_F)
    AB, DE, BC, EF = line(A, B), line(D, E), line(B, C), line(E, F)
    G, H = intersect(AB, DE), intersect(BC, EF)
    print('G:', G)
    print('H:', H)
    print(fraction(cancel(G[0]*H[1] - G[1]*H[0]))[0])

if __name__ == '__main__':
    main()