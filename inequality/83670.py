from sympy import *

def main():
    x = symbols('x')
    # https://math.stackexchange.com/q/3831395
    ineq = x**5 - x**3/2 - x + Integer(4)/5
    # x >= 1
    print('ineq(1,) =', factor(ineq.subs(x, x + 1)))
    # 1/2 <= x <= 1
    print('ineq(.5,1) =', factor(ineq.subs(x, 1 - 1/(2 + x))))
    # 0 <= x <= 1/2
    print('ineq(0,.5) =', factor(ineq.subs(x, 1/(2 + x))))
    print()

    # https://math.stackexchange.com/q/83670
    ineq = x**8 - x**7 + 2*x**6 - 2*x**5 + 3*x**4 - 3*x**3 + 4*x**2 - 4*x + Integer(5)/2
    # x >= 1
    print('ineq(1,) =', factor(ineq.subs(x, x + 1)))
    # 0 <= x <= 1
    print('ineq(0,1) =', factor(ineq.subs(x, 1/(1 + x))))
    # x <= 0
    print('ineq(,0) =', factor(ineq.subs(x, -x)))

if __name__ == '__main__':
    main()