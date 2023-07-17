import numpy as np
import matplotlib.pyplot as plt

def z(u, v):
    z0 = 90*u**7 + 190*u**6*v + 396*u**6 + 120*u**5*v**2 + 542*u**5*v + 630*u**5 + 55*u**4*v**3 + 41*u**4*v**2 + 164*u**4*v + 504*u**4 + 60*u**3*v**4 - 40*u**3*v**3 - 824*u**3*v**2 - 416*u**3*v + 252*u**3 + 25*u**2*v**5 + 115*u**2*v**4 - 332*u**2*v**3 - 984*u**2*v**2 - 156*u**2*v + 72*u**2 + 50*u*v**5 + 206*u*v**4 - 64*u*v**3 - 192*u*v**2 + 72*u*v + 90*v**5 + 216*v**4 + 108*v**3 + 72*v**2
    # intermediate step for sum_cyc(x**3/(8*x**2 + 3*y**2)) - (x + y + z)/11
    # z0 = 33*u**7 + 69*u**6*v + 143*u**6 + 42*u**5*v**2 + 190*u**5*v + 220*u**5 + 18*u**4*v**3 + 2*u**4*v**2 + 30*u**4*v + 165*u**4 + 21*u**3*v**4 - 24*u**3*v**3 - 336*u**3*v**2 - 194*u**3*v + 77*u**3 + 9*u**2*v**5 + 39*u**2*v**4 - 141*u**2*v**3 - 401*u**2*v**2 - 81*u**2*v + 22*u**2 + 18*u*v**5 + 71*u*v**4 - 42*u*v**3 - 92*u*v**2 + 22*u*v + 33*v**5 + 77*v**4 + 33*v**3 + 22*v**2
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