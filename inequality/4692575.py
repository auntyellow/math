from sympy import *

# https://math.stackexchange.com/q/4692575

def main():
    p, q = symbols('p, q', positive = True)
    # a, b >= 1 >= c
    a = 1 + p
    b = 1 + q
    # c >= 1 >= a, b
    # a = 1/(1 + p)
    # b = 1/(1 + q)
    c = 1/a/b
    print(factor(1/a + 1/b + 1/c + 6/(a + b + c) - 5))

if __name__ == '__main__':
    main()