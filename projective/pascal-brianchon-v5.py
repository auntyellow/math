from sympy import symbols
from homogeneous import *

def polar(P):
    x, y, z = P[0], P[1], P[2]
    a, b = symbols('a, b')
    # result from pole-polar-v.py
    return a*y - b*y + b*z, a*x - a*z - b*x, -a*y + b*x

def main():
    a, b = symbols('a, b')
    # results from steiner-conic-v.py
    A, B, C, D, E = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (a + 1, b + 1, (a + 1)*(b + 1))
    AA, BB, CC, DD, EE = polar(A), polar(B), polar(C), polar(D), polar(E)
    print('A\'s Tangent:', AA)
    print('B\'s Tangent:', BB)
    print('C\'s Tangent:', CC)
    print('D\'s Tangent:', DD)
    print('E\'s Tangent:', EE)

    AB, BC, CD, DE, EA = cross(A, B), cross(B, C), cross(C, D), cross(D, E), cross(E, A)
    G, H, J = cross(AB, DE), cross(BC, EA), cross(CD, AA)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear/concurrent?', incidence(G, H, J) == 0)

    K, L, M, N, P = cross(AA, BB), cross(BB, CC), cross(CC, DD), cross(DD, EE), cross(EE, AA)
    AM, KN, LP = cross(A, M), cross(K, N), cross(L, P)
    print('AM:', AM)
    print('KN:', KN)
    print('LP:', LP)
    print('Are AM, KN and LP concurrent/collinear?', incidence(AM, KN, LP) == 0)

if __name__ == '__main__':
    main()