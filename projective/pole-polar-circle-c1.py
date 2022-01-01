from cartesian import *

def cross_ratio(a, b, c, d):
    return cancel((a - c)*(b - d)/(a - d)/(b - c))

def main():
    # https://imomath.com/index.cgi?page=polePolarBrianchonBrokard (Theorem 7)
    # A and B are conjugated => (A,B;C,D)=-1
    a, b, x, y = symbols('a, b, x, y')
    A, B = (0, 1/a), (b, a)
    AB = line(A, B)
    circle = Eq(x**2 + y**2, 1)
    roots = solve([AB, circle], (x, y))
    C, D = roots[0], roots[1]
    print('(A,B;C,D) =', cross_ratio(A[0], B[0], C[0], D[0]))

if __name__ == '__main__':
    main()