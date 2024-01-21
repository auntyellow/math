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
    w0 = sqrt((x**2/169 + 4*(12*x/13 + 12*y/13 + z)**2)/(x*y/169 + 3*(12*x/13 + 12*y/13 + z)**2)) + sqrt((4*x**2/169 + y**2/169)/(3*x**2/169 + y*(12*x/13 + 12*y/13 + z)/13)) + sqrt((4*y**2/169 + (12*x/13 + 12*y/13 + z)**2)/(x*(12*x/13 + 12*y/13 + z)/13 + 3*y**2/169)) - D
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