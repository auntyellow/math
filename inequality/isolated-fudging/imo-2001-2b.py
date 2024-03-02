from math import nan, sqrt
import matplotlib.pyplot as plt

S13 = 1/sqrt(3)
S43 = 2/sqrt(3)

def z(x, y):
    a = x - S13*y
    b = S43*y
    c = 1 - a - b
    if a < 0 or b < 0 or c < 0 or a*b + a*c + b*c == 0:
        return nan
    f2 = a**2/(a**2 + 8*b*c)
    m, n, p, q = 0, 1, 2/5, 0
    g = n*a**2 + m*(b**2 + c**2) + p*(a*b + a*c) + q*b*c
    h = (n + 2*m)*(a**2 + b**2 + c**2) + (2*p + q)*(a*b + a*c + b*c)
    z0 = f2 - (g/h)**2
    return sqrt(z0)

def main():
    len = 1
    res = 500
    aspect = .87
    Z = [[z(j/res, i/res) for j in range(len*res)] for i in range(round(len*res*aspect))]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len*aspect], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()