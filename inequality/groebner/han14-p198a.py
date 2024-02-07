from math import log
import matplotlib.pyplot as plt

# ISBN 9787560349800, p198, ex 7.30

def z(u, v):
    z0 = 64*u**6 + 192*u**5*v + 576*u**5 + 240*u**4*v**2 - 288*u**4*v + 2160*u**4 + 160*u**3*v**3 - 2016*u**3*v**2 + 864*u**3*v + 4320*u**3 + 60*u**2*v**4 - 1008*u**2*v**3 - 1944*u**2*v**2 + 4752*u**2*v + 4860*u**2 + 12*u*v**5 + 180*u*v**4 - 648*u*v**3 + 1512*u*v**2 + 4860*u*v + 2916*u + v**6 + 18*v**5 + 135*v**4 + 540*v**3 + 1215*v**2 + 1458*v + 729
    return log(1 + z0)

def main():
    len = 20
    res = 20
    Z = [[z(j/res, i/res) for j in range(len*res)] for i in range(len*res)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()