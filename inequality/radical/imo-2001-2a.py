from numpy import sqrt
import numpy as np
import matplotlib.pyplot as plt

def z(u, v):
    return sqrt((u + 1)**2/(u**2 + 2*u + 8*v + 9)) + sqrt((v + 1)**2/(8*u + v**2 + 2*v + 9)) + sqrt(1/(8*u*v + 8*u + 8*v + 9)) - 1

def main():
    U, V = np.meshgrid(np.linspace(0.0, 3.0, 300), np.linspace(0.0, 3.0, 300))
    plt.imshow(z(U, V), origin='lower', extent = [0, 3, 0, 3], cmap=plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()