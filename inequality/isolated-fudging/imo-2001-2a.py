from math import nan, sqrt
import matplotlib.pyplot as plt

S13 = 1/sqrt(3)
S43 = 2/sqrt(3)

def z(x, y):
    a = x - S13*y
    b = S43*y
    c = 1 - a - b
    if a < 0 or b < 0 or c < 0 or a*b + a*c + b*c == 0:
        return nan
    if b > a and b > c:
        z0 = a/sqrt(a**2 + 8*b*c) + b/sqrt(b**2 + 8*a*c) + c/sqrt(c**2 + 8*a*b) - 1
        return sqrt(z0)
    m0, m2 = min(a, b, c), max(a, b, c)
    m1 = 1 - m0 - m2
    f2 = a**2/(a**2 + 8*b*c)
    if m2 < 5.5*m0:
        n, m = 1, -1/11
        g = n*a + m*(b + c)
        h = (n + 2*m)*(a + b + c)
        z0 = f2 - (g/h)**2
        return sqrt(z0)
    if 6*m1 < m2:
        n, m = 1, 0
        g = n*a + m*(b + c)
        h = (n + 2*m)*(a + b + c)
        z0 = f2 - (g/h)**2
        return sqrt(z0)
    z0 = a/sqrt(a**2 + 8*b*c) + b/sqrt(b**2 + 8*a*c) + c/sqrt(c**2 + 8*a*b) - 1
    return sqrt(z0)

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
    Z = [[z(j/res, i/res) for j in range(len*res)] for i in range(round(len*res*aspect))]
    plt.imshow(Z, origin = 'lower', extent = [0, len, 0, len*aspect], cmap = plt.cm.hsv)
    oo = 1e+10
    P00, P0O = xyz(0, 0), xyz(0, oo)
    plot((P0O[1], P0O[2]), (P00[0], P00[1]), (P0O[2], P0O[0]))
    plot((P0O[0], P0O[1]), (P00[0], P00[1]))
    P04, P5O, P45 = xyz(0, 4.5), xyz(5, oo), xyz(4.5, 5)
    plot((P5O[0], P5O[1]), (P45[1], P45[0]), (P04[0], P04[1]), (P45[2], P45[0]), (P5O[2], P5O[1]))
    plot((P5O[2], P5O[0]), (P45[2], P45[1]), (P04[0], P04[2]))
    plot((P5O[1], P5O[0]), (P45[0], P45[1]), (P04[1], P04[0]))
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()