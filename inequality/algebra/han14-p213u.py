from sympy import *

# ISBN 9787560349800, p213, ex 8.10

def main():
    a, b, c, x, y, z = symbols('a, b, c, x, y, z', negative = False)
    f = (x + a)/(a*c*x*y) + (y + b)/(b*a*y*z) + (z + c)/(c*b*z*x) - 3*(a + x)*(b + y)*(c + z)/(a*b*c + x*y*z)**2
    print(f.subs({a: 1, b: 2, c: 3, x: 1, y: 1, z: 1}))
    print(f.subs({a: 1, b: 1, c: 1, x: 1, y: 2, z: 3}))
    # print('f(a = max(abcxyz)) =', factor(f.subs({b: a*(1 - b), c: a*(1 - c), x: a*(1 - x), y: a*(1 - y), z: a*(1 - z)})))

if __name__ == '__main__':
    main()