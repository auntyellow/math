from math import sqrt
import matplotlib.pyplot as plt

def z(x, y):
    # (4*x - 3*y)**2 + 1, x -> 1/x, y -> 1/y, f(x = max(xy))
    # z0 = x**2*y**2 + 16*y**2 - 24*y + 9
    # (5*x - 3*y)**2 + 1, x -> 1/x, y -> 1/y, f(x = max(xy))
    # z0 = x**2*y**2 + 25*y**2 - 30*y + 9
    # (x - y)*(2*x - y) + 1/4, y -> 1/y
    # z0 = 2*x**2*y**2 - 3*x*y + 1/4*y**2 + 1
    # (3*x**2 - 5*y)**2 + 1, x -> 1/x, y -> 1/y, f(x = max(xy)), again
    z0 = x**4*y**4 + 25*x**2 - 30*x + 9
    return sqrt(z0)

def main():
    len = 1
    res = 200
    Z = [[z(j/res, i/res) for j in range(len*res)] for i in range(round(len*res))]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()