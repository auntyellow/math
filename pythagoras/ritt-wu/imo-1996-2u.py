from sympy import *

def collinear(P):
    return [P[0], P[1], 1]

def concyclic(P):
    x, y = P
    return [x**2 + y**2, x, y, 1]

def det(row_def, *points):
    mat = []
    for point in points:
        mat.append(row_def(point))
    return Matrix(mat).det()

def dist(P1, P2, d2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2 - d2

def main():
    # https://imomath.com/index.cgi?page=inversion (Example 2)
    b, c, d, e, p = symbols('b, c, d, e, p', positive = True)
    A, B, C, P = (0, 0), (b, -d), (c, e), (p, 0)
    # angles are converted to tan
    APB, APC = -(b - p)/d, -(c - p)/e

if __name__ == '__main__':
    main()