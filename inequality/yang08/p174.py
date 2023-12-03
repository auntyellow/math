import logging, itertools
from sympy import *

# ISBN 9787030207210, p174, 6-var Vasc's conjuction

def main():
    a1, a2, a3, a4, a5, a6 = symbols('a1, a2, a3, a4, a5, a6', negative = False)
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + \
        (a4 - a5)/(a5 + a6) + (a5 - a6)/(a6 + a1) + (a6 - a1)/(a1 + a2)
    f = fraction(cancel(f.subs(a6, 1)))
    print('f =', f)
    a1, a2, a3, a4, a5, a6 = 6.976670613304777e-07, 1.1409691171747112, 0.14036439615990903, 1.0290075762514708, 0.09001781709032528, 1
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + \
        (a4 - a5)/(a5 + a6) + (a5 - a6)/(a6 + a1) + (a6 - a1)/(a1 + a2)
    print('f(...) =', f)

if __name__ == '__main__':
    main()