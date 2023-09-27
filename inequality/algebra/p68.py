from sympy import *

# ISBN 9787542848482, p68, §2.4, ex8
# sum_cyc(sqrt(x**2 + y*z)) <= 3*(x + y + z)/2

def main():
    x, y, z, t = symbols('x, y, z, t', positive = True)
    # a**2 - b**2 <= 0 && a + b >= 0 => a - b <= 0
    e = (sqrt(x**2 + y*z) + sqrt(y**2 + z*x)) - (3*(x + y + z)/2 - sqrt(z**2 + x*y))
    f = (sqrt(x**2 + y*z) + sqrt(y**2 + z*x))**2 - (3*(x + y + z)/2 - sqrt(z**2 + x*y))**2
    # to prove: f1 = (sqrt(x**2 + y*z) + sqrt(y**2 + z*x)) + (3*(x + y + z)/2 - sqrt(z**2 + x*y)) >= 0
    f1 = (3*(x + y + z)/2)**2 - (sqrt(z**2 + x*y))**2
    print('f1 =', factor(f1))
    print('f =', factor(f))
    # should prove positive:
    g = (5*x**2 + 22*x*y + 14*x*z + 5*y**2 + 14*y*z + 13*z**2)**2 - (12*x*sqrt(x*y + z**2) + 12*y*sqrt(x*y + z**2) + 12*z*sqrt(x*y + z**2) + 8*sqrt(x**2 + y*z)*sqrt(x*z + y**2))**2
    # to prove: (5*x**2 + 22*x*y + 14*x*z + 5*y**2 + 14*y*z + 13*z**2) + (12*x*sqrt(x*y + z**2) + 12*y*sqrt(x*y + z**2) + 12*z*sqrt(x*y + z**2) + 8*sqrt(x**2 + y*z)*sqrt(x*z + y**2)) >= 0, which is obvious
    print('g =', factor(g))
    # should prove positive:
    h = (25*x**4 + 76*x**3*y + 76*x**3*z + 182*x**2*y**2 + 468*x**2*y*z + 182*x**2*z**2 + 76*x*y**3 + 468*x*y**2*z + 468*x*y*z**2 + 76*x*z**3 + 25*y**4 + 76*y**3*z + 182*y**2*z**2 + 76*y*z**3 + 25*z**4)**2 - (192*x*sqrt(x**2 + y*z)*sqrt(x*y + z**2)*sqrt(x*z + y**2) + 192*y*sqrt(x**2 + y*z)*sqrt(x*y + z**2)*sqrt(x*z + y**2) + 192*z*sqrt(x**2 + y*z)*sqrt(x*y + z**2)*sqrt(x*z + y**2))**2
    # to prove: (25*x**4 + 76*x**3*y + 76*x**3*z + 182*x**2*y**2 + 468*x**2*y*z + 182*x**2*z**2 + 76*x*y**3 + 468*x*y**2*z + 468*x*y*z**2 + 76*x*z**3 + 25*y**4 + 76*y**3*z + 182*y**2*z**2 + 76*y*z**3 + 25*z**4) + (192*x*sqrt(x**2 + y*z)*sqrt(x*y + z**2)*sqrt(x*z + y**2) + 192*y*sqrt(x**2 + y*z)*sqrt(x*y + z**2)*sqrt(x*z + y**2) + 192*z*sqrt(x**2 + y*z)*sqrt(x*y + z**2)*sqrt(x*z + y**2)) >= 0, which is obvious
    print('h =', factor(h))
    print('Is h cyclic?', h.subs(z, t).subs(y, z).subs(x, y).subs(t, x) == h)
    print('Is h symmetric?', h.subs(y, t).subs(x, y).subs(t, x) == h)
    u, v = symbols('u, v', positive = True)
    print('h =', factor(h.subs(y, x + u).subs(z, x + u + v)))
    # holds when x = 0 and v = 0 (y = z)

if __name__ == '__main__':
    main()