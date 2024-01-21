from math import log, nan, sqrt
import matplotlib.pyplot as plt

S13 = 1/sqrt(3)
S43 = 2/sqrt(3)
D = 3*sqrt(5)/2

def w(u, v):
    x = u - S13*v
    y = S43*v
    z = 1 - x - y
    if x < 0 or y < 0 or z < 0 or x*y + x*z + y*z == 0:
        return nan
    w0 = sqrt((4*x**2 + y**2)/(3*x**2 + y*z)) + sqrt((4*y**2 + z**2)/(3*y**2 + x*z)) + sqrt((4*z**2 + x**2)/(3*z**2 + x*y)) - D
    return sqrt(log(1 + w0))

def main():
    len = 1
    res = 500
    W = [[w(j/res, i/res) for j in range(len*res)] for i in range(len*res)]
    plt.imshow(W, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()