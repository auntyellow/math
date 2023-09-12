from sympy import *

# https://math.stackexchange.com/a/2120874
# https://math.stackexchange.com/q/1775572

def cyc(f):
    x, y, z, t = symbols('x, y, z, t')
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f):
    f1 = cyc(f)
    return f + f1 + cyc(f1)

def main():
    x, y, z = symbols('x, y, z')
    f = sum_cyc(x**4/(8*x**3 + 5*y**3)) - (x + y + z)/13
    u, v = symbols('u, v', positive = True)
    # x <= z <= y
    print('f(xzy) =', factor(f.subs(z, x*(1 + u)).subs(y, x*(1 + u + v))))
    # x <= y <= z doesn't work
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    f = 65*u**10 + 215*u**9*v + 546*u**9 + 285*u**8*v**2 + 1503*u**8*v + 1989*u**8 + 275*u**7*v**3 + 1488*u**7*v**2 + 4284*u**7*v + 4095*u**7 + 315*u**6*v**4 + 1061*u**6*v**3 + 2436*u**6*v**2 + 6093*u**6*v + 5226*u**6 + 285*u**5*v**5 + 1290*u**5*v**4 + 591*u**5*v**3 - 441*u**5*v**2 + 4029*u**5*v + 4329*u**5 + 135*u**4*v**6 + 1185*u**4*v**5 + 1725*u**4*v**4 - 3020*u**4*v**3 - 5898*u**4*v**2 + 570*u**4*v + 2392*u**4 + 25*u**3*v**7 + 500*u**3*v**6 + 1890*u**3*v**5 + 779*u**3*v**4 - 5556*u**3*v**3 - 6582*u**3*v**2 - 326*u**3*v + 858*u**3 + 75*u**2*v**7 + 690*u**2*v**6 + 1866*u**2*v**5 + 762*u**2*v**4 - 2778*u**2*v**3 - 2400*u**2*v**2 + 192*u**2*v + 156*u**2 + 75*u*v**7 + 636*u*v**6 + 1617*u*v**5 + 1527*u*v**4 + 318*u*v**3 + 114*u*v**2 + 156*u*v + 65*v**7 + 351*v**6 + 741*v**5 + 754*v**4 + 390*v**3 + 156*v**2
    s, t = symbols('s, t', positive = True)
    # u, v <= 1 doesn't work
    # u <= v <= 1
    print('f(uv1) =', factor(f.subs(v, 1/(1 + s)).subs(u, 1/(1 + s + t))))
    # v <= u <= 1
    print('f(vu1) =', factor(f.subs(u, 1/(1 + s)).subs(v, 1/(1 + s + t))))
    # u <= 1 <= v
    print('f(u1v) =', factor(f.subs(u, 1/(1 + s)).subs(v, 1 + t)))
    # v <= 1 <= u
    print('f(v1u) =', factor(f.subs(v, 1/(1 + s)).subs(u, 1 + t)))
    # 1 <= u, v
    print('f(1uv) =', factor(f.subs(u, 1 + s).subs(v, 1 + t)))

if __name__ == '__main__':
    main()