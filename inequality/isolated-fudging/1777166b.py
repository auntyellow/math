from math import nan, sqrt
import matplotlib.pyplot as plt

S13 = 1/sqrt(3)
S43 = 2/sqrt(3)

def z(x, y):
    a = x - S13*y
    b = S43*y
    c = 1 - a - b
    if a < 0 or b < 0 or c < 0 or a*b + a*c + b*c == 0:
        return nan
    x1 = 2*a/sqrt((a + b)*(a + c))
    y1 = 2*b/sqrt((b + c)*(b + a))
    z1 = 2*c/sqrt((c + a)*(c + b))
    z0 = x1**(8/5) + y1**(8/5) + z1**(8/5) - 3
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