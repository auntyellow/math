from sympy import *

# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Heron's_method

def main():
    r = symbols('r', negative = False)
    s = 2*sqrt(r)
    for i in range(3):
        s = (s + r/s)/2
    print('s =', s)
    error = factor((s**2 - r)/r)
    print('error =', 1.0/error)

if __name__ == '__main__':
    main()