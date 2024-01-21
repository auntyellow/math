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
    w0 = sqrt((x**2/100 + 4*(9*x/10 + 9*y/10 + z)**2)/(x*y/100 + 3*(9*x/10 + 9*y/10 + z)**2)) + sqrt((x**2/25 + y**2/100)/(3*x**2/100 + y*(9*x/10 + 9*y/10 + z)/10)) + sqrt((y**2/25 + (9*x/10 + 9*y/10 + z)**2)/(x*(9*x/10 + 9*y/10 + z)/10 + 3*y**2/100)) - 3*sqrt(5)/2
    w0 = sqrt(log(1 + w0))
    return w0

def main():
    len = 1
    res = 500
    W = [[w(j/res, i/res) for j in range(len*res)] for i in range(len*res)]
    plt.imshow(W, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()