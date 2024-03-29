from sympy import *

def reduced(coordinates):
    gcd = gcd_list(coordinates)
    reduced = []
    for i in coordinates:
        reduced.append(cancel(i/gcd))
    return reduced

def cross(P1, P2, P3):
    x10, x11, x12, x13 = P1
    x20, x21, x22, x23 = P2
    x30, x31, x32, x33 = P3
    # generated by cross-3d.py
    x = -x11*x22*x33 + x11*x23*x32 + x12*x21*x33 - x12*x23*x31 - x13*x21*x32 + x13*x22*x31
    y = x10*x22*x33 - x10*x23*x32 - x12*x20*x33 + x12*x23*x30 + x13*x20*x32 - x13*x22*x30
    z = -x10*x21*x33 + x10*x23*x31 + x11*x20*x33 - x11*x23*x30 - x13*x20*x31 + x13*x21*x30
    w = x10*x21*x32 - x10*x22*x31 - x11*x20*x32 + x11*x22*x30 + x12*x20*x31 - x12*x21*x30
    return reduced([x, y, z, w])

def plucker_list(Lx):
    return reduced([Lx[0, 1], Lx[0, 2], Lx[0, 3], Lx[1, 2], Lx[1, 3], Lx[2, 3]])

def plucker_matrix(L):
    return Matrix([[0, L[0], L[1], L[2]], [-L[0], 0, L[3], L[4]], [-L[1], -L[3], 0, L[5]], [-L[2], -L[4], -L[5], 0]])

def main():
    a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3, e0, e1, e2, e3, m, n = \
        symbols('a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3, e0, e1, e2, e3, m, n')
    A, B = Matrix([[a0 + m*b0, a1 + m*b1, a2 + m*b2, a3 + m*b3]]), Matrix([[a0 + n*b0, a1 + n*b1, a2 + n*b2, a3 + n*b3]])
    Lx = A.transpose()*B - B.transpose()*A
    L = plucker_list(Lx)
    print('L =', L)
    Lx = plucker_matrix(L)
    print('Lx =', Lx)
    print('det Lx =', Lx.det())
    A, B, C, D, E = [a0, a1, a2, a3], [b0, b1, b2, b3], [c0, c1, c2, c3], [d0, d1, d2, d3], [e0, e1, e2, e3]
    CDE = Matrix([cross(C, D, E)])
    F = expand(CDE*Lx).tolist()[0]
    print('Intersection F of AB and CDE:', F)
    print('Are ABF collinear?', Matrix([A, B, F]).rank() == 2)
    print('Are CDEF coplanar?', Matrix([C, D, E, F]).det() == 0)
    ABC, ABD = Matrix([cross(A, B, C)]), Matrix([cross(A, B, D)])
    print('Intersection of ABC and AB:', expand(ABC*Lx))
    Kx = ABC.transpose()*ABD - ABD.transpose()*ABC
    K = plucker_list(Kx)
    print('dual L =', K)
    Kx = plucker_matrix(K)
    print('dual Lx =', Kx)
    print('Their Product:', expand(Lx*Kx))
    print('Plane passing through AB and F:', expand(Matrix([F])*Kx))

if __name__ == '__main__':
    main()