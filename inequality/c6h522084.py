from sympy import *

# https://artofproblemsolving.com/community/c6h522084

def cyc(p):
    x, y, z, t = symbols('x, y, z, t')
    return p.subs(x, t).subs(y, x).subs(z, y).subs(t, z)

def sum_cyc(p):
    p1 = cyc(p)
    return p + p1 + cyc(p1)

def cyc4(p):
    a, b, c, d, t = symbols('a, b, c, d, t')
    return p.subs(a, t).subs(b, a).subs(c, b).subs(d, c).subs(t, d)

def sum_cyc4(p):
    p1 = cyc4(p)
    p2 = cyc4(p1)
    return p + p1 + p2 + cyc4(p2)

def main():
    x, y, z = symbols('x, y, z')
    ineq = sum_cyc(x**3 - x**2*y - x**2*z + x*y*z)
    p, q = symbols('p, q', positive = True)
    # y and z can swap
    # x <= y <= z
    print('ineq =', expand(ineq.subs(y, x + p).subs(z, x + p + q)))
    print()

    # for all triangles
    ineq = sum_cyc(x**3*y**2 - (x**2)*x*y*z)
    r = symbols('r', positive = True)
    # x <= y <= z
    print('ineq(xyz) =', expand(ineq.subs(x, p + q).subs(y, p + q + r).subs(z, p + 2*q + r)))
    # x <= z <= y
    print('ineq(xzy) =', expand(ineq.subs(x, p + q).subs(z, p + q + r).subs(y, p + 2*q + r)))
    print()

    a, b, c, d = symbols('a, b, c, d')
    ineq = sum_cyc4(a**4 + a*b*c*d - 2*a**2*b*c)
    # b and c can swap
    # a <= b <= c <= d
    print('ineq(abcd) =', expand(ineq.subs(b, a + p).subs(c, a + p + q).subs(d, a + p + q + r)))
    # a <= b <= d <= c
    print('ineq(abdc) =', expand(ineq.subs(b, a + p).subs(d, a + p + q).subs(c, a + p + q + r)))
    # a <= d <= b <= c
    print('ineq(adbc) =', expand(ineq.subs(d, a + p).subs(b, a + p + q).subs(c, a + p + q + r)))

if __name__ == '__main__':
    main()