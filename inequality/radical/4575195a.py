from math import sqrt
import matplotlib.pyplot as plt

def z(u, v):
    z0 = sqrt((u**2 + 2*u + 5)/(u*v + u + v + 4)) + sqrt((4*v**2 + 8*v + 5)/(u + 3*v**2 + 6*v + 4)) + sqrt((4*u**2 + 8*u + v**2 + 2*v + 5)/(3*u**2 + 6*u + v + 4)) - 3*sqrt(5)/2
    '''
    # f(1/u,v)
    z0 = 0 if u == 0 else sqrt((u**2*v**2 + 2*u**2*v + 5*u**2 + 8*u + 4)/(u**2*v + 4*u**2 + 6*u + 3)) + sqrt((5*u**2 + 2*u + 1)/(u*(u*v + 4*u + v + 1))) + sqrt(u*(4*v**2 + 8*v + 5)/(3*u*v**2 + 6*u*v + 4*u + 1)) - 3*sqrt(5)/2
    # f(u,1/v)
    z0 = 0 if v == 0 else sqrt((5*v**2 + 8*v + 4)/(u*v**2 + 4*v**2 + 6*v + 3)) + sqrt((4*u**2*v**2 + 8*u*v**2 + 5*v**2 + 2*v + 1)/(v*(3*u**2*v + 6*u*v + 4*v + 1))) + sqrt(v*(u**2 + 2*u + 5)/(u*v + u + 4*v + 1)) - 3*sqrt(5)/2
    # f(1/u,1/v)
    z0 = 0 if u == 0 or v == 0 else sqrt(u*(5*v**2 + 8*v + 4)/(4*u*v**2 + 6*u*v + 3*u + v**2)) + sqrt((5*u**2*v**2 + 2*u**2*v + u**2 + 8*u*v**2 + 4*v**2)/(v*(4*u**2*v + u**2 + 6*u*v + 3*v))) + sqrt(v*(5*u**2 + 2*u + 1)/(u*(4*u*v + u + v + 1))) - 3*sqrt(5)/2
    '''
    # show value near 0 clearly
    return -sqrt(-z0) if z0 < 0 else sqrt(z0)

def main():
    len = 6
    Z = [[z(j/100, i/100) for j in range(len*100)] for i in range(len*100)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()