from math import sqrt
from scipy.optimize import basinhopping
from sympy import nsimplify

def fun(X):
    u, v = X[0], X[1]
    bounds = 0
    for w in [u, v]:
        if w < 0:
            bounds += (1 + w**2)*1e10
    if bounds > 0:
        return bounds
    # g(vu)
    return u**4*v**2 + 3*u**3*v**2 + u**3*v + 2*u**2*v**2 + u**2 - 5*u*v + 3*u + v**2 - 3*v + 3

def main():
    res = basinhopping(fun, [1, 1], minimizer_kwargs = {'method': 'Nelder-Mead'})
    print(res)
    print('u =', res.x[0], '=', nsimplify(res.x[0], tolerance = 0.000001))
    print('v =', res.x[1], '=', nsimplify(res.x[1], tolerance = 0.000001))

if __name__ == '__main__':
    main()