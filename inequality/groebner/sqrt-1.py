from sympy import *

def main():
    # sqrt(a/b) + sqrt(b/a) >= 2
    a, b, A, B, l1, l2, l3 = symbols('a, b, A, B, l1, l2, l3', negative = False)
    g1 = A**2*a - b
    g2 = B**2*b - a
    g3 = a + b - 2
    f = A + B - 2
    L = f + l1*g1 + l2*g2 + l3*g3
    B = groebner([g1, g2, g3, diff(L, a), diff(L, b), diff(L, A), diff(L, B)], l1, l2, l3, A, B, a, b)
    print(B, len(B))

if __name__ == '__main__':
    main()