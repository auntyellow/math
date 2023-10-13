from math import sqrt, inf
from scipy.optimize import minimize
from sympy import nsimplify

# https://math.stackexchange.com/a/3658031
# sum_cyc(1/(2 + a**2 + b**2)) <= 3/4

def fun(X):
    p, q = X[0], X[1]
    non_positive_coeffs = [ \
        64*p - 32*q - 28, \
        128*p - 64*q - 56, \
        136*p - 96*q - 32, \
        80*p + 6*q - 76, \
        204*p - 144*q - 48, \
        72*p - 72*q, \
        16*p + 38*q - 48, \
        36*q - 72, \
        72*p - 72*q, \
        25*q - 17, \
        -34*p + 42*q - 28, \
        -72*p + 36*q - 36, \
    ]
    non_negative_coeffs = [ \
        38*p - 19*q + 25, \
        22*p + 40*q + 20, \
        110*p - 30*q + 44, \
        -20*p + 66*q - 8, \
        108*q, \
        72*p - 36*q + 36, \
        -4*p + 40*q - 24, \
        -84*p + 144*q - 48, \
        -72*p + 72*q, \
        8*q - 4, \
        -8*p + 48*q - 32, \
        -72*p + 72*q, \
        2*p - q + 4, \
        2*p - q + 4, \
        8*p + 8, \
        2 - q, \
        4*p + 4, \
        6*p + 6, \
    ]
    v = 0
    for coeff in non_positive_coeffs:
        v += coeff**2 if coeff > 0 else 0
    for coeff in non_negative_coeffs:
        v += coeff**2 if coeff < 0 else 0
    return v

def main():
    min = inf
    initial_guesses = [0]
    # not necessary to search range
    '''
    ratio = 2
    for i in range(-10, 11):
        initial_guesses.append(ratio**i)
        initial_guesses.insert(0, -ratio**i)
    '''
    for p0 in initial_guesses:
        print('Guess p0 =', p0, 'and all q0 ...')
        for q0 in initial_guesses:
            result = minimize(fun, [p0, q0], \
                method = 'Nelder-Mead', options={'xatol': 1e-10, 'maxiter': 10000})
            # necessary to check result.success ? 
            if result.fun < min:
                min = result.fun
                p, q = result.x[0], result.x[1]
                print(result)
                print(p0, '->', p, ',', q0, '->', q)
    print('p =', nsimplify(p, tolerance = 0.001))
    print('q =', nsimplify(q, tolerance = 0.001))

if __name__ == '__main__':
    main()