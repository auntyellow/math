from sympy import *

# https://artofproblemsolving.com/community/c6h156002

def main():
    x, y, z, t = symbols('x, y, z, t', positive = True)
    # a**2 - b**2 >= 0 && a + b >= 0 => a - b >= 0
    f = (sqrt(1 - 2*x*y) + sqrt(1 - 2*x*z))**2 - (sqrt(7) - sqrt(1 - 2*y*z))**2
    # to prove: sqrt(1 - 2*x*y) + sqrt(1 - 2*x*z) + sqrt(7) - sqrt(1 - 2*y*z) >= 0, which is obvious
    print('f =', factor(f))
    # should prove negative:
    g = (x*y + x*z - y*z + 3)**2 - (sqrt(-2*x*y + 1)*sqrt(-2*x*z + 1) + sqrt(7)*sqrt(-2*y*z + 1))**2
    # to prove: x*y + x*z - y*z + 3 + sqrt(-2*x*y + 1)*sqrt(-2*x*z + 1) + sqrt(7)*sqrt(-2*y*z + 1) >= 0, which is obvious
    print('g =', factor(g))
    # should prove negative:
    h = (x**2*y**2 - 2*x**2*y*z + x**2*z**2 - 2*x*y**2*z - 2*x*y*z**2 + 8*x*y + 8*x*z + y**2*z**2 + 8*y*z + 1)**2 - (2*sqrt(7)*sqrt(-2*x*y + 1)*sqrt(-2*x*z + 1)*sqrt(-2*y*z + 1))**2
    # to prove: (x**2*y**2 - 2*x**2*y*z + x**2*z**2 - 2*x*y**2*z - 2*x*y*z**2 + 8*x*y + 8*x*z + y**2*z**2 + 8*y*z + 1) + 2*sqrt(7)*sqrt(-2*x*y + 1)*sqrt(-2*x*z + 1)*sqrt(-2*y*z + 1) >= 0, which is obvious
    print('h =', factor(h))
    print('Is h cyclic?', h.subs(z, t).subs(y, z).subs(x, y).subs(t, x) == h)
    print('Is h symmetric?', h.subs(y, t).subs(x, y).subs(t, x) == h)
    s3 = Integer(1)/3
    print('h(1/3) =', h.subs(x, s3).subs(y, s3).subs(z, s3))
    u, v = symbols('u, v', positive = True)
    # x <= y <= 1/3 <= z
    print('f(xy3z) =', factor(h.subs(z, 1 - x - y).subs(y, s3/(1 + u)).subs(x, s3/(1 + u + v))))
    # x <= 1/3 <= y <= (1 - x)/2, z = 1 - x - y >= y
    print('f(x3yz) =', factor(h.subs(z, 1 - x - y).subs(y, s3 + ((1 - x)/2 - s3)/(1 + v)).subs(x, s3/(1 + u))))
    # another approach: X = 1, Y = 1 + u, Z = 1 + u + v, x = X/(X + Y + Z), ...
    X, Y, Z = 1, 1 + u, 1 + u + v
    XYZ = X + Y + Z
    print('f =', factor(h.subs(x, X/XYZ).subs(y, Y/XYZ).subs(z, Z/XYZ)))

if __name__ == '__main__':
    main()