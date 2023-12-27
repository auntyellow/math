import logging, itertools
from sympy import *

# ISBN 9787030207210, p174, 6-var Vasc's conjecture

def main():
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = symbols('a1, a2, a3, a4, a5, a6, a7, a8, a9, a10', negative = False)
    print('5-var Vasc\'s conjecture')
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + \
        (a3 - a4)/(a4 + a5) + (a4 - a5)/(a5 + a1) + (a5 - a1)/(a1 + a2)
    fn, fd = fraction(cancel(f))
    print('fn =', fn)
    print('fd =', fd)
    print()
    print('6-var Vasc\'s conjecture')
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + \
        (a4 - a5)/(a5 + a6) + (a5 - a6)/(a6 + a1) + (a6 - a1)/(a1 + a2)
    fn, fd = fraction(cancel(f.subs(a6, 1)))
    print('fn =', fn)
    print('fd =', fd)
    print()
    print('7-var Vasc\'s conjecture')
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + \
        (a4 - a5)/(a5 + a6) + (a5 - a6)/(a6 + a7) + (a6 - a7)/(a7 + a1) + (a7 - a1)/(a1 + a2)
    fn, fd = fraction(cancel(f))
    print('fn =', fn)
    print('fd =', fd)
    print()
    print('8-var Vasc\'s conjecture')
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + (a4 - a5)/(a5 + a6) + \
        (a5 - a6)/(a6 + a7) + (a6 - a7)/(a7 + a8) + (a7 - a8)/(a8 + a1) + (a8 - a1)/(a1 + a2)
    fn, fd = fraction(cancel(f.subs(a8, 1)))
    print('fn =', fn)
    print('fd =', fd)
    print()
    print('9-var Vasc\'s conjecture')
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + (a4 - a5)/(a5 + a6) + \
        (a5 - a6)/(a6 + a7) + (a6 - a7)/(a7 + a8) + (a7 - a8)/(a8 + a9) + (a8 - a9)/(a9 + a1) + (a9 - a1)/(a1 + a2)
    fn, fd = fraction(cancel(f))
    print('fn =', fn)
    print('fd =', fd)
    print()
    print('10-var Vasc\'s conjecture')
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + (a4 - a5)/(a5 + a6) + (a5 - a6)/(a6 + a7) + \
        (a6 - a7)/(a7 + a8) + (a7 - a8)/(a8 + a9) + (a8 - a9)/(a9 + a10) + (a9 - a10)/(a10 + a1) + (a10 - a1)/(a1 + a2)
    fn, fd = fraction(cancel(f.subs(a10, 1)))
    print('fn =', fn)
    print('fd =', fd)
    print()
    print('6-var Vasc\'s conjecture')
    a1, a2, a3, a4, a5, a6 = 6.976670613304777e-07, 1.1409691171747112, 0.14036439615990903, 1.0290075762514708, 0.09001781709032528, 1
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + \
        (a4 - a5)/(a5 + a6) + (a5 - a6)/(a6 + a1) + (a6 - a1)/(a1 + a2)
    print('f(...) =', f)
    print()
    print('8-var Vasc\'s conjecture')
    a1, a2, a3, a4, a5, a6, a7, a8 = 4.093344943826459e-11, 1.2619401528955225, 0.01863800491561328, 1.4932722180748064, 0.2920140535951068, 1.2170758709711391, 0.23964731019647567, 1
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + (a4 - a5)/(a5 + a6) + \
        (a5 - a6)/(a6 + a7) + (a6 - a7)/(a7 + a8) + (a7 - a8)/(a8 + a1) + (a8 - a1)/(a1 + a2)
    print('f(...) =', f)
    print()
    print('10-var Vasc\'s conjecture')
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = 0.10132961455129126, 1.1422173772021291, 0.346948219562095, 1.0077095883367586, 0.3783182697758817, 0.8007536838873939, 0.18103272230736667, 0.7407619169312529, 2.503440223257067e-10, 1
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + (a4 - a5)/(a5 + a6) + (a5 - a6)/(a6 + a7) + \
        (a6 - a7)/(a7 + a8) + (a7 - a8)/(a8 + a9) + (a8 - a9)/(a9 + a10) + (a9 - a10)/(a10 + a1) + (a10 - a1)/(a1 + a2)
    print('f(...) =', f)

if __name__ == '__main__':
    main()