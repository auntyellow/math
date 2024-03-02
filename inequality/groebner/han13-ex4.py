from sympy import *

# http://xbna.pku.edu.cn/CN/Y2013/V49/I4/545 , ex 4.4

def main():
    a, b, c, u, v = symbols('a, b, c, u, v', negative = False)
    # equality occurs when a = sin(pi/7)**2, b = sin(4*pi/7)**2 and c = sin(2*pi/7)**2
    # see https://math.stackexchange.com/q/2587996/
    f = (a**2 + b**2 + c**2)**2 - 3*(a**3*b + b**3*c + c**3*a)
    print('f(abc) =', factor(f.subs(c, a*(1 + u + v)).subs(b, a*(1 + u))))
    print('f(acb) =', factor(f.subs(b, a*(1 + u + v)).subs(c, a*(1 + u))))
    # f(acb)
    g = u**4 - u**3*v + u**3 - u**2*v**2 - 3*u**2*v + u**2 + u*v**3 - 2*u*v**2 + u*v + v**4 + v**3 + v**2
    # proved by polynomial-prover
    print('g(uv) =', factor(g.subs(v, u*(1 + v))))
    # unable to find rational zeros
    print('g(vu) =', factor(g.subs(u, v*(1 + u))))
    # g(vu)
    g1 = u**4*v**2 + 3*u**3*v**2 + u**3*v + 2*u**2*v**2 + u**2 - 5*u*v + 3*u + v**2 - 3*v + 3
    g1_u, g1_v = diff(g1, u), diff(g1, v)
    print('g1_u =', g1_u)
    print('g1_v =', g1_v)
    # B = groebner([g1_u, g1_v], v, u)
    # print(B)
    res = resultant(g1_u, g1_v, v)
    print('res =', factor(res), '= 0')
    u0 = nsolve(res, (0, 1), solver='bisect', verify=False)
    print('u =', u0)
    v0 = solve(g1_v.subs(u, u0))[0]
    print('v =', v0)
    print('g0 =', N(g1.subs(u, u0).subs(v, v0)))
    print()

    # prove g1(v0, u0) = 0:
    h1 = u**3 + 4*u**2 + 3*u - 1
    print('h1 =', h1)
    h2 = prem(g1_v, h1, u)
    print('h2 =', h2)
    R = prem(g1, h2, v)
    print('R =', R)
    R = prem(R, h1)
    print('R =', R)
    print()

    # another way to prove g1(v0, u0) = 0:
    res = resultant(g1, h1, u)
    print('res =', factor(res), '= 0')
    # disc = 0 means g1(v0) = g1_v(v0) = 0
    print('disc =', discriminant(res))

if __name__ == '__main__':
    main()