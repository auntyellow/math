import numpy as np
from scipy.optimize import basinhopping

# https://math.stackexchange.com/questions/4191759

'''
# simple case:
# H2O <-> H+ + OH-
# NH3 + H2O <-> NH4+ + OH-
C = np.array([0, 0, 0.1, 0])
N = np.array([
    [1, 1, 0, 0],
    [0, 1, -1, 1]
])
K = np.array([1e-14, 1.77e-5])
X0 = np.array([0, 0])
'''
# complicated case:
# H2O <-> H+ + OH-
# NH3 + H2O <-> NH4+ + OH-
# CO2 + H2O <-> H+ + HCO3-
# HCO3- <-> H+ + CO32-
# [H+, OH-, NH3, NH4+, CO2, HCO3-, CO32-]
# 0.1 mol/L NH4HCO3
C = np.array([0, 0, 0, 0.1, 0, 0.1, 0])
N = np.array([
    [1, 1, 0, 0, 0, 0, 0],
    [0, 1, -1, 1, 0, 0, 0],
    [1, 0, 0, 0, -1, 1, 0],
    [1, 0, 0, 0, 0, -1, 1],
])
K = np.array([1e-14, 1.77e-5, 4.3e-7, 4.8e-11])
X0 = np.array([0, 0, 0, 0])

def concentr(X):
    return np.matmul(N.transpose(), X) + C

def chem_eq(X):
    C1 = concentr(X)
    barrier = 0
    for c1 in C1:
        if c1 <= 0:
            barrier += (1 - c1)*1e+14
    if barrier > 0:
        return barrier
    return np.linalg.norm(np.matmul(N, np.log(C1)) - np.log(K))

def main():
    print('Inequilibrium:', chem_eq(X0))
    print('Concentrations:', concentr(X0))
    result = basinhopping(chem_eq, X0, \
            minimizer_kwargs = {'method': 'Nelder-Mead', 'options': {'xatol': 1e-14, 'maxiter': 10000}})
    print(result)
    X = result.x
    print('Inequilibrium:', chem_eq(X))
    print('Concentrations:', concentr(X))

if __name__ == '__main__':
    main()