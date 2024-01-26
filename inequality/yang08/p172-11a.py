from math import log, sqrt
import matplotlib.pyplot as plt

def z(u, v):
    # h1
    z0 = 170172209*u**2*v**4 + 60000000*u**2*v**3 - 170344418*u**2*v**2 + 180000000*u**2*v + 410344418*u**2 - 640688836*u*v**3 - 640688836*u*v**2 + 640688836*u*v - 320344418*u + 640688836*v**2 + 1281377672*v + 2082238717
    return log(1 + z0)

def main():
    len = 1
    res = 500
    Z = [[z(j/res, i/res) for j in range(len*res)] for i in range(len*res)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()