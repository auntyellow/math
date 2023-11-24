from itertools import permutations
from sympy import *

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

# successive difference substitution
# return [negative_when], [[zero_when]], max_depth
def sds(f, vars):
    deg = Poly(f).homogeneous_order()
    if deg == None:
        raise Exception(f'{f} is not homogeneous')
    max_depth = 0
    for vars_permutation in permutations(vars):
        # TODO check if permutation is necessary
        negative_when, positive_when, depth = sds0(f, vars_permutation, deg, False, 0)
        max_depth = max(max_depth, depth)
        if negative_when != None:
            return negative_when, None, max_depth
        # TODO add positive_when
    return None, None, max_depth

def sds0(f, vars, deg, permute, depth):
    vars_len = len(vars)
    if permute:
        vars_permutations = permutations(vars)
    else:
        vars_permutations = [vars]
    max_depth = depth
    for vars_permutation in vars_permutations:
        f1 = f
        x = vars_permutation[0]
        for i in range(1, vars_len):
            y = vars_permutation[i]
            # much faster than f1 = f1.subs(...) ... expand(...)
            f1 = expand(f1.subs(x, x + y))
            x = y
        p = Poly(f1, vars)
        neg = False
        for coeff in p.coeffs():
            if coeff < 0:
                neg = True
                break
        # TODO add zero_when
        # for term in p.terms():
        #     for exp in term[0]:
        if not neg:
            continue
        # there is negative term
        # if a*x**deg < 0: the polynomial is negative
        for x in vars_permutation:
            if p.coeff_monomial(x**deg) < 0:
                # TODO set negative_when
                return True, None, max_depth
        # else: recursive
        negative_when, positive_when, depth0 = sds0(f1, vars, deg, True, depth + 1)
        max_depth = max(max_depth, depth0)
        if negative_when != None:
            return negative_when, None, max_depth
        # TODO add positive_when
    return None, None, max_depth

def main():
    x, y, z = symbols('x, y, z', negative = False)
    print(sds(x**2 - 3*x*y + y**2, [x, y]))

    # ISBN 9787030207210, p169, §7.3.2, problem 5
    a1, a2, a3, a4, a5, a6 = symbols('a1, a2, a3, a4, a5, a6', negative = False)
    f = a1/(a2 + a3) + a2/(a3 + a4) + a3/(a4 + a5) + a4/(a5 + a1) + a5/(a1 + a2) - S(5)/2
    f = fraction(cancel(f))[0]
    # depth = 0
    # print(sds(f, [a1, a2, a3, a4, a5]))

    # p170, §7.3.3
    f = a1/(a2 + a3) + a2/(a3 + a4) + a3/(a4 + a1) + a4/(a1 + a2) - 2
    f = fraction(cancel(f))[0]
    # depth = 1
    # print(sds(f, [a1, a2, a3, a4]))

    # p171, problem 8
    f = x**4*y**2 - 2*x**4*y*z + x**4*z**2 + 3*x**3*y**2*z - 2*x**3*y*z**2 - 2*x**2*y**4 - 2*x**2*y**3*z + x**2*y**2*z**2 + 2*x*y**4*z + y**6
    # depth = 4

    # p171, problem 9
    f = 8*x**7 + (8*z + 6*y)*x**6 + 2*y*(31*y - 77*z)*x**5 - y*(69*y**2 - 2*z**2 - 202*y*z)*x**4 \
        + 2*y*(9*y**3 + 57*y*z**2 - 85*y**2*z + 9*z**3)*x**3 + 2*y**2*z*(-13*z**2 - 62*y*z + 27*y**2)*x**2 \
        + 2*y**3*z**2*(-11*z + 27*y)*x + y**3*z**3*(z + 18*y)
    # depth = 17
    # print(sds(f, [x, y, z]))

    # p172, problem 10
    a, b, c = symbols('a, b, c', negative = False)
    f = a*(a + b)**5 + b*(c + b)**5 + c*(a + c)**5
    # depth = 3
    # print(sds(f.subs(c, -c), [a, b, c]))
    # depth = 3
    # print(sds(f.subs(c, -c).subs(b, -b), [a, b, c]))

    # p172, problem 11
    f = 2572755344*x**4 - 20000000*x**3*y - 6426888360*x**3*z + 30000000*x**2*y**2 \
        + 5315682897*x**2*z**2 - 20000000*x*y**3 - 1621722090*x*z**3 + 170172209*y**4 \
        - 1301377672*y**3*z + 3553788598*y**2*z**2 - 3864133016*y*z**3 \
        + 1611722090*z**4
    # depth = 45
    # print(sds(f, [x, y, z]))

    # p174, 6-var Vasc's conjuction
    # see also: https://math.stackexchange.com/a/4693459
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + \
        (a4 - a5)/(a5 + a6) + (a5 - a6)/(a6 + a1) + (a6 - a1)/(a1 + a2)
    f = fraction(cancel(f))[0]
    # depth = 1
    print(sds(f, [a1, a2, a3, a4, a5, a6]))

    # https://math.stackexchange.com/a/2120874
    # https://math.stackexchange.com/q/1775572
    f = sum_cyc(x**4/(8*x**3 + 5*y**3), (x, y, z)) - (x + y + z)/13
    # depth = 1
    # https://math.stackexchange.com/q/1777075
    f = sum_cyc(x**3/(13*x**2 + 5*y**2), (x, y, z)) - (x + y + z)/18
    # depth = 4
    # This is not always non-negative:
    f = sum_cyc(x**3/(8*x**2 + 3*y**2), (x, y, z)) - (x + y + z)/11
    # https://math.stackexchange.com/q/3526427
    f = 3 - sum_cyc((x + y)**2*x**2/(x**2 + y**2)**2, (x, y, z))
    # depth = 1
    # https://math.stackexchange.com/q/3757790
    f = sum_cyc((y + z)/x, (x, y, z)) + 1728*x**3*y**3*z**3/((x + y)**2*(y + z)**2*(z + x)**2*(x + y + z)**3) - 4*sum_cyc(x/(y + z), (x, y, z)) - 1
    # depth = 1
    f = fraction(cancel(f))[0]
    print(sds(f, [x, y, z]))

if __name__ == '__main__':
    main()