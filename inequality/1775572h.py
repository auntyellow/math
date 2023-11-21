from sympy import *

# https://math.stackexchange.com/a/2120874
# https://math.stackexchange.com/q/1775572

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    x, y, z = symbols('x, y, z', negative = False)
    f = sum_cyc(x**4/(8*x**3 + 5*y**3), (x, y, z)) - (x + y + z)/13
    print('f(xyz) =', factor(f.subs(y, x + y).subs(z, x + y + z)))
    print('f(xzy) =', factor(f.subs(z, x + z).subs(y, x + y + z)))
    # result in f(xyz)
    g = 156*x**8*y**2 + 156*x**8*y*z + 156*x**8*z**2 + 858*x**7*y**3 + 192*x**7*y**2*z + 114*x**7*y*z**2 + 390*x**7*z**3 + 2392*x**6*y**4 - 326*x**6*y**3*z - 2400*x**6*y**2*z**2 + 318*x**6*y*z**3 + 754*x**6*z**4 + 4329*x**5*y**5 + 570*x**5*y**4*z - 6582*x**5*y**3*z**2 - 2778*x**5*y**2*z**3 + 1527*x**5*y*z**4 + 741*x**5*z**5 + 5226*x**4*y**6 + 4029*x**4*y**5*z - 5898*x**4*y**4*z**2 - 5556*x**4*y**3*z**3 + 762*x**4*y**2*z**4 + 1617*x**4*y*z**5 + 351*x**4*z**6 + 4095*x**3*y**7 + 6093*x**3*y**6*z - 441*x**3*y**5*z**2 - 3020*x**3*y**4*z**3 + 779*x**3*y**3*z**4 + 1866*x**3*y**2*z**5 + 636*x**3*y*z**6 + 65*x**3*z**7 + 1989*x**2*y**8 + 4284*x**2*y**7*z + 2436*x**2*y**6*z**2 + 591*x**2*y**5*z**3 + 1725*x**2*y**4*z**4 + 1890*x**2*y**3*z**5 + 690*x**2*y**2*z**6 + 75*x**2*y*z**7 + 546*x*y**9 + 1503*x*y**8*z + 1488*x*y**7*z**2 + 1061*x*y**6*z**3 + 1290*x*y**5*z**4 + 1185*x*y**4*z**5 + 500*x*y**3*z**6 + 75*x*y**2*z**7 + 65*y**10 + 215*y**9*z + 285*y**8*z**2 + 275*y**7*z**3 + 315*y**6*z**4 + 285*y**5*z**5 + 135*y**4*z**6 + 25*y**3*z**7
    print('g(xyz) =', expand(g.subs(y, x + y).subs(z, x + y + z)))
    print('g(xzy) =', expand(g.subs(z, x + z).subs(y, x + y + z)))
    print('g(yxz) =', expand(g.subs(x, x + y).subs(z, x + y + z)))
    print('g(yzx) =', expand(g.subs(z, y + z).subs(x, x + y + z)))
    print('g(zxy) =', expand(g.subs(x, x + z).subs(y, x + y + z)))
    print('g(zyx) =', expand(g.subs(y, y + z).subs(x, x + y + z)))

if __name__ == '__main__':
    main()