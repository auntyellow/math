from sympy import *

# https://math.stackexchange.com/q/4191759
# https://chemistry.stackexchange.com/q/153869

x0, x1, x2, x3, x4, x5, x6 = symbols('x0, x1, x2, x3, x4, x5, x6') 

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
subs = {
    c_NH3: nsimplify(0.1),
    k_H2O: nsimplify(1e-14),
    k_NH3: nsimplify(1.77e-5),
}

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
subs = {
    c_SO4: nsimplify(0.5),
    k_H2O: nsimplify(1e-14),
    k_HSO4: nsimplify(1e-2),
}

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
subs = {
    c_CO2: nsimplify(0.001),
    c_HCO3: nsimplify(0.01),
    k_H2O: nsimplify(1e-14),
    k_CO2: nsimplify(4.3e-7),
    k_HCO3: nsimplify(4.8e-11),
}

# H2O <-> H+ + OH-
# CH3COOH <-> H+ + CH3COO-
# NH3 + H2O <-> NH4+ + OH-
# [H+, OH-, CH3COOH, CH3COO-, NH3, NH4+]
# 0.1M CH3COONH4
c_CH3COONH4, k_H2O, k_CH3COOH, k_NH3 = symbols('c_CH3COONH4, k_H2O, k_CH3COOH, k_NH3')
C0 = Matrix([[0, 0, c_CH3COONH4, 0, c_CH3COONH4, 0]])
# equivalent to
# C0 = Matrix([[0, 0, 0, c_CH3COONH4, 0, c_CH3COONH4]])
# + 0.01M H+
# C0 = Matrix([[c_H, 0, c_CH3COONH4, 0, c_CH3COONH4, 0]])
N = Matrix([
    [1, 1, 0, 0, 0, 0],
    [1, 0, -1, 1, 0, 0],
    [0, 1, 0, 0, -1, 1],
])
X = Matrix([[x0, x1, x2]])
C = C0 + X*N
eqs = [
    C[0, 0]*C[0, 1] - k_H2O,
    C[0, 0]*C[0, 3] - k_CH3COOH*C[0, 2],
    C[0, 1]*C[0, 5] - k_NH3*C[0, 4],
]
subs = {
    c_CH3COONH4: nsimplify(0.1),
    k_H2O: nsimplify(1e-14),
    k_CH3COOH: nsimplify(1.75e-5),
    k_NH3: nsimplify(1.77e-5),
}

# H2O <-> H+ + OH-
# NH3 + H2O <-> NH4+ + OH-
# CO2 + H2O <-> H+ + HCO3-
# HCO3- <-> H+ + CO32-
# [H+, OH-, NH3, NH4+, CO2, HCO3-, CO32-]
# 0.1M NH4HCO3
c_NH4HCO3, k_H2O, k_NH3, k_CO2, k_HCO3 = symbols('c_NH4HCO3, k_H2O, k_NH3, k_CO2, k_HCO3')
C0 = Matrix([[0, 0, 0, c_NH4HCO3, 0, c_NH4HCO3, 0]])
N = Matrix([
    [1, 1, 0, 0, 0, 0, 0],
    [0, 1, -1, 1, 0, 0, 0],
    [1, 0, 0, 0, -1, 1, 0],
    [1, 0, 0, 0, 0, -1, 1],
])
X = Matrix([[x0, x1, x2, x3]])
C = C0 + X*N
eqs = [
    C[0, 0]*C[0, 1] - k_H2O,
    C[0, 1]*C[0, 3] - k_NH3*C[0, 2],
    C[0, 0]*C[0, 5] - k_CO2*C[0, 4],
    C[0, 0]*C[0, 6] - k_HCO3*C[0, 5],
]
subs = {
    c_NH4HCO3: nsimplify(0.1),
    k_H2O: nsimplify(1e-14),
    k_NH3: nsimplify(1.77e-5),
    k_CO2: nsimplify(4.3e-7),
    k_HCO3: nsimplify(4.8e-11),
}

