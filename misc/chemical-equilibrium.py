import numpy as np
import scipy.optimize as optimize

# https://math.stackexchange.com/questions/4191759

X_MIN = 1e-14
X_MAX = 1

# simple case:
# H2O <-> H+ + OH-
# NH3 + H2O <-> NH4+ + OH-
C = np.array([0, 0, 0.1, 0])
N = np.array([
    [1, 1, 0, 0],
    [0, 1, -1, 1]
])
K = np.array([1e-14, 1.77e-5])
X0 = np.array([1e-14, 1e-14])
# X0 = np.array([7.57E-12, 1.32E-3])
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
X0 = np.array([2e-14, -1e-14, -1e-14, 1e-14])
'''
def concentr(X):
    return N.transpose() @ X + C

def chem_eq(X):
    return np.linalg.norm(N @ np.log(concentr(X)) - np.log(K))

def main():
    print('Inequilibrium:', chem_eq(X0))
    print('Concentrations:', concentr(X0))
    result = optimize.minimize(chem_eq, X0, bounds=((X_MIN, X_MAX), (X_MIN, X_MAX)), \
            method = 'Nelder-Mead', options={'xatol': 1e-14, 'maxiter': 10000})
            # method = 'CG', options={'gtol': .5e-14, 'eps': .5e-14})
    print(result)
    X = result.x
    print('Inequilibrium:', chem_eq(X))
    print('Concentrations:', concentr(X))

if __name__ == '__main__':
    main()