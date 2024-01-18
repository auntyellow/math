import numpy as np
import matplotlib.pyplot as plt

def z(u, v):
    # result from Han23P341.java, depth = 12
    zs = [
        69*u**3*v**3 + 139*u**3*v**2 + 70*u**3*v + 139*u**2*v**3 - 196*u**2*v**2 - 276*u**2*v + 68*u**2 + 70*u*v**3 - 276*u*v**2 - 218*u*v + 137*u + 68*v**2 + 137*v + 69,
        1983*u**3*v**3 + 4024*u**3*v**2 + 2041*u**3*v + 4024*u**2*v**3 - 5316*u**2*v**2 - 7927*u**2*v + 1926*u**2 + 2041*u*v**3 - 7927*u*v**2 - 6581*u*v + 3909*u + 1926*v**2 + 3909*v + 1983,
        30383*u**3*v**3 + 62111*u**3*v**2 + 31728*u**3*v + 62111*u**2*v**3 - 76584*u**2*v**2 - 121302*u**2*v + 29084*u**2 + 31728*u*v**3 - 121302*u*v**2 - 105668*u*v + 59467*u + 29084*v**2 + 59467*v + 30383,
        69*u**3*v**3 + 137*u**3*v**2 + 68*u**3*v + 137*u**2*v**3 - 218*u**2*v**2 - 276*u**2*v + 70*u**2 + 68*u*v**3 - 276*u*v**2 - 196*u*v + 139*u + 70*v**2 + 139*v + 69,
        1983*u**3*v**3 + 3909*u**3*v**2 + 1926*u**3*v + 3909*u**2*v**3 - 6581*u**2*v**2 - 7927*u**2*v + 2041*u**2 + 1926*u*v**3 - 7927*u*v**2 - 5316*u*v + 4024*u + 2041*v**2 + 4024*v + 1983,
        30383*u**3*v**3 + 59467*u**3*v**2 + 29084*u**3*v + 59467*u**2*v**3 - 105668*u**2*v**2 - 121302*u**2*v + 31728*u**2 + 29084*u*v**3 - 121302*u*v**2 - 76584*u*v + 62111*u + 31728*v**2 + 62111*v + 30383,
    ]
    z1 = 0
    for z0 in zs:
        if z0 < 0:
            return -10
        z1 += z0
    return np.log(z1 + 1)

def main():
    len = 2
    Z = [[z(j/100, i/100) for j in range(len*100)] for i in range(len*100)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()