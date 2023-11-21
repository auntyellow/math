import logging
from itertools import permutations
from sympy import *

def non_negative(f, vars):
    sub_cnt = len(vars)
    for order in permutations(vars):
        f1 = f
        x = order[0]
        for i in range(1, sub_cnt):
            y = order[i]
            # much faster than f1 = f1.subs(...) ... expand(...)
            f1 = expand(f1.subs(x, x + y))
            x = y
        # TODO is each term positive?
        print(f1)

def main():
    logging.basicConfig(level = 'INFO')

    # ISBN 9787030207210, p169, §7.3.2, problem 5
    a1, a2, a3, a4, a5 = symbols('a1, a2, a3, a4, a5', negative = False)
    f = a1/(a2 + a3) + a2/(a3 + a4) + a3/(a4 + a5) + a4/(a5 + a1) + a5/(a1 + a2) - S(5)/2
    f = fraction(cancel(f))[0]
    non_negative(f, [a1, a2, a3, a4, a5])

if __name__ == '__main__':
    main()