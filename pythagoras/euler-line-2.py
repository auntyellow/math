from sympy import factor, Matrix, simplify, sqrt, symbols

def cos1(a, b, c):
    return (b**2 + c**2 - a**2)/2/b/c

def sin1(c):
    return sqrt(1 - c**2)

def cos2(a, b, c):
    cosA, cosB = cos1(a, b, c), cos1(b, c, a)
    return cosA*cosB + sin1(cosA)*sin1(cosB)

def main():
    a, b, c = symbols('a, b, c', positive = True)
    cosA, cosB, cosC = cos1(a, b, c), cos1(b, c, a), cos1(c, a, b)
    # https://en.wikipedia.org/wiki/Trilinear_coordinates
    G = [1/a, 1/b, 1/c]
    O = [cosA, cosB, cosC]
    H = [1/cosA, 1/cosB, 1/cosC]
    N = [cos2(b, c, a), cos2(c, a, b), cos2(a, b, c)]
    print('Are GOH collinear?', Matrix([G, O, H]).det() == 0)
    print('Are GON collinear?', simplify(Matrix([G, O, N]).det()) == 0)
    I = [1, 1, 1]
    print('GOI are collinear iff', factor(Matrix([G, O, I]).det()), '= 0')

if __name__ == '__main__':
    main()