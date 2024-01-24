from math import log, sqrt
import matplotlib.pyplot as plt

m, n = 121, 315

def z(u, v):
    # f(xyz) about u, v
    z0 = m**2*u**7 + 5*m**2*u**6*v + 7*m**2*u**6 + 10*m**2*u**5*v**2 + 30*m**2*u**5*v + 20*m**2*u**5 + 10*m**2*u**4*v**3 + 50*m**2*u**4*v**2 + 70*m**2*u**4*v + 29*m**2*u**4 + 5*m**2*u**3*v**4 + 40*m**2*u**3*v**3 + 96*m**2*u**3*v**2 + 78*m**2*u**3*v + 21*m**2*u**3 + m**2*u**2*v**5 + 15*m**2*u**2*v**4 + 59*m**2*u**2*v**3 + 87*m**2*u**2*v**2 + 39*m**2*u**2*v + 6*m**2*u**2 + 2*m**2*u*v**5 + 15*m**2*u*v**4 + 38*m**2*u*v**3 + 36*m**2*u*v**2 + 6*m**2*u*v + m**2*v**5 + 5*m**2*v**4 + 9*m**2*v**3 + 6*m**2*v**2 + m*n*u**7 + m*n*u**6*v + 6*m*n*u**6 - 2*m*n*u**5*v**2 + 2*m*n*u**5*v + 15*m*n*u**5 - 3*m*n*u**4*v**3 - 16*m*n*u**4*v**2 - m*n*u**4*v + 20*m*n*u**4 - m*n*u**3*v**4 - 16*m*n*u**3*v**3 - 34*m*n*u**3*v**2 + 14*m*n*u**3 - 4*m*n*u**2*v**4 - 20*m*n*u**2*v**3 - 20*m*n*u**2*v**2 + 6*m*n*u**2*v + 4*m*n*u**2 + 4*m*n*u*v**2 + 4*m*n*u*v + m*n*v**5 + 4*m*n*v**4 + 6*m*n*v**3 + 4*m*n*v**2 - n**2*u**6 - 2*n**2*u**5*v - 5*n**2*u**5 - n**2*u**4*v**2 - 9*n**2*u**4*v - 9*n**2*u**4 - 6*n**2*u**3*v**2 - 14*n**2*u**3*v - 7*n**2*u**3 - 3*n**2*u**2*v**3 - 11*n**2*u**2*v**2 - 9*n**2*u**2*v - 2*n**2*u**2 - n**2*u*v**4 - 6*n**2*u*v**3 - 8*n**2*u*v**2 - 2*n**2*u*v - n**2*v**4 - 3*n**2*v**3 - 2*n**2*v**2
    return -log(1 - z0) if z0 < 0 else log(1 + z0)

def main():
    len = 1
    Z = [[z(j/100, i/100) for j in range(len*100)] for i in range(len*100)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()