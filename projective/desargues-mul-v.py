from sympy import symbols
from homogeneous import *

def main():
    # This program shows the definition of multiplication
    # see ISBN 9787040537550 §10.2, Figure 10-6
    a, b = symbols('a, b')
    # desargues.md, trick 2c
    O, U, A, I, B, A0, B0 = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, a, 0), (1, b, 0)
    L, Lu, La, Lb = cross(O, U), cross(U, A), cross(A0, A), cross(B0, B)
    D = cross(cross(I, B), La)
    C = cross(cross(O, D), Lb)
    A0_B0 = cross(L, cross(A, C))
    print('I =', I)
    print('A0 =', A0)
    print('B0 =', B0)
    print('A =', A)
    print('B =', B)
    print('D =', D)
    print('C =', C)
    print('A0 * B0 =', A0_B0)

if __name__ == '__main__':
    main()