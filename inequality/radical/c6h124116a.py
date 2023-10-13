from math import sqrt, inf
from scipy.optimize import minimize
from sympy import nsimplify

def fun(X):
    x = 1
    y, z = X[0], X[1]
    return 253*sqrt(527)*(x + y + z)/140 - sqrt(578*x**2 + 1143*y*z) - sqrt(578*y**2 + 1143*z*x) - sqrt(578*z**2 + 1143*x*y)

def main():
    # https://artofproblemsolving.com/community/c6h124116
    # When does the equality hold (except for trival x = y = z = 0)? Assume x <= y <= z:
    min = inf
    initial_guesses = [1, 2, 4, 8, 16]
    for y0 in initial_guesses:
        for z0 in initial_guesses:
            result = minimize(fun, [y0, z0], bounds=((1, inf), (1, inf)), \
                method = 'Nelder-Mead', options={'xatol': 1e-10, 'maxiter': 10000})
                # CG doesn't seem to work here
                # method = 'CG', options={'gtol': 1e-15, 'eps': 1e-15})
            if result.success and result.fun < min:
                min = result.fun
                y, z = result.x[0], result.x[1]
                print(result)
                print(y0, '->', y, ',', z0, '->', z)
                if result.fun < 2e-10:
                    found = True
                    break
        if found:
            break
    print('y =', nsimplify(y, tolerance = 0.001))
    print('z =', nsimplify(z, tolerance = 0.001))

if __name__ == '__main__':
    main()