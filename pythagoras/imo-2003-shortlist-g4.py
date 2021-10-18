from sympy import Eq, simplify, solve, symbols

def circle(G):
    x, y = symbols('x, y')
    return Eq((x - G[0])**2 + (y - G[1])**2, G[0]**2 + G[1]**2)

def intersect(Ga, Gb):
    x, y = symbols('x, y')
    # Must root[0] be (0, 0)? 
    # return solve([Ga, Gb], (x, y))[1]
    yi = solve(Eq(Ga.lhs - Gb.lhs, Ga.rhs - Gb.rhs), y)[0]
    eqGa = Ga.subs(y, yi)
    # Divide a zero root to reduce order
    xi = solve(Eq(eqGa.lhs/x, eqGa.rhs/x), x)[0]
    return xi, yi.subs(x, xi)

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2

def main():
    # https://www.imomath.com/index.php?options=323 (Example 1)
    a, b, c, d, k = symbols('a, b, c, d, k')
    G1, G2, G3, G4 = circle((a, 0)), circle((b, k*b)), circle((c, 0)), circle((d, k*d))
    A, B, C, D, P = intersect(G1, G2), intersect(G2, G3), intersect(G3, G4), intersect(G4, G1), (0, 0)
    AB, BC, CD, DA, PB, PD = dist2(A, B), dist2(B, C), dist2(C, D), dist2(D, A), dist2(P, B), dist2(P, D)
    print('AB =', AB)
    print('BC =', BC)
    print('CD =', CD)
    print('DA =', DA)
    print('PB =', PB)
    print('PD =', PD)
    print('AB*BC*PD**2 - CD*DA*PB**2 =', simplify(AB*BC*PD**2 - CD*DA*PB**2))

if __name__ == '__main__':
    main()