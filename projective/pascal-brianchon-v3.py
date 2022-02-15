from sympy import symbols
from homogeneous import *

def polar(P):
    x, y, z = P[0], P[1], P[2]
    a, b = symbols('a, b')
    # result from pole-polar-v.py
    return a*y - b*y + b*z, a*x - a*z - b*x, -a*y + b*x

def main():
    A, B, C = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    aa, bb, cc = polar(A), polar(B), polar(C)
    print('A\'s Tangent:', aa)
    print('B\'s Tangent:', bb)
    print('C\'s Tangent:', cc)
    AB, BC, CA = cross(A, B), cross(B, C), cross(C, A)
    G, H, J = cross(AB, cc), cross(BC, aa), cross(CA, bb)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear/concurrent?', incidence(G, H, J) == 0)
    D, E, F = cross(bb, cc), cross(cc, aa), cross(aa, bb)
    AD, BE, CF = cross(A, D), cross(B, E), cross(C, F)
    print('AD:', AD)
    print('BE:', BE)
    print('CF:', CF)
    print('Are AD, BE and CF concurrent/collinear?', incidence(AD, BE, CF) == 0)

if __name__ == '__main__':
    main()