from math import sqrt
import matplotlib.pyplot as plt

def s(t):
    # return sqrt(t)
    # result from sqrt-quadratic.py
    return -t**2/2 + 3*t/2

def z(u, v):
    return s((u + 1)**2/(u**2 + 2*u + 8*v + 9)) + s((v + 1)**2/(8*u + v**2 + 2*v + 9)) + s(1/(8*u*v + 8*u + 8*v + 9)) - 1

def main():
    len = 15
    Z = [[z(j/100, i/100) for j in range(len*100)] for i in range(len*100)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()