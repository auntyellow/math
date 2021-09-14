from sympy import *

# https://en.wikipedia.org/wiki/Heron%27s_formula
a, b, c = symbols('a, b, c')
s = (a + b + c) / 2
A1 = sqrt(s * (s - a) * (s - b) * (s - c))
C = acos((a * a + b * b - c * c) / 2 / a / b)
A2 = a * b * sin(C) / 2
print(expand(A1 * A1))
print(expand(A2 * A2))