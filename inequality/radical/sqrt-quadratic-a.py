from math import sqrt
from scipy.optimize import basinhopping
from sympy import factor, nsimplify, symbols

def fun(X):
    k = X[0]
    non_negative_coeffs = [
        # 1,
        -k**2 + 2*k + 2,
        2*k + 1,
    ]
    bounds = 0
    for v in non_negative_coeffs:
        if v < 0:
            bounds += (1 + v**2)*1e10
    if bounds > 0:
        return bounds
    v = 0
    for x in [.25, .5]:
        s = k*x**2 + (1 - k)*x
        v += (x - s**2)**2
    return v

def main():
    res = basinhopping(fun, [0, 0], minimizer_kwargs = {'method': 'Nelder-Mead'})
    print(res)
    k = nsimplify(res.x[0], tolerance = 0.01, rational = True)
    print('k =', k)
    x, u = symbols('x, u')
    s = k*x**2 + (1 - k)*x
    print('s =', s)
    print('x - s**2 =', factor((x - s**2).subs(x, 1/(1 + u))))

if __name__ == '__main__':
    main()