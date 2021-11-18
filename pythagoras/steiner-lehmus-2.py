from sympy import factor
from cartesian import *

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2

def main():
    # https://math.stackexchange.com/questions/2391840
    # 0 < ∠CAB = 2α < π/2, 0 < ∠CBA = 2β < π/2
    # ∠DAB = α + δ, ∠DAC = α - δ, ∠EBA = β + δ, ∠EBC = β - δ, |δ| < min(α,β)
    # ∠DAB + ∠EBC = ∠DAC + ∠EBA = α + β, AD = AE, prove α = β
    # 0 < a = tan α < 1, 0 < b = tan β < 1, d = tan δ, |d| < min(a,b)
    # If δ = 0, it's Steiner-Lehmus theorem 
    a, b, c = symbols('a, b, c', positive = True)
    d, x, y = symbols('d, x, y')
    tan_2a = 2*a/(1 - a**2)
    tan_2b = 2*b/(1 - b**2)
    tan_ad = (a + d)/(1 - a*d)
    tan_bd = (b + d)/(1 - b*d) 
    A, B, C = (-c/tan_2a, 0), (c/tan_2b, 0), (0, c)
    AC, BC, AD, BE = line(A, C), line(B, C), Eq(y, tan_ad*(x - A[0])), Eq(y, -tan_bd*(x - B[0]))
    D, E = intersect(AD, BC), intersect(BE, AC)
    print('D:', D)
    print('E:', E)
    print('AD**2 - BE**2 =', factor(dist2(A, D) - dist2(B, E)))
    # should prove this factor is always negative:
    p = a**5*b**4 - 2*a**5*b**3*d + a**5*b**2*d**2 + a**4*b**5 - 6*a**4*b**4*d + 5*a**4*b**3*d**2 - 4*a**4*b**3 + 4*a**4*b**2*d - 2*a**3*b**5*d + 5*a**3*b**4*d**2 - 4*a**3*b**4 + 14*a**3*b**3*d - 5*a**3*b**2*d**2 + 5*a**3*b**2 - 4*a**3*b*d - a**3 + a**2*b**5*d**2 + 4*a**2*b**4*d - 5*a**2*b**3*d**2 + 5*a**2*b**3 - 14*a**2*b**2*d + 4*a**2*b*d**2 - 5*a**2*b + 2*a**2*d - 4*a*b**3*d + 4*a*b**2*d**2 - 5*a*b**2 + 6*a*b*d - a*d**2 - b**3 + 2*b**2*d - b*d**2

if __name__ == '__main__':
    main()