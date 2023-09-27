from sympy import *

# https://artofproblemsolving.com/community/c6h156002p876416

def main():
    x, y, z, t = symbols('x, y, z, t', positive = True)
    # a**2 - b**2 >= 0 && a + b >= 0 -> a - b >= 0
    f = (sqrt(9 - 32*x*y) + sqrt(9 - 32*x*z))**2 - (7 - sqrt(9 - 32*y*z))**2
    # to prove: (sqrt(9 - 32*x*y) + sqrt(9 - 32*x*z)) + (7 - sqrt(9 - 32*y*z)) >= 0, which is obvious
    print('f =', factor(f))
    # should prove negative:
    g = (16*x*y + 16*x*z - 16*y*z + 20)**2 - (sqrt(-32*x*y + 9)*sqrt(-32*x*z + 9) + 7*sqrt(-32*y*z + 9))**2
    # to prove: (16*x*y + 16*x*z - 16*y*z + 20) + (sqrt(-32*x*y + 9)*sqrt(-32*x*z + 9) + 7*sqrt(-32*y*z + 9)) >= 0, which is obvious
    print('g =', factor(g))
    # should prove negative:
    h = (128*x**2*y**2 - 256*x**2*y*z + 128*x**2*z**2 - 256*x*y**2*z - 256*x*y*z**2 + 464*x*y + 464*x*z + 128*y**2*z**2 + 464*y*z - 61)**2 - (7*sqrt(-32*x*y + 9)*sqrt(-32*x*z + 9)*sqrt(-32*y*z + 9))**2
    print('h =', factor(h))
    print('Is h cyclic?', h.subs(z, t).subs(y, z).subs(x, y).subs(t, x) == h)
    print('Is h symmetric?', h.subs(y, t).subs(x, y).subs(t, x) == h)
    u, v = symbols('u, v', positive = True)
    X, Y, Z = 1, 1 + u, 1 + u + v
    XYZ = X + Y + Z
    print('h =', factor(h.subs(x, X/XYZ).subs(y, Y/XYZ).subs(z, Z/XYZ)))

    # to prove: (128*x**2*y**2 - 256*x**2*y*z + 128*x**2*z**2 - 256*x*y**2*z - 256*x*y*z**2 + 464*x*y + 464*x*z + 128*y**2*z**2 + 464*y*z - 61) + (7*sqrt(-32*x*y + 9)*sqrt(-32*x*z + 9)*sqrt(-32*y*z + 9)) >= 0
    # holds at x = 0 and y = z = 1/2
    j = (-32*x*y + 9)*(-32*x*z + 9)*(-32*y*z + 9) - 81
    print('j =', factor(j.subs(x, X/XYZ).subs(y, Y/XYZ).subs(z, Z/XYZ)))
    k = (128*x**2*y**2 - 256*x**2*y*z + 128*x**2*z**2 - 256*x*y**2*z - 256*x*y*z**2 + 464*x*y + 464*x*z + 128*y**2*z**2 + 464*y*z - 61) + 7*sqrt(81)
    print('k =', factor(k.subs(x, X/XYZ).subs(y, Y/XYZ).subs(z, Z/XYZ)))

if __name__ == '__main__':
    main()