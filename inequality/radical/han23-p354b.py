from math import sqrt
import matplotlib.pyplot as plt

def z(u, v):
    x, y = 2/(1 + u) - 1, 2/(1 + v) - 1
    U, V = sqrt(u), sqrt(v)
    UV = 4*U*V/(u + 1)/(v + 1)
    return x*y + UV

def main():
    len = 10
    Z = [[z(j/100, i/100) for j in range(len*100)] for i in range(len*100)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()