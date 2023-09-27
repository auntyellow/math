from sympy import *

def cyc(f):
    x, y, z, t = symbols('x, y, z, t', positive = True)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f):
    f1 = cyc(f)
    return f + f1 + cyc(f1)

def cyc4(f):
    a, b, c, d, t = symbols('a, b, c, d, t', positive = True)
    return f.subs(d, t).subs(c, d).subs(b, c).subs(a, b).subs(t, a)

def sum_cyc4(f):
    f1 = cyc4(f)
    f2 = cyc4(f1)
    return f + f1 + f2 + cyc4(f2)

def cyc3(f):
    b, c, d, t = symbols('b, c, d, t', positive = True)
    return f.subs(d, t).subs(c, d).subs(b, c).subs(t, b)

def sum_comb4(f):
    f1 = cyc4(f)
    f2 = cyc4(f1)
    f3 = cyc3(f2)
    return f + f1 + f2 + cyc4(f2) + f3 + cyc4(f3)

def main():
    a, b, c, d = symbols('a, b, c, d', positive = True)
    u, v, w = symbols('u, v, w', positive = True)
    x, y, z = symbols('x, y, z', positive = True)

    # https://artofproblemsolving.com/community/c6h522084
    f = sum_cyc(x**3 - x**2*y - x**2*z + x*y*z)
    # y and z can swap
    # x <= y <= z
    print('f =', expand(f.subs(y, x + u).subs(z, x + u + v)))
    print()

    # for all triangles
    f = sum_cyc(x**3*y**2 - (x**2)*x*y*z)
    # x <= y <= z
    print('f(xyz) =', expand(f.subs(x, u + v).subs(y, u + v + w).subs(z, u + 2*v + w)))
    # x <= z <= y
    print('f(xzy) =', expand(f.subs(x, u + v).subs(z, u + v + w).subs(y, u + 2*v + w)))
    print()

    print(cyc4(a*b), cyc3(a*b), sum_cyc4(a*b), sum_comb4(a*b))
    f = sum_cyc4(a**4 + a*b*c*d - 2*a**2*b*c)
    # b and c can swap
    # a <= b <= c <= d
    print('f(abcd) =', expand(f.subs(b, a + u).subs(c, a + u + v).subs(d, a + u + v + w)))
    # a <= b <= d <= c
    print('f(abdc) =', expand(f.subs(b, a + u).subs(d, a + u + v).subs(c, a + u + v + w)))
    # a <= d <= b <= c
    print('f(adbc) =', expand(f.subs(d, a + u).subs(b, a + u + v).subs(c, a + u + v + w)))
    print()

    '''
    # https://math.stackexchange.com/q/2098409
    f = sum_cyc(1/(x + y - z) - 1/x)
    # x <= y <= z
    print('f(xyz) =', factor(f.subs(x, u + v).subs(y, u + v + w).subs(z, u + 2*v + w)))
    print()

    # https://math.stackexchange.com/q/4692575
    f = 1/a + 1/b + 1/c + 6/(a + b + c) - 5
    # a <= 1 <= b, c
    print('f(a1bc) =', factor(f.subs(a, 1/b/c).subs(b, 1 + u).subs(c, 1 + v)))
    # a, b <= 1 <= c
    print('f(ab1c) =', factor(f.subs(c, 1/a/b).subs(a, 1/(1 + u)).subs(b, 1/(1 + v))))
    print()

    # https://math.stackexchange.com/q/4765317
    f = 1/a + 1/b + 1/c - 6/(a + b + c) - 1
    # a <= 1 <= b, c
    print('f(a1bc) =', factor(f.subs(a, 1/(b*c + w)).subs(b, 1 + u).subs(c, 1 + v)))
    # a, b <= 1 <= c <= 1/ab
    print('f(ab1c) =', factor(f.subs(c, 1 + (1/a/b - 1)/(1 + w)).subs(a, 1/(1 + u)).subs(b, 1/(1 + v))))
    # a, b, c <= 1
    print('f(abc1) =', factor(f.subs(a, 1/(1 + u + v + w)).subs(b, 1/(1 + u + v)).subs(c, 1/(1 + u))))
    print()
 
    # https://math.stackexchange.com/q/4762885
    f = sum_cyc(x/(y + z)) + 3*x*y*z/sum_cyc(x*y*(x + y)) - 2
    # x <= y <= z
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print()

    # https://math.stackexchange.com/q/4765187
    f = ((1 + a)*(1 + b)*(1 + c))**7 - 7**7*a**4*b**4*c**4
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
    print()

    # https://math.stackexchange.com/q/4767134
    # https://i.stack.imgur.com/zVGzB.png
    k, l, m, n = symbols('k, l, m, n', positive = True)
    # k, l, m, n = a^2, b^2, c^2, d^2
    f = sum_cyc4((a**2*b**2 + b**2*c**2 + c**2*a**2)/(a**6 + b**6 + c**6)) - sum_comb4((a**4 + b**4)/(a**3*b**3))
    # too slow
    # print('f =', factor(f.subs(b, a*(1 + u)).subs(c, a*(1 + u + v)).subs(d, a*(1 + u + v + w))))

    # ISBN 9787030655189, p223, ex 8.5.1
    f = y**3 - (x + 1)*y**2 - (x**2 - 3*x + 1)*y + x**3 - x**2 - x + 1
    # f is symmetric
    # 0 <= x <= y <= 1
    print('f(xy1) =', factor(f.subs(x, 1/(1 + u + v)).subs(y, 1/(1 + v))))
    # 0 <= x <= 1 <= y
    print('f(x1y) =', factor(f.subs(x, 1/(1 + u)).subs(y, 1 + v)))
    # 1 <= x <= y
    print('f(1xy) =', factor(f.subs(x, 1 + u).subs(y, 1 + u + v)))
    print()

    # https://artofproblemsolving.com/community/c6h154
    A, B, C, D = x, x + u, x + u + v, x + u + v + w
    ABCD = A + B + C + D
    a, b, c, d = A/ABCD, B/ABCD, C/ABCD, D/ABCD
    print('f =', factor((1 + 176*a*b*c*d)/27 - b*c*d + c*d*a + d*a*b + a*b*c))
    print()
    '''

    # https://artofproblemsolving.com/community/c6h218191
    f = sum_cyc(x**5/(x**3 + y**3) + x**3/(x + y) - x**4/(x**2 + y**2) - x**2/2)
    # doesn't hold
    # f = sum_cyc(-x**5/(x**3 + y**3) + x**3/(x + y) + x**4/(x**2 + y**2) - x**2/2)
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    print('f(xzy) =', factor(f.subs(z, x*(1 + u)).subs(y, x*(1 + u + v))))
    print()

if __name__ == '__main__':
    main()