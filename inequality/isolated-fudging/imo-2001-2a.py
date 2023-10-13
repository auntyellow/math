from math import sqrt, inf
from scipy.optimize import minimize
from sympy import nsimplify

# # IMO 2001 problem 2
# sum_cyc(a/sqrt(a**2 + 8*b*c)) >= 1

def fun(X):
    p, q = X[0], X[1]
    non_positive_coeffs = [ \
        800*p**2 - 640*p + 128, \
        2400*p**2 - 1920*p + 384, \
        320*p**2 - 2048*p + 768, \
        3200*p**2 + 1120*p*q - 2560*p - 448*q + 512, \
        800*p**2 - 5120*p + 1920, \
        -4092*p**2 + 224*p*q - 3536*p - 196*q**2 + 1008*q + 1536, \
        2400*p**2 + 2240*p*q - 1920*p - 896*q + 384, \
        1600*p**2 + 1344*p*q - 5760*p - 1792*q + 2048, \
        -8184*p**2 + 448*p*q - 7072*p - 392*q**2 + 2016*q + 3072, \
        -5024*p**2 + 2016*p*q - 4000*p + 2016*q + 1024, \
        1000*p**2 + 1680*p*q - 800*p + 392*q**2 - 672*q + 160, \
        1600*p**2 + 2016*p*q - 3520*p - 2688*q + 1152, \
        -6264*p**2 - 2380*p*q - 5584*p - 588*q**2 - 1792*q + 1856, \
        -7536*p**2 + 3024*p*q - 6000*p + 3024*q + 1536, \
        -1512*p**2 + 1512*p*q - 1512*p + 1512*q, \
        200*p**2 + 560*p*q - 160*p + 392*q**2 - 224*q + 32, \
        880*p**2 + 1792*p*q - 1152*p + 784*q**2 - 1344*q + 320, \
        -2172*p**2 - 2604*p*q - 2048*p - 392*q**2 - 2800*q + 320, \
        -4416*p**2 - 2016*p*q - 4800*p - 2016*q - 384, \
        -1512*p**2 + 1512*p*q - 1512*p + 1512*q, \
        200*p**2 + 560*p*q - 160*p + 392*q**2 - 224*q + 32, \
        -195*p**2 - 98*p*q - 12*p + 245*q**2 - 196*q - 160, \
        -952*p**2 - 1512*p*q - 1400*p - 1512*q - 448, \
        -540*p**2 - 756*p*q - 1836*p - 756*q - 1296, \
        17*p**2 + 98*p*q - 288*p - 147*q**2 + 784*q - 1040, \
        158*p**2 + 448*p*q - 776*p - 686*q**2 + 3192*q - 3776, \
        106*p**2 + 756*p*q - 3008*p + 98*q**2 + 1344*q - 4192, \
        557*p**2 + 770*p*q + 204*p - 1519*q**2 + 6356*q - 5792, \
        818*p**2 + 4900*p*q - 8248*p - 1078*q**2 + 7448*q - 11712, \
        -579*p**2 - 98*p*q - 6828*p + 245*q**2 - 196*q - 6592, \
        868*p**2 + 532*p*q + 2408*p - 1960*q**2 + 7784*q - 4928, \
        2816*p**2 + 10696*p*q - 6968*p - 1960*q**2 + 16184*q - 13312, \
        -1620*p**2 + 7980*p*q - 14552*p - 392*q**2 + 7784*q - 12736, \
        -1208*p**2 - 1512*p*q - 5944*p - 1512*q - 4736, \
        512*p**2 - 224*p*q + 2900*p - 1568*q**2 + 5852*q - 2512, \
        4592*p**2 + 9912*p*q - 784*p - 1960*q**2 + 17360*q - 8512, \
        -864*p**2 + 17276*p*q - 11416*p - 588*q**2 + 17864*q - 9376, \
        -3792*p**2 + 5040*p*q - 8592*p + 5040*q - 4800, \
        -540*p**2 - 756*p*q - 1836*p - 756*q - 1296, \
        -40*p**2 - 616*p*q + 1544*p - 784*q**2 + 2520*q - 768, \
        3208*p**2 + 4368*p*q + 1712*p - 1176*q**2 + 9072*q - 3456, \
        2280*p**2 + 12544*p*q - 4288*p - 392*q**2 + 14112*q - 4608, \
        -4560*p**2 + 9072*p*q - 6096*p + 9072*q - 1536, \
        -1512*p**2 + 1512*p*q - 1512*p + 1512*q, \
        -100*p**2 - 280*p*q + 360*p - 196*q**2 + 504*q - 128, \
        520*p**2 + 448*p*q + 928*p - 392*q**2 + 2016*q - 768, \
        1908*p**2 + 3248*p*q - 608*p - 196*q**2 + 4032*q - 1536, \
        -1024*p**2 + 4032*p*q - 2048*p + 4032*q - 1024, \
        -1512*p**2 + 1512*p*q - 1512*p + 1512*q, \
    ]
    v = 0
    for coeff in non_positive_coeffs:
        v += coeff**2 if coeff > 0 else 0
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
                # Nelder-Mead works well. CG doesn't seem to work here
                # method = 'CG', options={'gtol': 1e-15, 'eps': 1e-15})
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