from sympy import *

# https://math.stackexchange.com/q/1767225

def main():
    a, b, c, d, e, f, g, h, j, k, m, n, x, y = symbols('a, b, c, d, e, f, g, h, j, k, m, n, x, y')
    F1 = a*x**2 + b*x*y + c*y**2 + d*x + e*y + f
    F2 = g*x**2 + h*x*y + j*y**2 + k*x + m*y + n

    # method 1: eliminate y
    y0 = solve(j*F1 - c*F2, y)[0]
    print('y =', y0)
    F12 = fraction(cancel(F1.subs(y, y0)))[0]/c
    print(poly(F12, x).expr, '= 0')
    print()

    # method 2: resultant
    F12 = resultant(F1, F2, y)
    print(poly(F12, x).expr, '= 0')
    print()

    # method 3: groebner basis (too slow)
    # print(groebner([F1, F2], y, x))
    # result from 1767225-sage.py
    F12 = x**4 + ((-c*e*g*h + c*d*h**2 - 2*c*d*g*j + 2*b*e*g*j - b*d*h*j - a*e*h*j + 2*a*d*j**2 + 2*c**2*g*k - b*c*h*k + b**2*j*k - 2*a*c*j*k - b*c*g*m + 2*a*c*h*m - a*b*j*m)/(c**2*g**2 - b*c*g*h + a*c*h**2 + b**2*g*j - 2*a*c*g*j - a*b*h*j + a**2*j**2))*x**3 + ((c*f*h**2 + e**2*g*j - 2*c*f*g*j - d*e*h*j - b*f*h*j + d**2*j**2 + 2*a*f*j**2 - c*e*h*k - 2*c*d*j*k + 2*b*e*j*k + c**2*k**2 - c*e*g*m + 2*c*d*h*m - b*d*j*m - a*e*j*m - b*c*k*m + a*c*m**2 + 2*c**2*g*n - b*c*h*n + b**2*j*n - 2*a*c*j*n)/(c**2*g**2 - b*c*g*h + a*c*h**2 + b**2*g*j - 2*a*c*g*j - a*b*h*j + a**2*j**2))*x**2 + ((-e*f*h*j + 2*d*f*j**2 + e**2*j*k - 2*c*f*j*k + 2*c*f*h*m - d*e*j*m - b*f*j*m - c*e*k*m + c*d*m**2 - c*e*h*n - 2*c*d*j*n + 2*b*e*j*n + 2*c**2*k*n - b*c*m*n)/(c**2*g**2 - b*c*g*h + a*c*h**2 + b**2*g*j - 2*a*c*g*j - a*b*h*j + a**2*j**2))*x + (f**2*j**2 - e*f*j*m + c*f*m**2 + e**2*j*n - 2*c*f*j*n - c*e*m*n + c**2*n**2)/(c**2*g**2 - b*c*g*h + a*c*h**2 + b**2*g*j - 2*a*c*g*j - a*b*h*j + a**2*j**2)
    F12 = fraction(cancel(F12))[0]
    print(poly(F12, x).expr, '= 0')
    print()

    # method 4: pencil
    C1 = Matrix([[a, b/2, d/2], [b/2, c, e/2], [d/2, e/2, f]])
    C2 = Matrix([[g, h/2, k/2], [h/2, j, m/2], [k/2, m/2, n]])
    X = Matrix([[x, y, 1]])
    print('F1 =', expand((X*C1*X.transpose())[0, 0]))
    print('F2 =', expand((X*C2*X.transpose())[0, 0]))
    t = symbols('t')
    T = det(C1 + t*C2)
    print('T =', poly(T, t).expr)
    # TODO solve t and factor T

if __name__ == '__main__':
    main()