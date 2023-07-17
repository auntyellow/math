import numpy as np
import matplotlib.pyplot as plt

def z(p, q):
    z0 = 90*p**7 + 190*p**6*q + 396*p**6 + 120*p**5*q**2 + 542*p**5*q + 630*p**5 + 55*p**4*q**3 + 41*p**4*q**2 + 164*p**4*q + 504*p**4 + 60*p**3*q**4 - 40*p**3*q**3 - 824*p**3*q**2 - 416*p**3*q + 252*p**3 + 25*p**2*q**5 + 115*p**2*q**4 - 332*p**2*q**3 - 984*p**2*q**2 - 156*p**2*q + 72*p**2 + 50*p*q**5 + 206*p*q**4 - 64*p*q**3 - 192*p*q**2 + 72*p*q + 90*q**5 + 216*q**4 + 108*q**3 + 72*q**2
    # intermediate step for sum_cyc(x**3/(8*x**2 + 3*y**2)) - (x + y + z)/11
    # z0 = 33*p**7 + 69*p**6*q + 143*p**6 + 42*p**5*q**2 + 190*p**5*q + 220*p**5 + 18*p**4*q**3 + 2*p**4*q**2 + 30*p**4*q + 165*p**4 + 21*p**3*q**4 - 24*p**3*q**3 - 336*p**3*q**2 - 194*p**3*q + 77*p**3 + 9*p**2*q**5 + 39*p**2*q**4 - 141*p**2*q**3 - 401*p**2*q**2 - 81*p**2*q + 22*p**2 + 18*p*q**5 + 71*p*q**4 - 42*p*q**3 - 92*p*q**2 + 22*p*q + 33*q**5 + 77*q**4 + 33*q**3 + 22*q**2
    z0[z0 >= 0] = np.log(1 + z0[z0 >= 0])
    z0[z0 < 0] = -np.log(1 - z0[z0 < 0])
    return z0

def main():
    P, Q = np.meshgrid(np.linspace(0.0, 3.0, 300), np.linspace(0.0, 3.0, 300))
    plt.imshow(z(P, Q), origin='lower', extent = [0, 3, 0, 3], cmap=plt.cm.hsv)
    plt.colorbar()
    plt.xlabel('p')
    plt.ylabel('q')
    plt.show()

if __name__ == '__main__':
    main()