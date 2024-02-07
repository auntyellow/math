from math import log, nan, sqrt
import matplotlib.pyplot as plt

S13 = 1/sqrt(3)
S43 = 2/sqrt(3)
D = 3*sqrt(5)/2
m, n = 121, 315
max = 1/n - 1/(n + m)

def w(u, v):
    x = u - S13*v
    y = S43*v
    z = 1 - x - y
    if x < 0 or y < 0 or z < 0 or x*y + x*z + y*z == 0:
        return nan
    w0 = x**3/(n*x**2 + m*y**2) + y**3/(n*y**2 + m*z**2) + z**3/(n*z**2 + m*x**2) - (x + y + z)/(n + m)
    if w0 < 0:
        return -.1 - sqrt(-w0/max)
    return sqrt(w0/max)

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