from math import sqrt
from scipy.optimize import minimize
from sympy.ntheory.continued_fraction import continued_fraction, continued_fraction_convergents

def ff(V):
    x = 1
    y, z = V[0], V[1]
    return 253*sqrt(527)*(x + y + z)/140 - sqrt(578*x**2 + 1143*y*z) - sqrt(578*y**2 + 1143*z*x) - sqrt(578*z**2 + 1143*x*y)

def main():
    # https://artofproblemsolving.com/community/c6h124116
    # When does the equality hold (except for trival x = y = z = 0)? Assume x <= y <= z:
    min = minimize(ff, [1, 1], bounds=((1, 10000), (1, 10000)), \
        method = 'Nelder-Mead', options={'xatol': 1e-15, 'maxiter': 10000})
        # CG doesn't seem work here
        # method = 'CG', options={'gtol': 1e-15, 'eps': 1e-15})
    print(min)
    y, z = min.x[0], min.x[1]
    print('y =', continued_fraction_convergents(continued_fraction(y)))
    print('z =', continued_fraction_convergents(continued_fraction(z)))

if __name__ == '__main__':
    main()