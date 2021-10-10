from sympy import Eq, simplify, solve, symbols

def pair(conic, line):
    x, y = symbols('x, y')
    p = solve([conic, Eq(y, line)], (x, y))
    return (simplify(p[0][0]), simplify(p[0][1])), (simplify(p[1][0]), simplify(p[1][1]))

def main():
    a, b, c, d, e, f, g, h, k, x, y = symbols('a, b, c, d, e, f, g, h, k, x, y')
    conic = Eq(a*x**2 + 2*b*x*y + c*y**2 + 2*d*x + 2*e*y + f, 0)
    (F, A), (D, C), (B, E) = pair(conic, g*x), pair(conic, h*x), pair(conic, k)
    print('x_A =', A[0])
    print('x_B =', B[0])
    print('x_C =', C[0])
    print('x_D =', D[0])
    print('x_E =', E[0])
    print('x_F =', F[0])

    subs = {a: 1, b: 0, c: 1, d: 0, e: 0, f: -1, g: 1, h: -1, k: 0}

    print('x_A =', A[0].evalf(subs = subs))
    print('x_B =', B[0].evalf(subs = subs))
    print('x_C =', C[0].evalf(subs = subs))
    print('x_D =', D[0].evalf(subs = subs))
    print('x_E =', E[0].evalf(subs = subs))
    print('x_F =', F[0].evalf(subs = subs))

if __name__ == '__main__':
    main()