from sympy import Matrix, prem, var

def collinear(x, y):
    return [x, y, 1]

def concyclic(x, y):
    return [x**2 + y**2, x, y, 1]

def det(row_def, *points):
    mat = []
    for point in points:
        mat.append(row_def(point[0], point[1]))
    return Matrix(mat).det()

def perpendicular(P1, P2, P3, P4):
    x1, y1, x2, y2, x3, y3, x4, y4 = P1[0], P1[1], P2[0], P2[1], P3[0], P3[1], P4[0], P4[1]
    return (x1 - x2)*(x3 - x4) + (y1 - y2)*(y3 - y4)

def main():
    # https://en.wikipedia.org/wiki/Simson_line
    var('x1:11')
    A, B, C, P, D, E, F = (0, 0), (0, 1), (x1, x2), (x3, x4), (x5, x6), (x7, x8), (x9, x10) 
    h1 = det(concyclic, A, B, C, P)
    print('h1 =', h1)
    h2 = det(collinear, B, C, D)
    print('h2 =', h2)
    h3 = perpendicular(B, C, D, P)
    print('h3 =', h3)
    h4 = det(collinear, C, A, E)
    print('h4 =', h4)
    h5 = perpendicular(C, A, E, P)
    print('h5 =', h5)
    h6 = det(collinear, A, B, F)
    print('h6 =', h6)
    h7 = perpendicular(A, B, F, P)  
    print('h7 =', h7)
    g = det(collinear, D, E, F)
    print('g =', g) 

if __name__ == '__main__':
    main()