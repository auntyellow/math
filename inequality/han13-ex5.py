from sympy import *

# http://xbna.pku.edu.cn/CN/Y2013/V49/I4/545 , ex 4.5

def main():
    a, b, c, d, e = symbols('a, b, c, d, e', negative = False)
    # (0, 0, 0, 0)
    f = (a**2 + 3)*(b**2 + 3)*(c**2 + 3)*(d**2 + 3) - 16*a**2 - 81
    # (sqrt(5)/3, sqrt(5)/3, 0, 0)
    f = (a**2 + 3)*(b**2 + 3)*(c**2 + 3)*(d**2 + 3) - 16*(a + b)**2 - S(704)/9
    # (1, 1, 1, 0)
    f = (a**2 + 3)*(b**2 + 3)*(c**2 + 3)*(d**2 + 3) - 16*(a + b + c)**2 - 48
    # (1, 1, 1, 1)
    f = (a**2 + 3)*(b**2 + 3)*(c**2 + 3)*(d**2 + 3) - 16*(a + b + c + d)**2
    print('f =', Poly(f).homogenize(e).expr)
    # proved by SDS

if __name__ == '__main__':
    main()