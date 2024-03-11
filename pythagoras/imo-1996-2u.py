from sympy import *

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2

def main():
    # https://imomath.com/index.cgi?page=inversion (Example 2)
    # let's prove the converse: if BO bisects ∠ABP and BO bisects ∠ACP,
    # then ∠APB + ∠ABC (∠B) = ∠APC + ∠ACB (∠C)
    a, b, x, y, x1, x2 = symbols('a, b, x, y, x1, x2')
    A, O, P, B = (-a, 0), (0, 0), (b, 0), (x, y)
    # put B on a curve such that PO bisects ∠ABP, i.e. AB/PB = AO/PO
    curve = b**2*dist2(A, B) - a**2*dist2(P, B)
    print('curve =', Poly(curve, x, y))
    y = solve(curve, y)[0]
    B, C = (x1, y.subs(x, x1)), (x2, -y.subs(x, x2))
    print('B =', B)
    print('C =', C)
    # angles are converted to tan
    # APB, APC = -(b - p)/d, -(c - p)/e
    AB2, AC2, BC2 = dist2(A, B), dist2(A, C), dist2(B, C)
    cosB = simplify((AB2 + BC2 - AC2)/2/sqrt(AB2*BC2))
    cosC = simplify((AC2 + BC2 - AB2)/2/sqrt(AC2*BC2))
    print('cos∠B =', cosB)
    print('cos∠C =', cosC)
    sinB = simplify(sqrt(1 - cosB**2))
    sinC = simplify(sqrt(1 - cosB**2))
    print('sin∠B =', sinB)
    print('sin∠C =', sinC)
    AP2, BP2, CP2 = dist2(A, P), dist2(B, P), dist2(C, P)
    cosAPB = simplify((AP2 + BP2 - AB2)/2/sqrt(AP2*BP2))
    cosAPC = simplify((AP2 + CP2 - AC2)/2/sqrt(AP2*CP2))
    print('cos∠APB =', cosAPB)
    print('cos∠APC =', cosAPC)
    sinAPB = simplify(sqrt(1 - cosAPB**2))
    sinAPC = simplify(sqrt(1 - cosAPB**2))
    print('sin∠APB =', sinAPB)
    print('sin∠APC =', sinAPC)
    g = sinAPB*cosB + cosAPB*sinB - sinAPC*cosC - cosAPC*sinC
    print('∠APB + ∠B - ∠APC - ∠C =', expand(g))

if __name__ == '__main__':
    main()