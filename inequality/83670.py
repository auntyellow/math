from sympy import *

def main():
    x = symbols('x')
    # https://math.stackexchange.com/q/3831395
    f = x**5 - x**3/2 - x + Integer(4)/5
    # x >= 1
    print('f(1,) =', factor(f.subs(x, x + 1)))
    # 1/2 <= x <= 1
    print('f(.5,1) =', factor(f.subs(x, 1 - 1/(2 + x))))
    # 0 <= x <= 1/2
    print('f(0,.5) =', factor(f.subs(x, 1/(2 + x))))
    print()

    # https://math.stackexchange.com/q/83670
    f = x**8 - x**7 + 2*x**6 - 2*x**5 + 3*x**4 - 3*x**3 + 4*x**2 - 4*x + Integer(5)/2
    # x >= 1
    print('f(1,) =', factor(f.subs(x, x + 1)))
    # 0 <= x <= 1
    print('f(0,1) =', factor(f.subs(x, 1/(1 + x))))
    # x <= 0
    print('f(,0) =', factor(f.subs(x, -x)))

if __name__ == '__main__':
    main()