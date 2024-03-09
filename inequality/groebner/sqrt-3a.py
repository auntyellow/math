from sympy import *

def main():
    # sum_cyc(sqrt(a/b)) >= 3
    a, b, c = symbols('a, b, c', negative = False)
    # result from sqrt-3-sage.py
    # B = [..., a + b + c - 1, B4, B2*B3, B0*B1*B2]
    B0 = 3*c - 1
    B1 = 5*c**2 - 10*c + 1
    B2 = 5*c**2 - 1
    B3 = 2*b + c - 1
    B4 = -10336*b**2 - 10336*b*c + 10336*b + 87075*c**7 - 337725*c**6 + 526425*c**5 - 405505*c**4 + 1737*c**3 + 114677*c**2 - 32437*c + 121
    c0 = solve(B0)[0]
    c1 = solve(B1)[0] # another root > 1
    c2 = solve(B2)[0] # can't use B3
    print('c0 =', c0)
    print('c1 =', c1)
    print('c2 =', c2)
    b0 = solve(B3.subs(c, c0))[0]
    print('b0 =', b0)
    print('verified by B4?', B4.subs({b: b0, c: c0}) == 0)
    b1 = solve(B3.subs(c, c1))[0]
    print('b1 =', b1)
    print('verified by B4?', simplify(B4.subs({b: b1, c: c1})) == 0)
    b2 = solve(B4.subs(c, c2))
    print(f'b2 = {b2} = [{N(b2[0])}, {N(b2[1])}]') # simplify doesn't work here
    b2 = [1 - 2/sqrt(5), 1/sqrt(5)]
    print(f'b2 = {b2} = [{N(b2[0])}, {N(b2[1])}]')
    print('a0 =', 1 - b0 - c0)
    print('a1 =', 1 - b1 - c1)
    print('a2 =', [1 - c2 - b2[0], 1 - c2 - b2[1]])
    print()

    # check if critical point
    a = 1 - b - c
    f = sqrt(a/(b + c)) + sqrt(b/(a + c)) + sqrt(c/(a + b)) - 2
    H = hessian(f, [b, c])
    H0 = N(H.subs({b: b0, c: c0}))
    print('H0 =', H0)
    print('|H0| =', det(H0)) # local minimum
    print('f0 =', N(f.subs({b: b0, c: c0})))
    H1 = N(H.subs({b: b1, c: c1}))
    print('H1 =', H1)
    print('|H1| =', det(H1)) # saddle point
    print('f1 =', N(f.subs({b: b1, c: c1})))

if __name__ == '__main__':
    main()