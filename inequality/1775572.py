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
    print('ineq(xzy) =', factor(ineq.subs(z, x*(1 + p)).subs(y, x*(1 + p + q))))
    # x <= y <= z doesn't work
    print('ineq(xyz) =', factor(ineq.subs(y, x*(1 + p)).subs(z, x*(1 + p + q))))
    ineq = 65*p**10 + 215*p**9*q + 546*p**9 + 285*p**8*q**2 + 1503*p**8*q + 1989*p**8 + 275*p**7*q**3 + 1488*p**7*q**2 + 4284*p**7*q + 4095*p**7 + 315*p**6*q**4 + 1061*p**6*q**3 + 2436*p**6*q**2 + 6093*p**6*q + 5226*p**6 + 285*p**5*q**5 + 1290*p**5*q**4 + 591*p**5*q**3 - 441*p**5*q**2 + 4029*p**5*q + 4329*p**5 + 135*p**4*q**6 + 1185*p**4*q**5 + 1725*p**4*q**4 - 3020*p**4*q**3 - 5898*p**4*q**2 + 570*p**4*q + 2392*p**4 + 25*p**3*q**7 + 500*p**3*q**6 + 1890*p**3*q**5 + 779*p**3*q**4 - 5556*p**3*q**3 - 6582*p**3*q**2 - 326*p**3*q + 858*p**3 + 75*p**2*q**7 + 690*p**2*q**6 + 1866*p**2*q**5 + 762*p**2*q**4 - 2778*p**2*q**3 - 2400*p**2*q**2 + 192*p**2*q + 156*p**2 + 75*p*q**7 + 636*p*q**6 + 1617*p*q**5 + 1527*p*q**4 + 318*p*q**3 + 114*p*q**2 + 156*p*q + 65*q**7 + 351*q**6 + 741*q**5 + 754*q**4 + 390*q**3 + 156*q**2
    r, s = symbols('r, s', positive = True)
    # p, q <= 1 doesn't work
    # p <= q <= 1
    print('ineq(pq1) =', factor(ineq.subs(q, 1/(1 + r)).subs(p, 1/(1 + r + s))))
    # q <= p <= 1
    print('ineq(qp1) =', factor(ineq.subs(p, 1/(1 + r)).subs(q, 1/(1 + r + s))))
    # p <= 1 <= q
    print('ineq(p1q) =', factor(ineq.subs(p, 1/(1 + r)).subs(q, 1 + s)))
    # q <= 1 <= p
    print('ineq(q1p) =', factor(ineq.subs(q, 1/(1 + r)).subs(p, 1 + s)))
    # 1 <= p, q
    print('ineq(1pq) =', factor(ineq.subs(p, 1 + r).subs(q, 1 + s)))

if __name__ == '__main__':
    main()