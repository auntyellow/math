from sympy import symbols
from homogeneous import *

def polar(P):
    x, y, z = P
    a, b = symbols('a, b')
    # result from pole-polar-v.py
    return a*y - b*y + b*z, a*x - a*z - b*x, -a*y + b*x

def main():
    A, B, C = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    AA, BB, CC = polar(A), polar(B), polar(C)
    print('A\'s Tangent:', AA)
    print('B\'s Tangent:', BB)
    print('C\'s Tangent:', CC)
    AB, BC, CA = cross(A, B), cross(B, C), cross(C, A)
    G, H, J = cross(AB, CC), cross(BC, AA), cross(CA, BB)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear/concurrent?', incidence(G, H, J) == 0)
    D, E, F = cross(BB, CC), cross(CC, AA), cross(AA, BB)
    AD, BE, CF = cross(A, D), cross(B, E), cross(C, F)
    print('AD:', AD)
    print('BE:', BE)
    print('CF:', CF)
    print('Are AD, BE and CF concurrent/collinear?', incidence(AD, BE, CF) == 0)

if __name__ == '__main__':
    main()