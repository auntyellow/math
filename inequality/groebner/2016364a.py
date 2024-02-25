from math import sqrt
from scipy.optimize import basinhopping
from sympy import nsimplify

def fun(X):
    a, b, c, d = X[0], X[1], X[2], X[3]
    bounds = 0
    for w in X:
        if w < 0:
            bounds += (1 + w**2)*1e10
        elif w > 1:
            bounds += (1 + (w - 1)**2)*1e10
    if bounds > 0:
        return bounds
    # f(----)
    # f = a**4 - 4*a**3 + a**2*b**2 - 2*a**2*b + a**2*d**2 - 2*a**2*d + 8*a**2 - 2*a*b**2 + 8*a*b*c*d + 8*a*b*c + 8*a*b*d + 12*a*b + 8*a*c*d + 8*a*c - 2*a*d**2 + 12*a*d + b**4 - 4*b**3 + b**2*c**2 - 2*b**2*c + 8*b**2 - 2*b*c**2 + 8*b*c*d + 12*b*c + 8*b*d + c**4 - 4*c**3 + c**2*d**2 - 2*c**2*d + 8*c**2 - 2*c*d**2 + 12*c*d + d**4 - 4*d**3 + 8*d**2
    # f(---+), 2 minima
    # f = a**4 - 4*a**3 + a**2*b**2 - 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2 - 8*a*b*c*d + 8*a*b*c - 8*a*b*d + 12*a*b - 8*a*c*d + 8*a*c - 2*a*d**2 - 12*a*d + b**4 - 4*b**3 + b**2*c**2 - 2*b**2*c + 8*b**2 - 2*b*c**2 - 8*b*c*d + 12*b*c - 8*b*d + c**4 - 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 - 2*c*d**2 - 12*c*d + d**4 + 4*d**3 + 8*d**2
    # f(---+, d <= 3/4)
    # f = 16*a**4 - 64*a**3 + 16*a**2*b**2 - 32*a**2*b + 4*a**2*d**2 + 16*a**2*d + 128*a**2 - 32*a*b**2 - 64*a*b*c*d + 128*a*b*c - 64*a*b*d + 192*a*b - 64*a*c*d + 128*a*c - 8*a*d**2 - 96*a*d + 16*b**4 - 64*b**3 + 16*b**2*c**2 - 32*b**2*c + 128*b**2 - 32*b*c**2 - 64*b*c*d + 192*b*c - 64*b*d + 16*c**4 - 64*c**3 + 4*c**2*d**2 + 16*c**2*d + 128*c**2 - 8*c*d**2 - 96*c*d + d**4 + 8*d**3 + 32*d**2
    # f(---+, d >= 3/4)
    f = 16*a**4 + 16*a**2*b**2 + 4*a**2*d**2 - 32*a**2*d + 64*a**2 - 64*a*b*c*d + 128*a*b*d + 128*a*c*d - 256*a*d + 16*b**4 + 16*b**2*c**2 + 128*b*c*d - 256*b*d + 16*c**4 + 4*c**2*d**2 - 32*c**2*d + 64*c**2 - 256*c*d + d**4 - 16*d**3 + 96*d**2 + 256*d
    # f(--++)
    # f = a**4 - 4*a**3 + a**2*b**2 - 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2 + 8*a*b*c*d - 8*a*b*c - 8*a*b*d + 12*a*b + 8*a*c*d - 8*a*c - 2*a*d**2 - 12*a*d + b**4 - 4*b**3 + b**2*c**2 + 2*b**2*c + 8*b**2 - 2*b*c**2 + 8*b*c*d - 12*b*c - 8*b*d + c**4 + 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 + 2*c*d**2 + 12*c*d + d**4 + 4*d**3 + 8*d**2
    # f(-+++)
    # f = a**4 - 4*a**3 + a**2*b**2 + 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2 - 8*a*b*c*d + 8*a*b*c + 8*a*b*d - 12*a*b + 8*a*c*d - 8*a*c - 2*a*d**2 - 12*a*d + b**4 + 4*b**3 + b**2*c**2 + 2*b**2*c + 8*b**2 + 2*b*c**2 - 8*b*c*d + 12*b*c + 8*b*d + c**4 + 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 + 2*c*d**2 + 12*c*d + d**4 + 4*d**3 + 8*d**2
    # f(++++)
    # f = a**4 + 4*a**3 + a**2*b**2 + 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 + 2*a*b**2 + 8*a*b*c*d - 8*a*b*c - 8*a*b*d + 12*a*b - 8*a*c*d + 8*a*c + 2*a*d**2 + 12*a*d + b**4 + 4*b**3 + b**2*c**2 + 2*b**2*c + 8*b**2 + 2*b*c**2 - 8*b*c*d + 12*b*c + 8*b*d + c**4 + 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 + 2*c*d**2 + 12*c*d + d**4 + 4*d**3 + 8*d**2
    # f(-+-+)
    # f = a**4 - 4*a**3 + a**2*b**2 + 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2 + 8*a*b*c*d - 8*a*b*c + 8*a*b*d - 12*a*b - 8*a*c*d + 8*a*c - 2*a*d**2 - 12*a*d + b**4 + 4*b**3 + b**2*c**2 - 2*b**2*c + 8*b**2 + 2*b*c**2 + 8*b*c*d - 12*b*c + 8*b*d + c**4 - 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 - 2*c*d**2 - 12*c*d + d**4 + 4*d**3 + 8*d**2
    return f

def main():
    res = basinhopping(fun, [1, 1, 1, 1], minimizer_kwargs = {'method': 'Nelder-Mead'})
    print(res)
    print('a =', res.x[0], '=', nsimplify(res.x[0], tolerance = 0.001))
    print('b =', res.x[1], '=', nsimplify(res.x[1], tolerance = 0.001))
    print('c =', res.x[2], '=', nsimplify(res.x[2], tolerance = 0.001))
    print('d =', res.x[3], '=', nsimplify(res.x[3], tolerance = 0.001))

if __name__ == '__main__':
    main()