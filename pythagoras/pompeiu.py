from sympy import *
from cartesian import *

# https://en.wikipedia.org/wiki/Pompeiu%27s_theorem

def main():
    x, y = symbols('x, y')
    A, B, C = (2, 0), (-1, sqrt(3)), (-1, -sqrt(3))
    P = (x, y)
    AP2, BP2, CP2 = dist2(A, P), dist2(B, P), dist2(C, P)
    print('AP^2 =', expand(AP2))
    print('BP^2 =', expand(BP2))
    print('CP^2 =', expand(CP2))
    fA = AP2 - BP2 - CP2
    print('f_A =', expand(fA))
    print('4*BP^2*CP^2 - f_A^2 =', factor(4*BP2*CP2 - fA**2))
    # AP2 = BP2 + CP2 if and only if f_A >= 0 and P is on circle
    fB = BP2 - AP2 - CP2
    print('f_B =', expand(fB))
    print('4*AP^2*CP^2 - f_B^2 =', factor(4*AP2*CP2 - fB**2))
    # BP2 = AP2 + CP2 if and only if f_B >= 0 and P is on circle
    fC = CP2 - AP2 - BP2
    print('f_C =', expand(fC))
    print('4*AP^2*BP^2 - f_C^2 =', factor(4*AP2*BP2 - fC**2))
    # CP2 = AP2 + BP2 if and only if f_C >= 0 and P is on circle
    print('f_A and f_B are tangent on', (solve(resultant(fA, fB, y)), solve(resultant(fA, fB, x))))
    print('f_A and f_C are tangent on', (solve(resultant(fA, fC, y)), solve(resultant(fA, fC, x))))
    print('f_B and f_C are tangent on', (solve(resultant(fB, fC, y)), solve(resultant(fB, fC, x))))

if __name__ == '__main__':
    main()