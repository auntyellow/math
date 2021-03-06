from sympy import Matrix, poly, symbols

def main():
    x10, x11, x12, x13 = symbols('x10, x11, x12, x13')
    x20, x21, x22, x23 = symbols('x20, x21, x22, x23')
    x30, x31, x32, x33 = symbols('x30, x31, x32, x33')
    x, y, z, w = symbols('x, y, z, w')
    mat = []
    mat.append([x10, x11, x12, x13])
    mat.append([x20, x21, x22, x23])
    mat.append([x30, x31, x32, x33])
    mat.append([x, y, z, w])
    det_poly = poly(Matrix(mat).det(), (x, y, z, w))
    print('x =', det_poly.nth(1, 0, 0, 0))
    print('y =', det_poly.nth(0, 1, 0, 0))
    print('z =', det_poly.nth(0, 0, 1, 0))
    print('w =', det_poly.nth(0, 0, 0, 1))

if __name__ == '__main__':
    main()