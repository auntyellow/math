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
    # easy https://artofproblemsolving.com/community/c6h23113
    # ineq = sum_cyc(x**4/(x**3 + y**3)) - (x + y + z)/2
    ineq = sum_cyc(x**4/(3*x**3 + 2*y**3)) - (x + y + z)/5
    # hard https://math.stackexchange.com/q/1775572
    # ineq = sum_cyc(x**4/(8*x**3 + 5*y**3)) - (x + y + z)/13
    p, q = symbols('p, q', positive = True)
    # x <= z <= y
    print('ineq(xzy) =', factor(ineq.subs(z, x*(1 + p)).subs(y, x*(1 + p + q))))
    # x <= y <= z doesn't work
    print('ineq(xyz) =', factor(ineq.subs(y, x*(1 + p)).subs(z, x*(1 + p + q))))
    ineq = 10*p**10 + 34*p**9*q + 85*p**9 + 48*p**8*q**2 + 243*p**8*q + 315*p**8 + 50*p**7*q**3 + 267*p**7*q**2 + 720*p**7*q + 665*p**7 + 56*p**6*q**4 + 221*p**6*q**3 + 525*p**6*q**2 + 1109*p**6*q + 880*p**6 + 48*p**5*q**5 + 246*p**5*q**4 + 276*p**5*q**3 + 267*p**5*q**2 + 909*p**5*q + 765*p**5 + 22*p**4*q**6 + 204*p**4*q**5 + 390*p**4*q**4 - 130*p**4*q**3 - 450*p**4*q**2 + 384*p**4*q + 445*p**4 + 4*p**3*q**7 + 82*p**3*q**6 + 336*p**3*q**5 + 300*p**3*q**4 - 485*p**3*q**3 - 627*p**3*q**2 + 127*p**3*q + 165*p**3 + 12*p**2*q**7 + 114*p**2*q**6 + 336*p**2*q**5 + 270*p**2*q**4 - 180*p**2*q**3 - 177*p**2*q**2 + 84*p**2*q + 30*p**2 + 12*p*q**7 + 103*p*q**6 + 276*p*q**5 + 306*p*q**4 + 141*p*q**3 + 69*p*q**2 + 30*p*q + 10*q**7 + 55*q**6 + 120*q**5 + 130*q**4 + 75*q**3 + 30*q**2
    r = symbols('r', positive = True)
    # p <= q
    print('ineq(pq) =', factor(ineq.subs(q, p*(1 + r))))
    # q <= p
    print('ineq(qp) =', factor(ineq.subs(p, q*(1 + r))))

if __name__ == '__main__':
    main()