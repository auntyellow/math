from math import sqrt
from scipy.optimize import basinhopping
from sympy import nsimplify

def fun(X):
    a1, a2, a3, a4, a5 = X[0], X[1], X[2], X[3], X[4]
    bounds = 0
    for v in X:
        if v < 0:
            bounds += (1 + v**2)*1e10
    if bounds > 0:
        return bounds
    return a1**3*a3*a4*a5 + a1**3*a3*a4 + a1**3*a3*a5**2 + a1**3*a3*a5 + a1**3*a4**2*a5 + a1**3*a4**2 + a1**3*a4*a5**2 + a1**3*a4*a5 + a1**2*a2**2*a4*a5 + a1**2*a2**2*a4 + a1**2*a2**2*a5**2 + a1**2*a2**2*a5 + a1**2*a2*a3**2*a5 + a1**2*a2*a3**2 + a1**2*a2*a3*a4**2 - a1**2*a2*a3*a4*a5 - a1**2*a2*a3*a4 - 2*a1**2*a2*a3*a5**2 - a1**2*a2*a3*a5 + a1**2*a2*a4**3 - 2*a1**2*a2*a4**2*a5 - 2*a1**2*a2*a4**2 - 2*a1**2*a2*a4*a5**2 - a1**2*a2*a4*a5 + a1**2*a3**3*a5 + a1**2*a3**3 + a1**2*a3**2*a4**2 - 2*a1**2*a3**2*a4*a5 - 2*a1**2*a3**2*a4 - 3*a1**2*a3**2*a5**2 - 2*a1**2*a3**2*a5 + a1**2*a3*a4**3 - 2*a1**2*a3*a4**2*a5 - 2*a1**2*a3*a4**2 - 2*a1**2*a3*a4*a5**2 + a1**2*a3*a4 + a1**2*a3*a5**2 + a1**2*a3*a5 + a1**2*a4**2*a5 + a1**2*a4**2 + a1**2*a4*a5**2 + a1**2*a4*a5 + a1*a2**3*a4*a5 + a1*a2**3*a4 + a1*a2**3*a5**2 + a1*a2**3*a5 + a1*a2**2*a3**2*a5 + a1*a2**2*a3**2 + a1*a2**2*a3*a4**2 - a1*a2**2*a3*a4*a5 - a1*a2**2*a3*a4 - 2*a1*a2**2*a3*a5**2 - a1*a2**2*a3*a5 + a1*a2**2*a4**3 - 2*a1*a2**2*a4**2*a5 - 2*a1*a2**2*a4**2 - 2*a1*a2**2*a4*a5**2 + a1*a2**2*a4 + a1*a2**2*a5**2 + a1*a2**2*a5 + a1*a2*a3**3*a5 + a1*a2*a3**3 + a1*a2*a3**2*a4**2 - a1*a2*a3**2*a4*a5 - a1*a2*a3**2*a4 - 2*a1*a2*a3**2*a5**2 + a1*a2*a3**2 + a1*a2*a3*a4**3 - a1*a2*a3*a4**2*a5 - a1*a2*a3*a4 + a1*a2*a3*a5**3 - a1*a2*a3*a5**2 - a1*a2*a3*a5 + a1*a2*a4**3 + a1*a2*a4**2*a5**2 - a1*a2*a4**2*a5 - 2*a1*a2*a4**2 + a1*a2*a4*a5**3 - a1*a2*a4*a5**2 - a1*a2*a4*a5 + a1*a3**3*a5 + a1*a3**3 + a1*a3**2*a4**2 + a1*a3**2*a4*a5**2 - a1*a3**2*a4*a5 - 2*a1*a3**2*a4 + a1*a3**2*a5**3 - 2*a1*a3**2*a5**2 - 2*a1*a3**2*a5 + a1*a3*a4**3 + a1*a3*a4**2*a5**2 - a1*a3*a4**2*a5 - 2*a1*a3*a4**2 + a1*a3*a4*a5**3 - a1*a3*a4*a5**2 - a1*a3*a4*a5 + a2**3*a4*a5 + a2**3*a4 + a2**3*a5**2 + a2**3*a5 + a2**2*a3**2*a5 + a2**2*a3**2 + a2**2*a3*a4**2 + a2**2*a3*a4*a5**2 - a2**2*a3*a4*a5 - 2*a2**2*a3*a4 + a2**2*a3*a5**3 - 2*a2**2*a3*a5**2 - 2*a2**2*a3*a5 + a2**2*a4**3 + a2**2*a4**2*a5**2 - 2*a2**2*a4**2*a5 - 3*a2**2*a4**2 + a2**2*a4*a5**3 - 2*a2**2*a4*a5**2 - 2*a2**2*a4*a5 + a2*a3**3*a5 + a2*a3**3 + a2*a3**2*a4**2 + a2*a3**2*a4*a5**2 - a2*a3**2*a4*a5 - 2*a2*a3**2*a4 + a2*a3**2*a5**3 - 2*a2*a3**2*a5**2 - 2*a2*a3**2*a5 + a2*a3*a4**3 + a2*a3*a4**2*a5**2 - a2*a3*a4**2*a5 - 2*a2*a3*a4**2 + a2*a3*a4*a5**3 - a2*a3*a4*a5**2 + a2*a3*a4 + a2*a3*a5**2 + a2*a3*a5 + a2*a4**2*a5 + a2*a4**2 + a2*a4*a5**2 + a2*a4*a5 + a3**2*a4*a5 + a3**2*a4 + a3**2*a5**2 + a3**2*a5 + a3*a4**2*a5 + a3*a4**2 + a3*a4*a5**2 + a3*a4*a5

def main():
    res = basinhopping(fun, [1, 1, 1, 1, 1], minimizer_kwargs = {'method': 'Nelder-Mead'})
    print(res)
    print('a1 =', res.x[0], '=', nsimplify(res.x[0], tolerance = 0.000001))
    print('a2 =', res.x[1], '=', nsimplify(res.x[1], tolerance = 0.000001))
    print('a3 =', res.x[2], '=', nsimplify(res.x[2], tolerance = 0.000001))
    print('a4 =', res.x[3], '=', nsimplify(res.x[3], tolerance = 0.000001))
    print('a5 =', res.x[4], '=', nsimplify(res.x[4], tolerance = 0.000001))

if __name__ == '__main__':
    main()