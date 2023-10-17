from math import sqrt
from scipy.optimize import basinhopping
from sympy import nsimplify

def fun(X):
    x = 1
    y, z = X[0], X[1]
    if y < 1 or z < 1:
        return 1143
    return 253*sqrt(527)*(x + y + z)/140 - sqrt(578*x**2 + 1143*y*z) - sqrt(578*y**2 + 1143*z*x) - sqrt(578*z**2 + 1143*x*y)

def main():
    # https://artofproblemsolving.com/community/c6h124116
    # When does the equality hold (except for trival x = y = z = 0)? Assume x <= y <= z:
    res = basinhopping(fun, [1, 1], minimizer_kwargs = {'method': 'Nelder-Mead'})
    print(res)
    print('y =', nsimplify(res.x[0], tolerance = 0.001))
    print('z =', nsimplify(res.x[1], tolerance = 0.001))

if __name__ == '__main__':
    main()