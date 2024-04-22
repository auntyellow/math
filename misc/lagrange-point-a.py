from math import nan, sqrt
import matplotlib.pyplot as plt

# https://en.wikipedia.org/wiki/Lagrange_point

R = 1
m = 3e-6

def z(x, y):
    if y == 0 and (x == 0 or x == 1):
        return nan
    V_M = -1/sqrt(x**2 + y**2)
    if V_M < -1000:
        return nan
    V_m = -m/sqrt((x - R)**2 + y**2)
    if V_m < -.001:
        return nan
    V_c = -(x**2 + y**2)/R**3/2
    return V_M + V_m + V_c

def main():
    # L1
    # x0, x1, y0, y1 = .98, 1, -.01, .01
    # L2
    x0, x1, y0, y1 = 1, 1.02, -.01, .01
    # L3, saddle is significant when m > .5
    # x0, x1, y0, y1 = -1.5, -.5, -.5, .5
    # L4, saddle is significant when m > .001
    # x0, x1, y0, y1 = .4, .6, .8, 1
    res = 500
    Z = [[z(x0 + j*(x1 - x0)/res, y0 + i*(y1 - y0)/res) for j in range(res)] for i in range(res)]
    plt.imshow(Z, origin = 'lower', extent = [x0, x1, y0, y1], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()