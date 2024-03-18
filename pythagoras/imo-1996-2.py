from sympy import *

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2

def main():
    # https://imomath.com/index.cgi?page=inversion (Example 2)
    # let's prove the converse: if BQ bisects ∠ABP and BQ bisects ∠ACP,
    # then ∠APB - ∠ACB (∠C) = ∠APC - ∠ABC (∠B)
    a, b, c, p = symbols('a, b, c, p', positive = True)
    x, y = symbols('x, y')
    A, O, P, B = (-a - p, 0), (0, 0), (p, 0), (x, y)
    # put B on a curve such that PQ bisects ∠ABP, i.e. AB/PB = AQ/PQ
    curve = p**2*dist2(A, B) - (a + p)**2*dist2(P, B)
    print('curve =', Poly(curve, x, y))
    poly = Poly(curve.subs(y, -p*x/b), x)
    B = (-factor(poly.nth(1)/poly.nth(2)), factor(p*poly.nth(1)/poly.nth(2)/b))
    print('B =', B)
    print('Is B on circle?', factor(curve.subs({x: B[0], y: B[1]})) == 0)
    C = (B[0].subs(b, -c), B[1].subs(b, -c))
    print('C =', C)
    AB2, AC2, BC2 = dist2(A, B), dist2(A, C), dist2(B, C)
    print('AB =', factor(sqrt(AB2)))
    print('AC =', factor(sqrt(AC2)))
    print('BC =', factor(sqrt(BC2)))
    D, E, F, G = symbols('B, C, D, E', positive = True)
    # D = sqrt(a**2*b**2 + a**2*p**2 + 4*a*b**2*p + 4*b**2*p**2)
    # E = sqrt(a**2*c**2 + a**2*p**2 + 4*a*c**2*p + 4*c**2*p**2)
    # F = sqrt(b**2 + p**2)
    # G = sqrt(c**2 + p**2)
    AB = (a + p)*D/a/F
    AC = (a + p)*E/a/G
    BC = 2*p**2*(a + p)*(b + c)/a/F/G
    cosB = factor((AB2 + BC2 - AC2)/2/AB/BC)
    cosC = factor((AC2 + BC2 - AB2)/2/AC/BC)
    print('cos∠B =', cosB)
    print('cos∠C =', cosC)
    n2_sinB = factor(AB2*BC2 - (cosB*AB*BC)**2)
    n2_sinC = factor(AC2*BC2 - (cosC*AC*BC)**2)
    sinB = sqrt(n2_sinB)/AB/BC
    sinC = sqrt(n2_sinC)/AC/BC
    print('sin∠B =', sinB)
    print('sin∠C =', sinC)
    print('sin²∠B + cos²∠B =', factor((n2_sinB + (cosB*AB*BC)**2)/AB2/BC2))
    print('sin²∠C + cos²∠C =', factor((n2_sinC + (cosC*AC*BC)**2)/AC2/BC2))
    AP2, BP2, CP2 = dist2(A, P), dist2(B, P), dist2(C, P)
    print('AP =', factor(sqrt(AP2)))
    print('BP =', factor(sqrt(BP2)))
    print('CP =', factor(sqrt(CP2)))
    AP = sqrt(AP2)
    BP = b*D/F/(a - b)
    CP = b*E/G/(a - b)
    cosAPB = factor((AP2 + BP2 - AB2)/2/AP/BP)
    cosAPC = factor((AP2 + CP2 - AC2)/2/AP/CP)
    print('cos∠APB =', cosAPB)
    print('cos∠APC =', cosAPC)
    n2_sinAPB = factor(BP2 - (cosAPB*BP)**2)
    n2_sinAPC = factor(CP2 - (cosAPC*CP)**2)
    sinAPB = sqrt(n2_sinAPB)/BP
    sinAPC = sqrt(n2_sinAPC)/CP
    print('sin∠APB =', sinAPB)
    print('sin∠APC =', sinAPC)
    print('sin²∠APB + cos²∠APB =', factor((n2_sinAPB + (cosAPB*BP)**2)/BP2))
    print('sin²∠APC + cos²∠APC =', factor((n2_sinAPC + (cosAPC*CP)**2)/CP2))
    g = cosAPB*cosC + sinAPB*sinC - cosAPC*cosB - sinAPC*sinB
    print('cos(∠APB - ∠C) - cos(∠APC - ∠B) =', factor(g))

    '''
    Now let's prove the original proposition (see imo-1996-2.ggb), i.e.
    if BQ bisects ∠ABP and C'Q' bisects ∠AC'P and Q ≠ Q', then ∠APB - ∠AC'B ≠ ∠APC' - ∠ABC'.
    According to above proof, B is on O (the circle determined by PQA) and
    C' is on O' (the circle determined by PQ'A).
    Assume PQ' > PQ, then it's easy to prove O' is outside O (two circles don't intersect).
    Make C the intersect of PC' and O,
    then ∠APB - ∠AC'B = ∠PAC' + ∠PBC' > ∠PAC + ∠PBC = ∠APB - ∠ACB = ∠APC - ∠ABC > ∠APC - ∠ABC' (QED),
    where the first two equalities are from angle relationship in triangle or quadrilateral,
    and the last equality is from above proved converse.
    '''

if __name__ == '__main__':
    main()