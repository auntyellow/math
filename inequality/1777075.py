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
    # easy
    # ineq = sum_cyc(x**3/(2*x**2 + y**2)) - (x + y + z)/3
    # ineq = sum_cyc(x**3/(11*x**2 + 5*y**2)) - (x + y + z)/16
    ineq = sum_cyc(x**3/(12*x**2 + 5*y**2)) - (x + y + z)/17
    # hard
    # ineq = sum_cyc(x**3/(5*x**2 + 2*y**2)) - (x + y + z)/7
    # ineq = sum_cyc(x**3/(13*x**2 + 5*y**2)) - (x + y + z)/18
    p, q = symbols('p, q', positive = True)
    # x <= z <= y
    print('ineq(xzy) =', factor(ineq.subs(z, x*(1 + p)).subs(y, x*(1 + p + q))))
    # x <= y <= z doesn't work
    print('ineq(xyz) =', factor(ineq.subs(y, x*(1 + p)).subs(z, x*(1 + p + q))))
    ineq = 85*p**7 + 185*p**6*q + 391*p**6 + 130*p**5*q**2 + 582*p**5*q + 680*p**5 + 70*p**4*q**3 + 146*p**4*q**2 + 394*p**4*q + 629*p**4 + 65*p**3*q**4 + 40*p**3*q**3 - 504*p**3*q**2 - 66*p**3*q + 357*p**3 + 25*p**2*q**5 + 135*p**2*q**4 - 157*p**2*q**3 - 609*p**2*q**2 + 39*p**2*q + 102*p**2 + 50*p*q**5 + 231*p*q**4 + 86*p*q**3 - 12*p*q**2 + 102*p*q + 85*q**5 + 221*q**4 + 153*q**3 + 102*q**2
    r = symbols('r', positive = True)
    # p <= q doesn't work
    print('ineq(pq) =', factor(ineq.subs(q, p*(1 + r))))
    # q <= p
    print('ineq(qp) =', factor(ineq.subs(p, q*(1 + r))))
    ineq = 25*p**5*r**5 + 190*p**5*r**4 + 580*p**5*r**3 + 980*p**5*r**2 + 1040*p**5*r + 560*p**5 + 50*p**4*r**5 + 385*p**4*r**4 + 1080*p**4*r**3 + 1576*p**4*r**2 + 1784*p**4*r + 1344*p**4 + 85*p**3*r**5 + 656*p**3*r**4 + 1617*p**3*r**3 + 1261*p**3*r**2 + 264*p**3*r + 729*p**3 + 221*p**2*r**4 + 970*p**2*r**3 + 975*p**2*r**2 - 142*p**2*r + 261*p**2 + 153*p*r**3 + 447*p*r**2 + 474*p*r + 537*p + 102*r**2 + 306*r + 306
    s = symbols('s', positive = True)
    # p <= r
    print('ineq(pr) =', factor(ineq.subs(r, p*(1 + s))))
    # r <= p
    print('ineq(rp) =', factor(ineq.subs(p, r*(1 + s))))
    

if __name__ == '__main__':
    main()