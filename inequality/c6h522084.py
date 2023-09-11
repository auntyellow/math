from sympy import *

# https://artofproblemsolving.com/community/c6h522084

def cyc(f):
    x, y, z, t = symbols('x, y, z, t')
    return f.subs(x, t).subs(y, x).subs(z, y).subs(t, z)

def sum_cyc(f):
    f1 = cyc(f)
    return f + f1 + cyc(f1)

def cyc4(f):
    a, b, c, d, t = symbols('a, b, c, d, t')
    return f.subs(a, t).subs(b, a).subs(c, b).subs(d, c).subs(t, d)

def sum_cyc4(f):
    f1 = cyc4(f)
    f2 = cyc4(f1)
    return f + f1 + f2 + cyc4(f2)

def main():
    x, y, z = symbols('x, y, z')
    f = sum_cyc(x**3 - x**2*y - x**2*z + x*y*z)
    u, v = symbols('u, v', positive = True)
    # y and z can swap
    # x <= y <= z
    print('f =', expand(f.subs(y, x + u).subs(z, x + u + v)))
    print()

    # for all triangles
    f = sum_cyc(x**3*y**2 - (x**2)*x*y*z)
    w = symbols('w', positive = True)
    # x <= y <= z
    print('f(xyz) =', expand(f.subs(x, u + v).subs(y, u + v + w).subs(z, u + 2*v + w)))
    # x <= z <= y
    print('f(xzy) =', expand(f.subs(x, u + v).subs(z, u + v + w).subs(y, u + 2*v + w)))
    print()

    a, b, c, d = symbols('a, b, c, d')
    f = sum_cyc4(a**4 + a*b*c*d - 2*a**2*b*c)
    # b and c can swap
    # a <= b <= c <= d
    print('f(abcd) =', expand(f.subs(b, a + u).subs(c, a + u + v).subs(d, a + u + v + w)))
    # a <= b <= d <= c
    print('f(abdc) =', expand(f.subs(b, a + u).subs(d, a + u + v).subs(c, a + u + v + w)))
    # a <= d <= b <= c
    print('f(adbc) =', expand(f.subs(d, a + u).subs(b, a + u + v).subs(c, a + u + v + w)))
    print()

    # https://math.stackexchange.com/q/2098409
    f = sum_cyc(1/(x + y - z) - 1/x)
    # x <= y <= z
    print('f(xyz) =', factor(f.subs(x, u + v).subs(y, u + v + w).subs(z, u + 2*v + w)))
    print()

    # https://math.stackexchange.com/q/4762885
    f = sum_cyc(x/(y + z)) + 3*x*y*z/sum_cyc(x*y*(x + y)) - 2
    # x <= y <= z
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print()

    # https://math.stackexchange.com/q/4765187
    f = ((1 + a)*(1 + b)*(1 + c))**7 - 7**7*a**4*b**4*c**4
    u, v, w = symbols('u, v, w', positive = True)
    # a, b, c <= 1
    print('f(abc1) =', factor(f.subs(a, 1/(1 + u)).subs(b, 1/(1 + v)).subs(c, 1/(1 + w))))
    # a, b <= 1 <= c
    print('f(ab1c) =', factor(f.subs(a, 1/(1 + u)).subs(b, 1/(1 + v)).subs(c, 1 + w)))
    # a <= 1 <= b, c
    print('f(a1bc) =', factor(f.subs(a, 1/(1 + u)).subs(b, 1 + v).subs(c, 1 + w)))
    # 1 <= a, b, c
    print('f(1abc) =', factor(f.subs(a, 1 + u).subs(b, 1 + v).subs(c, 1 + w)))
    print()

    # https://math.stackexchange.com/q/4744552
    a = sqrt(x/(x + y + z))
    b = sqrt(y/(x + y + z))
    c = sqrt(z/(x + y + z))
    f = a*b/c + b*c/a + c*a/b
    # x <= y <= z
    print('f(xyz) =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    # so we guess maximum or minimum is sqrt(3) when u = v = 0 (x = y = z)
    f23 = f*f - 3
    print('f^2 - 3 =', factor(f23.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    # f23 >= 0 so sqrt(3) is minimum

if __name__ == '__main__':
    main()