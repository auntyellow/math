from sympy import *

def collinear(P):
    return [P[0], P[1], 1]

def det(row_def, *points):
    mat = []
    for point in points:
        mat.append(row_def(point))
    return Matrix(mat).det()

def perpendicular(P1, P2, P3, P4):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = P1, P2, P3, P4
    return (x1 - x2)*(x3 - x4) + (y1 - y2)*(y3 - y4)

def main():
    var('x1:11')
    A, B, C, F, E, D, H = (0, 0), (0, 1), (x1, x2), (x3, x4), (x5, x6), (x7, x8), (x9, x10)
    h1 = det(collinear, A, B, F)   # x3
    h2 = perpendicular(A, B, F, C) # x3, x4
    h3 = det(collinear, C, A, E)   # x5, x6
    h4 = perpendicular(C, A, E, B) # x5, x6
    h5 = det(collinear, B, C, D)   # x7, x8
    h6 = perpendicular(B, C, D, A) # x7, x8
    h7 = det(collinear, A, D, H)   # x9, x10
    h8 = det(collinear, B, E, H)   # x9, x10
    g = det(collinear, C, F, H)    # x9, x10
    h7a = prem(h8, h7, x10)
    h5a = prem(h6, h5, x8)
    h3a = prem(h4, h3, x6)
    R = prem(g, h8, x10)
    print('R(x10) =', R)
    R = prem(R, h7a, x9)
    print('R(x9) =', R)
    R = prem(R, h6, x8)
    print('R(x8) =', R)
    R = prem(R, h5a, x7)
    print('R(x7) =', R)
    R = prem(R, h4, x6)
    print('R(x6) =', R)
    R = prem(R, h3a, x5)
    print('R(x5) =', R)
    R = prem(R, h2, x4)
    print('R(x4) =', R)
    R = prem(R, h1, x3)
    print('R(x3) =', R)

if __name__ == '__main__':
    main()