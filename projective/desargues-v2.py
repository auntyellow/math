from sympy import symbols
from homogeneous import *

def main():
    # This program shows the definition of addition
    # see ISBN 9787040537550 §10.2, Figure 10-4
    a, b = symbols('a, b')
    O, U, A = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    A0, B0, B = span(1, O, a, U), span(1, O, b, U), span(1, A, 1, U)
    L, Lu1, La, Lb = cross(O, U), cross(U, A), cross(A0, A), cross(B0, B)
    D = cross(cross(O, B), La)
    Lu2 = cross(U, D)
    C = cross(Lu2, Lb)
    A0_B0 = cross(L, cross(A, C))
    print('A0 =', A0)
    print('B0 =', B0)
    print('A =', A)
    print('B =', B)
    print('D =', D)
    print('C =', C)
    print('A0 + B0 =', A0_B0)

if __name__ == '__main__':
    main()