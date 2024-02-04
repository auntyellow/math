from math import log, nan, sqrt
import matplotlib.pyplot as plt

S13 = 1/sqrt(3)
S43 = 2/sqrt(3)
D = 3*sqrt(5)/2

def w(u, v):
    x = u - S13*v
    y = S43*v
    z = 1 - x - y
    if x < 0 or y < 0 or z < 0:
        return nan
    # (4*x - 3*y)**2 + 1
    # w0 = 16*x**2 - 24*x*y + 9*y**2 + z**2
    # (5*x - 4*y)**2 + x
    # w0 = 25*x**2 - 40*x*y + x*z + 16*y**2
    # (x**2 - y)**2 + 1
    w0 = x**4 - 2*x**2*y*z + y**2*z**2 + z**4
    return w0**.2

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