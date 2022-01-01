from cartesian import *

def cross_ratio(a, b, c, d):
    return cancel((a - c)*(b - d)/(a - d)/(b - c))

def main():
    # https://imomath.com/index.cgi?page=polePolarBrianchonBrokard (Theorem 7)
    # (A,B;C,D)=-1 => A(0,a1) and B(b,a) are conjugated, i.e. a1=1/a
    a, b, a1, x, y = symbols('a, b, a1, x, y')
    A, B = (0, a1), (b, a)
    AB = line(A, B)
    circle = Eq(x**2 + y**2, 1)
    roots = solve([AB, circle], (x, y))
    C, D = roots[0], roots[1]
    A = (0, solve(Eq(cross_ratio(A[0], B[0], C[0], D[0]), -1), a1)[0])
    print('A:', A)

if __name__ == '__main__':
    main()