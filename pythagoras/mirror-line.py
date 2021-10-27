from cartesian import *

def main():
    x1, x2, y1, y2, x, y = symbols('x1, x2, y1, y2, x, y')
    H = intersect(Eq(x*y2, y*x2), Eq(x2*(x - x1) + y2*(y - y1), 0))
    slope = fraction(cancel((2*H[1] - y1)/(2*H[0] - x1)))
    print('x =', slope[1])
    print('y =', slope[0])
    a, b = y1/x1, y2/x2
    b2 = 2*b/(1 - b**2)
    slope = fraction(cancel((b2 - a)/(1 + b2*a)))
    print('x =', slope[1])
    print('y =', slope[0])

if __name__ == '__main__':
    main()