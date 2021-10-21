from sympy import expand, poly, symbols
from homogeneous import *

def append_coeffs(mat, vec, P):
    x, y, z = P[0], P[1], P[2]
    mat.append([x**2, x*y, y**2, x*z, y*z])
    vec.append([-z**2])

def on_conic(conic, P):
    x, y, z = symbols('x, y, z')
    return expand(conic.subs(x, P[0]).subs(y, P[1]).subs(z, P[2])) == 0

def main():
    a0, a1, a2, b0, b1, b2, c0, c1, c2, d0, d1, d2, e0, e1, e2, x, y, z = symbols('a0, a1, a2, b0, b1, b2, c0, c1, c2, d0, d1, d2, e0, e1, e2, x, y, z')
    # a1 = 0 can speed up calculation (AF on x-axis)
    # For Brianchon's theorem, a1 = 0 makes lines A and F intersect at infinity on y-axis, so use a2 = 0 instead (lines A and F intersect at origin)
    A, B, C, D, E = (a0, a1, a2), (b0, b1, b2), (c0, c1, c2), (d0, d1, d2), (e0, e1, e2)
    mat, vec = [], []
    append_coeffs(mat, vec, A)
    append_coeffs(mat, vec, B)
    append_coeffs(mat, vec, C)
    append_coeffs(mat, vec, D)
    append_coeffs(mat, vec, E)
    mat = Matrix(mat)
    vec = mat.adjugate()*Matrix(vec)
    a, b, c, d, e, f = expand(vec[0, 0]), expand(vec[1, 0]), expand(vec[2, 0]), expand(vec[3, 0]), expand(vec[4, 0]), expand(mat.det())
    # Nothing to reduce
    # print(gcd_list([a, b, c, d, e, f]))
    conic = a*x**2 + b*x*y + c*y**2 + d*x*z + e*y*z + f*z**2
    print('Conic Equation in Homogeneous:', conic, '= 0')
    print('Is A on Conic?', on_conic(conic, A))
    print('Is B on Conic?', on_conic(conic, B))
    print('Is C on Conic?', on_conic(conic, C))
    print('Is D on Conic?', on_conic(conic, D))
    print('Is E on Conic?', on_conic(conic, E))
    # Make AF parallel to x-axis
    # For Brianchon's theorem, this makes lines A and F intersect on y-axis
    conic_coeffs = poly(conic.subs(y, a1).subs(z, a2), x).all_coeffs()
    # Vieta's formula: x_A + x_F = -b/a
    F = multiplied(-conic_coeffs[1]/conic_coeffs[0] - a0, a1, a2)
    print('F:', F)
    # This takes too much time. Can set more zeros (e.g. b0 = 0, c2 = 0) to verify.
    # print('Is F on Conic?', on_conic(conic, F))

    AB, BC, CD, DE, EF, FA = cross(A, B), cross(B, C), cross(C, D), cross(D, E), cross(E, F), cross(F, A)
    G, H, J = cross(AB, DE), cross(BC, EF), cross(CD, FA)
    print('G:', G)
    print('H:', H)
    print('J:', J)
    print('Are GHJ collinear/concurrent?', incidence(G, H, J) == 0)

if __name__ == '__main__':
    main()