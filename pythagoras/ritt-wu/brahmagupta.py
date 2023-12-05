from sympy import Matrix, factor, prem, solve, sqrt, symbols

def collinear(P):
    return [P[0], P[1], 1]

def concyclic(P):
    x, y = P
    return [x**2 + y**2, x, y, 1]

def det(row_def, *points):
    mat = []
    for point in points:
        mat.append(row_def(point))
    return Matrix(mat).det()

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2

def main():
    # set positive true to cancel sqrt(d**2*...)/d
    a, b, c, d = symbols('a, b, c, d', positive = True)
    e, f, g, h, S = symbols('e, f, g, h, S')
    A, B, C, D = (0, 0), (a, 0), (e, f), (g, h)
    BC = dist2(B, C) - b**2
    CD = dist2(C, D) - c**2
    DA = dist2(D, A) - d**2
    concyc = det(concyclic, A, B, C, D)
    S0 = (det(collinear, A, B, C) + det(collinear, A, C, D))/2
    # eliminate e, f, g and h by 'solve'
    # hard to solve
    for (e0, f0, g0, h0) in solve([BC, CD, DA, concyc], (e, f, g, h)):
        print('S =', factor(S0.subs({e: e0, f: f0, g: g0, h: h0})))
    return
    h1 = BC
    h2 = CD
    h3 = DA
    h4 = concyc
    g = S - S0
    print('h1 =', h1)
    print('h2 =', h2)
    h1a = prem(h2, h1, e)
    print('h1a =', h1a)
    R = prem(h2, g, e)
    print('R(e) =', R)
    R = prem(R, h1a, d)
    print('R(d) =', factor(R))

if __name__ == '__main__':
    main()