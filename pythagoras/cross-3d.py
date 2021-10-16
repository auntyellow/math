from sympy import Matrix, poly, symbols

x10, x11, x12, x13 = symbols('x10, x11, x12, x13')
x20, x21, x22, x23 = symbols('x20, x21, x22, x23')
x30, x31, x32, x33 = symbols('x30, x31, x32, x33')
x, y, z, w = symbols('x, y, z, w')
mat = []
mat.append([x10, x11, x12, x13])
mat.append([x20, x21, x22, x23])
mat.append([x30, x31, x32, x33])
mat.append([x, y, z, w])
det = Matrix(mat).det()
print('x =', poly(det, x).nth(1))
print('y =', poly(det, y).nth(1))
print('z =', poly(det, z).nth(1))
print('w =', poly(det, w).nth(1))