# H2O <-> H+ + OH-
# H3PO4 <-> H+ + H2PO4-
# H2PO4- <-> H+ + HPO42-
# HPO42- <-> H+ + PO43-
# [H+, OH-, H3PO4, H2PO4-, HPO42-, PO43-]
# 0.1M H2PO4-
c_H2PO4, k_H2O, k_H3PO4, k_H2PO4, k_HPO4 = symbols('c_H2PO4, k_H2O, k_H3PO4, k_H2PO4, k_HPO4')
C0 = Matrix([[0, 0, 0, c_H2PO4, 0, 0]])
N = Matrix([
    [1, 1, 0, 0, 0, 0],
    [1, 0, -1, 1, 0, 0],
    [1, 0, 0, -1, 1, 0],
    [1, 0, 0, 0, -1, 1],
])
X = Matrix([[x0, x1, x2, x3]])
C = C0 + X*N
eqs = [
    C[0, 0]*C[0, 1] - k_H2O,
    C[0, 0]*C[0, 3] - k_H3PO4*C[0, 2],
    C[0, 0]*C[0, 4] - k_H2PO4*C[0, 3],
    C[0, 0]*C[0, 5] - k_HPO4*C[0, 4],
]
subs = {
    c_H2PO4: nsimplify(0.1),
    k_H2O: nsimplify(1e-14),
    k_H3PO4: nsimplify(7.11e-3),
    k_H2PO4: nsimplify(6.32e-8),
    k_HPO4: nsimplify(4.49e-13),
}

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
c_HPO4, c_H3Citrate, k_H2O, k_H3PO4, k_H2PO4, k_HPO4, k_H3Citrate, k_H2Citrate, k_HCitrate = symbols('c_HPO4, c_H3Citrate, k_H2O, k_H3PO4, k_H2PO4, k_HPO4, k_H3Citrate, k_H2Citrate, k_HCitrate')
C0 = Matrix([[0, 0, 0, 0, c_HPO4, 0, c_H3Citrate, 0, 0, 0]])
N = Matrix([
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, -1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, -1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, -1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, -1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, -1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, -1, 1],
])
X = Matrix([[x0, x1, x2, x3, x4, x5, x6]])
C = C0 + X*N
eqs = [
    C[0, 0]*C[0, 1] - k_H2O,
    C[0, 0]*C[0, 3] - k_H3PO4*C[0, 2],
    C[0, 0]*C[0, 4] - k_H2PO4*C[0, 3],
    C[0, 0]*C[0, 5] - k_HPO4*C[0, 4],
    C[0, 0]*C[0, 7] - k_H3Citrate*C[0, 6],
    C[0, 0]*C[0, 8] - k_H2Citrate*C[0, 7],
    C[0, 0]*C[0, 9] - k_HCitrate*C[0, 8],
]
subs = {
    c_HPO4: nsimplify(0.04),
    c_H3Citrate: nsimplify(0.08),
    k_H2O: nsimplify(1e-14),
    k_H3PO4: nsimplify(7.11e-3),
    k_H2PO4: nsimplify(6.32e-8),
    k_HPO4: nsimplify(4.49e-13),
    k_H3Citrate: nsimplify(7.41e-4),
    k_H2Citrate: nsimplify(1.74e-5),
    k_HCitrate: nsimplify(4.0e-7),
}

def convert(arr, convert_def):
    arr_ret = []
    for e in arr:
        arr_ret.append(convert_def(e))
    return arr_ret

def to_decimal(arr):
    return convert(arr, lambda x: x.n())

def main():
    B = groebner(convert(eqs, lambda x: x.subs(subs)), x0, x1, x2, x3, x4, x5, x6)
    print(B, len(B))
    x60 = to_decimal(solve(B[6]))
    print('x6 =', x60)
    x60 = x60[3]
    print('x6 =', x60)
    x50 = to_decimal(solve(B[5].subs(x6, x60)))[0]
    print('x5 =', x50)
    x40 = to_decimal(solve(B[4].subs({x5: x50, x6: x60})))[0]
    print('x4 =', x40)
    x30 = to_decimal(solve(B[3].subs({x4: x40, x5: x50, x6: x60})))[0]
    print('x3 =', x30)
    x20 = to_decimal(solve(B[2].subs({x3: x30, x4: x40, x5: x50, x6: x60})))[0]
    print('x2 =', x20)
    x10 = to_decimal(solve(B[1].subs({x2: x20, x3: x30, x4: x40, x5: x50, x6: x60})))[0]
    print('x1 =', x10)
    x00 = to_decimal(solve(B[0].subs({x1: x10, x2: x20, x3: x30, x4: x40, x5: x50, x6: x60})))[0]
    print('x0 =', x00)
    print(C.subs(subs).subs({x0: x00, x1: x10, x2: x20, x3: x30, x4: x40, x5: x50, x6: x60}))

if __name__ == '__main__':
    main()