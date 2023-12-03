from math import sqrt
from scipy.optimize import basinhopping
from sympy import nsimplify

def fun(X):
    x1, x2, x3, x4 = X[0], X[1], X[2], X[3]
    bounds = 0
    for v in X:
        if v < 0:
            bounds += (1 + v**2)*1e10
    if bounds > 0:
        return bounds
    return (x1**2 + 3)*(x2**2 + 3)*(x3**2 + 3)*(x4**2 + 3) - 16*(x1 + x2 + x3 + x4)**2

def main():
    res = basinhopping(fun, [1, 1, 1, 1], minimizer_kwargs = {'method': 'Nelder-Mead'})
    print(res)
    print('x1 =', res.x[0], '=', nsimplify(res.x[0], tolerance = 0.000001))
    print('x2 =', res.x[1], '=', nsimplify(res.x[1], tolerance = 0.000001))
    print('x3 =', res.x[2], '=', nsimplify(res.x[2], tolerance = 0.000001))
    print('x4 =', res.x[3], '=', nsimplify(res.x[3], tolerance = 0.000001))

if __name__ == '__main__':
    main()