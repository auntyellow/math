from sympy import *

# https://math.stackexchange.com/a/2120874
# https://math.stackexchange.com/q/1775572

def cyc(p):
    x, y, z, t = symbols('x, y, z, t')
    return p.subs(x, t).subs(y, x).subs(z, y).subs(t, z)

def sum_cyc(p):
    p1 = cyc(p)
    return p + p1 + cyc(p1)

def main():
    x, y, z = symbols('x, y, z')
    ineq = sum_cyc(x**4/(8*x**3 + 5*y**3)) - (x + y + z)/13
    p, q = symbols('p, q', positive = True)
    # x <= z <= y
    print('ineq(xzy) =', factor(ineq.subs(z, x + p).subs(y, x + p + q)))
    print()
    # x <= y <= z doesn't work
    print('ineq(xyz) =', factor(ineq.subs(y, x + p).subs(z, x + p + q)))

if __name__ == '__main__':
    main()