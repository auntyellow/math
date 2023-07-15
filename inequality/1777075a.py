import numpy as np
import matplotlib.pyplot as plt

def z(p, q):
    return np.log(1 + 90*p**7 + 190*p**6*q + 396*p**6 + 120*p**5*q**2 + 542*p**5*q + 630*p**5 + 55*p**4*q**3 + 41*p**4*q**2 + 164*p**4*q + 504*p**4 + 60*p**3*q**4 - 40*p**3*q**3 - 824*p**3*q**2 - 416*p**3*q + 252*p**3 + 25*p**2*q**5 + 115*p**2*q**4 - 332*p**2*q**3 - 984*p**2*q**2 - 156*p**2*q + 72*p**2 + 50*p*q**5 + 206*p*q**4 - 64*p*q**3 - 192*p*q**2 + 72*p*q + 90*q**5 + 216*q**4 + 108*q**3 + 72*q**2)

def main():
    x, y = np.linspace(0.0, 3.0, 300), np.linspace(0.0, 3.0, 300)
    X, Y = np.meshgrid(x, y)
    plt.imshow(z(X, Y), origin='lower', extent = [0, 3, 0, 3], cmap=plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()