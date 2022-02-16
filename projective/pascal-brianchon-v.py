from sympy import symbols
from homogeneous import *

def polar(P):
    x, y, z = P[0], P[1], P[2]
    a, b = symbols('a, b')
    # result from pole-polar-v.py
    return a*y - b*y + b*z, a*x - a*z - b*x, -a*y + b*x

def main():
    a, b, t = symbols('a, b, t')
    # results from steiner-conic-v.py
    A, B, C, D, E, F = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (a + 1, b + 1, (a + 1)*(b + 1)), (t*(a + t), t*(b + t), (a + t)*(b + t))
    AB, BC, CD, DE, EF, FA = cross(A, B), cross(B, C), cross(C, D), cross(D, E), cross(E, F), cross(F, A)
    G, H, J = cross(AB, DE), cross(BC, EF), cross(CD, FA)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear/concurrent?', incidence(G, H, J) == 0)

    AA, BB, CC, DD, EE, FF = polar(A), polar(B), polar(C), polar(D), polar(E), polar(F)
    print('A\'s Tangent:', AA)
    print('B\'s Tangent:', BB)
    print('C\'s Tangent:', CC)
    print('D\'s Tangent:', DD)
    print('E\'s Tangent:', EE)
    print('F\'s Tangent:', FF)
    K, L, M, N, P, Q = cross(AA, BB), cross(BB, CC), cross(CC, DD), cross(DD, EE), cross(EE, FF), cross(FF, AA)
    KN, LP, MQ = cross(K, N), cross(L, P), cross(M, Q)
    print('KN:', KN)
    print('LP:', LP)
    print('MQ:', MQ)
    print('Are KN, LP and MQ concurrent/collinear?', incidence(KN, LP, MQ) == 0)

if __name__ == '__main__':
    main()