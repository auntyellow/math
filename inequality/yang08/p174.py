import logging, itertools
from sympy import *

# ISBN 9787030207210, p174, 6-var Vasc's conjuction

def main():
    a1, a2, a3, a4, a5, a6, a7, a8 = symbols('a1, a2, a3, a4, a5, a6, a7, a8', negative = False)
    print('6-var Vasc\'s conjuction')
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + \
        (a4 - a5)/(a5 + a6) + (a5 - a6)/(a6 + a1) + (a6 - a1)/(a1 + a2)
    fn, fd = fraction(cancel(f.subs(a6, 1)))
    print('fn =', fn)
    print('fd =', fd)
    print('8-var Vasc\'s conjuction')
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + (a4 - a5)/(a5 + a6) + \
        (a5 - a6)/(a6 + a7) + (a6 - a7)/(a7 + a8) + (a7 - a8)/(a8 + a1) + (a8 - a1)/(a1 + a2)
    fn, fd = fraction(cancel(f.subs(a8, 1)))
    print('fn =', fn)
    print('fd =', fd)
    print('6-var Vasc\'s conjuction')
    a1, a2, a3, a4, a5, a6 = 6.976670613304777e-07, 1.1409691171747112, 0.14036439615990903, 1.0290075762514708, 0.09001781709032528, 1
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + \
        (a4 - a5)/(a5 + a6) + (a5 - a6)/(a6 + a1) + (a6 - a1)/(a1 + a2)
    print('f(...) =', f)
    print('8-var Vasc\'s conjuction')
    a1, a2, a3, a4, a5, a6, a7, a8 = 4.093344943826459e-11, 1.2619401528955225, 0.01863800491561328, 1.4932722180748064, 0.2920140535951068, 1.2170758709711391, 0.23964731019647567, 1
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + (a4 - a5)/(a5 + a6) + \
        (a5 - a6)/(a6 + a7) + (a6 - a7)/(a7 + a8) + (a7 - a8)/(a8 + a1) + (a8 - a1)/(a1 + a2)
    print('f(...) =', f)

if __name__ == '__main__':
    main()