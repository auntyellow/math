from math import log, nan, sqrt
import matplotlib.pyplot as plt

# sum_cyc(sqrt(x/(y + z))) >= 2

S13 = 1/sqrt(3)
S43 = 2/sqrt(3)

def w(u, v):
    x = u - S13*v
    y = S43*v
    z = 1 - x - y
    if x < 0 or y < 0 or z < 0 or x*y + x*z + y*z < .02:
        return nan
    w0 = sqrt(x/(y + z)) + sqrt(y/(x + z)) + sqrt(z/(x + y)) - 2
    return sqrt(log(1 + w0))

def main():
    len = 1
    res = 500
    aspect = .87
    W = [[w(j/res, i/res) for j in range(len*res)] for i in range(round(len*res*aspect))]
    plt.imshow(W, origin = 'lower', extent = [0, len, 0, len*aspect], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()