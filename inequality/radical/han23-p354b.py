from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def z(u, v):
    x, y = 2/(1 + u) - 1, 2/(1 + v) - 1
    U, V = sqrt(u), sqrt(v)
    UV = 4*U*V/(u + 1)/(v + 1)
    return x*y + UV

def main():
    Z = [[z(i/100, j/100) for j in range(1000)] for i in range(1000)]
    plt.imshow(Z, origin='lower', extent = [0, 10, 0, 10], cmap=plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()