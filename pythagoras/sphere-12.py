from sympy import Eq, Matrix, cancel, expand, fraction, gcd_list, lcm_list, poly, solve, symbols

def sphere(P1, P2, P3):
    # return F(x, y, z) such that F(x, y, z) = 0 is the sphere's equation
    g, h, j, k, x, y, z = symbols('g, h, j, k, x, y, z')
    sphere_eq = Eq(x**2 + y**2 + z**2 + g*x + h*y + k, 0)
    sphere_eqs = []
    sphere_eqs.append(sphere_eq.subs(x, P1[0]).subs(y, P1[1]).subs(z, P1[2]))
    sphere_eqs.append(sphere_eq.subs(x, P2[0]).subs(y, P2[1]).subs(z, P2[2]))
    sphere_eqs.append(sphere_eq.subs(x, P3[0]).subs(y, P3[1]).subs(z, P3[2]))
    s = solve(sphere_eqs, (g, h, k))
    return fraction(cancel(x**2 + y**2 + z**2 + s[g]*x + s[h]*y + s[k]))[0]

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

def intersect(P, S, sphere_l):
    # return the intersection of PS and sphere_l(x, y, z) = 0:
    x, y, z, t = symbols('x, y, z, t')
    xt, yt, zt = P[0] + (S[0] - P[0])*t, P[1] + (S[1] - P[1])*t, P[2] + (S[2] - P[2])*t
    t0 = solve(Eq(sphere_l.subs(x, xt).subs(y, yt).subs(z, zt)/t, 0), t)[0]
    return xt.subs(t, t0), yt.subs(t, t0), zt.subs(t, t0)

def multiplied(x, y, z, w):
    x1, y1, z1, w1 = fraction(cancel(x)), fraction(cancel(y)), fraction(cancel(z)), fraction(cancel(w))
    lcd = lcm_list([x1[1], y1[1], z1[1], w1[1]])
    return x1[0]*cancel(lcd/x1[1]), y1[0]*cancel(lcd/y1[1]), z1[0]*cancel(lcd/z1[1]), w1[0]*cancel(lcd/w1[1])

def to_homogeneous(P):
    return multiplied(P[0], P[1], P[2], 1)

def reduced(x, y, z, w):
    gcd = gcd_list([x, y, z, w])
    return cancel(x/gcd), cancel(y/gcd), cancel(z/gcd), cancel(w/gcd)

def cross(P1, P2, P3):
    x10, x11, x12, x13 = P1
    x20, x21, x22, x23 = P2
    x30, x31, x32, x33 = P3
    # generated by cross-3d.py
    x = -x11*x22*x33 + x11*x23*x32 + x12*x21*x33 - x12*x23*x31 - x13*x21*x32 + x13*x22*x31
    y = x10*x22*x33 - x10*x23*x32 - x12*x20*x33 + x12*x23*x30 + x13*x20*x32 - x13*x22*x30
    z = -x10*x21*x33 + x10*x23*x31 + x11*x20*x33 - x11*x23*x30 - x13*x20*x31 + x13*x21*x30
    w = x10*x21*x32 - x10*x22*x31 - x11*x20*x32 + x11*x22*x30 + x12*x20*x31 - x12*x21*x30
    return reduced(x, y, z, w)

def on_sphere(sphere_h, P):
    x, y, z, w = symbols('x, y, z, w')
    return expand(sphere_h.subs(x, P[0]).subs(y, P[1]).subs(z, P[2]).subs(w, P[3])) == 0

def tangent_plane(sphere_poly, P):
    # Tangent plane to point (x0, y0, z0, w0) and quadratic curve plane
    # /x\T/a b d g\/x\        /a b d g\/x0\
    # |y| |b c e h||y| = 0 is |b c e h||y0|
    # |z| |d e f j||z|        |d e f j||z0|
    # \w/ \g h j k/\w/        \g h j k/\w0/
    # For a sphere with equator on xy:
    # a = c = f
    # b = d = e = j = 0
    x, y, z, w = symbols('x, y, z, w')
    coeff_a = sphere_poly.nth(2, 0, 0, 0)
    coeff_g = sphere_poly.nth(1, 0, 0, 1)/2
    coeff_h = sphere_poly.nth(0, 1, 0, 1)/2
    coeff_k = sphere_poly.nth(0, 0, 0, 2)
    x0 = coeff_a*P[0] + coeff_g*P[3]
    y0 = coeff_a*P[1] + coeff_h*P[3]
    z0 = coeff_a*P[2]
    w0 = coeff_g*P[0] + coeff_h*P[1] + coeff_k*P[3]
    return reduced(x0, y0, z0, w0)

def dist2(P1, P2):
    return cancel((P1[0]/P1[3] - P2[0]/P2[3])**2 + (P1[1]/P1[3] - P2[1]/P2[3])**2 + (P1[2]/P1[3] - P2[2]/P2[3])**2)

def main():
    # https://imomath.com/index.cgi?page=inversion (Problem 12)
    a, b, c, d, e, f, x, y, z, w = symbols('a, b, c, d, e, f, x, y, z, w')
    A, B, C, S = (a, 0, 0), (0, b, 0), (c, 0, 0), (d, e, f)
    sphere_l = sphere(A, B, C)
    print('Sphere Equation:', sphere_l, '= 0')
    A1, B1, C1 = intersect(A, S, sphere_l), intersect(B, S, sphere_l), intersect(C, S, sphere_l)
    sphere_poly = poly(sphere_l, (x, y, z)).homogenize(w)
    sphere_h = sphere_poly.expr
    print('Sphere Equation in Homogeneous:', sphere_h, '= 0')
    S, A, B, C = to_homogeneous(S), to_homogeneous(A), to_homogeneous(B), to_homogeneous(C)
    A1, B1, C1 = to_homogeneous(A1), to_homogeneous(B1), to_homogeneous(C1)
    print('A1:', A1)
    print('B1:', B1)
    print('C1:', C1)
    print('Is A on Sphere?', on_sphere(sphere_h, A))
    print('Is B on Sphere?', on_sphere(sphere_h, B))
    print('Is C on Sphere?', on_sphere(sphere_h, C))
    print('Is A1 on Sphere?', on_sphere(sphere_h, A1))
    print('Is B1 on Sphere?', on_sphere(sphere_h, B1))
    print('Is C1 on Sphere?', on_sphere(sphere_h, C1))
    plane_A1 = tangent_plane(sphere_poly, A1)
    plane_B1 = tangent_plane(sphere_poly, B1)
    plane_C1 = tangent_plane(sphere_poly, C1)
    print('Tangent plane to A1:', plane_A1)
    print('Tangent plane to B1:', plane_B1)
    print('Tangent plane to C1:', plane_C1)
    O = cross(plane_A1, plane_B1, plane_C1)
    print('O:', O)
    OS2 = dist2(O, S)
    print('OS**2 =', OS2)
    print('OS**2 - OA1**2 =', OS2 - dist2(O, A1))
    print('OS**2 - OB1**2 =', OS2 - dist2(O, B1))
    print('OS**2 - OC1**2 =', OS2 - dist2(O, C1))

if __name__ == '__main__':
    main()