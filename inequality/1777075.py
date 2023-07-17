from sympy import *

# https://math.stackexchange.com/a/2120874
# https://math.stackexchange.com/q/1777075

def cyc(p):
    x, y, z, t = symbols('x, y, z, t')
    return p.subs(x, t).subs(y, x).subs(z, y).subs(t, z)

def sum_cyc(p):
    p1 = cyc(p)
    return p + p1 + cyc(p1)

def main():
    x, y, z = symbols('x, y, z')
    ineq = sum_cyc(x**3/(13*x**2 + 5*y**2)) - (x + y + z)/18
    # This is not always non-negative:
    # ineq = sum_cyc(x**3/(8*x**2 + 3*y**2)) - (x + y + z)/11
    p, q = symbols('p, q', positive = True)
    # x <= z <= y
    print('ineq(xzy) =', factor(ineq.subs(z, x*(1 + p)).subs(y, x*(1 + p + q))))
    # x <= y <= z doesn't work
    print('ineq(xyz) =', factor(ineq.subs(y, x*(1 + p)).subs(z, x*(1 + p + q))))
    ineq = 90*p**7 + 190*p**6*q + 396*p**6 + 120*p**5*q**2 + 542*p**5*q + 630*p**5 + 55*p**4*q**3 + 41*p**4*q**2 + 164*p**4*q + 504*p**4 + 60*p**3*q**4 - 40*p**3*q**3 - 824*p**3*q**2 - 416*p**3*q + 252*p**3 + 25*p**2*q**5 + 115*p**2*q**4 - 332*p**2*q**3 - 984*p**2*q**2 - 156*p**2*q + 72*p**2 + 50*p*q**5 + 206*p*q**4 - 64*p*q**3 - 192*p*q**2 + 72*p*q + 90*q**5 + 216*q**4 + 108*q**3 + 72*q**2
    r, s = symbols('r, s', positive = True)
    # p <= q <= 1 doesn't work
    print('ineq(pq1) =', factor(ineq.subs(q, 1/(1 + r)).subs(p, 1/(1 + r + s))))
    # q <= p <= 1
    print('ineq(qp1) =', factor(ineq.subs(p, 1/(1 + r)).subs(q, 1/(1 + r + s))))
    # p <= 1 <= q doesn't work
    print('ineq(p1q) =', factor(ineq.subs(p, 1/(1 + r)).subs(q, 1 + s)))
    # q <= 1 <= p
    print('ineq(q1p) =', factor(ineq.subs(q, 1/(1 + r)).subs(p, 1 + s)))
    # 1 <= p <= q doesn't work
    print('ineq(1pq) =', factor(ineq.subs(p, 1 + r).subs(q, 1 + r + s)))
    # 1 <= q <= p
    print('ineq(1qp) =', factor(ineq.subs(q, 1 + r).subs(p, 1 + r + s)))

if __name__ == '__main__':
    main()