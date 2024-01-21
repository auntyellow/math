from math import log, sqrt
import matplotlib.pyplot as plt

def z(u, v):
    # f(z=max)
    z0 = sqrt((u + 1)*(v**2 + 2*v + 5)/(3*u + v**2 + 2*v + 4)) + sqrt((u**2 + 2*u + 4*v**2 + 8*v + 5)/((v + 1)*(u**2 + 2*u + 3*v + 4))) + sqrt((v + 1)*(4*u**2 + 8*u + 5)/((u + 1)*(3*u*v + 3*u + 3*v + 4))) - 3*sqrt(5)/2
    # show value near 0 clearly
    return sqrt(log(1 + z0))

def main():
    len = 6
    Z = [[z(j/100, i/100) for j in range(len*100)] for i in range(len*100)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()