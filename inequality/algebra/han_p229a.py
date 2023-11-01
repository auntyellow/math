from scipy.optimize import basinhopping
from sympy import nsimplify

# ISBN 9787312056185, p229, ex 6.44

def fun(X):
    bounds = 0
    for v in X:
        if v < 0:
            bounds += (1 + v**2)*1e10
    if bounds > 0:
        return bounds
    # g1(uvw)
    # s, t = X[0], X[1]
    # return 729*s**6 + 1458*s**5*t + 1836*s**5 + 1215*s**4*t**2 + 756*s**4*t - 1188*s**4 + 540*s**3*t**3 + 1080*s**3*t**2 - 15984*s**3*t + 2592*s**3 + 135*s**2*t**4 + 1512*s**2*t**3 - 7128*s**2*t**2 - 28512*s**2*t + 33264*s**2 + 18*s*t**5 + 540*s*t**4 + 1296*s*t**3 - 9504*s*t**2 - 6048*s*t + 53568*s + t**6 + 36*t**5 + 540*t**4 + 864*t**3 - 1296*t**2 + 8640*t + 25920
    # f(d=0)
    u, v = X[0], X[1]
    return 64*u**6 + 192*u**5*v + 576*u**5 + 240*u**4*v**2 - 288*u**4*v + 2160*u**4 + 160*u**3*v**3 - 2016*u**3*v**2 + 864*u**3*v + 4320*u**3 + 60*u**2*v**4 - 1008*u**2*v**3 - 1944*u**2*v**2 + 4752*u**2*v + 4860*u**2 + 12*u*v**5 + 180*u*v**4 - 648*u*v**3 + 1512*u*v**2 + 4860*u*v + 2916*u + v**6 + 18*v**5 + 135*v**4 + 540*v**3 + 1215*v**2 + 1458*v + 729

def main():
    res = basinhopping(fun, [0, 0], niter = 1000, \
        minimizer_kwargs = {'method': 'Nelder-Mead'})
    print(res)
    print(res.x)
    s0 = nsimplify(res.x[0], tolerance = 0.001)
    t0 = nsimplify(res.x[1], tolerance = 0.001)
    print('f({},{}) ='.format(s0, t0), fun([s0, t0]))

if __name__ == '__main__':
    main()