import numpy as np
import matplotlib.pyplot as plt

def z(u, v):
    # g(uv)
    z0 = u**2*v**4 + 5*u**2*v**3 + 8*u**2*v**2 + 4*u**2*v + u**2 + u*v**3 + u*v**2 - 4*u*v - 3*u + v**2 + 3*v + 3
    # g(vu)
    z0 = u**4*v**2 + 3*u**3*v**2 + u**3*v + 2*u**2*v**2 + u**2 - 5*u*v + 3*u + v**2 - 3*v + 3
    z0[z0 >= 0] = np.log(1 + z0[z0 >= 0])
    z0[z0 < 0] = -np.log(1 - z0[z0 < 0])
    return z0

def main():
    U, V = np.meshgrid(np.linspace(0.0, 3.0, 300), np.linspace(0.0, 3.0, 300))
    plt.imshow(z(U, V), origin='lower', extent = [0, 3, 0, 3], cmap=plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()