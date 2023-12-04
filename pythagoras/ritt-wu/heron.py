from sympy import Eq, factor, prem, solve, symbols

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2

def main():
    a, b, c, d, e, S = symbols('a, b, c, d, e, S')
    A, B, C = (0, 0), (c, 0), (d, e)
    '''
    # eliminate d and e by 'solve'
    AC = Eq(dist2(A, C), b**2)
    BC = Eq(dist2(B, C), a**2)
    d, e = solve([AC, BC], (d, e))[1]
    print('S^2 =', (c*e/2)**2)
    '''
    h1 = dist2(A, C) - b**2
    h2 = dist2(B, C) - a**2
    g = 2*S - c*e
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