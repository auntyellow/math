from numpy import sqrt
import matplotlib.pyplot as plt

def s(x):
    return sqrt(x)
    # result from sqrt-quadratic-a.py
    # return -x**2/2 + 3*x/2

def z(u, v):
    z0 = s((u**2 + 2*u + 5)/(u*v + u + v + 4)) + s((4*v**2 + 8*v + 5)/(u + 3*v**2 + 6*v + 4)) + s((4*u**2 + 8*u + v**2 + 2*v + 5)/(3*u**2 + 6*u + v + 4)) - 3*sqrt(5)/2
    # show value near 0 clearly
    return sqrt(z0)

def main():
    len = 10
    Z = [[z(j/100, i/100) for j in range(len*100)] for i in range(len*100)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()