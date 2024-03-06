from math import log, nan, sqrt
import matplotlib.pyplot as plt

def z(u, v):
    a = 4/(1 + u)
    b = (4 - a)/(1 + v)
    c = (4 - a - b)/(1 + a*b)
    if a*b + b*c + a*c == 0:
        return nan
    z0 = 1/sqrt(a**2 + 4*b*c) + 1/sqrt(b**2 + 4*a*c) + 1/sqrt(c**2 + 4*a*b) - 5/4
    return sqrt(log(1 + z0))

def main():
    len = 2
    Z = [[z(j/100, i/100) for j in range(len*100)] for i in range(len*100)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()