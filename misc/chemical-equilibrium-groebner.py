from sympy import *

# https://math.stackexchange.com/q/4191759
# https://chemistry.stackexchange.com/q/153869

x0, x1, x2, x3 = symbols('x0, x1, x2, x3') 

'''
# x0: H2O <-> H+ + OH-
# x1: NH3 + H2O <-> NH4+ + OH-
# [H+, OH-, NH3, NH4+]
# 0.1M NH3
c_NH3, k_H2O, k_NH3 = symbols('c_NH3, k_H2O, k_NH3')
C0 = Matrix([[0, 0, c_NH3, 0]])
N = Matrix([
    [1, 1, 0, 0],
    [0, 1, -1, 1]
])
X = Matrix([[x0, x1]])
C = C0 + X*N
eqs = [
    C[0, 0]*C[0, 1] - k_H2O,
    C[0, 1]*C[0, 3] - k_NH3*C[0, 2],
]
subs = {c_NH3: 0.1, k_H2O: 1e-14, k_NH3: 1.77e-5}

# x0: H2O <-> H+ + OH-
# x1: HSO4- <-> H+ + SO42-
# [H+, OH-, HSO4-, SO42-]
# 0.5M H2SO4
c_SO4, k_H2O, k_HSO4 = symbols('c_SO4, k_H2O, k_HSO4')
C0 = Matrix([[c_SO4*2, 0, 0, c_SO4]])
# equivalent to
# C0 = Matrix([[c_SO4, 0, c_SO4, 0]])
N = Matrix([
    [1, 1, 0, 0],
    [1, 0, -1, 1]
])
X = Matrix([[x0, x1]])
C = C0 + X*N
eqs = [
    C[0, 0]*C[0, 1] - k_H2O,
    C[0, 0]*C[0, 3] - k_HSO4*C[0, 2],
]
print(eqs)
subs = {c_SO4: 0.5, k_H2O: 1e-14, k_HSO4: 1e-2}

'''
# H2O <-> H+ + OH-
# CO2 + H2O <-> H+ + HCO3-
# HCO3- <-> H+ + CO32-
# [H+, OH-, CO2, HCO3-, CO32-]
# 0.001M CO2 + 0.01M HCO3-
c_CO2, c_HCO3, k_H2O, k_CO2, k_HCO3 = symbols('c_CO2, c_HCO3, k_H2O, k_CO2, k_HCO3')
C0 = Matrix([[0, 0, c_CO2, c_HCO3, 0]])
N = Matrix([
    [1, 1, 0, 0, 0],
    [1, 0, -1, 1, 0],
    [1, 0, 0, -1, 1],
])
X = Matrix([[x0, x1, x2]])
C = C0 + X*N
eqs = [
    C[0, 0]*C[0, 1] - k_H2O,
    C[0, 0]*C[0, 3] - k_CO2*C[0, 2],
    C[0, 0]*C[0, 4] - k_HCO3*C[0, 3],
]
subs = {c_CO2: 0.001, c_HCO3: 0.01, k_H2O: 1e-14, k_CO2: 4.3e-7, k_HCO3: 4.8e-11}

# TODO: NH4.CH3COO, NH4.HCO3, H3PO4, H3PO4 + Citrate

def main():
    B = groebner(eqs, x2, x1, x0)
    print(B, len(B))
    x00 = solve(B[2].subs(subs))[3]
    print('x0 =', x00)
    x10 = solve(B[1].subs(subs).subs(x0, x00))[0]
    print('x1 =', x10)
    x20 = solve(B[0].subs(subs).subs({x0: x00, x1: x10}))[0]
    print('x2 =', x20)
    print(C.subs(subs).subs({x0: x00, x1: x10, x2: x20}))

if __name__ == '__main__':
    main()