from matplotlib import pyplot

RES = 20

def plot(f):
    xx, yy, zz = [], [], []
    for i in range(0, RES + 1):
        for j in range(0, RES + 1):
            for k in range(0, RES + 1):
                x, y, z = f(i/RES, j/RES, k/RES)
                xx.append(x)
                yy.append(y)
                zz.append(z)
    return xx, yy, zz

def main():
    fig = pyplot.figure()
    ax = fig.add_subplot(projection = '3d')
    xx, yy, zz = plot(lambda v, k1, k2: (v, v*k1, v*k2))
    ax.scatter(xx, yy, zz, s = 0.5, marker = '.', color = 'red')
    xx, yy, zz = plot(lambda v, k1, k2: (v*k1, v, v*k2))
    ax.scatter(xx, yy, zz, s = 0.5, marker = '.', color = 'green')
    xx, yy, zz = plot(lambda v, k1, k2: (v*k1, v*k2, v))
    ax.scatter(xx, yy, zz, s = 0.5, marker = '.', color = 'blue')
    ax.axes.set_xlim3d(-0.1, 1.1)
    ax.axes.set_ylim3d(-0.1, 1.1)
    ax.axes.set_zlim3d(-0.1, 1.1)
    pyplot.show()

if __name__ == '__main__':
    main()