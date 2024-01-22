from sympy import *

def main():
    m, n, x, y, z = symbols('m, n, x, y, z', negative = False)
    # for all x, y, z >= 0 and z >= m*x and z >= m*y, find m to keep x1, y1, z1 >= 0 while
    # x, y, z = x1/n, y1/n, z1 + x1*(n - 1)/n + y1*(n - 1)/n
    A = Matrix([[1/n, 0, 0], [0, 1/n, 0], [(n - 1)/n, (n - 1)/n, 1]]).inv()
    print('A =', A)
    X1 = A*Matrix([[x], [y], [z]])
    x1, y1, z1 = X1[0, 0], X1[1, 0], X1[2, 0]
    print('x1 =', x1, '>= 0')
    print('y1 =', y1, '>= 0')
    print('z1 =', z1, '>=', factor(z1.subs(x, z/m).subs(y, z/m)), '>= 0')
    # m >= 2*n - 2 can guarantee z1 >= 0
    # show that m < 2*n - 2 doesn't work:
    e = symbols('ε', positive = True)
    m = 2*n - 2 - e
    y = x
    z = m*y
    X1 = A*Matrix([[x], [y], [z]])
    x1, y1, z1 = X1[0, 0], X1[1, 0], X1[2, 0]
    print('z1(m = 2*n - 2 - ε) =', factor(z1))

if __name__ == '__main__':
    main()