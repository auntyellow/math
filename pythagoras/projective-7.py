from sympy import symbols
from homogeneous import *

def main():
    # https://imomath.com/index.cgi?page=problemsInProjectiveGeometry (Problem 7)
    m = symbols('m')
    A = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]
    M = (1, m, 0)
    print(f'M_{{0}} = {M}')
    for i in range(12):
        M = cross(cross(A[(i + 1) % 4], A[(i + 2) % 4]), cross(A[(i + 3) % 4], M))
        print(f'M_{{{i + 1}}} = {M}')

if __name__ == '__main__':
    main()