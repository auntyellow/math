from sympy import Eq, Matrix, cancel, expand, fraction, gcd_list, lcm_list, poly, solve, symbols

def sphere(P1, P2, P3, P4):
    # return F(x, y, z) such that F(x, y, z) = 0 is the sphere's equation
    g, h, j, k, x, y, z = symbols('g, h, j, k, x, y, z')
    sphere_eq = Eq(x**2 + y**2 + z**2 + g*x + h*y + j*z + k, 0)
    sphere_eqs = []
    sphere_eqs.append(sphere_eq.subs(x, P1[0]).subs(y, P1[1]).subs(z, P1[2]))
    sphere_eqs.append(sphere_eq.subs(x, P2[0]).subs(y, P2[1]).subs(z, P2[2]))
    sphere_eqs.append(sphere_eq.subs(x, P3[0]).subs(y, P3[1]).subs(z, P3[2]))
    sphere_eqs.append(sphere_eq.subs(x, P4[0]).subs(y, P4[1]).subs(z, P4[2]))
    s = solve(sphere_eqs, (g, h, j, k))
    return fraction(cancel(x**2 + y**2 + z**2 + s[g]*x + s[h]*y + s[j]*z + s[k]))[0]

def coplanar(P1, P2, P3, P4):
    mat = []
    mat.append([P1[0], P1[1], P1[2], 1])
    mat.append([P2[0], P2[1], P2[2], 1])
    mat.append([P3[0], P3[1], P3[2], 1])
    mat.append([P4[0], P4[1], P4[2], 1])
    return Eq(fraction(cancel(Matrix(mat).det()))[0], 0)

def plane(P1, P2, P3):
    x, y, z = symbols('x, y, z')
    return coplanar((x, y, z), P1, P2, P3)

def intersect(P1, P2, P3, slope, sphere_l, ai0, ai1, ai2):
    axes = symbols('x, y, z')
    axis0, axis1, axis2 = axes[ai0], axes[ai1], axes[ai2]
    # return the intersect point P of:
    # `axis2 = plane_p(axis0, axis1)` passing through P1, P2 and P3 
    # `axis1 = plane_q(axis0)` with `slope = axis1/axis0` passing through P1
    # `sphere_l(x, y, z) = 0`
    plane_p = solve(plane(P1, P2, P3), axis2)[0]
    plane_q = slope*(axis0 - P1[ai0]) + P1[ai1]
    sphere_coeffs = poly(sphere_l.subs(axis2, plane_p).subs(axis1, plane_q), axis0).all_coeffs()
    P = {}
    P[axis0] = -sphere_coeffs[1]/sphere_coeffs[0] - P1[ai0]
    P[axis1] = plane_q.subs(axis0, P[axis0])
    P[axis2] = plane_p.subs(axis0, P[axis0]).subs(axis1, P[axis1])
    return P[axes[0]], P[axes[1]], P[axes[2]]

def multiplied(x, y, z, w):
    x1, y1, z1, w1 = fraction(cancel(x)), fraction(cancel(y)), fraction(cancel(z)), fraction(cancel(w))
    lcd = lcm_list([x1[1], y1[1], z1[1], w1[1]])
    return x1[0]*cancel(lcd/x1[1]), y1[0]*cancel(lcd/y1[1]), z1[0]*cancel(lcd/z1[1]), w1[0]*cancel(lcd/w1[1])

def to_homogeneous(P):
    return multiplied(P[0], P[1], P[2], 1)

def reduced(x, y, z, w):
    gcd = gcd_list([x, y, z, w])
    if gcd == 0:
        return 0, 0, 0, 1
    return cancel(x/gcd), cancel(y/gcd), cancel(z/gcd), cancel(w/gcd)

def cross(P1, P2, P3):
    x10, x11, x12, x13 = P1[0], P1[1], P1[2], P1[3]
    x20, x21, x22, x23 = P2[0], P2[1], P2[2], P2[3]
    x30, x31, x32, x33 = P3[0], P3[1], P3[2], P3[3]
    # generated by cross-3d.py
    x = -x11*x22*x33 + x11*x23*x32 + x12*x21*x33 - x12*x23*x31 - x13*x21*x32 + x13*x22*x31
    y = x10*x22*x33 - x10*x23*x32 - x12*x20*x33 + x12*x23*x30 + x13*x20*x32 - x13*x22*x30
    z = -x10*x21*x33 + x10*x23*x31 + x11*x20*x33 - x11*x23*x30 - x13*x20*x31 + x13*x21*x30
    w = x10*x21*x32 - x10*x22*x31 - x11*x20*x32 + x11*x22*x30 + x12*x20*x31 - x12*x21*x30
    return reduced(x, y, z, w)

def on_sphere(sphere_h, P):
    x, y, z, w = symbols('x, y, z, w')
    return expand(sphere_h.subs(x, P[0]).subs(y, P[1]).subs(z, P[2]).subs(w, P[3])) == 0

def main():
    # https://www.imomath.com/index.php?options=323 (Problem 11)
    a, b, c, d, e, f, g, h, j, x, y, z, w = symbols('a, b, c, d, e, f, g, h, j, x, y, z, w')
    # quick test a special case
    # b, d, e = 0, 0, 0
    O, A, B, C = (0, 0, 0), (a, 0, 0), (b, c, 0), (d, e, f)
    sphere_l = sphere(O, A, B, C)
    print('Sphere Equation:', sphere_l, '= 0')
    # If we choose plane $y=kx$ through point O, we'll get G with too many terms:
    # G[0] has 12319 terms
    # G[1] has 9959 terms
    # G[2] has 6337 terms
    # G[3] has 8760 terms
    # D = intersect(O, B, C, g, sphere_l, 1, 2, 0)
    # E = intersect(O, C, A, h, sphere_l, 2, 0, 1)
    # F = intersect(O, A, B, j, sphere_l, 0, 1, 2)
    D = intersect(C, B, O, g, sphere_l, 1, 2, 0)
    E = intersect(A, C, O, h, sphere_l, 2, 0, 1)
    F = intersect(B, A, O, j, sphere_l, 0, 1, 2)
    sphere_h = poly(sphere_l, (x, y, z)).homogenize(w).expr
    print('Sphere Equation in Homogeneous:', sphere_h, '= 0')
    A, B, C = to_homogeneous(A), to_homogeneous(B), to_homogeneous(C)
    D, E, F = to_homogeneous(D), to_homogeneous(E), to_homogeneous(F)
    print('D:', D)
    print('E:', E)
    print('F:', F)
    print('Is A on Sphere?', on_sphere(sphere_h, A))
    print('Is B on Sphere?', on_sphere(sphere_h, B))
    print('Is C on Sphere?', on_sphere(sphere_h, C))
    print('Is D on Sphere?', on_sphere(sphere_h, D))
    print('Is E on Sphere?', on_sphere(sphere_h, E))
    print('Is F on Sphere?', on_sphere(sphere_h, F))
    CDE, BFD, AEF = cross(C, D, E), cross(B, F, D), cross(A, E, F)
    print('CDE:', CDE)
    print('BFD:', BFD)
    print('AEF:', AEF)
    G = cross(CDE, BFD, AEF)
    print('G:', G)
    print('G[0] has', len(G[0].args), 'terms')
    print('G[1] has', len(G[1].args), 'terms')
    print('G[2] has', len(G[2].args), 'terms')
    print('G[3] has', len(G[3].args), 'terms')
    print('Is G on Sphere?', on_sphere(sphere_h, G))

if __name__ == '__main__':
    main()