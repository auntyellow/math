from math import log, sqrt
import matplotlib.pyplot as plt

def z(u, v):
    # f(abc)
    z0 = 6*u**5 + 5*u**4*v + 24*u**4 - 8*u**3*v**2 + 16*u**3*v + 30*u**3 - 9*u**2*v**3 - 18*u**2*v**2 + 21*u**2*v + 12*u**2 - 2*u*v**4 - 10*u*v**3 + 3*u*v**2 + 12*u*v + 6*v**3 + 12*v**2
    return -log(1 - z0) - .1 if z0 < 0 else log(1 + z0) + .1

def main():
    len = 4
    res = 100
    Z = [[z(j/res, i/res) for j in range(len*res)] for i in range(len*res)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()