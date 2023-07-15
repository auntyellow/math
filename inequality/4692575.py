from sympy import *

# https://math.stackexchange.com/q/4692575

def main():
    a, b, c = symbols('a, b, c', positive = True)
    ineq = 1/a + 1/b + 1/c + 6/(a + b + c) - 5
    p, q = symbols('p, q', positive = True)
    # a <= 1 <= b, c
    print('ineq(a1bc) = ', factor(ineq.subs(a, 1/b/c).subs(b, 1 + p).subs(c, 1 + q)))
    # a, b <= 1 <= c 
    print('ineq(ab1c) = ', factor(ineq.subs(c, 1/a/b).subs(a, 1/(1 + p)).subs(b, 1/(1 + q))))

if __name__ == '__main__':
    main()