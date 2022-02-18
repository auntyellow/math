from sympy import symbols
from homogeneous import *

def main():
    a, b, c = symbols('a, b, c')
    # desargues.md, trick 2a
    O, A1, B1, C1, A2, B2, C2 = (1, 1, 1), (1, 0, 0), (0, 1, 0), (0, 0, 1), (a + 1, 1, 1), (1, b + 1, 1), (1, 1, c + 1)
    # desargues.md, trick 2b
    # O, A1, B1, C1, A2, B2, C2 = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, a, 1), (1, 1, 0), (1, 0, b), (c + 1, a, 1)
    # desargues.md, trick 2c
    # O, A1, B1, C1, A2, B2, C2 = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, a, b), (1, 1, 0), (1, 0, 1), (c + 1, a, b)
    print('Are O, A1 and A2 collinear/concurrent?', incidence(O, A1, A2) == 0)
    print('Are O, B1 and B2 collinear/concurrent?', incidence(O, B1, B2) == 0)
    print('Are O, C1 and C2 collinear/concurrent?', incidence(O, C1, C2) == 0)
    print('Are A1A2, B1B2 and C1C2 concurrent/collinear?', incidence(cross(A1, A2), cross(B1, B2), cross(C1, C2)) == 0)
    A1B1, A1C1, B1C1 = cross(A1, B1), cross(A1, C1), cross(B1, C1)
    A2B2, A2C2, B2C2 = cross(A2, B2), cross(A2, C2), cross(B2, C2)
    G, H, J = cross(A1B1, A2B2), cross(A1C1, A2C2), cross(B1C1, B2C2)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear/concurrent?', incidence(G, H, J) == 0)

if __name__ == '__main__':
    main()