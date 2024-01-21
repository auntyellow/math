from sympy import *

def main():
    m, n, x, y, z = symbols('m, n, x, y, z', negative = False)
    # for all x, y, z >= 0 and z >= m*x and z >= m*y, exists x1, y1, z1 >= 0:
    # x, y, z = x1/n, y1/n, z1 + x1*(n - 1)/n + y1*(n - 1)/n
    A = Matrix([[1/n, 0, 0], [0, 1/n, 0], [(n - 1)/n, (n - 1)/n, 1]]).inv()
    z1 = (A*Matrix([[x], [y], [z]]))[2, 0]
    # TODO >= or <= ?
    print('z1 =', z1, '>=', factor(z1.subs(x, z/m).subs(y, z/m)))
    # m >= 2*n - 2

if __name__ == '__main__':
    main()