from sympy import *

def main():
    # sum_cyc(sqrt(a/b)) >= 3
    a, b, c, A, B, C, l1, l2, l3, l4 = symbols('a, b, c, A, B, C, l1, l2, l3, l4', negative = False)
    g1 = A**2*b - c
    g2 = B**2*c - a
    g3 = C**2*a - b
    g4 = a + b + c - 3
    f = A + B + C - 3
    L = f + l1*g1 + l2*g2 + l3*g3 + l4*g4
    B = groebner([g1, g2, g3, g4, diff(L, a), diff(L, b), diff(L, c), diff(L, A), diff(L, B), diff(L, C)], l1, l2, l3, l4, A, B, C, a, b, c)
    print(B, len(B))

if __name__ == '__main__':
    main()