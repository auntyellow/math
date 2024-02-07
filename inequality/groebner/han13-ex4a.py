from math import log
import matplotlib.pyplot as plt

def z(u, v):
    # g
    # z0 = u**4 - u**3*v + u**3 - u**2*v**2 - 3*u**2*v + u**2 + u*v**3 - 2*u*v**2 + u*v + v**4 + v**3 + v**2
    # g(uv)
    # z0 = u**2*v**4 + 5*u**2*v**3 + 8*u**2*v**2 + 4*u**2*v + u**2 + u*v**3 + u*v**2 - 4*u*v - 3*u + v**2 + 3*v + 3
    # g(vu)
    z0 = u**4*v**2 + 3*u**3*v**2 + u**3*v + 2*u**2*v**2 + u**2 - 5*u*v + 3*u + v**2 - 3*v + 3
    return log(1 + z0)

def main():
    len = 3
    res = 200
    Z = [[z(j/res, i/res) for j in range(len*res)] for i in range(len*res)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()