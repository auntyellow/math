from numpy import sqrt
import numpy as np
import matplotlib.pyplot as plt

def s(x):
    # return sqrt(x)
    # result from sqrt-quadratic-a.py
    return -x**2/2 + 3*x/2

def z(u, v):
    return s((u + 1)**2/(u**2 + 2*u + 8*v + 9)) + s((v + 1)**2/(8*u + v**2 + 2*v + 9)) + s(1/(8*u*v + 8*u + 8*v + 9)) - 1

def main():
    U, V = np.meshgrid(np.linspace(0.0, 20.0, 2000), np.linspace(0.0, 20.0, 2000))
    plt.imshow(z(U, V), origin='lower', extent = [0, 20, 0, 20], cmap=plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()