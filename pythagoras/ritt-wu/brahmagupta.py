from sympy import Matrix, factor, prem, solve, symbols

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
    a, b, c, d, x1, x2, x3, x4, S = symbols('a, b, c, d, x1, x2, x3, x4, S')
    A, B, C, D = (0, 0), (a, 0), (x1, x2), (x3, x4)
    BC = dist2(B, C) - b**2
    CD = dist2(C, D) - c**2
    DA = dist2(D, A) - d**2
    concyc = det(concyclic, A, B, C, D)
    S0 = (det(collinear, A, B, C) + det(collinear, A, C, D))/2
    '''
    # eliminate x1-x4 by 'solve'
    # hard to solve
    for (x10, x20, x30, x40) in solve([BC, CD, DA, concyc], x1, x2, x3, x4):
        print('S^2 =', factor(S0.subs({x1: x10, x2: x20, x3: x30, x4: x40})**2))
    '''
    h1 = BC
    h2 = CD
    h3 = DA
    h4 = concyc
    g = S - S0
    print('h1 =', h1)
    print('h2 =', h2)
    print('h3 =', h3)
    print('h4 =', h4)
    print('g =', g)
    h3a = prem(h4, h3, x4)
    print('h3a =', h3a)
    h1a = prem(h2, h1, x2)
    print('h1a =', h1a)
    R = prem(h4, g, x4)
    print('R(x4) =', R)
    R = prem(R, h3a, x3)
    print('R(x3) =', R)
    R = prem(R, h2, x2)
    print('R(x2) =', R)
    R = prem(R, h1a, x1)
    print('R(x1) =', R)

if __name__ == '__main__':
    main()