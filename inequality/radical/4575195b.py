from math import log, nan, sqrt
import matplotlib.pyplot as plt

S13 = 1/sqrt(3)
S43 = 2/sqrt(3)
D = 3*sqrt(5)/2

def w(u, v):
    x = u - S13*v
    y = S43*v
    z = 1 - x - y
    if x < 0 or y < 0 or z < 0 or x*y + x*z + y*z == 0:
        return nan
    w0 = sqrt((4*x**2 + y**2)/(3*x**2 + y*z)) + sqrt((4*y**2 + z**2)/(3*y**2 + x*z)) + sqrt((4*z**2 + x**2)/(3*z**2 + x*y)) - D
    w0 = sqrt(log(1 + w0))
    '''
    # mark the case u < 5 in 4575195u.py
    m0, m2 = min(x, y, z), max(x, y, z)
    m1 = 1 - m0 - m2
    if m2 < 6*m0: # and m2 < 6*m1
        return -w0
    if 24*m1 < m2: # and 24*m0 < m2:
        return -w0
    '''
    return w0

def xyz(u, v):
    u1, v1 = 1/(u + 1), 1/(v + 1)
    z = 1/(1 + u1 + v1)
    x, y = u1*z, v1*z
    return x, y, z

def add_point(Px, Py, x, y):
    Px.append(x + y/2)
    Py.append(y/S43)

def plot(*P_n):
    Px, Py = [], []
    for P in P_n:
        add_point(Px, Py, P[0], P[1])
    plt.plot(Px, Py, linewidth = .5, color = 'black')    

def main():
    len = 1
    res = 500
    aspect = .87
    W = [[w(j/res, i/res) for j in range(len*res)] for i in range(round(len*res*aspect))]
    plt.imshow(W, origin = 'lower', extent = [0, len, 0, len*aspect], cmap = plt.cm.hsv)
    oo = 1e+10
    P00, P0O = xyz(0, 0), xyz(0, oo)
    plot((P0O[1], P0O[2]), (P00[0], P00[1]), (P0O[0], P0O[1]))
    P05, P23, P5_23 = xyz(0, 5), xyz(23, oo), xyz(5, 23)
    plot((P05[0], P05[1]), (P5_23[1], P5_23[0]), (P23[0], P23[1]))
    plot((P05[1], P05[0]), (P5_23[0], P5_23[1]), (P23[1], P23[0]))
    P12 = xyz(12, oo)
    plot((P12[0], P12[1]), (P12[1], P12[0]))
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()