from sympy import *

def main():
    x, y, z = symbols('x, y, z')
    # https://math.stackexchange.com/a/4397060
    plane = Eq(4*x + 3*z + 29, 0)
    sphere = (x + 1)**2 + (y - 3)**2 + z**2 - 25
    section = expand(sphere.subs(z, solve(plane, z)[0]))
    print('Their section is:', section, '= 0')
    p = poly(section, (x, y))
    a, b, c, d, e, f = p.nth(2, 0), p.nth(1, 1), p.nth(0, 2), p.nth(1, 0), p.nth(0, 1), p.nth(0, 0)
    assert b == 0
    # a*(x + d/a/2)**2 + c*(y + e/c/2)**2 = 0
    tangent_point = a*(x + d/a/2)**2 + c*(y + e/c/2)**2
    print('Are they tangent?', f == d**2/4/a + e**2/4/c)
    print('If they are tangent, the tangent point is:', tangent_point, '= 0')
    print('Are they tangent?', expand(tangent_point) == section)

if __name__ == '__main__':
    main()