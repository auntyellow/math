from sympy import Matrix, factor, prem, solve, symbols

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2

def collinear(P):
    return [P[0], P[1], 1]

def det(row_def, *points):
    mat = []
    for point in points:
        mat.append(row_def(point))
    return Matrix(mat).det()

def main():
    a, b, c, d, e, S = symbols('a, b, c, d, e, S')
    A, B, C = (0, 0), (c, 0), (d, e)
    AC = dist2(A, C) - b**2
    BC = dist2(B, C) - a**2
    S0 = det(collinear, A, B, C)/2
    '''
    # eliminate d and e by 'solve'
    for (d0, e0) in solve([AC, BC], d, e):
        # negative area if ABC is clockwise
        print('S =', factor(S0.subs({d: d0, e: e0})))
    '''
    h1 = AC
    h2 = BC
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