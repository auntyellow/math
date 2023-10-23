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
# + 0.01M H+
# C = np.array([0.01, 0, 0.1, 0, 0.1, 0])
N = np.array([
    [1, 1, 0, 0, 0, 0],
    [1, 0, -1, 1, 0, 0],
    [0, 1, 0, 0, -1, 1],
])
K = np.array([1e-14, 1.75e-5, 1.77e-5])
X0 = np.array([0, 0, 0])

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

# H2O <-> H+ + OH-
# H3PO4 <-> H+ + H2PO4-
# H2PO4- <-> H+ + HPO42-
# HPO42- <-> H+ + PO43-
# [H+, OH-, H3PO4, H2PO4-, HPO42-, PO43-]
# 0.1M H2PO4-
C = np.array([0, 0, 0, 0.1, 0, 0])
N = np.array([
    [1, 1, 0, 0, 0, 0],
    [1, 0, -1, 1, 0, 0],
    [1, 0, 0, -1, 1, 0],
    [1, 0, 0, 0, -1, 1],
])
K = np.array([1e-14, 7.11e-3, 6.32e-8, 4.49e-13])
X0 = np.array([0, 0, 0, 0])
'''

# H2O <-> H+ + OH-
# H3PO4 <-> H+ + H2PO4-
# H2PO4- <-> H+ + HPO42-
# HPO42- <-> H+ + PO43-
# H3Citrate <-> H+ + H2Citrate-
# H2Citrate- <-> H+ + HCitrate2-
# HCitrate2- <-> H+ + Citrate3-
# [H+, OH-, H3PO4, H2PO4-, HPO42-, PO43-, H3Citrate, H2Citrate-, HCitrate2-, Citrate3-]
# https://en.wikipedia.org/wiki/McIlvaine_buffer
# 0.04M HPO42- + 0.08M H3Citrate
# C = np.array([0, 0, 0, 0, 0.0411, 0, 0.07945, 0, 0, 0]) # pH=3
# C = np.array([0, 0, 0, 0, 0.0771, 0, 0.06145, 0, 0, 0]) # pH=4
# C = np.array([0, 0, 0, 0, 0.1030, 0, 0.04850, 0, 0, 0]) # pH=5
# C = np.array([0, 0, 0, 0, 0.1263, 0, 0.03685, 0, 0, 0]) # pH=6
# C = np.array([0, 0, 0, 0, 0.1647, 0, 0.01765, 0, 0, 0]) # pH=7
C = np.array([0, 0, 0, 0, 0.1945, 0, 0.00275, 0, 0, 0]) # pH=8
N = np.array([
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, -1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, -1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, -1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, -1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, -1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, -1, 1],
])
K = np.array([1e-14, 7.11e-3, 6.32e-8, 4.49e-13, 7.41e-4, 1.74e-5, 4.0e-7])
X0 = np.array([0, 0, 0, 0, 0, 0, 0])

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
    # `niter` should be so large for H3PO4
    result = basinhopping(chem_eq, X0, niter = 10000, \
            minimizer_kwargs = {'method': 'Nelder-Mead', 'options': {'xatol': 1e-14, 'maxiter': 10000}})
    print(result)
    X = result.x
    print('Inequilibrium:', chem_eq(X))
    print('Concentrations:', concentr(X))

if __name__ == '__main__':
    main()