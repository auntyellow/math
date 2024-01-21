from math import nan, sqrt
import matplotlib.pyplot as plt

S13 = 1/sqrt(3)
S43 = 2/sqrt(3)
S176 = 17/6

def z(x, y):
    a = x - S13*y
    b = S43*y
    c = 1 - a - b
    if a < 0 or b < 0 or c < 0 or a*b + a*c + b*c == 0:
        return nan
    z0 = a/sqrt(a**2 + 8*b*c) + b/sqrt(b**2 + 8*a*c) + c/sqrt(c**2 + 8*a*b) - 1
    # mark the case u < 11/6 in imo-2001-2.py
    m0, m2 = min(a, b, c), max(a, b, c)
    if m2 < S176*m0:
        return -z0
    # mark the case u > 12 in imo-2001-2.py
    if 13*m0 < m2:
        return -z0
    return z0

def main():
    len = 1
    res = 500
    Z = [[z(j/res, i/res) for j in range(len*res)] for i in range(len*res)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()