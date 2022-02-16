from sympy import poly, symbols
from homogeneous import *

def circle_row(x, y, z):
    return [x**2 + y**2, x*z, y*z, z**2]

def main():
    x, y, z, x1, y1, z1, x2, y2, z2, x3, y3, z3 = symbols('x, y, z, x1, y1, z1, x2, y2, z2, x3, y3, z3')
    circle_poly = poly(Matrix([circle_row(x, y, z), circle_row(x1, y1, z1), circle_row(x2, y2, z2), circle_row(x3, y3, z3)]).det(), (x, y, z))
    assert circle_poly.nth(2, 0, 0) == circle_poly.nth(0, 2, 0)
    print('Circle coefficients:')
    a, d, e, f = circle_poly.nth(2, 0, 0), circle_poly.nth(1, 0, 1), circle_poly.nth(0, 1, 1), circle_poly.nth(0, 0, 2)
    print(f'a = expand({a})')
    print(f'd = expand({d})')
    print(f'e = expand({e})')
    print(f'f = expand({f})')
    # nothing to reduce

if __name__ == '__main__':
    main()