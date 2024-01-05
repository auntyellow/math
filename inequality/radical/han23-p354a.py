from sympy import *

def main():
    # 0 <= x, y <= 1, prove: x*y + sqrt((1 - x**2)*(1 - y**2)) <= 1
    x, y = symbols('x, y', negative = False)
    # A = x*y - 1, B = sqrt((1 - x**2)*(1 - y**2))
    # A**2 - B**2 >= 0 and A + B >= 0 -> A - B >= 0
    f = (1 - x*y)**2 - (1 - x**2)*(1 - y**2)
    print('f =', factor(f))
    # analogously, -1 <= x <= 0 <= y <= 1 -> x*y - sqrt((1 - x**2)*(1 - y**2) >= -1

if __name__ == '__main__':
    main()