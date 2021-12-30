from sympy import poly, symbols
from homogeneous import *

def on_conic(conic, P):
    x, y, z = symbols('x, y, z')
    return expand(conic.subs(x, P[0]).subs(y, P[1]).subs(z, P[2])) == 0

def main():
    a0, a1, a2, b0, b1, b2, c0, c1, c2, d0, d1, d2, e0, e1, e2, x, y, z = symbols('a0, a1, a2, b0, b1, b2, c0, c1, c2, d0, d1, d2, e0, e1, e2, x, y, z')
    # a1 = 0 can speed up calculation (AF on x-axis)
    # For Brianchon's theorem, a1 = 0 makes lines A and F intersect at infinity on y-axis, so use a2 = 0 instead (lines A and F intersect at origin)
    A, B, C, D, E = (a0, a1, a2), (b0, b1, b2), (c0, c1, c2), (d0, d1, d2), (e0, e1, e2)
    # Get conic equation in this way: https://en.wikipedia.org/wiki/Five_points_determine_a_conic#Construction
    # This is much faster than 6x6 matrix:
    # mat = [[a0**2, b0**2, c0**2, d0**2, e0**2, x**2], ...]
    # conic_poly = poly(Matrix(mat).det(), (x, y, z))
    # a = conic_poly.coeff_monomial(x**2)
    # ...
    # SymPy's det() may be very slow. More efficient ways in this case could be:
    # 1. use adjugate() or Laplace expansion to reduce to 4x4 matrix
    # 2. https://stackoverflow.com/a/37056325/4260959
    r1 = [a0**2, b0**2, c0**2, d0**2, e0**2]
    r2 = [a0*a1, b0*b1, c0*c1, d0*d1, e0*e1]
    r3 = [a1**2, b1**2, c1**2, d1**2, e1**2]
    r4 = [a0*a2, b0*b2, c0*c2, d0*d2, e0*e2]
    r5 = [a1*a2, b1*b2, c1*c2, d1*d2, e1*e2]
    r6 = [a2**2, b2**2, c2**2, d2**2, e2**2]
    a, b = Matrix([r2, r3, r4, r5, r6]).det(), -Matrix([r1, r3, r4, r5, r6]).det()
    c, d = Matrix([r1, r2, r4, r5, r6]).det(), -Matrix([r1, r2, r3, r5, r6]).det()
    e, f = Matrix([r1, r2, r3, r4, r6]).det(), -Matrix([r1, r2, r3, r4, r5]).det()
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