from math import nan, sqrt
import matplotlib.pyplot as plt

S13 = 1/sqrt(3)
S43 = 2/sqrt(3)
S176 = 17/6
SCALE = 1/3

def z(x, y):
    # a, b << c
    a = (x - S13*y)*SCALE
    b = S43*y*SCALE
    c = 1 - a - b
    if a < 0 or b < 0 or c < 1 - SCALE or a*b + a*c + b*c == 0:
        return nan
    z0 = a/sqrt(a**2 + 8*b*c) + b/sqrt(b**2 + 8*a*c) + c/sqrt(c**2 + 8*a*b) - 1
    return z0

def main():
    len = 1
    res = 500
    aspect = .87
    Z = [[z(j/res, i/res) for j in range(len*res)] for i in range(round(len*res*aspect))]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len*aspect], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()