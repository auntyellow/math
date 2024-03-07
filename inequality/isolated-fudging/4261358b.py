from math import nan, sqrt
import matplotlib.pyplot as plt

S13 = 1/sqrt(3)
S43 = 2/sqrt(3)

def z(x, y):
    a = 3*(x - S13*y)
    b = 3*S43*y
    c = 3 - a - b
    if a < 0 or b < 0 or c < 0:
        return nan
    z0 = a**(1/3) + b**(1/3) + c**(1/3) - a*b - b*c - a*c
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