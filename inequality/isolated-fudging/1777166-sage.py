from sympy import *

# https://math.stackexchange.com/q/1777166

def main():
    a, b, c = var('a, b, c')
    x = 2*a/sqrt((a + b)*(a + c))
    y = 2*b/sqrt((b + c)*(b + a))
    z = 2*c/sqrt((c + a)*(c + b))
    f5 = x**8

    m, n, p, q = var('m, n, p, q')
    n = 1
    m = -7*p/22 - q/2 + 2/11
    g = n*a**2 + m*(b**2 + c**2) + p*(a*b + a*c) + q*b*c
    h = (n + 2*m)*(a**2 + b**2 + c**2) + (2*p + q)*(a*b + a*c + b*c)
    f = f5 - (3*g/h)**5
    U = Integer(100)/99
    # a <= b <= c <= U*a
    u, v = var('u, v')
    # too slow and exhaust memory
    fabcU = factor(f.subs({c: a*(U + u)/(1 + u), b: a*(U + u + v)/(1 + u + v)}))
    fcbaU = factor(f.subs({a: c*(U + u)/(1 + u), b: c*(U + u + v)/(1 + u + v)}))
    fbacU = factor(f.subs({c: b*(U + u)/(1 + u), a: b*(U + u + v)/(1 + u + v)}))
    print()
    for fi in [fabcU, fcbaU, fbacU]:
        print(fi)

if __name__ == '__main__':
    main()