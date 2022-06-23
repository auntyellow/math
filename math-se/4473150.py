from sympy import *
from cartesian import *

def midpoint(A, B):
    return (A[0] + B[0])/2, (A[1] + B[1])/2

def main():
    # https://math.stackexchange.com/q/4473150
    a, b, r = symbols('a, b, r', positive = True)
    A, B, C, D = (0, 0), (1, 0), (r*cos(a), r*sin(a)), (1 - r*cos(b), r*sin(b))
    E, F = midpoint(B, C), midpoint(A, D)
    AC, BD, EF = line(A, C), line(B, D), line(E, F)
    G, H, J = intersect(AC, EF), intersect(BD, EF), intersect(AC, BD)
    GJ2, HJ2 = dist2(G, J), dist2(H, J)
    print('GJ**2 - HJ**2 =', simplify(GJ2 - HJ2))

if __name__ == '__main__':
    main()