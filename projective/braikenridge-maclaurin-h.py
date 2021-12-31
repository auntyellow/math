from sympy import symbols
from homogeneous import *

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, p, q, x, y, z = symbols('a, b, c, d, e, f, g, h, j, k, m, n, p, q, x, y, z')
    A, C, E, G, H, J = (a, b, c), (d, e, f), (g, 0, h), (0, j, k), (0, m, n), (0, p, q)
    # The dual theorem is also proved when lines GHJ are parallel.
    # To prove the common case that GHJ are concurrent, we should use:
    # A, C, E, G, H, J = (a, b, c), (d, e, f), (g, 0, h), (j, k, 0), (m, n, 0), (p, q, 0)
    AB, BC, CD, DE, EF, FA = cross(A, G), cross(H, C), cross(C, J), cross(G, E), cross(E, H), cross(J, A)
    B, D, F = cross(AB, BC), cross(CD, DE), cross(EF, FA)
    print('B:', B)
    print('D:', D)
    print('F:', F)
    points = [A, B, C, D, E, F]
    coefficients = [x**2, x*y, y**2, x*z, y*z, z**2]
    subs, mat = [], []
    for s in range(6):
        row = []
        for t in range(6):
            rst = symbols('r' + str(s) + str(t))
            subs.append((rst, coefficients[t].subs(x, points[s][0]).subs(y, points[s][1]).subs(z, points[s][2])))
            row.append(rst)
        mat.append(row)
    print('M =', Matrix(mat).subs(subs))
    print('det M =', expand(Matrix(mat).det().subs(subs)))

if __name__ == '__main__':
    main()