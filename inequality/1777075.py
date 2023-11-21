from sympy import *

# https://math.stackexchange.com/a/2120874
# https://math.stackexchange.com/q/1777075

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    x, y, z = symbols('x, y, z', negative = False)
    f = sum_cyc(x**3/(13*x**2 + 5*y**2), (x, y, z)) - (x + y + z)/18
    # This is not always non-negative:
    # f = sum_cyc(x**3/(8*x**2 + 3*y**2), (x, y, z)) - (x + y + z)/11
    u, v = symbols('u, v', negative = False)
    # x <= z <= y
    print('f(xzy) =', factor(f.subs(z, x*(1 + u)).subs(y, x*(1 + u + v))))
    # x <= y <= z doesn't work
    print('f(xyz) =', factor(f.subs(y, x*(1 + u)).subs(z, x*(1 + u + v))))
    f = 90*u**7 + 190*u**6*v + 396*u**6 + 120*u**5*v**2 + 542*u**5*v + 630*u**5 + 55*u**4*v**3 + 41*u**4*v**2 + 164*u**4*v + 504*u**4 + 60*u**3*v**4 - 40*u**3*v**3 - 824*u**3*v**2 - 416*u**3*v + 252*u**3 + 25*u**2*v**5 + 115*u**2*v**4 - 332*u**2*v**3 - 984*u**2*v**2 - 156*u**2*v + 72*u**2 + 50*u*v**5 + 206*u*v**4 - 64*u*v**3 - 192*u*v**2 + 72*u*v + 90*v**5 + 216*v**4 + 108*v**3 + 72*v**2
    # proved non-negative in polynomial-prover.py
    '''
    s, t = symbols('s, t', negative = False)
    # u <= v <= 1 doesn't work
    print('f(uv1) =', factor(f.subs(v, 1/(1 + s)).subs(u, 1/(1 + s + t))))
    # v <= u <= 1
    print('f(vu1) =', factor(f.subs(u, 1/(1 + s)).subs(v, 1/(1 + s + t))))
    # u <= 1 <= v doesn't work
    print('f(u1v) =', factor(f.subs(u, 1/(1 + s)).subs(v, 1 + t)))
    # v <= 1 <= u
    print('f(v1u) =', factor(f.subs(v, 1/(1 + s)).subs(u, 1 + t)))
    # 1 <= u <= v doesn't work
    print('f(1uv) =', factor(f.subs(u, 1 + s).subs(v, 1 + s + t)))
    # 1 <= v <= u
    print('f(1vu) =', factor(f.subs(v, 1 + s).subs(u, 1 + s + t)))
    '''

if __name__ == '__main__':
    main()