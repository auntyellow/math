from math import nan, sqrt
import matplotlib.pyplot as plt

# https://en.wikipedia.org/wiki/Lagrange_point

R = 1
m = 3e-6

# TODO: show local minimum

def z(x, y):
    if y == 0 and (x == 0 or x == 1):
        return nan
    V_M = 1/sqrt(x**2 + y**2)
    if V_M > 100:
        return nan
    V_m = m/sqrt((x - R)**2 + y**2)
    if V_m > 10:
        return nan
    V_c = (x**2 + y**2)/R**3/2
    return sqrt(V_M + V_m + V_c)

def main():
    len = 1.1
    res = 500
    Z = [[z(j/res, i/res) for j in range(round(len*res))] for i in range(round(len*res))]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()