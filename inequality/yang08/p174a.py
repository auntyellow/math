from math import sqrt
from scipy.optimize import basinhopping
from sympy import nsimplify

def fun(X):
    a1, a2, a3, a4, a5, a6, a7 = X[0], X[1], X[2], X[3], X[4], X[5], X[6]
    bounds = 0
    for v in X:
        if v < 0:
            bounds += (1 + v**2)*1e10
    if bounds > 0:
        return bounds
    # return a1**3*a3*a4*a5 + a1**3*a3*a4 + a1**3*a3*a5**2 + a1**3*a3*a5 + a1**3*a4**2*a5 + a1**3*a4**2 + a1**3*a4*a5**2 + a1**3*a4*a5 + a1**2*a2**2*a4*a5 + a1**2*a2**2*a4 + a1**2*a2**2*a5**2 + a1**2*a2**2*a5 + a1**2*a2*a3**2*a5 + a1**2*a2*a3**2 + a1**2*a2*a3*a4**2 - a1**2*a2*a3*a4*a5 - a1**2*a2*a3*a4 - 2*a1**2*a2*a3*a5**2 - a1**2*a2*a3*a5 + a1**2*a2*a4**3 - 2*a1**2*a2*a4**2*a5 - 2*a1**2*a2*a4**2 - 2*a1**2*a2*a4*a5**2 - a1**2*a2*a4*a5 + a1**2*a3**3*a5 + a1**2*a3**3 + a1**2*a3**2*a4**2 - 2*a1**2*a3**2*a4*a5 - 2*a1**2*a3**2*a4 - 3*a1**2*a3**2*a5**2 - 2*a1**2*a3**2*a5 + a1**2*a3*a4**3 - 2*a1**2*a3*a4**2*a5 - 2*a1**2*a3*a4**2 - 2*a1**2*a3*a4*a5**2 + a1**2*a3*a4 + a1**2*a3*a5**2 + a1**2*a3*a5 + a1**2*a4**2*a5 + a1**2*a4**2 + a1**2*a4*a5**2 + a1**2*a4*a5 + a1*a2**3*a4*a5 + a1*a2**3*a4 + a1*a2**3*a5**2 + a1*a2**3*a5 + a1*a2**2*a3**2*a5 + a1*a2**2*a3**2 + a1*a2**2*a3*a4**2 - a1*a2**2*a3*a4*a5 - a1*a2**2*a3*a4 - 2*a1*a2**2*a3*a5**2 - a1*a2**2*a3*a5 + a1*a2**2*a4**3 - 2*a1*a2**2*a4**2*a5 - 2*a1*a2**2*a4**2 - 2*a1*a2**2*a4*a5**2 + a1*a2**2*a4 + a1*a2**2*a5**2 + a1*a2**2*a5 + a1*a2*a3**3*a5 + a1*a2*a3**3 + a1*a2*a3**2*a4**2 - a1*a2*a3**2*a4*a5 - a1*a2*a3**2*a4 - 2*a1*a2*a3**2*a5**2 + a1*a2*a3**2 + a1*a2*a3*a4**3 - a1*a2*a3*a4**2*a5 - a1*a2*a3*a4 + a1*a2*a3*a5**3 - a1*a2*a3*a5**2 - a1*a2*a3*a5 + a1*a2*a4**3 + a1*a2*a4**2*a5**2 - a1*a2*a4**2*a5 - 2*a1*a2*a4**2 + a1*a2*a4*a5**3 - a1*a2*a4*a5**2 - a1*a2*a4*a5 + a1*a3**3*a5 + a1*a3**3 + a1*a3**2*a4**2 + a1*a3**2*a4*a5**2 - a1*a3**2*a4*a5 - 2*a1*a3**2*a4 + a1*a3**2*a5**3 - 2*a1*a3**2*a5**2 - 2*a1*a3**2*a5 + a1*a3*a4**3 + a1*a3*a4**2*a5**2 - a1*a3*a4**2*a5 - 2*a1*a3*a4**2 + a1*a3*a4*a5**3 - a1*a3*a4*a5**2 - a1*a3*a4*a5 + a2**3*a4*a5 + a2**3*a4 + a2**3*a5**2 + a2**3*a5 + a2**2*a3**2*a5 + a2**2*a3**2 + a2**2*a3*a4**2 + a2**2*a3*a4*a5**2 - a2**2*a3*a4*a5 - 2*a2**2*a3*a4 + a2**2*a3*a5**3 - 2*a2**2*a3*a5**2 - 2*a2**2*a3*a5 + a2**2*a4**3 + a2**2*a4**2*a5**2 - 2*a2**2*a4**2*a5 - 3*a2**2*a4**2 + a2**2*a4*a5**3 - 2*a2**2*a4*a5**2 - 2*a2**2*a4*a5 + a2*a3**3*a5 + a2*a3**3 + a2*a3**2*a4**2 + a2*a3**2*a4*a5**2 - a2*a3**2*a4*a5 - 2*a2*a3**2*a4 + a2*a3**2*a5**3 - 2*a2*a3**2*a5**2 - 2*a2*a3**2*a5 + a2*a3*a4**3 + a2*a3*a4**2*a5**2 - a2*a3*a4**2*a5 - 2*a2*a3*a4**2 + a2*a3*a4*a5**3 - a2*a3*a4*a5**2 + a2*a3*a4 + a2*a3*a5**2 + a2*a3*a5 + a2*a4**2*a5 + a2*a4**2 + a2*a4*a5**2 + a2*a4*a5 + a3**2*a4*a5 + a3**2*a4 + a3**2*a5**2 + a3**2*a5 + a3*a4**2*a5 + a3*a4**2 + a3*a4*a5**2 + a3*a4*a5
    return a1**3*a3*a4*a5*a6*a7 + a1**3*a3*a4*a5*a6 + a1**3*a3*a4*a5*a7**2 + a1**3*a3*a4*a5*a7 + a1**3*a3*a4*a6**2*a7 + a1**3*a3*a4*a6**2 + a1**3*a3*a4*a6*a7**2 + a1**3*a3*a4*a6*a7 + a1**3*a3*a5**2*a6*a7 + a1**3*a3*a5**2*a6 + a1**3*a3*a5**2*a7**2 + a1**3*a3*a5**2*a7 + a1**3*a3*a5*a6**2*a7 + a1**3*a3*a5*a6**2 + a1**3*a3*a5*a6*a7**2 + a1**3*a3*a5*a6*a7 + a1**3*a4**2*a5*a6*a7 + a1**3*a4**2*a5*a6 + a1**3*a4**2*a5*a7**2 + a1**3*a4**2*a5*a7 + a1**3*a4**2*a6**2*a7 + a1**3*a4**2*a6**2 + a1**3*a4**2*a6*a7**2 + a1**3*a4**2*a6*a7 + a1**3*a4*a5**2*a6*a7 + a1**3*a4*a5**2*a6 + a1**3*a4*a5**2*a7**2 + a1**3*a4*a5**2*a7 + a1**3*a4*a5*a6**2*a7 + a1**3*a4*a5*a6**2 + a1**3*a4*a5*a6*a7**2 + a1**3*a4*a5*a6*a7 + a1**2*a2**2*a4*a5*a6*a7 + a1**2*a2**2*a4*a5*a6 + a1**2*a2**2*a4*a5*a7**2 + a1**2*a2**2*a4*a5*a7 + a1**2*a2**2*a4*a6**2*a7 + a1**2*a2**2*a4*a6**2 + a1**2*a2**2*a4*a6*a7**2 + a1**2*a2**2*a4*a6*a7 + a1**2*a2**2*a5**2*a6*a7 + a1**2*a2**2*a5**2*a6 + a1**2*a2**2*a5**2*a7**2 + a1**2*a2**2*a5**2*a7 + a1**2*a2**2*a5*a6**2*a7 + a1**2*a2**2*a5*a6**2 + a1**2*a2**2*a5*a6*a7**2 + a1**2*a2**2*a5*a6*a7 + a1**2*a2*a3**2*a5*a6*a7 + a1**2*a2*a3**2*a5*a6 + a1**2*a2*a3**2*a5*a7**2 + a1**2*a2*a3**2*a5*a7 + a1**2*a2*a3**2*a6**2*a7 + a1**2*a2*a3**2*a6**2 + a1**2*a2*a3**2*a6*a7**2 + a1**2*a2*a3**2*a6*a7 + a1**2*a2*a3*a4**2*a6*a7 + a1**2*a2*a3*a4**2*a6 + a1**2*a2*a3*a4**2*a7**2 + a1**2*a2*a3*a4**2*a7 + a1**2*a2*a3*a4*a5**2*a7 + a1**2*a2*a3*a4*a5**2 + a1**2*a2*a3*a4*a5*a6**2 - a1**2*a2*a3*a4*a5*a6*a7 - a1**2*a2*a3*a4*a5*a6 - 2*a1**2*a2*a3*a4*a5*a7**2 - a1**2*a2*a3*a4*a5*a7 + a1**2*a2*a3*a4*a6**3 - 2*a1**2*a2*a3*a4*a6**2*a7 - 2*a1**2*a2*a3*a4*a6**2 - 2*a1**2*a2*a3*a4*a6*a7**2 - a1**2*a2*a3*a4*a6*a7 + a1**2*a2*a3*a5**3*a7 + a1**2*a2*a3*a5**3 + a1**2*a2*a3*a5**2*a6**2 - 2*a1**2*a2*a3*a5**2*a6*a7 - 2*a1**2*a2*a3*a5**2*a6 - 3*a1**2*a2*a3*a5**2*a7**2 - 2*a1**2*a2*a3*a5**2*a7 + a1**2*a2*a3*a5*a6**3 - 2*a1**2*a2*a3*a5*a6**2*a7 - 2*a1**2*a2*a3*a5*a6**2 - 2*a1**2*a2*a3*a5*a6*a7**2 - a1**2*a2*a3*a5*a6*a7 + a1**2*a2*a4**3*a6*a7 + a1**2*a2*a4**3*a6 + a1**2*a2*a4**3*a7**2 + a1**2*a2*a4**3*a7 + a1**2*a2*a4**2*a5**2*a7 + a1**2*a2*a4**2*a5**2 + a1**2*a2*a4**2*a5*a6**2 - 2*a1**2*a2*a4**2*a5*a6*a7 - 2*a1**2*a2*a4**2*a5*a6 - 3*a1**2*a2*a4**2*a5*a7**2 - 2*a1**2*a2*a4**2*a5*a7 + a1**2*a2*a4**2*a6**3 - 3*a1**2*a2*a4**2*a6**2*a7 - 3*a1**2*a2*a4**2*a6**2 - 3*a1**2*a2*a4**2*a6*a7**2 - 2*a1**2*a2*a4**2*a6*a7 + a1**2*a2*a4*a5**3*a7 + a1**2*a2*a4*a5**3 + a1**2*a2*a4*a5**2*a6**2 - 2*a1**2*a2*a4*a5**2*a6*a7 - 2*a1**2*a2*a4*a5**2*a6 - 3*a1**2*a2*a4*a5**2*a7**2 - 2*a1**2*a2*a4*a5**2*a7 + a1**2*a2*a4*a5*a6**3 - 2*a1**2*a2*a4*a5*a6**2*a7 - 2*a1**2*a2*a4*a5*a6**2 - 2*a1**2*a2*a4*a5*a6*a7**2 - a1**2*a2*a4*a5*a6*a7 + a1**2*a3**3*a5*a6*a7 + a1**2*a3**3*a5*a6 + a1**2*a3**3*a5*a7**2 + a1**2*a3**3*a5*a7 + a1**2*a3**3*a6**2*a7 + a1**2*a3**3*a6**2 + a1**2*a3**3*a6*a7**2 + a1**2*a3**3*a6*a7 + a1**2*a3**2*a4**2*a6*a7 + a1**2*a3**2*a4**2*a6 + a1**2*a3**2*a4**2*a7**2 + a1**2*a3**2*a4**2*a7 + a1**2*a3**2*a4*a5**2*a7 + a1**2*a3**2*a4*a5**2 + a1**2*a3**2*a4*a5*a6**2 - 2*a1**2*a3**2*a4*a5*a6*a7 - 2*a1**2*a3**2*a4*a5*a6 - 3*a1**2*a3**2*a4*a5*a7**2 - 2*a1**2*a3**2*a4*a5*a7 + a1**2*a3**2*a4*a6**3 - 3*a1**2*a3**2*a4*a6**2*a7 - 3*a1**2*a3**2*a4*a6**2 - 3*a1**2*a3**2*a4*a6*a7**2 - 2*a1**2*a3**2*a4*a6*a7 + a1**2*a3**2*a5**3*a7 + a1**2*a3**2*a5**3 + a1**2*a3**2*a5**2*a6**2 - 3*a1**2*a3**2*a5**2*a6*a7 - 3*a1**2*a3**2*a5**2*a6 - 4*a1**2*a3**2*a5**2*a7**2 - 3*a1**2*a3**2*a5**2*a7 + a1**2*a3**2*a5*a6**3 - 3*a1**2*a3**2*a5*a6**2*a7 - 3*a1**2*a3**2*a5*a6**2 - 3*a1**2*a3**2*a5*a6*a7**2 - 2*a1**2*a3**2*a5*a6*a7 + a1**2*a3*a4**3*a6*a7 + a1**2*a3*a4**3*a6 + a1**2*a3*a4**3*a7**2 + a1**2*a3*a4**3*a7 + a1**2*a3*a4**2*a5**2*a7 + a1**2*a3*a4**2*a5**2 + a1**2*a3*a4**2*a5*a6**2 - 2*a1**2*a3*a4**2*a5*a6*a7 - 2*a1**2*a3*a4**2*a5*a6 - 3*a1**2*a3*a4**2*a5*a7**2 - 2*a1**2*a3*a4**2*a5*a7 + a1**2*a3*a4**2*a6**3 - 3*a1**2*a3*a4**2*a6**2*a7 - 3*a1**2*a3*a4**2*a6**2 - 3*a1**2*a3*a4**2*a6*a7**2 - 2*a1**2*a3*a4**2*a6*a7 + a1**2*a3*a4*a5**3*a7 + a1**2*a3*a4*a5**3 + a1**2*a3*a4*a5**2*a6**2 - 2*a1**2*a3*a4*a5**2*a6*a7 - 2*a1**2*a3*a4*a5**2*a6 - 3*a1**2*a3*a4*a5**2*a7**2 - 2*a1**2*a3*a4*a5**2*a7 + a1**2*a3*a4*a5*a6**3 - 2*a1**2*a3*a4*a5*a6**2*a7 - 2*a1**2*a3*a4*a5*a6**2 - 2*a1**2*a3*a4*a5*a6*a7**2 + a1**2*a3*a4*a5*a6 + a1**2*a3*a4*a5*a7**2 + a1**2*a3*a4*a5*a7 + a1**2*a3*a4*a6**2*a7 + a1**2*a3*a4*a6**2 + a1**2*a3*a4*a6*a7**2 + a1**2*a3*a4*a6*a7 + a1**2*a3*a5**2*a6*a7 + a1**2*a3*a5**2*a6 + a1**2*a3*a5**2*a7**2 + a1**2*a3*a5**2*a7 + a1**2*a3*a5*a6**2*a7 + a1**2*a3*a5*a6**2 + a1**2*a3*a5*a6*a7**2 + a1**2*a3*a5*a6*a7 + a1**2*a4**2*a5*a6*a7 + a1**2*a4**2*a5*a6 + a1**2*a4**2*a5*a7**2 + a1**2*a4**2*a5*a7 + a1**2*a4**2*a6**2*a7 + a1**2*a4**2*a6**2 + a1**2*a4**2*a6*a7**2 + a1**2*a4**2*a6*a7 + a1**2*a4*a5**2*a6*a7 + a1**2*a4*a5**2*a6 + a1**2*a4*a5**2*a7**2 + a1**2*a4*a5**2*a7 + a1**2*a4*a5*a6**2*a7 + a1**2*a4*a5*a6**2 + a1**2*a4*a5*a6*a7**2 + a1**2*a4*a5*a6*a7 + a1*a2**3*a4*a5*a6*a7 + a1*a2**3*a4*a5*a6 + a1*a2**3*a4*a5*a7**2 + a1*a2**3*a4*a5*a7 + a1*a2**3*a4*a6**2*a7 + a1*a2**3*a4*a6**2 + a1*a2**3*a4*a6*a7**2 + a1*a2**3*a4*a6*a7 + a1*a2**3*a5**2*a6*a7 + a1*a2**3*a5**2*a6 + a1*a2**3*a5**2*a7**2 + a1*a2**3*a5**2*a7 + a1*a2**3*a5*a6**2*a7 + a1*a2**3*a5*a6**2 + a1*a2**3*a5*a6*a7**2 + a1*a2**3*a5*a6*a7 + a1*a2**2*a3**2*a5*a6*a7 + a1*a2**2*a3**2*a5*a6 + a1*a2**2*a3**2*a5*a7**2 + a1*a2**2*a3**2*a5*a7 + a1*a2**2*a3**2*a6**2*a7 + a1*a2**2*a3**2*a6**2 + a1*a2**2*a3**2*a6*a7**2 + a1*a2**2*a3**2*a6*a7 + a1*a2**2*a3*a4**2*a6*a7 + a1*a2**2*a3*a4**2*a6 + a1*a2**2*a3*a4**2*a7**2 + a1*a2**2*a3*a4**2*a7 + a1*a2**2*a3*a4*a5**2*a7 + a1*a2**2*a3*a4*a5**2 + a1*a2**2*a3*a4*a5*a6**2 - a1*a2**2*a3*a4*a5*a6*a7 - a1*a2**2*a3*a4*a5*a6 - 2*a1*a2**2*a3*a4*a5*a7**2 - a1*a2**2*a3*a4*a5*a7 + a1*a2**2*a3*a4*a6**3 - 2*a1*a2**2*a3*a4*a6**2*a7 - 2*a1*a2**2*a3*a4*a6**2 - 2*a1*a2**2*a3*a4*a6*a7**2 - a1*a2**2*a3*a4*a6*a7 + a1*a2**2*a3*a5**3*a7 + a1*a2**2*a3*a5**3 + a1*a2**2*a3*a5**2*a6**2 - 2*a1*a2**2*a3*a5**2*a6*a7 - 2*a1*a2**2*a3*a5**2*a6 - 3*a1*a2**2*a3*a5**2*a7**2 - 2*a1*a2**2*a3*a5**2*a7 + a1*a2**2*a3*a5*a6**3 - 2*a1*a2**2*a3*a5*a6**2*a7 - 2*a1*a2**2*a3*a5*a6**2 - 2*a1*a2**2*a3*a5*a6*a7**2 - a1*a2**2*a3*a5*a6*a7 + a1*a2**2*a4**3*a6*a7 + a1*a2**2*a4**3*a6 + a1*a2**2*a4**3*a7**2 + a1*a2**2*a4**3*a7 + a1*a2**2*a4**2*a5**2*a7 + a1*a2**2*a4**2*a5**2 + a1*a2**2*a4**2*a5*a6**2 - 2*a1*a2**2*a4**2*a5*a6*a7 - 2*a1*a2**2*a4**2*a5*a6 - 3*a1*a2**2*a4**2*a5*a7**2 - 2*a1*a2**2*a4**2*a5*a7 + a1*a2**2*a4**2*a6**3 - 3*a1*a2**2*a4**2*a6**2*a7 - 3*a1*a2**2*a4**2*a6**2 - 3*a1*a2**2*a4**2*a6*a7**2 - 2*a1*a2**2*a4**2*a6*a7 + a1*a2**2*a4*a5**3*a7 + a1*a2**2*a4*a5**3 + a1*a2**2*a4*a5**2*a6**2 - 2*a1*a2**2*a4*a5**2*a6*a7 - 2*a1*a2**2*a4*a5**2*a6 - 3*a1*a2**2*a4*a5**2*a7**2 - 2*a1*a2**2*a4*a5**2*a7 + a1*a2**2*a4*a5*a6**3 - 2*a1*a2**2*a4*a5*a6**2*a7 - 2*a1*a2**2*a4*a5*a6**2 - 2*a1*a2**2*a4*a5*a6*a7**2 + a1*a2**2*a4*a5*a6 + a1*a2**2*a4*a5*a7**2 + a1*a2**2*a4*a5*a7 + a1*a2**2*a4*a6**2*a7 + a1*a2**2*a4*a6**2 + a1*a2**2*a4*a6*a7**2 + a1*a2**2*a4*a6*a7 + a1*a2**2*a5**2*a6*a7 + a1*a2**2*a5**2*a6 + a1*a2**2*a5**2*a7**2 + a1*a2**2*a5**2*a7 + a1*a2**2*a5*a6**2*a7 + a1*a2**2*a5*a6**2 + a1*a2**2*a5*a6*a7**2 + a1*a2**2*a5*a6*a7 + a1*a2*a3**3*a5*a6*a7 + a1*a2*a3**3*a5*a6 + a1*a2*a3**3*a5*a7**2 + a1*a2*a3**3*a5*a7 + a1*a2*a3**3*a6**2*a7 + a1*a2*a3**3*a6**2 + a1*a2*a3**3*a6*a7**2 + a1*a2*a3**3*a6*a7 + a1*a2*a3**2*a4**2*a6*a7 + a1*a2*a3**2*a4**2*a6 + a1*a2*a3**2*a4**2*a7**2 + a1*a2*a3**2*a4**2*a7 + a1*a2*a3**2*a4*a5**2*a7 + a1*a2*a3**2*a4*a5**2 + a1*a2*a3**2*a4*a5*a6**2 - a1*a2*a3**2*a4*a5*a6*a7 - a1*a2*a3**2*a4*a5*a6 - 2*a1*a2*a3**2*a4*a5*a7**2 - a1*a2*a3**2*a4*a5*a7 + a1*a2*a3**2*a4*a6**3 - 2*a1*a2*a3**2*a4*a6**2*a7 - 2*a1*a2*a3**2*a4*a6**2 - 2*a1*a2*a3**2*a4*a6*a7**2 - a1*a2*a3**2*a4*a6*a7 + a1*a2*a3**2*a5**3*a7 + a1*a2*a3**2*a5**3 + a1*a2*a3**2*a5**2*a6**2 - 2*a1*a2*a3**2*a5**2*a6*a7 - 2*a1*a2*a3**2*a5**2*a6 - 3*a1*a2*a3**2*a5**2*a7**2 - 2*a1*a2*a3**2*a5**2*a7 + a1*a2*a3**2*a5*a6**3 - 2*a1*a2*a3**2*a5*a6**2*a7 - 2*a1*a2*a3**2*a5*a6**2 - 2*a1*a2*a3**2*a5*a6*a7**2 + a1*a2*a3**2*a5*a6 + a1*a2*a3**2*a5*a7**2 + a1*a2*a3**2*a5*a7 + a1*a2*a3**2*a6**2*a7 + a1*a2*a3**2*a6**2 + a1*a2*a3**2*a6*a7**2 + a1*a2*a3**2*a6*a7 + a1*a2*a3*a4**3*a6*a7 + a1*a2*a3*a4**3*a6 + a1*a2*a3*a4**3*a7**2 + a1*a2*a3*a4**3*a7 + a1*a2*a3*a4**2*a5**2*a7 + a1*a2*a3*a4**2*a5**2 + a1*a2*a3*a4**2*a5*a6**2 - a1*a2*a3*a4**2*a5*a6*a7 - a1*a2*a3*a4**2*a5*a6 - 2*a1*a2*a3*a4**2*a5*a7**2 - a1*a2*a3*a4**2*a5*a7 + a1*a2*a3*a4**2*a6**3 - 2*a1*a2*a3*a4**2*a6**2*a7 - 2*a1*a2*a3*a4**2*a6**2 - 2*a1*a2*a3*a4**2*a6*a7**2 + a1*a2*a3*a4**2*a6 + a1*a2*a3*a4**2*a7**2 + a1*a2*a3*a4**2*a7 + a1*a2*a3*a4*a5**3*a7 + a1*a2*a3*a4*a5**3 + a1*a2*a3*a4*a5**2*a6**2 - a1*a2*a3*a4*a5**2*a6*a7 - a1*a2*a3*a4*a5**2*a6 - 2*a1*a2*a3*a4*a5**2*a7**2 + a1*a2*a3*a4*a5**2 + a1*a2*a3*a4*a5*a6**3 - a1*a2*a3*a4*a5*a6**2*a7 - a1*a2*a3*a4*a5*a6 + a1*a2*a3*a4*a5*a7**3 - a1*a2*a3*a4*a5*a7**2 - a1*a2*a3*a4*a5*a7 + a1*a2*a3*a4*a6**3 + a1*a2*a3*a4*a6**2*a7**2 - a1*a2*a3*a4*a6**2*a7 - 2*a1*a2*a3*a4*a6**2 + a1*a2*a3*a4*a6*a7**3 - a1*a2*a3*a4*a6*a7**2 - a1*a2*a3*a4*a6*a7 + a1*a2*a3*a5**3*a7 + a1*a2*a3*a5**3 + a1*a2*a3*a5**2*a6**2 + a1*a2*a3*a5**2*a6*a7**2 - a1*a2*a3*a5**2*a6*a7 - 2*a1*a2*a3*a5**2*a6 + a1*a2*a3*a5**2*a7**3 - 2*a1*a2*a3*a5**2*a7**2 - 2*a1*a2*a3*a5**2*a7 + a1*a2*a3*a5*a6**3 + a1*a2*a3*a5*a6**2*a7**2 - a1*a2*a3*a5*a6**2*a7 - 2*a1*a2*a3*a5*a6**2 + a1*a2*a3*a5*a6*a7**3 - a1*a2*a3*a5*a6*a7**2 - a1*a2*a3*a5*a6*a7 + a1*a2*a4**3*a6*a7 + a1*a2*a4**3*a6 + a1*a2*a4**3*a7**2 + a1*a2*a4**3*a7 + a1*a2*a4**2*a5**2*a7 + a1*a2*a4**2*a5**2 + a1*a2*a4**2*a5*a6**2 + a1*a2*a4**2*a5*a6*a7**2 - a1*a2*a4**2*a5*a6*a7 - 2*a1*a2*a4**2*a5*a6 + a1*a2*a4**2*a5*a7**3 - 2*a1*a2*a4**2*a5*a7**2 - 2*a1*a2*a4**2*a5*a7 + a1*a2*a4**2*a6**3 + a1*a2*a4**2*a6**2*a7**2 - 2*a1*a2*a4**2*a6**2*a7 - 3*a1*a2*a4**2*a6**2 + a1*a2*a4**2*a6*a7**3 - 2*a1*a2*a4**2*a6*a7**2 - 2*a1*a2*a4**2*a6*a7 + a1*a2*a4*a5**3*a7 + a1*a2*a4*a5**3 + a1*a2*a4*a5**2*a6**2 + a1*a2*a4*a5**2*a6*a7**2 - a1*a2*a4*a5**2*a6*a7 - 2*a1*a2*a4*a5**2*a6 + a1*a2*a4*a5**2*a7**3 - 2*a1*a2*a4*a5**2*a7**2 - 2*a1*a2*a4*a5**2*a7 + a1*a2*a4*a5*a6**3 + a1*a2*a4*a5*a6**2*a7**2 - a1*a2*a4*a5*a6**2*a7 - 2*a1*a2*a4*a5*a6**2 + a1*a2*a4*a5*a6*a7**3 - a1*a2*a4*a5*a6*a7**2 - a1*a2*a4*a5*a6*a7 + a1*a3**3*a5*a6*a7 + a1*a3**3*a5*a6 + a1*a3**3*a5*a7**2 + a1*a3**3*a5*a7 + a1*a3**3*a6**2*a7 + a1*a3**3*a6**2 + a1*a3**3*a6*a7**2 + a1*a3**3*a6*a7 + a1*a3**2*a4**2*a6*a7 + a1*a3**2*a4**2*a6 + a1*a3**2*a4**2*a7**2 + a1*a3**2*a4**2*a7 + a1*a3**2*a4*a5**2*a7 + a1*a3**2*a4*a5**2 + a1*a3**2*a4*a5*a6**2 + a1*a3**2*a4*a5*a6*a7**2 - a1*a3**2*a4*a5*a6*a7 - 2*a1*a3**2*a4*a5*a6 + a1*a3**2*a4*a5*a7**3 - 2*a1*a3**2*a4*a5*a7**2 - 2*a1*a3**2*a4*a5*a7 + a1*a3**2*a4*a6**3 + a1*a3**2*a4*a6**2*a7**2 - 2*a1*a3**2*a4*a6**2*a7 - 3*a1*a3**2*a4*a6**2 + a1*a3**2*a4*a6*a7**3 - 2*a1*a3**2*a4*a6*a7**2 - 2*a1*a3**2*a4*a6*a7 + a1*a3**2*a5**3*a7 + a1*a3**2*a5**3 + a1*a3**2*a5**2*a6**2 + a1*a3**2*a5**2*a6*a7**2 - 2*a1*a3**2*a5**2*a6*a7 - 3*a1*a3**2*a5**2*a6 + a1*a3**2*a5**2*a7**3 - 3*a1*a3**2*a5**2*a7**2 - 3*a1*a3**2*a5**2*a7 + a1*a3**2*a5*a6**3 + a1*a3**2*a5*a6**2*a7**2 - 2*a1*a3**2*a5*a6**2*a7 - 3*a1*a3**2*a5*a6**2 + a1*a3**2*a5*a6*a7**3 - 2*a1*a3**2*a5*a6*a7**2 - 2*a1*a3**2*a5*a6*a7 + a1*a3*a4**3*a6*a7 + a1*a3*a4**3*a6 + a1*a3*a4**3*a7**2 + a1*a3*a4**3*a7 + a1*a3*a4**2*a5**2*a7 + a1*a3*a4**2*a5**2 + a1*a3*a4**2*a5*a6**2 + a1*a3*a4**2*a5*a6*a7**2 - a1*a3*a4**2*a5*a6*a7 - 2*a1*a3*a4**2*a5*a6 + a1*a3*a4**2*a5*a7**3 - 2*a1*a3*a4**2*a5*a7**2 - 2*a1*a3*a4**2*a5*a7 + a1*a3*a4**2*a6**3 + a1*a3*a4**2*a6**2*a7**2 - 2*a1*a3*a4**2*a6**2*a7 - 3*a1*a3*a4**2*a6**2 + a1*a3*a4**2*a6*a7**3 - 2*a1*a3*a4**2*a6*a7**2 - 2*a1*a3*a4**2*a6*a7 + a1*a3*a4*a5**3*a7 + a1*a3*a4*a5**3 + a1*a3*a4*a5**2*a6**2 + a1*a3*a4*a5**2*a6*a7**2 - a1*a3*a4*a5**2*a6*a7 - 2*a1*a3*a4*a5**2*a6 + a1*a3*a4*a5**2*a7**3 - 2*a1*a3*a4*a5**2*a7**2 - 2*a1*a3*a4*a5**2*a7 + a1*a3*a4*a5*a6**3 + a1*a3*a4*a5*a6**2*a7**2 - a1*a3*a4*a5*a6**2*a7 - 2*a1*a3*a4*a5*a6**2 + a1*a3*a4*a5*a6*a7**3 - a1*a3*a4*a5*a6*a7**2 - a1*a3*a4*a5*a6*a7 + a2**3*a4*a5*a6*a7 + a2**3*a4*a5*a6 + a2**3*a4*a5*a7**2 + a2**3*a4*a5*a7 + a2**3*a4*a6**2*a7 + a2**3*a4*a6**2 + a2**3*a4*a6*a7**2 + a2**3*a4*a6*a7 + a2**3*a5**2*a6*a7 + a2**3*a5**2*a6 + a2**3*a5**2*a7**2 + a2**3*a5**2*a7 + a2**3*a5*a6**2*a7 + a2**3*a5*a6**2 + a2**3*a5*a6*a7**2 + a2**3*a5*a6*a7 + a2**2*a3**2*a5*a6*a7 + a2**2*a3**2*a5*a6 + a2**2*a3**2*a5*a7**2 + a2**2*a3**2*a5*a7 + a2**2*a3**2*a6**2*a7 + a2**2*a3**2*a6**2 + a2**2*a3**2*a6*a7**2 + a2**2*a3**2*a6*a7 + a2**2*a3*a4**2*a6*a7 + a2**2*a3*a4**2*a6 + a2**2*a3*a4**2*a7**2 + a2**2*a3*a4**2*a7 + a2**2*a3*a4*a5**2*a7 + a2**2*a3*a4*a5**2 + a2**2*a3*a4*a5*a6**2 + a2**2*a3*a4*a5*a6*a7**2 - a2**2*a3*a4*a5*a6*a7 - 2*a2**2*a3*a4*a5*a6 + a2**2*a3*a4*a5*a7**3 - 2*a2**2*a3*a4*a5*a7**2 - 2*a2**2*a3*a4*a5*a7 + a2**2*a3*a4*a6**3 + a2**2*a3*a4*a6**2*a7**2 - 2*a2**2*a3*a4*a6**2*a7 - 3*a2**2*a3*a4*a6**2 + a2**2*a3*a4*a6*a7**3 - 2*a2**2*a3*a4*a6*a7**2 - 2*a2**2*a3*a4*a6*a7 + a2**2*a3*a5**3*a7 + a2**2*a3*a5**3 + a2**2*a3*a5**2*a6**2 + a2**2*a3*a5**2*a6*a7**2 - 2*a2**2*a3*a5**2*a6*a7 - 3*a2**2*a3*a5**2*a6 + a2**2*a3*a5**2*a7**3 - 3*a2**2*a3*a5**2*a7**2 - 3*a2**2*a3*a5**2*a7 + a2**2*a3*a5*a6**3 + a2**2*a3*a5*a6**2*a7**2 - 2*a2**2*a3*a5*a6**2*a7 - 3*a2**2*a3*a5*a6**2 + a2**2*a3*a5*a6*a7**3 - 2*a2**2*a3*a5*a6*a7**2 - 2*a2**2*a3*a5*a6*a7 + a2**2*a4**3*a6*a7 + a2**2*a4**3*a6 + a2**2*a4**3*a7**2 + a2**2*a4**3*a7 + a2**2*a4**2*a5**2*a7 + a2**2*a4**2*a5**2 + a2**2*a4**2*a5*a6**2 + a2**2*a4**2*a5*a6*a7**2 - 2*a2**2*a4**2*a5*a6*a7 - 3*a2**2*a4**2*a5*a6 + a2**2*a4**2*a5*a7**3 - 3*a2**2*a4**2*a5*a7**2 - 3*a2**2*a4**2*a5*a7 + a2**2*a4**2*a6**3 + a2**2*a4**2*a6**2*a7**2 - 3*a2**2*a4**2*a6**2*a7 - 4*a2**2*a4**2*a6**2 + a2**2*a4**2*a6*a7**3 - 3*a2**2*a4**2*a6*a7**2 - 3*a2**2*a4**2*a6*a7 + a2**2*a4*a5**3*a7 + a2**2*a4*a5**3 + a2**2*a4*a5**2*a6**2 + a2**2*a4*a5**2*a6*a7**2 - 2*a2**2*a4*a5**2*a6*a7 - 3*a2**2*a4*a5**2*a6 + a2**2*a4*a5**2*a7**3 - 3*a2**2*a4*a5**2*a7**2 - 3*a2**2*a4*a5**2*a7 + a2**2*a4*a5*a6**3 + a2**2*a4*a5*a6**2*a7**2 - 2*a2**2*a4*a5*a6**2*a7 - 3*a2**2*a4*a5*a6**2 + a2**2*a4*a5*a6*a7**3 - 2*a2**2*a4*a5*a6*a7**2 - 2*a2**2*a4*a5*a6*a7 + a2*a3**3*a5*a6*a7 + a2*a3**3*a5*a6 + a2*a3**3*a5*a7**2 + a2*a3**3*a5*a7 + a2*a3**3*a6**2*a7 + a2*a3**3*a6**2 + a2*a3**3*a6*a7**2 + a2*a3**3*a6*a7 + a2*a3**2*a4**2*a6*a7 + a2*a3**2*a4**2*a6 + a2*a3**2*a4**2*a7**2 + a2*a3**2*a4**2*a7 + a2*a3**2*a4*a5**2*a7 + a2*a3**2*a4*a5**2 + a2*a3**2*a4*a5*a6**2 + a2*a3**2*a4*a5*a6*a7**2 - a2*a3**2*a4*a5*a6*a7 - 2*a2*a3**2*a4*a5*a6 + a2*a3**2*a4*a5*a7**3 - 2*a2*a3**2*a4*a5*a7**2 - 2*a2*a3**2*a4*a5*a7 + a2*a3**2*a4*a6**3 + a2*a3**2*a4*a6**2*a7**2 - 2*a2*a3**2*a4*a6**2*a7 - 3*a2*a3**2*a4*a6**2 + a2*a3**2*a4*a6*a7**3 - 2*a2*a3**2*a4*a6*a7**2 - 2*a2*a3**2*a4*a6*a7 + a2*a3**2*a5**3*a7 + a2*a3**2*a5**3 + a2*a3**2*a5**2*a6**2 + a2*a3**2*a5**2*a6*a7**2 - 2*a2*a3**2*a5**2*a6*a7 - 3*a2*a3**2*a5**2*a6 + a2*a3**2*a5**2*a7**3 - 3*a2*a3**2*a5**2*a7**2 - 3*a2*a3**2*a5**2*a7 + a2*a3**2*a5*a6**3 + a2*a3**2*a5*a6**2*a7**2 - 2*a2*a3**2*a5*a6**2*a7 - 3*a2*a3**2*a5*a6**2 + a2*a3**2*a5*a6*a7**3 - 2*a2*a3**2*a5*a6*a7**2 - 2*a2*a3**2*a5*a6*a7 + a2*a3*a4**3*a6*a7 + a2*a3*a4**3*a6 + a2*a3*a4**3*a7**2 + a2*a3*a4**3*a7 + a2*a3*a4**2*a5**2*a7 + a2*a3*a4**2*a5**2 + a2*a3*a4**2*a5*a6**2 + a2*a3*a4**2*a5*a6*a7**2 - a2*a3*a4**2*a5*a6*a7 - 2*a2*a3*a4**2*a5*a6 + a2*a3*a4**2*a5*a7**3 - 2*a2*a3*a4**2*a5*a7**2 - 2*a2*a3*a4**2*a5*a7 + a2*a3*a4**2*a6**3 + a2*a3*a4**2*a6**2*a7**2 - 2*a2*a3*a4**2*a6**2*a7 - 3*a2*a3*a4**2*a6**2 + a2*a3*a4**2*a6*a7**3 - 2*a2*a3*a4**2*a6*a7**2 - 2*a2*a3*a4**2*a6*a7 + a2*a3*a4*a5**3*a7 + a2*a3*a4*a5**3 + a2*a3*a4*a5**2*a6**2 + a2*a3*a4*a5**2*a6*a7**2 - a2*a3*a4*a5**2*a6*a7 - 2*a2*a3*a4*a5**2*a6 + a2*a3*a4*a5**2*a7**3 - 2*a2*a3*a4*a5**2*a7**2 - 2*a2*a3*a4*a5**2*a7 + a2*a3*a4*a5*a6**3 + a2*a3*a4*a5*a6**2*a7**2 - a2*a3*a4*a5*a6**2*a7 - 2*a2*a3*a4*a5*a6**2 + a2*a3*a4*a5*a6*a7**3 - a2*a3*a4*a5*a6*a7**2 + a2*a3*a4*a5*a6 + a2*a3*a4*a5*a7**2 + a2*a3*a4*a5*a7 + a2*a3*a4*a6**2*a7 + a2*a3*a4*a6**2 + a2*a3*a4*a6*a7**2 + a2*a3*a4*a6*a7 + a2*a3*a5**2*a6*a7 + a2*a3*a5**2*a6 + a2*a3*a5**2*a7**2 + a2*a3*a5**2*a7 + a2*a3*a5*a6**2*a7 + a2*a3*a5*a6**2 + a2*a3*a5*a6*a7**2 + a2*a3*a5*a6*a7 + a2*a4**2*a5*a6*a7 + a2*a4**2*a5*a6 + a2*a4**2*a5*a7**2 + a2*a4**2*a5*a7 + a2*a4**2*a6**2*a7 + a2*a4**2*a6**2 + a2*a4**2*a6*a7**2 + a2*a4**2*a6*a7 + a2*a4*a5**2*a6*a7 + a2*a4*a5**2*a6 + a2*a4*a5**2*a7**2 + a2*a4*a5**2*a7 + a2*a4*a5*a6**2*a7 + a2*a4*a5*a6**2 + a2*a4*a5*a6*a7**2 + a2*a4*a5*a6*a7 + a3**2*a4*a5*a6*a7 + a3**2*a4*a5*a6 + a3**2*a4*a5*a7**2 + a3**2*a4*a5*a7 + a3**2*a4*a6**2*a7 + a3**2*a4*a6**2 + a3**2*a4*a6*a7**2 + a3**2*a4*a6*a7 + a3**2*a5**2*a6*a7 + a3**2*a5**2*a6 + a3**2*a5**2*a7**2 + a3**2*a5**2*a7 + a3**2*a5*a6**2*a7 + a3**2*a5*a6**2 + a3**2*a5*a6*a7**2 + a3**2*a5*a6*a7 + a3*a4**2*a5*a6*a7 + a3*a4**2*a5*a6 + a3*a4**2*a5*a7**2 + a3*a4**2*a5*a7 + a3*a4**2*a6**2*a7 + a3*a4**2*a6**2 + a3*a4**2*a6*a7**2 + a3*a4**2*a6*a7 + a3*a4*a5**2*a6*a7 + a3*a4*a5**2*a6 + a3*a4*a5**2*a7**2 + a3*a4*a5**2*a7 + a3*a4*a5*a6**2*a7 + a3*a4*a5*a6**2 + a3*a4*a5*a6*a7**2 + a3*a4*a5*a6*a7

def main():
    res = basinhopping(fun, [1, 1, 1, 1, 1, 1, 1], minimizer_kwargs = {'method': 'Nelder-Mead'})
    print(res)
    print('a1 =', res.x[0], '=', nsimplify(res.x[0], tolerance = 0.000001))
    print('a2 =', res.x[1], '=', nsimplify(res.x[1], tolerance = 0.000001))
    print('a3 =', res.x[2], '=', nsimplify(res.x[2], tolerance = 0.000001))
    print('a4 =', res.x[3], '=', nsimplify(res.x[3], tolerance = 0.000001))
    print('a5 =', res.x[4], '=', nsimplify(res.x[4], tolerance = 0.000001))
    print('a6 =', res.x[5], '=', nsimplify(res.x[5], tolerance = 0.000001))
    print('a7 =', res.x[6], '=', nsimplify(res.x[6], tolerance = 0.000001))

if __name__ == '__main__':
    main()