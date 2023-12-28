import logging, itertools
from sympy import *

# Vasc's conjecture
# https://math.stackexchange.com/a/4693459

def gen_vasc(a, n):
    f = 0
    for i in range(n):
        ai, ai1, ai2 = a[i], a[(i + 1)%n], a[(i + 2)%n]
        f += (ai - ai1)/(ai1 + ai2)
    return f

def main():
    a = symbols('a1, a2, a3, a4, a5, a6, a7, a8, a9, a10', negative = False)
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = a
    '''
    print('5-var Vasc\'s conjecture')
    fn, fd = fraction(cancel(gen_vasc(a, 5)))
    print('fn =', fn)
    print('fd =', fd)
    print()
    print('6-var Vasc\'s conjecture')
    fn, fd = fraction(cancel(gen_vasc(a, 6).subs(a6, 1)))
    print('fn =', fn)
    print('fd =', fd)
    print()
    print('7-var Vasc\'s conjecture')
    fn, fd = fraction(cancel(gen_vasc(a, 7)))
    print('fn =', fn)
    print('fd =', fd)
    print()
    print('8-var Vasc\'s conjecture')
    fn, fd = fraction(cancel(gen_vasc(a, 8).subs(a8, 1)))
    print('fn =', fn)
    print('fd =', fd)
    print()
    print('9-var Vasc\'s conjecture')
    fn, fd = fraction(cancel(gen_vasc(a, 9)))
    print('fn =', fn)
    print('fd =', fd)
    print()
    print('10-var Vasc\'s conjecture')
    fn, fd = fraction(cancel(gen_vasc(a, 10).subs(a10, 1)))
    print('fn =', fn)
    print('fd =', fd)
    print()
    '''
    print('6-var Vasc\'s conjecture')
    # result from vasc-bh.py
    a0 = (0, S(929380)/864801, S(74402)/705831, S(366165)/383132, S(4529)/375041, 1)
    print('f(...) =', gen_vasc(a0, 6))
    print()
    print('8-var Vasc\'s conjecture')
    # result from vasc-bh.py
    a0 = (0, S(890043)/698869, S(2954)/454313, S(1580103)/996818, S(223591)/479341, S(445163)/378456, S(30775)/95986, 1)
    print('f(...) =', gen_vasc(a0, 8))
    print()
    print('10-var Vasc\'s conjecture')
    # result from vasc-bh.py
    a0 = (0, S(956875)/790624, 0, S(1009269)/693958, S(114517)/768733, S(1065208)/755933, S(20029)/53395, S(1029077)/998050, S(141689)/845191, 1)
    print('f(...) =', gen_vasc(a0, 10))

if __name__ == '__main__':
    main()