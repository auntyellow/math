from math import log, nan, sqrt
import matplotlib.pyplot as plt

# sum_cyc(sqrt(x/(y + z))) >= 2

S13 = 1/sqrt(3)
S43 = 2/sqrt(3)

def z(x, y):
    a = x - S13*y
    b = S43*y
    c = 1 - a - b
    if a < .05 or b < .05 or c < .05:
        return nan
    z0 = sqrt(a/(b + c)) + sqrt(b/(a + c)) + sqrt(c/(a + b)) - 2
    return sqrt(log(1 + z0))

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