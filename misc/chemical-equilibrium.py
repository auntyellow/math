import numpy as np
from scipy.optimize import basinhopping

# https://math.stackexchange.com/q/4191759
# https://chemistry.stackexchange.com/q/153869

'''
# H2O <-> H+ + OH-
# NH3 + H2O <-> NH4+ + OH-
# [H+, OH-, NH3, NH4+]
# 0.1M NH3
C = np.array([0, 0, 0.1, 0])
N = np.array([
    [1, 1, 0, 0],
    [0, 1, -1, 1]
])
K = np.array([1e-14, 1.77e-5])
X0 = np.array([0, 0])

# H2O <-> H+ + OH-
# HSO4- <-> H+ + SO42-
# [H+, OH-, HSO4-, SO42-]
# 0.5M H2SO4
C = np.array([1.0, 0, 0, 0.5])
# equivalent to
# C = np.array([0.5, 0, 0.5, 0])
N = np.array([
    [1, 1, 0, 0],
    [1, 0, -1, 1]
])
K = np.array([1e-14, 1e-2])
X0 = np.array([0, 0])

# H2O <-> H+ + OH-
# CO2 + H2O <-> H+ + HCO3-
# HCO3- <-> H+ + CO32-
# [H+, OH-, CO2, HCO3-, CO32-]
# 0.001M CO2 + 0.01M HCO3-
C = np.array([0, 0, 0.001, 0.01, 0])
N = np.array([
    [1, 1, 0, 0, 0],
    [1, 0, -1, 1, 0],
    [1, 0, 0, -1, 1],
])
K = np.array([1e-14, 4.3e-7, 4.8e-11])
X0 = np.array([0, 0, 0])

# H2O <-> H+ + OH-
# CH3COOH <-> H+ + CH3COO-
# NH3 + H2O <-> NH4+ + OH-
# [H+, OH-, CH3COOH, CH3COO-, NH3, NH4+]
# 0.1M CH3COONH4
C = np.array([0, 0, 0.1, 0, 0.1, 0])
# equivalent to
# C = np.array([0, 0, 0, 0.1, 0, 0.1])
# + 0.01M HCl
# C = np.array([0.01, 0, 0.1, 0, 0.1, 0])
N = np.array([
    [1, 1, 0, 0, 0, 0],
    [1, 0, -1, 1, 0, 0],
    [0, 1, 0, 0, -1, 1],
])
K = np.array([1e-14, 1.75e-5, 1.77e-5])
X0 = np.array([0, 0, 0])
'''

# H2O <-> H+ + OH-
# NH3 + H2O <-> NH4+ + OH-
# CO2 + H2O <-> H+ + HCO3-
# HCO3- <-> H+ + CO32-
# [H+, OH-, NH3, NH4+, CO2, HCO3-, CO32-]
# 0.1M NH4HCO3
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
    bounds = 0
    for c1 in C1:
        if c1 <= 0:
            bounds += (1 - c1)*1e+14
    if bounds > 0:
        return bounds
    return np.linalg.norm(np.matmul(N, np.log(C1)) - np.log(K))

def main():
    print('Inequilibrium:', chem_eq(X0))
    print('Concentrations:', concentr(X0))
    result = basinhopping(chem_eq, X0, niter = 200, \
            minimizer_kwargs = {'method': 'Nelder-Mead', 'options': {'xatol': 1e-14, 'maxiter': 2000}})
    print(result)
    X = result.x
    print('Inequilibrium:', chem_eq(X))
    print('Concentrations:', concentr(X))

if __name__ == '__main__':
    main()