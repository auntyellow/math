from sympy import factor
from cartesian import *

def main():
    # https://math.stackexchange.com/questions/2391840
    # 0 < ∠ABC = 2β < π/2, 0 < ∠ACB = 2γ < π/2
    # ∠DBC = β + δ, ∠DBA = β - δ, ∠ECB = γ + δ, ∠EBA = γ - δ, |δ| < min(β,γ)
    # ∠DBC + ∠ECA = ∠DBA + ∠ECB = β + γ, BD = CE, prove β = γ
    # 0 < b = tan β < 1, 0 < c = tan γ < 1, d = tan δ, |d| < min(b,c)
    # If δ = 0, it's Steiner-Lehmus theorem 
    a, b, c = symbols('a, b, c', positive = True)
    d, x, y = symbols('d, x, y')
    tan_2b = 2*b/(1 - b**2)
    tan_2c = 2*c/(1 - c**2)
    tan_bd = (b + d)/(1 - b*d)
    tan_cd = (c + d)/(1 - c*d) 
    A, B, C = (0, a), (-a/tan_2b, 0), (a/tan_2c, 0)
    AB, AC, BD, CE = line(A, B), line(A, C), Eq(y, tan_bd*(x - B[0])), Eq(y, -tan_cd*(x - C[0]))
    D, E = intersect(BD, AC), intersect(CE, AB)
    print('D:', D)
    print('E:', E)
    print('BD**2 - CE**2 =', factor(dist2(B, D) - dist2(C, E)))
    # should prove this factor is always negative:
    p = b**5*c**4 + 2*b**5*c**3*d + b**5*c**2*d**2 + b**4*c**5 + 6*b**4*c**4*d + 5*b**4*c**3*d**2 - 4*b**4*c**3 - 4*b**4*c**2*d + 2*b**3*c**5*d + 5*b**3*c**4*d**2 - 4*b**3*c**4 - 14*b**3*c**3*d - 5*b**3*c**2*d**2 + 5*b**3*c**2 + 4*b**3*c*d - b**3 + b**2*c**5*d**2 - 4*b**2*c**4*d - 5*b**2*c**3*d**2 + 5*b**2*c**3 + 14*b**2*c**2*d + 4*b**2*c*d**2 - 5*b**2*c - 2*b**2*d + 4*b*c**3*d + 4*b*c**2*d**2 - 5*b*c**2 - 6*b*c*d - b*d**2 - c**3 - 2*c**2*d - c*d**2
    # https://math.stackexchange.com/a/4313860
    r, s, t = symbols('r, s, t', positive = True)
    q = p.subs(d, c*(1 - r)/(1 + r)).subs(c, s/(1 + s)).subs(b, (s + t)/(1 + s + t))
    print(p, '=', factor(q))

if __name__ == '__main__':
    main()