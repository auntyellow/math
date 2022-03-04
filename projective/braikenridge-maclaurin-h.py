from sympy import symbols
from homogeneous import *

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q')
    A, C, E, G, H, J = (a, b, c), (d, e, f), (g, 0, h), (0, j, k), (0, m, n), (0, p, q)
    # The dual theorem is also proved when lines GHJ are parallel.
    # To prove the common case that GHJ are concurrent, we should use:
    # A, C, E, G, H, J = (a, b, c), (d, e, f), (g, 0, h), (j, k, 0), (m, n, 0), (p, q, 0)
    AB, BC, CD, DE, EF, FA = cross(A, G), cross(H, C), cross(C, J), cross(G, E), cross(E, H), cross(J, A)
    B, D, F = cross(AB, BC), cross(CD, DE), cross(EF, FA)
    print('B:', B)
    print('D:', D)
    print('F:', F)

    mat = []
    for P in [A, B, C, D, E, F]:
        x, y, z = P[0], P[1], P[2]
        mat.append([x*x, x*y, y*y, x*z, y*z, z*z])
    print('M =', Matrix(mat))
    print('det M =', Matrix(mat).det(method='domain-ge'))

if __name__ == '__main__':
    main()