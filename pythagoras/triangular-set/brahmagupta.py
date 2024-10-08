from sympy import *

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

def vars(expr):
    return sorted(expr.free_symbols, key = lambda s: s.name)

def main():
    # https://en.wikipedia.org/wiki/Brahmagupta%27s_formula
    a, b, c, d, x1, x2, x3, x4, S = symbols('a, b, c, d, x1, x2, x3, x4, S')
    A, B, C, D = (0, 0), (a, 0), (x1, x2), (x3, x4)
    h1 = dist2(B, C) - b**2
    h2 = dist2(C, D) - c**2
    h3 = dist2(D, A) - d**2
    h4 = det(concyclic, A, B, C, D)
    S0 = (det(collinear, A, B, C) + det(collinear, A, C, D))/2
    # too slow, try brahmagupta-sage.py
    # B = groebner([BC, CD, DA, concyc], x1, x2, x3, x4)
    B = [
        -2*a**8*b**2*d**2 - a**8*d**4 + 6*a**6*b**4*d**2 + a**6*b**2*c**2*d**2 - 5*a**6*b**2*d**4 + 7*a**6*c**2*d**4 + 3*a**6*d**6 - 6*a**4*b**6*d**2 - 3*a**4*b**4*c**2*d**2 + 13*a**4*b**4*d**4 + 5*a**4*b**2*c**4*d**2 - 15*a**4*b**2*c**2*d**4 - 4*a**4*b**2*d**6 - 11*a**4*c**4*d**4 + 6*a**4*c**2*d**6 - 3*a**4*d**8 + 2*a**2*b**8*d**2 + 3*a**2*b**6*c**2*d**2 - 7*a**2*b**6*d**4 - 11*a**2*b**4*c**2*d**4 + 9*a**2*b**4*d**6 - 5*a**2*b**2*c**6*d**2 + 21*a**2*b**2*c**4*d**4 + 5*a**2*b**2*c**2*d**6 - 5*a**2*b**2*d**8 + 5*a**2*c**6*d**4 - 9*a**2*c**4*d**6 + 3*a**2*c**2*d**8 + a**2*d**10 - b**8*c**2*d**2 + 3*b**6*c**4*d**2 + 3*b**6*c**2*d**4 - 3*b**4*c**6*d**2 - 2*b**4*c**4*d**4 - 3*b**4*c**2*d**6 + b**2*c**8*d**2 - b**2*c**6*d**4 - b**2*c**4*d**6 + b**2*c**2*d**8 + x1*(4*a**7*b**2*d**2 - 8*a**5*b**4*d**2 - 8*a**5*b**2*c**2*d**2 + 8*a**5*b**2*d**4 - 4*a**5*c**2*d**4 + 4*a**3*b**6*d**2 + 8*a**3*b**4*c**2*d**2 - 8*a**3*b**4*d**4 + 4*a**3*b**2*c**4*d**2 + 4*a**3*b**2*d**6 + 8*a**3*c**4*d**4 - 8*a**3*c**2*d**6 - 4*a*b**4*c**2*d**4 - 8*a*b**2*c**4*d**4 + 8*a*b**2*c**2*d**6 - 4*a*c**6*d**4 + 8*a*c**4*d**6 - 4*a*c**2*d**8) + x4**2*(-4*a**6*d**4 + 8*a**4*b**2*c**2*d**2 - 4*a**4*b**2*d**4 + 4*a**4*c**2*d**4 + 4*a**4*d**6 - 4*a**2*b**4*c**4 + 8*a**2*b**4*c**2*d**2 - 8*a**2*b**2*c**4*d**2 - 8*a**2*b**2*c**2*d**4 - 4*b**6*c**4 + 4*b**4*c**6 + 4*b**4*c**4*d**2),
        x2*(2*a**6*b**2*d**4 - 4*a**4*b**4*d**4 - 4*a**4*b**2*c**2*d**4 + 4*a**4*b**2*d**6 - 2*a**4*c**2*d**6 + 2*a**2*b**6*d**4 + 4*a**2*b**4*c**2*d**4 - 4*a**2*b**4*d**6 + 2*a**2*b**2*c**4*d**4 + 2*a**2*b**2*d**8 + 4*a**2*c**4*d**6 - 4*a**2*c**2*d**8 - 2*b**4*c**2*d**6 - 4*b**2*c**4*d**6 + 4*b**2*c**2*d**8 - 2*c**6*d**6 + 4*c**4*d**8 - 2*c**2*d**10) + x4**3*(-4*a**4*b**2*d**4 + 4*a**4*d**6 + 8*a**2*b**4*c**2*d**2 - 8*a**2*b**2*c**2*d**4 - 4*b**6*c**4 + 4*b**4*c**4*d**2) + x4*(-3*a**6*b**2*d**4 + a**6*d**6 - a**4*b**4*c**2*d**2 + 6*a**4*b**4*d**4 + 9*a**4*b**2*c**2*d**4 - 4*a**4*b**2*d**6 - 2*a**4*c**2*d**6 - 2*a**4*d**8 + 2*a**2*b**6*c**2*d**2 - 3*a**2*b**6*d**4 + 2*a**2*b**4*c**4*d**2 - 22*a**2*b**4*c**2*d**4 + 7*a**2*b**4*d**6 - 9*a**2*b**2*c**4*d**4 + 22*a**2*b**2*c**2*d**6 - 5*a**2*b**2*d**8 + a**2*c**4*d**6 - 2*a**2*c**2*d**8 + a**2*d**10 - b**8*c**2*d**2 + 2*b**6*c**4*d**2 + 5*b**6*c**2*d**4 - b**4*c**6*d**2 + 4*b**4*c**4*d**4 - 7*b**4*c**2*d**6 + 3*b**2*c**6*d**4 - 6*b**2*c**4*d**6 + 3*b**2*c**2*d**8),
        -a**4*d**2 + 2*a**2*b**2*d**2 + 2*a**2*c**2*d**2 - 6*a**2*d**4 - b**4*d**2 + 2*b**2*c**2*d**2 + 2*b**2*d**4 - c**4*d**2 + 2*c**2*d**4 - d**6 + x3*(4*a**3*d**2 - 4*a*b**2*d**2 - 4*a*c**2*d**2 + 4*a*d**4) + x4**2*(4*a**2*d**2 - 4*b**2*c**2),
        a**8*d**4 - 4*a**6*b**2*d**4 - 4*a**6*c**2*d**4 - 4*a**6*d**6 + 6*a**4*b**4*d**4 + 4*a**4*b**2*c**2*d**4 + 4*a**4*b**2*d**6 + 6*a**4*c**4*d**4 + 4*a**4*c**2*d**6 + 6*a**4*d**8 - 4*a**2*b**6*d**4 + 4*a**2*b**4*c**2*d**4 + 4*a**2*b**4*d**6 + 4*a**2*b**2*c**4*d**4 - 40*a**2*b**2*c**2*d**6 + 4*a**2*b**2*d**8 - 4*a**2*c**6*d**4 + 4*a**2*c**4*d**6 + 4*a**2*c**2*d**8 - 4*a**2*d**10 + b**8*d**4 - 4*b**6*c**2*d**4 - 4*b**6*d**6 + 6*b**4*c**4*d**4 + 4*b**4*c**2*d**6 + 6*b**4*d**8 - 4*b**2*c**6*d**4 + 4*b**2*c**4*d**6 + 4*b**2*c**2*d**8 - 4*b**2*d**10 + c**8*d**4 - 4*c**6*d**6 + 6*c**4*d**8 - 4*c**2*d**10 + d**12 + x4**4*(16*a**4*d**4 - 32*a**2*b**2*c**2*d**2 + 16*b**4*c**4) + x4**2*(8*a**6*d**4 + 8*a**4*b**2*c**2*d**2 - 16*a**4*b**2*d**4 - 16*a**4*c**2*d**4 - 16*a**4*d**6 - 16*a**2*b**4*c**2*d**2 + 8*a**2*b**4*d**4 - 16*a**2*b**2*c**4*d**2 + 96*a**2*b**2*c**2*d**4 - 16*a**2*b**2*d**6 + 8*a**2*c**4*d**4 - 16*a**2*c**2*d**6 + 8*a**2*d**8 + 8*b**6*c**2*d**2 - 16*b**4*c**4*d**2 - 16*b**4*c**2*d**4 + 8*b**2*c**6*d**2 - 16*b**2*c**4*d**4 + 8*b**2*c**2*d**6),
    ]
    '''
    # wu's method doesn't seem to work?
    g = S - S0
    x_i = [x1, x2, x3, x4]
    print('h4 =', poly(h4, x_i).expr, vars(h4))
    print('h3 =', poly(h3, x_i).expr, vars(h3))
    h3a = resultant(h4, h3, x4) # eliminate x4, prem doesn't work
    print('h3a =', poly(h3a, x_i).expr, vars(h3a))
    print('h2 =', poly(h2, x_i).expr, vars(h2))
    h2b = resultant(h3, h2, x4) # eliminate x4, prem doesn't work
    print('h2b =', poly(h2b, x_i).expr, vars(h2b))
    h2a = resultant(h3a, h2b, x3) # eliminate x3, prem doesn't work
    print('h2a =', poly(h2a, x_i).expr, vars(h2a))
    print('h1 =', poly(h1, x_i).expr, vars(h1))
    h1a = prem(h2a, h1, x2) # eliminate x2, prem(h1, h2a, x2) doesn't work
    print('h1a =', poly(h1a, x_i).expr, vars(h1a))
    print('g =', poly(g, x_i).expr, vars(g))
    print()

    R = prem(h4, g, x4) # eliminate x4, prem(g, h4, x4) doesn't work
    print('R(x4) =', poly(R, x_i).expr, vars(R))
    R = resultant(R, h3a, x3) # eliminate x3, prem doesn't work
    print('R(x3) =', poly(R, x_i).expr, vars(R))
    R = resultant(R, h2a, x2) # eliminate x2, too slow, prem doesn't work
    print('R(x2) =', poly(R, x_i).expr, vars(R))
    '''
    for x40 in solve(B[3], x4):
        x10 = solve(B[0].subs(x4, x40), x1)[0]
        x20 = solve(B[1].subs(x4, x40), x2)[0]
        x30 = solve(B[2].subs(x4, x40), x3)[0]
        print('S^2 =', factor(S0.subs({x1: x10, x2: x20, x3: x30, x4: x40})**2))

if __name__ == '__main__':
    main()