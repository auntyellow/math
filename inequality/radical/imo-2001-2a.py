from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def z(u, v):
    # return sqrt((u + 1)**2/(u**2 + 2*u + 8*v + 9)) + sqrt((v + 1)**2/(8*u + v**2 + 2*v + 9)) + sqrt(1/(8*u*v + 8*u + 8*v + 9)) - 1
    # f(1/u,v)
    # return sqrt(u/(8*u*v + 9*u + 8*v + 8)) + sqrt((u + 1)**2/(8*u**2*v + 9*u**2 + 2*u + 1)) + sqrt(u*(v + 1)**2/(u*v**2 + 2*u*v + 9*u + 8)) - 1
    # f(u,1/v)
    # return sqrt(v/(8*u*v + 8*u + 9*v + 8)) + sqrt((v + 1)**2/(8*u*v**2 + 9*v**2 + 2*v + 1)) + sqrt(v*(u + 1)**2/(u**2*v + 2*u*v + 9*v + 8)) - 1
    # f(1/u,1/v)
    if u == 0 and v == 0:
        return sqrt(u*v/(9*u*v + 8*u + 8*v + 8)) + 1
    return sqrt(u*v/(9*u*v + 8*u + 8*v + 8)) + sqrt(u*(v + 1)**2/(9*u*v**2 + 2*u*v + u + 8*v**2)) + sqrt(v*(u + 1)**2/(9*u**2*v + 8*u**2 + 2*u*v + v)) - 1

def main():
    len = 2
    Z = [[z(j/100, i/100) for j in range(len*100)] for i in range(len*100)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()