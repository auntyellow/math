from math import *

DEGREE = pi / 180

def S(degree):
    return sin(degree * DEGREE)

def C(degree):
    return cos(degree * DEGREE)

# https://en.wikipedia.org/wiki/Langley%27s_Adventitious_Angles
# ABC is an isosceles triangle, ∠B=∠C=80◦, CF at 30◦ to AC cuts AB in F, BE at 20◦ to AB cuts AC in E, solve ∠BEF.
BC = 1
AB = AC = BC * S(80) / S(20)
BE = AB * S(20) / S(140)
CF = AC * S(20) / S(130)
BF = CF * S(50) / S(80)
CE = BE * S(60) / S(80)
AE, AF = AC - CE, AB - BF
EF = sqrt(AE * AE + AF * AF - 2 * AE * AF * C(20))
BEF = asin(BF * S(20) / EF)
print('BEF =', BEF / DEGREE, 'degree')