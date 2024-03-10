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

def perpendicular(P1, P2, P3, P4):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = P1, P2, P3, P4
    return (x1 - x2)*(x3 - x4) + (y1 - y2)*(y3 - y4)

def main():
    # https://en.wikipedia.org/wiki/Simson_line
    var('x1:11')
    A, B, C, P, F, E, D = (0, 0), (0, 1), (x1, x2), (x3, x4), (x5, x6), (x7, x8), (x9, x10)
    h1 = det(concyclic, A, B, C, P) # x3, x4
    h2 = det(collinear, A, B, F)    # x5
    h3 = perpendicular(A, B, F, P)  # x5, x6
    h4 = det(collinear, C, A, E)    # x7, x8
    h5 = perpendicular(C, A, E, P)  # x7, x8
    h6 = det(collinear, B, C, D)    # x9, x10
    h7 = perpendicular(B, C, D, P)  # x9, x10
    g = det(collinear, D, E, F)     # x9, x10
    h6a = prem(h7, h6, x10)
    h4a = prem(h5, h4, x8)
    R = prem(g, h7, x10)
    print('R(x10) =', R)
    R = prem(R, h6a, x9)
    print('R(x9) =', R)
    R = prem(R, h5, x8)
    print('R(x8) =', R)
    R = prem(R, h4a, x7)
    print('R(x7) =', R)
    R = prem(R, h3, x6)
    print('R(x6) =', R)
    R = prem(R, h2, x5)
    print('R(x5) =', R)
    R = prem(R, h1, x4)
    print('R(x4) =', R)

if __name__ == '__main__':
    main()