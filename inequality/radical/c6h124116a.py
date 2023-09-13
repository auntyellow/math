from math import *

def main():
    # https://artofproblemsolving.com/community/c6h124116
    # When does the equality hold (except for trival x = y = z = 0)? Assume x <= y <= z:
    xm, ym, zm, fm = -1, -1, -1, -inf
    x = 1
    for i in range(0, 2000):
        # y = 1 + i / 100.0
        # y = 1.33 + i / 100000.0
        y = 1.34210 + i / 100000000.0
        for j in range(0, 2000):
            # z = 1 + j / 100.0
            # z = 1.33 + j / 100000.0
            z = 1.34210 + j / 100000000.0
            f = sqrt(578*x**2 + 1143*y*z) + sqrt(578*y**2 + 1143*z*x) + sqrt(578*z**2 + 1143*x*y) - 253*sqrt(527)*(x + y + z)/140
            if f > fm:
                xm, ym, zm, fm = x, y, z, f
    print('xm = 1')
    print('ym =', ym)
    print('zm =', zm)
    print('fm =', fm)
    # 1st iteration: (1, 1.34, 1.34)
    # 2nd iteration: (1, 1.34211, 1.34211)
    # 3rd iteration: (1, 1.34210430, 1.34210505)
    # 1.342105 = 1 + 1/(2 + 1/(1 + 1/12)) = 51/38
    # (x, y, z) = (38, 51, 51)

if __name__ == '__main__':
    main()