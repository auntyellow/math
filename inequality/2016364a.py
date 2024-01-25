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
    return a**4 + b**4 + c**4 + d**4 + a**2*b**2 + b**2*c**2 + c**2*d**2 + d**2*a**2 + 8*(1 - a)*(1 - b)*(1 - c)*(1 - d) - 1

def main():
    res = basinhopping(fun, [.5, .5, .5, .5], niter = 1000, minimizer_kwargs = {'method': 'Nelder-Mead'})
    print(res)
    print('a =', res.x[0], '=', nsimplify(res.x[0], tolerance = 0.001))
    print('b =', res.x[1], '=', nsimplify(res.x[1], tolerance = 0.001))
    print('c =', res.x[1], '=', nsimplify(res.x[2], tolerance = 0.001))
    print('d =', res.x[1], '=', nsimplify(res.x[3], tolerance = 0.001))

if __name__ == '__main__':
    main()