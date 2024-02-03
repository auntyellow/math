from math import log, sqrt
import matplotlib.pyplot as plt

def z(u, v):
    # f(x=max(xyz))
    z0 = 170172209*u**4 - 1301377672*u**3*v + 640688836*u**3 + 3553788598*u**2*v**2 - 3203444180*u**2*v + 640688836*u**2 - 3864133016*u*v**3 + 4484821852*u*v**2 - 1281377672*u*v + 1611722090*v**4 - 961033254*v**3 + 2082238717*v**2
    # f(y=max(xyz))
    # z0 = 2572755344*u**4 - 6426888360*u**3*v - 3844133016*u**3 + 5315682897*u**2*v**2 + 8649299286*u**2*v + 1441549881*u**2 - 1621722090*u*v**3 - 5766199524*u*v**2 - 2883099762*u*v + 1611722090*v**4 - 961033254*v**3 + 2082238717*v**2
    # f(z=max(xyz))
    # z0 = 2572755344*u**4 - 20000000*u**3*v - 3844133016*u**3 + 30000000*u**2*v**2 + 1441549881*u**2 - 20000000*u*v**3 + 170172209*v**4 + 640688836*v**3 + 640688836*v**2
    return log(1 + z0)

def main():
    len = 1
    res = 500
    Z = [[z(j/res, i/res) for j in range(len*res)] for i in range(len*res)]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len], cmap = plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()