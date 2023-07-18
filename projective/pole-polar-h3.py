from sympy import Eq, Matrix, expand, factor, poly, solve, symbols

def coeff_matrix(p):
    a, b, c, d, e, f = p.nth(2, 0, 0), p.nth(1, 1, 0), p.nth(0, 2, 0), p.nth(1, 0, 1), p.nth(0, 1, 1), p.nth(0, 0, 2)
    return Matrix([[a, b/2, d/2], [b/2, c, e/2], [d/2, e/2, f]])

def main():
    # This program shows why line $p_0^T{\cdot}A{\cdot}p=0$ is tangent to the conic $p^T{\cdot}A{\cdot}p=0$,
    # and why B is A's adjugate for a point conic $p^T{\cdot}A{\cdot}p=0$ and its line conic $l^T{\cdot}B{\cdot}l=0$
    a, b, c, d, e, f, u, v, w, x, y, z, x0, y0 = symbols('a, b, c, d, e, f, u, v, w, x, y, z, x0, y0')
    conic_eq = a*x**2 + 2*b*x*y + c*y**2 + 2*d*x + 2*e*y + f
    line_eq = (a*x0 + b*y0 + d)*x + (b*x0 + c*y0 + e)*y + (d*x0 + e*y0 + f)
    print('Conic Equation:', conic_eq, '= 0')
    print('Line Equation:', line_eq, '= 0')
    y1 = solve(Eq(line_eq, 0), y)[0]
    conic_poly = poly(conic_eq.subs(y, y1), x)
    print('Discriminant =', factor(conic_poly.nth(1)**2 - 4*conic_poly.nth(2)*conic_poly.nth(0)))
    line_eq = u*x + v*y + w
    print('Line Equation:', line_eq, '= 0')
    y1 = solve(Eq(line_eq, 0), y)[0]
    conic_poly = poly(conic_eq.subs(y, y1), x)
    print('Discriminant =', factor(conic_poly.nth(1)**2 - 4*conic_poly.nth(2)*conic_poly.nth(0)))

    point_coeffs = coeff_matrix(poly(a*x**2 + 2*b*x*y + c*y**2 + 2*d*x*z + 2*e*y*z + f*z**2, (x, y, z)))
    line_coeffs = coeff_matrix(poly(a*c*w**2 - 2*a*e*v*w + a*f*v**2 - b**2*w**2 + 2*b*d*v*w + 2*b*e*u*w - 2*b*f*u*v - 2*c*d*u*w + c*f*u**2 - d**2*v**2 + 2*d*e*u*v - e**2*u**2, (u, v, w)))
    print('Coefficients of Point Conic:', point_coeffs)
    print('Coefficients of Line Conic:', line_coeffs)
    print('Their Product:', expand(point_coeffs*line_coeffs))

if __name__ == '__main__':
    main()