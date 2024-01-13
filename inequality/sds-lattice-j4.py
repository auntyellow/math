from math import *
from matplotlib import pyplot

SIMPLICES_J4 = [
    [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]],
    [[0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0]],
    [[0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1], [1, 1, 0, 0]],
    [[0, 0, 1, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0]],
    [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0]],
]

SIN_30 = .5
COS_30 = sqrt(3)/2
COS_35 = sqrt(2/3)
SQRT_12 = sqrt(3)/4

def transform(vertex):
    one = vertex[0] + vertex[1] + vertex[2] + vertex[3]
    x, y, z = vertex[0]/one, vertex[1]/one, vertex[3]/one
    return x + y*SIN_30 + z*SQRT_12, y*COS_30 + z*SIN_30, z*COS_35

def main():
    colors = ['black', 'blue', 'red', 'green', 'orange']
    fig = pyplot.figure()
    ax = fig.add_subplot(projection = '3d')
    for i in range(0, 5):
        simplex = SIMPLICES_J4[i]
        x0, y0, z0 = transform(simplex[0])
        x1, y1, z1 = transform(simplex[1])
        x2, y2, z2 = transform(simplex[2])
        x3, y3, z3 = transform(simplex[3])
        ax.plot([x0, x1, x2, x3], [y0, y1, y2, y3], [z0, z1, z2, z3], linewidth = .5, color = colors[i])
        ax.plot([x2, x0, x3, x1], [y2, y0, y3, y1], [z2, z0, z3, z1], linewidth = .5, color = colors[i])
    ax.axes.set_xlim3d(-0.01, 1.01)
    ax.axes.set_ylim3d(-0.01, COS_30 + 0.01)
    ax.axes.set_zlim3d(-0.01, COS_35 + 0.01)
    pyplot.show()

if __name__ == '__main__':
    main()